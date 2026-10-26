#!/usr/bin/env python3
"""Merge Silver Cymbal tab pull + /next exact details into one full list. Usage: python3 -I sc_build.py <rawdir> <out.json>"""
import sys, json, os, statistics
raw, out = sys.argv[1], sys.argv[2]
tab = json.load(open(os.path.join(raw, "tab-allsorts-2026-10-23.json")))
nx = {}
for l in open(os.path.join(raw, "next-2026-10-23.jsonl")):
    r = json.loads(l); nx[r["id"]] = r
pop_rank = {v["id"]: i + 1 for i, v in enumerate(tab["sorts"]["Popular"])}
def secs(t):
    if not t: return None
    p = [int(x) for x in t.split(":")]; s = 0
    for x in p: s = s * 60 + x
    return s
vids = []
for i, v in enumerate(tab["sorts"]["Latest"]):
    n = nx.get(v["id"], {})
    vids.append({"id": v["id"], "title": n.get("title") or v["title"], "title_tab": v["title"],
                 "views": n.get("views"), "views_tab_rounded": v["views_tab"], "published": n.get("date"),
                 "date_text": n.get("date_text"), "duration_text": v["dur"], "duration_s": secs(v["dur"]),
                 "latest_rank": i + 1, "popular_rank": pop_rank.get(v["id"]),
                 "src": {"title": "innertube /next videoPrimaryInfoRenderer (tab title kept as title_tab)",
                         "views": "innertube /next videoViewCountRenderer, exact, pulled " + (n.get("pulled") or "")[:19] + "Z",
                         "published": "innertube /next dateText (exact day)",
                         "duration_s": "channel Videos tab thumbnail overlay text (m:ss, exact to the second)"}})
res = {"channel": tab["channel"], "channel_id": tab["id"], "handle": "@SilverCymbal", "subs_header": tab["subs"],
       "videos_header": tab["videos"], "tab_pulled": tab["pulled"], "source": tab["source"],
       "sort_checks": {"Popular": "works: 538 videos, 0 cases of views rising down the list (rounded tab text), checked 2026-10-23",
                       "Oldest": "works: 538 videos, 0 cases of age text getting newer down the list; first KZL7tt3culs (2015-08-29), last = newest upload",
                       "Latest": "default page + its continuation stopped at 30; the Latest chip paged to all 538 = Oldest reversed",
                       "same_ids": "Popular, Oldest and Latest-chip lists hold the same 538 IDs"}, "shorts_tab": ["EpGDf1jp0vA (1 Short; Shorts tab, 'Few Know the 3 Uses for the Metal Cap on a Drywall Knife #Shorts', ~2 million views per accessibility text)"],
       "n_videos_tab": len(vids), "videos": vids}
json.dump(res, open(out, "w"), indent=1, ensure_ascii=False)
lf = [v for v in vids if v["duration_s"] is not None and v["duration_s"] >= 300]
print("total", len(vids), "longform", len(lf), "under300", len([v for v in vids if v["duration_s"] is not None and v["duration_s"] < 300]), "nodur", len([v for v in vids if v["duration_s"] is None]))
