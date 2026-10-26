#!/usr/bin/env python3
"""Deliverable 2 (new channels taking off), HVAC study, round 3. Written 2026-10-26 by the new-channels helper.

Reads (all pulled 2026-10-26 unless noted):
  data/raw/census-channels-2026-10-26.csv   tiers, NEW_12M, subs, joined (About 2026-10-23/24)
  data/raw/census-videos-2026-10-26.csv     every long-form video (tab views ROUNDED, dates APPROXIMATE)
  data/raw/census-2026-10-26/<id>.json      Videos tab (Latest / Popular / Oldest sorts, exact order)
  data/raw/census-sells-2026-10-26.csv      what each channel sells
  data/raw/census-types-{A,B,C}-2026-10-26.csv  types, if present (else the census CSV's carried type)
  data/raw/channels-master-about-2026-10-24.json  About text (persona name / background readings)
  data/raw/new-channels-handread-2026-10-26.csv   round 6 hand read of every long-form title of 103 channels (y / n)

Usage:
  python3 -I new_channels_build.py select <ids_out.txt>      rank, pick top 25, write video IDs for exact pulls
  python3 -I new_channels_build.py build <exact.jsonl> <copy_matches.json> [<copies.json>]
      writes data/raw/new-channels-2026-10-26.csv and data/raw/new-channels-exact-2026-10-26.json
  (copy_matches.json and copies.json come from new_channels_copycats.py; the md tables were generated from the CSV)
"""
import csv, json, sys, os, re, statistics as st, math, collections, datetime
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "raw"))
STUDY = os.path.normpath(os.path.join(HERE, "..", ".."))
PULL = date(2026, 10, 26)
WINDOW = date(2025, 10, 26)            # 12 months before the pull
W = WINDOW.isoformat()
TOP_N = 25
HIT = 100_000                           # "first hit" = first long-form since start with 100,000+ views
# Round 3 fix 4.1 (round 3 fixer, 2026-10-26; main session decision): "well above" also needs an HVAC view share of
# 20%+ = views on HVAC titles (census is_hvac) / all long-form views since the start, both from census-videos (tab
# views, rounded). The ranking (score) is unchanged; a channel under 20% keeps its rank but is not "well above".
HVAC_SHARE_MIN = 0.20
# Hand check of the share (round 3 fixer, 2026-10-26): the census is_hvac rule misses some heating titles ("Heats a
# House", "Heated the House"). Every channel the 20% rule drops, and the borderline Elias Yoder (20.6%), was read by
# hand: titles the rule missed are added and its false hits removed (titles exactly as in census-videos; operator rules
# apply: insulation / windows need a heat word, water heaters, frozen pipes, car heat and food cold-storage are out).
# The hand share decides "well above" where one is given. Channel: (add titles, remove titles, note).
HVAC_SHARE_HAND = {
    "UCf4NyCLKkNrah_L9q5HVvzA": (["The $12 Norwegian Stove That Heats a House for 18 Hours on One Log — Rocket Mass Heater Decoded",
                                  "$15 Russian Pechka — The Brick Stove That Cooked, Heated, and Slept Entire Families for 800 Years",
                                  "The $30 Korean Ondol System That Heated Floors for 2,000 Years — Why Modern Builders Forgot It",
                                  "$8 Solar Box That Heats a Room All Winter — The Off-Grid Trick Nobody Uses",
                                  "The 1767 Swedish Tile Stove: Twelve Hours of Heat From One Fire — And How It Works"], [],
                                 "Hidden Systems: home-heating stoves the rule missed"),
    "UCMXFneU1qRWt9X_lNc36Zdw": (["Old-Timers Never Heated the House When the Power Died. They Did This ($0)",
                                  "I've Never Lost Heat in 30 Winters Off the Grid: 12 Ways Ranked Deadliest to Safest"], [],
                                 "Elias Mercer: outage home heat the rule missed"),
    "UC_yTHwUQS--7ZsCo8fxW67A": (["Stove That Saves 50% Of Firewood And Heats The House For 50 Hours Without A Fire!",
                                  'How One Mountain Man\'s "Wrong" Stove Placement Became His Smartest Idea Ever!',
                                  "How One Mountain Man’s \"Secret\" Trick Made Cabins Cooler in Summer and Warmer in Winter"], [],
                                 "Silas Mercer: 3 heating titles added (a self-heating blanket left out); still under 20%"),
    "UCntW8YWdZzyvj8cVLeyki1A": (["How Long Can 1,000 Gallons of Hot Water Heat Your House?",
                                  "This Hot Water Tank Can Heat Your Home for Days — But There’s a Catch!",
                                  "Can Your Shower Wastewater Heat Your Home AND Flush Your Toilet?"], [],
                                 "Passive House Technology: 3 heat titles added; its 2.6M video is a battery, still under 20%"),
    "UC--v6NZz9jkKIgqPsIAfQog": (["The Amish Never Heated the House When the Power Died. They Did This ($0)"], [],
                                 "Elias Homestead: 1 title added; lawn and weed channel, still under 20%"),
    "UCgdljd9PHGxqvDGgabrKvZg": (["This $300 Sand Drum Warms Any Home All Winter. Why Did They Remove It?",
                                  "Why Did We Quit Using Ammonia To Cool Our Homes?"], [],
                                 "Hidden Homestead: 2 titles added (food-cold and insulation-without-heat-word left out); still under 20%"),
    "UCEInLGzWBsSsI5UVb4NowUQ": (["9 Winter Mistakes That Are Costing You Hundreds in Your Home"], [],
                                 "Donna Fixes: 1 title added; winter living-alone lists are not HVAC; still under 20%"),
    "UCaj8oe2fiZNjXzX1QEZ1F2A": ([], ["Crystal Clear Water With a Bucket... The Cheap Old Filter",
                                      "The $15 AMISH Wood-Stove TRICK That Makes FREE ELECTRICITY (No Solar, No Grid)."],
                                 "Elias Yoder (borderline 20.6% by rule): a water filter and a power (not heat) title removed; stays over 20%"),
}
# read by hand, nothing to add or remove (all still under 20%): Forgotten American Survival (blackout meals and kits),
# Walter's Tool Talk (frozen pipes, out), SafeMind (outdoor cold survival, car heat), Walt Brandt (water heaters, out),
# The Sensei's Home (food cold / generators not for warmth), Forgotten Appalachian Skills (winter-storm lore).
#
# Round 6 hand read (round 6 fixer, 2026-10-26; replaces the title rule for the channels it covers): every long-form
# title of 103 channels (the 60 well above, every channel scoring 2.4+ = 0.8x the score threshold, every channel with an
# HVAC view share of 10-30%) marked in scope y / n by round4/LABEL-GUIDE.md, in data/raw/new-channels-handread-2026-10-26.csv
# (round 4 hand labels reused where the title has one and agrees; every row says its source). For a channel in that file
# the hand read decides the HVAC view share (it replaces HVAC_SHARE_HAND above), the best HVAC video and the takeoff
# videos' HVAC column; the 20% rule is unchanged. Channels not in the file keep the census rule (is_hvac). Readings.
HANDREAD_PATH = os.path.join(RAW, "new-channels-handread-2026-10-26.csv")
HANDREAD = collections.defaultdict(dict)
if os.path.exists(HANDREAD_PATH):
    for _h in csv.DictReader(open(HANDREAD_PATH)):
        assert _h["in_scope"] in ("y", "n"), _h
        HANDREAD[_h["channel_id"]][_h["video_id"]] = _h["in_scope"]


