#!/usr/bin/env python3
"""Up-next (suggested / 'watch next') list for YouTube videos via the innertube /next endpoint, logged out.
The /watch page and /player are blocked from the cloud (Google 'sorry' redirect / LOGIN_REQUIRED, 2026-10-23),
but POST /youtubei/v1/next works. Its secondaryResults hold the up-next list (lockupViewModel items in 2026;
compactVideoRenderer also handled), ending in a continuationItemRenderer whose token loads the next page.

Usage: python3 -I upnext.py <out.json> <pages> <video_id> [<video_id> ...]
       (pages = 1 for the first page only, 2 = first page + one continuation, ...)
Writes/updates out.json as {video_id: record}; ids already present without an error are skipped.
Requests are paced (PAUSE seconds between calls)."""
import sys, json, subprocess, datetime, os, re, time

CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}
URL = "https://www.youtube.com/youtubei/v1/next?prettyPrint=false"
PAUSE = 1.5


def post(body):
    body = dict(body, context=CTX)
    for attempt in range(3):
        out = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
                              URL, "-d", json.dumps(body)], capture_output=True, text=True).stdout
        try:
            return json.loads(out)
        except Exception:
            time.sleep(3 + attempt * 3)
    return None


def secs(t):
    if not t or not re.match(r'^\d+(:\d{2}){1,2}$', t):
        return None
    s = 0
    for p in t.split(":"):
        s = s * 60 + int(p)
    return s


def walk(o, key):
    """yield every value stored under `key` anywhere in o"""
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                yield v
            yield from walk(v, key)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v, key)


def parse_lockup(l):
    rec = {"id": l.get("contentId"), "type": l.get("contentType", "").replace("LOCKUP_CONTENT_TYPE_", "").lower()}
    md = l.get("metadata", {}).get("lockupMetadataViewModel", {})
    rec["title"] = md.get("title", {}).get("content")
    badges = [b.get("text") for b in walk(l.get("contentImage", {}), "thumbnailBadgeViewModel") if isinstance(b, dict)]
    rec["length_text"] = next((b for b in badges if b and secs(b) is not None), None)
    rec["badges"] = [b for b in badges if b and b != rec["length_text"]]
    rec["length_s"] = secs(rec["length_text"])
    be = next(walk(md.get("image", {}), "browseEndpoint"), None) or {}
    rec["channel_id"] = be.get("browseId")
    rec["handle"] = (be.get("canonicalBaseUrl") or "").lstrip("/") or None
    rows = md.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", [])
    parts = [[(p.get("text", {}) or {}).get("content") for p in r.get("metadataParts", [])] for r in rows]
    labels = [[p.get("accessibilityLabel") for p in r.get("metadataParts", [])] for r in rows]
    rec["channel"] = parts[0][0] if parts and parts[0] else None
    rec["views_text"] = rec["age_text"] = None
    for prow, lrow in zip(parts[1:], labels[1:]):
        for p, lab in zip(prow, lrow):
            if lab and "view" in lab:
                rec["views_text"] = p; rec["views_label"] = lab
            elif lab and "ago" in lab:
                rec["age_text"] = p
            elif p and "ago" in p:
                rec["age_text"] = p
            elif p and "view" in p.lower():
                rec["views_text"] = p
    return rec


def parse_compact(c):
    def tx(o):
        if not o: return None
        return o.get("simpleText") or "".join(r.get("text", "") for r in o.get("runs", []))
    be = next(walk(c.get("longBylineText", {}), "browseEndpoint"), None) or {}
    lt = tx(c.get("lengthText"))
    return {"id": c.get("videoId"), "type": "video", "title": tx(c.get("title")), "channel": tx(c.get("longBylineText")),
            "channel_id": be.get("browseId"), "handle": (be.get("canonicalBaseUrl") or "").lstrip("/") or None,
            "views_text": tx(c.get("viewCountText")), "age_text": tx(c.get("publishedTimeText")),
            "length_text": lt, "length_s": secs(lt)}


def items_of(results):
    out, tok = [], None
    for r in results or []:
        if "lockupViewModel" in r:
            out.append(parse_lockup(r["lockupViewModel"]))
        elif "compactVideoRenderer" in r:
            out.append(parse_compact(r["compactVideoRenderer"]))
        elif "continuationItemRenderer" in r:
            tok = next(walk(r, "token"), None)
        else:
            out.append({"type": "other:" + list(r.keys())[0]})
    return out, tok


def one(vid, pages):
    rec = {"seed": vid, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "source": "innertube POST /youtubei/v1/next videoId=%s (logged out, hl=en gl=US)" % vid, "items": []}
    d = post({"videoId": vid})
    if not d:
        rec["error"] = "bad response"; return rec
    t = json.dumps(d)
    m = re.search(r'"videoPrimaryInfoRenderer": \{"title": \{"runs": \[\{"text": "((?:[^"\\]|\\.)*)"', t)
    rec["seed_title"] = json.loads('"' + m.group(1) + '"') if m else None
    m = re.search(r'"videoOwnerRenderer": .*?"title": \{"runs": \[\{"text": "([^"]+)"', t)
    rec["seed_owner"] = m.group(1) if m else None
    try:
        res = d["contents"]["twoColumnWatchNextResults"]["secondaryResults"]["secondaryResults"]["results"]
    except KeyError:
        rec["error"] = "no secondaryResults"; return rec
    its, tok = items_of(res)
    for i in its: i["page"] = 1
    rec["items"] += its
    p = 1
    while tok and p < pages:
        time.sleep(PAUSE)
        d2 = post({"continuation": tok})
        p += 1
        if not d2:
            rec["cont_error"] = "bad response page %d" % p; break
        res2 = []
        for a in walk(d2, "appendContinuationItemsAction"):
            res2 += a.get("continuationItems", [])
        its, tok = items_of(res2)
        for i in its: i["page"] = p
        rec["items"] += its
    rec["pages_loaded"] = p
    rec["more_available"] = bool(tok)
    for n, i in enumerate(rec["items"], 1):
        i["pos"] = n
    return rec


def main():
    out, pages, ids = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
    data = json.load(open(out)) if os.path.exists(out) else {}
    for vid in ids:
        if vid in data and "error" not in data[vid]:
            continue
        data[vid] = one(vid, pages)
        r = data[vid]
        print(vid, r.get("error") or "%d items, %d pages" % (len(r["items"]), r.get("pages_loaded", 0)), flush=True)
        json.dump(data, open(out, "w"), indent=1, ensure_ascii=False)
        time.sleep(PAUSE)


if __name__ == "__main__":
    main()
