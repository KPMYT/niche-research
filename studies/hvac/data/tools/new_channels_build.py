#!/usr/bin/env python3
"""Deliverable 2 (new channels taking off), HVAC study, round 3. Written 2026-10-26 by the new-channels helper.

Reads (all pulled 2026-10-26 unless noted):
  data/raw/census-channels-2026-10-26.csv   tiers, NEW_12M, subs, joined (About 2026-10-23/24)
  data/raw/census-videos-2026-10-26.csv     every long-form video (tab views ROUNDED, dates APPROXIMATE)
  data/raw/census-2026-10-26/<id>.json      Videos tab (Latest / Popular / Oldest sorts, exact order)
  data/raw/census-sells-2026-10-26.csv      what each channel sells
  data/raw/census-types-{A,B,C}-2026-10-26.csv  types, if present (else the census CSV's carried type)
  data/raw/channels-master-about-2026-10-24.json  About text (persona name / background readings)

Usage:
  python3 -I new_channels_build.py select <ids_out.txt>      rank, pick top 25, write video IDs for exact pulls
  python3 -I new_channels_build.py build <exact.jsonl>       write new-channels CSV + exact JSON + tables (md parts)
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
    d0 = date.fromisoformat(start) if start else None
    months = max(((PULL - d0).days / 30.44) if d0 else 0, 0.5)
    return dict(since=since, lf_since=len(since), lf_views_since=tot, views_90d=v90,
                best_views=num(best["views_tab"]) if best else 0, best=best,
                hvac_lf_since=len(hv), hvac_views_since=sum(num(v["views_tab"]) for v in hv),
                hvac_best=hbest, months=months, pace=len(since) / months, subs=num(r["subs"]))


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
    r["_well_above"] = r["_score"] >= 3 and r["_n3x"] >= 2
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
    print("well above:", sum(r["_well_above"] for r in NEW), {t: sum(r["_well_above"] for r in NEW if r["tier"] == t) for t in "ABC"})
    print(collections.Counter(r["_status"] for r in NEW))
    for i, r in enumerate(NEW[:40], 1):
        m = r["_m"]
        print(i, r["tier"], r["name"], r["_status"], r["subs"], m["lf_since"], m["lf_views_since"], m["views_90d"], m["best_views"],
              round(r["_score"], 1), r["_n3x"], r["lane_tags"])
    print(len(ids), "ids")