def in_scope(cid, v):
    """HVAC title or not: the round 6 hand read where the channel has one, else the census rule."""
    if cid in HANDREAD:
        return HANDREAD[cid][v["video_id"]] == "y"
    return v["is_hvac"] == "yes"

csv.field_size_limit(10**9)
ch = {r["channel_id"]: r for r in csv.DictReader(open(os.path.join(RAW, "census-channels-2026-10-26.csv")))}
vids = collections.defaultdict(list)
for v in csv.DictReader(open(os.path.join(RAW, "census-videos-2026-10-26.csv"))):
    vids[v["channel_id"]].append(v)
sells = {r["channel_id"]: r for r in csv.DictReader(open(os.path.join(RAW, "census-sells-2026-10-26.csv")))}
about = json.load(open(os.path.join(RAW, "channels-master-about-2026-10-24.json")))["channels"]
types = {}
for t in "ABC":
    p = os.path.join(RAW, f"census-types-{t}-2026-10-26.csv")
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            cid = r.get("channel_id") or r.get("id")
            if cid:
                types[cid] = r

AGE_RX = re.compile(r"^(\d+)\s*(min|h|d|w|mo|y)\s+ago$")


def age(a):
    m = AGE_RX.match((a or "").strip())
    return (m.group(2), int(m.group(1))) if m else (None, None)


