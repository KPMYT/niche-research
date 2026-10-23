#!/usr/bin/env python3
"""YouTube search autocomplete pull for the HVAC round 2 keyword list.

Written 2026-10-23 for studies/hvac/seeds/keywords-round2.md.

Usage:
    python3 autocomplete.py [out.json]     # pull (cached; re-runs fetch only missing queries)
    python3 autocomplete.py build          # filter, dedupe, label, write keywords-round2.csv

Calls the free YouTube suggest endpoint
    https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=en&gl=us&q=<query>
for every query in the plan below (topic seeds, audience framings, known-title
phrases and an a-z expansion of the 10 main seeds), 0.3 s apart.
Results are cached in the output JSON, so a re-run only fetches missing queries.
Autocomplete returns suggestion strings in the endpoint's own order; it gives
no search volumes, and none are inferred here.
"""
import json, os, string, subprocess, sys, time, urllib.parse
from datetime import datetime, timezone

OUT = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "build" else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "raw", "autocomplete-2026-10-23.json")
ENDPOINT = "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=en&gl=us&q="
PAUSE = 0.3

# topic code -> seeds. The first seed of each topic is its "noun" used with the framing templates.
TOPICS = {
    "ac-central":      ["ac", "air conditioner", "central air", "ac not cooling", "ac unit", "ac drain line", "ac tune up"],
    "ac-window":       ["window ac", "window air conditioner", "portable ac", "portable air conditioner"],
    "mini-split":      ["mini split", "ductless mini split", "mini split vs central air"],
    "heat-pump":       ["heat pump", "heat pump in winter", "heat pump vs furnace", "heat pump emergency heat"],
    "furnace":         ["furnace", "gas furnace", "furnace not working", "furnace pilot light", "furnace flame sensor"],
    "oil-furnace":     ["oil furnace", "oil boiler", "heating oil", "oil burner", "oil tank"],
    "boiler-steam":    ["boiler", "radiator", "steam radiator", "steam heat", "hot water baseboard", "bleeding radiators", "cast iron radiator"],
    "thermostat":      ["thermostat", "thermostat setting", "smart thermostat", "nest thermostat", "thermostat wiring"],
    "filters":         ["air filter", "furnace filter", "ac filter", "hvac filter", "merv filter"],
    "ducts-vents":     ["air ducts", "duct cleaning", "closing vents", "return vent", "air vents", "dampers hvac"],
    "parts":           ["capacitor", "ac capacitor", "contactor", "blower motor", "furnace igniter", "condensate pump", "hvac fuse", "ac disconnect"],
    "coil-cleaning":   ["condenser coil", "clean ac unit", "evaporator coil", "clean condenser"],
    "maintenance":     ["hvac maintenance", "furnace maintenance", "ac maintenance", "hvac tune up"],
    "energy-bill":     ["electric bill", "heating bill", "energy bill", "gas bill", "utility bill", "power bill"],
    "insulation":      ["insulation", "attic insulation", "spray foam", "rim joist insulation", "blown in insulation"],
    "drafts":          ["drafts", "weatherstripping", "drafty house", "door draft", "draft stopper", "caulking windows"],
    "windows":         ["windows", "window insulation", "window film", "thermal curtains", "storm windows", "replacement windows"],
    "humidity":        ["dehumidifier", "humidity in house", "humidifier", "whole house humidifier", "basement dehumidifier"],
    "indoor-air":      ["indoor air quality", "air purifier", "uv light hvac", "mold in ac", "carbon monoxide furnace"],
    "outage-heat":     ["power outage heat", "heat without power", "heat house without electricity", "stay warm without power", "generator furnace"],
    "brands":          ["best hvac brands", "best ac brands", "best furnace brands", "best heat pump brands", "hvac brands to avoid"],
    "refrigerant":     ["freon", "refrigerant", "r22", "r410a", "ac recharge", "refrigerant leak"],
    "ac-freezing":     ["ac freezing up", "ac frozen", "ice on ac", "frozen evaporator coil"],
    "short-cycling":   ["short cycling", "ac short cycling", "furnace short cycling"],
    "smells":          ["furnace smell", "ac smell", "burning smell furnace", "smell from vents"],
    "noises":          ["furnace noise", "ac noise", "loud furnace", "ac making noise", "banging radiator"],
    "scams-upsells":   ["hvac scam", "hvac scams", "hvac upsell", "hvac companies", "hvac technician", "hvac contractor"],
    "replacement-cost":["hvac replacement cost", "new ac cost", "new furnace cost", "replace ac", "replace furnace", "hvac quote"],
    "wood-stove":      ["wood stove", "pellet stove", "wood burning stove", "fireplace insert", "fireplace heat"],
    "space-heater":    ["space heater", "space heater vs central heat", "electric heater", "kerosene heater", "propane heater"],
    "ceiling-fan":     ["ceiling fan", "ceiling fan direction", "ceiling fan winter", "fan cooling"],
    "attic-fan":       ["attic fan", "whole house fan", "attic ventilation", "solar attic fan", "hot attic"],
    "keep-cool":       ["keep house cool", "cool house without ac", "cool a room", "hot room", "upstairs hot"],
    "keep-warm":       ["keep house warm", "heat house cheap", "warm house winter", "cold room", "heat a room"],
    "evap-cooler":     ["swamp cooler", "evaporative cooler"],
    "electric-heat":   ["baseboard heater", "electric baseboard heat", "radiant floor heating", "electric furnace"],
    "geothermal":      ["geothermal", "geothermal heat pump"],
    "home-warranty":   ["home warranty hvac", "hvac warranty"],
    "hvac-general":    ["hvac", "hvac tips", "hvac secrets", "hvac homeowner", "hvac diy"],
}

# The audience framings asked for in the helper brief, applied to each topic's first seed.
FRAMINGS = [
    "why is my {n}", "how to {n}", "how to fix {n}", "how to clean {n}", "stop {n}", "never {n}",
    "never do this {n}", "{n} mistakes", "don't {n}", "before you {n}", "before you turn on your {n}",
    "before you replace your {n}", "the only {n}", "{n} vs", "{n} secret", "{n} hack", "cheap {n}",
    "{n} save money", "save money {n}", "lower {n} bill", "{n} old house", "old house {n}", "{n} seniors",
    "{n} winter", "{n} summer", "{n} fall", "{n} spring", "{n} myth", "{n} scam", "{n} cost",
    "{n} problems", "{n} tips", "{n} trick", "{n} doesn't want you to know", "{n} companies hate",
]
# Topics whose noun reads as a thing you own ("why is my X"): all framings. Others: a shorter set.
SHORT_FRAMINGS = ["{n} mistakes", "{n} vs", "the only {n}", "{n} hack", "cheap {n}", "{n} save money",
                  "{n} old house", "{n} winter", "{n} summer", "{n} myth", "{n} cost", "{n} tips",
                  "{n} secret", "how to {n}", "{n} doesn't want you to know", "before you {n}"]
FULL_FRAMING_TOPICS = {"ac-central", "ac-window", "mini-split", "heat-pump", "furnace", "oil-furnace", "boiler-steam",
                       "thermostat", "filters", "ducts-vents", "parts", "energy-bill", "insulation", "humidity",
                       "wood-stove", "space-heater", "ceiling-fan", "attic-fan", "hvac-general", "keep-warm",
                       "keep-cool", "windows", "drafts"}
# Extra nouns that also get the full framing set.
EXTRA_NOUNS = {"heater": "furnace", "heat": "furnace", "air conditioning": "ac-central", "heating": "furnace",
               "radiators": "boiler-steam", "electric bill": "energy-bill", "heating bill": "energy-bill"}

