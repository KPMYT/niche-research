#!/usr/bin/env python3
"""Fetch a channel's videos (latest page + popular pages) from YouTube directly.
Usage: yt.py <channel_id or @handle> <outdir> [popular_pages]
Writes <outdir>/<key>.json with {"channel":..., "subs":..., "latest":[...], "popular":[...]}"""
import sys, re, json, subprocess, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url):
    return subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1", url], capture_output=True, text=True).stdout

def post(token, ctx):
    body = json.dumps({"context": ctx, "continuation": token})
    out = subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Content-Type: application/json",
                          "-H", "Accept-Language: en-US,en;q=0.9",
                          "https://www.youtube.com/youtubei/v1/browse?prettyPrint=false", "-d", body],
                         capture_output=True, text=True).stdout
    return json.loads(out)

def lockups(o, acc):
    if isinstance(o, dict):
        if "lockupViewModel" in o:
            lv = o["lockupViewModel"]
            vid = lv.get("contentId")
            md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
            title = md.get("title", {}).get("content")
            parts = []
            for row in md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []):
                for p in row.get("metadataParts", []):
                    t = p.get("text", {}).get("content")
                    if t: parts.append(t)
            dur = None
            for m in re.finditer(r'"text": "(\d+:\d+(?::\d+)?)"', json.dumps(lv.get("contentImage", {}))):
                dur = m.group(1); break
            acc.append({"id": vid, "title": title, "meta": parts, "dur": dur})
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

def main():
    key, outdir = sys.argv[1], sys.argv[2]
    pages = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    base = f"https://www.youtube.com/channel/{key}" if key.startswith("UC") else f"https://www.youtube.com/{key}"
    html = get(base + "/videos")
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
    d = json.loads(m.group(1))
    cfg = re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html)
    ctx = json.loads(cfg.group(1)) if cfg else {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}
    hdr = json.dumps(d.get("header", {}))
    meta = d.get("metadata", {}).get("channelMetadataRenderer", {})
    subs = re.search(r'"content": "([\d.,]+[KMB]? subscribers)"', hdr)
    nvid = re.search(r'"content": "([\d,]+ videos)"', hdr)
    latest = []; lockups(d, latest)
    txt = json.dumps(d)
    pop = []
    pm = re.search(r'"chipViewModel": \{"text": "Popular".*?"continuationCommand": \{"token": "([^"]+)"', txt)
    if pm:
        r = post(pm.group(1), ctx); lockups(r, pop)
        for _ in range(pages - 1):
            c = []; find_cont(r, c)
            if not c: break
            r = post(c[-1], ctx); lockups(r, pop)
    else:
        # no Popular chip (e.g. members-only tab): page through Latest instead
        pop = list(latest); r = d
        for _ in range(pages - 1):
            c = []; find_cont(r, c)
            if not c: break
            r = post(c[-1], ctx); lockups(r, pop)
    for lst in (latest, pop):
        for v in lst: v["views"] = views(v["meta"])
    res = {"key": key, "channel": meta.get("title"), "id": meta.get("externalId"), "subs": subs.group(1) if subs else None,
           "videos": nvid.group(1) if nvid else None, "latest": latest, "popular": pop}
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, (meta.get("externalId") or key.strip("@")) + ".json")
    json.dump(res, open(fn, "w"), indent=1)
    lv = [v["views"] for v in latest if v["views"] is not None]
    print(res["channel"], res["id"], res["subs"], res["videos"], "latest n=", len(lv),
          "avg=", int(sum(lv) / len(lv)) if lv else None, "median=", sorted(lv)[len(lv) // 2] if lv else None, "popular n=", len(pop), "->", fn)

main()
