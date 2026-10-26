#!/usr/bin/env python3
"""Round 4 (labelling) batches, 2026-10-26. The set: every tier A-C HVAC video in raw/subniches-2026-10-26.csv
whose scope is home / general / unmapped / adjacent (trade and out left out), plus the top-100 and recent-winner
videos not already in it. Split into 8 batches by channel (a channel's videos stay together), each with the same
40 calibration titles (calib=1, seed 2627) so agreement between labellers can be measured.
Writes raw/round4/batch-1..8.csv. Usage: python3 -I round4_batches.py"""
import csv, os, random, re, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(os.path.dirname(HERE), "raw"); STUDY = os.path.dirname(os.path.dirname(HERE))
rows, seen = [], set()
for r in csv.DictReader(open(os.path.join(RAW, "subniches-2026-10-26.csv"), encoding="utf-8")):
    if r["tier"] in ("A", "B", "C") and r["scope"] in ("home", "general", "unmapped", "adjacent") and r["video_id"] not in seen:
        seen.add(r["video_id"])
        rows.append({"video_id": r["video_id"], "title": r["title"], "channel": r["channel"], "channel_id": r["channel_id"],
                     "tier": r["tier"], "type": r["type"], "views": r["views_tab"], "views_kind": "tab-rounded",
                     "approx_date": r["approx_date"], "last12m": r["last12m"], "multiple": r["multiple"],
                     "rule_subniche": r["subniche"], "source": "census"})
extra = []
for name in ("top-100.csv",):
    for r in csv.DictReader(open(os.path.join(STUDY, name), encoding="utf-8")):
        if r["video_id"] not in seen:
            seen.add(r["video_id"])
            extra.append({"video_id": r["video_id"], "title": r["title"], "channel": r["channel"], "channel_id": r["channel_id"],
                          "tier": r.get("census_tier", ""), "type": r.get("channel_type", ""), "views": r["views"], "views_kind": "exact",
                          "approx_date": r["upload_date"], "last12m": "", "multiple": r.get("multiple", ""),
                          "rule_subniche": r.get("subniche_reading", ""), "source": "top-100"})
# recent-winners.md tables: pull video IDs in backticks with 11 chars
rw = open(os.path.join(STUDY, "recent-winners.md"), encoding="utf-8").read()
ids = set(re.findall(r"`([A-Za-z0-9_-]{11})`", rw))
exact = {}
import json
try:
    for v in json.load(open(os.path.join(RAW, "topvideos-exact-2026-10-26.json"))).get("videos", []):
        exact[v.get("id") or v.get("video_id")] = v
except Exception:
    pass
for vid in sorted(ids - seen):
    m = re.search(r"\|[^|\n]*`" + re.escape(vid) + r"`[^\n]*", rw)
    line = m.group(0) if m else ""
    t = re.search(r'"([^"]+)"', line)
    seen.add(vid)
    extra.append({"video_id": vid, "title": t.group(1) if t else "", "channel": "", "channel_id": "", "tier": "", "type": "",
                  "views": "", "views_kind": "see recent-winners.md", "approx_date": "", "last12m": "1", "multiple": "",
                  "rule_subniche": "", "source": "recent-winners"})
allrows = rows + extra
random.seed(2627)
calib = random.sample(rows, 40)
calib_ids = {r["video_id"] for r in calib}
N = 8
batches = [[] for _ in range(N)]
for r in allrows:
    if r["video_id"] in calib_ids: continue
    k = int(hashlib.md5((r["channel_id"] or r["video_id"]).encode()).hexdigest(), 16) % N
    batches[k].append(r)
cols = list(allrows[0].keys()) + ["calib"]
os.makedirs(os.path.join(RAW, "round4"), exist_ok=True)
for i, b in enumerate(batches, 1):
    with open(os.path.join(RAW, "round4", f"batch-{i}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in calib: w.writerow({**r, "calib": 1})
        for r in b: w.writerow({**r, "calib": 0})
    print(i, len(b) + 40)
print("total", len(allrows), "census", len(rows), "extra", len(extra))
