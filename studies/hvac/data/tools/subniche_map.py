#!/usr/bin/env python3
"""Round 3 sub-niche map (HVAC study, deliverable 3), written 2026-10-26 by the round 3 sub-niche helper.

Rerunnable. Reads only local files; no network, no web searches.

Inputs (studies/hvac/data/raw/):
  census-videos-2026-10-26.csv     every long-form video of every pulled channel (census_build.py)
  census-channels-2026-10-26.csv   tiers, baselines, provisional type (round 2 carry-forward)
  census-types-{A,B,C}-2026-10-26.csv   (optional) channel types from the round 3 type helpers; used when present,
                                   in preference to the provisional type in the channels CSV.

Outputs:
  raw/subniches-2026-10-26.csv     one row per HVAC long-form video (is_hvac = yes, all tiers incl. X), with the
                                   primary sub-niche, its labels.md parent, scope and every rule that matched.
  ../../subniches.md               deliverable 3: the method, the tables, the splits, the biggest videos, the hand-check.

Usage: python3 -I subniche_map.py           (build both outputs)
       python3 -I subniche_map.py sample    (print the seed-2611 hand-check sample with the rule's tags)
       python3 -I subniche_map.py unmapped  (print 200 random unmapped A-C titles, to improve the rules)

Every sub-niche here is a READING by keyword rule on the title only (no thumbnails, descriptions or transcripts).
Views are the Videos tab's ROUNDED text ("24K"), so views and multiples are approximate. Upload dates are
APPROXIMATE (from the tab's age text); "last 12 months" = age text up to "11mo ago".

Tie-break (one primary sub-niche per video): the FIRST rule in SUBNICHE_RULES that matches wins. Order:
  1. out of scope / adjacent / trade-facing (vehicle AC, water heaters, frozen pipes, fridges, trade careers,
     trade training, commercial) - so they never land in a homeowner bucket;
  2. the cross-cutting homeowner QUESTIONS the title sells (outage, scams and upsells, the bill, replacement cost and
     quotes, brand verdicts, choosing a contractor, buy or replace, smells and noises) - these win over the
     equipment named, because the title is about the question, not the box;
  3. distinct appliance families (evaporative coolers, cooling without AC, fans for cooling, portable AC, window AC,
     RV / van / camping, garage and shop, mini-split, heat pumps);
  4. the component (thermostats, filters, parts, refrigerant, coils, condensate drain, ducts, humidity, indoor air,
     carbon monoxide, insulation) - wins over the generic system it sits in;
  5. heat-system families (off-grid DIY heat, oil heat, boilers, wood stoves, diesel / propane heaters, space
     heaters, staying warm, furnaces, fuel choice);
  6. broad topics (seasonal maintenance, energy savings, AC central general, error codes, solar), then general
     catch-alls (HVAC basics, service-call vlogs, no heat, general heating, general cooling), then "not mapped".
The column all_tags lists EVERY rule a title matched, so a reader can see the secondary topics.
"""
import csv, glob, os, random, re, statistics, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(os.path.dirname(HERE), "raw")
STUDY = os.path.dirname(os.path.dirname(HERE))
VIDEOS = os.path.join(RAW, "census-videos-2026-10-26.csv")
CHANNELS = os.path.join(RAW, "census-channels-2026-10-26.csv")
OUT_CSV = os.path.join(RAW, "subniches-2026-10-26.csv")
OUT_MD = os.path.join(STUDY, "subniches.md")
SEED = 2611
MIN_N = 15
RECENT_AGES = re.compile(r"^\d+\s*(min|h|d|w|mo)\s+ago$")


def norm(t):
    t = (t or "").lower().replace("’", "'").replace("‘", "'").strip()
    return re.sub(r"\s+", " ", t)


# Parents = the labels.md section 4 sub-niche each fine sub-niche rolls up to. "NEW" = not in labels.md
# (proposed here; needs the operator's yes before it is treated as fixed). Scope: home = homeowner HVAC
# (ranked); trade / adjacent / out = shown, not ranked; general = catch-alls (equipment or topic not named).
P_AC = "AC: central"
P_OFF = "alternative and supplemental heat (off-grid heat)"
P_BUY = "buying and replacing a system"
P_AIR = "humidity, ventilation and indoor air"
P_BOIL = "boilers and old-house heat"
NEWP = "NEW (not in labels.md)"

