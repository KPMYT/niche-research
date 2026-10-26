#!/usr/bin/env python3
"""YouTube search. Usage: ytsearch.py <query> [channel|video] [pages] [sort:views]
Prints one line per result."""
import sys, re, json, subprocess, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
q = sys.argv[1]; kind = sys.argv[2] if len(sys.argv) > 2 else "video"
pages = int(sys.argv[3]) if len(sys.argv) > 3 else 1
sort = sys.argv[4] if len(sys.argv) > 4 else ""
sp = {"channel": "EgIQAg%3D%3D", "video": "EgIQAQ%3D%3D"}[kind]
if kind == "video" and sort == "views": sp = "CAMSAhAB"
url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=" + sp + "&hl=en&gl=US"

def get(u):
    return subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", "-b", "CONSENT=YES+1", u],
                          capture_output=True, text=True).stdout

def walk(o, acc, conts):
    if isinstance(o, dict):
        if "channelRenderer" in o:
            c = o["channelRenderer"]
            acc.append(("CH", c.get("channelId"), c.get("title", {}).get("simpleText"),
                        c.get("videoCountText", {}).get("simpleText") or json.dumps(c.get("videoCountText", {}))[:40],
                        c.get("subscriberCountText", {}).get("simpleText")))
            return
        if "videoRenderer" in o:
            v = o["videoRenderer"]
            title = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
            ch = "".join(r.get("text", "") for r in v.get("ownerText", {}).get("runs", []))
            chid = re.search(r'"browseId": "(UC[^"]+)"', json.dumps(v.get("ownerText", {})))
            acc.append(("V", v.get("videoId"), title, ch, chid.group(1) if chid else None,
                        v.get("viewCountText", {}).get("simpleText"), v.get("publishedTimeText", {}).get("simpleText"),
                        v.get("lengthText", {}).get("simpleText")))
            return
        if "continuationCommand" in o:
            conts.append(o["continuationCommand"].get("token"))
        for x in o.values(): walk(x, acc, conts)
    elif isinstance(o, list):
        for x in o: walk(x, acc, conts)

html = get(url)
m = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
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
    walk(json.loads(out), acc, conts)
seen = set()
for a in acc:
    if a[1] in seen: continue
    seen.add(a[1]); print(" | ".join(str(x) for x in a))