def within90(a):
    u, n = age(a)
    return u in ("min", "h", "d", "w") or (u == "mo" and n <= 2)


def tabjson(cid):
    p = os.path.join(RAW, "census-2026-10-26", cid + ".json")
    return json.load(open(p)) if os.path.exists(p) else None


def num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def coverage_ok(r, js):
    """Is the window boundary inside the pulled lists? (Latest complete, or Latest reaches before the window,
    or the Oldest list reaches into the window.) Without it a pivot or a silence could sit in an unpulled gap."""
    if r["latest_list_complete"] == "yes":
        return True
    u, n = age(r["latest_list_oldest_age"])
    if u == "y":
        return True
    if js:
        old = [x for x in (js["sorts"].get("Oldest") or []) if x.get("meta")]
        if old:
            u2, n2 = age(old[-1]["meta"][-1])
            if u2 and not (u2 == "y"):
                return True
    return False


def classify(r):
    """Returns (status, basis, start_date_iso or None). status: joined / first-longform / pivot / restart / None."""
    vs = vids[r["channel_id"]]
    pre = [v for v in vs if v["approx_date"] < W]
    post = [v for v in vs if v["approx_date"] >= W]
    if r["new_12m"] == "yes":
        b = r["new_12m_basis"]
        if b.startswith("joined"):
            return "joined", b, r["joined"]
        firsts = sorted(post, key=lambda v: v["approx_date"])
        return "first-longform", "old account (joined " + r["joined"] + "); " + b, (firsts[0]["approx_date"] if firsts else None)
    js = tabjson(r["channel_id"])
    if not coverage_ok(r, js):
        return None, "boundary not covered by the pulled lists", None
    hpre = sum(v["is_hvac"] == "yes" for v in pre)
    hpost = [v for v in post if v["is_hvac"] == "yes"]
    if len(pre) >= 3 and hpre / len(pre) < 0.10 and len(post) >= 5 and len(hpost) >= 3 and len(hpost) / len(post) >= 0.30:
        first = min(hpost, key=lambda v: v["approx_date"])
        return "pivot", (f"pivot: {hpre}/{len(pre)} HVAC long-form before {W}, {len(hpost)}/{len(post)} since; "
                         f"first HVAC long-form in window '{first['age_text']}'"), first["approx_date"]
    if pre and len(post) >= 5:
        np_ = max(pre, key=lambda v: v["approx_date"])
        u, n = age(np_["age_text"])
        if u == "y" and n >= 2:
            first = min(post, key=lambda v: v["approx_date"])
            return "restart", (f"restart: newest long-form before the window '{np_['age_text']}' (12+ months silent), "
                               f"{len(post)} long-form since, first '{first['age_text']}'"), first["approx_date"]
    return None, "", None


