#!/usr/bin/env python3
"""Merge the up-next pulls (upnext.py) and the NexLev results into one raw file, and print the tables
for seeds/leads-channels.md.  Usage: python3 -I upnext_build.py <scratch_dir> <out.json>
<scratch_dir> holds hop1.json, hop2.json, nlsim/<seed>.txt|.inline.json, nl_simchannels.txt, nlsugg/<query>.txt.
Topic and HVAC tags are keyword readings of the titles (regexes below), not measured facts."""
import sys, os, json, re, collections, datetime

SCR, OUT = sys.argv[1], sys.argv[2]
SC = "UC67dKTEwpAhKv2oYDATwR8g"
SEEDS22 = ["_b6p0fkWhCY", "qAxJb0J1HH0", "Wejop_Rjpv0", "o8KQu_MlpoY", "DSNUyxZtrmo", "nsRHhU6q5RY", "zvFKD95z7IM",
           "5GbXgEYw5TE", "leEsPGaaru8", "BP1iDvKpNZA", "NsPBamTmOPM", "uObGbs4sGQY", "yCZqfnlBYW8", "ED3bfesbE_Y",
           "GdTOl1WcHV0", "flpbqJu2sT8", "kEWzIfnIhUw", "Xd-Og809TUo", "yZavrHJsBAw", "S8XO4wFhrPU", "OGVXmIZtEG8",
           "cC-J0ZCUH28"]
BORDER5 = ["sHL4lBAhklA", "9d9TL02idO4", "pPMm0reEBPM", "yNBXE3BszEM", "EjLJm0g4whg"]
HOP2 = ["_ZgVjFpBnQA", "k7PSzi7NSyc", "D_2T5H7CFmA", "BSTkKiJPeaQ", "AQ4EYHNCDzg", "5dCCntGj1wM", "dOZ-8__G4uU",
        "GfMNLWzaUHU", "k1HGyewDZ_k", "2mKwCmaR5Qg"]

# HVAC / energy / insulation title reading (core HVAC + bill/insulation + home heating appliances)
HVAC = re.compile(r"\b(a/?c\b|a/c|air ?condition\w*|hvac|furnace|heat ?pumps?|mini[- ]?splits?|ductless|condenser|evaporator|"
                  r"ac coils?|capacitor|thermostat|boilers?|radiators?|circulator|btu|ducts?|ductwork|vents?\b|"
                  r"(air|furnace|ac) filters?|freon|refrigerant|compressor|blower|air handler|condensate|drain line|"
                  r"swamp cooler|evaporative cooler|portable (ac|air)|window (ac|unit)|cool (your|the|a) (house|home|room)|"
                  r"without ac|heat(ing)? (your|the|my|a) (house|home|shop|garage|room)|central heat\w*|no heat|"
                  r"heating (system|bill|oil)|oil heat|heating|insulat\w*|weather ?strip\w*|draft\w*|spray foam|"
                  r"energy bill|electric bill|utility bill|dehumidif\w*|humidity|indoor air|space heaters?|"
                  r"diesel heater|wood ?stove|pellet stove|rocket (stove|heater|mass)|geothermal|heat(s|ing|er|ers)?|warm(er|th)?|"
                  r"cool(ing)?|colder|coldest|mr ?cool|firewood|stoves?|fireplace|chimney|ventilation|exhaust fan|"
                  r"air purifier|attic|crawl ?space|oil burners?|burner nozzle|cad cell|refrigeration|air ?con|split system|"
                  r"hydronic\w*|expansion (vessel|tank)|radiant floor|fuel oil|oilheat|oil to gas|acs|cooler|grundfos|"
                  r"taco|coil cleaners?|dust free)\b", re.I)
ALT_HEAT = re.compile(r"\b(diesel heater|wood ?stove|pellet stove|rocket (stove|heater|mass)|sawdust|firewood|stove|"
                      r"unlimited heat|sand heater|heater)\b", re.I)
WATER_HEATER = re.compile(r"(hot )?water heat\w*|tankless", re.I)


def is_hv(title):
    """HVAC reading of a title; water heaters are plumbing, so they are removed before matching"""
    return bool(HVAC.search(WATER_HEATER.sub(" ", title or "")))