# Phrases taken from known winning titles (findings/2026-10-22-hvac-and-electrical.md section 1 and
# recovered/2026-10-22-roger-sub-brands/research/lane2-trades.md).
KNOWN_TITLE_PHRASES = {  # phrase -> (topic, the known title it comes from)
    "hvac companies hate": ("scams-upsells", "HVAC Companies HATE That You Can Do This Yourself (739K)"),
    "hvac companies hope": ("scams-upsells", "5 AC Mistakes HVAC Companies Hope You Keep Making (Ray Dutton's Garage, 589K)"),
    "hvac companies don't want you to know": ("scams-upsells", "HVAC Companies HATE That You Can Do This Yourself (739K)"),
    "utility company doesn't want": ("energy-bill", "The Utility Company HATES This Air Conditioner (317K)"),
    "utility companies hate": ("energy-bill", "The Utility Company HATES This Air Conditioner (317K)"),
    "power company doesn't want you to": ("energy-bill", "Your Power Company Doesn't Want You To See This! (128K)"),
    "thermostat habits": ("thermostat", "The 5 Thermostat Habits That Wear Out Your AC Years Early (Ray Dutton's Garage, 1.1M)"),
    "before you turn on your heat": ("maintenance", "Before You Turn On Your Heat This Fall, Do This (Ray Dutton's Garage, 926K)"),
    "before you shut your ac down": ("maintenance", "Before You Shut Your AC Down This Fall, Do This (Ray Dutton's Garage, 1.1M)"),
    "before you turn on your ac": ("maintenance", "Before You Shut Your AC Down This Fall, Do This (Ray Dutton's Garage, 1.1M) [flipped to spring]"),
    "only hvac brands worth buying": ("brands", "The Only 5 HVAC Brands Worth Buying (HVAC Exposed, 571-576K)"),
    "ac brands worth buying": ("brands", "The Only 4 AC Brands Worth Buying in 2026 (Vent Exposed, 666K)"),
    "do this once a month ac": ("maintenance", "Do THIS Once a Month and Your AC Will Last 25 Years (John The HVAC Guy, 232K)"),
    "do this before winter furnace": ("maintenance", "Do THIS Before Winter and Your Furnace Will Last 30 Years (John The HVAC Guy, 176K)"),
    "turning your heat down": ("thermostat", "Turning Your Heat Down Is NOT Saving You Money... (Gus Whitaker, 74K)"),
    "keep your family warm during a power outage": ("outage-heat", "Keep Your Family Warm During A Power Outage By Installing This $5 Part (The DIY HVAC Guy, 4.2M)"),
    "heat a room with no power": ("outage-heat", "9 Ways I Keep One Room Warm With No Power (June's Kitchen Table, 151K)"),
    "keep bed warm with no heat": ("outage-heat", "9 Ways I Keep My Bed Warm With No Heat (June's Kitchen Table, 318K)"),
    "why is your heat bill so high": ("energy-bill", "THIS is Why Your Heat Bill is So High! Rim Joist Insulation (5.8M)"),
    "lower your electric bill": ("energy-bill", "Can This Device Actually Lower Your Electric Bill By 30%?? (2.6M)"),
    "home designs that stayed cool": ("keep-cool", "20 Forgotten Home Designs That Stayed Cool Before Air Conditioning (405K)"),
    "cool your attic": ("attic-fan", "This $0 Fix Cools Your Attic by 55F. Why Don't Roofers Tell You? (Candlelight Archives, 586K)"),
    "ac blow colder": ("ac-central", "The $5 Fix That Makes Your AC Blow 9 Degrees Colder... (Hank Cole, 156K)"),
    "make your ac run like new": ("ac-central", "Doing This Will Make Your AC Run Like NEW Again! (Exposi, 321K)"),
    "beating the hvac industry": ("scams-upsells", "How Smart Homeowners Are Beating the HVAC Industry (HVAC Exposed, 381K)"),
    "secret ac trick": ("ac-central", "This SECRET AC Trick is Only Known by 1% of HVAC Technicians (193K)"),
    "hvac technicians": ("scams-upsells", "This SECRET AC Trick is Only Known by 1% of HVAC Technicians (193K)"),
    "ac filter destroying": ("filters", "The $30 AC Filter Is Destroying Your HVAC System (Ray Dutton's Garage, 761K)"),
    "energy bill mistakes": ("energy-bill", "5 Energy Bill Mistakes Utility Companies Hope You Keep Making (Ray Dutton's Garage, 397K)"),
    "ac mistakes": ("ac-central", "5 AC Mistakes HVAC Companies Hope You Keep Making (Ray Dutton's Garage, 589K)"),
    "ac last 25 years": ("maintenance", "Do THIS Once a Month and Your AC Will Last 25 Years (John The HVAC Guy, 232K)"),
    "furnace last 30 years": ("maintenance", "Do THIS Before Winter and Your Furnace Will Last 30 Years (John The HVAC Guy, 176K)"),
    "heat your home all winter for free": ("outage-heat", "No Gas, No Wood: This DIY Stove Heats Your Home All Winter for FREE (Wes Tucker Prepping, 297K)"),
    "heats a room all winter with no power": ("outage-heat", "Why Don't Seniors Try This $10 Bucket of Salt That Heats a Room All Winter With No Power? (Jhon Construction, 570K)"),
    "ventilation tricks": ("keep-cool", "20 Old-House Ventilation Tricks... (193K)"),
    "radiator trick": ("boiler-steam", "Plumbers Used to Do Heat Too: The Radiator Trick My Old Partner Swore By (proposed hand-off title, not a published video)"),
    "cuts the oil bill": ("oil-furnace", "Plumbers Used to Do Heat Too: The Radiator Trick My Old Partner Swore By (Cuts the Oil Bill) (proposed hand-off title, not a published video)"),
    "$5 fix ac": ("ac-central", "The $5 Fix That Makes Your AC Blow 9 Degrees Colder... (Hank Cole, 156K)"),
    "turning your heat down is not saving you money": ("thermostat", "Turning Your Heat Down Is NOT Saving You Money... (Gus Whitaker, 74K)"),
}

