#!/usr/bin/env python3
"""Channel medians for the multiple (RESEARCH-BRIEF section 3).
For each channel: Videos tab, Latest, up to 3 pages (90 videos). Long-form = 5:00+.
Basis A: median views of long-form uploads from the last 12 months (relative age < "1y ago"), if at least 10.
Basis B otherwise: median of the last 30 long-form uploads.
Views are list-page rounded values. Usage: channel_medians.py <in.csv> <out.csv>  (resumable: skips ids already in out)."""
import csv, json, os, re, statistics, subprocess, sys
YT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yt.py")
def secs(l):
    p = [int(x) for x in re.findall(r"\d+", l or "")]
    return p[0]*3600+p[1]*60+p[2] if len(p) == 3 else (p[0]*60+p[1] if len(p) == 2 else None)
def within12(age):
    a = (age or "").lower()
    if not a: return False
    if re.search(r"\d+\s*(y|year)", a): return False
    return bool(re.search(r"\d+\s*(mo|month|w|week|d|day|h|hour|min|s\b|second)", a))
inp, outp = sys.argv[1], sys.argv[2]
done = set()
if os.path.exists(outp):
    done = {r["channel_id"] for r in csv.DictReader(open(outp))}
fields = ["channel_id", "channel", "subs", "n_long_loaded", "n_long_12mo", "basis", "median", "n_in_basis", "pulled", "error"]
new = not os.path.exists(outp)
f = open(outp, "a", newline=""); w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
if new: w.writeheader()
for r in csv.DictReader(open(inp)):
    cid = r["channel_id"]
    if not cid or cid in done: continue
    try:
        d = json.loads(subprocess.run([sys.executable, "-I", YT, "channel", cid, "latest", "3"], capture_output=True, text=True, timeout=240).stdout)
        if not d.get("channel") and not d.get("subs") and not d.get("videos"):
            raise RuntimeError("blank page (no channel, subs or videos)")  # added 2026-10-26 after checker E: silent failed loads
        vids = [v for v in d.get("videos", []) if (secs(v.get("dur")) or 0) >= 300 and v.get("views") is not None]
        y = [v["views"] for v in vids if within12(v.get("age"))]
        if len(y) >= 10: basis, vals = "A: long-form last 12 months", y
        else: basis, vals = "B: last 30 long-form", [v["views"] for v in vids[:30]]
        w.writerow({"channel_id": cid, "channel": d.get("channel") or r.get("channel"), "subs": d.get("subs"), "n_long_loaded": len(vids),
                    "n_long_12mo": len(y), "basis": basis, "median": statistics.median(vals) if vals else "", "n_in_basis": len(vals),
                    "pulled": "2026-10-26 yt.py Videos tab Latest (list-page rounded views)", "error": d.get("error", "")})
    except Exception as e:
        w.writerow({"channel_id": cid, "channel": r.get("channel"), "error": repr(e)[:200], "pulled": "2026-10-26"})
    f.flush()