TOPICS = [  # first match wins; applied only to items NOT tagged HVAC
    ("non-English", r"[\u0400-\u04FF\u0600-\u06FF\u0900-\u097F\u3040-\u30FF\u4E00-\u9FFF]|\b(comment|agir|gestion|meccset|nyerj\u00fck|mo\u017ee\u0161|samo)\b"),
    ("news / politics", r"\b(trump|putin|russia\w*|ukrain\w*|zelensk\w*|canada|carney|kushner|iran|hormuz|hegseth|vance|"
                        r"kennedy|biden|gaza|israel|nato|congress|senate|election|daily show|tariff|migrants?|weidel|afd|"
                        r"macron|ursula|kiev|kyiv|war\b|jets? crash|breaking)\b"),
    ("generators / power stations / solar", r"\b(generator|power station|ecoflow|jackery|anker|solix|bluetti|solar|"
                                            r"battery backup|whole (house|home) (backup|power)|kwh|7200w|power outage)\b"),
    ("electrical", r"\b(wires?|wiring|neutral|outlets?|breakers?|electrician|electrical|volt\w*|hz\b|amps?\b|panel|"
                   r"gfci|wago|extension cord|lightning)\b"),
    ("plumbing / water heater", r"\b(plumb\w*|pipes?|water heater|toilet|faucet|leak\w*|drain|sewer|shower|sink|"
                                r"valve|pex|sharkbite|hose clamp|hot water|recirculat\w*|teflon tape|coupling)\b"),
    ("cars / trucks / vehicles", r"\b(cars?|truck\w*|engine|tesla|vehicle\w*|headlights?|roadster|drivers?|tires?|"
                                 r"jeep|ford|toyota|chevy|honda|street legal|trailer\w*|power steering|rv\b|camper|van\b|byd|carmakers|"
                                 r"dashboard|fuel stabilizer|gasoline|diesel|7\.3)\b"),
    ("lawn / garden / outdoor", r"\b(lawn|garden\w*|grass|mow\w*|sprinkler|weeds?|trees?|stump|mosquito|yard|"
                                r"homestead\w*|chickens?|forest)\b"),
    ("house building / renovation / cabins", r"\b(build\w* (a|my|the) (house|home|cabin)|dream home|cabin|renovat\w*|"
                                             r"remodel\w*|tub\b|tile|roof\w*|house in the forest|stone ruin|"
                                             r"home features|tiny house|bunker)\b"),
    ("tools / DIY hacks / repair tricks", r"\b(tools?|drill|hack\w*|trick\w*|diy|welding|glue|caulk\w*|repair|fix\w*|"
                                          r"handyman|screw\w*|rust)\b"),
    ("tech / gadgets / science", r"\b(iphone|gadgets?|amazon|tech|netflix|engineering|science|alien|enigma|ai\b|"
                                 r"computer|phone|smart)\b"),
    ("military / history", r"\b(wwii|b-17|ww2|military|navy|soldier|nazi|history|gunner)\b"),
    ("money / deals / scams", r"\b(costco|deals?|scam\w*|money|\$\d|cheap\w*|save)\b"),
]
TOPICS = [(n, re.compile(p, re.I)) for n, p in TOPICS]


def topic(title):
    if is_hv(title):
        return "HVAC / energy / insulation"
    for n, p in TOPICS:
        if p.search(title or ""):
            return n
    return "other / unclassified"


def load_nlsim(seed):
    for ext in (".txt", ".inline.json"):
        p = os.path.join(SCR, "nlsim", seed + ext)
        if os.path.exists(p):
            break
    else:
        return None
    if ext == ".txt":
        j = json.loads(json.load(open(p))[1]["text"])
        vids = [{"videoId": v.get("videoId"), "title": v.get("title"), "channelTitle": v.get("channelTitle"),
                 "channelId": v.get("channelId"), "viewCount": v.get("viewCount"),
                 "publishedTimeText": v.get("publishedTimeText"), "lengthText": v.get("lengthText"),
                 "similarity_score": v.get("similarity_score")} for v in j["videos"]]
        return {"source": "NexLev get_similar_videos videoId=%s (tool result saved to file, parsed by script)" % seed,
                "totalResults": j.get("totalResults"), "videos": vids}
    j = json.load(open(p))
    vids = [dict(zip(["videoId", "title", "channelTitle", "channelId", "viewCount", "publishedTimeText", "lengthText",
                      "similarity_score"], r)) for r in j["videos"]]
    return {"source": "NexLev get_similar_videos videoId=%s; %s" % (seed, j["note"]), "totalResults": j["totalResults"],
            "videos": vids}