# Keyword phrases cut from Silver Cymbal's seed titles (studies/hvac/seeds/silver-cymbal.md, round 1 seed helper,
# views as pulled there on 2026-10-23), plus the in-scope borderline and under-5-minute HVAC titles it lists.
SC = "Silver Cymbal title: "
SILVER_CYMBAL_PHRASES = {
    "central air conditioning not cooling": ("ac-central", SC + '"#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" (_b6p0fkWhCY, 4,307,728)'),
    "ac not cooling quick fix": ("ac-central", SC + '"#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" (_b6p0fkWhCY, 4,307,728)'),
    "unclog ac drain line": ("ac-central", SC + '"How to UNCLOG your AC DRAIN Condensate line FAST..." (qAxJb0J1HH0, 3,772,025)'),
    "water stains on ceiling from ac": ("ac-central", SC + '"How to UNCLOG your AC DRAIN Condensate line FAST - Water stains on Ceiling?..." (qAxJb0J1HH0, 3,772,025)'),
    "install your own air conditioning": ("mini-split", SC + '"Install your own AIR CONDITIONING in 4 HOURS! DIY Mini Split MR COOL" (Wejop_Rjpv0, 3,087,177)'),
    "diy mini split": ("mini-split", SC + '"Install your own AIR CONDITIONING in 4 HOURS! DIY Mini Split MR COOL" (Wejop_Rjpv0, 3,087,177)'),
    "window air conditioner not cooling": ("ac-window", SC + '"Window Air Conditioner Not Cooling? EASY Common Fix - How to Clean a Windows AC" (o8KQu_MlpoY, 2,363,606)'),
    "how to clean a window ac": ("ac-window", SC + '"Window Air Conditioner Not Cooling? EASY Common Fix - How to Clean a Windows AC" (o8KQu_MlpoY, 2,363,606)'),
    "clean mini split condenser": ("mini-split", SC + '"How to Clean Your Mini Split AC Condenser - Make it Cold Again" (DSNUyxZtrmo, 1,859,343)'),
    "central air conditioner condenser cleaning": ("coil-cleaning", SC + '"Central Air Conditioner Condenser Cleaning - How To - Make it COLD again!" (nsRHhU6q5RY, 1,454,183)'),
    "mr cool mini split install": ("mini-split", SC + '"How to Install a Mr Cool 18,000 BTU AC in Just 1 Day!" (zvFKD95z7IM, 1,296,956)'),
    "oil heat boiler how it works": ("oil-furnace", SC + '"Oil Heat Boilers - How it works - Understand the Basics" (5GbXgEYw5TE, 820,639)'),
    "battery powered air conditioner": ("ac-window", SC + '"EcoFlow Wave PORTABLE Battery Powered Air Conditioner 4000 BTU" (leEsPGaaru8, 698,976)'),
    "heat pumps leaving people cold": ("heat-pump", SC + '"Why Heat Pumps are now leaving people COLD" (BP1iDvKpNZA, 631,905)'),
    "single hose portable ac": ("ac-window", SC + '"This Tiny Portable AC can Keep Anyone COOL - 14,000 BTU Dreo - Single Hose Trigger Warning!" (NsPBamTmOPM, 527,951)'),
    "tiny portable ac": ("ac-window", SC + '"Say Goodbye to BIG Air Conditioners - This Tiny Portable AC Blows them Away!" (uObGbs4sGQY, 503,681)'),
    "stuck circulator pump": ("boiler-steam", SC + '"Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" (yCZqfnlBYW8, 470,352)'),
    "boiler no heat": ("boiler-steam", SC + '"Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" (yCZqfnlBYW8, 470,352)'),
    "change furnace filter the right way": ("filters", SC + '"Furnace Filter - How to Change it the Right Way & SAVE Money" (ED3bfesbE_Y, 388,617)'),
    "furnace filter save money": ("filters", SC + '"Furnace Filter - How to Change it the Right Way & SAVE Money" (ED3bfesbE_Y, 388,617)'),
    "heating oil vs gas": ("oil-furnace", SC + '"Why Heating Oil is BETTER than GAS - Explained" (GdTOl1WcHV0, 343,444)'),
    "replace circulator pump boiler": ("boiler-steam", SC + '"How to Replace a Circulator Pump on a Boiler" (flpbqJu2sT8, 236,222)'),
    "install ductless ac and heating": ("mini-split", SC + '"How To install Split Ductless AC & Heating System // Start to Finish - 1 PERSON!" (kEWzIfnIhUw, 221,217)'),
    "no heat troubleshooting": ("furnace", SC + '"Top 10 Heating Problems EASY Fixes for No HEAT - Boiler / Furnace Troubleshooting OIL HEAT" (Xd-Og809TUo, 216,421)'),
    "oil heat troubleshooting": ("oil-furnace", SC + '"Top 10 Heating Problems EASY Fixes for No HEAT - Boiler / Furnace Troubleshooting OIL HEAT" (Xd-Og809TUo, 216,421)'),
    "best portable air conditioner": ("ac-window", SC + '"The BEST Portable Air Conditioner Just Got BETTER for 2026" (OGVXmIZtEG8, 65,273)'),
    "mini split hidden features": ("mini-split", SC + '"3 Unknown Features on Mr Cool Mini Split Air Conditioners" (cC-J0ZCUH28, 32,326)'),
    "pellet stove tax credit": ("wood-stove", SC + '[borderline, lean include] "Everyone will be buying pellet stoves after learning this news" (9d9TL02idO4, 1,399,618)'),
    "spray foam alternative": ("insulation", SC + '[borderline, operator call] "Spray Foam is Expensive. Use THIS Instead!" (sHL4lBAhklA, 1,519,132)'),
    "garage door seal": ("drafts", SC + '[borderline, operator call] "How to Make Your Garage Door SEAL TIGHT as a Fridge" (EjLJm0g4whg, 906,215)'),
    "crawl space encapsulation": ("humidity", SC + '[borderline, operator call] "MINDBLOWING Crawlspace Transformation - Next Level ENCAPSULATION" (CXjNHwFg0aQ, 242,232)'),
    "staying warm when the power is out": ("outage-heat", SC + '[under 5 min] "Best Kept Secret for Staying Warm When the Power is Out" (SIyntnwE7O8, 43,932)'),
    "zone valve no heat": ("boiler-steam", SC + '[under 5 min] "No Heat? How to Replace & Troubleshoot a Taco Zone Valve" (xuswKBmauI4, 136,871)'),
    "cheapest air conditioner": ("ac-window", SC + '[under 5 min] "TESTING the CHEAPEST AIR CONDITIONER on Amazon" (JDq4i_lT8YI, 174,583)'),
    "dual hose portable air conditioner": ("ac-window", SC + '[under 5 min] "BEST Portable Air Conditioner I have ever tested - DUAL HOSE" (NI-KNyp9tdQ, 519,566)'),
}

ALPHA_SEEDS = ["ac", "furnace", "heat pump", "thermostat", "air filter", "electric bill", "heating bill",
               "boiler", "hvac", "insulation"]


def plan():
    q = {}
    def add(query, topic, kind):
        query = " ".join(query.split())
        if query and query not in q:
            q[query] = {"topic": topic, "kind": kind}
    for t, seeds in TOPICS.items():
        for s in seeds:
            add(s, t, "seed")
        n = seeds[0]
        for f in (FRAMINGS if t in FULL_FRAMING_TOPICS else SHORT_FRAMINGS):
            add(f.format(n=n), t, "framing")
    for n, t in EXTRA_NOUNS.items():
        for f in FRAMINGS:
            add(f.format(n=n), t, "framing")
    for p, (t, _title) in KNOWN_TITLE_PHRASES.items():
        add(p, t, "known-title")
    for p, (t, _title) in SILVER_CYMBAL_PHRASES.items():
        add(p, t, "silver-cymbal")
    for s in ALPHA_SEEDS:
        t = next((k for k, v in TOPICS.items() if s in v), "hvac-general")
        for ch in string.ascii_lowercase:
            add(f"{s} {ch}", t, "alphabet")
    return q


def fetch(query):
    url = ENDPOINT + urllib.parse.quote(query)
    for attempt in range(3):
        r = subprocess.run(["curl", "-sS", "-m", "20", url], capture_output=True, text=True)
        try:
            data = json.loads(r.stdout)
            return data[1]
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    return None


