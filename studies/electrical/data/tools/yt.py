#!/usr/bin/env python3
"""Logged-out YouTube page loads for the electrical study. One script so every helper pulls the same way.

Usage:
  yt.py channel <UCid|@handle> <latest|popular|oldest> [pages]   -> JSON: channel info + videos (id, title, views, dur, age)
  yt.py search  "<query>" <relevance|views|week|month|year|views_month|views_year|long|views_long> [pages] [video|channel]\n      (channel search: relevance only; "long" = over 20 minutes)
  yt.py video   <video_id>                                        -> JSON: title, channel, exact date, views, up-next list
  yt.py thumb   <video_id> <outdir>                               -> downloads hqdefault.jpg (falls back to mqdefault)
Views from list pages are rounded ("1.2M"); `video` gives the exact count and exact upload date.
Lengths come from list pages (the player page is blocked logged out)."""
import sys, re, json, subprocess, urllib.parse, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}

def get(url):
    return subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1", url], capture_output=True, text=True).stdout

def api(ep, body, ctx=None):
    body = dict(body); body["context"] = ctx or CTX
    out = subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, "-H", "Content-Type: application/json",
                          "-H", "Accept-Language: en-US,en;q=0.9",
                          f"https://www.youtube.com/youtubei/v1/{ep}?prettyPrint=false", "-d", json.dumps(body)],
                         capture_output=True, text=True).stdout
    return json.loads(out)

def initial(html):
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
    cfg = re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html)
    return json.loads(m.group(1)) if m else {}, (json.loads(cfg.group(1)) if cfg else CTX)

def num(s):
    if s is None: return None
    s = s.strip()
    if s.lower().startswith("no views"): return 0
    m = re.match(r'^([\d.,]+)\s*([KMB]?)(\s+views?)?$', s)
    if not m: return None
    return int(round(float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)]))

def lockups(o, acc):
    if isinstance(o, dict):
        if "lockupViewModel" in o:
            lv = o["lockupViewModel"]
            md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
            parts = [p.get("text", {}).get("content") for row in md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", [])
                     for p in row.get("metadataParts", []) if p.get("text", {}).get("content")]
            dur = None
            m = re.search(r'"text": "(\d+:\d+(?::\d+)?)"', json.dumps(lv.get("contentImage", {})))
            if m: dur = m.group(1)
            chid = re.search(r'"browseId": "(UC[\w-]{22})"', json.dumps(md))
            v = {"id": lv.get("contentId"), "type": lv.get("contentType"), "title": md.get("title", {}).get("content"), "dur": dur, "meta": parts,
                 "channel_id": chid.group(1) if chid else None}
            v["views"] = next((num(p) for p in parts if "ago" not in p and num(p) is not None), None)
            v["age"] = next((p for p in parts if "ago" in p or "Streamed" in p), None)
            acc.append(v); return
        if "videoRenderer" in o:
            r = o["videoRenderer"]
            chid = re.search(r'"browseId": "(UC[\w-]{22})"', json.dumps(r.get("ownerText", {})))
            vt = r.get("viewCountText", {}).get("simpleText") or "".join(x.get("text", "") for x in r.get("viewCountText", {}).get("runs", []))
            acc.append({"id": r.get("videoId"), "type": "VIDEO", "title": "".join(x.get("text", "") for x in r.get("title", {}).get("runs", [])),
                        "channel": "".join(x.get("text", "") for x in r.get("ownerText", {}).get("runs", [])),
                        "channel_id": chid.group(1) if chid else None, "views": num(vt.replace(",", "") if vt else None) if vt else None,
                        "views_text": vt, "age": r.get("publishedTimeText", {}).get("simpleText"), "dur": r.get("lengthText", {}).get("simpleText")})
            return
        if "channelRenderer" in o:
            c = o["channelRenderer"]
            acc.append({"type": "CHANNEL", "channel_id": c.get("channelId"), "title": c.get("title", {}).get("simpleText"),
                        "handle": c.get("subscriberCountText", {}).get("simpleText"),
                        "subs": c.get("videoCountText", {}).get("simpleText")})
            return
        if "videoWithContextRenderer" in o or "shortsLockupViewModel" in o or "reelItemRenderer" in o:
            return
        for v in o.values(): lockups(v, acc)
    elif isinstance(o, list):
        for x in o: lockups(x, acc)

def conts(o, out):
    if isinstance(o, dict):
        if "continuationCommand" in o: out.append(o["continuationCommand"].get("token"))
        for v in o.values(): conts(v, out)
    elif isinstance(o, list):
        for x in o: conts(x, out)

def grid_conts(o, out):
    """Tokens from continuationItemRenderer only (the video grid / results list), not the About panel's."""
    if isinstance(o, dict):
        if "continuationItemRenderer" in o:
            t = re.search(r'"token": "([^"]+)"', json.dumps(o["continuationItemRenderer"]))
            if t: out.append(t.group(1))
        for v in o.values(): grid_conts(v, out)
    elif isinstance(o, list):
        for x in o: grid_conts(x, out)

def dedupe(lst, key="id"):
    seen, res = set(), []
    for v in lst:
        k = v.get(key) or v.get("channel_id")
        if k in seen: continue
        seen.add(k); res.append(v)
    return res