def secs(t):
    if not t or not re.match(r"^\d+(:\d{2}){1,2}$", t):
        return None
    s = 0
    for p in t.split(":"):
        s = s * 60 + int(p)
    return s


hop1 = json.load(open(os.path.join(SCR, "hop1.json")))
hop2 = json.load(open(os.path.join(SCR, "hop2.json")))
nlsim = {s: load_nlsim(s) for s in SEEDS22}
scj = json.loads(json.load(open(os.path.join(SCR, "nl_simchannels.txt")))[-1]["text"])
simch = []
for c in scj["channels"]:
    a = c.get("about", {})
    simch.append({"channelId": a.get("channelId"), "name": a.get("channelName"), "subscriberCount": a.get("subscriberCount"),
                  "viewCount": a.get("viewCount"), "videoCount": a.get("videoCount"), "joinedDate": a.get("joinedDate"),
                  "country": a.get("country"), "avgVideoLengthSeconds": a.get("avgVideoLengthSeconds"),
                  "lastVideoUploadDate": a.get("lastVideoUploadDate"), "updatedAt": a.get("updatedAt"),
                  "similarityScore": c.get("similarityScore"), "tags": c.get("tags")})
sugg = {}
for f in sorted(os.listdir(os.path.join(SCR, "nlsugg"))):
    j = json.loads(json.load(open(os.path.join(SCR, "nlsugg", f)))[-1]["text"])
    sugg[j["filters"]["query"]] = {"filters": j["filters"], "meta": j["meta"],
                                   "videos": [{k: v.get(k) for k in ("videoId", "title", "ytChannelId", "views", "duration",
                                                                     "publishDate", "channelSubCount", "outlierScore",
                                                                     "createdAt")} for v in j["videos"]]}

# ---------- counts
ch = collections.defaultdict(lambda: {"name": None, "handle": None, "h1": set(), "h1_core": set(), "h1_items": 0, "h2": set(),
                                      "h2_items": 0, "nl": set(), "hv_items": 0, "alt_items": 0, "all_items": 0, "vids": {}})
vid = collections.defaultdict(lambda: {"h1": set(), "h2": set(), "nl": set()})


def add(it, src, hop):
    if it.get("type") != "video" or not it.get("id"):
        return
    c = ch[it["channel_id"]]
    c["name"] = c["name"] or it["channel"]; c["handle"] = c["handle"] or it["handle"]
    c[hop].add(src); c[hop + "_items"] += 1; c["all_items"] += 1
    if hop == "h1" and src in SEEDS22:
        c["h1_core"].add(src)
    if is_hv(it["title"]):
        c["hv_items"] += 1
        if ALT_HEAT.search(it["title"] or ""):
            c["alt_items"] += 1
    c["vids"].setdefault(it["id"], it)
    v = vid[it["id"]]
    for k in ("title", "channel", "channel_id", "handle", "views_text", "views_label", "age_text", "length_text", "length_s"):
        v.setdefault(k, it.get(k))
    v[hop].add(src)


for s, r in hop1.items():
    for it in r["items"]:
        add(it, s, "h1")
for s, r in hop2.items():
    for it in r["items"]:
        add(it, s, "h2")
for s, r in nlsim.items():
    for v in (r or {}).get("videos", []):
        if not v.get("channelId"):
            continue
        c = ch[v["channelId"]]; c["name"] = c["name"] or v["channelTitle"]; c["nl"].add(s)
        vv = vid[v["videoId"]]
        vv.setdefault("title", v["title"]); vv.setdefault("channel", v["channelTitle"]); vv.setdefault("channel_id", v["channelId"])
        vv.setdefault("views_text", None); vv.setdefault("length_text", v["lengthText"]); vv.setdefault("length_s", secs(v["lengthText"]))
        vv["nl_views"] = v["viewCount"]; vv["nl"].add(s)

