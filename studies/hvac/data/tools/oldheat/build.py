import json, re, statistics, collections, sys
S = "/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/"
MATCHED_HEAT = ["how to bleed radiators","banging radiator","steam radiator not getting hot","boiler pressure low","boiler no heat",
                "hot water baseboard heat","oil furnace maintenance","heating oil vs gas","old house heating cost","boiler vs furnace"]

def views(t):
    if not t: return None
    if t.startswith("No views"): return 0
    m = re.match(r"([\d,]+) views?", t)
    return int(m.group(1).replace(",", "")) if m else None

def secs(t):
    if not t: return None
    p = [int(x) for x in t.split(":")]
    s = 0
    for x in p: s = s * 60 + x
    return s

def age_months(t):
    """approx months since upload from age text; years -> 12*y (lower bound)."""
    if not t: return None
    t = t.replace("Streamed ", "")
    m = re.match(r"(\d+)\s*(second|minute|hour|day|week|month|year|s|min|h|d|w|mo|y)\w*\s+ago", t)
    if not m: return None
    n, u = int(m.group(1)), m.group(2)
    if u in ("second","minute","hour","s","min","h"): return 0
    if u in ("day","d"): return n / 30.4
    if u in ("week","w"): return n * 7 / 30.4
    if u in ("month","mo"): return n
    if u in ("year","y"): return 12 * n
def recent(t):
    a = age_months(t); return a is not None and a < 12

NONLATIN = re.compile(r"[^\x00-ɏ -⯿️\U0001F000-\U0001FAFF]")
FOREIGN_CH = re.compile(r"[äöüßñãõçåøæłąęśźżčřšžőű]", re.I)
FOREIGN_W = re.compile(r"\b(de|la|el|los|las|como|cómo|para|und|der|die|das|mit|für|nicht|le|les|du|des|och|het|een|con|sin|y|o|em|não|você|ar|aire|caldera|calefacci\w*|radiador\w*|heizung\w*|heizk\w*|chaudi\w*|selbst|gemacht|abgleich|kostet|bringt|ketel|reparatie|loopt|volledig|warmtepomp|wärmepumpe|entlüften|spart|kosten|sparen|niet|voor|ook|deze|zo|je|jij|wat|werkt|hoe|haar|zijn|nog|naar|ich|nicht|auch|sich|jetzt|immer|richtig|radiateur\w*|verwarming|kocio\w*|grzejnik\w*|caldaia|termosifon\w*|kombi|petek|klima\w*|acondicionado|condicionado|aquecedor|estufa|ce|cum|pe|si|il|di|che|una|un|ein|eine|wie|ist|så|og|på|är|jak|na|nie|ve|bir|mo|ng|sa)\b", re.I)
def english(title):
    if NONLATIN.search(title): return False
    if FOREIGN_CH.search(title): return False
    if len(FOREIGN_W.findall(title)) >= 1: return False
    return True

CAR = re.compile(r"\b(car|cars|truck|vehicle|auto|automotive|engine|coolant|jeep|honda|toyota|ford|chevy|chevrolet|bmw|nissan|hyundai|kia|dodge|gmc|mercedes|audi|vw|subaru|mazda|tesla|rv|camper|motorcycle|pc|gpu|cpu|aio|water.?cool\w*|antifreeze|thermostat housing|lawn ?mower|tractor|boat|scooter|motorbike|bike|pcx|aerox|integra|civic|fiat|k-?swap|radiator (hose|cap|fluid|flush|fan))\b", re.I)
HEAT = re.compile(r"radiator|boiler|steam (heat|radiator|system|pipe|vent|trap|boiler|heating)|one.?pipe|two.?pipe steam|\bsteam\b.*\b(heat|radiator|vent)|hydronic|baseboard|circulator|zone valve|expansion tank|\boil (furnace|burner|boiler|heat\w*|tank|fired|nozzle|filter|to)\b|heating oil|home heating oil|oil.?fired|oil heat|gravity furnace|octopus furnace|old (house|home)\b.*\b(heat|heating|furnace)|(heat|heating)\b.*\bold (house|home)|hot water heat(ing)?\b(?! (heater|tank))|radiant (floor )?heat|\bburner\b|aquastat|pressure relief valve.*boiler|oil (vs|or) (gas|propane|heat pump)", re.I)
HEAT_EX = re.compile(r"white noise|asmr|sleep|relax|\d+ hours?\b|boiler ?room|boilerroom|boiler plate|boilerplate|tankless water heater|water heater|steam ?deck|steam cleaner|steam engine|steam locomotive|pressure washer|olive oil|essential oil|oil change|motor oil|cooking oil|frying|\bburner phone|burner account|stove ?top|gas burner|bunsen", re.I)
AC = re.compile(r"\b(ac|a/c|a\.c\.?|hvac)\b|air ?condition\w*|mini.?split|ductless|condenser|evaporator|capacitor|central air|thermostat|heat pump|compressor|air filter|furnace filter|refrigerant|freon", re.I)
AC_EX2 = re.compile(r"resistor|diode|electronic|\bsmd\b|rc circuit|physics|electroboom|hydraulic|thermoelectric|\bclutch\b", re.I)
AC_EX = re.compile(r"\b(fridge|refrigerator|freezer|ice maker|chest freezer|car amp|guitar|amplifier|audio)\b", re.I)

