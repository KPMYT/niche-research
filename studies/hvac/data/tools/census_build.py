#!/usr/bin/env python3
"""Round 3 census build (HVAC study), written 2026-10-26 by the round 3 census-build helper.

Rerunnable. Reads only local files; no network, no web searches.

Inputs (all under studies/hvac/data/raw/):
  census-2026-10-26/<channelId>.json   Videos tab of every tier A-D channel, logged out, pulled 2026-10-26
                                       by census_pull.py -> yt_allsorts.py (Latest, Popular, Oldest; up to ~120 each).
  channels-master-2026-10-24.csv       round 2 master list (old tier, subs, total views, joined, country, NexLev outlier, type).
  About panels (description text, for the D check): channels-master-about-2026-10-24.json,
      channel-finds-pages-2026-10-23/about.json, round2-nexlev-pages-2026-10-24/about.json,
      round2-oldheat-2026-10-24.json (channel_about), check-master-2026-10-24.json (about).
  check-master-2026-10-24.json         round 2 checker's thumbnail type for 86 channels (carried forward as "type").
  census-handcheck-2026-10-26.csv      (optional) the hand-check of 40 random channels; agreement is computed if present.

Outputs:
  raw/census-channels-2026-10-26.csv   one row per pulled channel (all new tiers, X included)
  raw/census-videos-2026-10-26.csv     every long-form (>= 5:00) video of every channel
  raw/census-build-2026-10-26.json     counts, tier moves, word lists, the hand-check sample and agreement
  ../channels.md, ../channels.csv      deliverable 1 (in progress): tiers A-D

Usage: python3 -I census_build.py            (build everything)
       python3 -I census_build.py sample     (print the seed-2610 hand-check sample with titles)

Everything rule-based here (HVAC title marks, lane words, tiers, sub-niches) is a READING by keyword rule, not a
measurement. Views are the Videos tab's ROUNDED text (e.g. "24K"), so multiples are approximate; exact counts come
later for the top 100 and the winners. Upload dates are APPROXIMATE, from the tab's age text ("3mo ago").
"""
import csv, glob, json, os, random, re, statistics, sys
from collections import Counter, OrderedDict
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(os.path.dirname(HERE), "raw")
STUDY = os.path.dirname(os.path.dirname(HERE))
CENSUS_DIR = os.path.join(RAW, "census-2026-10-26")
PULL_DATE = date(2026, 10, 26)
NEW_SINCE = date(2025, 10, 26)
sys.path.insert(0, HERE)
from autocomplete import is_hvac as _is_hvac_r2, norm, EXCLUDE as R2_EXCLUDE  # noqa: E402

# ---------------------------------------------------------------------------------------------------------------
# 1. HVAC title rule = autocomplete.is_hvac (round 2) + census fixes. Calibrated against the round 2 checker's
#    hand marks (check-master-2026-10-24.json, 2,893 titles): see census-build-2026-10-26.json "hvac_rule_calibration".
#    Scope as check-master.md step 3: counted = AC, heat pumps, furnaces, boilers, radiators, thermostats, filters,
#    ducts, parts, refrigerant, humidity / indoor air, bath and attic fans, insulation and drafts about heat / cooling /
#    the bill, the energy bill, wood / pellet / diesel / space heaters, "free heat / cooling", warmth in an outage.
#    Not counted: water heaters, frozen pipes, generator / power-station reviews, car AC, PC cooling, ceiling-fan
#    wiring and remotes, patio heaters, grills.
# ---------------------------------------------------------------------------------------------------------------
# (a) tokens stripped before the round 2 rule runs, because its EXCLUDE list (built for a US keyword sweep) drops
#     real HVAC titles on them in a channel census: UK / Ireland / Australia (English-speaking channels), "combi"
#     (UK boilers), "unboxing", "walkthrough", "vlog", "app" (thermostat / mini-split apps), "math" ("I did the math"),
#     "vacuum switch / pump" (pellet stoves, refrigeration), "tankless coil" (boilers), "diverter" (boilers),
#     "1-9 hours" (install times; 10-hour sleep sounds stay excluded), "GTA" when it is the Toronto area,
#     "Panasonic" (its "sonic" hit a game word), "square feet" ("feet" hit a body word), "engineer(s)" ("engine").
STRIP = re.compile(r"\buk\b|\bireland\b|\baustralia\b|\bcombi\b|\bunboxing\b|\bwalkthrough\b|\bvlog\b|\bapp\b|"
                   r"\bmath\b|\bvacuum (switch|pump|test)\w*|\bash vacuum\b|\btankless coil\b|\bdiverter\b|"
                   r"\b[1-9] ?hours?\b|\bpanasonic\b|\bsquare (feet|foot)\b|\bsq\.? ?ft\b|\bengineers?\b")
GTA_CANADA = re.compile(r"toronto|ontario|vaughan|etobicoke|canada|homeowners|enbridge|mississauga|brampton")
# (b) census excludes (checked first): clear non-HVAC uses of HVAC-looking words seen in the census titles.
CENSUS_EXCLUDE = re.compile(
    r"\b3d print|\bprinter\b|\bbbq\b|barbecue|soda can stove|alcohol stove|camp(ing)? stove|golf cart|\bac motor\b|"
    r"\bac (current|voltage|adapter|plug|cord|charger|circuit|outlet|power supply)\b|current meter|\bsmd\b|"
    r"garage door|\bwater bill|hot water|water filter|water system|running water|well pump|root cellar|springhouse|"
    r"smokehouse|cold pantry|\bkeeps? (food|milk)|food (fresh|from)|\beating\b|hot chocolate|macbook|neck fan|"
    r"industrial fan|dry iron|steam iron|flat iron|washer|washing machine|\bpool\b|freightliner|cascadia|kenworth|"
    r"peterbilt|semi truck|trimmer|weed eater|duct tape|can lights?|recessed light|cooktop|stove ?top|gas stove|"
    r"electric stove|stove burner|wood stove ashes|\bashes\b|work gloves|sports fan|\bcomputer\b|thermal (camera|imag)|"
    r"thermal master|immersion heater|megaflo|\bgmc\b|\bs10\b|blazer|pontiac|buick|cadillac|chrysler|lexus|mazda|"
    r"volvo|\baudi\b|volkswagen|\bvw\b|porsche|acura|infiniti|automotive|\bdance\b|bhojpuri|golden knight|graveyard|"
    r"\bdeck is\b|air compressor|\btire\b|\btyre\b|inflator|nail gun|pancake compressor|\bmini fridge|patio heater|"
    r"pellet grill|heated (vest|jacket|gloves|socks|blanket)|hand warmer|\bsous vide|"
    r"winteriz\w* (your |the )?(plumbing|pipes)|\bpipes?\b.{0,30}freez|freez\w* pipes?|\bgrill(ing|s)?\b|"
    r"\bgarden (wood )?stoves?\b|\boutdoor (wood )?stoves?\b|stoves? for cooking|\bcook ?stoves?\b|\boven\b|"
    r"\brice\b|\bbaking\b")
# (c) words a title may lean on that only count when the title is about warmth / cooling / the bill (operator rules:
#     generators only for keeping the house warm; drafts, windows, insulation only about heat, cooling or the bill).
DEPENDENT = re.compile(r"\bwindows?\b|\bgenerators?\b|power station|powerwall|solar generator|whole[- ]home backup|"
                       r"backup (power|system)|power outage|without power|no power\b|without electricity|"
                       r"no electricity|\bblackout\b|\bgrid\b|\bmold\b|\bmould\b|\binsulat\w*|\bfans?\b|"
                       r"rocket stoves?|\bpower (goes|went) out\b|\bcondensation\b")
WARMTH = re.compile(r"\bwarm\w*|\bheat\w*|\bcold\w*|\bwinter\w*|\bfreez\w*|\bfrost|\bcool\w*|\bhot\b|\bhotter\b|"
                    r"\bchill|draft|draught|\benergy\b|\bbills?\b|temperature|°f|degrees|\bfurnace|\bac\b|\ba/c\b|"
                    r"air condition|humid|dehumid|\bstove|\bfirewood|\bblanket|\bsnow|\bice storm|\bsummer|heatwave|"
                    r"thermal curtain|\battic\b|\bhvac\b|ventilat|\bair quality|\bduct|\bvent\b|\bthermostat")
# (d) census additions (clear misses of the round 2 rule).
CENSUS_STRONG = re.compile(
    r"\bboilers?\b|\bradiators?\b|\bchillers?\b|\baquastat|\boil[- ]?fired\b|\bbeckett\b|\briello\b|"
    r"\bburner (nozzle|motor|electrode)|\bcompressor\b|magnetic cooling|\brefrigeration\b|\bepa ?608\b|"
    r"\bheat (goes|went) out\b|\bfurnace (goes|went) out\b|\bfirst (hard )?freeze\b|\bpower (goes|went|is) out\b|"
    r"\b(lose|losing|lost) power\b|\bgrid (fails|failure|goes down|down|collapse)|\bgrid-down\b|"
    r"\b(your|my|the|an?|old|new|home|house|window|central|portable|solar|wall|bedroom) a/?c\b|"
    r"\ba/?c\b (sounds?|last|lasts|unit|runs?|running|blow|blows|blowing|not|won'?t|isn'?t|keeps?|line|drain|"
    r"filter|tune|repair|service|mistakes?|tips?|hacks?|secrets?|brands?|system|leak|freez|cool|down|off|on|"
    r"units|trick|tricks|problems?|noise|smell|bill|cost|install\w*)\b|"
    r"\bphantom (power|load)|\benergy monitor|\bflue\b|\bpellet (stove|insert|stoves|inserts)\b|\bwood pellets\b|"
    r"\bcombustion blower|\bburn pot|\bhumid\b|\bupstairs\b.{0,25}\b(hot|hotter|warm|cold|colder)\b|"
    r"hotter than downstairs|\bseal(ing)?\b.{0,40}\bbefore winter|\bwinteriz\w* (your |the |an? )?(old )?(home|house)|"
    r"\bdraughts?\b|\bashp\b|\bair[- ]source\b|\bground[- ]source\b|\bcarrier\b(?!.{0,20}(aircraft|phone|cell|wireless|pigeon))|"
    r"\btrane\b|\blennox\b|\bdaikin\b|\bmitsubishi (electric|mini|hyper|heat|ac)|\bfujitsu\b|\bmr ?cool\b|\bruud\b|"
    r"\brheem\b|\bamana\b|\bgoodman (ac|furnace|heat|unit|hvac|air)|\bvaillant\b|\bremeha\b|\bworcester\b|\bbaxi\b|"
    r"\bviessmann\b|\bglow-?worm\b|\bideal logic\b|\batag\b|\btado\b|\bevohome\b|\bharman (p\d|accentra|pellet|stove)|"
    r"\benglander\b|\bcomfortbilt\b|\bpelpro\b|\bclimatemaster\b|\bgeoexchange\b|\betherea\b|\bemura\b|"
    r"\bindoor head\b|\buv (light|technology|lamp)|\bclean(s|ing)? (the )?air\b|\boctopus (agile|cosy|go|energy)|"
    r"\bprice cap\b|\bbuy an a/?c\b|\b(air|copper|diy|bucket|homemade|ice|room|evaporative) coolers?\b|"
    r"\bearth tubes?\b|\bcools? (your|the|my|any|a|every) (attic|roof|house|home|room|bedroom|garage|space)|"
    r"\bkeep(s|ing)? (your |the |my |a )?(whole )?(house|home|room|bedroom|attic|garage|bed) "
    r"(cool|warm|cooler|warmer)|\bstay(s|ing)? (warm|cool)\b|\btoo (hot|cold) to sleep\b|"
    r"\bwinter (survival|tricks?|hacks?)\b|\bfirewood\b|\bpassive ?house\b|\bpassivhaus\b|\bforced[- ]air\b|"
    r"\bradiant (heat|floor|vs)|\bmanual j\b|\bload calc|\bbuilding envelope\b|\bsolar a/?c\b|"
    r"\b(cuts?|lower|lowers|slash|slashes|halve|reduce|reduces|cut) (your|my|the) (\w+ )?bills?\b|\bheat loss\b|"
    r"\bheating (season|costs?)\b|\bblower door\b|\benergy audits?\b|\bair[- ]?seal\w*|\bhome performance\b|"
    r"\b(house|home|garage|room|bedroom|upstairs|attic|basement)\b.{0,30}\b\d+ ?(°|degrees?) ?f?\b|"
    r"\b\d+ ?(°|degrees?) ?f?\b.{0,30}\b(house|home|garage|room|bedroom|upstairs|attic|basement)\b|\bcooling (costs?|load)\b|\bdiesel heaters?\b|\bheat (a|your|the|my) "
    r"(home|house|room|garage|shop|bedroom|cabin|greenhouse)\b")


# Bath, exhaust, attic and whole-house fans count (check-master.md step 3 scope); checked before the fan rule.
VENT_FANS = re.compile(r"\b(bath(room)?|exhaust|attic|whole[- ]house|roof|ventilation|inline) (exhaust )?fans?\b|"
                       r"\bwhisper ?(fit|green|value|ceiling)\b|\bbath fan\b")


def _r2(t):
    return _is_hvac_r2(t)


def hvac_title(title):
    """True when a title is HVAC by the census rule (a reading by keyword rule)."""
    t = norm(title or "")
    if CENSUS_EXCLUDE.search(t):
        return False
    c = STRIP.sub(" ", t)
    if re.search(r"\bgta\b", c) and GTA_CANADA.search(c):
        c = re.sub(r"\bgta\b", " ", c)
    if R2_EXCLUDE.search(c):
        return False
    if VENT_FANS.search(c):
        return True
    hit = _r2(c) or bool(CENSUS_STRONG.search(c))
    if not hit:
        return False
    if DEPENDENT.search(c):
        bare = DEPENDENT.sub(" ", c)
        if not (_r2(bare) or CENSUS_STRONG.search(bare) or WARMTH.search(bare)):
            return False
    return True


