"""Fetch a storyboard sprite (frames from inside the video) for the first search hit of a query.
Usage: python3 -I sb.py "exact title query" OUTFILE.jpg
"""
import json, re, sys, urllib.parse, urllib.request, ssl
sys.path.insert(0, "/tmp/claude-0/-home-user/d5acabeb-7481-55ab-bfba-e93a497d3593/scratchpad/water1tools")
from yt import get, initial, find, txt, UA, CTX

q, out = sys.argv[1], sys.argv[2]
d = initial(get("https://www.youtube.com/results?search_query=" + urllib.parse.quote(q)))
vr = find(d, "videoRenderer")[0]
vid = vr["videoId"]
print("VIDEO:", vid, "|", txt(vr.get("title")), "|", txt(vr.get("ownerText")))
html = get("https://www.youtube.com/watch?v=" + vid)
m = re.search(r'"playerStoryboardSpecRenderer":\{"spec":"([^"]+)"', html)
spec = m.group(1).replace("\\u0026", "&")
parts = spec.split("|")
base = parts[0]
# choose highest level
lvl = len(parts) - 2
fields = parts[-1].split("#")
sigh = fields[-1]
url = base.replace("$L", str(lvl)).replace("$N", fields[6] if len(fields) > 6 else "M$M").replace("$M", "1")
if "sigh=" not in url:
    url += ("&" if "?" in url else "?") + "sigh=" + sigh
req = urllib.request.Request(url, headers={"User-Agent": UA})
data = urllib.request.urlopen(req, context=CTX, timeout=40).read()
open(out, "wb").write(data)
print("saved", out, len(data))