CAR_CH = re.compile(r"chrisfix|auto hacks|obd insights|youngstatic|greyfox|ilham imanulloh|meccanica|eric the car guy|scotty kilmer|engineering explained|humble mechanic|south main auto|1a auto|ericthecarguy|carsntoys|auto v fix", re.I)
HEAT_EX2 = re.compile(r"waste oil|used oil|vegetable oil|diesel|crude|refiner|\blpg\b|petrol|power plant|thermal power|turbine|fire.?tube|water.?tube|\bid fan|\bfd fan|boiler tube|boiler drum|blowdown|industrial|marine|narrowboat|railway|railroad|trains?\b|locomotive|auxiliary boiler|chiller|commercial|camping|oil stove|\bgarage|workshop|\bshop\b|\bbarn\b|\bshed\b|\bvan\b|sprinter|crafter|radiant floor|in.?floor|\bslab\b|concrete|wood ?stove|wood boiler|outdoor boiler|wood oil|pellet|coffee|espresso|breville|tea urn|watch winder|world of tanks|gaming|heat trade|miami heat|pointer sisters|bourbon|scrap|junk|recycling|shroud|billet|\bcnc\b|swing arm|ferrari|cuda|\bktm\b|duke 250|\bsym\b|adxtg|\bmoto|xmax|vario|hitachi|oil cooler|after ?cooler|yamaha|loadstar|jb weld|petromax|electric baseboard|240 volts|\bmysa\b|dimplex|bag closing|steam review|nuclear|steam pipeline|melted salt|off.?grid|alaska|thermal expansion tank|thermostat housing|last caretaker|hot water heat pump|solar|burner stove|box turtle|keara riley", re.I)
BAD_CH = re.compile(r"^(RealPars|LifeAda|Think and Achieve|Creative Surface|unique Smart Technical|Technical Engineering School|WARE Boilers|DIVI Group.*|MonitorMax|Power Plant Guide|Power Plant Discussion|HIMT|PT INDIRA MITRA BOILER|Сша Сша|FactZaara|Steam Management, Inc\.|Building Systems Academy|Lanair Products|Power Eagle USA|Documentary Central|Rail Secrets Unlocked|Vale of Rheidol Railway|Maniaques|Heat Latest|koollatter|GerrysDiy|Creative Phil|Creative inventions LMTN|Turbo Schneider|Unknowns Lab 101)$", re.I)
OHO = re.compile(r"\|?\s*(ask )?this old house\b", re.I)
EXP = re.compile(r"expansion tank", re.I)
HEATCTX = re.compile(r"boiler|heating|hydronic|radiator|baseboard", re.I)
BASEB = re.compile(r"baseboard", re.I)
BASECTX = re.compile(r"hot ?water|hydronic|boiler|bleed|\bair\b|cover|enclosure|base-?ray|slant|zone|pipe|radiator|noisy|quiet|move|heat\b|heating", re.I)
def topical(side, title, channel=""):
    if CAR.search(title) or CAR_CH.search(channel or ""): return False
    if side == "heat":
        t = OHO.sub("", title)
        if not HEAT.search(t) or HEAT_EX.search(t) or HEAT_EX2.search(t) or BAD_CH.search((channel or "").strip()): return False
        if EXP.search(t) and not HEATCTX.search(t): return False
        if BASEB.search(t) and not re.search(r"radiator|boiler|steam|oil", t, re.I) and not BASECTX.search(t): return False
        return True
    if not AC.search(title) or AC_EX.search(title) or AC_EX2.search(title): return False
    if re.search(r"capacitor", title, re.I) and not re.search(r"\b(ac|a/c|hvac)\b|air|furnace|compressor|condenser|fan", title, re.I): return False
    return True

def med(x): return statistics.median(x) if x else None