def channel(key, sort, pages):
    base = f"https://www.youtube.com/channel/{key}" if key.startswith("UC") else f"https://www.youtube.com/{key}"
    d, ctx = initial(get(base + "/videos"))
    meta = d.get("metadata", {}).get("channelMetadataRenderer", {})
    hdr = json.dumps(d.get("header", {}))
    subs = re.search(r'"content": "([\d.,]+[KMB]? subscribers)"', hdr)
    nvid = re.search(r'"content": "([\d,.]+[KMB]? videos?)"', hdr)
    vids = []
    if sort == "latest":
        lockups(d, vids); r = d
    else:
        chip = {"popular": "Popular", "oldest": "Oldest"}[sort]
        m = re.search(r'"chipViewModel": \{"text": "%s".*?"continuationCommand": \{"token": "([^"]+)"' % chip, json.dumps(d))
        if not m:
            return {"error": f"no {chip} chip on Videos tab", "channel": meta.get("title"), "id": meta.get("externalId")}
        r = api("browse", {"continuation": m.group(1)}, ctx); lockups(r, vids)
    for _ in range(pages - 1):
        c = []; grid_conts(r, c)   # fixed 2026-10-23: the old code took the last token (a panel's), capping lists at 30; the grid's is the first
        if not c: break
        r = api("browse", {"continuation": c[0]}, ctx); lockups(r, vids)
    vids = [v for v in dedupe(vids) if v.get("type") in (None, "VIDEO", "LOCKUP_CONTENT_TYPE_VIDEO")]
    return {"channel": meta.get("title"), "id": meta.get("externalId"), "handle": meta.get("vanityChannelUrl"),
            "description": meta.get("description"), "subs": subs.group(1) if subs else None, "videos_count": nvid.group(1) if nvid else None,
            "sort": sort, "videos": vids}

# Search filters, checked 2026-10-23 on "outlet mistakes":
#   relevance works; views works roughly (biggest first, a few out of order);
#   "upload date" (CAISAhAB) NO LONGER SORTS BY DATE, so newest = the date windows below, which do filter correctly;
#   YouTube search has no "oldest" sort (use a channel's Oldest tab instead).
SP = {("video", "relevance"): "EgIQAQ%3D%3D", ("video", "views"): "CAMSAhAB",
      ("video", "week"): "EgQIAxAB", ("video", "month"): "EgQIBBAB", ("video", "year"): "EgQIBRAB",
      ("video", "views_month"): "CAMSBAgEEAE%3D", ("video", "views_year"): "CAMSBAgFEAE%3D",
      ("video", "long"): "EgQQARgC", ("video", "views_long"): "CAMSBBABGAI%3D",
      ("channel", "relevance"): "EgIQAg%3D%3D"}

def search(q, sort, pages, kind):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=" + SP[(kind, sort)] + "&hl=en&gl=US"
    d, ctx = initial(get(url)); acc = []; lockups(d, acc); r = d
    for _ in range(pages - 1):
        c = []; grid_conts(r, c)
        if not c: break
        r = api("search", {"continuation": c[-1]}, ctx); lockups(r, acc)
    return dedupe(acc)

def video(vid):
    r = api("next", {"videoId": vid}); t = json.dumps(r)
    def g(p):
        m = re.search(p, t); return m.group(1) if m else None
    pri = json.dumps(r.get("contents", {}).get("twoColumnWatchNextResults", {}).get("results", {}))
    title = re.search(r'"videoPrimaryInfoRenderer": \{"title": \{"runs": \[(.*?)\]', pri)
    title = "".join(re.findall(r'"text": "((?:[^"\\]|\\.)*)"', title.group(1))) if title else None
    owner = re.search(r'"videoOwnerRenderer": \{.*?"title": \{"runs": \[\{"text": "((?:[^"\\]|\\.)*)".*?"browseId": "(UC[\w-]{22})"', pri)
    views = g(r'"viewCount": \{"simpleText": "([\d,]+) views?"')
    sec = r.get("contents", {}).get("twoColumnWatchNextResults", {}).get("secondaryResults", {})
    upnext = []; lockups(sec, upnext)
    return {"id": vid, "title": json.loads('"%s"' % title) if title else None, "channel": owner.group(1) if owner else None,
            "channel_id": owner.group(2) if owner else None, "views": int(views.replace(",", "")) if views else None,
            "date": g(r'"dateText": \{"simpleText": "([^"]+)"'), "up_next": [v for v in dedupe(upnext) if v.get("id")]}

def thumb(vid, outdir):
    os.makedirs(outdir, exist_ok=True)
    for name in ("maxresdefault", "hqdefault", "mqdefault"):
        fn = os.path.join(outdir, f"{vid}.jpg")
        subprocess.run(["curl", "-sS", "-m", "30", "-o", fn, f"https://i.ytimg.com/vi/{vid}/{name}.jpg"])
        if os.path.exists(fn) and os.path.getsize(fn) > 2000: return fn
    return None

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "channel": out = channel(a[1], a[2], int(a[3]) if len(a) > 3 else 1)
    elif a[0] == "search": out = search(a[1], a[2], int(a[3]) if len(a) > 3 else 1, a[4] if len(a) > 4 else "video")
    elif a[0] == "video": out = video(a[1])
    elif a[0] == "thumb": out = thumb(a[1], a[2])
    print(json.dumps(out, indent=1, ensure_ascii=False))