def main():
    db = {}
    if os.path.exists(OUT):
        with open(OUT) as f:
            db = json.load(f)
    db.setdefault("meta", {
        "endpoint": ENDPOINT + "<query>",
        "pulled": "2026-10-23",
        "note": "YouTube search autocomplete (ds=yt), English/US. Suggestions are in the endpoint's order. No volumes.",
    })
    res = db.setdefault("queries", {})
    p = plan()
    todo = [k for k in p if k not in res or res[k].get("suggestions") is None]
    print(f"plan {len(p)} queries, {len(todo)} to fetch", flush=True)
    for i, query in enumerate(todo, 1):
        sugg = fetch(query)
        res[query] = dict(p[query], suggestions=sugg,
                          fetched_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
        if i % 50 == 0:
            with open(OUT, "w") as f:
                json.dump(db, f, indent=1)
            print(f"{i}/{len(todo)}", flush=True)
        time.sleep(PAUSE)
    with open(OUT, "w") as f:
        json.dump(db, f, indent=1)
    failed = [k for k, v in res.items() if v.get("suggestions") is None]
    print(f"done. queries {len(res)}, failed {len(failed)}", flush=True)


# ---------------------------------------------------------------------------
# build: filter to HVAC, dedupe, label topic and framing, mark priority, write CSV
# ---------------------------------------------------------------------------
import re

BRIEF_TOPICS = {"ac-central", "ac-window", "mini-split", "heat-pump", "furnace", "oil-furnace", "boiler-steam",
                "thermostat", "filters", "ducts-vents", "parts", "coil-cleaning", "maintenance", "energy-bill",
                "insulation", "drafts", "windows", "humidity", "indoor-air", "outage-heat", "brands", "refrigerant",
                "ac-freezing", "short-cycling", "smells", "noises", "scams-upsells", "replacement-cost",
                "wood-stove", "space-heater", "ceiling-fan", "attic-fan"}
# helper-added topics: keep-cool, keep-warm, evap-cooler, electric-heat, geothermal, home-warranty, hvac-general

STRONG = re.compile(r"hvac|furnace|heat ?pump|air condition|mini[ -]?splits?|ductless|thermostat|"
                    r"contactor|blower motor|igniter|ignitor|flame sensor|evaporator coil|freon|refrigerant|"
                    r"\br-?22\b|r-?410a?|r-?454|dehumidif|humidifier|spray foam|weather ?strip|baseboard heat|"
                    r"space heaters?|wood ?stoves?|wood burning stove|pellet stoves?|kerosene heater|propane heater|"
                    r"swamp cooler|evaporative cooler|geothermal|ceiling fans?|attic fan|attic insulation|"
                    r"whole house fan|\belectric bills?\b|\benergy bills?\b|\bgas bills?\b|\butility bills?\b|"
                    r"\bpower bills?\b|\bheating bills?\b|\belectricity bills?\b|\blight bills?\b|heating oil|"
                    r"oil burner|oil furnace|steam heat|steam radiator|cast iron radiator|\bducts?\b|ductwork|"
                    r"short cycl|\bmerv\b|nest thermostat|ecobee|air purifier|indoor air|carbon monoxide|"
                    r"power outage|window ac|portable ac|\bac units?\b|central air|central ac|home warranty|drafty|"
                    r"draft stopper|draft blocker|hydronic|heating system|cooling system|electric heat|radiant floor|"
                    r"fireplace insert|heat exchanger|condensate|utility compan|power compan|without power|"
                    r"no power\b|without electricity|no electricity|without heat|no heat\b|without ac\b|no ac\b|"
                    r"air vents?|blown in insulation|rim joist|ac capacitor|hvac capacitor|run capacitor|"
                    r"start capacitor|condenser coil|condenser fan|ac condenser|air quality|zone valve|crawl ?space|"
                    r"weather seal|door seals?\b|\bwarmer\b.*\b(house|home|room)\b")
WEAK = re.compile(r"\bac\b|\ba/c\b|\bheat(ing|er|ers)?\b|\bcool(ing)?\b|\bwarm\b|\bcold\b|\bfilters?\b|\bvents?\b|"
                  r"\bwindows?\b|\bfans?\b|\bmold\b|\bhumidity\b|\bfireplace\b|\bgenerator\b|\bcurtains?\b|"
                  r"\bcaulk|\bdrafts?\b|\bcoils?\b|\bstove\b|\bchimney\b|\bpropane\b|\bkerosene\b|\bfreezing\b|"
                  r"\bhot\b|\benergy\b|\bthermal\b|\bcondensation\b|\bboilers?\b|\bradiators?\b|\bcapacitors?\b|"
                  r"\battic\b|\binsulat\w*|\bcondenser\b|\bsteam\b|\bpilot light\b")
CONTEXT = re.compile(r"\bhouse\b|\bhome\b|\broom\b|bedroom|basement|\battic|apartment|upstairs|\bwinter\b|"
                     r"\bunit\b|not cooling|not working|not heating|blowing|leaking|freez|frozen|\bbill\b|"
                     r"\bair\b|\bcentral\b|\bwindow ac\b|outside unit|compressor|\bdrain\b|breaker|"
                     r"\bseer\b|\bton\b|\binstall|\brepair|\bmaintenance|\bclean|\btune|\bhvac\b|\bfurnace\b|"
                     r"\bduct|cheap|save money|\bdoor\b|\bstorm\b|\bfilm\b|\binsulat|\bfloor\b|\bwall\b|"
                     r"\bceiling\b|\bfirewood\b|\bwood\b|\bpower outage\b|\bno power\b|\bthermostat\b|"
                     r"\bkeep\b|\bwithout\b|\bcheaply\b|\bdiy\b|\btips\b|\bhack|\bmistake|\bfix\b|\bnoise|\bsmell|"
                     r"\bcapacitor|\bcoil|\bfreon|\bwater\b|\bice\b|\bturn(ing)? (on|off)\b|\bvs\b|"
                     r"\bbrands?\b|\bcost\b|\bsystem\b|\belectric\b|\bgas\b|\boil\b|\bsenior|\bleak|\bpressure\b|"
                     r"\bvalve|\bbleed|\bbanging|\bpipes?\b|\bbaseboard|\bthermal|\bfiberglass|\bspray|\bfoam\b|"
                     r"\bbattery\b|\bpellet|\bburn|\bplumb|\bvent|\bheater|\bheating\b|\bproblems?\b|\btrouble|"
                     r"\bnot\b|\bwon'?t\b|\bsymptoms?\b|\bold\b|\bbest\b|\bworth\b|replacement|\bpump\b|\btank\b|"
                     r"overheat|piping|safet|\bseal|encapsul|compan|stop working|turn (the )?heat|expansion")
EXCLUDE = re.compile(r"\bcar\b|\bcars\b|\bauto\b|vehicle|\btruck|\bjeep\b|honda|toyota|\bford\b|chevy|chevrolet|bmw|"
                     r"nissan|hyundai|\bkia\b|tesla|subaru|dodge|\bram 1500|silverado|f-?150|\brv\b|camper|\bvan\b|"
                     r"\bboat\b|motorcycle|engine|coolant|minecraft|\bgame\b|gaming|\bgta\b|fortnite|roblox|valhalla|"
                     r"assassin|ac ?/ ?dc|\bac dc\b|\bmilan\b|\bsong\b|lyrics|\bmusic\b|anime|\bmovie|\basmr\b|"
                     r"white noise|sleep(ing)? sound|\bhours?\b|\b10 hr|\bambien|crackling|relaxing|\b4k\b|"
                     r"\bhindi\b|\btamil\b|\burdu\b|telugu|bangla|kannada|malayalam|\bkaise\b|\bkya\b|\bwala\b|"
                     r"\bmein\b|\bka\b|\bki\b|\bke\b|\bse\b|\bcomo\b|\bpara\b|\baire\b|india|pakistan|bangladesh|"
                     r"philippines|dubai|nigeria|\bpc\b|\bcpu\b|laptop|\bphone|iphone|aquarium|fish tank|chicken|"
                     r"\bdogs?\b|\bcats?\b|reptile|greenhouse|\btent\b|grow tent|water heater|hot water heater|"
                     r"tankless|heat press|heat gun|heat transfer|heat rash|heat stroke|heat exhaustion|"
                     r"\bnfl\b|fantasy|windows 1[01]|windows 7|microsoft|\bvinyl\b|frozen pipe|pipes? freez|"
                     r"pool heater|hot tub|\bspa\b|sauna|air fryer|\bfridge|refrigerator|freezer|ice maker|"
                     r"\bcake\b|recipe|cooking|\bgrill\b|\bsmoker\b|\bdryer\b|\bgenerator review|\btiktok|"
                     r"youtube shorts|#shorts|\bmeme|\bprank|funny|\bkids?\b|cartoon|\bdrawing|\bpaint(ing)?\b|"
                     r"radiator (fan|cap|flush|fluid|hose)|\bcoolant\b|\bmilwaukee\b|\bdewalt\b|\bryobi\b|"
                     r"\bmakita\b|\bfinger|\bbody\b|\bskin\b|\bhair\b|\bface\b|\bfeet\b|\bbaby\b|\bpet\b|"
                     r"ventriloquis|\bvent(ing)? (session|video)|\bfan ?made\b|\bfanmade\b|\bfans? (react|edit)|"
                     r"\bfan art\b|\bhot (dog|wheels|ones|sauce|girl|take)|\bcold (case|war|open|play|plunge|"
                     r"shower|brew|turkey)|\bwarm up\b|\bfire stick|\bfirestick|\bboiler room\b|\bboilermaker|"
                     r"windows? (xp|vista|update|install|server|key|activation)|\bpanes?\b of glass|"
                     r"\bac vs dc\b|\bdc\b|oil tanker|natok|outcome memories|secret door|\bmods?\b|"
                     r"steel furnace|blast furnace|terraria|stardew|valheim|factorio|satisfactory|\bark\b|"
                     r"resistor|1\.5 ton|voltas|lloyd|blue ?star|godrej|price in\b|\brs\.? ?\d|"
                     r"\bmotherboard|\bgpu\b|\bbike\b|\bscooter|\bmower|\bcompanion\b|\bpokemon|"
                     r"\bwow\b|\bskyrim|\bzelda|\bsims\b|\btarkov|\bdayz\b|\bvalorant|\bfire red\b|"
                     r"sonic|\bfnf\b|clash|royale|\brust\b|don'?t starve|egg boiler|espresso|breville|coffee|"
                     r"check online|\bapp\b|bkash|\bksa\b|\bodia\b|bengal|manipur|gpay|paytm|\bbo6\b|black ops|"
                     r"warzone|\bcod\b|\bunity\b|odyssey|origins|shadows|syndicate|mirage|thermostat housing|"
                     r"\bdd15\b|mercedes|furrion|shower|family guy|spongebob|remix|sparta|breast milk|"
                     r"thermodynamic|softening|engineering|chemistry|cabin (air )?filter|cold air intake|fuel filter|velocity stack|"
                     r"exhaust (system|manifold|tip|sound)|melting|induction furnace|calentador|punju|geyser|murgi|ranna|steamos|\bshark\b|"
                     r"vacuum|k&n|splendor|pulsar|\bbmc\b|\bfz\b|kettle|instant pot|pressure cooker|thermistor|"
                     r"leadership|diverter|\buk\b|ireland|australia|\bcombi\b|\bmath\b|problem solving|"
                     r"problem application|application form|download|pay online|name change|\bpumped\b|\bnatok\b|\bvlog\b|\bgta\b|"
                     r"\bmlbb\b|free fire|\bpubg\b|\bbgmi\b|\bstalker\b|\bterraria|\boutpost\b|"
                     r"skins?\b|\bemote|secret base|\bboss\b|secret level|\bost\b|\bwalkthrough|\bgameplay|"
                     r"\bdriving\b|\bturbo|predator \d|lid flip|ar condicionado|springer|dielectric|capacitance|equations|inductors|"
                     r"in circuits|grade 1\d|capacitor (arrangement|bipolar|assets|business|company|esc)|nfs heat|cover song|\(cover\)|\bcover by\b|billie|eilish|brockhampton|saigon|neko case|lullaby|football|gold rush|\bxcx\b|"
                     r"zenekar|mekanism|heroes|juniors|\birl\b|division 2|unboxing|eggman|baba is you|activate|"
                     r"draft tips|mock draft|draft picks?|\bjee\b|react native|\bkvl\b|lavadora|daewoo|delhi|mumbai|"
                     r"bangalore|chennai|hyderabad|karachi|lahore|dhaka|\bnepal|\bsri lanka|\bkenya|\bghana|"
                     r"\bmicrophone|\bmic\b|\bguitar|\bamp\b|\bamplifier|\bspeaker|\baudio|\bpedal|\bsynth|"
                     r"\bpcb\b|\barduino|\bphysics|\bclass 1[0-2]|\bformula\b|\bderivation|\bnumericals?|"
                     r"\bsteam deck|\bsteam game|\bsteam (sale|account|workshop|link|wallet|summer sale)|\bon steam\b|"
                     r"\bfull steam|\bsteamboat|\bsteam engine|\bsteam train|\blocomotive|\btrain\b|"
                     r"\bxbox\b|\bps[45]\b|\bplaystation|\bnintendo|\bswitch 2\b")

TOPIC_RULES = [
    (r"power outage|without power|no power|without electricity|no electricity|generator|blackout(?! curtain)", "outage-heat"),
    (r"short cycl", "short-cycling"),
    (r"freez|frozen|\bice\b|icing", "ac-freezing"),
    (r"smell|odor|odour|stink", "smells"),
    (r"noise|noisy|\bloud\b|bang|squeal|humming|buzz|click|rattl|whistl|knock|screech|vibrat", "noises"),
    (r"freon|refrigerant|\br-?22\b|r-?410|r-?454|recharge|refill", "refrigerant"),
    (r"capacitor|contactor|blower motor|igniter|ignitor|flame sensor|condensate pump|\bfuse\b|disconnect|"
     r"limit switch|inducer|pressure switch|circuit board|control board|\brelay\b|transformer|compressor|"
     r"thermocouple|pilot light|\bbelt\b|fan motor|\bbreaker\b", "parts"),
    (r"scam|upsell|rip ?off|technician|contractor|compan(y|ies) (hate|hope|don)|hvac compan|\bhvac guy|"
     r"\bquote\b|hvac industry|hvac tech\b|hvac techs\b|dishonest|overcharg|\btricks? (hvac|they)", "scams-upsells"),
    (r"\bbrands?\b|worth buying|\bcarrier\b|\btrane\b|lennox|goodman|rheem|daikin|mitsubishi|bryant|\byork\b|"
     r"\bruud\b|amana|fujitsu|\blg\b|midea|gree\b|pioneer|mrcool|mr cool|american standard|\bworst\b|to avoid",
     "brands"),
    (r"filter", "filters"),
    (r"thermostat|\bnest\b|ecobee|honeywell|temperature setting|set (the|your) (heat|ac|temp)|heat down", "thermostat"),
    (r"warranty", "home-warranty"),
    (r"(cost|price|how much|quote).*(ac\b|air condition|furnace|hvac|heat pump|boiler|mini ?split|system|unit)|"
     r"(ac\b|air condition|furnace|hvac|heat pump|boiler|mini ?split|system|unit).*(cost|price|how much)|"
     r"replace(ment)? (your |the |my |an |a )?(ac|air condition|furnace|hvac|heat pump|boiler|system|unit)|"
     r"new (ac|furnace|hvac|heat pump|air condition)|replace or repair|repair or replace", "replacement-cost"),
    (r"\bducts?\b|ductwork|\bvents?\b|register|damper|return air", "ducts-vents"),
    (r"condenser|\bcoils?\b|\bfins?\b|clean(ing)? (the |your |my )?(ac|air condition|outside|outdoor)", "coil-cleaning"),
    (r"mini[ -]?split|ductless", "mini-split"),
    (r"window (ac|air|unit)|portable (ac|air)|window air", "ac-window"),
    (r"heat ?pump", "heat-pump"),
    (r"\boil (furnace|boiler|burner|tank|heat|heater)|heating oil|oil fired|oil bill", "oil-furnace"),
    (r"boiler|radiator|steam|hot water baseboard|hydronic", "boiler-steam"),
    (r"baseboard|radiant floor|electric furnace|electric heat\b|heated floor", "electric-heat"),
    (r"wood ?stove|pellet|wood burn|fireplace|firewood|chimney|\bstove\b", "wood-stove"),
    (r"geothermal", "geothermal"),
    (r"swamp cooler|evaporative", "evap-cooler"),
    (r"insulat|spray foam|blown in|fiberglass|rim joist|cellulose", "insulation"),
    (r"attic|whole house fan|soffit|ridge vent", "attic-fan"),
    (r"ceiling fan|box fan|fan direction|(?<!hvac )(?<!furnace )(?<!ac )(?<!blower )\bfans?\b", "ceiling-fan"),
    (r"weather ?strip|draft|caulk|door sweep|air seal", "drafts"),
    (r"window|curtain|blinds|shades", "windows"),
    (r"dehumidif|humidif|humidity|condensation|damp", "humidity"),
    (r"purifier|air quality|\bmold\b|mould|uv light|carbon monoxide|\bdust|allerg|clean air", "indoor-air"),
    (r"space heater|kerosene|propane heater|electric heater|oil filled|\bheaters?\b", "space-heater"),
    (r"bill|save energy|energy sav|utility|power compan|electric compan|kwh|energy efficien|electricity", "energy-bill"),
    (r"maintenance|tune ?up|service|checklist|before (winter|summer|fall)|\bfall\b|\bspring\b|once a month|"
     r"every month|last \d+ years|shut (your |the )?ac|turn on (your |the )?(heat|ac|furnace)", "maintenance"),
    (r"furnace|gas heat|heating system", "furnace"),
    (r"keep .*cool|cool (house|room|down|a room|your|the)|without ac|no ac\b|hot (room|house|upstairs|attic)|"
     r"upstairs|heat wave|stay cool|beat the heat", "keep-cool"),
    (r"keep .*warm|\bwarm\b|cold (room|house|floor)|heat (a|the|your|my) (room|house|home)|stay warm|heat house", "keep-warm"),
    (r"\bac\b|air condition|central air|not cooling|cooling", "ac-central"),
    (r"hvac", "hvac-general"),
]
TOPIC_RULES = [(re.compile(p), t) for p, t in TOPIC_RULES]

FRAMING_RULES = [
    ("X vs Y", r"\bvs\.?\b|\bversus\b|compared to|better than|which is better|\bor\b.*\b(better|cheaper)\b"),
    ("the only X", r"\bthe only\b|worth buying|\bbest\b.*\bbrands?\b|\bbrands?\b.*\b(avoid|best|worst|worth)\b|\bworst\b|"
                   r"\bonly \d|\btop \d+\b|best .*to buy|which .* to buy|\bbest\b"),
    ("before you", r"\bbefore you\b|before (winter|summer|fall|spring|turning|the cold)"),
    ("they don't want you to know", r"don'?t want you to|doesn'?t want you|\bhates?\b|\bhope you\b|\bsecrets?\b|"
                                    r"don'?t tell|won'?t tell|nobody tells|never tell|\bscams?\b|\bscammers?\b|upsell|"
                                    r"rip ?off|exposed|truth about|\blies\b|beating the|overcharg|dishonest|"
                                    r"\bonly known\b|tricks? (hvac|they)|\b1%"),
    ("mistakes", r"mistake|\bnever\b|\bdon'?t\b|\bdo not\b|stop (doing|using|turning|running|setting|closing|buying|"
                 r"wasting)|\bwrong\b|\bbad idea|\bruin|\bdestroy|\bkilling\b|wearing out|wear out|habits"),
    ("myth", r"\bmyths?\b|\breally\b|\bactually\b|\bdoes\b.*\b(work|save|help)\b|\bdo\b.*\b(work|save|help)\b|"
             r"\bis it (worth|true|bad|safe|ok|okay|better|cheaper)|worth it|\btrue\b|should (i|you)|"
             r"\bis it\b|not saving|\bdebunk"),
    ("cheap hack", r"\bhacks?\b|\btricks?\b|\bcheap|\bdiy\b|\$\d|\bfree\b|\bbudget\b|without (ac|power|electricity|heat)|"
                   r"no (power|electricity)\b|save money|saving money|lower (your |my |the )?([a-z]+ )?bills?|"
                   r"cut .*bills?|reduce|\bsave on\b|\bsave\b|blow colder|run like new|colder air"),
    ("cost", r"\bcost|\bprices?\b|how much|expensive|\bquotes?\b|\bworth\b|\bpay\b"),
    ("problem symptom", r"why is my|why does my|why is the|\bnot (working|cooling|heating|blowing|turning|coming|kicking|"
                        r"running|igniting|lighting|staying|getting|reaching|shutting)|won'?t|wont |keeps|leak|freez|"
                        r"frozen|\bice\b|icing|smell|odor|noise|noisy|\bloud\b|bang|squeal|humming|buzz|click|"
                        r"\btripping|short cycl|blowing (hot|cold|warm)|high (electric|energy|gas|heating|power|utility)?"
                        r" ?bills?|too (hot|cold|humid)|cold air|hot air|warm air|blink|problems?|trouble|broken|"
                        r"\bdead\b|stopped|condensation|\bmold\b|\bwet\b|dripping|sweating|uneven|cold spots?|"
                        r"\bhot (upstairs|room|spots?)|always running|running constantly|runs constantly|"
                        r"so high|\berror\b|\bcode\b|flashing|\bhigh\b|clog|not on\b|starts then|then stops|not firing|"
                        r"won'?t start|no heat\b|no cool|symptoms?|troubleshoot|\bbad\b|failing|failure|"
                        r"\bweak\b|\bslow\b|\btripp|\blosing\b"),
    ("how-to", r"\bhow to\b|\bhow do\b|\binstall|\breplac|\bclean|\bfix|\brepair|\bset(ting|tings)?\b|\bwire|\bwiring|"
               r"\btest|\bcheck|\bchange|\breset|\bbleed|\bmaintenance|tune ?up|step by step|\bguide\b|\btips\b|"
               r"\bdiy\b|\bdo this\b|\bways\b|\bwhat to do\b|\bbuild|\bmake\b|\bkeep\b|\bdrain\b|\bflush|"
               r"\bservice|\blight(ing)? (a|the|pilot)|\binsulate|\bseal|\bunclog|\bcharge|\bsize|\bsizing"),
]
FRAMING_RULES = [(f, re.compile(p)) for f, p in FRAMING_RULES]
FRAMINGS_ORDER = ["plain topic", "problem symptom", "mistakes", "X vs Y", "the only X", "before you",
                  "they don't want you to know", "cheap hack", "myth", "how-to", "cost"]


def is_hvac(k):
    if EXCLUDE.search(k):
        return False
    if STRONG.search(k):
        return True
    weak = WEAK.findall(k)
    return bool(weak and (CONTEXT.search(k) or len(weak) >= 2))


def topic_of(k, fallback):
    for rx, t in TOPIC_RULES:
        if rx.search(k):
            return t
    return fallback


def framing_of(k):
    for f, rx in FRAMING_RULES:
        if rx.search(k):
            return f
    return "plain topic"


def norm(k):
    k = k.lower().replace("\u2019", "'").strip()
    k = re.sub(r"\s+", " ", k)
    return k


def build():
    here = os.path.dirname(os.path.abspath(__file__))
    raw = os.path.join(here, "..", "raw")
    db = json.load(open(os.path.join(raw, "autocomplete-2026-10-23.json")))
    res = db["queries"]
    plan_q = plan()
    rows = {}  # keyword -> dict

    def add(k, topic_fallback, source, src_kind):
        k = norm(k)
        if not k:
            return
        if k in rows:
            if source not in rows[k]["sources"]:
                rows[k]["sources"].append(source)
            return
        rows[k] = {"keyword": k, "topic": topic_of(k, topic_fallback), "framing": framing_of(k),
                   "sources": [source], "kind": src_kind}

    # 1. brief / helper seeds
    for t, seeds in TOPICS.items():
        for s in seeds:
            add(s, t, "brief topic list" if t in BRIEF_TOPICS else "helper-added seed", "seed")
    # 2. known-title phrases
    for p, (t, title) in KNOWN_TITLE_PHRASES.items():
        add(p, t, f"known title: {title}", "known-title")
    # 4. phrases from Silver Cymbal's titles (hand-cut, see SILVER_CYMBAL_PHRASES)
    sc_path = os.path.join(here, "..", "..", "seeds", "silver-cymbal.md")
    sc_titles = sorted({v[1] for v in SILVER_CYMBAL_PHRASES.values()})
    for p, (t, title) in SILVER_CYMBAL_PHRASES.items():
        add(p, t, title, "silver-cymbal")

    # 3. autocomplete, in plan order (the first query that returned a suggestion is its source)
    dropped = []
    for q in plan_q:
        r = res.get(q)
        if not r or not r.get("suggestions"):
            continue
        for s in r["suggestions"]:
            sn = norm(s)
            if not is_hvac(sn):
                dropped.append(sn)
                continue
            add(sn, plan_q[q]["topic"], f'autocomplete of "{q}"', "autocomplete")
    for k, r in rows.items():
        r["priority"] = "PRIORITY" if k in PRIORITY else "EXTENDED"
    missing = [k for k in PRIORITY if k not in rows]
    out = os.path.join(raw, "keywords-round2.csv")
    import csv
    order = sorted(rows.values(), key=lambda r: (r["priority"] != "PRIORITY", r["topic"],
                                                 FRAMINGS_ORDER.index(r["framing"]), r["keyword"]))
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["keyword", "topic", "framing", "source", "priority"])
        for r in order:
            w.writerow([r["keyword"], r["topic"], r["framing"], "; ".join(r["sources"]), r["priority"]])
    if os.environ.get("BUILD_REPORT"):  # optional debug dump (scratch path), not part of the outputs
        json.dump({"dropped_non_hvac": sorted(set(dropped)), "priority_missing": missing,
                   "silver_cymbal_titles": sc_titles}, open(os.environ["BUILD_REPORT"], "w"), indent=1)
    write_md(rows, res, plan_q, dropped, sc_titles, sc_path)
    print(f"keywords {len(rows)}, priority {sum(r['priority']=='PRIORITY' for r in rows.values())}, "
          f"missing priority {missing}, dropped suggestions {len(set(dropped))}, "
          f"silver cymbal titles {len(sc_titles)}")