def metrics(r, start):
    vs = vids[r["channel_id"]]
    # joined / first-longform: every long-form video is inside the window; pivot / restart: from the start date on
    since = list(vs) if r["_status"] in ("joined", "first-longform") else [v for v in vs if v["approx_date"] >= start]
    since = [v for v in since if num(v["views_tab"]) is not None]
    tot = sum(num(v["views_tab"]) for v in since)
    v90 = sum(num(v["views_tab"]) for v in since if within90(v["age_text"]))
    best = max(since, key=lambda v: num(v["views_tab"])) if since else None
    hv = [v for v in since if v["is_hvac"] == "yes"]
    hbest = max(hv, key=lambda v: num(v["views_tab"])) if hv else None
    # round 6 hand read (where the channel has one): HVAC titles and the best HVAC video by hand
    cid = r["channel_id"]
    hh = [v for v in since if in_scope(cid, v)] if cid in HANDREAD else None
    hhbest = (max(hh, key=lambda v: num(v["views_tab"])) if hh else None) if hh is not None else hbest
    d0 = date.fromisoformat(start) if start else None
    months = max(((PULL - d0).days / 30.44) if d0 else 0, 0.5)
    return dict(since=since, lf_since=len(since), lf_views_since=tot, views_90d=v90,
                best_views=num(best["views_tab"]) if best else 0, best=best,
                hvac_lf_since=len(hv), hvac_views_since=sum(num(v["views_tab"]) for v in hv),
                hvac_best_rule=hbest, hvac_best=hhbest,
                hvac_lf_since_hand=len(hh) if hh is not None else None,
                hvac_views_since_hand=sum(num(v["views_tab"]) for v in hh) if hh is not None else None,
                months=months, pace=len(since) / months, subs=num(r["subs"]))


# ---- 1. the new set
NEW = []
for r in ch.values():
    if r["tier"] not in ("A", "B", "C"):
        continue
    s, b, start = classify(r)
    if not s:
        continue
    r["_status"], r["_basis"], r["_start"] = s, b, start
    r["_m"] = metrics(r, start)
    NEW.append(r)

# ---- 2. tier medians among the new set, ratios, score
KEYS = ["lf_views_since", "views_90d", "subs", "best_views"]
MED = {}
for t in "ABC":
    tr = [r for r in NEW if r["tier"] == t]
    MED[t] = {k: st.median([r["_m"][k] or 0 for r in tr]) for k in KEYS}
    MED[t]["n"] = len(tr)
for r in NEW:
    rat = {}
    for k in KEYS:
        med = max(MED[r["tier"]][k], 1)
        rat[k] = (r["_m"][k] or 0) / med
    r["_ratio"] = rat
    r["_score"] = math.exp(sum(math.log(max(x, 0.01)) for x in rat.values()) / len(rat))
    r["_n3x"] = sum(x >= 3 for x in rat.values())
    r["_well_above_score_rule"] = r["_score"] >= 3 and r["_n3x"] >= 2
    m_ = r["_m"]
    r["_hvac_share"] = (m_["hvac_views_since"] / m_["lf_views_since"]) if m_["lf_views_since"] else 0.0
    r["_hvac_share_hand"], r["_hvac_share_hand_note"] = None, ""
    if r["channel_id"] in HANDREAD:
        byid = {v["video_id"]: v for v in m_["since"]}
        added = sum(1 for i, v in byid.items() if in_scope(r["channel_id"], v) and v["is_hvac"] != "yes")
        removed = sum(1 for i, v in byid.items() if not in_scope(r["channel_id"], v) and v["is_hvac"] == "yes")
        r["_hvac_share_hand"] = m_["hvac_views_since_hand"] / m_["lf_views_since"] if m_["lf_views_since"] else 0.0
        r["_hvac_share_hand_note"] = (f"round 6 hand read of all {len(byid)} long-form titles since the start "
                                      f"({m_['hvac_lf_since_hand']} in scope; +{added} / -{removed} vs the rule; "
                                      f"hand share {r['_hvac_share_hand']:.3f})")
    elif r["channel_id"] in HVAC_SHARE_HAND:
        add, rem, note = HVAC_SHARE_HAND[r["channel_id"]]
        byt = {v["title"]: v for v in m_["since"]}
        miss = [t for t in add + rem if t not in byt]
        assert not miss, (r["name"], miss)
        hv = m_["hvac_views_since"] + sum(num(byt[t]["views_tab"]) for t in add if byt[t]["is_hvac"] != "yes") \
            - sum(num(byt[t]["views_tab"]) for t in rem if byt[t]["is_hvac"] == "yes")
        r["_hvac_share_hand"] = hv / m_["lf_views_since"] if m_["lf_views_since"] else 0.0
        r["_hvac_share_hand_note"] = f"{note} (+{len(add)} / -{len(rem)} titles; hand share {r['_hvac_share_hand']:.3f})"
    share_used = r["_hvac_share"] if r["_hvac_share_hand"] is None else r["_hvac_share_hand"]
    r["_well_above"] = r["_well_above_score_rule"] and share_used >= HVAC_SHARE_MIN