# ---------------------------------------------------------------------------------------------------------------
# 2. Adjacent-lane words: check-master.md step 4's list, grouped (plus three clear synonyms of "no power":
#    "without power", "without electricity", "power goes / went out"). "emergency heat" (a heat pump setting) is not
#    a lane word. Added after the 40-channel hand-check (2026-10-26), as clear misses: "waste oil" (off-grid heat, in
#    the master's C definition), grandma / grandpa / depression-era / old-fashioned / pioneer / WWII (old-ways),
#    "cost pennies" / "zero-cost" (frugal), and "N best" / "best ... 2026" product lists (not only "Top 5 Best"). Used for the C test (>= 30% of the latest 30 long-form titles) and the lane tags.
# ---------------------------------------------------------------------------------------------------------------
LANES = OrderedDict([
    ("off-grid", r"\boff[- ]?grid\b|\bhomestead\w*|\bfree heat\b|\bwood ?stoves?\b|\bpellets?\b|\bdiesel heaters?\b|\bwaste[- ]oil\b"),
    ("outage", r"\boutages?\b|\bblackouts?\b(?! curtain)|\bno power\b|\bwithout power\b|\bwithout electricity\b|"
               r"\bpower (goes|went) out\b|(?<!off[- ])(?<!off)\bgrid\b"),
    ("survival", r"\bpreppers?\b|\bprepping\b|\bsurvival\b|\bemergency\b(?! heat)|\bstockpil\w*|\bnasa\b"),
    ("solar", r"\bsolar\b|\bbatter(y|ies)\b|\bpower stations?\b"),
    ("generator", r"\bgenerators?\b"),
    ("old-ways", r"\bold[- ]timers?\b|\bamish\b|\bjapanese\b|\bancient\b|\bforgotten\b|\bgrand(ma|pa|mother|father|parents?)'?s?\b|"
                 r"\bdepression[- ]era\b|\bold[- ]fashioned\b|\bpioneers?\b|\bwwii\b"),
    ("frugal", r"\bfrugal\b|\bdollar tree\b|\bwalmart\b|\b(cost|for) pennies\b|\bzero[- ]cost\b"),
    ("energy", r"\bnet[- ]zero\b|\bcleantech\b"),
    ("product-lists", r"\b(top )?\d+ (best|worst)\b|\bbest\b.{1,60}\b20[23]\d\b"),
    # census addition (2026-10-26), a lane TAG only (not used in the C test): DIY stove-building and "free energy"
    # craft channels (cement / gas-cylinder / barrel stoves), which the HVAC rule counts as off-grid heat.
    ("diy-stove-craft", r"\bcement\b|\bfree energy\b|\bgas cylinders?\b|\b(build|built|make|made|making)\b.{0,40}"
                        r"\b(stoves?|heaters?)\b|\brocket stoves?\b|\bbarrel\b|\bcopper pipe\b"),
])
C_TEST_LANES = [k for k in LANES if k != "diy-stove-craft"]
LANES_RX = {k: re.compile(v) for k, v in LANES.items()}


def lane_words(title):
    t = norm(title or "")
    return [k for k, rx in LANES_RX.items() if rx.search(t)]


def lane_c_word(lanes):
    return any(l in C_TEST_LANES for l in lanes)


# Trade-facing title words (the D flag (b) of check-master.md step 1; a flag only, confirmed by reading).
TRADE = re.compile(r"\btechs\b|\b(hvac|hvacr|service|ac|a/c|refrigeration|maintenance) tech\b|\btechnicians?\b(?! (tell|told|know|don'?t|won'?t|hate|say|reveal|secret))|"
                   r"\bfor (hvac )?(pros|contractors|installers)\b|\binstallers?'? guide|\btraining\b|\bepa ?60[89]\b|"
                   r"\bapprentices?\b|\bjourneym[ae]n\b|\bhvac (business|school|students?|careers?|license|apprentice)|"
                   r"\bgas engineers?\b|\bsuperheat\b|\bsubcool\w*|\bmanual j\b|\bload calc|\bvr[fv]\b|\bchillers?\b|"
                   r"\bcommercial\b|\brtus?\b|\brooftop units?\b|\bcallbacks?\b|\bride ?along\b|\bday in the life\b|"
                   r"\bservice (manager|techs?)\b|\b(sales|marketing) (for|tips|training)|\bbusiness owners?\b|"
                   r"\bfault codes?\b|\btrade school\b|\bfield ?piece\b|\bmanifold gauges?\b|\bnate\b|\bceu\b|"
                   r"\bwiring diagrams?\b|\bsequence of operation\b|\bpt chart\b")
# Homeowner "insider" framings that name the trade but address the homeowner (not trade-facing): removed first.
TRADE_HOMEOWNER = re.compile(r"\b\d+ ?% of (hvac |ac )?(techs?|technicians|installers|contractors|plumbers|pros)\b|"
                             r"\b(techs?|technicians|contractors|installers|pros|companies)\b (don'?t|won'?t|hate|never|hope|"
                             r"actually|secretly|wish|swear|refuse|tell|told|say|reveal|charge|install in|use in)\b")


def trade_title(title):
    return bool(TRADE.search(TRADE_HOMEOWNER.sub(" ", norm(title or ""))))


# Company words (D flag (a)): in the channel name, and company markers in the About text (confirmation).
NAME_COMPANY = re.compile(
    r"heating ?(&|and|n'?) ?(air|cooling)|air ?(&|and) ?heat|heating,? cooling|cooling ?(&|and) ?heating|"
    r"plumbing ?(&|and)|(&|and) plumbing|\bmechanical\b|\bservices?\b|\bsuppl(y|ies)\b|\bparts\b|\bstoves?\b|"
    r"\bfireplaces?\b|\bllc\b|\binc\b|\bltd\b|\blimited\b|\bcompany\b|\bco\b\.?$|\bcorp\b|\bcorporation\b|"
    r"\bdistribut|\bwholesale\b|\bdealers?\b|\bofficial\b|\bgroup\b|\bindustries\b|\bmanufactur|\bstore\b|"
    r"\bshop\b|\boutlet\b|\bdirect\b|\bdepot\b|\bwarehouse\b|\bsales\b|\bacademy\b|\binstitute\b|\bschool\b|"
    r"\btraining\b|\buniversity\b|\bcollege\b|\binsulation\b|\bwindows? (&|and) doors?\b|\bsolutions\b|\bpros?\b$|"
    r"\benergy\b|\bair conditioning\b|\bcomfort\b|\bhome services\b|\bhvacr?\b.*\b(inc|llc|co|services|company)\b")
ABOUT_COMPANY = re.compile(
    r"\bllc\b|\binc\b\.?|\bltd\b|\bcompany\b|\bcorporation\b|\bour (team|company|technicians|techs|showroom|store|"
    r"products?|customers|business|service area|crew|staff|employees|dealers?|brand|family business)\b|"
    r"\bfamily[- ](owned|operated|business)\b|\blocally owned\b|\bserving (the )?\w+|\bservice area\b|"
    r"\bcall (us|today|now)\b|\bschedule (a|an|your)\b|\blicensed\b|\bfree (estimate|quote|consultation)|"
    r"\bshowroom\b|\bdealers?\b|\bdistribut\w+|\bmanufactur\w+|\bwholesale\b|\bsupplier\b|\bretailer\b|"
    r"\bshop (now|online|our)\b|\border (online|now|today)\b|\bwe (sell|install|service|repair|offer|provide|"
    r"manufacture|carry|stock)\b|\bwe are (a|an|the) \w+|\bsince (19|20)\d\d\b|\(\d{3}\) ?\d{3}|\b\d{3}[-.]\d{3}[-.]\d{4}\b")
ABOUT_TRADE = re.compile(r"\btechnicians?\b|\btechs\b|\bapprentices?\b|\bstudents?\b|\btraining\b|\bcourses?\b|"
                         r"\bcontractors\b|\binstallers\b|\bfor (the )?trade\b|\bindustry\b|\bprofessionals?\b|"
                         r"\bhvac(r)? (pros|professionals|techs|business|industry|career)|\bcertification|\bepa\b|"
                         r"\bgas engineers?\b|\bengineers\b|\bacademy\b")
# Contractor (a company that serves local homeowners) vs brand / retailer / trade school.
CONTRACTOR = re.compile(r"heating ?(&|and|n'?) ?(air|cooling)|air ?(&|and) ?heat|cooling ?(&|and) ?heating|"
                        r"\bmechanical\b|\bserving\b|\bservice area\b|\blicensed\b|\bfree (estimate|quote)|"
                        r"\bcall (us|today|now)\b|\bschedule (a|an|your)\b|\bresidential\b|\bhomeowners in\b|"
                        r"\bcontractor\b|\bhome services\b|\bplumbing ?(&|and)|(&|and) plumbing|\bwe (install|service|repair)\b")
BRAND = re.compile(r"\bmanufactur\w+|\bdistribut\w+|\bwholesale\b|\bsupplier\b|\bretailer\b|\bshop (now|online|our)\b|"
                   r"\border (online|now|today)\b|\bour products?\b|\bwe (sell|manufacture|carry|stock)\b|\bstore\b|"
                   r"\bshowroom\b|\bdealers?\b|\bsuppl(y|ies)\b|\bparts\b|\bacademy\b|\binstitute\b|\bschool\b|"
                   r"\bcourses?\b|\btraining\b|\bofficial\b")

# ---------------------------------------------------------------------------------------------------------------
# 3. Sub-niches (labels.md section 4), one per HVAC title, first matching rule wins (a reading by keyword rule).
#    Order: outage and off-grid heat first, then brand verdicts, then the equipment named (labels.md: 'the equipment
#    or topic the title is about'), then parts, buying / replacing, airflow, air quality, envelope, heat types, bills.
# ---------------------------------------------------------------------------------------------------------------
SUBNICHE_RULES = [
    ("heat and power in an outage", r"outage|without power|no power\b|without electricity|no electricity|blackout|"
                                    r"power (goes|went|is) out|(lose|losing|lost) power|\bgrid\b|generator"),
    ("alternative and supplemental heat (off-grid heat)", r"wood ?stove|wood burning|pellet|diesel heater|"
                                    r"space heater|kerosene|propane heater|rocket (stove|heater|mass)|candle|"
                                    r"free heat|firewood|fireplace|earth tube|salt|terracotta|clay pot|"
                                    r"buddy heater|oil[- ]filled|infrared heater|electric heater|\bheaters?\b"),
    ("brand verdicts", r"\bbrands?\b|worth buying|to avoid|never buy|which (one|model) (to|should)|"
                       r"\b(best|worst) (ac|air conditioner|heat pump|furnace|mini[ -]?split|hvac|thermostat)s?\b"),
    ("AC: portable", r"portable (ac|a/c|air|heat pump)|ecoflow|battery[- ]powered (ac|air)|\bwave \d"),
    ("AC: window", r"window (ac|a/c|air conditioner|unit|units)|\bwindow-?mounted"),
    ("mini-split", r"mini[ -]?splits?|ductless|mr ?cool|\bsplit (ac|system|unit)"),
    ("heat pumps", r"heat ?pumps?|\bashp\b|air[- ]source|ground[- ]source|geothermal"),
    ("thermostats", r"thermostat|\bnest\b|ecobee|honeywell"),
    ("filters", r"\bfilters?\b|\bmerv\b"),
    ("parts homeowners touch", r"capacitor|contactor|disconnect|\bfuse|condensate pump|igniter|ignitor|"
                               r"flame sensor|blower motor|limit switch|pressure switch|inducer|control board|"
                               r"\brelay\b|transformer|\bmotor\b|thermocouple"),
    ("buying and replacing a system", r"\breplace(ment|ing)? (your |the |my |an? |old )?(whole |entire )?(ac|a/c|air conditioner|"
                                      r"furnace|hvac|system|heat pump|unit|boiler)s?\b(?! (capacitor|contactor|filter|motor|"
                                      r"fan|coil|board|thermostat|igniter|ignitor|part|sensor|switch|relay|valve))|"
                                      r"\bnew (ac|a/c|furnace|hvac|system|heat pump|unit|air conditioner)\b|\bquotes?\b|"
                                      r"\bsiz(e|ing)\b|repair or replace|how much (does|do|is|should)|\bcosts? (of|to)\b|"
                                      r"\bprices?\b|\bhire\b|\brebates?\b|financ|warranty|\bscams?\b|\bupsell|"
                                      r"\bcontractors?\b|\bsalesm[ae]n\b"),
    ("ducts and vents", r"\bducts?\b|ductwork|\bvents?\b|\bregisters?\b|return air|airflow|damper"),
    ("humidity, ventilation and indoor air", r"humid|dehumid|\bmold|\bmould|air quality|purifier|indoor air|"
                                             r"crawl ?space|exhaust fan|bath(room)? fan|\buv\b|carbon monoxide|"
                                             r"ventilat|condensation|\bclean(s|ing)? (the )?air|erv\b|hrv\b"),
    ("drafts, insulation and air sealing", r"insulat|draft|draught|weather ?strip|spray foam|caulk|window film|"
                                           r"air seal|\battic\b|curtain|\bwindows?\b|\bseal|passive ?house|"
                                           r"\broof\b|\bshade\b"),
    ("boilers and old-house heat", r"boiler|radiator|baseboard|\bsteam\b|hydronic|oil burner|oil[- ]fired|"
                                   r"zone valve|circulator|aquastat|radiant|beckett|\bflue\b|combi|"
                                   r"vaillant|remeha|worcester|baxi|viessmann"),
    ("furnaces", r"furnace|pilot light|forced[- ]air|\bburner\b|heat exchanger"),
    ("heating fuel and fuel choice", r"heating oil|\bpropane\b|natural gas|\bfuel\b|\boil vs|gas vs|vs gas|"
                                     r"\bgas or electric"),
    ("seasonal maintenance", r"maintenance|tune[- ]?up|before (winter|summer|you turn|the first)|checklist|"
                             r"\bspring\b|\bfall\b|\bclean(ing)? (your|the|an?) (ac|a/c|unit|condenser|coil)|"
                             r"\bwinteriz|first freeze|\bsummer\b|\bwinter\b"),
    ("energy bills", r"\bbills?\b|save (money|energy|on)|energy (costs?|efficien|saving|usage|use)|utility|"
                     r"\bkwh\b|cheaper to run|running costs?|electricity|price cap|octopus|phantom"),
    ("AC: central", r"\ba/?c\b|air condition|central air|condenser|\bcoils?\b|freon|refrigerant|compressor|"
                    r"\bcool\w*|drain line|r-?22|r-?410"),
]
SUBNICHE_RX = [(n, re.compile(p)) for n, p in SUBNICHE_RULES]
SUBNICHE_FALLBACK = "HVAC, not mapped (general heating / cooling)"