# (fine sub-niche, parent, scope, regex). First match wins.
SUBNICHE_RULES = [
    # 1. out of scope, adjacent, trade-facing
    ("out of scope: vehicle AC and heat", "out of scope", "out",
     r"\b(car|cars|truck|trucks|vehicle|automotive|jeep|tesla|semi|tractor|motorcycle|golf cart|forklift)'?s?\b.{0,40}"
     r"\b(ac|a/c|air ?con\w*|heater|heat|climate|cooling|refrigerant|freon|compressor)\b|\b(ac|a/c|air conditioning|heater|"
     r"heat|cooling)\b.{0,30}\b(car|cars|truck|vehicle|jeep|tesla)\b|heater core|r-?1234yf|\bauto (ac|a/c)\b"),
    ("adjacent: water heaters", "adjacent: water heaters", "adjacent",
     r"water heaters?|tankless|hot water (heater|tank|cylinder|tap)|\bwater tank|anode|immersion heater|"
     r"heat pump water|hpwh|\bhot water (not|no|problem|fix)|no hot water"),
    ("adjacent: frozen pipes", "adjacent: frozen pipes", "adjacent",
     r"frozen (water )?pipes?|pipes? (from )?(freez|burst)|burst pipes?|(keep|stop|prevent) (your )?pipes|"
     r"\bpipes? freez|heat tape|faucet cover|drip (your )?faucets?"),
    ("adjacent: fridges and freezers", "adjacent: fridges and freezers", "adjacent",
     r"\bfridge|refrigerator|\bfreezers?\b(?! (burn|bag))|mini fridge|kegerator|ice maker"),
    ("trade: commercial and refrigeration", "trade-facing", "trade",
     r"chiller|walk[- ]?in|\brtus?\b|rooftop (units?|ac|hvac)|\bvr[fv]\d?\b|ice machine|commercial|glycol|"
     r"cooling tower|reach[- ]in|make ?up air|\bahus?\b|cold (storage|room)|data cent|refrigeration (system|rack|"
     r"repair|equipment|unit)|industrial|supermarket|restaurant|hotel|hospital|school building|\bptac"),
    ("trade: careers, business and tech life", "trade-facing", "trade",
     r"hvac (life|business|sales|school|career|careers|student|students|license|licensing|owner|owners|entrepreneur|"
     r"marketing|branding|podcast|company owners?|apprentice|industry|job|jobs|interview)|day in the life|\bvlog\b|"
     r"apprentice|journeym|\bsalary|\bwages|get paid|how much (can|do|does) (a |an )?(hvac )?(tech|techs|technician)|"
     r"tech pay|\bpay per|sales (call|process|training|myth|tips|advice|manager|team|meeting)|\bclosers?\b|"
     r"business owners?|#hvaclife|#hvacbusiness|#bluecollar|#hvacguy|women in hvac|ride ?along|along for the ride|"
     r"\bpodcast|interview|\bhiring\b|\bcustomers?\b.{0,20}\b(upset|difficult|angry|service)|de-?escalat|"
     r"\bmy (first|last) (day|year|week)\b|quit(ting)? (my|the) (job|trade)|\bthe trade\b|\btradesm[ae]n|"
     r"\bcareer|\bburn ?out|mindset|recession|\bscal(e|ing) (your|a|my)\b|\bdealer meeting|\bexpo\b|ahr|"
     r"\bep(isode|\.)? ?\d|\bseason \d|\bpart \d+ of \d+|\bsession \d|\blive\b.{0,10}\b(q ?& ?a|stream)|q ?& ?a|"
     r"\bhvac (tech|technician)s?\b.{0,25}\b(life|vlog|pov|pay|day|work day|week|year)|\bpov\b|tool ?bag|"
     r"bag (loadout|setup)|tool (review|haul|tour)|\bnew tools?\b|tools? (i use|every (hvac )?tech|for (hvac )?techs)|"
     r"\bvan tour|work van|service van|\bcrew\b"),
    ("trade: technical training", "trade-facing", "trade",
     r"training|practice test|exam|\bepa ?60[89]|\bceu|superheat|subcool|manifold|\bgauges?\b|wiring diagram|"
     r"sequence of operation|pt chart|\btxv|\btev\b|expansion valve|metering device|\bpiston\b|brazing|\bbraz|"
     r"nitrogen|micron|vacuum pump|pulling (a )?vacuum|\bevacuat|recovery machine|\bmeasurequick|\bimanifold|"
     r"\bfieldpiece|\bveto\b|\bklein\b|\bmultimeter|\bmeter\b(?! (test|reading))|\bamp (draw|clamp)|\bohms?\b|"
     r"\bmanual [jsd]\b|load calc|static pressure|\bcfm\b|\bdelta t\b|psychrometr|\benthalpy|\bbtu\b.{0,10}(a measure|"
     r"formula)|\bfor (beginners|techs|technicians|apprentices|new techs)|\bhvac (\d{3}|101 for techs)\b|"
     r"\bfaults? codes?\b(?=.{0,20}(training|class))|\bclass\b|\blesson|lecture|course|\bschematic"),
    # 2. cross-cutting homeowner questions
    ("heat and power in an outage", "heat and power in an outage", "home",
     r"outage|without power|no power\b|without electricity|no electricity|blackout|power (goes|went|is|was) out|"
     r"(lose|losing|lost) power|power dies|grid[- ]down|\bgrid (fails|failure|goes|collapse)|\boff the grid\b|"
     r"generator|when the power|power cut|ice storm|winter storm|snow ?storm|\bstorm\b|hurricane|emergency heat(?! strip)|"
     r"emergency (heating|heater|warmth)|\bshtf|\bprepper|\bsurvival\b|survive (a|the) (winter|cold|storm|freeze)"),
    ("scams and upsells", P_BUY, "home",
     r"\bscam|rip(ped|s)?[- ]?off|\bupsell|\bconned|\bcon (job|artist)|gouge|gouging|overcharg|over-?charg|hack job|"
     r"dishonest|\bfraud|crooked|shady|\bliars?\b|\blie(s|d)?\b|\blying\b|don'?t (fall for|get fooled|be fooled)|"
     r"(companies|contractors?|techs?|technicians|installers|salesm[ae]n|dealers?|hvac guys?|repairm[ae]n) "
     r"(don'?t|won'?t|never|hope|hate|lie|charge|tricks?|secretly|use|want|wish|will try|try)|"
     r"don'?t let (them|the|your|an?|any)|\btricks? (they|hvac|companies|contractors|techs)|second opinion|"
     r"bad install|botched|installer (ruined|messed)|ruined (my|our|the)|nightmare|\bunnecessary|"
     r"\bdon'?t need (a |an )?(new|to replace)|what (they|your (tech|contractor|installer|salesman)) (won'?t|didn'?t|don'?t)"),
    ("energy bills", "energy bills", "home",
     r"\bbills?\b|cost(s|ing)? (to run|to operate|per (hour|day|week|month|year))|cost of running|running costs?|"
     r"costs? (pennies|less|nothing|\$?\d+(\.\d+)? ?(cents?|a (day|month|year)))|\bkwh\b|price cap|octopus|phantom|"
     r"\btariffs?\b|electricity (prices?|costs?|usage|rates?)|power (usage|consumption)|\bwatts?\b|wattage|"
     r"use(s)? (less|more) (electricity|energy|power)|\bsave(s|d)? (\$|money|energy|on|you|hundreds|thousands|big)|"
     r"saving (money|energy|on)|energy[- ]sav|cut (your )?(heating|cooling|energy)|lower (your )?(heating|cooling|"
     r"energy|electric|utility)|cheaper (to run|than)|\butility\b|utilities|money[- ]saving|\bwasting (money|energy)|"
     r"waste (money|energy)"),
    ("replacement cost and quotes", P_BUY, "home",
     r"\bquotes?\b|how much (does|do|is|should|will|did|it|for|to)|\bcosts?\b|\bprices?\b|\bpric(ing|ed)\b|"
     r"\bfinanc|\brebates?\b|tax credits?|\bwarrant(y|ies)|\bexpensive|\b\$\d[\d,.]*k?\b|\bdollars?\b|\bafford|"
     r"\bbudget|\bworth the (money|price|cost|investment)|\bpaid\b|\bpay\b|\binvoice|\bestimate"),
    ("brand verdicts", "brand verdicts", "home",
     r"\bbrands?\b|worth buying|to avoid|never buy|don'?t buy|which (one|model|brand|is better|should)|"
     r"\b(best|worst|top \d+|\d+ best) (\w+ ){0,3}(ac|a/c|air conditioners?|heat pumps?|furnaces?|mini[ -]?splits?|"
     r"hvac|thermostats?|boilers?|units?|systems?|dehumidifiers?|purifiers?|heaters?|space heaters?|window|portable|"
     r"filters?)|\b(carrier|trane|lennox|goodman|rheem|ruud|york|amana|daikin|bryant|american standard|mitsubishi|"
     r"fujitsu|\blg\b|gree|bosch|mr ?cool|pioneer|senville|midea|payne|heil|tempstar|coleman|maytag|frigidaire|"
     r"friedrich|haier|ge|toshiba|samsung|panasonic|aciq|daikin)\b.{0,40}\b(vs\.?|versus|good (and|or|&) bad|"
     r"any good|junk|garbage|reliab|honest (opinion|review)|problems|failing|worst|best|better)|\bvs\.? "
     r"(carrier|trane|lennox|goodman|rheem|ruud|york|amana|daikin|bryant|american standard|mitsubishi|fujitsu)"),
    ("choosing a contractor", P_BUY, "home",
     r"(hire|hiring|choos(e|ing)|find(ing)?|pick(ing)?|vet(ting)?|good|right|best|trust(ed|worthy)?|top) (an? |the |your |"
     r"\w+ )?(hvac |ac |heating |local )?(contractor|company|companies|tech|technician|installer|dealer)s?\b|"
     r"\bcontractors?\b|\bdealers? in\b|\binstallers?\b"),
    ("buy or replace (sizing, repair vs replace, new system)", P_BUY, "home",
     r"repair (or|vs\.?) replace|replace (or|vs\.?) repair|should (i|you|we) (replace|repair|buy|get|upgrade)|"
     r"time to replace|when to replace|replace (it|your system) (now|or)|how long (do|does|should|will) .{0,30}last|"
     r"\blifespan|life expectancy|\bsiz(e|ed|ing)\b|what size|right size|oversiz|undersiz|how many btus?|"
     r"buying (a|an|your|the) |before (you )?(buy|buying|replac)|buyer'?s guide|what to (buy|look for)|\bseer2?\b|"
     r"\bafue\b|efficiency rating|replac(e|ed|ing|ement) (of )?(your |the |my |an? |old |our |a whole |the whole |"
     r"the entire )?(whole |entire )?(old )?(ac|a/c|air conditioner|furnace|hvac|system|heat pump|unit|boiler|"
     r"condenser|equipment)s?\b(?! (capacitor|contactor|filter|motor|fan|coil|board|thermostat|igniter|ignitor|part|"
     r"sensor|switch|relay|valve))|new (hvac|ac|a/c) system|change ?out|\bupgrad(e|ed|ing) (your|my|the|to)"),
    ("smells and noises", NEWP, "home",
     r"\bsmell|odou?r|stink|\bnois(e|y|es)\b|buzz|humm(ing|s)?\b|\bbang(ing|s)?\b|click(ing|s)?\b|squeal|whistl|"
     r"rattl|grind(ing)?\b|\bloud\b|rotten egg|dirty sock|musty|sound(s|ing)? like|\bscreech|\bsqueak|\bpopping\b|"
     r"\bknock(ing)?\b|\bthump"),
    # 3. distinct appliance families
    ("evaporative coolers", NEWP, "home",
     r"swamp cooler|evaporative|\bair coolers?\b|\bcooler (fan|unit)|desert cooler|hessaire|\bportacool"),
    ("cooling without AC (tricks, DIY coolers)", NEWP, "home",
     r"without (an? )?(ac|a/c|air ?con\w*)|\bno (ac|a/c|air conditioning)\b|diy (ac|a/c|air ?con\w*|air cooler|cooler|"
     r"swamp)|homemade (ac|a/c|air ?con\w*|cooler)|\bice (fan|cooler|bucket|block|chest)|bucket (ac|cooler|air)|"
     r"(keep|keeping|stay|staying) (\w+ ){0,3}cool\b|cool (a|your|the|my) (room|house|home|bedroom|tent|garage) "
     r"(down|without|for|with)|beat the heat|heat ?wave|frozen water bottle|5 gallon (bucket )?(ac|air)|cooler ac|"
     r"(fan|cooler) (that )?(blows|makes) cold|ice cold air|free (ac|air conditioning|cooling)"),
    ("fans for cooling (ceiling, whole-house, box)", NEWP, "home",
     r"ceiling fans?|whole[- ]house fans?|attic fans?|box fans?|window fans?|tower fans?|bladeless fan|"
     r"\bfans?\b(?! (motor|blade|capacitor|relay|limit|control|speed|setting|on|auto|switch|coil))"),
    ("AC: portable", "AC: portable", "home",
     r"portable (ac|a/c|air|heat pump|unit|units|air conditioners?)|ecoflow wave|\bwave \d|battery[- ]powered (ac|air)|"
     r"zero ?breeze|\bdreo\b|midea duo|\bwindmill\b|\bbluetti\b.{0,20}(ac|cool)|\bsolar (powered )?(ac|air ?con\w*)"),
    ("AC: window", "AC: window", "home",
     r"window (ac|a/c|air conditioners?|units?|air|conditioner)|window-?mounted|\bu[- ]shaped|midea u\b|"
     r"through[- ]the[- ]wall|wall (ac|a/c|unit|air conditioner)|in-?wall (ac|unit)|sleeve"),
    ("RV, van, tent and camping heat or cool", NEWP, "home",
     r"\brvs?\b|camper|motorhome|\bvan\b|vanlife|\btents?\b|camping|ice fishing|\bboat\b|\bbus\b|skoolie|"
     r"travel trailer|\btruck camper|overland|\bhunting (blind|cabin)|\bcabin\b(?= heat)"),
    ("garage, shop and outbuildings", NEWP, "home",
     r"garage|workshop|\bshop\b|\bbarn\b|greenhouse|chicken coop|\bcoop\b|\bshed\b|outbuilding|pole barn|"
     r"tiny (house|home)|\bcabin\b|container home|shipping container|\byurt"),
    ("mini-split", "mini-split", "home",
     r"mini[ -]?splits?|ductless|mr ?cool|\bsplit (ac|a/c|system|unit|air|heat pump)|senville|pioneer (mini|ductless|"
     r"diy)|diy (ac|a/c|heat pump) (install|kit)|\bline ?set|\bhead unit|\bindoor unit|wall unit|\bmulti[- ]zone"),
    ("heat pumps", "heat pumps", "home",
     r"heat ?pumps?|\bashp|air[- ]source|ground[- ]source|geothermal|reverse cycle|\bdefrost|aux(iliary)? heat|"
     r"emergency heat|\bem heat|cold[- ]climate|heat strips?|\bdual fuel|hybrid (heat|system)"),
    # 4. components
    ("smart thermostats", "thermostats", "home",
     r"smart thermostat|\bnest\b|ecobee|wi-?fi thermostat|\bsensi\b|google home|alexa|thermostat.{0,30}(app|wifi|"
     r"wi-fi|smart|learning)|smart (home|vents?)|\bc[- ]wire|common wire"),
    ("thermostats", "thermostats", "home",
     r"thermostat|\bwhat temperature|(best|right|ideal|perfect|correct) temperature|set (your|the) (temp|heat|ac|a/c|"
     r"thermostat)|\b\d\d ?(°|degrees|deg\b)|honeywell|\bfan (on|auto)\b|auto (vs\.?|or) on|setback|"
     r"temperature (setting|you should)|\bthermostat"),
    ("filters", "filters", "home",
     r"\bfilters?\b|\bmerv\b|filtrete|\bhepa\b(?=.{0,20}filter)"),
    ("parts homeowners touch", "parts homeowners touch", "home",
     r"capacitor|contactor|disconnect|\bfuses?\b|condensate pump|igniter|ignitor|hot surface|flame (sensor|rod)|"
     r"blower (motor|wheel)|limit switch|pressure switch|rollout|inducer|control board|circuit board|\bboard\b|"
     r"\brelays?\b|transformer|\bmotors?\b|thermocouple|\bbreakers?\b|gas valve|\bsensors?\b|\bwir(e|es|ing)\b|"
     r"low voltage|hard start|start kit|\bbelt\b|bearing|\bbreaker\b|\becm\b|\bpsc\b|ignition|\bspark"),
    ("refrigerant", P_AC, "home",
     r"freon|refrigerant|r-?22\b|r-?410a?\b|r-?454b?\b|r-?32\b|r-?290|r-?134a?\b|recharg|low on (freon|refrigerant|charge)|"
     r"\bleak (search|detect|repair|check)|refrigerant leak|\bleaks?\b(?! water)|\bcharg(e|ing) (an? |the |your |my )?"
     r"(ac|a/c|system|unit|air conditioner|heat pump)|add(ing)? (freon|refrigerant)|epa (ban|rule)|phase ?out|"
     r"a2l|new refrigerant|\btop(ping)? off"),
    ("coils and condenser cleaning", P_AC, "home",
     r"\bcoils?\b|condenser (clean|wash)|clean(ing|s)? (the |your |an? |my |our )?(ac |a/c |outside |outdoor |hvac |"
     r"air conditioner |air conditioning )?(condenser|unit|coils?|fins|outdoor unit|outside unit)|\bfins?\b|"
     r"frozen (coil|ac|a/c|unit|line|air conditioner)|ice (on|build|up)|iced up|ic(ing|ed) up|freez(ing|es|e)? up|"
     r"evaporator|coil clean|hose (off|down)|pressure wash"),
    ("condensate drain and water leaks", P_AC, "home",
     r"drain (line|pan|pipe|lines)|condensate|water (leak|leaking|dripping|on the floor|coming|in (the )?pan|"
     r"puddle)|leaking water|dripping water|clogged drain|\bp-?trap|float switch|\bdrain\b|\bpan\b|\bsweating\b"),
    ("ducts and vents", "ducts and vents", "home",
     r"\bducts?\b|ductwork|\bvents?\b(?![- ]?(free|less))|\bregisters?\b|return air|\breturns?\b|air ?flow|"
     r"damper|\bplenum|upstairs|downstairs|second floor|2nd floor|hot (room|rooms|spots?|bedroom)|cold (room|rooms|"
     r"spots?|bedroom)|uneven|zoning|\bzones?\b(?! valve)|air ?handler|\bblower\b|duct ?clean"),
    ("carbon monoxide and gas safety", P_AIR, "home",
     r"carbon monoxide|\bco (detector|alarm|poison|leak)|\bco\b(?= ?(poison|danger|risk))|gas leak|smell gas|"
     r"cracked heat exchanger|heat exchanger crack|\bco2\b|poison|\bfumes?\b|explo(de|sion|sive)|\bfire hazard|"
     r"fire risk|\bsafe(ty|ly)?\b.{0,20}(heater|furnace|gas|propane)|(heater|furnace|gas|propane).{0,20}\bsafe(ty|ly)?\b"),
    ("humidity and dehumidifiers", P_AIR, "home",
     r"humid|dehumid|\bmou?ld|mildew|crawl ?space|condensation|\bdamp|moisture|sweating (windows|ducts|pipes)|"
     r"vapou?r barrier|\bdry (air|out)|static shock|nosebleed"),
    ("indoor air and purifiers", P_AIR, "home",
     r"purifier|air quality|indoor air|\buv\b|\bhepa\b|ventilat|\berv\b|\bhrv\b|fresh air|exhaust fan|bath(room)? fan|"
     r"range hood|allerg|\bdust\b|dusty|air scrubber|ioniz|ozone|wildfire smoke|\bsmoke\b|\biaq\b|clean air|"
     r"breath(e|ing)|asthma|\bvoc|\bradon"),
    ("drafts, insulation and windows", "drafts, insulation and air sealing", "home",
     r"insulat|\bdrafts?\b|drafty|draught|weather ?strip|spray foam|caulk|window film|air seal|\battic\b|curtains?|"
     r"\bblinds\b|\bwindows?\b|\bseal(ing|ed|s)?\b|passive ?house|\broof\b|\bshades?\b|energy audit|blower door|"
     r"thermal (bridg|imag|camera)|bubble wrap|door sweep|cold air (coming|leaking|getting)|heat loss|"
     r"(keep|keeping) (the )?(heat|cold|warmth|warm air|cool air) (in|out)|r-?value|cellulose|fiberglass|"
     r"radiant barrier|\bexterior wall|\bwalls?\b(?= .{0,15}(cold|warm|heat))|\bdoors?\b"),
    # 5. heat-system families
    ("off-grid heat: free-heat tricks and DIY heaters", P_OFF, "home",
     r"candle|terracotta|clay pot|flower ?pot|rocket (stove|heater|mass)|free (heat|heating|energy|fuel|warmth)|"
     r"earth (tube|tunnel|battery|pipe)|underground (tube|pipe|tunnel)|\bsalt\b|solar (air )?(heater|heat|furnace|"
     r"collector|panel heater)|can heater|soda cans?|beer cans?|tuna can|aluminum cans|tin cans?|waste oil|used oil|"
     r"motor oil|diy (heater|stove|heating|furnace)|homemade (heater|stove|heating|furnace)|make (a|your own) (heater|"
     r"stove)|no (gas|wood|electricity|fuel)\b|sand battery|thermal mass|compost heat|cement stove|\bbrick|"
     r"charcoal|alcohol (heater|stove)|heat bank|\bjar\b|\bbottles?\b|\bpvc\b|invention|\bgenius|ingenious|"
     r"\btrick\b|\bhack\b|\bclever\b|\bforgotten\b|\bold[- ]?(time|fashioned|school|timers?)\b|\bamish\b|"
     r"\bgrand(ma|pa|mother|father|parents)|depression[- ]era|pioneer|\bancient\b|\bvictorian\b|\b1800s\b|"
     r"\bmountain men\b|\bsoviet\b|\bmiracle\b|perpetual|unlimited heat|\bbanned\b|\bsecret\b"),
    ("oil heat", P_BOIL, "home",
     r"oil burner|oil[- ]fired|heating oil|oil tank|oil furnace|oil heat|\boil boiler|beckett|riello|\bnozzle|"
     r"home heating oil|\boil (delivery|prices?|line|filter|pump|level)|fuel oil|\b#2 oil|\boil vs\.?|vs\.? oil\b"),
    ("boilers, radiators and steam", P_BOIL, "home",
     r"boiler|radiator|baseboard|\bsteam\b|hydronic|zone valve|circulator|aquastat|radiant (floor|heat)|in-?floor|"
     r"underfloor|\bflue\b|combi|vaillant|remeha|worcester|baxi|viessmann|navien|\bbleed|expansion tank|"
     r"pressure relief|old house heat|cast iron|\bmanifold\b(?= .{0,10}(floor|radiant))|\bufh\b|gravity (heat|system)"),
    ("off-grid heat: wood and pellet stoves, fireplaces", P_OFF, "home",
     r"wood ?stoves?|wood[- ]?burn|woodburn|pellet|firewood|fire ?wood|fireplace|chimney|\bstoves?\b|"
     r"masonry heater|wood heat|\bkindling|\bcord(s)? of|seasoned wood|\bsplitting\b|\bmulti[- ]?fuel|\binsert\b|"
     r"\bcreosote|\bwood\b"),
    ("off-grid heat: diesel, propane and kerosene heaters", P_OFF, "home",
     r"diesel heater|parking heater|chinese (diesel )?heater|vevor|kerosene|propane heater|buddy heater|"
     r"mr\.? heater|\bk-?1\b|vent[- ]?free|ventless|catalytic|gas heaters?|paraffin|\bdiesel\b|\bheatbox|"
     r"tent heater|\bpropane\b.{0,20}\bheat|\bbuddy\b"),
    ("space heaters (electric)", P_OFF, "home",
     r"space heaters?|electric heaters?|oil[- ]filled|infrared heater|panel heaters?|radiant heaters?|ceramic heater|"
     r"storage heaters?|electric (radiators?|heating|heat\b|fireplace)|\bheaters?\b|\bconvector|\bdelonghi|\bdyson"),
    ("staying warm without heating (body, bed, clothes)", P_OFF, "home",
     r"(keep|keeps|keeping|stay|staying|sleep|sleeping) (\w+ ){0,3}warm|warm (bed|blanket|feet|hands)|hand ?warmers?|"
     r"blankets?|sleeping bags?|heated (blanket|vest|jacket|clothing|socks|throw|mattress|pad)|\blayers|"
     r"thermal underwear|hot water bottle|freezing nights?|without (heat|heating)|\bcold (night|nights)\b|"
     r"warm(er|est)? (room|bedroom|house|home)|\bbed\b|\bbedroom\b"),
    ("furnaces", "furnaces", "home",
     r"furnace|pilot light|forced[- ]air|\bburner\b|heat exchanger|\bgas heat\b|\bgas fired\b|\bhigh efficiency\b"),
    ("heating fuel and fuel choice", "heating fuel and fuel choice", "home",
     r"\bpropane\b|natural gas|\bfuel\b|gas vs|vs\.? gas|gas or electric|electric vs\.? gas|\blpg\b|"
     r"cheapest (way|heat|heating|to heat|form)|\bgas (prices?|supply|ban|line|meter|company)|\bgas\b"),
    # 6. broad topics, then catch-alls
    ("seasonal maintenance", "seasonal maintenance", "home",
     r"maintenance|maintain|tune[- ]?up|before (winter|summer|you turn|the first|heating season|cooling season|it gets|"
     r"the cold|the heat|fall|spring)|checklist|\bspring\b|\bfall\b|\bautumn\b|\bwinteriz|summeriz|first freeze|"
     r"start[- ]?up|turn(ing)? on (your|the) (heat|ac|a/c|furnace|air)|every (homeowner|year|month|season)|annual|"
     r"preventa?t?ive|clean(ing)? (your|the|an?|my) (ac|a/c|hvac|furnace|system|air conditioner)|\bservic(e|ing) "
     r"(your|my|the) (ac|a/c|hvac|furnace|system|unit|air conditioner)|\bsummer\b|\bwinter\b|\bdiy\b.{0,10}\b(clean|service)|"
     r"\bhomeowners? (should|must|need)"),
    ("AC: central", P_AC, "home",
     r"\ba/?c\b|air ?con\w*|central air|condenser|compressor|blowing (warm|hot)|not cooling|won'?t cool|"
     r"outdoor unit|outside unit|\bhvac unit\b|\bcooling\b|\bcools?\b|split system|\bac'?s\b"),
    ("error codes and troubleshooting", NEWP, "home",
     r"troubleshoot|diagnos|error codes?|fault codes?|\bcodes?\b|blink|flashing|\b[a-z]\d{1,2}\b (code|error)|"
     r"\berror\b|not working|won'?t (turn|start|come)|stopped working|\bfix(ed|ing|es)?\b|\brepair"),
    ("adjacent: solar, batteries and home energy systems", "adjacent: solar and home energy", "adjacent",
     r"\bsolar|powerwall|home batter|\bbatter(y|ies)\b|\bev\b|electric (car|vehicle)|\binverter\b(?! (ac|mini|heat))|"
     r"net zero|zero carbon|\benergy (system|independence|storage)|hydrogen|\bnuclear\b|wind turbine"),
    ("general: HVAC basics and how it works", NEWP, "general",
     r"how (does |do |a |an |your |the )?(hvac|heating|cooling|ac|a/c|system|it)( system)? works?|hvac (basics|101|"
     r"explained|components|system)|explained|how .{0,30} works?\b|\bhvac\b"),
    ("general: no heat (equipment not named)", NEWP, "general",
     r"no heat|not heating|heat(er|ing)? (is )?not working|won'?t heat|no (warm|hot) air|blowing cold|"
     r"house (is|so|too|feels) cold"),
    ("general: heating (equipment not named)", NEWP, "general",
     r"\bheat(s|ed|ing|er)?\b|\bwarm(th|er|ing|s)?\b|\bcold\b|\bfreez(e|ing)|\bwinter|\bchill|\bfrost"),
    ("general: cooling (equipment not named)", NEWP, "general",
     r"\bcool(er|est|ing|s)?\b|\bhot\b|\bsummer|\btemperature"),
]
SUBNICHE_RX = [(n, p, s, re.compile(rx)) for n, p, s, rx in SUBNICHE_RULES]
FALLBACK = ("HVAC, not mapped", "not mapped", "unmapped")
SCOPE_OF = {n: s for n, p, s, rx in SUBNICHE_RULES}
SCOPE_OF[FALLBACK[0]] = FALLBACK[2]
PARENT_OF = {n: p for n, p, s, rx in SUBNICHE_RULES}
PARENT_OF[FALLBACK[0]] = FALLBACK[1]


