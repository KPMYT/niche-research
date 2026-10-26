"""Small YouTube scraper (fallback while NexLev is rate-limited).
Usage:
  python3 -I yt.py chsearch "query"            -> channels: id | title | handle | subs
  python3 -I yt.py vsearch "query" [sp]        -> videos: views | age | title | channel | channelId
  python3 -I yt.py about CHANNEL_ID            -> joined, total views, subs, video count, country, desc head
  python3 -I yt.py popular CHANNEL_ID [n]      -> top videos by views (title | views | age)
  python3 -I yt.py latest CHANNEL_ID [n]       -> newest videos
"""
import json, re, sys, urllib.request, urllib.parse, ssl

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9",
                                               "Cookie": "CONSENT=YES+1; PREF=hl=en&gl=US"})
    return urllib.request.urlopen(req, context=CTX, timeout=40).read().decode("utf-8", "replace")


def post(endpoint, body, key, client_version):
    body = dict(body)
    body["context"] = {"client": {"clientName": "WEB", "clientVersion": client_version, "hl": "en", "gl": "US"}}
    req = urllib.request.Request(f"https://www.youtube.com/youtubei/v1/{endpoint}?key={key}&prettyPrint=false",
                                 data=json.dumps(body).encode(),
                                 headers={"User-Agent": UA, "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, context=CTX, timeout=40).read())


def initial(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        m = re.search(r'window\["ytInitialData"\] = (\{.*?\});', html, re.S)
    return json.loads(m.group(1))


def cfg(html):
    key = re.search(r'"INNERTUBE_API_KEY":"([^"]+)"', html).group(1)
    ver = re.search(r'"INNERTUBE_CLIENT_VERSION":"([^"]+)"', html).group(1)
    return key, ver


def find(o, k, out=None):
    if out is None:
        out = []
    if isinstance(o, dict):
        if k in o:
            out.append(o[k])
        for v in o.values():
            find(v, k, out)
    elif isinstance(o, list):
        for v in o:
            find(v, k, out)
    return out


def txt(x):
    if not x:
        return ""
    if isinstance(x, str):
        return x
    if "simpleText" in x:
        return x["simpleText"]
    if "runs" in x:
        return "".join(r.get("text", "") for r in x["runs"])
    if "content" in x:
        return x["content"]
    return ""


def chsearch(q):
    d = initial(get("https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=EgIQAg%253D%253D"))
    for c in find(d, "channelRenderer"):
        subs = txt(c.get("videoCountText"))
        handle = txt(c.get("subscriberCountText"))
        print(f'{c["channelId"]} | {txt(c.get("title"))} | {handle} | {subs}')


def vsearch(q, sp=""):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q)
    if sp:
        url += "&sp=" + sp
    d = initial(get(url))
    for v in find(d, "videoRenderer"):
        ch = v.get("ownerText", {}).get("runs", [{}])[0]
        cid = ch.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId", "")
        print(f'{txt(v.get("viewCountText"))} | {txt(v.get("publishedTimeText"))} | {txt(v.get("lengthText"))} | {txt(v.get("title"))} | {ch.get("text","")} | {cid}')


def lockups(d):
    rows = []
    for v in find(d, "richItemRenderer"):
        c = v.get("content", {})
        vr = c.get("videoRenderer")
        if vr:
            rows.append((txt(vr.get("title")), txt(vr.get("viewCountText")), txt(vr.get("publishedTimeText")), txt(vr.get("lengthText"))))
            continue
        lv = c.get("lockupViewModel")
        if lv:
            md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
            title = md.get("title", {}).get("content", "")
            parts = []
            for r in find(md, "metadataParts"):
                for p in r:
                    parts.append(p.get("text", {}).get("content", ""))
            rows.append((title, " / ".join(parts), "", ""))
    return rows


def videos(cid, sort, n=10):
    html = get(f"https://www.youtube.com/channel/{cid}/videos")
    d = initial(html)
    title = find(d, "channelMetadataRenderer")
    print("CHANNEL:", title[0].get("title") if title else cid)
    if sort == "popular":
        key, ver = cfg(html)
        tok = None
        for chip in find(d, "chipViewModel"):
            if chip.get("text", "").lower() == "popular":
                tok = find(chip, "continuationCommand")
                tok = tok[0]["token"] if tok else None
        if not tok:
            for chip in find(d, "chipCloudChipRenderer"):
                if txt(chip.get("text")).lower() == "popular":
                    t = find(chip, "continuationCommand")
                    tok = t[0]["token"] if t else None
        if not tok:
            print("(no popular chip; showing latest)")
        else:
            d = post("browse", {"continuation": tok}, key, ver)
    for r in lockups(d)[:n]:
        print(" | ".join(x for x in r if x))


def about(cid):
    html = get(f"https://www.youtube.com/channel/{cid}")
    d = initial(html)
    key, ver = cfg(html)
    md = find(d, "channelMetadataRenderer")
    if md:
        print("TITLE:", md[0].get("title"), "|", md[0].get("vanityChannelUrl", ""))
        print("DESC:", (md[0].get("description") or "")[:400].replace("\n", " "))
    tok = None
    for c in find(d, "continuationCommand"):
        t = c.get("token", "")
        tok = t  # take last; about panel token usually appears in header
    toks = [c.get("token") for c in find(d, "continuationCommand")]
    for t in toks:
        try:
            r = post("browse", {"continuation": t}, key, ver)
        except Exception:
            continue
        a = find(r, "aboutChannelViewModel")
        if a:
            a = a[0]
            for k in ("subscriberCountText", "viewCountText", "videoCountText", "joinedDateText", "country"):
                v = a.get(k)
                if isinstance(v, dict):
                    v = v.get("content", txt(v))
                print(f"{k}: {v}")
            return
    print("(about panel not found)")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "chsearch":
        chsearch(sys.argv[2])
    elif cmd == "vsearch":
        vsearch(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
    elif cmd == "about":
        about(sys.argv[2])
    elif cmd == "popular":
        videos(sys.argv[2], "popular", int(sys.argv[3]) if len(sys.argv) > 3 else 5)
    elif cmd == "latest":
        videos(sys.argv[2], "latest", int(sys.argv[3]) if len(sys.argv) > 3 else 5)
