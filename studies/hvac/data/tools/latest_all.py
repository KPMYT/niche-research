#!/usr/bin/env python3
"""Page through a channel's Videos tab (newest first) and count uploads by age.
Usage: latest_all.py <channel_id> <out.json> [max_pages]
Counts use YouTube's rounded ages: <30 days = 'N days/weeks ago' (weeks <=4), <90 days adds '1 month'/'2 months ago'."""
import sys, re, json, subprocess
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url):
    return subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1; PREF=hl=en&gl=US", url], capture_output=True, text=True).stdout

def post(token, ctx):
    body = json.dumps({"context": ctx, "continuation": token})
    return json.loads(subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Content-Type: application/json",
        "https://www.youtube.com/youtubei/v1/browse?prettyPrint=false", "-d", body], capture_output=True, text=True).stdout)

def lockups(o, acc):
    if isinstance(o, dict):
        if "lockupViewModel" in o:
            lv = o["lockupViewModel"]; md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
            parts = [p.get("text", {}).get("content") for row in md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []) for p in row.get("metadataParts", [])]
            dur = re.search(r'"text": "(\d+:\d+(?::\d+)?)"', json.dumps(lv.get("contentImage", {})))
            acc.append({"id": lv.get("contentId"), "title": md.get("title", {}).get("content"), "meta": [p for p in parts if p], "dur": dur.group(1) if dur else None}); return
        for v in o.values(): lockups(v, acc)
    elif isinstance(o, list):
        for x in o: lockups(x, acc)

def conts(o, out):
    if isinstance(o, dict):
        if "continuationItemRenderer" in o:
            t = re.search(r'"token": "([^"]+)"', json.dumps(o["continuationItemRenderer"]))
            if t: out.append(t.group(1))
        for v in o.values(): conts(v, out)
    elif isinstance(o, list):
        for x in o: conts(x, out)

def age_days(meta):
    for p in meta:
        m = re.match(r'^(\d+)\s*(s|sec|second|min|minute|h|hr|hour|d|day|w|wk|week|mo|month|y|yr|year)s? ago$', p.strip())
        if m:
            n = int(m.group(1)); u = m.group(2)
            u = {"s": "second", "sec": "second", "min": "minute", "h": "hour", "hr": "hour", "d": "day", "w": "week", "wk": "week", "mo": "month", "y": "year", "yr": "year"}.get(u, u)
            return {"second": 0, "minute": 0, "hour": 0, "day": n, "week": 7 * n, "month": 30 * n, "year": 365 * n}[u]
    return None

def secs(d):
    if not d: return None
    s = 0
    for x in d.split(":"): s = s * 60 + int(x)
    return s

cid, out = sys.argv[1], sys.argv[2]; maxp = int(sys.argv[3]) if len(sys.argv) > 3 else 15
html = get(f"https://www.youtube.com/channel/{cid}/videos")
d = json.loads(re.search(r'var ytInitialData = (\{.*?\});</script>', html).group(1))
cfg = re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html)
ctx = json.loads(cfg.group(1)) if cfg else {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}
vids = []; lockups(d, vids); r = d
for _ in range(maxp):
    c = []; conts(r, c)
    if not c: break
    n0 = len(vids); r = post(c[0], ctx); lockups(r, vids)
    if len(vids) == n0: break
for v in vids: v["age_days_floor"] = age_days(v["meta"]); v["secs"] = secs(v["dur"])
def cnt(limit):
    return sum(1 for v in vids if v["age_days_floor"] is not None and v["age_days_floor"] < limit and not (limit == 30 and v["age_days_floor"] >= 30))
res = {"channel_id": cid, "pulled": "2026-10-23", "n_listed": len(vids), "last30": cnt(30), "last90": cnt(90),
       "long_ge_300s": sum(1 for v in vids if (v["secs"] or 0) >= 300), "under_300s": sum(1 for v in vids if v["secs"] is not None and v["secs"] < 300), "videos": vids}
json.dump(res, open(out, "w"), indent=1)
print(cid, "listed", len(vids), "last30", res["last30"], "last90", res["last90"], "long>=300s", res["long_ge_300s"], "under300s", res["under_300s"])
