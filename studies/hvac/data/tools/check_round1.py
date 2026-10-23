#!/usr/bin/env python3
"""Checker tool for HVAC round 1 (written 2026-10-23 by the checker, independent of the helpers' scripts).
Usage:
  python3 -I check_round1.py tab <channel_id> <out.json> [Latest|Popular|Oldest]  # every item on the Videos tab under that sort chip, all pages
  python3 -I check_round1.py shorts <channel_id>              # count of items on the Shorts tab (first pages)
  python3 -I check_round1.py next <out.jsonl> <id> [<id>...]  # exact title, views, date, owner, channel id via innertube /next
  python3 -I check_round1.py upnext <id> <pages>              # up-next list: id | channel | channelId
  python3 -I check_round1.py about <channel_id>               # about panel: subs, joined, videos, views, handle, title
  python3 -I check_round1.py resolve <@handle>                # channel id + title for a handle
  python3 -I check_round1.py ac "<query>"                     # YouTube autocomplete suggestions
Logged out, hl=en gl=US. Uses curl (honours the agent proxy)."""
import sys, re, json, subprocess, datetime, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}


def curl(args):
    return subprocess.run(["curl", "-sS", "-m", "45", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1; PREF=hl=en&gl=US"] + args, capture_output=True, text=True).stdout


def page(url):
    html = curl([url])
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    return json.loads(m.group(1)) if m else {}, html


def api(endpoint, body):
    body = dict(body); body["context"] = CTX
    for _ in range(3):
        out = curl(["-H", "Content-Type: application/json", "-d", json.dumps(body),
                    f"https://www.youtube.com/youtubei/v1/{endpoint}?prettyPrint=false"])
        try:
            return json.loads(out)
        except Exception:
            continue
    return {}


def walk(o, key, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                acc.append(v)
            walk(v, key, acc)
    elif isinstance(o, list):
        for x in o:
            walk(x, key, acc)
    return acc


def text(x):
    if not x: return None
    if "simpleText" in x: return x["simpleText"]
    if "runs" in x: return "".join(r.get("text", "") for r in x["runs"])
    if "content" in x: return x["content"]
    return None


def tab_items(data):
    items = []
    for vr in walk(data, "videoRenderer", []):
        items.append({"id": vr.get("videoId"), "title": text(vr.get("title")), "views_text": text(vr.get("viewCountText")),
                      "age": text(vr.get("publishedTimeText")), "dur": text(vr.get("lengthText"))})
    for lv in walk(data, "lockupViewModel", []):
        md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
        parts = [p.get("text", {}).get("content") for r in md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []) for p in r.get("metadataParts", [])]
        durs = re.findall(r'"text": "(\d+:\d\d(?::\d\d)?)"', json.dumps(lv.get("contentImage", {})))
        items.append({"id": lv.get("contentId"), "title": md.get("title", {}).get("content"), "meta": parts, "dur": durs[0] if durs else None})
    return items


def conts(data):
    toks = []
    for c in walk(data, "continuationItemRenderer", []):
        t = walk(c, "token", [])
        if t: toks.append(t[0])
    return toks


def cmd_tab(cid, out, sort="Latest"):
    """Load the Videos tab, click the sort chip (Latest / Popular / Oldest), then follow the grid's continuation."""
    data, _ = page(f"https://www.youtube.com/channel/{cid}/videos")
    chip = [c for c in walk(data, "chipViewModel", []) if c.get("text") == sort]
    r = api("browse", {"continuation": walk(chip[0], "token", [])[0]}) if chip else data
    items = tab_items(r); pages = 1
    while True:
        toks = [t for t in conts(r)]
        if not toks: break
        got = False
        for t in toks:
            r2 = api("browse", {"continuation": t})
            new = tab_items(r2)
            if new:
                items += new; r = r2; pages += 1; got = True; break
        if not got: break
    seen = set(); uniq = []
    for i in items:
        if i["id"] and i["id"] not in seen:
            seen.add(i["id"]); uniq.append(i)
    json.dump({"channel_id": cid, "sort": sort, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(), "pages": pages,
               "n": len(uniq), "items": uniq}, open(out, "w"), indent=1)
    print("sort", sort, "pages", pages, "items", len(items), "unique", len(uniq))


def cmd_shorts(cid):
    data, _ = page(f"https://www.youtube.com/channel/{cid}/shorts")
    ids = set(re.findall(r'"videoId": "([\w-]{11})"', json.dumps(data)))
    toks = conts(data); n = 1
    while toks and n < 20:
        r = api("browse", {"continuation": toks[-1]}); n += 1
        ids |= set(re.findall(r'"videoId": "([\w-]{11})"', json.dumps(r))); toks = conts(r)
    print("shorts ids", len(ids), sorted(ids)[:20])


def nxt(vid):
    r = api("next", {"videoId": vid})
    rec = {"id": vid, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(), "source": "innertube /next"}
    pi = walk(r, "videoPrimaryInfoRenderer", [])
    si = walk(r, "videoSecondaryInfoRenderer", [])
    if pi:
        rec["title"] = text(pi[0].get("title"))
        vc = walk(pi[0], "videoViewCountRenderer", [])
        rec["views_text"] = text(vc[0].get("viewCount")) if vc else None
        rec["date_text"] = text(pi[0].get("dateText"))
    if si:
        orr = walk(si[0], "videoOwnerRenderer", [])
        if orr:
            rec["owner"] = text(orr[0].get("title"))
            be = walk(orr[0], "browseId", [])
            rec["owner_id"] = be[0] if be else None
            rec["owner_subs"] = text(orr[0].get("subscriberCountText"))
    m = re.match(r"^([\d,]+) views?$", rec.get("views_text") or "")
    rec["views"] = int(m.group(1).replace(",", "")) if m else None
    dm = re.search(r"([A-Z][a-z]{2} \d{1,2}, \d{4})", rec.get("date_text") or "")
    rec["date"] = datetime.datetime.strptime(dm.group(1), "%b %d, %Y").date().isoformat() if dm else None
    return rec, r


def cmd_next(out, ids):
    with open(out, "a") as f:
        for v in ids:
            rec, _ = nxt(v)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(f"{v} | {rec.get('title')} | {rec.get('owner')} {rec.get('owner_id')} | {rec.get('views')} | {rec.get('date')}")


def upnext_items(r):
    res = []
    for lv in walk(r, "lockupViewModel", []):
        if lv.get("contentType") not in (None, "LOCKUP_CONTENT_TYPE_VIDEO"): continue
        md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
        js = json.dumps(md)
        ch = re.findall(r'"browseId": "(UC[\w-]{22})"', json.dumps(lv))
        parts = [p.get("text", {}).get("content") for r_ in md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []) for p in r_.get("metadataParts", [])]
        res.append({"id": lv.get("contentId"), "title": md.get("title", {}).get("content"), "channel": parts[0] if parts else None,
                    "channel_id": ch[0] if ch else None, "meta": parts})
    for cv in walk(r, "compactVideoRenderer", []):
        res.append({"id": cv.get("videoId"), "title": text(cv.get("title")), "channel": text(cv.get("longBylineText")),
                    "channel_id": (walk(cv.get("longBylineText", {}), "browseId", []) or [None])[0]})
    return res


def cmd_upnext(vid, pages):
    rec, r = nxt(vid)
    sr = walk(r, "secondaryResults", [])
    items = upnext_items(sr); toks = []
    for c in walk(sr, "continuationItemRenderer", []):
        t = walk(c, "token", [])
        if t: toks.append(t[0])
    for _ in range(int(pages) - 1):
        if not toks: break
        r2 = api("next", {"continuation": toks[0]})
        items += upnext_items(r2)
        toks = [walk(c, "token", [])[0] for c in walk(r2, "continuationItemRenderer", []) if walk(c, "token", [])]
        toks = toks[:1]
    print(json.dumps({"seed": vid, "pulled": rec["pulled"], "n": len(items), "items": items}, ensure_ascii=False))


def cmd_about(cid):
    data, html = page(f"https://www.youtube.com/channel/{cid}/about")
    title = (walk(data, "channelMetadataRenderer", [{}]) or [{}])[0].get("title")
    van = (walk(data, "channelMetadataRenderer", [{}]) or [{}])[0].get("vanityChannelUrl")
    a = walk(data, "aboutChannelViewModel", [])
    out = {"channel_id": cid, "title": title, "vanity": van, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    if not a:
        # about lives behind a continuation on newer layouts
        toks = re.findall(r'"token": "([^"]+)"', json.dumps(walk(data, "channelHeaderLinksViewModel", []) + walk(data, "descriptionPreviewViewModel", [])))
        for t in toks:
            r = api("browse", {"continuation": t})
            a = walk(r, "aboutChannelViewModel", [])
            if a: break
    if a:
        a = a[0]
        for k in ("subscriberCountText", "viewCountText", "videoCountText", "country", "canonicalChannelUrl"):
            out[k] = a.get(k)
        jd = a.get("joinedDateText")
        out["joined"] = jd.get("content") if isinstance(jd, dict) else jd
    print(json.dumps(out, ensure_ascii=False))


def cmd_resolve(handle):
    data, html = page(f"https://www.youtube.com/{handle}")
    md = (walk(data, "channelMetadataRenderer", [{}]) or [{}])[0]
    print(json.dumps({"handle": handle, "externalId": md.get("externalId"), "title": md.get("title"), "vanity": md.get("vanityChannelUrl")}, ensure_ascii=False))


def cmd_ac(q):
    url = "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=en&gl=us&q=" + urllib.parse.quote(q)
    out = curl([url])
    try:
        print(json.dumps({"q": q, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(), "suggestions": json.loads(out)[1]}, ensure_ascii=False))
    except Exception:
        print(json.dumps({"q": q, "error": out[:200]}))


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "tab": cmd_tab(sys.argv[2], sys.argv[3], *(sys.argv[4:5]))
    elif c == "shorts": cmd_shorts(sys.argv[2])
    elif c == "next": cmd_next(sys.argv[2], sys.argv[3:])
    elif c == "upnext": cmd_upnext(sys.argv[2], sys.argv[3])
    elif c == "about": cmd_about(sys.argv[2])
    elif c == "resolve": cmd_resolve(sys.argv[2])
    elif c == "ac": cmd_ac(sys.argv[2])