NEW.sort(key=lambda r: -r["_score"])
TOP = NEW[:TOP_N]


def order_list(cid):
    """Exact upload order (oldest first) of the Videos tab where known: Latest list reversed, extended by Oldest."""
    js = tabjson(cid)
    if not js:
        return [], False
    lat = [x for x in (js["sorts"].get("Latest") or []) if x.get("id")]
    old = [x for x in (js["sorts"].get("Oldest") or []) if x.get("id")]
    lat_ids = [x["id"] for x in lat]
    seq = list(reversed(lat))
    complete = ch[cid]["latest_list_complete"] == "yes"
    if not complete and old:
        ids = set(lat_ids)
        if any(x["id"] in ids for x in old):          # the two lists overlap: full order known
            pre = []
            for x in old:
                if x["id"] in ids:
                    break
                pre.append(x)
            seq = pre + seq
            complete = True
        else:                                          # no overlap: Oldest list, then a gap, then the Latest list
            seq = old + [{"id": "__GAP__"}] + seq
    return seq, complete


def first_longform(r):
    """The first long-form video since the start: earliest in exact tab order where the order is known."""
    since = {v["video_id"]: v for v in r["_m"]["since"]}
    seq, _ = order_list(r["channel_id"])
    for x in seq:
        if x["id"] in since:
            return since[x["id"]]
    return min(since.values(), key=lambda v: v["approx_date"]) if since else None


if __name__ == "__main__" and sys.argv[1] == "select":
    ids = []
    for r in TOP:
        m = r["_m"]
        top3 = sorted(m["since"], key=lambda v: -num(v["views_tab"]))[:3]
        hits = [v for v in m["since"] if num(v["views_tab"]) >= int(HIT * 0.8)]
        hb = [m["hvac_best"]] if m["hvac_best"] else []
        fl = first_longform(r)
        for v in top3 + hits + hb + ([fl] if fl else []):
            if v["video_id"] not in ids:
                ids.append(v["video_id"])
    open(sys.argv[2], "w").write("\n".join(ids) + "\n")
    print(len(NEW), "new;", {t: MED[t] for t in MED})
    print("well above (score rule only):", sum(r["_well_above_score_rule"] for r in NEW),
          [r["name"] for r in NEW if r["_well_above_score_rule"] and not r["_well_above"]])
    print("well above:", sum(r["_well_above"] for r in NEW), {t: sum(r["_well_above"] for r in NEW if r["tier"] == t) for t in "ABC"})
    print(collections.Counter(r["_status"] for r in NEW))
    for i, r in enumerate(NEW[:40], 1):
        m = r["_m"]
        print(i, r["tier"], r["name"], r["_status"], r["subs"], m["lf_since"], m["lf_views_since"], m["views_90d"], m["best_views"],
              round(r["_score"], 1), r["_n3x"], r["lane_tags"])
    print(len(ids), "ids")