def subniche(title):
    t = norm(title or "")
    for n, rx in SUBNICHE_RX:
        if rx.search(t):
            return n
    return SUBNICHE_FALLBACK


# ---------------------------------------------------------------------------------------------------------------
# 4. Parsing helpers.
# ---------------------------------------------------------------------------------------------------------------
AGE_RX = re.compile(r"^(\d+)\s*(min|h|d|w|mo|y)\s+ago$")
UNIT_DAYS = {"min": 1 / 1440, "h": 1 / 24, "d": 1, "w": 7, "mo": 30.44, "y": 365.25}


def parse_dur(s):
    if not s or not re.match(r"^\d+(:\d+){1,2}$", s):
        return None
    sec = 0
    for p in s.split(":"):
        sec = sec * 60 + int(p)
    return sec


def age_of(meta):
    """(text, unit, n) from the tab meta (last part like '3mo ago'); None when no age (premieres)."""
    for p in reversed(meta or []):
        m = AGE_RX.match(p.replace("\xa0", " ").strip())
        if m:
            return p.replace("\xa0", " ").strip(), m.group(2), int(m.group(1))
    return None


def approx_date(unit, n):
    """Approximate upload date = pull date minus the MIDPOINT of the age text's range (n to n+1 units)."""
    days = (n + 0.5) * UNIT_DAYS[unit] if unit in ("d", "w", "mo", "y") else n * UNIT_DAYS[unit]
    return PULL_DATE - timedelta(days=round(days))


def within(unit, n, window):
    """Is the age text certainly inside the window? 30 d: min/h/d/w; 90 d: + 1-2 mo; 365 d: + 3-11 mo."""
    if unit in ("min", "h", "d", "w"):
        return True
    if unit == "mo":
        return {30: False, 90: n <= 2, 365: n <= 11}[window]
    return False


def parse_count(s):
    """'26.6K subscribers' / '1,234 views' / '115 videos' -> int (rounded where the text is rounded)."""
    if s is None:
        return None
    m = re.search(r"([\d.,]+)\s*([KMB]?)\b", str(s))
    if not m:
        return None
    n = float(m.group(1).replace(",", ""))
    return int(round(n * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)]))


def fnum(x):
    return "" if x is None else (f"{x:,}" if isinstance(x, int) else str(x))


def median(xs):
    return statistics.median(xs) if xs else None


# ---------------------------------------------------------------------------------------------------------------
# 5. Loading.
# ---------------------------------------------------------------------------------------------------------------
def load_master():
    rows = list(csv.DictReader(open(os.path.join(RAW, "channels-master-2026-10-24.csv"), encoding="utf-8")))
    return {r["channel_id"]: r for r in rows}


def load_about():
    out = {}

    def add(name, d):
        for k, v in d.items():
            if isinstance(v, dict) and v.get("DESC") is not None and k not in out:
                out[k] = (name, v)
    add("channels-master-about-2026-10-24.json",
        json.load(open(os.path.join(RAW, "channels-master-about-2026-10-24.json")))["channels"])
    add("channel-finds-pages-2026-10-23/about.json",
        json.load(open(os.path.join(RAW, "channel-finds-pages-2026-10-23", "about.json"))))
    add("round2-nexlev-pages-2026-10-24/about.json",
        json.load(open(os.path.join(RAW, "round2-nexlev-pages-2026-10-24", "about.json"))))
    add("round2-oldheat-2026-10-24.json",
        json.load(open(os.path.join(RAW, "round2-oldheat-2026-10-24.json")))["channel_about"])
    cm = json.load(open(os.path.join(RAW, "check-master-2026-10-24.json")))["channels"]
    add("check-master-2026-10-24.json", {c["channel_id"]: c.get("about") or {} for c in cm})
    return out


def load_checker_types():
    cm = json.load(open(os.path.join(RAW, "check-master-2026-10-24.json")))["channels"]
    return {c["channel_id"]: c.get("thumb_type_checker") for c in cm if c.get("thumb_type_checker")}