simscore = {c["channelId"]: c for c in simch}

# ---------- topic counts (hop 1 and hop 2, every up-next item)
tc = {"h1": collections.Counter(), "h2": collections.Counter()}
tcv = {"h1": collections.defaultdict(set), "h2": collections.defaultdict(set)}
tex = collections.defaultdict(list)
for hop, data in (("h1", hop1), ("h2", hop2)):
    for s, r in data.items():
        for it in r["items"]:
            if it.get("type") != "video":
                continue
            t = topic(it["title"])
            tc[hop][t] += 1; tcv[hop][t].add(it["id"])
            if it["id"] not in [e[0] for e in tex[t]] and len(tex[t]) < 400:
                tex[t].append((it["id"], it["title"], it["channel"], it["views_text"], len(vid[it["id"]]["h1"]) + len(vid[it["id"]]["h2"])))

about_mine = json.load(open(os.path.join(SCR, "about_mine.json"))) if os.path.exists(os.path.join(SCR, "about_mine.json")) else {}
about_other_p = os.path.join(os.path.dirname(OUT), "channel-finds-pages-2026-10-23", "about.json")
about_other = json.load(open(about_other_p)) if os.path.exists(about_other_p) else {}


def subs_of(cid):
    a = about_mine.get(cid) or {}
    if a.get("subscriberCountText"):
        return "%s (About, this pull)" % a["subscriberCountText"].replace(" subscribers", "")
    a = about_other.get(cid) or {}
    if a.get("subscriberCountText"):
        return "%s (About, about.json)" % a["subscriberCountText"].replace(" subscribers", "")
    sc = simscore.get(cid)
    if sc and sc.get("subscriberCount"):
        return "%s (NexLev sim-ch, %s)" % (format(sc["subscriberCount"], ","), (sc.get("updatedAt") or "")[:10])
    return "not found"


out = {
    "pulled": "2026-10-23",
    "by": "HVAC study round 2 helper (up-next / similar harvest)",
    "method": {
        "up_next": "innertube POST https://www.youtube.com/youtubei/v1/next {context WEB 2.20241001, hl=en, gl=US, videoId}, logged out, "
                   "via data/tools/upnext.py; first page (20 items) + 2 continuation pages (20 each) = 60 items per video. "
                   "Views in up-next are YouTube's rounded short text (e.g. '958K'); length is the thumbnail badge text.",
        "hop1_inputs": {"seeds_22": SEEDS22, "borderline_top5": BORDER5},
        "hop2_inputs": HOP2,
        "hop2_rule": "the 10 most-recommended HVAC videos (title reading) from channels other than Silver Cymbal in hop 1, ranked by "
                     "number of hop-1 sources (27) whose up-next list holds them; ties at 4 broken by best mean position.",
        "nexlev_similar_videos": "get_similar_videos(videoId) for each of the 22 seeds (not the 5 borderline). Semantic title match "
                                 "over NexLev's index, not YouTube's recommendations. 4 results came back inline (short) and their "
                                 "key fields were transcribed by the helper (marked in 'source').",
        "nexlev_similar_channels": "get_similar_channels(UC67dKTEwpAhKv2oYDATwR8g, level=3, async) -> 159 channels",
        "nexlev_suggested_videos": "search_youtube_suggested_videos has no video-ID input, so it cannot give 'suggested next to seed X'. "
                                   "Ran 6 title-keyword queries (isFromHomeFeed=true, minDuration=300, sortBy=views, limit=100). Its "
                                   "keyword match is loose (e.g. 'boiler' returns 'Boiler Room' DJ sets, 'mini split' returns kids' "
                                   "videos), so results are kept raw only and not used in the tables.",
        "tags": "HVAC / topic tags are regex readings of titles (data/tools/upnext_build.py), not measured.",
    },
    "hop1": hop1, "hop2": hop2, "nexlev_similar_videos": nlsim,
    "nexlev_similar_channels": {"jobId": scj.get("jobId"), "status": scj.get("status"), "totalResults": scj.get("totalResults"),
                                "level": 3, "channels": simch},
    "nexlev_suggested_videos_keyword": sugg,
    "channel_about_this_pull": about_mine,
    "recheck_same_seed_repull": json.load(open(os.path.join(SCR, "recheck.json"))) if os.path.exists(os.path.join(SCR, "recheck.json")) else {},
}
json.dump(out, open(OUT, "w"), indent=1, ensure_ascii=False)

