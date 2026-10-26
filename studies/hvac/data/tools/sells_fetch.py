#!/usr/bin/env python3
"""Round 3 'what it sells': pull the description of each tier A-D channel's newest long-form video
(dur >= 5:00, Latest sort) and its most popular long-form video (Popular sort) via innertube /next
(logged out; the /watch page is blocked from the cloud). Saves the full description text, every link
target (the q= of YouTube's redirect links, plus plain links in the text) and a few page markers.
Usage: python3 -I sells_fetch.py <master.csv> <census_dir> <out.jsonl> [workers]
Skips video ids already saved without error. Paced ~0.7 s per request per worker."""
import sys, os, re, json, csv, time, subprocess, datetime, urllib.parse
from concurrent.futures import ThreadPoolExecutor

CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}
MARKERS = ["sponsorButtonRenderer", "merchandiseShelfRenderer", "productListItemRenderer",
           "shoppingOverlay", "paidContentOverlay", "ticketShelfRenderer", "membershipOfferRenderer"]


def secs(d):
    try:
        p = [int(x) for x in (d or "").split(":")]
    except ValueError:
        return None
    s = 0
    for x in p:
        s = s * 60 + x
    return s


def pick(census):
    s = census.get("sorts", {})
    latest = s.get("Latest") or s.get("Latest_initialpage") or []
    popular = s.get("Popular") or []
    out = []
    lf = [v for v in latest if (secs(v.get("dur")) or 0) >= 300]
    if lf:
        out.append(("newest_longform", lf[0]))
    elif latest:
        out.append(("newest_any (no long-form in Latest)", latest[0]))
    pf = [v for v in popular if (secs(v.get("dur")) or 0) >= 300]
    if pf:
        out.append(("popular_longform", pf[0]))
    elif popular:
        out.append(("popular_any (no long-form in Popular)", popular[0]))
    return out


def find(o, key):
    if isinstance(o, dict):
        if key in o:
            return o[key]
        for v in o.values():
            x = find(v, key)
            if x is not None:
                return x
    elif isinstance(o, list):
        for v in o:
            x = find(v, key)
            if x is not None:
                return x
    return None


def fetch(job):
    cid, role, v = job
    vid = v["id"]
    rec = {"channel_id": cid, "role": role, "id": vid, "tab_title": v.get("title"), "dur": v.get("dur"),
           "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "source": "innertube /next videoId=" + vid}
    t = None
    for attempt in range(3):
        time.sleep(0.7)
        out = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
                              "https://www.youtube.com/youtubei/v1/next?prettyPrint=false",
                              "-d", json.dumps({"context": CTX, "videoId": vid})], capture_output=True, text=True).stdout
        try:
            r = json.loads(out)
            t = out
            break
        except Exception:
            time.sleep(2 + attempt * 3)
    if t is None:
        rec["error"] = "bad response"
        return rec
    sec = find(r, "videoSecondaryInfoRenderer") or {}
    ad = sec.get("attributedDescription") or {}
    desc = ad.get("content") or ""
    links = []
    for cr in ad.get("commandRuns") or []:
        ep = (((cr.get("onTap") or {}).get("innertubeCommand") or {}).get("urlEndpoint") or {}).get("url")
        if not ep:
            continue
        txt = desc[cr.get("startIndex", 0): cr.get("startIndex", 0) + cr.get("length", 0)]
        q = urllib.parse.parse_qs(urllib.parse.urlparse(ep).query).get("q")
        links.append({"text": txt, "url": q[0] if q else ep})
    rec["description"] = desc
    rec["links"] = links
    rec["markers"] = {m: t.count(m) for m in MARKERS if m in t}
    pri = find(r, "videoPrimaryInfoRenderer") or {}
    try:
        rec["title"] = "".join(x["text"] for x in pri["title"]["runs"])
    except Exception:
        rec["title"] = None
    own = find(r, "videoOwnerRenderer") or {}
    try:
        rec["owner"] = own["title"]["runs"][0]["text"]
        rec["owner_id"] = own["title"]["runs"][0]["navigationEndpoint"]["browseEndpoint"]["browseId"]
    except Exception:
        rec["owner"] = None
    if not desc and not rec["title"]:
        rec["error"] = "no description or title (video unavailable?)"
    return rec


def main():
    master, cdir, outp = sys.argv[1], sys.argv[2], sys.argv[3]
    workers = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    rows = [r for r in csv.DictReader(open(master)) if r["tier"] in ("A", "B", "C", "D")]
    done = set()
    if os.path.exists(outp):
        for l in open(outp):
            if l.strip():
                j = json.loads(l)
                if "error" not in j:
                    done.add((j["channel_id"], j["id"]))
    jobs = []
    for r in rows:
        cid = r["channel_id"]
        p = os.path.join(cdir, cid + ".json")
        if not os.path.exists(p):
            continue
        seen = set()
        for role, v in pick(json.load(open(p))):
            if v["id"] in seen:
                continue
            seen.add(v["id"])
            if (cid, v["id"]) not in done:
                jobs.append((cid, role, v))
    print(len(rows), "channels;", len(jobs), "videos to fetch;", len(done), "already had", flush=True)
    n = 0
    with open(outp, "a") as f, ThreadPoolExecutor(workers) as ex:
        for rec in ex.map(fetch, jobs):
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            n += 1
            if n % 100 == 0:
                print(n, "fetched", flush=True)
    print("done", n, flush=True)


main()