# ---------------------------------------------------------------------------------------------------------------
# 6. Manual decisions (each one a reading, with its reason). D_CONFIRM: the "one look at the About page" that
#    check-master.md asks for, recorded per channel where the word flags and the stored tier disagree.
#    Filled after reading the flagged list (see census-build-2026-10-26.json "d_review").
#    Value: (decision, reason); decision in {"D", "not D", "contractor"}.
# ---------------------------------------------------------------------------------------------------------------
D_CONFIRM = {
    'UCDWlhWMW8Ji0rwlBwL8fpQw': ('contractor', "one-man home-performance contractor (title 'Everything I Carry to Be a One-Man Home Performance Contractor'); found in the hand-check"),  # Home Comfort Guy
    'UCL6-fPMM4kGL5qSTVnklNuA': ('contractor', 'AAA Heating & Cooling, Portland duct-cleaning / HVAC contractor'),  # AAAHeatingCooling
    'UC2eJMGkfkpwJ6JZfDYBRZow': ('contractor', 'Aabbott Ferraro, Twin Cities residential contractor'),  # Aabbott Ferraro
    'UCnMnz5jXwrPlZsdRV8rxFig': ('D', 'distributor (Able Distributors), for installers'),  # Able Distributors - Your HVAC Solutions Delivered!
    'UCOZR-1IqsAer9wzlvFgb4mA': ('D', 'LLC name; training content for techs (Training, brazing, commissioning titles)'),  # AC Service Tech LLC
    'UCsnKFNRChikWLQHzk1XxZ-w': ('D', 'industry podcast for HVAC business owners'),  # Accelerated HVAC Success
    'UC7pgNPrndhM_ptJCljbTnHg': ('contractor', 'Aced It! Cooling & Heating, founded by two technicians; homeowner titles'),  # Aced It! Cooling & Heating
    'UCuRShsGbjls2dUwOY9pN_Xw': ('D', 'manufacturer / brand for contractors (ACiQ)'),  # ACiQ
    'UC2td_67-1-2VF-6903GxHdw': ('contractor', "heat-pump installer's working-day vlog (Rowlandson Heating)"),  # Adam Rowlandson
    'UC14pNd6CMexfOpHPpQkPGtw': ('contractor', 'one-man HVAC shop (since 2006) documenting installs'),  # Advantage Heating & Cooling
    'UCy3mIZxWpEs9VIbTqL1IXuw': ('contractor', 'Advantage HVAC, Plumbing, and Electrical, Florida Panhandle company'),  # Advantage HVAC, Plumbing, and Electrical
    'UCAvd1mKr_jbr28dDPvL8mFg': ('D', 'training in HVAC installation methods'),  # AGL Mechanical Tips
    'UCxj9SjLaEhf2FtiySEykkvA': ('not D', 'individual; mixed how-tos'),  # AIR MAN
    'UC770qV6hY89oUhZwiz8YFcw': ('contractor', 'duct-cleaning company (Montreal)'),  # Air Plus Montreal
    'UCJjE8ZU9of_W5QWy40O7QpQ': ('not D', 'individual air-purification consultant reviewing products'),  # Air Purification Education
    'UC_AIrBKbQ-hOzeJ5okzfN_Q': ('not D', 'individual technician (service calls, trade talk, help for homeowners)'),  # Air Smith HVAC
    'UCSy0XnpfO30nwdnNppGjdMw': ('D', 'manufacturer of duct-cleaning equipment for businesses'),  # Air-Care
    'UCs64HIuo3bghzMMLDukRf0A': ('D', 'UK retailer of portable ACs, dehumidifiers and fans'),  # AirCon Centre
    'UC9uAexMxluUzXjJtxQ2ysHA': ('D', 'product company (Airspool solar AC)'),  # Airspool
    'UCjxb3s2iW-EMrcInABRVxjQ': ('contractor', 'Albert Air Inc., Carrier installer; homeowner titles'),  # Albert Air Inc.
    'UCCEkrdkurnRF-gNh0h_61HA': ('D', 'Leeds plumbing and heating company (power-flushing, boiler installs); under 50% HVAC'),  # Allen Hart
    'UCMvzPcAmmdFJr6Yk-2v0k-w': ('D', "retailer ('America's Heating and Cooling Store')"),  # alpinehomeair
    'UC1Ox1WqBLGR6GXDiEDDz3Hw': ('D', 'parts and supplies retailer (Alternative Heating & Supplies)'),  # Alternative Heating & Supplies
    'UCCOnzdWPBU9ZAF-PjO9NdeA': ('contractor', 'American Veteran Air & Heat, LLC, licensed contractor'),  # American Veteran Air & Heat
    'UC0ZXEoSP3PaTD86T0MfGE-A': ('D', "About: 'guide new tradesmen/tradeswomen'"),  # Andrew Greaves
    'UCFxf3hjNRSQ706L3jgDYnBw': ('not D', 'individual technician talking to DIYers'),  # Anti DIY HVAC
    'UCSS6u9ZmKOg-fIQoU71Vtgg': ('D', 'manufacturer (AprilAire)'),  # AprilAire
    'UC8k-lOaV6xf04pJgR_QWI1Q': ('contractor', 'mini-split / heat-pump installation business with how-to videos'),  # Atlantis Energy Heat Pumps
    'UCWtuOnlW7BeXLgr6M1_Z49g': ('contractor', 'Atlas AC Repair, residential company in Texas'),  # Atlas AC
    'UC2R_ibkoxgz0Ww06hnt_Ojg': ('contractor', 'UK oil-boiler engineers (company) documenting jobs'),  # Barton Oil Burner Services
    'UC3A49fGGkMo2RwdddC35Tiw': ('D', 'manufacturer (Baxi)'),  # Baxi - sustainable heating and hot water solutions
    'UCUcfImILZgYkx8WhE3XNj7A': ('contractor', 'Birmingham gas-engineer company; boiler error-code repairs'),  # Birmingham Boiler Fix
    'UCqH89ezsE1REn1cPXnKfu8g': ('D', 'blue-collar trade-career education'),  # Blue Collar Edu
    'UCBcvJZZwIKcm6i0UsBX2LBA': ('D', "About: 'directed to boiler and hvac service techs, engineers and designers'"),  # Boiler Room Detective
    'UCOa9595DxOeB3wJ83XFXuMw': ('D', 'HVAC career / apprenticeship channel'),  # Brandon Does HVAC
    'UCX4W5IzSGtu8kPcNk2TIM1Q': ('contractor', 'Breeze AC, family-owned Sarasota contractor'),  # Breeze AC SRQ
    'UCUYaEVokctnDfwkjSlPQdBw': ('D', "licensed HVAC contractor's trade talk (commercial contracts, business)"),  # Brian Barraza
    'UCAgHhEfnQZjbYERIuUT_wJA': ('contractor', 'duct-cleaning company (Florida)'),  # Bright Air Duct Cleaning - Florida
    'UCaMO8kXSLmJckRwNyGEAb5Q': ('D', 'manufacturer (Bryant)'),  # Bryant Home Comfort
    'UCCBmTrGcX65GRxqSOG_t0ww': ('D', 'building-systems training'),  # Building Systems Academy
    'UC5AfXN4jSlv3cmqlUCWsrUQ': ('D', 'custom home builder that sells and reviews stoves and grills (dealer content)'),  # Cameron Contracting Ltd.
    'UC4mk6WwFmteS8LpmmKaAqpg': ('not D', 'individual technician; About addressed to pros and homeowners alike'),  # ChilesHeatCool
    'UCqYmdUjo5w0v1NdN7paCKmA': ('D', 'master plumber in business since 1993; plumbing-led'),  # Chuck Barron
    'UCZ77CtPot5ZyLrMoAKByZ3Q': ('contractor', 'Chud Cooling, Heating, Plumbing & Electric, family-owned'),  # Chud Cooling & Heating
    'UC0Nyjfbj69iZOOeo6d4Whwg': ('D', 'manufacturer (Clade Engineering)'),  # Clade Engineering Systems
    'UC0FAp9pyHx3m9Z5O7gOsxlA': ('contractor', 'Clean Air Heating & Cooling, Bellingham WA'),  # Clean Air Heating & Cooling
    'UCXis46kUpTe_PqjUO4ziW8Q': ('D', 'ClimateMaster dealer-network channel'),  # cmdealernet
    'UCt47_v_207fZOLrHhwXpIdA': ('not D', 'consumer-advocate channel'),  # Coil Exposed
    'UCIdzZrKCdyNf1Oh1cGjSYnA': ('contractor', 'crawl-space repair company (Huntsville), homeowner topics'),  # Crawl Space Ninja
    'UC-f-UnJbXdRlfgBffP7cq_w': ('D', 'commercial / industrial technician day-in-the-life (trade titles 17/25)'),  # CREATIVEHVACR
    'UC3envseXVPBCiIYk4oRkHpw': ('contractor', 'D-Air Conditioning Company, Inc., California contractor'),  # D Air Conditioning
    'UCpSSopClZmwUZ-TrGgJ4z-w': ('not D', 'individual NYC technician, mixed homeowner / pro titles; About not addressed to the trade'),  # D2D NY Real World HVAC Simplified
    'UCUc6K0I4CQjEOR6ZBMBttSg': ('D', 'technician POV / tool loadouts (trade titles 6/11)'),  # Daniel Palacios
    'UCGzd_cifQY0qKQG87uMU_BQ': ('not D', 'individual technician vlog'),  # Davevid 
    'UCzu2gnt-w90r652axiNodKQ': ('contractor', 'duct-cleaning company'),  # DaVine Air
    'UCqe96z4oQMUvVl0gdXHuqzQ': ('not D', "individual technician's service calls (Long Island); not presented as a company"),  # DC HVAC
    'UChJnJHST89yDi8-Gzj5CClQ': ('contractor', 'GM of a One Hour Heating & Air franchise; homeowner titles'),  # Derek Cole
    'UCpOuHQWSdUYzIVOkNU-GCOg': ('not D', 'individual DIY repair channel (plus SEO courses)'),  # DIY HVACMillionaire Advice Class "Capacitor Freon"
    'UCCZbLEJAq6HCJu4_iOfVs3g': ('contractor', 'energy-audit / insulation company, homeowner topics'),  # Dr. Energy Saver
    'UCTpYboVUYzeXK4ztWJ5OnZQ': ('D', 'dealer-network channel (Dr. Energy Saver dealers)'),  # Dr. Energy Saver Dealers
    'UCMRQNX0-nhuyvl7SlGIzrNQ': ('contractor', "owner of Drew's Crew Heating & Air; service calls and homeowner tips"),  # Drewdriskle
    'UCgxUX-M20ZY8tUod77rB8Bw': ('contractor', 'Ductless Plus, Mitsubishi install company (Denver)'),  # Ductless Plus HVAC
    'UCIEtNMQBSXbocED9v6G2wWg': ('D', 'duct-cleaning franchise brand (DUCTZ)'),  # DUCTZInternational
    'UCyYzJxK_6DMvIgqSpR2zN6Q': ('not D', 'individual persona channel'),  # Earl The Furnace Man
    'UCXr0IGX4MDukgTQnmoq2AWw': ('D', 'manufacturer (ecobee)'),  # ecobee
    'UCOZ8J2HTW6BsD-x5cVfQ1_Q': ('contractor', 'Efficient AC, Electric & Plumbing, Austin family-owned contractor'),  # Efficient AC, Electric & Plumbing
    'UCrtiO8HVIr0AbA3dE-yL1sw': ('D', 'retailer (Electric Radiators Direct)'),  # Electric Radiators Direct
    'UC2veDhI08nz8VvM0Pj8Xvcw': ('contractor', 'AC installation company (Samsung installs, planning-permission explainer)'),  # Electrum Electrical
    'UCx0w_u6S-Z1emYEstp6-FPA': ('contractor', 'Elite Services Group, UK heat-pump / solar installer; customer case studies'),  # Elite - Supporting a sustainable future
    'UCAXtn7slzglgBiNS3za5YgA': ('contractor', 'UK renewables installer (Elite Renewables); home case studies'),  # Elite Renewables
    'UCW4B9N7cA8FxxDnaYr5gIKQ': ('D', "manufacturer's representative (Emerson Swan)"),  # Emerson Swan, Inc.
    'UC9nEaKOfm5xtp9irCMiGkLg': ('D', 'home-performance training for pros (HPP)'),  # Eric George | Home Performance Pro
    'UCBYfyv9uLaGNzlC_10S_fVw': ('D', 'commercial installation crew vlog (new construction projects), not for homeowners'),  # ETB Seui
    'UC1dsZcHNdBxasfw1IUkKILQ': ('D', 'About: for HVACR professionals; commercial equipment'),  # Everything HVACR
    'UCME4xG68IQbZP0YgkPT_3FQ': ('D', 'technician career / day-in-the-life content'),  # Ewok
    'UCsbMH54DgBeke5RE8IVL8Vg': ('D', 'industrial process-instrumentation training'),  # Expert Technicians
    'UCQCRIhHQ__ncUxtOHiIXI4A': ('not D', 'consumer-advocate channel (A)'),  # Exposi
    'UCyzxIMhRid9TBYInYNmzzaQ': ('D', 'radiator retailer with showroom (Feature Radiators Ltd)'),  # Feature Radiators Ltd
    'UCVdf0x94g-t4zIY5oGjma3g': ('contractor', 'Fire & Ice Home Services; homeowner cost and repair questions'),  # Fire & Ice Home Services
    'UCJHLqwsRD4NEXzvNkY4Gm-A': ('not D', 'roofing tips site with product reviews; not an HVAC company'),  # Fixmyroof
    'UCSIClXw_5lT1buMo2BM6q7g': ('not D', 'individual repair channel'),  # Forever Tech English
    'UCvQxGD5oNn5N6Hd6Zfvhb4w': ('not D', 'individual old-ways channel'),  # Forgotten Materials 
    'UCjEPa1OUEKwjRTMlevzzNrg': ('contractor', 'Fowler Heating & Cooling, family-owned Southern Illinois contractor'),  # Fowler Heating & Cooling
    'UCjKCB2ujHpe0mYEKhKVe3Aw': ('contractor', 'Fox Family Heating and Air Conditioning, Sacramento'),  # Fox Family Heating and Air Conditioning
    'UC1Y9nzjbI5uAT1wFOiXdo4w': ('not D', 'individual persona channel'),  # Frank From Maintenance
    'UC-ZPTqzkJujjUouZZohAvDw': ('not D', 'individual; DIY heating repair for homeowners'),  # FurnaceTech
    'UCwmXHahFSti0E9jgax6px3Q': ('contractor', 'Fuse Service, Silicon Valley contractor; homeowner titles'),  # Fuse Service: HVAC, Electrical & Plumbing
    'UCWmlRLAOpx9f1t_cVkBx8-g': ('D', 'manufacturer (Google Nest)'),  # Google Nest
    'UC8eT35xEnHJH6uUStaQkzsg': ('D', 'retailer (Got Ductless)'),  # Got Ductless
    'UCBRMjS8mOM2AhmAjuRarK1A': ('not D', 'consumer-advocate channel'),  # Green Exposed
    'UCdihWWSNXWmO-MYtVx5bx-A': ('D', 'lead-generation marketplace company for installers'),  # GreenMatch UK
    'UCCUTw-CU2QS13BlMjdLiHFA': ('D', 'manufacturer (Harman)'),  # HarmanStoves
    'UCTppb1CuxtXej-1JE4BxoZg': ('D', 'online distributor / retailer (HeatAndCool.com)'),  # HeatAndCool.com
    'UC4fE-DGWS8pixzNnXrNXw_Q': ('contractor', 'owner of ATC Cooling & Heating (Kingsport TN); homeowner stories'),  # Heating and Cooling Explained
    'UCeZre0NPsyD6QXfgO7U2wfQ': ('D', 'HeatingHelp.com, heating-trade publisher (pipe stories, industry awards)'),  # Heating Help
    'UCefT9u9901XwmbD5THUN3RA': ('D', 'engineer working with developers and contractors (trade-facing valve content)'),  # Heating Solutions
    'UCIdsfvVPdc4S9wQ5_VpyTJA': ('contractor', 'Heritage Home Service, family-owned NE contractor'),  # Heritage Home Service
    'UCI2VDyfqdsttBE0X3c-ArXg': ('not D', 'building-science creators (Corbett and Grace Lunsford), homeowner and pro audience'),  # Home Performance
    'UCr_B6AgjbPVOaTtXsBy1LHA': ('D', 'home-repair-plan company (HomeServe), brand channel'),  # HomeServe
    'UCeO2QdRNK3y6Srm8SpFaeTw': ('D', 'marketing agency for home-service businesses'),  # Hook Agency
    'UCl16ptu7IK-jhdsBBdm1xQw': ('not D', 'individual hobby channel'),  # Hotrods & Homestead
    'UCW5aDZyLh2s8hOE18uqqrWg': ('not D', 'independent air-purifier review site (not a maker or seller)'),  # HouseFresh
    'UCgUj5yLMYNyyqC8VaEuQR7g': ('not D', "individual refrigeration mechanic's job videos"),  # Hozer HVAC
    'UCNXmHUxNpoa_DiC54VxkJjg': ('D', 'process training for HVAC contractors'),  # HVAC 2.0
    'UCjA9yNcieoTyGmKcozlAQ0A': ('D', 'HVAC careers / interview training'),  # HVAC Academy
    'UCk_Epq89IzNRDJDLvlnS9rg': ('not D', "individual technician's service-call vlogs"),  # HVAC AO
    'UCc8BAqKC3JEcrrEGksWxl3w': ('D', "commercial technician; trade-career titles ('Why Most HVAC Techs Stay Broke')"),  # HVAC Dean 
    'UCcv3wg9ehzTs3UNPtBM88Fg': ('D', 'HVAC business / sales coaching'),  # HVAC Greatness by Pete Ramsey
    'UCrkPKl9wg6Ev_F1QNoobxzA': ('D', "About: 'learn about the HVAC Industry'; trade titles"),  # HVAC Guide for Pros
    'UCiz21FXLOV65NTgiUfJsxTg': ('D', "About: 'help instruct technicians'"),  # HVAC GUY
    'UC_nPPCBJNGsAruAjRpph-VA': ('D', "About: 'help educate fellow technicians'"),  # HVAC in SC
    'UC5llJRQJa1szHYDjxQ5N_QA': ('D', 'trade podcast'),  # HVAC Knights
    'UC-MsPg9zbyneDX2qurAqoNQ': ('D', 'trade podcast / life in the field'),  # HVAC Know It All
    'UC-5zd31qI3tWQt8u4ZIJr-A': ('not D', "individual technician's tips"),  # HVAC Life
    'UChKYmZsxMtfBlVwj_NSWAXQ': ('not D', 'individual technician vlog'),  # HVAC Life with Alex
    'UCZkMaUzBwshDHOss7mfFRTw': ('not D', "individual tradesman's 'fails' videos"),  # Hvac Nerd
    'UCDUAuJEO5e7GcBAPnodUvrw': ('D', 'HVAC job-interview questions (trade careers)'),  # HVAC OFFICIAL CHANNEL
    'UCiK3xbhxxNaJF1EGUM0ugeQ': ('not D', "individual technician's job videos"),  # HVAC OTJ
    'UCJGQJF0p5AxwZdeqx4Y8kFw': ('D', 'trade podcast'),  # HVAC Overtime
    'UCra3t-e5-94H4VksgiLPa6A': ('D', "contractor (NY Boiler & Air Conditioning Repair) whose About addresses 'the HVAC & plumbing industry'"),  # HVAC PAPI
    'UC2Zt04YT6VJeKfOBjuz9E1w': ('D', 'trade-facing system-design content (round 2 checker: D)'),  # HVAC Pro Blog
    'UC1-zqhgCQaEolVtVJ-cL5ww': ('D', 'technician day-in-the-life (trade titles 19/30)'),  # HVAC Roddy
    'UCdLlUhD9LUGm0-NTYDASPFA': ('D', "trade school: 'training primarily for techs, by techs'"),  # HVAC School
    'UC_wC1rbMeYAv0qQUj6YmFcw': ('D', 'training boot camps'),  # HVAC Service Mentor
    'UCWM8W1bB5cLCVEXfGF0_vMg': ('D', 'trade titles 10/30; About: 21-year service technician teaching'),  # HVAC Service Technician Talk
    'UCE5lQKOyYXz6J6UgZQn2ptw': ('D', 'online training for students and mechanical engineers'),  # HVAC SIMPLIFIED
    'UCSbqV46NJaeIkQAoQmDv8Jw': ('D', "About: 'for beginner and seasoned technicians'"),  # HVAC Tech Knowledgy
    'UCADuLs5Slc_oXtQuVzEG5ww': ('D', 'tech tips, tool reviews for techs'),  # HVAC Tech Tips
    'UCRmPv4sdRiPqyWXqPDVWNKg': ('D', 'sales and business growth for HVAC companies'),  # HVAC Technician Sales Secrets
    'UCWhFqsrrNfGWQnXSAVEAaZg': ('not D', "individual retired tech; affiliate product reviews for buyers ('Training' in every title is the channel name, not trade content)"),  # HVAC Training 101
    'UC7xFt-7K4A05tc1TdrgDQEg': ('D', "About: 'for commercial HVAC professionals'"),  # HVAC TV
    'UCczJ6EU5aLBogQOzFZ_W0HQ': ('not D', 'independent consumer investigation channel'),  # HVAC Uncovered
    'UCdDmgTEJKpbZQD-eRYO5u1Q': ('D', 'retailer (HVACDirect.com)'),  # HVACDirect
    'UCJnBJy9jSIRy9dbtqyMW_Uw': ('D', 'commercial / industrial technician diaries (trade titles 17/30)'),  # HVACJess - The HVAC Diaries
    'UCvqYNMZq4c2sTztlX7ZqeNg': ('D', 'HVAC business coaching'),  # HVACmillionaire
    'UCncYLcGLWT2IfaiDQCP5zCw': ('D', 'instructional commercial HVAC / refrigeration for techs'),  # HVACR North
    'UC7EJjONRyeihmQELDIFF8qQ': ('D', "commercial and industrial refrigeration, 'life in the trade'"),  # HVACR Survival
    'UC6CeEomD0vavKtCwOyjcHIw': ('D', 'About: training for technicians, engineers, students'),  # HVACR Training Membership
    'UC5Pnrxqqg4BLTsfsUzWw5Pw': ('D', "commercial refrigeration technician; 'involved in the trade'"),  # HVACR VIDEOS
    'UCIz2gu2HcfuuGoLYAPl9x8g': ('not D', 'individual; homeowner comparison videos'),  # hvacrepairguy
    'UCRdNcv3g_4rpbNEyFopZwDg': ('D', 'chiller technician education'),  # HVACTIME
    'UCvFNzcf6rbYdxaYiqf3ZkMw': ('contractor', 'hydronic heating installer (one install video)'),  # Hydrotherm Hydronic Heating
    'UCrAj3hHqpndzrsRiU9_VhPQ': ('contractor', 'ICS Comfort Boss residential HVAC company; homeowner titles'),  # ICS Comfort Boss
    'UCPSRel4gokJaQCsxVALBDcw': ('D', 'distributor (Insulation Distributors Inc.)'),  # IDI: Insulation Distributors Inc.
    'UCerPF8NznYBUB4Yf2um1gaw': ('D', 'UK installer company (instant online quotes, finance)'),  # iHeat
    'UC4YkHp8NgTkOLtFQtq3q8ig': ('not D', 'individual; About addressed to techs and homeowners alike'),  # INDOOR AIR QUALITY 
    'UC8ZWT3Qi3UbBK2oBi2ymyOA': ('D', 'industrial building-controls technical content'),  # Insight Control System
    'UCwjtvUT3hRjTxegKH8gZcYA': ('contractor', 'Insulwise, Pittsburgh home-performance company; homeowner topics'),  # Insulwise Energy & Comfort Solutions
    'UCj1uAkvY__HfwHl23Nes1tw': ('D', 'HVAC careers / trade (Pakistan)'),  # JabirWaqas
    'UCsVYxwEvQIlB6b0MDDi7dpw': ('not D', "individual technician's service calls; About not addressed to the trade"),  # Jeff’s HVAC Adventures
    'UCxzAJacWR8mwOcUbplo9U-A': ('D', "refrigeration-cycle diagnostics teaching for techs (reading of titles); '40 years in the trades'"),  # Jersey Mike HVAC
    'UC5XhfPghpQ9e3BOC81mb48Q': ('not D', "individual technician's service calls"),  # Jesse Kelley HVAC
    'UCdQJI4OshsphxL6Vt8FJE-g': ('contractor', 'HVAC contractor in Des Moines educating homeowners and contractors'),  # Joe Tollari
    'UCkWMTCAS-1mKq342t_gVhYw': ('not D', "individual technician's service calls; About not addressed to the trade"),  # John Israel HVAC
    'UC5__d2EyNdmeOr717apCjKQ': ('D', 'About: teaching beginning HVAC technicians'),  # John Jennings
    'UCfyMMHJv-V10UpTkXxCvikg': ('not D', "individual; About: 'here to help you as the consumer'"),  # Jordan Dearden
    'UCUisLZYxDNx-rKrgCcDDO5A': ('D', 'commercial / industrial service (cooling towers, water-source heat pumps): trade-facing'),  # Jumper man Tech
    'UCQLQI7hMy_v7cXknTdGrqQw': ('contractor', 'licensed HVAC contractor in Greenville SC; service-call stories'),  # JustintimeHVAC
    'UCam5-STAaS2ddkKEYF9w8RA': ('D', "About: technician humour for 'the trades'"),  # Koolin’ with Krauss 
    'UCJqqdHV4bemYBJUvloyJ8DA': ('contractor', "Leaky's Plumbing, Heating & A/C; About: 'help you take your home back'"),  # Leaky’s Plumbing, Heating & A/C
    'UCz-HGcQ9vXaBtkXPMIOtOmA': ('D', 'engineering / interview training'),  # Learn Engineering MEP
    'UCAhvDdx7KbeJuLqybIRVnGg': ('D', 'custom home builder company'),  # Legacy Classic Homes
    'UConWX7kH2qW9pOgUx2LBhww': ('D', 'manufacturer (Lennox)'),  # Lennox Learning Solutions
    'UCIXjGRqwen1b48euVcqZxcA': ('not D', 'individual persona channel'),  # Leroy Bell's Repair
    'UCRbha3ai17bUF2Ac6R6nRYw': ('D', 'About: for new and veteran maintenance technicians'),  # Lex Vance
    'UCNZKG4lCeMACucQV90M5tmg': ('contractor', "UK heating installer (Lloyd's Gas & Renewables)"),  # Lloyd's Gas & Renewables
    'UCX1q8fsuXltR9kjhj7cOTQg': ('D', 'manufacturer (Lomanco)'),  # LomancoVents
    'UCicgREcAyh_AsQyie6rwJ7Q': ('D', 'manufacturer (Lopi Stoves)'),  # Lopi Stoves
    'UCIoD-SEdUWMA74tWXRMyCZQ': ('D', "About: 'HVAC R education... getting started in the trade'"),  # Love2HVAC with Ty Branaman
    'UCf0mHkUi_xiAdb97QnecFAA': ('contractor', "Magic Touch Mechanical, Phoenix, 'whether you're a homeowner'"),  # Magic Touch: Fire & Air
    'UCeSzwJbwcKgQ9iJAhcd7S4w': ('contractor', "UK gas engineer company, 'Helping you with your heating in your home'"),  # Mark Ballard LTD, Professional Heating Engineer
    'UC1pLRqHUCuwufmLvLya7cKg': ('D', 'sheet-metal / insulation-cladding pattern development (trade)'),  # mark wood
    'UCek4-YG3VQEO-QvDiyEOJCw': ('not D', 'individual licensed technician; homeowners and techs'),  # Maryland Hvac Repair
    'UCwHKitVzl3iANcndhHRQhhA': ('D', 'manufacturer (Meaco)'),  # Meaco
    'UCYkz4FCKONzTPekh-zkUAmQ': ('D', "About: 'mastering the HVAC trade'"),  # Mechanical Pros
    'UCmFkUrOFd_FaASmI9HysA3g': ('D', 'MEP trade training and business information'),  # MEP Academy
    'UCGFOhDShl9eHClzJ7YOwNJA': ('contractor', 'one-man HVAC service company'),  # Michaels HVAC Service
    'UCQxmS3iVsThKYAsNQ540jZw': ('not D', 'individual technician vlog'),  # Michigan Heating Guy
    'UCqPFxcbyCnlWz6tmackoJMQ': ('not D', 'individual energy-data channel'),  # Mick Wall (Energy Stats UK)
    'UCWGn3bkhut23-X6DEJsyEpw': ('D', 'manufacturer (Midea)'),  # Midea America
    'UCK9DXL31fZSNi3h7DTqTyzg': ('D', 'construction company teaching installation methods to the trade'),  # Miillers Construction
    'UCG_Pwm8tfMnJg1Rp2Fsd-qA': ('contractor', 'Pipe Doctor Plumbing & Heating & Air; real service calls, About not addressed to techs'),  # Mikey Pipes - Pipe Doctor Plumbing & Heating & Air
    'UCsdjQ9GmaSwm4LADVGy-f9g': ('D', 'HVAC training channel'),  # Mikey Pipes HVAC Training
    'UCc7-1fGMymjPAgg4OwKLNug': ('D', "HVAC business owner's raw business vlog (hiring, employees, quotes)"),  # Mikey Pipes Uncensored
    'UCXyM5L5Kf4ejlbtjHb8YTsA': ('D', 'pellet-stove retailer (small family business)'),  # Miles Pellet Stoves
    'UCpWTaO34JGTv2GKFfNb-yNQ': ('contractor', 'MARAC Services Pty Ltd, Sydney installer; job vlogs'),  # Mitch Attwood 
    'UCAiLfdXEsKVOAarqANjSweQ': ('contractor', 'Monkey Wrench Plumbing, Heating, Air & Electric'),  # Monkey Wrench Plumbing, Heating, Air & Electric
    'UCtjmjQ_lBAg-XdoT1MJgdTQ': ('not D', 'individual AC repair technician (India)'),  # MR AC TECH
    'UCa3r1wr9L-2HVXKLlf2FeuQ': ('D', 'manufacturer (MRCOOL)'),  # MRCOOL
    'UCBJ7O-VYUUHrKEQhuX9N7mg': ('D', "About: 'help new technicians learn'"),  # My HVAC Life
    'UCESseadPQFXRUJngZSWQGBg': ('contractor', 'N.E.T.R., Inc., Boston installer; homeowner ductless guides'),  # N.E.T.R., Inc.
    'UChPCjkQVmJhhDa5oPqZaWNg': ('D', "commercial and refrigeration tech content; About: 'the HVAC business'"),  # NathansHVAC
    'UC7fmaDG-Q4ZLKSCmIkgMVWA': ('D', 'trade-facing: commercial service (Trane IntelliPak, RTUs) and tool content for technicians and apprentices'),  # Nighthawk HVAC
    'UChtHZS5botR-fCEW5hbxqJw': ('D', 'oil-tank replacement company'),  # Oil Tank Replacement
    'UCUBvvBHGf6WOlc1MVfoZdZQ': ('not D', 'individual persona channel'),  # Old Maine Firewood
    'UCVkVhwXnattecHEyw7xSIJA': ('not D', 'individual old-ways channel'),  # Old Ways Restored
    'UCp6Lo9LEIkHNDO5kelQAB0g': ('D', 'parts retailer (humidifier / air-cleaner parts)'),  # On Time Mall Inc
    'UCCfVNgkRrgMzNPrb8nOKigA': ('contractor', 'one-man HVAC business (Georgia) running service calls'),  # OnemanHVAC
    'UClBatBtSdx7ijQQ7zWfasXg': ('D', 'parts seller (Open To Public HVAC Parts); homeowner how-tos, but a retailer'),  # OPEN TO PUBLIC HVAC SCHOOL
    'UCCQOrvsD4vP0VAmW4QaX81Q': ('contractor', 'Paul The Plumber, family-owned plumbing / HVAC company in NH'),  # Paul The Plumber
    'UCJDGdJnqLldzvMABFtv_EDA': ('not D', 'individual; wood stove builds (not a company)'),  # Penpen vn 1
    'UCN6vSgbZ3JEEaH6h8MnugeA': ('D', 'About: tutorials for students in the heating industry'),  # Pete's Shed
    'UC6vA_TPy34Xb_oin4WV-_vA': ('D', 'HVAC instructor; commercial / building-automation training'),  # Pioneer HVAC Controls
    'UCDjLxKkmLNjOaA8SSgJvtBQ': ('D', "UK plumbing and heating engineer's job vlogs (plumbing-led)"),  # Plumb Like Tom
    'UCKrKCoFuka42Py6dkINM34A': ('D', 'commercial / industrial boiler and chiller rental company'),  # Power Mechanical Inc.
    'UCbRUa-hRUKYQbgSqo3ILq4w': ('not D', 'individual technician vlog'),  # Powlas HVAC
    'UCXzUc27pNwYfbjrow8jjbEw': ('not D', 'individual persona channel'),  # Practical Home Energy
    'UCtigCSJWeP9OsMsgqqATVlw': ('contractor', 'Prime AC & Heat, DFW family-owned contractor'),  # PRIME AC AND HEAT
    'UCfsNbViu-G8TnbteFo8RCxQ': ('D', 'marine electro-technical officer (trade)'),  # ProbeLem®
    'UCK5IaMcKs3dku7n63fElgsQ': ('D', "HVAC design company's industry / business education"),  # ProCalcs University
    'UCk6hUUjw6QNmLe22_tezL1A': ('D', 'manufacturer (Quadra-Fire)'),  # QuadraFire Stoves
    'UC2AsqyR6xLMkte3mQHf-umw': ('contractor', "'Family owned HVAC company in the middle TN area'"),  # Quality HVACR
    'UChv3pdhzcfTjqvaphUqQC0g': ('D', 'manufacturer (Qvantum)'),  # Qvantum Sverige
    'UCeuOI9DTbXqOznX2Rg_TFzA': ('D', 'parts retailer (QXParts.com)'),  # QXParts
    'UC6-fqz6a3gJmCqJ25KTenyw': ('D', 'manufacturer (R.W. Beckett)'),  # R.W. Beckett Corporation
    'UCS5bTRiJE5Go1JE2aBfU7EA': ('D', 'trade training (India / Bahrain, Hindi)'),  # Refrigeration and HVAC technical fault
    'UChR4HQuEJCXSLw0cinvmTrQ': ('D', "supplier 'working with the trade'"),  # Renewable Equipment Solutions
    'UCJHKy9ghT7YuWSIvcc3wjbQ': ('D', 'commercial kitchen / refrigeration repair company'),  # Restaurant Repairs
    'UCWqoUvmG3PDzKpx_oxn5SIQ': ('contractor', 'RetroFoam of Michigan, insulation contractor serving homeowners'),  # RetroFoamofMichigan
    'UCZWo0yDYklinlnCWKlCzu3A': ('not D', 'individual technician'),  # Reuben Sahlstrom
    'UCYUc96NXRnnbRSRE3BuuS5w': ('contractor', 'small HVAC business owner (Destin FL) day-to-day service'),  # RHODES - Cosmic Cooling
    'UC3QY2CP1RnEUDeJ0qwXAQdg': ('D', 'HVAC Training Solutions (trade school)'),  # Ron Walker
    'UCDx7t_XxrIcwRU9DOmJqToA': ('D', 'trade titles 9/14 (becoming a tech, tools for new techs)'),  # Rosa The Female HVAC Tech
    'UC9RjN42ym2mamtWJSl0iHfw': ('not D', "individual technician's workday vlogs"),  # Ryan Hughes HVAC
    'UCxcTqtjCsGkjlDhpYxJ2gzw': ('not D', 'individual fireplace / stove channel'),  # Ryan’s Fireplace Diaries
    'UCXp3Y8eQFa88gmpvUQ3iqGg': ('D', 'students / interview training (India)'),  # S R HVAC
    'UCBx2gWCETkG6EqJRQHMy4qA': ('D', "About: 'help training videos for the advanced heating technician'"),  # Scott Taylor (TayloredSteam)
    'UCWp7BGt8Bq68IuAuOfWJmJA': ('contractor', "Service First HVAC Solutions, Ontario; About: 'helping homeowners understand their HVAC'"),  # Service-First-HVAC-Solutions
    'UC0dZcV01OIUkGURb9ot4iOw': ('D', "About: 'Technician Training & HVAC Education'"),  # ServiceTechSonny
    'UCoXVJcgdZninmc0lXeBJGCw': ('not D', 'individual technician vlog'),  # Shorty HVAC
    'UCC-uuGy0BRA3sWMKZP-yQJA': ('contractor', 'Sierra LLC, Las Vegas contractor; thermostat how-tos for customers'),  # Sierra LLC Air Conditioning & Plumbing
    'UCA_ZKNA-k-nA4eH5qNb3jXA': ('contractor', 'steam-heat service company (antique systems)'),  # Silent Steam Team
    'UCsXTVYa8FRFHUcfm7R8EXyQ': ('D', 'energy nonprofit; teacher / trade training'),  # Slipstream
    'UCpCfTy6di2SLqFnlRyJQNsQ': ('not D', "technician's own DIY / solar mini-split channel (round 2 checker: A)"),  # SmitHVAC
    'UCV5KIzspjE12UCOONVNsCnw': ('D', 'manufacturer (Soleus)'),  # SoleusDesign
    'UC1GMIsKba5cYnBWzI1ngoSw': ('D', "spray foam contractor whose About is about pushing 'the industry forward'; pro titles"),  # Spray Jones
    'UCjk87mntdBpQGLaJxhS3HBA': ('D', 'distributor (Standard Supply)'),  # Standard Supply
    'UCEijc4Yemonsqa-jp96nZvA': ('D', "About: 'HVAC LIFE! Training Troubleshooting'"),  # Stephen Rardon
    'UCcrs-w2r-S3VR7pe8t9DIew': ('contractor', 'Goettl (Arizona HVAC contractor) technician tips'),  # Stephen Shares HVAC Tips at Goettl
    'UCyRGxgEIXqduyp0ae0IO1tw': ('D', 'parts retailer (Stove & Grill Parts For Less)'),  # Stove & Grill Parts For Less
    'UCBB6HsvyQ3awb3BBqyZLPBQ': ('D', 'commercial service work (trade titles 18/30)'),  # Subcool HVAC
    'UCf7fJOIXkHsNE79RlLSvWnw': ('D', 'sales training organisation'),  # Success4others
    'UCRHmFBkYbze6ryOxECIuNDw': ('D', 'app company for technicians (SuperCool slide rule)'),  # SuperCool Slide Rule
    'UCT9cQmwV26zhwXH2cUOp6Eg': ('D', 'compliance and energy-services company for housing associations'),  # Sureserve
    'UC4-0mhhsVWFILK117k4wEDQ': ('contractor', 'San Diego HVAC company (phone number in About)'),  # Surf Bros HVAC
    'UC4I1sSqwTIKfcb9TFokkTwg': ('contractor', 'one-man service company (T&N Services LLC) posting its service calls'),  # T&N Services LLC.
    'UCuMyjTVlkM4xZ5z_eSyoB1w': ('not D', "individual; homeowner DIY titles ('What to Check Before You Call a Tech')"),  # Taddy Digest
    'UChqTAS8GVF1TM3pFyxvnPxg': ('not D', 'individual; tool reviews'),  # Talyn875
    'UCeslqDRHBPqBsb-C4FbEhFA': ('D', 'distributor channel (Temperature Equipment Corporation) for technicians'),  # Tec Tube
    'UCAdFjmRMULgz3aGszCKenFA': ('contractor', 'residential installer in the San Gabriel Valley documenting jobs'),  # The Air Conditioning Guy
    'UCXuC2KTVSVH7sS7bNkirRZQ': ('contractor', 'One Hour Heating and Air (Olathe) franchise; homeowner tips'),  # The Air Of Authority
    'UCGBhHzTWHeYR3rMTdy2gceA': ('contractor', 'one-man UK central-heating business; About: help people with central heating problems'),  # The Bearded Heating Co°
    'UCAfr7wP6i20uG4_DhSkCNfQ': ('contractor', "The General Heating & Air (Houston); About: 'helps homeowners understand'"),  # The General HVAC
    'UCrfmXRgZpJt_AlCG4RG4ZoA': ('not D', 'individual; homeowner tips'),  # The Heat and Air Guy
    'UCNOsm1Xq_tdrBXWyYGSSg6g': ('contractor', 'one-man service company in North New Jersey (phone number in About)'),  # The HVAC Hacker
    'UCFdB_qR3qdbNHBOzYrSBGdQ': ('not D', 'individual 25-year pro talking to homeowners (round 2 checker: A)'),  # The HVAC Veteran
    'UCQNax-Pjy7phzcy3X-gvgnA': ('contractor', 'Scottish renewables installer (heat pumps, solar)'),  # The Natural Energy Company
    'UCPJ4MHBwRVAtATykjXrEElQ': ('D', 'UK HVAC-industry show (engineers, business guests, manufacturer face-offs)'),  # The Outspoken Engineer 
    'UCB28a68UFEEqX2VI8kNSdXg': ('not D', "individual persona channel; 'techs don't want you to know' titles are homeowner insider framing, not trade"),  # The Technician’s Blacklist
    'UCJ8kHDNGalK8DDPUKUVOr6Q': ('D', 'apprentice / trade-career channel'),  # Tico
    'UCn6U4wQe3DPYFFp4kiy_z0w': ('D', 'sales and home-performance training for contractors'),  # Tim DeStasio HVAC
    'UC40oxncV1iBKl3svCW3R8Xw': ('contractor', "Tradesman Heating and Air Conditioning; About: 'challenges that homeowners are asking'"),  # Tradesman Mechanical Services Ltd.
    'UCU066MbiauN7De4fbU9iqng': ('not D', "individual; About: 'teach homeowners and up and coming HVAC technicians'"),  # Travis Poe
    'UC9cDwLvkUpIxCkgk5cznhGQ': ('contractor', 'True Blue Heating & Cooling, Tulsa contractor'),  # True Blue Heating & Cooling
    'UCsEbjz-3vvfTfkejhylJifA': ('D', 'certification test prep (EPA 608, NATE)'),  # TruePrep
    'UCWDa_bhiU5Vz-Xw487IQdZw': ('D', 'UK heating company; About: how to design, install and commission (trade)'),  # Urban Plumbers
    'UCXlG9qR4aQ5BtlhEN33N5GA': ('D', 'manufacturer (US Boiler)'),  # US Boiler
    'UCTDbUAjE9Ab_wwvuV7cgtvQ': ('not D', 'consumer-advocate channel (A)'),  # Vent Exposed
    'UCbSeBsLKPf6sLCiqlSrmVhw': ('contractor', 'Vese Heating & Cooling (company by name), homeowner titles'),  # Vese Heating & Cooling
    'UCj5vlWLsADBKBbFb5PxD1vg': ('not D', 'individual technician vlog'),  # Victor of HVAC
    'UClaWcomJXXcevL8xx6OgmOA': ('contractor', 'Victory Heating & Air Services (LLC); service calls'),  # Victory Heating & Air Services
    'UCLs9csMJsP-4Y4cJcd2M1iA': ('not D', 'individual persona channel'),  # Walt Brennan
    'UCNRXHwAfOsAANg5tx4r-G2A': ('D', 'boiler rental / sales / service company, industry content'),  # WARE Boilers
    'UCtcIJto3pbwTywD9PtJVgQw': ('D', 'manufacturer (WarmlyYours)'),  # WarmlyYours
    'UCm3nG4rxdX28gXcMxoC5rBg': ('D', 'HVAC sales training'),  # Weldon Long
    'UCVQkjsO0NwvsljBsJbTwp_A': ('contractor', 'Willman Air, NE Florida residential contractor'),  # Willman Air Heating and Air Conditioning
    'UCqUy9i3U1SoRRMHxveUO6lw': ('D', 'manufacturer (Worcester Bosch)'),  # Worcester Bosch
    'UCX9qUeV57Z7gqX1uwp8XOqg': ('D', "About: 'your guide to the trade'"),  # WW HVAC
    'UCQyTPsQjdotmBQxVsM0sOtQ': ('D', 'installer day-in-the-life, trade podcasts, AHR show'),  # Xavierhvac
    'UCOtjEgHlsAxG0YNzaSVIOgw': ('contractor', 'Yarbrough & Sons, OKC contractor; homeowner titles'),  # Yarbrough & Sons Heating, Cooling & Plumbing
    'UC_ggVVZ08PW9v9KMMHlLPGg': ('not D', 'individual technician vlog'),  # Yung HVAC
    'UCZMrx-G84K5PIynOtA47pAw': ('D', 'engineering / HVAC training (India)'),  # Zebra Learnings
    'UCu67ms6tiDFP4GZ0GoCJ2og': ('D', 'manufacturer (Zero Breeze)'),  # ZERO BREEZE
    'UCR0EfsRZIwA5TVDaQbTqwEQ': ('D', 'power-plant / industrial engineering education'),  # شادى غازى
}
# Clear-error fixes found by the hand-check (channel id -> (tier, reason)). Logged in channels.md.
HAND_FIXES = {}