# =====================================================================================================================
# build: CSV, exact JSON, markdown table parts
# =====================================================================================================================
LANE_OF_TAG = {"outage": "outage and winter prep", "survival": "outage and winter prep", "generator": "outage and winter prep",
               "off-grid": "off-grid, old ways and free heat", "old-ways": "off-grid, old ways and free heat",
               "diy-stove-craft": "off-grid, old ways and free heat", "solar": "off-grid, old ways and free heat",
               "frugal": "bills and frugal hacks", "energy": "bills and frugal hacks", "product-lists": "product lists"}


def lane(r):
    """Lane by rule (a reading): first (most common) lane tag; else brand verdict if that is the top sub-niche of an
    A channel; else 'HVAC repair and explainers' for tier A, 'mixed / other main topic' for B and C."""
    tags = [t for t in r["lane_tags"].split(";") if t]
    if tags:
        return LANE_OF_TAG.get(tags[0], tags[0])
    if r["tier"] == "A":
        if r["main_subniches"].startswith("brand verdicts"):
            return "HVAC brand verdicts"
        return "HVAC repair and explainers"
    return "mixed / other main topic"


def load_exact(p):
    ex = {}
    for l in open(p):
        if l.strip():
            d = json.loads(l)
            if "error" not in d:
                ex[d["id"]] = d
    return ex


HOOK_RX = r"banned|illegal|hid(e|den|ing)?\b|buried|bury|don'?t want you|won'?t tell|nobody tells|secret|1% of|they (don'?t|won'?t)|hope you|exterminators|mechanics want|monopol"


def tmpl(title):
    """Title template of a takeoff video (a reading by rule; first match wins). Order matters."""
    t = title.lower()
    rules = [
        ("'(The X Way)' / Amish tradition key", r"\(the \w+ way\)|\bamish\b"),
        ("'Before you X, do this (or pay for it)'", r"^before you|or pay (for it|the price)"),
        ("'N [store] items for winter / a blackout'", r"^\d+ .*(dollar tree|walmart|tractor supply|tesco)"),
        ("'I tested X' / 'Can X really ...? I tried it'", r"^i tested|i (actually )?tried it|^will my|^can (a|an|this)"),
        ("'The only N X worth buying'", r"only \d+ .*worth|brands? (to avoid|worth)"),
        ("'Do this and your X will last N years'", r"(will|can) last \d+ years|last(s)? \d+ years if"),
        ("'Why ...?' expose ('Why did we stop X?', 'Why X is destroying Y')", r"^why (did|do|don'?t|is|are|aren'?t|the|your|installing)"),
        ("insider secret ('only 1% of techs know', 'the loophole')", r"1% of|loophole|only known"),
        ("'N X worth a fortune' (collectibles)", r"worth a fortune"),
        ("how-to", r"^how to"),
        ("'This $X thing does Y (forever / for free / no power)'", r"^(this|these|the) (\$|\d|\"|[a-z\-]+ )?.*(cools?|heats?|keeps?|beats?|pulls?|kills?|makes?|purif|repels?|freezes|costs?|cuts?)"),
        ("'N X mistakes / habits / dangers / things'", r"^(the )?\d+ .*(mistakes|habits|dangers|things|signs|fees|settings|woods)"),
        ("'N [cheap / old / forgotten] tricks / ways / sources'", r"^(the )?\d+ .*(tricks|ways|sources|items|hacks|recipes|methods|designs|heaters)"),
        ("'Doing this will ...' / 'Do THIS ...' command", r"^(do|doing|stop|kill|turn|mix|attach|connecting|\$\d+ liquid|1 cup)"),
        ("'DIY build' / 'turning X into Y'", r"diy|turning|build|homemade"),
        ("first-person job story", r"^(my|they|single|i |we )"),
    ]
    for name, rx in rules:
        if re.search(rx, t):
            return name
    return "other"


