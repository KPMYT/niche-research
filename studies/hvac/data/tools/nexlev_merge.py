#!/usr/bin/env python3
"""Merge saved NexLev niche-finder results (tool-result files) into one JSON keyed by channel.
Usage: python3 -I nexlev_merge.py out.json file1 [file2 ...]
Each input is the saved MCP result ([{type,text},{type,text(json)}]). Records which query found each channel."""
import json, sys
out = sys.argv[1]
try: db = json.load(open(out))
except Exception: db = {"pulled": "2026-10-23", "source": "NexLev search_niche_finder_channels", "queries": [], "channels": {}}
for f in sys.argv[2:]:
    try: d = json.load(open(f))
    except Exception as e: print("skip", f, e); continue
    js = None
    for part in d:
        t = part.get("text", "")
        if t.strip().startswith("{"):
            try: js = json.loads(t)
            except Exception: pass
    if not js or "channels" not in js: print("nojson", f); continue
    q = js.get("niche") or js.get("query") or "?"
    if q not in [x["query"] for x in db["queries"]]:
        db["queries"].append({"query": q, "file": f.split("/")[-1], "n": len(js["channels"])})
    for c in js["channels"]:
        cid = c["ytChannelId"]
        e = db["channels"].setdefault(cid, {"rec": c, "found_by": []})
        if q not in e["found_by"]: e["found_by"].append(q)
json.dump(db, open(out, "w"), indent=1)
print(len(db["queries"]), "queries,", len(db["channels"]), "channels")