# ---------- print tables
mode = sys.argv[3] if len(sys.argv) > 3 else "all"
print("hop1 sources", len(hop1), "items", sum(len(r["items"]) for r in hop1.values()),
      "| hop2 sources", len(hop2), "items", sum(len(r["items"]) for r in hop2.values()))
print("unique videos (up-next both hops)", len([v for v in vid.values() if v["h1"] or v["h2"]]),
      "| unique channels (up-next both hops)", len([c for c in ch.values() if c["h1"] or c["h2"]]),
      "| with NexLev similar", len(vid), len(ch))
if mode in ("all", "ch"):
    rows = sorted(ch.items(), key=lambda x: (-len(x[1]["h1"]), -len(x[1]["h2"]), -len(x[1]["nl"]), -x[1]["all_items"]))
    for cid, c in rows:
        if len(c["h1"]) + len(c["h2"]) + len(c["nl"]) < int(sys.argv[4] if len(sys.argv) > 4 else 3):
            continue
        ex = sorted(c["vids"].values(), key=lambda v: -(len(vid[v["id"]]["h1"]) + len(vid[v["id"]]["h2"])))
        exh = [v for v in ex if is_hv(v["title"])] or ex
        e = exh[0] if exh else None
        sc = simscore.get(cid)
        print("CH|%s|%s|%s|%d|%d|%d|%d|%d|%d/%d|alt%d|%s|%s|%s" % (
            c["name"], c["handle"], cid, len(c["h1"]), len(c["h1_core"]), len(c["h2"]), len(c["nl"]), c["all_items"],
            c["hv_items"], c["all_items"], c["alt_items"],
            ("%s|%s|%s|%s|%d" % (e["title"], e["id"], e["views_text"], e["length_text"],
                                 len(vid[e["id"]]["h1"]) + len(vid[e["id"]]["h2"]))) if e else "-",
            ("NLsim %s subs %s" % (sc["similarityScore"], sc["subscriberCount"])) if sc else "-", ""))
if mode in ("all", "vid"):
    vr = sorted(vid.items(), key=lambda x: (-(len(x[1]["h1"]) + len(x[1]["h2"])), -len(x[1]["nl"])))
    n = 0
    for k, v in vr:
        if not is_hv(v.get("title")):
            continue
        if v.get("length_s") is not None and v["length_s"] < 300:
            continue
        if not (v["h1"] or v["h2"]):
            continue
        n += 1
        print("V|%d|%s|%s|%s|%s|%s|%s|%d|%d|%d" % (n, k, v["title"], v["channel"], v.get("views_text"), v.get("nl_views"),
                                                 v.get("length_text"), len(v["h1"]), len(v["h2"]), len(v["nl"]), v["channel_id"] == SC))
        if n >= int(sys.argv[5] if len(sys.argv) > 5 else 60):
            break
if mode in ("all", "top"):
    for hop in ("h1", "h2"):
        tot = sum(tc[hop].values())
        for t, n in tc[hop].most_common():
            print("T|%s|%s|%d|%d|%.1f%%" % (hop, t, n, len(tcv[hop][t]), 100 * n / tot))
    for t, exs in tex.items():
        exs.sort(key=lambda e: -e[4])
        print("TX|%s|%s" % (t, " || ".join("%s (%s, %s, %s, x%d)" % (e[1], e[2], e[3], e[0], e[4]) for e in exs[:4])))