rows = [json.loads(l) for l in open(S + "search.jsonl")]
OE = {}
for l in open(S + "oembed.jsonl"):
    j = json.loads(l)
    if j.get("orig_title"): OE[j["id"]] = j["orig_title"]
# collab rows ("X and Y" / "X and 3 more") carry no channelId: map to the first-named channel when it is known
NAME2ID = {}
for r in rows:
    for v in r["rows"]:
        if v.get("channelId") and v.get("channel"): NAME2ID.setdefault(v["channel"], v["channelId"])
for r in rows:
    for v in r["rows"]:
        if not v.get("channelId") and v.get("channel"):
            m = re.match(r"(.+?) and (\d+ more|.+)$", v["channel"])
            if m and m.group(1) in NAME2ID:
                v["collab"] = v["channel"]; v["channel"] = m.group(1); v["channelId"] = NAME2ID[m.group(1)]
            else:
                v["collab"] = v["channel"]; v["channelId"] = "collab:" + v["channel"]
# per side: dict id -> video (max views seen)
def collect(sel):
    vids = {}; raw = 0; seen_any = set(); lf = set(); en = set()
    for r in sel:
        for v in r["rows"]:
            raw += 1; seen_any.add(v["id"])
            s = secs(v["length"]); vw = views(v["views"])
            if s is None or s < 300: continue
            lf.add(v["id"])
            ot = OE.get(v["id"], v["title"])
            if not english(ot) or not english(v["channel"] or "") or not english(v["title"]): continue
            en.add(v["id"])
            if not topical(r["side"], v["title"], v.get("channel")): continue
            d = vids.setdefault(v["id"], dict(v, orig_title=OE.get(v["id"]), translated=(v["id"] in OE and OE[v["id"]] != v["title"]), views_n=vw, secs=s, keywords=set(), sorts=set()))
            d["keywords"].add(r["keyword"]); d["sorts"].add(r["sort"])
            if vw is not None and (d["views_n"] is None or vw > d["views_n"]): d["views_n"] = vw
    return vids, dict(raw_rows=raw, distinct_any=len(seen_any), distinct_longform=len(lf), distinct_lf_english=len(en), distinct_topical=len(vids))

def summary(vids):
    vs = [v["views_n"] for v in vids.values() if v["views_n"] is not None]
    rec = [v for v in vids.values() if recent(v["age"])]
    rvs = [v["views_n"] for v in rec if v["views_n"] is not None]
    chans = {v["channelId"] for v in vids.values()}
    q = lambda xs, p: sorted(xs)[int(p * (len(xs) - 1))] if xs else None
    return dict(videos=len(vids), channels=len(chans), median=med(vs), p25=q(vs, .25), p75=q(vs, .75), p90=q(vs, .9), max=max(vs) if vs else None,
                total=sum(vs), n_100k=sum(x >= 1e5 for x in vs), n_1m=sum(x >= 1e6 for x in vs),
                recent_n=len(rec), recent_median=med(rvs), recent_100k=sum(x >= 1e5 for x in rvs),
                recent_channels=len({v["channelId"] for v in rec}))

def jsonable(vids):
    out = []
    for v in sorted(vids.values(), key=lambda v: -(v["views_n"] or 0)):
        d = dict(v); d["keywords"] = sorted(d["keywords"]); d["sorts"] = sorted(d["sorts"]); d["recent_12mo"] = recent(v["age"]); out.append(d)
    return out

res = {}
for side in ("heat", "ac"):
    sel = [r for r in rows if r["side"] == side]
    vids, funnel = collect(sel)
    res[side] = dict(funnel=funnel, summary=summary(vids), vids=vids, keywords=sorted({r["keyword"] for r in sel}))
    # per keyword
    pk = {}
    for kw in res[side]["keywords"]:
        kv, f = collect([r for r in sel if r["keyword"] == kw])
        pk[kw] = dict(f, **summary(kv))
    res[side]["per_kw"] = pk
mv, mf = collect([r for r in rows if r["side"] == "heat" and r["keyword"] in MATCHED_HEAT])
res["heat_matched"] = dict(funnel=mf, summary=summary(mv), vids=mv)

if __name__ == "__main__":
    for side in ("heat", "heat_matched", "ac"):
        print(side, res[side]["funnel"], res[side]["summary"])
    for side in ("heat", "ac"):
        for k, v in res[side]["per_kw"].items():
            print(side, k, {x: v[x] for x in ("raw_rows","distinct_any","distinct_topical","channels","median","max","n_100k","recent_n","recent_median")})