TOPIC_NAMES = {
    "ac-central": "AC: central air", "ac-window": "AC: window and portable", "mini-split": "Mini-splits",
    "heat-pump": "Heat pumps", "furnace": "Furnaces (gas)", "oil-furnace": "Oil furnaces and oil heat",
    "boiler-steam": "Boilers, radiators, steam (old-house heat)", "electric-heat": "Electric and baseboard heat",
    "thermostat": "Thermostats", "filters": "Filters", "ducts-vents": "Ducts and vents",
    "parts": "Parts homeowners touch (capacitors, contactors, igniters...)", "coil-cleaning": "Condenser and coil cleaning",
    "maintenance": "Seasonal maintenance", "energy-bill": "Energy bills", "insulation": "Insulation",
    "drafts": "Drafts and weatherstripping", "windows": "Windows, film, curtains", "humidity": "Humidity, dehumidifiers, humidifiers",
    "indoor-air": "Indoor air (purifiers, mold, CO)", "outage-heat": "Heat (and cooling) in a power outage",
    "brands": "Brand verdicts", "refrigerant": "Refrigerant / Freon", "ac-freezing": "AC freezing up",
    "short-cycling": "Short cycling", "smells": "Smells", "noises": "Noises", "scams-upsells": "HVAC scams, upsells, contractors",
    "replacement-cost": "Replacement cost, repair or replace", "wood-stove": "Wood and pellet stoves, fireplaces",
    "space-heater": "Space heaters", "ceiling-fan": "Ceiling fans and fans", "attic-fan": "Attic fans, whole-house fans, hot attics",
    "keep-cool": "Keeping the house cool (no-AC tricks)", "keep-warm": "Keeping the house warm cheaply",
    "evap-cooler": "Swamp / evaporative coolers", "geothermal": "Geothermal", "home-warranty": "Home warranties",
    "hvac-general": "HVAC general",
}