def tags(title):
    t = norm(title)
    return [n for n, p, s, rx in SUBNICHE_RX if rx.search(t)]


def primary(title):
    tg = tags(title)
    return tg[0] if tg else FALLBACK[0]


# ---------------------------------------------------------------------------------------------------------------
# Hand-check: 100 random HVAC titles of tiers A-C (random.Random(2611).sample of the video IDs, sorted). My own
# reading of each title's primary sub-niche under the same tie-break. "=" = I agree with the rule's tag (as it
# stood when I read the sample: FIRST_PASS). Filled in by hand after reading the titles.
# ---------------------------------------------------------------------------------------------------------------
HANDCHECK = {}  # video_id -> (my sub-niche or "=", note)
FIRST_PASS = {}  # video_id -> the rule's tag when the sample was first read (before the fixes it led to)


# ---------------------------------------------------------------------------------------------------------------
def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def load():
    chans = {r["channel_id"]: r for r in csv.DictReader(open(CHANNELS, encoding="utf-8"))}
    # types: round 3 type helpers' files first, provisional carry-forward second
    typed, type_files = {}, []
    for f in sorted(glob.glob(os.path.join(RAW, "census-types-*-2026-10-26.csv"))):
        type_files.append(os.path.basename(f))
        for r in csv.DictReader(open(f, encoding="utf-8")):
            cid = r.get("channel_id") or r.get("channelId") or ""
            ty = (r.get("type") or r.get("channel_type") or "").strip()
            if not cid and r.get("handle"):
                cid = next((c for c, x in chans.items() if x["handle"].lower() == r["handle"].lower()), "")
            if cid and ty:
                typed[cid] = (ty, os.path.basename(f))
    vids = []
    for r in csv.DictReader(open(VIDEOS, encoding="utf-8")):
        if r["is_hvac"] != "yes":
            continue
        c = chans.get(r["channel_id"], {})
        tier = c.get("tier", "")
        if r["channel_id"] in typed:
            ty, tsrc = typed[r["channel_id"]]
        else:
            ty, tsrc = c.get("type", ""), ("provisional: " + c.get("type_source", "")) if c.get("type") else ""
        tg = tags(r["title"])
        pr = tg[0] if tg else FALLBACK[0]
        vids.append({
            "video_id": r["video_id"], "channel_id": r["channel_id"], "channel": r["channel"].strip(),
            "handle": c.get("handle", ""), "tier": tier, "type": ty, "type_source": tsrc, "title": r["title"],
            "views": fnum(r["views_tab"]), "views_tab": r["views_tab"], "age_text": r["age_text"],
            "approx_date": r["approx_date"], "last12m": bool(RECENT_AGES.match(r["age_text"].strip())),
            "multiple": fnum(r["multiple"]), "baseline": r["baseline"], "baseline_rule": r["baseline_rule"],
            "subniche": pr, "parent": PARENT_OF[pr], "scope": SCOPE_OF[pr], "all_tags": tg,
            "census_subniche": r["subniche"]})
    return chans, vids, typed, type_files


