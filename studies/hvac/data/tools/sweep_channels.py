#!/usr/bin/env python3
"""Channel-finder sweep (2026-10-23). Runs YouTube video searches (logged out, hl=en gl=US)
for each query in the sorts in SORTS (view count sp=CAMSAhAB; view count within upload-date filters
"this year" sp=CAMSBAgFEAE%3D and "this month" sp=CAMSBAgEEAE%3D). The old "upload date" sort (CAISAhAB / CAI%3D)
was tested 2026-10-23 and does NOT work any more (returns relevance order), so the date filters replace it.
2 pages each, and writes every result row to a JSON file.
Usage: python3 -I sweep_channels.py queries.txt out.json"""
import sys, re, json, subprocess, urllib.parse, time

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
SORTS = {"views": "CAMSAhAB", "year": "CAMSBAgFEAE%3D", "month": "CAMSBAgEEAE%3D"}

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

def search(q, sp, pages=2):
    html = get("https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=" + sp + "&hl=en&gl=US")
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
    if not m: return []
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

qs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
res = []
for q in qs:
    for name, sp in SORTS.items():
        try: rows = search(q, sp)
        except Exception as e: rows = []; print("ERR", q, name, e, file=sys.stderr)
        for r in rows: r.update({"query": q, "sort": name})
        res.extend(rows)
        print(q, name, len(rows), file=sys.stderr)
        time.sleep(0.5)
json.dump({"pulled": "2026-10-23", "source": "youtube.com/results logged out hl=en gl=US", "rows": res},
          open(sys.argv[2], "w"), indent=0)
