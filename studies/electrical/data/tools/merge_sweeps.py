#!/usr/bin/env python3
"""Merge the round 2 sweep videos.csv files into one deduped table (data/merged/videos-all.csv).
Keeps the row with the most exact views source; records every group that surfaced the video.
Long-form only (5:00+); rows the helper marked out (subniche 'out' or group 'out') are kept but flagged."""
import csv, os, re, sys
base = os.path.join(os.path.dirname(__file__), "..")
groups = ["wiring", "panels", "cords", "devices", "fire", "explainers"]
def secs(l):
    p = [int(x) for x in re.findall(r"\d+", l or "")]
    return p[0]*3600+p[1]*60+p[2] if len(p) == 3 else (p[0]*60+p[1] if len(p) == 2 else None)
rows = {}
for g in groups:
    for r in csv.DictReader(open(os.path.join(base, "sweep", g, "videos.csv"))):
        vid = r["video_id"]
        try: v = int(float(str(r["views"]).replace(",", "")))
        except: v = None
        s = secs(r.get("length"))
        exact = "exact" in (r.get("views_source") or "").lower() or "yt.py video" in (r.get("views_source") or "")
        rec = {"video_id": vid, "title": r["title"], "channel": r["channel"], "channel_id": r["channel_id"], "views": v,
               "views_source": r.get("views_source"), "age_or_date": r.get("age_or_date"), "length": r.get("length"), "length_s": s,
               "subniche": r.get("subniche"), "format": r.get("format"), "groups": g, "exact": exact,
               "notes": r.get("notes", "")}
        if vid in rows:
            o = rows[vid]; o["groups"] += ";" + g
            if (exact and not o["exact"]) or (v and o["views"] and v > o["views"] and exact == o["exact"]):
                for k in ("views", "views_source", "age_or_date", "exact"): o[k] = rec[k]
            if o.get("subniche") in (None, "", "out") and rec["subniche"] not in (None, "", "out"):
                o["subniche"], o["format"] = rec["subniche"], rec["format"]
        else:
            rows[vid] = rec
out = sorted(rows.values(), key=lambda x: -(x["views"] or 0))
fn = os.path.join(base, "merged", "videos-all.csv")
with open(fn, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(out)
lf = [r for r in out if r["length_s"] and r["length_s"] >= 300]
print("unique", len(out), "long-form", len(lf), "flagged out", sum(1 for r in lf if (r["subniche"] or "") == "out"), "->", fn)
