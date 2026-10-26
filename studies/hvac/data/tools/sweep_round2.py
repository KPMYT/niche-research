#!/usr/bin/env python3
"""Round 2 keyword sweep (2026-10-24). Based on sweep_channels.py.
Logged-out YouTube video searches (hl=en gl=US). Sorts:
  relevance  sp=EgIQAQ%3D%3D (videos only)
  views      sp=CAMSAhAB (view count)
  year       sp=CAMSBAgFEAE%3D (view count, uploaded this year)
  month      sp=CAMSBAgEEAE%3D (view count, uploaded this month)
The "upload date" sort no longer works (tested 2026-10-23) and search has no "oldest" sort; the operator
approved this substitute on 2026-10-24 (old videos come from each channel's Oldest tab instead).
Note (tested 2026-10-24): the "year" and "month" filters let a few older videos through and are not strictly in view order; filter by the "age" text in analysis.
Resumable: appends one JSON line per (keyword, sort) to OUT.jsonl and skips pairs already done.
Usage: python3 -I sweep_round2.py keywords.csv OUT.jsonl priority|extended [shard N of M]"""
import sys, re, json, subprocess, urllib.parse, time, csv, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
SORTS = {"relevance": "EgIQAQ%3D%3D", "views": "CAMSAhAB", "year": "CAMSBAgFEAE%3D", "month": "CAMSBAgEEAE%3D"}

def get(u):
    return subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1", u], capture_output=True, text=True).stdout

def walk(o, acc, conts):
    if isinstance(o, dict):
        if "videoRenderer" in o:
            v = o["videoRenderer"]
            title = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
            runs = v.get("ownerText", {}).get("runs", [{}])
            be = runs[0].get("navigationEndpoint", {}).get("browseEndpoint", {}) if runs else {}
            acc.append({"id": v.get("videoId"), "title": title, "channel": runs[0].get("text") if runs else None,
                        "channelId": be.get("browseId"), "handle": be.get("canonicalBaseUrl"),
                        "views": v.get("viewCountText", {}).get("simpleText"),
                        "age": v.get("publishedTimeText", {}).get("simpleText"),
                        "length": v.get("lengthText", {}).get("simpleText")})
            return
        if "continuationCommand" in o:
            conts.append(o["continuationCommand"].get("token"))
        for x in o.values(): walk(x, acc, conts)
    elif isinstance(o, list):
        for x in o: walk(x, acc, conts)

def search(q, sp, pages):
    html = get("https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=" + sp + "&hl=en&gl=US")
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
    if not m: return None
    d = json.loads(m.group(1))
    cfg = re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html)
    ctx = json.loads(cfg.group(1)) if cfg else None
    acc, conts = [], []
    walk(d, acc, conts)
    for _ in range(pages - 1):
        if not conts or not ctx: break
        tok = conts[-1]; conts = []
        out = subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Content-Type: application/json",
                              "https://www.youtube.com/youtubei/v1/search?prettyPrint=false",
                              "-d", json.dumps({"context": ctx, "continuation": tok})], capture_output=True, text=True).stdout
        try: walk(json.loads(out), acc, conts)
        except Exception: break
    return acc

kwfile, out, mode = sys.argv[1], sys.argv[2], sys.argv[3]
shard, nshards = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (0, 1)
rows = [r for r in csv.DictReader(open(kwfile)) if (r["priority"].strip().lower() in ("yes", "priority", "1", "true")) == (mode == "priority")]
rows = rows[shard::nshards]
sorts = list(SORTS) if mode == "priority" else ["relevance"]
pages = 2 if mode == "priority" else 1
done = set()
if os.path.exists(out):
    for l in open(out):
        try: j = json.loads(l); done.add((j["keyword"], j["sort"]))
        except Exception: pass
fails = 0
with open(out, "a") as f:
    for r in rows:
        for s in sorts:
            if (r["keyword"], s) in done: continue
            try: res = search(r["keyword"], SORTS[s], pages)
            except Exception as e: res = None
            if res is None:
                fails += 1; print("FAIL", r["keyword"], s, file=sys.stderr)
                if fails > 20: sys.exit("too many failures; stopping (rate limit?)")
                time.sleep(10); continue
            fails = 0
            f.write(json.dumps({"keyword": r["keyword"], "topic": r["topic"], "framing": r["framing"], "sort": s,
                                "pulled": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "n": len(res), "rows": res}) + "\n")
            f.flush()
            time.sleep(0.6)
print("done", file=sys.stderr)