# ---------- markdown tables (mode md)
NOTES = {  # helper's reading of a channel from its recommended titles (not measured)
    "UCuJxFxVuj4s_MmupOMmDqCQ": "no: electrical explainers (neutral wire, 60 Hz, solid vs stranded)",
    "UCCVFpW5fDEXY47ysgDVV-AQ": "no: home-design list video (collab of 3 channels)",
    "UCe_5cyghC66jIC64KnUs77w": "no: DIY repair hacks",
    "UCT-HKsjRFI3S3BQVqeYdsYw": "heating-adjacent: off-grid / diesel-heater home heating",
    "UCkmEk3ldK7uJ1OvdLKwGrxg": "heating-adjacent: wood stoves, DIY heaters",
    "UC_eTsy7fL7l2ZXUUTiT3ShQ": "heating-adjacent: wood stoves (About title now 'Smokeless Stoves')",
    "UCj-e0GX6QhDChCPUBeX-FbA": "yes, mixed: diesel heaters + mini-split cleaning + oil burners",
    "UCq0fxytZwEYul4AmfEiXL_w": "heating-adjacent: 'unlimited heat, no electric' rocket/candle heaters",
    "UCLXV9vzJwgYOyGaZlD89VfA": "heating-adjacent: diesel heaters",
    "UC-5at4izid5vmBmbMd0RylQ": "heating-adjacent: diesel heaters",
    "UC3sPVoO93NhSdJ_vi4FpGfA": "heating-adjacent: diesel heaters",
    "UC31d5ED-_bJ7BR4hKEZSmCg": "heating-adjacent: DIY wood heater for a shop",
    "UCBK3AwEX1vL8qky015Z93vA": "partly: Japanese homes without central heating",
    "UCVsNMiYQkqwIq_gd0rTJF9g": "yes (portable / battery ACs for van and camping)",
    "UC2rzsm1Qi6N1X-wuOg_p0Ng": "partly: product tests, some AC and diesel heaters",
    "UCtXVIqkc3iBk0bV5gvcNWgw": "partly: handyman business, mini-split installs",
    "UCpb-xu6Oun_d41RjztUgFWA": "yes: AC cleaning/fixes, capacitor, filters",
    "UC2w60mhlxFmAhoi2oSDcEng": "yes: HVAC contractor DIY (Utah)",
    "UCvcKEgZcY9ZgEULZouaNAOA": "yes: faceless 'retired HVAC pro' (Roger's model)",
    "UC6nh_16KkkMHjccUXBNPEfQ": "yes: cooling/heating 'The Mexican Way'",
    "UCy0tKL1T7wFoYcxCe0xjN6Q": "partly: tech explainers incl. portable AC, heat pumps",
    "UCXuqSBlHAE6Xw-yeJA0Tunw": "no: tech (one AC video)",
    "UCR2C--KENITllxSo1aAbWWA": "operator's own plumbing channel (AC drain-line video)",
    "UCH5muwkuaCG6wBUoEWgUKBg": "no: home security (retired locksmith collab)",
    "UCwrRvd_li-w3r0SVii1YpPw": "yes: split-system AC (Australian wording), 42 subs",
    "UCm3B_8DYaxvCoK_337_ACGw": "partly: portable ACs for camping",
    "UCes1EvRjcKU4sY_UEavndBw": "no: cars (its 'cooling system' video is a car radiator)",
    "UCuxpxCCevIlF-k-K5YU8XPA": "no: cars (car AC)",
    "UCZ32JAyPXVY2f3g2VxekBjA": "partly: window-AC cleaning + dryer vents",
}
if mode == "md":
    def hv_reading(cid, c):
        if cid in NOTES:
            return NOTES[cid] + " (reading)"
        if c["all_items"] == 0:
            return "not read (NexLev similar only)"
        share = c["hv_items"] / c["all_items"]
        if share >= 0.6:
            r = "yes"
        elif share >= 0.2:
            r = "partly"
        elif share > 0:
            r = "mostly no"
        else:
            r = "no"
        if c["hv_items"] and c["alt_items"] * 2 >= c["hv_items"]:
            r = "heating-adjacent (stoves / diesel heaters)"
        return "%s (%d of %d titles; reading)" % (r, c["hv_items"], c["all_items"])

    rows = sorted(ch.items(), key=lambda x: (-len(x[1]["h1"]), -len(x[1]["h2"]), -len(x[1]["nl"]), -x[1]["all_items"]))
    hv_rows, no_rows = [], []
    for cid, c in rows:
        if cid == SC:
            continue
        isno = c["hv_items"] == 0 and c["all_items"] > 0
        if isno:
            if len(c["h1"]) >= 5:
                no_rows.append((cid, c))
        elif len(c["h1"]) + len(c["h2"]) >= 3 or len(c["nl"]) >= 3:
            hv_rows.append((cid, c))

    def ex_of(c):
        ex = sorted(c["vids"].values(), key=lambda v: -(len(vid[v["id"]]["h1"]) + len(vid[v["id"]]["h2"])))
        exh = [v for v in ex if is_hv(v["title"])] or ex
        if exh:
            e = exh[0]
            return '"%s" (`%s`, %s views, %s)' % (e["title"].replace("|", "/"), e["id"], e["views_text"] or "not shown", e["length_text"] or "not shown")
        # NexLev-only channel: take its first NexLev similar video
        for s, r in nlsim.items():
            for v in (r or {}).get("videos", []):
                if v.get("channelId") == cid_cur[0]:
                    return '"%s" (`%s`, %s views [NexLev], %s) [NexLev similar]' % (v["title"].replace("|", "/"), v["videoId"], format(int(v["viewCount"]), ",") if (v.get("viewCount") or "").isdigit() else v.get("viewCount"), v.get("lengthText"))
        return "not found"
    cid_cur = [None]
    print("| # | Channel | ID / handle | Up-next hop 1 (of 27 sources; of 22 seeds) | Up-next hop 2 (of 10) | NexLev similar videos (of 22 seeds) | HVAC-related? | Example recommended video | Subs seen (source) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for n, (cid, c) in enumerate(hv_rows, 1):
        cid_cur[0] = cid
        print("| %d | %s | `%s` %s | %d (%d) | %d | %d | %s | %s | %s |" % (
            n, (c["name"] or "").strip().replace("|", "/"), cid, c["handle"] or "", len(c["h1"]), len(c["h1_core"]), len(c["h2"]), len(c["nl"]),
            hv_reading(cid, c), ex_of(c), subs_of(cid)))
    print()
    print("NONHV")
    print("| Channel | ID / handle | Up-next hop 1 (of 27; of 22 seeds) | Hop 2 (of 10) | What it is (reading) | Example recommended video |")
    print("|---|---|---|---|---|---|")
    for cid, c in no_rows:
        cid_cur[0] = cid
        print("| %s | `%s` %s | %d (%d) | %d | %s | %s |" % ((c["name"] or "").strip().replace("|", "/"), cid, c["handle"] or "", len(c["h1"]), len(c["h1_core"]), len(c["h2"]), NOTES.get(cid, "") , ex_of(c)))
    print()
    print("VIDS")
    print("| # | Video ID | Title | Channel | Views (up-next text) | Length | Up-next hop 1 (of 27) / hop 2 (of 10) | NexLev similar (of 22) |")
    print("|---|---|---|---|---|---|---|---|")
    vr = sorted(vid.items(), key=lambda x: (-(len(x[1]["h1"]) + len(x[1]["h2"])), -len(x[1]["nl"])))
    n = 0
    own = []
    for k, v in vr:
        if not is_hv(v.get("title")) or not (v["h1"] or v["h2"]):
            continue
        if v.get("length_s") is not None and v["length_s"] < 300:
            continue
        if v.get("channel_id") == SC:
            own.append((k, v)); continue
        n += 1
        if n <= 40:
            print("| %d | `%s` | \"%s\" | %s | %s | %s | %d / %d | %d |" % (n, k, v["title"].replace("|", "/"), (v["channel"] or "").replace("|", "/"),
                  v.get("views_text") or "not shown", v.get("length_text") or "not shown", len(v["h1"]), len(v["h2"]), len(v["nl"])))
    print()
    print("OWN", "; ".join('"%s" (`%s`) %d/%d' % (v["title"], k, len(v["h1"]), len(v["h2"])) for k, v in own[:12]))
    print("counts: hv_rows", len(hv_rows), "no_rows", len(no_rows), "hvac videos (>=5min or no length, other channels)", n)