# ---------------------------------------------------------------------------------------------------------------
# 7. Per-channel build.
# ---------------------------------------------------------------------------------------------------------------
def build_channel(d, mrow, about, ctype):
    cid = d.get("id") or d.get("key")
    sorts = d.get("sorts") or {}
    lat_chip, lat_init = sorts.get("Latest"), sorts.get("Latest_initialpage") or []
    latest = lat_chip if (lat_chip is not None and len(lat_chip) >= len(lat_init)) else lat_init
    latest_src = "Latest" if latest is lat_chip else "Latest_initialpage"
    popular, oldest = sorts.get("Popular"), sorts.get("Oldest")
    vids = OrderedDict()  # id -> record, union of sorts
    for sname in ("Latest", "Latest_initialpage", "Popular", "Oldest"):
        for it in (sorts.get(sname) or []):
            vid = it.get("id")
            if not vid:
                continue
            if vid not in vids:
                a = age_of(it.get("meta"))
                vids[vid] = {"id": vid, "title": it.get("title") or "", "dur_text": it.get("dur"),
                             "dur": parse_dur(it.get("dur")), "views": it.get("views_tab"),
                             "age": a, "sorts": [sname]}
            elif sname not in vids[vid]["sorts"]:
                vids[vid]["sorts"].append(sname)
    for v in vids.values():
        v["long"] = v["dur"] is not None and v["dur"] >= 300
        v["hvac"] = hvac_title(v["title"])
        v["lanes"] = lane_words(v["title"])
        v["trade"] = trade_title(v["title"])
    # recency order: the Latest list (contiguous newest uploads)
    lat_ids = [it["id"] for it in latest if it.get("id")]
    lat_long = [vids[i] for i in lat_ids if vids[i]["long"] and vids[i]["age"]]
    n_videos_text = parse_count(d.get("videos"))
    latest_complete = n_videos_text is not None and len(lat_ids) >= n_videos_text
    oldest_latest_age = vids[lat_ids[-1]]["age"] if lat_ids and vids[lat_ids[-1]]["age"] else None
    flags = []
    # --- HVAC share of the latest 30 long-form (check-master.md step 2)
    basis = "latest 30 long-form"
    sample = lat_long[:30]
    if len(lat_long) == 0 and lat_ids:
        sample = [vids[i] for i in lat_ids[:30]]
        basis = "latest 30 of any length (no long-form in the Latest list)"
        flags.append("ANY-LENGTH")
    elif len(lat_long) < 10:
        top = (popular or [])[:10]
        pool = list(lat_long) + [vids[t["id"]] for t in top if t.get("id") and vids[t["id"]] not in lat_long]
        sample = pool
        basis = f"LOW-N: {len(lat_long)} long-form pooled with the Popular top 10"
        flags.append("LOW-N")
    n_s = len(sample)
    h_s = sum(1 for v in sample if v["hvac"])
    share = (h_s / n_s) if n_s else None
    lane_hits = sum(1 for v in sample if lane_c_word(v["lanes"]))
    lane_share = (lane_hits / n_s) if n_s else None
    trade_hits = sum(1 for v in sample if v["trade"])
    trade_share = (trade_hits / n_s) if n_s else None
    lane_counts = Counter(l for v in sample for l in v["lanes"])
    lane_tags = [l for l, c in lane_counts.most_common() if c >= 3 and n_s and c / n_s >= 0.10]
    # newest 10 long-form (DRIFT)
    new10 = lat_long[:10]
    h_new10 = sum(1 for v in new10 if v["hvac"])
    # top 10 popular (any length, as the tab shows); fallback = 10 most-viewed collected
    if popular:
        top10 = [vids[t["id"]] for t in popular[:10] if t.get("id")]
        top10_basis = "Popular sort top 10 (any length)"
    else:
        top10 = sorted([v for v in vids.values() if v["views"] is not None], key=lambda v: -v["views"])[:10]
        top10_basis = "no Popular sort: 10 most-viewed of the pulled videos"
    h_top10 = sum(1 for v in top10 if v["hvac"])
    # --- D flags
    name = d.get("channel") or (mrow or {}).get("name") or ""
    src_about, ab = about.get(cid, (None, {}))
    desc = (ab.get("DESC") or "")
    desc_n = norm(desc)
    name_n = norm(name)
    f_name = bool(NAME_COMPANY.search(name_n))
    f_about_company = bool(ABOUT_COMPANY.search(desc_n))
    f_about_trade = bool(ABOUT_TRADE.search(desc_n))
    f_trade_titles = trade_share is not None and trade_share >= 0.30
    stored = (mrow or {}).get("tier", "")
    # automatic D reading: company (name flag + About company markers), or trade titles confirmed by About trade
    # words, or the stored D (90% right in check-master) with any supporting flag.
    auto_d = ((f_name and f_about_company) or (f_trade_titles and (f_about_trade or f_name))
              or (stored == "D" and (f_name or f_about_company or f_trade_titles or f_about_trade)))
    d_basis = []
    if f_name: d_basis.append("name")
    if f_about_company: d_basis.append("About company words")
    if f_about_trade: d_basis.append("About trade words")
    if f_trade_titles: d_basis.append(f"trade titles {trade_hits}/{n_s}")
    if stored == "D": d_basis.append("stored D")
    is_contractor = bool(CONTRACTOR.search(name_n + " " + desc_n)) and not BRAND.search(name_n)
    manual = D_CONFIRM.get(cid)
    if manual:
        dec = manual[0]
        is_d = dec in ("D", "contractor")
        if dec == "contractor":
            is_contractor = True
        elif dec == "D":
            is_contractor = False
        d_note = f"manual: {dec} ({manual[1]})"
    else:
        is_d = auto_d
        d_note = "auto"
    # --- tier rule (check-master.md, with the operator's 2026-10-26 defaults)
    lane_c = lane_share is not None and lane_share >= 0.30
    contractor_a = is_d and is_contractor and share is not None and share >= 0.50 and (
        (manual and manual[0] == "contractor") or (trade_share or 0) < 0.30)
    if share is None:
        tier, why = "NO-DATA", "no videos in the pull"
    elif is_d and share < 0.10:
        # census adjustment (2026-10-26): a company / trade channel with under 10% HVAC titles is off-niche (X),
        # not D (round 2 had Google Help, Made by Google and Lowe's in D).
        tier, why = "X", f"company / trade channel, HVAC {h_s}/{n_s} (off-niche)"
        flags.append("COMPANY")
        if top10 and h_top10 / len(top10) >= 0.30:
            flags.append("LEGACY")
            why += f"; top 10 HVAC {h_top10}/{len(top10)}"
    elif is_d and not contractor_a:
        tier, why = "D", "trade or company (" + "; ".join(d_basis) + ")"
    elif share >= 0.50:
        tier, why = "A", f"HVAC {h_s}/{n_s}"
        if is_d:
            flags.append("contractor")
            why += "; contractor teaching homeowners (operator default 2026-10-26)"
    elif share >= 0.10:
        tier = "C" if lane_c else "B"
        why = f"HVAC {h_s}/{n_s}; lane words {lane_hits}/{n_s}"
    else:
        tier, why = "X", f"HVAC {h_s}/{n_s}"
        if top10 and h_top10 / len(top10) >= 0.30:
            flags.append("LEGACY")
            why += f"; top 10 HVAC {h_top10}/{len(top10)}"
    if tier == "A" and len(new10) >= 10 and h_new10 <= 2:
        flags.append("DRIFT")
    if cid in HAND_FIXES:
        tier, fx = HAND_FIXES[cid][0], HAND_FIXES[cid][1]
        why += f"; HAND FIX: {fx}"
        flags.append("HAND-FIX")
    if lane_tags and tier == "A":
        why += "; lane " + "/".join(lane_tags)
    # Main session, 2026-10-26: DIY stove-building and "free energy" craft channels are not Roger's competitors;
    # keep them visible in the off-grid lane (C), not A. To be confirmed by the operator in the round 7 report.
    if tier == "A" and "diy-stove-craft" in lane_tags:
        tier = "C"
        why += "; moved A->C: diy-stove-craft (main session default 2026-10-26)"
        flags.append("STOVE-CRAFT")
    # --- baseline (labels.md section 6), from the Latest list only (an unbiased recent window)
    l12 = [v for v in lat_long if within(v["age"][1], v["age"][2], 365) and v["views"] is not None]
    capped = (not latest_complete) and oldest_latest_age is not None and within(oldest_latest_age[1], oldest_latest_age[2], 365)
    if len(l12) >= 10:
        base_set = l12
        rule = "12M" + (" (Latest list ends inside 12 months: latest %d uploads only)" % len(lat_ids) if capped else "")
    else:
        base_set = [v for v in lat_long if v["views"] is not None][:30]
        rule = f"last30 (only {len(l12)} long-form in 12 months)"
    baseline = median([v["views"] for v in base_set])
    for v in vids.values():
        v["mult"] = (v["views"] / baseline) if (baseline and v["views"] is not None and v["long"]) else None
    share2x = (sum(1 for v in base_set if v["mult"] is not None and v["mult"] >= 2) / len(base_set)) if base_set and baseline else None
    longs = [v for v in vids.values() if v["long"]]
    n2x_all = sum(1 for v in longs if v["mult"] is not None and v["mult"] >= 2)
    # --- upload counts (approx, from age text; floors when the Latest list is capped)
    c30 = sum(1 for v in lat_long if within(v["age"][1], v["age"][2], 30))
    c90 = sum(1 for v in lat_long if within(v["age"][1], v["age"][2], 90))
    c365 = len([v for v in lat_long if within(v["age"][1], v["age"][2], 365)])
    floor = lambda w: (not latest_complete) and oldest_latest_age is not None and within(oldest_latest_age[1], oldest_latest_age[2], w)
    # --- top 3 long-form by views (all sorts)
    top3 = sorted([v for v in longs if v["views"] is not None], key=lambda v: -v["views"])[:3]
    # --- sub-niches (all HVAC long-form pulled)
    sn = Counter(subniche(v["title"]) for v in longs if v["hvac"])
    # --- NEW_12M
    joined = (mrow or {}).get("joined", "")
    first_age, first_basis = None, ""
    if oldest:
        ol = [vids[t["id"]] for t in oldest if t.get("id") and vids[t["id"]]["long"] and vids[t["id"]]["age"]]
        if ol:
            first_age, first_basis = ol[0]["age"], "Oldest sort"
    elif latest_complete and lat_long:
        first_age, first_basis = lat_long[-1]["age"], "Latest list (complete)"
    new_reasons = []
    try:
        jd = date.fromisoformat(joined)
        if jd >= NEW_SINCE:
            new_reasons.append(f"joined {joined}")
    except ValueError:
        jd = None
    if first_age and within(first_age[1], first_age[2], 365):
        new_reasons.append(f"first long-form upload '{first_age[0]}' ({first_basis})")
    if new_reasons:
        new12, new_basis = "yes", "; ".join(new_reasons)
    elif jd is None and not first_age:
        new12, new_basis = "not found", "no joined date; first upload not found"
    else:
        bits = []
        if jd: bits.append(f"joined {joined}")
        if first_age: bits.append(f"first long-form '{first_age[0]}' ({first_basis})")
        else: bits.append("first long-form upload not found (no Oldest sort, Latest list incomplete)")
        new12, new_basis = "no", "; ".join(bits)
    # --- subs, views, etc.
    subs = parse_count(d.get("subs"))
    subs_src = "census Videos tab header 2026-10-26 (rounded)"
    if subs is None:
        subs = parse_count((mrow or {}).get("subs"))
        subs_src = ("master CSV: " + (mrow or {}).get("subs_source", "")) if subs is not None else "not found"
    vcount = n_videos_text
    vcount_src = "census Videos tab header 2026-10-26"
    if vcount is None:
        vcount = parse_count((mrow or {}).get("video_count"))
        vcount_src = ("master CSV: " + (mrow or {}).get("video_count_source", "")) if vcount is not None else "not found"
    m = mrow or {}
    # type carried forward
    if ctype:
        typ, typ_src = ctype, "round 2 checker, 3 recent thumbnails, 2026-10-24"
    elif m.get("type") and m.get("type") != "not checked":
        typ = m["type"]
        prov = "provisional" in (m.get("type_detail", "") + m.get("type_source", "")) or m.get("type_source") in ("name", "")
        typ_src = (m.get("type_source") or "master CSV") + (" (provisional)" if prov else "")
        if m.get("type_source") == "name":
            typ_src = "name (brand by channel name; provisional)"
    else:
        typ, typ_src = "", "not yet checked (round 3 type helper)"
    row = OrderedDict([
        ("tier", tier), ("old_tier", stored), ("tier_basis", why), ("flags", ";".join(flags)),
        ("name", name), ("handle", (m.get("handle") or "")), ("channel_id", cid),
        ("link", f"https://www.youtube.com/channel/{cid}"),
        ("hvac_latest30", f"{h_s}/{n_s}"), ("hvac_share_latest30", "" if share is None else round(share, 3)),
        ("hvac_share_basis", basis), ("hvac_newest10", f"{h_new10}/{len(new10)}"),
        ("hvac_top10", f"{h_top10}/{len(top10)}"), ("top10_basis", top10_basis),
        ("lane_word_titles_latest30", f"{lane_hits}/{n_s}"), ("lane_tags", ";".join(lane_tags)),
        ("trade_word_titles_latest30", f"{trade_hits}/{n_s}"), ("d_flags", ";".join(d_basis)), ("d_decision", d_note),
        ("subs", subs if subs is not None else "not found"), ("subs_source", subs_src),
        ("total_views", m.get("total_views") or "not found"), ("total_views_source", m.get("total_views_source", "") or ""),
        ("joined", joined or "not found"), ("joined_source", m.get("joined_source", "") or ""),
        ("country", m.get("country") or "not found"),
        ("video_count", vcount if vcount is not None else "not found"), ("video_count_source", vcount_src),
        ("videos_pulled", len(vids)), ("longform_pulled", len(longs)), ("latest_list", f"{latest_src} {len(lat_ids)}"),
        ("latest_list_complete", "yes" if latest_complete else "no"),
        ("latest_list_oldest_age", oldest_latest_age[0] if oldest_latest_age else ""),
        ("uploads_30d", f"{c30}{'+' if floor(30) else ''}"), ("uploads_90d", f"{c90}{'+' if floor(90) else ''}"),
        ("uploads_365d", f"{c365}{'+' if floor(365) else ''}"),
        ("pace_per_month_90d", round(c90 / 3, 1)),
        ("baseline", "" if baseline is None else int(round(baseline))), ("baseline_rule", rule), ("baseline_n", len(base_set)),
        ("share_2x_baseline_set", "" if share2x is None else round(share2x, 3)), ("n_2x_all_longform_pulled", n2x_all),
        ("nexlev_outlier", m.get("nexlev_outlier") or "not found"),
    ])
    for i in range(3):
        v = top3[i] if i < len(top3) else None
        row[f"top{i+1}_title"] = v["title"] if v else ""
        row[f"top{i+1}_id"] = v["id"] if v else ""
        row[f"top{i+1}_views"] = v["views"] if v else ""
        row[f"top{i+1}_age"] = v["age"][0] if v and v["age"] else ""
    row["hvac_longform_pulled"] = sum(1 for v in longs if v["hvac"])
    row["main_subniches"] = "; ".join(f"{k} ({c})" for k, c in sn.most_common(3))
    row["new_12m"], row["new_12m_basis"] = new12, new_basis
    row["type"], row["type_source"] = typ, typ_src
    row["sells"] = "to fill (round 3 helper)"
    row["about_source"] = src_about or "not found"
    row["pulled"] = d.get("pulled", "")
    vrows = []
    for v in longs:
        vrows.append(OrderedDict([
            ("video_id", v["id"]), ("channel_id", cid), ("channel", name), ("title", v["title"]),
            ("views_tab", "" if v["views"] is None else v["views"]), ("dur_seconds", v["dur"]),
            ("age_text", v["age"][0] if v["age"] else ""),
            ("approx_date", approx_date(v["age"][1], v["age"][2]).isoformat() if v["age"] else ""),
            ("is_hvac", "yes" if v["hvac"] else "no"), ("subniche", subniche(v["title"]) if v["hvac"] else ""),
            ("lane_words", ";".join(v["lanes"])), ("multiple", "" if v["mult"] is None else round(v["mult"], 2)),
            ("baseline", "" if baseline is None else int(round(baseline))), ("baseline_rule", rule.split(" ")[0]),
            ("sorts", ";".join(v["sorts"])),
        ]))
    detail = {"sample": [(v["id"], v["title"], v["dur_text"], v["hvac"], v["lanes"], v["trade"]) for v in sample],
              "top10": [(v["id"], v["title"], v["hvac"]) for v in top10], "desc": desc[:400], "name": name,
              "auto_d": auto_d, "is_contractor": is_contractor, "share": share, "stored": stored}
    return row, vrows, detail


