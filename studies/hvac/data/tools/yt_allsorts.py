#!/usr/bin/env python3
"""Page through ALL of a channel's Videos tab under each sort chip (Latest, Popular, Oldest).
Usage: python3 -I yt_allsorts.py <channel_id> <outfile.json> [max_pages]
Adapted from yt.py (2026-10-23). Writes {"channel","id","subs","videos","pulled","sorts":{"Latest":[...],"Popular":[...],"Oldest":[...]}}
Each item: id, title, meta (tab text parts e.g. '1.2M views', '3 years ago'), dur (tab overlay text), views_tab (parsed from rounded text)."""
import sys, re, json, subprocess, os, datetime

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url):
    return subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1", url], capture_output=True, text=True).stdout

def post(token, ctx):
    body = json.dumps({"context": ctx, "continuation": token})
    for _ in range(3):
        out = subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, "-H", "Content-Type: application/json",
                              "-H", "Accept-Language: en-US,en;q=0.9",
                              "https://www.youtube.com/youtubei/v1/browse?prettyPrint=false", "-d", body],
                             capture_output=True, text=True).stdout
        try:
            return json.loads(out)
        except Exception:
            continue
    return {}

def lockups(o, acc):
    if isinstance(o, dict):
        if "lockupViewModel" in o:
            lv = o["lockupViewModel"]
            md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
            parts = []
            for row in md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []):
                for p in row.get("metadataParts", []):
                    t = p.get("text", {}).get("content")
                    if t: parts.append(t)
            dur = None
            for m in re.finditer(r'"text": "(\d+:\d+(?::\d+)?)"', json.dumps(lv.get("contentImage", {}))):
                dur = m.group(1); break
            acc.append({"id": lv.get("contentId"), "title": md.get("title", {}).get("content"), "meta": parts, "dur": dur})
            return
        if "richItemRenderer" in o and "videoRenderer" in json.dumps(o)[:200]:
            pass
        if "videoRenderer" in o:
            vr = o["videoRenderer"]
            acc.append({"id": vr.get("videoId"), "title": "".join(r.get("text", "") for r in vr.get("title", {}).get("runs", [])),
                        "meta": [vr.get("viewCountText", {}).get("simpleText", ""), vr.get("publishedTimeText", {}).get("simpleText", "")],
                        "dur": vr.get("lengthText", {}).get("simpleText")})
            return
        for v in o.values(): lockups(v, acc)
    elif isinstance(o, list):
        for x in o: lockups(x, acc)

def find_cont(o, out):
    if isinstance(o, dict):
        if "continuationItemRenderer" in o:
            t = re.search(r'"token": "([^"]+)"', json.dumps(o["continuationItemRenderer"]))
            if t: out.append(t.group(1))
        for v in o.values(): find_cont(v, out)
    elif isinstance(o, list):
        for x in o: find_cont(x, out)

def views(meta):
    for p in meta:
        m = re.match(r'^([\d.,]+)\s*([KMB]?)(\s+views?)?$', p.strip())
        if m:
            n = float(m.group(1).replace(",", ""))
            return int(n * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])
        if p.startswith("No views"): return 0
    return None

def page_all(first, ctx, maxp):
    acc = []; lockups(first, acc); r = first; n = 1
    while n < maxp:
        c = []; find_cont(r, c)
        if not c: break
        r = post(c[-1], ctx); n += 1
        before = len(acc); lockups(r, acc)
        if len(acc) == before: break
    return acc, n

def main():
    key, outfile = sys.argv[1], sys.argv[2]
    maxp = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    base = f"https://www.youtube.com/channel/{key}"
    html = get(base + "/videos")
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
    d = json.loads(m.group(1))
    cfg = re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html)
    ctx = json.loads(cfg.group(1)) if cfg else {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}
    hdr = json.dumps(d.get("header", {}))
    meta = d.get("metadata", {}).get("channelMetadataRenderer", {})
    subs = re.search(r'"content": "([\d.,]+[KMB]? subscribers)"', hdr)
    nvid = re.search(r'"content": "([\d,]+ videos)"', hdr)
    txt = json.dumps(d)
    sorts = {}; pages = {}
    # Latest = default tab load
    sorts["Latest_initialpage"], pages["Latest_initialpage"] = page_all(d, ctx, maxp)
    for chip in ("Latest", "Popular", "Oldest"):
        pm = re.search(r'"chipViewModel": \{"text": "' + chip + r'".*?"continuationCommand": \{"token": "([^"]+)"', txt)
        if not pm:
            sorts[chip] = None; continue
        r = post(pm.group(1), ctx)
        sorts[chip], pages[chip] = page_all(r, ctx, maxp)
    for lst in sorts.values():
        for v in (lst or []): v["views_tab"] = views(v["meta"])
    res = {"key": key, "channel": meta.get("title"), "id": meta.get("externalId"), "subs": subs.group(1) if subs else None,
           "videos": nvid.group(1) if nvid else None, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "source": "YouTube channel Videos tab, logged-out curl + innertube /browse continuations",
           "pages": pages, "sorts": sorts}
    json.dump(res, open(outfile, "w"), indent=1)
    print(res["channel"], res["id"], res["subs"], res["videos"], {k: (len(v) if v is not None else None) for k, v in sorts.items()}, pages)

main()
