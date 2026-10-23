#!/usr/bin/env python3
"""Print a video's description links/text. Usage: desc.py <video_id> [chars]"""
import sys, re, json, subprocess
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}
vid = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 700
out = subprocess.run(["curl", "-sS", "-m", "30", "-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
                      "https://www.youtube.com/youtubei/v1/next?prettyPrint=false",
                      "-d", json.dumps({"context": CTX, "videoId": vid})], capture_output=True, text=True).stdout
r = json.loads(out)
def find(o):
    if isinstance(o, dict):
        if "videoSecondaryInfoRenderer" in o:
            return o["videoSecondaryInfoRenderer"].get("attributedDescription", {}).get("content", "")
        for v in o.values():
            x = find(v)
            if x is not None: return x
    elif isinstance(o, list):
        for v in o:
            x = find(v)
            if x is not None: return x
    return None
d = find(r) or ""
t = json.dumps(r)
title = re.search(r'"videoPrimaryInfoRenderer": \{"title": \{"runs": \[\{"text": "([^"]+)"', t)
print("==", vid, title.group(1) if title else "")
print(d[:n].replace("\n", " / "))
print("LINKS:", sorted(set(re.findall(r'(?:https?://)?(?:www\.)?([a-z0-9.-]+\.(?:com|net|org|to|co|io|shop|store|ly|us)\b[^\s]*)', d)))[:25])
