#!/usr/bin/env python3
"""Join channel medians to the merged videos (multiple = views / channel median) and build the sub-niche and format maps.
Inputs: data/merged/videos-all.csv, data/medians/channel-medians.csv. Outputs: data/merged/videos-with-multiples.csv,
data/merged/subniche-map.csv, data/merged/format-map.csv."""
import csv, os, statistics
from collections import defaultdict
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
med = {r["channel_id"]: r for r in csv.DictReader(open(os.path.join(base, "medians", "channel-medians.csv"))) if r["median"]}
rows = [r for r in csv.DictReader(open(os.path.join(base, "merged", "videos-all.csv"))) if r["subniche"] != "out"]
for r in rows:
    m = med.get(r["channel_id"])
    try: v = int(float(r["views"]))
    except: v = None
    r["views_int"] = v
    if m and v is not None and float(m["median"]) > 0:
        r["channel_median"] = m["median"]; r["median_basis"] = m["basis"]; r["multiple"] = round(v / float(m["median"]), 2)
    else:
        r["channel_median"] = r["median_basis"] = r["multiple"] = ""
out = os.path.join(base, "merged", "videos-with-multiples.csv")
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(rows)
def build(key, fn):
    d = defaultdict(list)
    for r in rows:
        k = (r[key] or "").split(";")[0].replace("other:", "") or "unlabelled"
        d[k].append(r)
    res = []
    for k, L in d.items():
        vs = [r["views_int"] for r in L if r["views_int"] is not None]
        ms = [r["multiple"] for r in L if r["multiple"] != ""]
        top = sorted(L, key=lambda r: -(r["views_int"] or 0))[:3]
        res.append({key: k, "videos": len(L), "channels": len({r["channel_id"] for r in L}),
                    "median_views": int(statistics.median(vs)) if vs else "", "videos_1M_plus": sum(1 for v in vs if v >= 1_000_000),
                    "videos_with_multiple": len(ms), "median_multiple": round(statistics.median(ms), 2) if ms else "",
                    "share_2x_plus": f"{100*sum(1 for m in ms if m >= 2)/len(ms):.0f}%" if ms else "",
                    "biggest": " ; ".join(f'{t["title"][:70]} ({t["channel"]}, {t["video_id"]}, {t["views_int"]:,})' for t in top if t["views_int"] is not None)})
    res.sort(key=lambda r: -(r["median_views"] or 0))
    with open(os.path.join(base, "merged", fn), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(res)
    return res
s = build("subniche", "subniche-map.csv"); fm = build("format", "format-map.csv")
print("rows", len(rows), "with multiple", sum(1 for r in rows if r["multiple"] != ""))
for r in s: print(f'{r["subniche"]:24} {r["videos"]:5} ch{r["channels"]:5} med {r["median_views"]:>8} mult {r["median_multiple"]:>5} 2x+ {r["share_2x_plus"]:>4} 1M+ {r["videos_1M_plus"]}')
print("---")
for r in fm:
    if r["videos"] >= 20: print(f'{r["format"]:34} {r["videos"]:5} med {r["median_views"]:>8} mult {r["median_multiple"]:>5} 2x+ {r["share_2x_plus"]:>4}')