def type_group(ty):
    t = (ty or "").lower()
    if t.startswith("faceless persona"):
        return "faceless persona"
    if t.startswith("faceless"):
        return "faceless"
    if t.startswith("on camera"):
        return "on camera"
    if not t or "not yet" in t:
        return "untyped"
    return "other"  # brand, AI avatar


def stats(vs):
    n = len(vs)
    views = [v["views"] for v in vs if v["views"] is not None]
    mult = [v["multiple"] for v in vs if v["multiple"] is not None]
    ch = Counter(v["channel"] for v in vs)
    return {"n": n, "channels": len(ch),
            "med_views": statistics.median(views) if views else None,
            "med_mult": statistics.median(mult) if mult else None,
            "n_mult": len(mult),
            "share2x": (sum(1 for m in mult if m >= 2) / len(mult)) if mult else None,
            "top_ch_share": (ch.most_common(1)[0][1] / n) if n else None,
            "persona": sum(1 for v in vs if type_group(v["type"]) == "faceless persona")}


def fv(x):
    if x is None:
        return "-"
    if x >= 1e6:
        return f"{x / 1e6:.1f}M".replace(".0M", "M")
    if x >= 1e3:
        return f"{x / 1e3:.0f}K" if x >= 1e4 else f"{x / 1e3:.1f}K".replace(".0K", "K")
    return f"{x:.0f}"