def md_escape(s):
    return s.replace("|", "\\|")


def write_md(rows, res, plan_q, dropped, sc_titles, sc_path):
    from collections import Counter
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "..", "seeds", "keywords-round2.md")
    allr = list(rows.values())
    pri = [r for r in allr if r["priority"] == "PRIORITY"]
    ext = [r for r in allr if r["priority"] != "PRIORITY"]
    nq = len(res)
    nq_nonempty = sum(1 for v in res.values() if v.get("suggestions"))
    nsugg = sum(len(v.get("suggestions") or []) for v in res.values())
    nuniq = len({norm(s) for v in res.values() for s in (v.get("suggestions") or [])})
    kinds = Counter(v["kind"] for v in plan_q.values())
    src_kind = Counter(r["kind"] for r in allr)
    by_topic = Counter(r["topic"] for r in allr)
    by_topic_p = Counter(r["topic"] for r in pri)
    by_fr = Counter(r["framing"] for r in allr)
    by_fr_p = Counter(r["framing"] for r in pri)
    L = []
    a = L.append
    a("# HVAC round 2: the keyword list for the keyword sweep")
    a("")
    a("Built 2026-10-23 by a round 1 helper, for deliverable 8 of `RESEARCH-BRIEF.md` (the keyword sweep). "
      "Each PRIORITY keyword is to be searched on YouTube four ways (relevance, newest, oldest, most viewed); "
      "EXTENDED keywords get a relevance search only.")
    a("")
    a("**Status:** not yet re-checked by a second helper (working rule 3). The topic and framing labels are a "
      "rule-based reading of the keyword's words, not a measurement.")
    a("")
    a("Files: this page; `studies/hvac/data/raw/keywords-round2.csv` (every keyword: keyword, topic, framing, source, "
      "priority); `studies/hvac/data/raw/autocomplete-2026-10-23.json` (every autocomplete query and its raw "
      "suggestions, with fetch times); `studies/hvac/data/tools/autocomplete.py` (the pull, plus `build`, which makes "
      "the CSV and this page).")
    a("")
    a("## Method")
    a("")
    a("1. **Brief topics.** Each topic in `RESEARCH-BRIEF.md` section 1 (and the helper brief's longer list) became "
      "a topic code with 1 to 8 plain seeds (for example `furnace`, `oil furnace`, `steam radiator`, `ac capacitor`). "
      "Seven topics were added by this helper because the autocomplete kept pointing at them: keep-cool, keep-warm, "
      "evap-cooler, electric-heat, geothermal, home-warranty, hvac-general. Source label: `brief topic list` or "
      "`helper-added seed`.")
    a("2. **Known winning titles.** Short phrases were lifted from the winners quoted in "
      "`findings/2026-10-22-hvac-and-electrical.md` section 1 and "
      "`recovered/2026-10-22-roger-sub-brands/research/lane2-trades.md` (for example \"thermostat habits\", "
      "\"before you turn on your heat\", \"hvac companies hate\"). Source label: `known title: <title (channel, views as quoted there)>`. "
      "Two phrases (\"radiator trick\", \"cuts the oil bill\") come from a *proposed* hand-off title in lane2-trades, "
      "not a published video, and say so.")
    a("3. **YouTube autocomplete.** `https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=en&gl=us&q=<query>`, "
      "0.3 s between calls, pulled 2026-10-23. Queries: every seed; the first seed of each topic with the audience "
      "framings (\"why is my X\", \"how to X\", \"stop X\", \"never X\", \"X mistakes\", \"don't X\", \"before you X\", "
      "\"the only X\", \"X vs\", \"X secret\", \"X hack\", \"cheap X\", \"X save money\", \"lower X bill\", \"X old house\", "
      "\"X seniors\", \"X winter/summer/fall/spring\", \"X myth\", \"X scam\", \"X cost\" and a few more; the full set "
      "for 23 owned-equipment topics, a 16-framing set for the rest); the same framings on 7 extra nouns (heater, "
      "heat, heating, air conditioning, radiators, electric bill, heating bill); every known-title phrase; every Silver Cymbal phrase (below); and an "
      "a-to-z expansion (`seed a` ... `seed z`) of 10 main seeds: "
      + ", ".join(f"`{s}`" for s in ALPHA_SEEDS) + ".")
    a("4. **Filter.** Autocomplete returns a lot that is not home HVAC (video games, car AC, Indian-market AC, "
      "Windows software, music, Hindi/Bangla/Spanish phrases, water heaters, which belong to plumbing). A suggestion "
      "is kept only if it has a strong HVAC word (furnace, thermostat, heat pump, insulation, electric bill...) or a "
      "weak one (ac, heat, filter, vent, window, fan...) plus a home context word, and none of the exclusion words. "
      "The rules are in `autocomplete.py` (`STRONG`, `WEAK`, `CONTEXT`, `EXCLUDE`). "
      f"{len(set(dropped))} distinct suggestions were dropped. The filter is a heuristic: some off-topic strings "
      "remain in EXTENDED (mostly harmless; the sweep will show it) and a few on-topic ones may have been dropped.")
    a("5. **Dedupe and label.** Lower-cased, spaces and apostrophes normalised, exact duplicates merged (all sources "
      "kept in the CSV, joined by `;`). A suggestion's autocomplete source is the first query in plan order that "
      "returned it. Topic and framing come from ordered word rules (`TOPIC_RULES`, `FRAMING_RULES`): the first rule "
      "that matches wins, so a keyword carries one topic and one framing (for example \"why is my ac freezing up\" is "
      "ac-freezing / problem symptom).")
    a("6. **Priority.** The PRIORITY set was picked by hand from the labelled list, to cover every topic and mix "
      "plain topics with each framing, leaning towards what the 2026-10-22 findings say works for this audience "
      "(money, distrust of the trade, mistakes, before-you, brand verdicts, old-house heat, outage heat). "
      "It is the helper's judgement, not a measured ranking.")
    a("")
    a("**What autocomplete does and doesn't tell us.** It shows phrases people type on YouTube, in the endpoint's "
      "own order. It gives no search volume, and none is claimed here. A phrase appearing does not mean videos on it "
      "do well; the sweep measures that.")
    a("")
    a(f"**Silver Cymbal titles:** `studies/hvac/seeds/silver-cymbal.md` (the round 1 seed helper's file, read on "
      f"2026-10-23) was read once it appeared. {len(SILVER_CYMBAL_PHRASES)} short phrases were cut by hand from "
      f"{len(sc_titles)} of its titles (the 22 seeds, plus in-scope borderline and under-5-minute HVAC titles it lists, "
      "marked as such), added as keywords (source `Silver Cymbal title: \"<title>\" (video ID, views as listed there)`) "
      "and also run through autocomplete. Its views are that helper's figures, not re-checked here. If that file "
      "changes, update `SILVER_CYMBAL_PHRASES` in the script and re-run `python3 autocomplete.py` then "
      "`python3 autocomplete.py build`.")
    a("")
    a("## Counts")
    a("")
    hits = Counter(v["kind"] for q, v in plan_q.items()
                   if any(is_hvac(norm(s)) for s in (res.get(q, {}).get("suggestions") or [])))
    a(f"- Autocomplete queries sent: **{nq}** ({kinds['seed']} seeds, {kinds['framing']} framed, "
      f"{kinds['known-title']} known-title phrases, {kinds['silver-cymbal']} Silver Cymbal phrases, "
      f"{kinds['alphabet']} a-z). {nq_nonempty} returned at least one suggestion; {nq - nq_nonempty} returned none; "
      f"no request failed.")
    a("- Queries that returned at least one kept (home HVAC) suggestion: " + ", ".join(
        f"{k} {hits[k]} of {kinds[k]}" for k in ["seed", "framing", "known-title", "silver-cymbal", "alphabet"]) + ".")
    a(f"- Suggestions returned: {nsugg} ({nuniq} distinct); {len(set(dropped))} distinct dropped as not home HVAC.")
    a(f"- **Keywords in the list: {len(allr)}** — PRIORITY **{len(pri)}**, EXTENDED **{len(ext)}**.")
    a(f"- By first source: autocomplete {src_kind['autocomplete']}, brief/helper seeds {src_kind['seed']}, "
      f"known-title phrases {src_kind['known-title']}, Silver Cymbal titles {src_kind.get('silver-cymbal', 0)}.")
    a("")
    a("| Topic | Code | All keywords | PRIORITY |")
    a("|---|---|---:|---:|")
    for t in TOPIC_NAMES:
        a(f"| {TOPIC_NAMES[t]} | `{t}` | {by_topic[t]} | {by_topic_p[t]} |")
    a(f"| **Total** | | **{len(allr)}** | **{len(pri)}** |")
    a("")
    a("| Framing | All keywords | PRIORITY |")
    a("|---|---:|---:|")
    for f in FRAMINGS_ORDER:
        a(f"| {f} | {by_fr[f]} | {by_fr_p[f]} |")
    a("")
    a(f"**Reading (counted from this list, not a volume):** framed phrasings are rare in autocomplete. Of "
      f"{len(allr)} keywords, {by_fr['mistakes']} read as mistakes, {by_fr['before you']} as before-you, "
      f"{by_fr['they don\'t want you to know']} as they-don't-want-you-to-know and {by_fr['myth']} as myth, against "
      f"{by_fr['problem symptom']} problem-symptom and {by_fr['how-to']} how-to. Several known winning phrases "
      "return nothing on topic (\"before you turn on your heat\" gives only \"before you turn off the light\"; "
      "\"thermostat habits\" gives nothing about HVAC). People type the problem; the framing lives in the titles. "
      "So the PRIORITY set adds the known-title phrases by hand, and the sweep should count framings from the "
      "video titles it returns.")
    a("")
    a("Framing notes: \"they don't want you to know\" also holds scam / upsell / secret phrasings. \"the only X\" also "
      "holds best / worst / brands-to-avoid. \"story\" and \"test\" (from deliverable 8) don't show up in autocomplete "
      "phrasing; they will have to be counted from the sweep's video titles.")
    a("")
    a("## PRIORITY keywords (full 4-sort sweep)")
    a("")
    a("| # | Keyword | Topic | Framing | Source |")
    a("|---:|---|---|---|---|")
    keyf = lambda r: (list(TOPIC_NAMES).index(r["topic"]), FRAMINGS_ORDER.index(r["framing"]), r["keyword"])
    for i, r in enumerate(sorted(pri, key=keyf), 1):
        a(f"| {i} | {md_escape(r['keyword'])} | `{r['topic']}` | {r['framing']} | {md_escape("; ".join(r['sources']))} |")
    a("")
    a("## EXTENDED keywords (relevance search only), by topic")
    a("")
    a("One line each: keyword · framing · first source. Full source lists are in the CSV.")
    for t in TOPIC_NAMES:
        items = sorted([r for r in ext if r["topic"] == t], key=keyf)
        if not items:
            continue
        a("")
        a(f"### {TOPIC_NAMES[t]} (`{t}`, {len(items)})")
        a("")
        for r in items:
            a(f"- {r['keyword']} · {r['framing']} · {r['sources'][0]}")
    a("")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


