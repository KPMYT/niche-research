#!/usr/bin/env python3
"""Batch channel page pull (2026-10-23). For each channel ID: About panel (yt_water1.py about) and
Videos tab latest + Popular first page (yt.py). Usage: python3 -I about_batch.py ids.txt outdir
Writes outdir/<id>.json (from yt.py) and outdir/about.json (all About panels)."""
import sys, json, subprocess, os
here = os.path.dirname(os.path.abspath(__file__))
ids = [l.split()[0] for l in open(sys.argv[1]) if l.strip() and l.startswith("UC")]
out = sys.argv[2]; os.makedirs(out, exist_ok=True)
ap = os.path.join(out, "about.json")
try: about = json.load(open(ap))
except Exception: about = {}
for cid in ids:
    if cid in about and os.path.exists(os.path.join(out, cid + ".json")): continue
    try:
        r = subprocess.run(["python3", "-I", os.path.join(here, "yt_water1.py"), "about", cid], capture_output=True, text=True, timeout=90).stdout
    except Exception as e: r = "ERR " + str(e)
    a = {}
    for line in r.splitlines():
        if ":" in line:
            k, v = line.split(":", 1); a[k.strip()] = v.strip()
    about[cid] = a
    json.dump(about, open(ap, "w"), indent=1)
    try:
        subprocess.run(["python3", "-I", os.path.join(here, "yt.py"), cid, out, "1"], capture_output=True, text=True, timeout=120)
    except Exception: pass
    print(cid, a.get("TITLE", "?"), a.get("subscriberCountText"), flush=True)