def load_census():
    out = []
    for f in sorted(glob.glob(os.path.join(CENSUS_DIR, "UC*.json"))):
        out.append(json.load(open(f, encoding="utf-8")))
    return out


def run_all():
    master, about, ctypes = load_master(), load_about(), load_checker_types()
    rows, vrows, details = [], [], {}
    for d in load_census():
        cid = d.get("id") or d.get("key")
        r, vr, det = build_channel(d, master.get(cid), about, ctypes.get(cid))
        rows.append(r); vrows.extend(vr); details[cid] = det
    return rows, vrows, details, master


def handcheck_sample(rows):
    ids = sorted(r["channel_id"] for r in rows)
    rnd = random.Random(2610)
    return rnd.sample(ids, 40)


# ---------------------------------------------------------------------------------------------------------------
# 8. Outputs.
# ---------------------------------------------------------------------------------------------------------------
def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def subs_key(r):
    return r["subs"] if isinstance(r["subs"], int) else -1


def md_escape(s):
    return str(s).replace("|", "/").replace("\n", " ")


def write_md(rows, moves, hc, build_info):
    tiers = Counter(r["tier"] for r in rows)
    L = []
    L.append("# HVAC channel census (deliverable 1, in progress)\n")
    L.append("Built 2026-10-26 by `data/tools/census_build.py` (round 3 census-build helper) from the Videos-tab pulls of "
             "2026-10-26 (`data/raw/census-2026-10-26/`, logged out, Latest / Popular / Oldest sorts, up to ~120 videos "
             "each). Nothing committed or pushed. **Not yet re-checked by a second helper (working rule 3).** "
             "The `type` and `sells` columns are being filled by other round 3 helpers; `type` here is carried forward "
             "from round 2 where it existed (source in the CSV, provisional where marked).\n")
    L.append("Full tables: `data/raw/census-channels-2026-10-26.csv` (every pulled channel, X included), "
             "`data/raw/census-videos-2026-10-26.csv` (every long-form video), `channels.csv` (tiers A-D).\n")
    L.append("## Method\n")
    L.append("- **Long-form** = tab duration 5:00 or more. Videos = the union of the Latest, Popular and Oldest sorts "
             "(the pull caps each at about 120). Views are the tab's **rounded** text (\"24K\"); exact counts come later "
             "for the top 100 and winners. Upload dates are **approximate** (pull date minus the midpoint of the age "
             "text's range, e.g. \"3mo ago\" = about 3.5 months before 2026-10-26).\n"
             "- **HVAC title mark** (a reading by keyword rule): `is_hvac` from `data/tools/autocomplete.py` plus census "
             "fixes (word lists in `census_build.py`: `STRIP`, `CENSUS_EXCLUDE`, `DEPENDENT`/`WARMTH`, `CENSUS_STRONG`). "
             f"Calibrated on the round 2 checker's 2,893 hand-marked titles: {build_info['calib']}.\n"
             "- **Tier rule** (`round2/check-master.md`, applied by script): D first for trade or company channels "
             "(flagged by name / About / title words, confirmed by About text; see below); A if 50%+ of the latest 30 "
             "long-form titles are HVAC; B 10-49%, C instead of B when 30%+ of those titles carry an adjacent-lane word; "
             "X under 10% (LEGACY when 30%+ of the Popular top 10 is HVAC). Fewer than 10 long-form: pooled with the "
             "Popular top 10 (LOW-N). DRIFT = an A whose newest 10 long-form hold 2 or fewer HVAC titles (flagged, kept "
             "A, per the brief for this build). Operator defaults of 2026-10-26: contractor channels teaching homeowners "
             "= A marked `contractor`; outage / off-grid channels that are mostly HVAC = A with their lane tag.\n"
             "- **Lane tags**: a lane whose words appear in 3+ (and 10%+) of the latest 30 long-form titles.\n"
             "- **Baseline** (labels.md section 6): median tab views of the channel's long-form uploads in the last 12 "
             "months (age text up to \"11mo ago\"), taken from the Latest list only; if fewer than 10, the median of "
             "its last 30 long-form. Multiple = views / baseline. Share at 2x+ is within the baseline set.\n"
             "- **Uploads in 30 / 90 / 365 days** are approximate (age text); a `+` means the Latest list (about 120 "
             "uploads) ends inside that window, so the count is a floor.\n"
             "- **Sub-niches**: each HVAC long-form title mapped to a `labels.md` sub-niche by keyword rule "
             "(`SUBNICHE_RULES`); top 3 by count (a reading).\n"
             "- **NEW_12M**: joined on or after 2025-10-26 (About date, master CSV) or first long-form upload "
             "\"11mo ago\" or newer (Oldest sort). A pivot that restarted in the window is not detected here.\n")
    L.append("## Counts by new tier\n")
    L.append("| New tier | Channels | of which flags |\n|---|---:|---|")
    for t in ("A", "B", "C", "D", "X", "NO-DATA"):
        if tiers.get(t):
            fl = Counter(f for r in rows if r["tier"] == t for f in r["flags"].split(";") if f)
            L.append(f"| {t} | {tiers[t]:,} | " + ", ".join(f"{k} {v}" for k, v in fl.most_common()) + " |")
    L.append(f"| **All pulled** | **{len(rows):,}** | |\n")
    L.append("**How tiers moved from round 2** (rows = round 2 tier, columns = new tier):\n")
    cols = ["A", "B", "C", "D", "X", "NO-DATA"]
    L.append("| Round 2 \\ new | " + " | ".join(cols) + " | Unchanged | Total |")
    L.append("|---|" + "---:|" * (len(cols) + 2))
    for o in ("A", "B", "C", "D"):
        rr = [r for r in rows if r["old_tier"] == o]
        L.append(f"| {o} | " + " | ".join(str(sum(1 for r in rr if r['tier'] == c)) for c in cols)
                 + f" | {sum(1 for r in rr if r['tier'] == o)} | {len(rr)} |")
    L.append("")
    L.append("**Census list:** tiers A-D after re-tiering = "
             f"{sum(tiers[t] for t in 'ABCD'):,} channels (round 2: 1,122). The round 2 X tier (819 channels) was not pulled "
             "and is not re-tiered here.\n")
    L.append(build_info["d_text"])
    L.append(build_info["hc_text"])
    leg = sorted([r for r in rows if "LEGACY" in r["flags"]], key=lambda r: -subs_key(r))
    L.append(f"## LEGACY (tier X, 30%+ of the Popular top 10 is HVAC: {len(leg)} channels)\n")
    L.append("Kept for outlier mining, not as competitors (`check-master.md` step 5).\n")
    L.append("| Channel | Subs | HVAC latest 30 | HVAC top 10 | Top video (views) |\n|---|---:|---|---|---|")
    for r in leg:
        top = f"\"{md_escape(r['top1_title'])[:70]}\" ({r['top1_id']}, {fnum(r['top1_views'])})" if r["top1_id"] else "not found"
        L.append(f"| [{md_escape(r['name'])}]({r['link']}) | {fnum(r['subs'])} | {r['hvac_latest30']} | {r['hvac_top10']} | {top} |")
    L.append("")
    dr = [r for r in rows if "DRIFT" in r["flags"]]
    L.append(f"**DRIFT** (tier A whose newest 10 long-form hold 2 or fewer HVAC titles; flagged, kept A): {len(dr)}: "
             + ("; ".join(f"{r['name']} (newest 10: {r['hvac_newest10']}, latest 30: {r['hvac_latest30']})" for r in dr) or "none") + ".\n")
    keycols = ("| # | Channel | Subs | HVAC latest 30 | Lane | Flags | Baseline (rule, n) | Uploads 90 d | "
               "Top video (views) | Main sub-niches | NEW_12M | Type (carried, provisional) |")
    for t in ("A", "B", "C", "D"):
        rr = sorted([r for r in rows if r["tier"] == t], key=lambda r: -subs_key(r))
        L.append(f"## Tier {t} ({len(rr):,} channels, by subscribers)\n")
        L.append("Subs = Videos-tab header 2026-10-26 (rounded) unless the CSV says otherwise. Type and sells are being "
                 "filled by round 3 helpers. Tier, HVAC marks, lanes and sub-niches are readings by rule.\n")
        L.append(keycols)
        L.append("|---:|---|---:|---|---|---|---|---:|---|---|---|---|")
        for i, r in enumerate(rr, 1):
            h = f"[@{r['handle'].lstrip('@')}]({r['link']})" if r["handle"] else f"[link]({r['link']})"
            top = (f"\"{md_escape(r['top1_title'])[:70]}\" ({r['top1_id']}, {fnum(r['top1_views'])})"
                   if r["top1_id"] else "not found")
            base = f"{fnum(r['baseline'])} ({r['baseline_rule'].split(' ')[0]}, n={r['baseline_n']})" if r["baseline"] != "" else "not found"
            L.append(f"| {i} | {md_escape(r['name'])} {h} | {fnum(r['subs'])} | {r['hvac_latest30']} "
                     f"({'' if r['hvac_share_latest30'] == '' else round(100 * r['hvac_share_latest30'])}%) | "
                     f"{r['lane_tags'] or '-'} | {r['flags'] or '-'} | {base} | {r['uploads_90d']} | {top} | "
                     f"{md_escape(r['main_subniches']) or '-'} | {r['new_12m']} | {r['type'] or '-'} |")
        L.append("")
    open(os.path.join(STUDY, "channels.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")


def main():
    rows, vrows, details, master = run_all()
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        for cid in handcheck_sample(rows):
            r = next(x for x in rows if x["channel_id"] == cid)
            det = details[cid]
            print(f"\n=== {cid} | {r['name']} | rule {r['tier']} ({r['tier_basis']}) | old {r['old_tier']} | "
                  f"flags {r['flags']} | subs {r['subs']} | top10 {r['hvac_top10']}")
            print("  ABOUT:", det["desc"][:220].replace("\n", " "))
            for vid, t, dur, h, lanes, tr in det["sample"]:
                print(f"  {'H' if h else '.'}{'T' if tr else ' '}{'L' if lanes else ' '} {dur} {t[:95]}")
            print("  TOP10:", " || ".join(("H " if h else "") + t[:50] for _, t, h in det["top10"]))
        return
    if len(sys.argv) > 1 and sys.argv[1] == "dreview":
        for cid, det in sorted(details.items(), key=lambda kv: kv[1]["name"].lower()):
            r = next(x for x in rows if x["channel_id"] == cid)
            if r["d_flags"] and (det["auto_d"] != (det["stored"] == "D") or r["tier"] == "A" and "contractor" in r["flags"]
                                 or (det["auto_d"] and (det["share"] or 0) >= 0.5)):
                print(f"\n{cid} | {det['name']} | stored {det['stored']} | auto_d {det['auto_d']} | contractor {det['is_contractor']} "
                      f"| now {r['tier']} | HVAC {r['hvac_latest30']} | trade {r['trade_word_titles_latest30']} | {r['d_flags']}")
                print("  ABOUT:", det["desc"][:260].replace("\n", " "))
                print("  T:", " || ".join(t[:60] for _, t, *_ in det["sample"][:6]))
        return
    # hand-check agreement
    hc_path = os.path.join(RAW, "census-handcheck-2026-10-26.csv")
    hc = []
    if os.path.exists(hc_path):
        hc = list(csv.DictReader(open(hc_path, encoding="utf-8")))
    calib = calibrate()
    info = {"calib": calib["text"]}
    # D review text
    nd = Counter(r["d_decision"].split(":")[0] for r in rows if r["tier"] == "D" or "contractor" in r["flags"])
    info["d_text"] = ("## The D check\n\nD candidates are flagged by words (channel name, About text, or 30%+ trade "
                      "words in the latest 30 titles) and confirmed by About-text company or trade markers (rule in "
                      "`census_build.py`: `NAME_COMPANY`, `ABOUT_COMPANY`, `ABOUT_TRADE`, `TRADE`). Where the automatic "
                      "reading and the round 2 tier disagreed, or a flagged company is mostly homeowner HVAC, I read the "
                      f"About text and titles and recorded a decision with its reason (`D_CONFIRM`, {len(D_CONFIRM)} "
                      "channels). Contractor = a company serving local homeowners (heating-and-air companies, "
                      "mechanical contractors); brands, retailers, parts sellers, trade schools and trade shows stay D "
                      "even when their videos are homeowner HVAC.\n")
    if hc:
        agree_b = sum(1 for h in hc if h["my_tier"] == h["rule_tier_before_fixes"])
        cur = {r["channel_id"]: r["tier"] for r in rows}
        agree_a = sum(1 for h in hc if h["my_tier"] == cur.get(h["channel_id"]))
        info["hc_text"] = ("## Hand-check (40 random channels, `random.Random(2610).sample` of the sorted channel IDs)\n\n"
                           "I read each sampled channel's latest 30 long-form titles (and its Popular top 10) and gave my own "
                           "tier (a reading). **Agreement with the rule: " + f"{agree_b} of {len(hc)} before fixes, "
                           f"{agree_a} of {len(hc)} after** (the rule tiers below are recomputed on every run). "
                           "Fixes made, all word-list misses (no threshold changed): bath / exhaust / attic fans and "
                           "air-sealing words (blower door, energy audit) counted as HVAC, as `check-master.md`'s scope says; "
                           "\"A/C units\" and \"garage at 70°F\" patterns; lane words \"waste oil\", grandma / grandpa / "
                           "depression-era / old-fashioned, \"cost pennies\", and \"7 Best ... 2026\" product lists. "
                           "Left as the rule has them (borderline B vs C or X, none touching tier A): Secret Sparks, NOBOX7, "
                           "Halden Row (LOW-N pooling, as check-master.md found with Live Free), RomanUrsuHack. "
                           "Rows: `data/raw/census-handcheck-2026-10-26.csv`.\n\n" + build_hc_table(hc, cur) + "\n")
        info["hc_agree"] = f"{agree_b}/{len(hc)} before fixes, {agree_a}/{len(hc)} after"
    else:
        info["hc_text"] = "## Hand-check\n\nnot done yet.\n"
    write_csv(os.path.join(RAW, "census-channels-2026-10-26.csv"), rows)
    write_csv(os.path.join(RAW, "census-videos-2026-10-26.csv"), vrows)
    write_csv(os.path.join(STUDY, "channels.csv"), [r for r in rows if r["tier"] in ("A", "B", "C", "D")])
    moves = Counter((r["old_tier"], r["tier"]) for r in rows)
    write_md(rows, moves, hc, info)
    out = {"built": "2026-10-26", "by": "round 3 census-build helper", "script": "data/tools/census_build.py",
           "channels": len(rows), "videos_longform": len(vrows),
           "tiers": Counter(r["tier"] for r in rows), "moves": {f"{a}->{b}": n for (a, b), n in sorted(moves.items())},
           "flags": Counter(f for r in rows for f in r["flags"].split(";") if f),
           "hvac_rule_calibration": calib, "handcheck_sample": handcheck_sample(rows),
           "handcheck_agreement": info.get("hc_agree", "not done"),
           "d_confirm": {k: list(v) for k, v in D_CONFIRM.items()}, "hand_fixes": {k: list(v) for k, v in HAND_FIXES.items()},
           "word_lists": {"STRIP": STRIP.pattern, "CENSUS_EXCLUDE": CENSUS_EXCLUDE.pattern, "DEPENDENT": DEPENDENT.pattern,
                          "WARMTH": WARMTH.pattern, "CENSUS_STRONG": CENSUS_STRONG.pattern, "LANES": LANES,
                          "TRADE": TRADE.pattern, "NAME_COMPANY": NAME_COMPANY.pattern, "ABOUT_COMPANY": ABOUT_COMPANY.pattern,
                          "ABOUT_TRADE": ABOUT_TRADE.pattern, "CONTRACTOR": CONTRACTOR.pattern, "BRAND": BRAND.pattern,
                          "SUBNICHE_RULES": SUBNICHE_RULES}}
    json.dump(out, open(os.path.join(RAW, "census-build-2026-10-26.json"), "w"), indent=1, default=str)
    print(json.dumps({k: out[k] for k in ("channels", "videos_longform", "tiers", "flags", "handcheck_agreement")}, default=str))


def build_hc_table(hc, cur):
    L = ["| # | Channel | Round 2 tier | HVAC latest 30 (rule, now) | Rule tier before fixes | Rule tier now | My tier | Agree now | My note |",
         "|---:|---|:---:|---|:---:|:---:|:---:|:---:|---|"]
    for i, h in enumerate(hc, 1):
        now = cur.get(h["channel_id"], "")
        ok = "yes" if h["my_tier"] == now else "**no**"
        L.append(f"| {i} | {md_escape(h['name'])} | {h['old_tier']} | {h['hvac_latest30']} | {h['rule_tier_before_fixes']} | {now} | "
                 f"{h['my_tier']} | {ok} | {md_escape(h['note'])} |")
    return "\n".join(L)


def calibrate():
    """Census HVAC rule vs the round 2 checker's hand marks (check-master-2026-10-24.json)."""
    d = json.load(open(os.path.join(RAW, "check-master-2026-10-24.json")))
    n = ok = ok_r2 = fp = fn = 0
    for c in d["channels"]:
        for key in ("latest_longform_30", "popular_top10", "latest_any_length_30", "top10_fallback"):
            for v in (c.get(key) or []):
                if "hvac_checker" not in v:
                    continue
                n += 1
                p = hvac_title(v["title"])
                ok += p == v["hvac_checker"]
                ok_r2 += _is_hvac_r2(norm(v["title"])) == v["hvac_checker"]
                fp += p and not v["hvac_checker"]
                fn += (not p) and v["hvac_checker"]
    return {"titles": n, "agree_census_rule": ok, "agree_round2_is_hvac": ok_r2, "false_pos": fp, "false_neg": fn,
            "text": f"the census rule agrees on {ok:,} of {n:,} ({100 * ok / n:.1f}%; round 2 `is_hvac` alone "
                    f"{ok_r2:,}, {100 * ok_r2 / n:.1f}%); {fp} marked HVAC that the checker did not, {fn} missed. "
                    "This is the set the fixes were written from, so it is not an independent test (the 40-channel "
                    "hand-check below is)"}


if __name__ == "__main__":
    main()