def fm(x):
    return "-" if x is None else f"{x:.2f}"


def fp(x):
    return "-" if x is None else f"{100 * x:.0f}%"


def md(s):
    return (s or "").replace("|", "/").replace("\n", " ").strip()


def sample(vids):
    pool = sorted((v for v in vids if v["tier"] in ("A", "B", "C")), key=lambda v: v["video_id"])
    return random.Random(SEED).sample(pool, 100)


def write_csv(vids):
    cols = ["video_id", "channel_id", "channel", "handle", "tier", "type", "type_source", "title", "views_tab",
            "age_text", "approx_date", "last12m", "multiple", "baseline", "baseline_rule", "subniche", "parent",
            "scope", "all_tags", "census_subniche"]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for v in sorted(vids, key=lambda v: (v["tier"], v["channel"], v["video_id"])):
            row = dict(v)
            row["last12m"] = "yes" if v["last12m"] else "no"
            row["multiple"] = "" if v["multiple"] is None else round(v["multiple"], 2)
            row["all_tags"] = "; ".join(v["all_tags"])
            w.writerow([row[c] for c in cols])


def main_table(groups, title_note, ranked=True):
    out = ["| # | Sub-niche (reading) | labels.md parent | n videos | channels | median views | median multiple (n with multiple) "
           "| share at 2x+ | biggest channel's share of n | faceless-persona videos |",
           "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    rows = sorted(groups.items(), key=lambda kv: (-(kv[1]["med_mult"] or 0), -kv[1]["n"]))
    for i, (k, s) in enumerate(rows, 1):
        out.append(f"| {i if ranked else '-'} | {k} | {PARENT_OF[k]} | {s['n']:,} | {s['channels']} | {fv(s['med_views'])} | "
                   f"{fm(s['med_mult'])} ({s['n_mult']}) | {fp(s['share2x'])} | {fp(s['top_ch_share'])} | {s['persona']} |")
    return out


def build(vids, chans, typed, type_files):
    W = []
    ac = [v for v in vids if v["tier"] in ("A", "B", "C")]
    d_t = [v for v in vids if v["tier"] == "D"]
    rec = [v for v in ac if v["last12m"]]
    n_ac = len(ac)
    unm = sum(1 for v in ac if v["subniche"] == FALLBACK[0])
    gen = sum(1 for v in ac if SCOPE_OF[v["subniche"]] == "general")
    old_unm = sum(1 for v in ac if v["census_subniche"].startswith("HVAC, not mapped"))
    ad = [v for v in vids if v["tier"] in ("A", "B", "C", "D")]
    unm_ad = sum(1 for v in ad if v["subniche"] == FALLBACK[0])
    old_unm_ad = sum(1 for v in ad if v["census_subniche"].startswith("HVAC, not mapped"))
    ac_ch = {v["channel_id"] for v in ac}
    tg_counts = Counter(type_group(v["type"]) for v in ac)
    ch_types = Counter(type_group(next(x["type"] for x in ac if x["channel_id"] == c)) for c in ac_ch)
    typed_from_helpers = sum(1 for c in ac_ch if c in typed)

    def by(vs, key="subniche"):
        g = defaultdict(list)
        for v in vs:
            g[v[key]].append(v)
        return g

    W.append("# HVAC sub-niche map (deliverable 3)\n")
    W.append("Built 2026-10-26 by `data/tools/subniche_map.py` (round 3 sub-niche helper) from the census pull of "
             "2026-10-26 (`data/raw/census-videos-2026-10-26.csv`, `census-channels-2026-10-26.csv`). Nothing committed "
             "or pushed. **Not yet re-checked by a second helper (working rule 3).** Per-video table: "
             "`data/raw/subniches-2026-10-26.csv`.\n")
    W.append("## Read this first\n")
    W.append("- **Measured:** views (the Videos tab's **rounded** text, e.g. \"24K\", pulled logged out on 2026-10-26), "
             "the multiple (views / the channel's baseline, from `census_build.py`), counts.")
    W.append("- **Approximate:** upload dates come from the tab's age text (\"3mo ago\"), so \"last 12 months\" means age "
             "text up to \"11mo ago\" (about 2025-10-26 to 2026-10-26, edges fuzzy). Multiples inherit the rounding.")
    W.append("- **Readings, not measurements:** the HVAC mark (`is_hvac`, census rule), the tiers, the channel types and "
             "**every sub-niche tag** (a keyword rule on the title only; no thumbnails, descriptions or transcripts). "
             "Hand-check accuracy is below.")
    W.append("- **The multiple** (labels.md section 6): views / median views of the channel's long-form videos from the "
             "last 12 months (`12M`); if it had fewer than 10, the median of its last 30 long-form (`last30`). In the "
             f"map set: {sum(1 for v in ac if v['baseline_rule'] == '12M'):,} videos on the 12M rule, "
             f"{sum(1 for v in ac if v['baseline_rule'] == 'last30'):,} on last30, "
             f"{sum(1 for v in ac if v['multiple'] is None)} with no multiple. **Caution:** an old video against a "
             "recent baseline gets a high multiple partly from age and partly from the channel's recent decline, so "
             "the all-time multiples lean high for old-video sub-niches; the 12-month table is the fairer comparison.")
    W.append("- **Medians, not means,** and every row shows n. Sub-niches with n under 15 are listed separately, not ranked. "
             "\"Biggest channel's share\" warns when one channel makes most of a row.\n")

    W.append("## Method\n")
    W.append(f"- **The map set:** every long-form (5:00+) video marked HVAC (`is_hvac = yes`) of the **tier A, B and C** "
             f"channels: **{n_ac:,} videos from {len(ac_ch)} channels** ({sum(1 for v in ac if v['tier']=='A'):,} A, "
             f"{sum(1 for v in ac if v['tier']=='B'):,} B, {sum(1 for v in ac if v['tier']=='C'):,} C). Tier D "
             f"(trade and company channels, {len(d_t):,} HVAC videos) is shown in its own table, as a contrast; "
             "tier X (under 10% HVAC) is in the CSV but not in any table.")
    W.append(f"- **Last 12 months:** {len(rec):,} of those videos.")
    W.append("- **Sub-niche rules:** `SUBNICHE_RULES` in `subniche_map.py` (my own file; `census_build.py` was not "
             "edited). Each fine sub-niche rolls up to its `labels.md` section 4 parent; the ones marked "
             "\"NEW (not in labels.md)\" (smells and noises, evaporative coolers, cooling without AC, fans for cooling, "
             "RV / van / camping, garage and shop, error codes, and the general catch-alls) are **proposals** and need "
             "the operator's yes before `labels.md` takes them. Fine splits inside a parent (refrigerant, coils, "
             "condensate drain inside AC: central; smart thermostats inside thermostats; oil heat inside boilers and "
             "old-house heat; the four off-grid splits; scams, quotes, contractor choice and buy-or-replace inside "
             "buying and replacing) are also my proposals.")
    W.append("- **One primary sub-niche per video. Ties break by rule order: the first rule that matches wins.** The order "
             "(top of `subniche_map.py`): out-of-scope, adjacent and trade-facing first; then the homeowner *question* "
             "the title sells (outage, scams, the bill, cost and quotes, brands, contractor, buy or replace, smells and "
             "noises), which wins over the equipment named; then distinct appliance families (coolers, fans, portable, "
             "window, RV, garage, mini-split, heat pumps); then the component (thermostat, filter, part, refrigerant, "
             "coil, drain, ducts, humidity, indoor air, CO, insulation), which wins over the system it sits in; then "
             "heat-system families; then broad topics; then catch-alls. Every rule a title matched is in the CSV's "
             "`all_tags` column.")
    W.append("- **Scope:** `home` sub-niches are ranked. `trade` (careers and tech life, technical training, commercial), "
             "`adjacent` (water heaters, frozen pipes, fridges, solar and batteries; labels.md: \"seen but not counted\") "
             "and `out` (vehicle AC) are shown in their own table, not ranked. `general` catch-alls (heating or cooling "
             "with no equipment or topic named, HVAC basics) are mapped but flagged.")
    W.append(f"- **Coverage:** the census builder left {old_unm:,} of {n_ac:,} A-C HVAC titles unmapped "
             f"({100 * old_unm / n_ac:.1f}%; {100 * old_unm_ad / len(ad):.1f}% of A-D). This map leaves "
             f"**{unm:,} unmapped ({100 * unm / n_ac:.1f}%)** of A-C ({unm_ad:,}, {100 * unm_ad / len(ad):.1f}% of A-D). "
             f"A further {gen:,} ({100 * gen / n_ac:.1f}%) fall to a `general` catch-all, so "
             f"{100 * (unm + gen) / n_ac:.1f}% have no specific topic. Many of the unmapped are not HVAC at all "
             "(errors of the `is_hvac` title mark, e.g. juicers, lawn care), which this map does not re-decide.")
    tyline = (f"- **Channel types:** the round 3 type helpers' files ({', '.join(type_files)}) typed "
              f"{typed_from_helpers} of the {len(ac_ch)} A-C channels in the map; the rest use the provisional type "
              "carried forward from round 2 in `census-channels-2026-10-26.csv` (sources R1, NX2, the round 2 checker, "
              "and \"brand by channel name\"), where one exists.") if type_files else (
              "- **Channel types:** no `census-types-*-2026-10-26.csv` file existed when this was built (the round 3 "
              "type helpers were still running), so types are the **provisional** ones carried forward from round 2 "
              "in `census-channels-2026-10-26.csv` (sources R1, NX2, the round 2 checker, \"brand by channel name\"). "
              "Rerun the script when the type files land.")
    W.append(tyline)
    W.append(f"  Typed A-C channels in the map: on camera {ch_types['on camera']}, faceless {ch_types['faceless']}, "
             f"faceless persona {ch_types['faceless persona']}, other (brand, AI avatar) {ch_types['other']}, "
             f"untyped {ch_types['untyped']} (videos: on camera {tg_counts['on camera']:,}, faceless "
             f"{tg_counts['faceless']:,}, faceless persona {tg_counts['faceless persona']:,}, other {tg_counts['other']:,}, "
             f"untyped {tg_counts['untyped']:,}). The type split covers typed channels only.\n")

    # --- main tables
    for label, vs in (("all time", ac), ("last 12 months", rec)):
        g = by([v for v in vs if SCOPE_OF[v["subniche"]] in ("home", "general")])
        st = {k: stats(x) for k, x in g.items()}
        big = {k: s for k, s in st.items() if s["n"] >= MIN_N}
        small = {k: s for k, s in st.items() if s["n"] < MIN_N}
        allst = stats(vs)
        W.append(f"## The map, {label} (tiers A-C, sorted by median multiple)\n")
        W.append(f"All {len(vs):,} A-C HVAC videos ({label}): median views {fv(allst['med_views'])}, median multiple "
                 f"{fm(allst['med_mult'])}, share at 2x+ {fp(allst['share2x'])}. Homeowner and general sub-niches with "
                 f"n >= {MIN_N}:\n")
        W.extend(main_table(big, label))
        W.append("")
        if small:
            W.append(f"**n under {MIN_N} ({label}), not ranked:** " + "; ".join(
                f"{k} (n {s['n']}, median views {fv(s['med_views'])}, median multiple {fm(s['med_mult'])})"
                for k, s in sorted(small.items(), key=lambda kv: -kv[1]["n"])) + ".\n")
        g2 = by([v for v in vs if SCOPE_OF[v["subniche"]] in ("trade", "adjacent", "out", "unmapped")])
        W.append(f"**Trade-facing, adjacent, out of scope and unmapped ({label}), not ranked:**\n")
        W.extend(main_table({k: stats(x) for k, x in g2.items()}, label, ranked=False))
        W.append("")
        # parents roll-up
        gp = by([v for v in vs if SCOPE_OF[v["subniche"]] in ("home", "general")], "parent")
        W.append(f"**Rolled up to the labels.md parents ({label}):**\n")
        W.append("| labels.md parent | n | channels | median views | median multiple | share at 2x+ |")
        W.append("|---|---:|---:|---:|---:|---:|")
        for k, x in sorted(gp.items(), key=lambda kv: -(stats(kv[1])["med_mult"] or 0)):
            s = stats(x)
            W.append(f"| {k} | {s['n']:,} | {s['channels']} | {fv(s['med_views'])} | {fm(s['med_mult'])} | {fp(s['share2x'])} |")
        W.append("")

    # --- tier split
    def split_table(vs, keyf, ga, gb, la, lb):
        g = by([v for v in vs if SCOPE_OF[v["subniche"]] in ("home", "general")])
        rows = []
        for k, x in g.items():
            a = stats([v for v in x if keyf(v) in ga])
            b = stats([v for v in x if keyf(v) in gb])
            gap = (a["med_mult"] - b["med_mult"]) if (a["n"] >= MIN_N and b["n"] >= MIN_N and a["med_mult"] is not None
                                                      and b["med_mult"] is not None) else None
            rows.append((k, a, b, gap))
        out = [f"| Sub-niche | {la} n | {la} median views | {la} median multiple | {la} 2x+ | {lb} n | {lb} median views | "
               f"{lb} median multiple | {lb} 2x+ | gap in median multiple ({la} minus {lb}; both n >= {MIN_N}) |",
               "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        rows.sort(key=lambda r: (r[3] is None, -(abs(r[3]) if r[3] is not None else 0), -(r[1]["n"] + r[2]["n"])))
        for k, a, b, gap in rows:
            if a["n"] + b["n"] < MIN_N:
                continue
            out.append(f"| {k} | {a['n']:,} | {fv(a['med_views'])} | {fm(a['med_mult'])} | {fp(a['share2x'])} | {b['n']:,} | "
                       f"{fv(b['med_views'])} | {fm(b['med_mult'])} | {fp(b['share2x'])} | "
                       f"{'-' if gap is None else f'{gap:+.2f}'} |")
        return out, rows

    tier_key = lambda v: v["tier"]
    type_key = lambda v: type_group(v["type"])
    W.append("## Split by tier: A vs B/C\n")
    W.append("Tier A = 50%+ of the latest 30 long-form titles HVAC; B/C = 10-49% (C = adjacent-lane channels: off-grid, "
             "old ways, frugal, energy). Rows sorted by the size of the gap (where both sides have n >= 15), then by n; "
             "rows with fewer than 15 videos in total are left out.\n")
    gaps = {}
    for label, vs in (("all time", ac), ("last 12 months", rec)):
        W.append(f"### {label}\n")
        t, rows = split_table(vs, tier_key, {"A"}, {"B", "C"}, "A", "B/C")
        gaps[("tier", label)] = rows
        W.extend(t)
        W.append("")
    W.append("## Split by channel type: faceless (incl. faceless persona) vs on camera\n")
    W.append("Types are readings (see Method for how many channels were typed and from where). Brand and AI-avatar "
             "channels and untyped channels are left out of this split. Faceless-persona videos are also counted in "
             "every map row and shown separately below.\n")
    for label, vs in (("all time", ac), ("last 12 months", rec)):
        W.append(f"### {label}\n")
        t, rows = split_table(vs, type_key, {"faceless", "faceless persona"}, {"on camera"}, "faceless", "on camera")
        gaps[("type", label)] = rows
        W.extend(t)
        W.append("")
    W.append("### Faceless persona only (all time and last 12 months)\n")
    W.append("| Sub-niche | persona n (all time) | channels | median views | median multiple | 2x+ | persona n (12 m) | "
             "median multiple (12 m) | 2x+ (12 m) |")
    W.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    gpa = by([v for v in ac if type_key(v) == "faceless persona" and SCOPE_OF[v["subniche"]] in ("home", "general")])
    for k, x in sorted(gpa.items(), key=lambda kv: -len(kv[1])):
        s = stats(x)
        r = stats([v for v in x if v["last12m"]])
        W.append(f"| {k} | {s['n']} | {s['channels']} | {fv(s['med_views'])} | {fm(s['med_mult'])} | {fp(s['share2x'])} | "
                 f"{r['n']} | {fm(r['med_mult'])} | {fp(r['share2x'])} |")
    W.append("")

    # --- D contrast
    W.append("## Tier D contrast (trade and company channels, all time)\n")
    W.append("Not part of the map; shown so the reader can see what the trade side makes. Rows with n >= 15.\n")
    gd = {k: stats(x) for k, x in by(d_t).items()}
    W.extend(main_table({k: s for k, s in gd.items() if s["n"] >= MIN_N}, "D", ranked=False))
    W.append("")

    # --- detail per sub-niche
    W.append("## Per sub-niche: top channels, biggest videos, faceless-persona count (tiers A-C, all time)\n")
    W.append("Biggest = by tab views (rounded). Multiple = views / that channel's baseline. Sorted by n.\n")
    g = by(ac)
    for k, x in sorted(g.items(), key=lambda kv: -len(kv[1])):
        s = stats(x)
        top3 = Counter((v["channel"], v["handle"], v["tier"]) for v in x).most_common(3)
        W.append(f"### {k} ({PARENT_OF[k]}; scope {SCOPE_OF[k]})\n")
        W.append(f"n {s['n']:,} videos, {s['channels']} channels; last 12 months n {sum(1 for v in x if v['last12m']):,}. "
                 f"Faceless-persona videos: {s['persona']}. Top 3 channels by videos: " +
                 "; ".join(f"{c} ({h}, tier {t}) {n}" for (c, h, t), n in top3) + ".\n")
        W.append("| # | Title | Channel | Views (tab) | Multiple | Age | ID |")
        W.append("|---:|---|---|---:|---:|---|---|")
        for i, v in enumerate(sorted(x, key=lambda v: -(v["views"] or 0))[:5], 1):
            W.append(f"| {i} | \"{md(v['title'])}\" | {md(v['channel'])} | {fv(v['views'])} | {fm(v['multiple'])} | "
                     f"{v['age_text']} | `{v['video_id']}` |")
        W.append("")

    # --- hand-check
    smp = sample(vids)
    W.append("## Hand-check: 100 random A-C HVAC titles (seed 2611)\n")
    W.append("`random.Random(2611).sample` of the A-C HVAC video IDs, sorted. I read each title and gave my own primary "
             "sub-niche under the same tie-break (a reading). \"First pass\" = the rule's tag when I first read the "
             "sample; \"rule now\" = after the fixes the sample led to (the rules were then re-run). Agreement after "
             "fixes is not an independent test, because the fixes were written from this sample.\n")
    if HANDCHECK:
        agree_first = sum(1 for v in smp if HANDCHECK.get(v["video_id"], ("?",))[0] in ("=", FIRST_PASS.get(v["video_id"])))
        def mine(v):
            m = HANDCHECK[v["video_id"]][0]
            return FIRST_PASS.get(v["video_id"], v["subniche"]) if m == "=" else m
        agree_now = sum(1 for v in smp if mine(v) == v["subniche"])
        agree_parent = sum(1 for v in smp if PARENT_OF.get(mine(v), mine(v)) == v["parent"])
        nothvac = sum(1 for v in smp if HANDCHECK[v["video_id"]][0] == "not HVAC")
        W.append(f"**Agreement (fine sub-niche): first pass {agree_first} of 100; after fixes {agree_now} of 100. At the "
                 f"labels.md parent level after fixes: {agree_parent} of 100.** {nothvac} of the 100 are not HVAC in my "
                 "reading (errors of the `is_hvac` title mark, not of this map; counted as disagreements).\n")
        W.append("| # | ID | Title | Rule first pass | Rule now | Mine | Agree now | Note |")
        W.append("|---:|---|---|---|---|---|:---:|---|")
        for i, v in enumerate(smp, 1):
            m = mine(v)
            W.append(f"| {i} | `{v['video_id']}` | \"{md(v['title'])}\" | {FIRST_PASS.get(v['video_id'], '-')} | "
                     f"{v['subniche']} | {m} | {'yes' if m == v['subniche'] else '**no**'} | {md(HANDCHECK[v['video_id']][1])} |")
        W.append("")
    else:
        W.append("(not yet filled)\n")
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(W) + "\n")
    return gaps


if __name__ == "__main__":
    chans, vids, typed, type_files = load()
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        for i, v in enumerate(sample(vids), 1):
            print(f"{i}\t{v['video_id']}\t{v['subniche']}\t{v['title']}")
    elif len(sys.argv) > 1 and sys.argv[1] == "unmapped":
        u = [v for v in vids if v["tier"] in ("A", "B", "C") and v["subniche"] == FALLBACK[0]]
        print(len(u))
        for v in random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 1).sample(u, min(200, len(u))):
            print(v["tier"], "|", v["title"][:120])
    elif len(sys.argv) > 1 and sys.argv[1] == "counts":
        ac = [v for v in vids if v["tier"] in ("A", "B", "C")]
        c = Counter(v["subniche"] for v in ac)
        for k, n in c.most_common():
            print(n, k)
        print(len(ac))
    else:
        write_csv(vids)
        build(vids, chans, typed, type_files)
        print("wrote", OUT_CSV, "and", OUT_MD)
