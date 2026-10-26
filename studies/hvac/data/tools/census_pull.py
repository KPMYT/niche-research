#!/usr/bin/env python3
"""Round 3 census pull (2026-10-26): runs yt_allsorts.py (Videos tab: Latest, Popular, Oldest; up to 4 pages = ~120
videos per sort) for every tier A-D channel in raw/channels-master-2026-10-24.csv. Resumable: skips channels whose
output file exists. Usage: python3 -I census_pull.py OUTDIR SHARD NSHARDS"""
import csv, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(os.path.dirname(HERE), "raw")
out, shard, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
os.makedirs(out, exist_ok=True)
rows = [r for r in csv.DictReader(open(os.path.join(RAW, "channels-master-2026-10-24.csv"))) if r["tier"] in ("A", "B", "C", "D") and r["channel_id"].startswith("UC")]
rows.sort(key=lambda r: r["channel_id"])
for r in rows[shard::n]:
    f = os.path.join(out, r["channel_id"] + ".json")
    if os.path.exists(f): continue
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, "yt_allsorts.py"), r["channel_id"], f, "4"], capture_output=True, text=True, timeout=600)
    print(r["channel_id"], (p.stdout or p.stderr).strip()[-160:], flush=True)
    time.sleep(0.5)
print("done", flush=True)