PRIORITY = {  # hand-picked 2026-10-23 (see the md, method step 6); every one must exist in the built list
    # ac-central
    "air conditioner", "ac not cooling", "why is my ac blowing hot air", "ac mistakes", "save money on ac",
    "secret ac trick", "central air conditioning not cooling", "unclog ac drain line", "adding air conditioning to old house",
    # ac-window
    "window air conditioner", "window ac not cooling", "window ac vs portable ac", "best portable air conditioner",
    # mini-split
    "mini split", "mini split vs central air", "mini split mistakes", "mini split cost installed",
    # heat-pump
    "heat pump", "heat pump vs furnace", "do heat pumps save money", "the truth about heat pumps",
    "why is my heat pump blowing cold air", "heat pumps leaving people cold",
    # furnace
    "furnace", "why is my furnace blowing cold air", "save money on heating",
    # oil-furnace
    "oil furnace", "oil furnace won't ignite", "oil furnace maintenance", "oil furnace vs gas furnace", "heating oil vs gas",
    # boiler-steam
    "boiler", "steam radiator", "steam heat", "bleeding radiators old house", "steam radiator not getting hot",
    "boiler vs furnace", "old house boiler", "boiler no heat",
    # electric-heat
    "baseboard heater",
    # thermostat
    "thermostat habits", "what temperature should you set your thermostat", "thermostat save money",
    "turning your heat down", "smart thermostat save money", "nest thermostat vs ecobee",
    # filters
    "air filter", "ac filter destroying", "furnace filter mistakes", "how often should you change your air filter",
    "furnace filters cheap vs expensive", "do air filters really work",
    # ducts-vents
    "duct cleaning", "duct cleaning scams", "closing vents", "is ac duct cleaning worth it",
    # parts
    "ac capacitor", "contactor", "furnace flame sensor", "furnace igniter",
    # coil-cleaning
    "how to clean ac unit", "cleaning ac unit with pressure washer", "central air conditioner condenser cleaning",
    # maintenance
    "hvac maintenance", "before you turn on your heat", "before you shut your ac down", "before you turn on your ac",
    "do this once a month ac", "do this before winter furnace",
    # energy-bill
    "electric bill", "heating bill", "why is my electric bill so high", "lower your electric bill",
    "energy bill mistakes", "power company doesn't want you to", "how to save money on electric bill in winter",
    "why is your heat bill so high",
    # insulation
    "attic insulation", "rim joist insulation", "spray foam", "insulation mistakes", "spray foam alternative",
    # drafts
    "weatherstripping", "drafty house", "draft stopper",
    # windows
    "window insulation", "window film", "thermal curtains",
    # humidity
    "dehumidifier", "humidity in house", "dehumidifier mistakes",
    # indoor-air
    "indoor air quality", "air purifier", "carbon monoxide furnace",
    # outage-heat
    "power outage heat", "heat without power", "stay warm without power",
    "keep your family warm during a power outage", "furnace not working after power outage",
    # brands
    "best hvac brands", "best ac brands", "best furnace brands", "best heat pump brands", "hvac brands to avoid",
    "only hvac brands worth buying",
    # refrigerant
    "freon", "ac recharge", "ac losing freon",
    # ac-freezing
    "ac freezing up", "why is my ac freezing up", "frozen evaporator coil",
    # short-cycling
    "short cycling", "furnace short cycling", "ac short cycling",
    # smells
    "furnace smell", "burning smell furnace",
    # noises
    "furnace noise", "ac making noise", "banging radiator",
    # scams-upsells
    "hvac scam", "hvac scam caught on camera", "hvac upsell", "hvac companies hate",
    "hvac companies don't want you to know", "beating the hvac industry",
    # replacement-cost
    "hvac replacement cost", "new ac cost", "new furnace cost", 
    # wood-stove
    "wood stove", "pellet stove", "wood stove mistakes",
    # space-heater
    "space heater", "space heater vs central heat", "space heater save money",
    # ceiling-fan
    "ceiling fan direction", "ceiling fan winter",
    # attic-fan
    "attic fan", "whole house fan", "cool your attic",
    # keep-cool
    "keep house cool", "cool house without ac", "home designs that stayed cool",
    # keep-warm
    "keep house warm", "heat house cheap",
    # evap-cooler, geothermal, home-warranty
    "swamp cooler", "geothermal", "home warranty hvac",
    # hvac-general
    "hvac tips", "hvac secrets", "hvac mistakes",
}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        build()
    else:
        main()