def build(exact_path, copies_path, copy_list_path=None):
    ex = load_exact(exact_path)
    rows = []
    for rank, r in enumerate(NEW, 1):
        m = r["_m"]
        ty = types.get(r["channel_id"], {})
        sl = sells.get(r["channel_id"], {})
        best = m["best"]
        row = {"rank": rank, "tier": r["tier"], "name": r["name"].strip(), "handle": r["handle"], "channel_id": r["channel_id"],
               "link": r["link"], "start_status": r["_status"], "start_basis": r["_basis"], "start_date_approx": r["_start"],
               "joined": r["joined"], "type": ty.get("type4") or ty.get("type") or r["type"] or "not found",
               "type_before_fix2": ty.get("type", ""),
               "company": ty.get("company") or r.get("company") or "not found",
               "type_source": ("census-types-%s-2026-10-26.csv" % r["tier"]) if ty else (r["type_source"] or "not found"),
               "persona_name": ty.get("persona_name", "") or "", "claimed_background": (ty.get("claimed_background", "") or "")[:300],
               "subs": m["subs"] if m["subs"] is not None else "not found", "total_views_about": r["total_views"],
               "lf_videos_since_start": m["lf_since"], "lf_views_since_start": m["lf_views_since"], "views_90d_floor": m["views_90d"],
               "best_video_views_tab": m["best_views"], "best_video_id": best["video_id"] if best else "",
               "best_video_title": best["title"] if best else "",
               "hvac_lf_since_start": m["hvac_lf_since"], "hvac_lf_views_since_start": m["hvac_views_since"],
               "hvac_view_share": round(m["hvac_views_since"] / m["lf_views_since"], 3) if m["lf_views_since"] else "",
               "best_hvac_video_id": m["hvac_best"]["video_id"] if m["hvac_best"] else "",
               "best_hvac_video_title": m["hvac_best"]["title"] if m["hvac_best"] else "",
               "best_hvac_video_views_tab": num(m["hvac_best"]["views_tab"]) if m["hvac_best"] else "",
               "best_hvac_video_source": ("round 6 hand read" if r["channel_id"] in HANDREAD else "census rule (is_hvac)"),
               "hvac_lf_since_start_hand": m["hvac_lf_since_hand"] if m["hvac_lf_since_hand"] is not None else "",
               "hvac_lf_views_since_start_hand": m["hvac_views_since_hand"] if m["hvac_views_since_hand"] is not None else "",
               "lf_per_month_since_start": round(m["pace"], 1), "uploads_90d_census": r["uploads_90d"],
               "ratio_lf_views": round(r["_ratio"]["lf_views_since"], 2), "ratio_views_90d": round(r["_ratio"]["views_90d"], 2),
               "ratio_subs": round(r["_ratio"]["subs"], 2), "ratio_best": round(r["_ratio"]["best_views"], 2),
               "score": round(r["_score"], 2), "metrics_at_3x": r["_n3x"],
               "well_above_score_rule": "yes" if r["_well_above_score_rule"] else "no",
               "hvac_view_share_hand": round(r["_hvac_share_hand"], 3) if r["_hvac_share_hand"] is not None else "",
               "hvac_view_share_hand_note": r["_hvac_share_hand_note"],
               "hvac_view_share_ok": "yes" if (r["_hvac_share"] if r["_hvac_share_hand"] is None else r["_hvac_share_hand"]) >= HVAC_SHARE_MIN else "no",
               "well_above": "yes" if r["_well_above"] else "no",
               "lane_rule": lane(r), "lane_tags": r["lane_tags"], "hvac_latest30": r["hvac_latest30"], "main_subniches": r["main_subniches"],
               "sells": sl.get("sells_categories", "not found"), "own_products": sl.get("own_products", "not found")}
        # takeoff detail for the top 25
        if rank <= TOP_N:
            since = {v["video_id"]: v for v in m["since"]}
            pulled = [ex[i] for i in since if i in ex]
            top3 = sorted(pulled, key=lambda e: -(e["views"] or 0))[:3]
            for k, e in enumerate(top3, 1):
                row[f"takeoff{k}_id"] = e["id"]; row[f"takeoff{k}_title"] = e["title"]
                row[f"takeoff{k}_views_exact"] = e["views"]; row[f"takeoff{k}_date_exact"] = e["date"]
                row[f"takeoff{k}_template"] = tmpl(e["title"])
                row[f"takeoff{k}_hidden_truth_hook"] = "yes" if re.search(HOOK_RX, e["title"].lower()) else "no"
                row[f"takeoff{k}_hvac"] = "yes" if in_scope(r["channel_id"], since[e["id"]]) else "no"
            seq, complete = order_list(r["channel_id"])
            seq_ids = [x["id"] for x in seq]
            hits = sorted([e for e in pulled if (e["views"] or 0) >= HIT], key=lambda e: (e["date"], seq_ids.index(e["id"]) if e["id"] in seq_ids else 0))
            fl = first_longform(r)
            fle = ex.get(fl["video_id"]) if fl else None
            row["first_lf_id"] = fl["video_id"] if fl else ""
            row["first_lf_date_exact"] = fle["date"] if fle else "not found"
            if fle:
                months = max((PULL - date.fromisoformat(fle["date"])).days / 30.44, 0.5)
                row["lf_per_month_since_first_lf"] = round(m["lf_since"] / months, 1)
            if hits:
                h = hits[0]
                row["first_hit_id"] = h["id"]; row["first_hit_title"] = h["title"]
                row["first_hit_views_exact"] = h["views"]; row["first_hit_date_exact"] = h["date"]; row["first_hit_month"] = h["date"][:7]
                i0 = seq_ids.index(fl["video_id"]) if fl and fl["video_id"] in seq_ids else None
                ih = seq_ids.index(h["id"]) if h["id"] in seq_ids else None
                if i0 is not None and ih is not None and "__GAP__" not in seq_ids[i0:ih]:
                    part = seq[i0:ih]
                    row["videos_before_first_hit_all"] = len(part)
                    row["lf_before_first_hit"] = sum(1 for x in part if x["id"] in since)
                    row["order_basis"] = "Videos tab order (Latest%s), 2026-10-26" % (" + Oldest" if not ch[r["channel_id"]]["latest_list_complete"] == "yes" else "")
                else:
                    row["videos_before_first_hit_all"] = "not found"; row["lf_before_first_hit"] = "not found"
                    row["order_basis"] = "first hit or first video outside the pulled order (gap)"
                if fle:
                    row["days_first_lf_to_first_hit"] = (date.fromisoformat(h["date"]) - date.fromisoformat(fle["date"])).days
            else:
                row["first_hit_id"] = "none (no long-form video at 100,000+)"
        rows.append(row)
    cols = []
    for rr in rows:
        for k in rr:
            if k not in cols:
                cols.append(k)
    out_csv = os.path.join(RAW, "new-channels-2026-10-26.csv")
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for rr in rows:
            w.writerow(rr)
    copies = json.load(open(copies_path))
    out_json = os.path.join(RAW, "new-channels-exact-2026-10-26.json")
    json.dump({"pulled": "2026-10-26 (innertube /next, logged out; /watch is blocked from the cloud)",
               "tool": "data/tools/vid_next_batch.py",
               "videos": sorted(ex.values(), key=lambda e: e["id"]),
               "copycat_matches": copies,
               "copycat_copies": json.load(open(copy_list_path)) if copy_list_path else "not built"},
              open(out_json, "w"), indent=1, ensure_ascii=False)
    print("wrote", out_csv, len(rows), "rows;", out_json, len(ex), "videos")
    return rows, ex, copies


if __name__ == "__main__" and sys.argv[1] == "build":
    build(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
