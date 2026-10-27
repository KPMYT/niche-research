#!/usr/bin/env python3
"""Search within a channel. Usage: chsearch.py <channel_id> <query>"""
import sys, re, json, subprocess, urllib.parse
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
cid, q = sys.argv[1], sys.argv[2]
html = subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", "-b", "CONSENT=YES+1",
                       f"https://www.youtube.com/channel/{cid}/search?query=" + urllib.parse.quote(q)],
                      capture_output=True, text=True).stdout
d = json.loads(re.search(r'var ytInitialData = (\{.*?\});</script>', html).group(1))
out = []
def walk(o):
    if isinstance(o, dict):
        if "videoRenderer" in o:
            v = o["videoRenderer"]
            t = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
            out.append((v.get("videoId"), t, v.get("viewCountText", {}).get("simpleText"), v.get("publishedTimeText", {}).get("simpleText"), v.get("lengthText", {}).get("simpleText")))
            return
        for x in o.values(): walk(x)
    elif isinstance(o, list):
        for x in o: walk(x)
walk(d)
for r in out: print(" | ".join(str(x) for x in r))
