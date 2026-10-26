#!/usr/bin/env python3
"""Exact pulls for the top-100 / recent-winners build (HVAC study, round 3), written 2026-10-26.

For each video ID: innertube /next (logged out; the /watch page and /player are blocked from the cloud) for the
EXACT view count, the exact upload date, the title, the owner channel ID / handle and the description (used only to
spot non-English videos, e.g. "in Hindi"); plus oEmbed for the ORIGINAL title (logged-out pages auto-translate).

Usage: python3 -I top_pull.py <ids.txt> <out.jsonl>     (appends; skips IDs already pulled without error)
"""
import sys, re, json, subprocess, datetime, os, urllib.parse
from concurrent.futures import ThreadPoolExecutor

CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}


def walk(o, key):
    if isinstance(o, dict):
        if key in o:
            yield o[key]
        for v in o.values():
            yield from walk(v, key)
    elif isinstance(o, list):
        for x in o:
            yield from walk(x, key)


def first(o, key):
    return next(walk(o, key), None)


def runs(x):
    if not x:
        return None
    if "simpleText" in x:
        return x["simpleText"]
    return "".join(r.get("text", "") for r in x.get("runs", []))


def curl(args):
    return subprocess.run(["curl", "-sS", "-m", "40"] + args, capture_output=True, text=True).stdout


def one(vid):
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rec = {"id": vid, "pulled": now, "source": "innertube /next videoId=" + vid + " (logged out, hl=en gl=US); oEmbed"}
    d = None
    for _ in range(3):
        out = curl(["-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
                    "https://www.youtube.com/youtubei/v1/next?prettyPrint=false",
                    "-d", json.dumps({"context": CTX, "videoId": vid})])
        try:
            d = json.loads(out)
            break
        except Exception:
            d = None
    if d is None:
        rec["error"] = "bad /next response"
        return rec
    pri = first(d, "videoPrimaryInfoRenderer") or {}
    sec = first(d, "videoSecondaryInfoRenderer") or {}
    rec["title_next"] = runs(pri.get("title"))
    vc = first(pri, "videoViewCountRenderer") or {}
    rec["views_text"] = runs(vc.get("viewCount"))
    rec["date_text"] = runs(pri.get("dateText"))
    own = first(sec, "videoOwnerRenderer") or {}
    rec["owner"] = runs(own.get("title"))
    be = first(own, "browseEndpoint") or {}
    rec["owner_channel_id"] = be.get("browseId")
    rec["owner_handle"] = (be.get("canonicalBaseUrl") or "").lstrip("/") or None
    desc = first(d, "attributedDescription") or {}
    rec["description_head"] = (desc.get("content") or "")[:600]
    v = re.match(r"^([\d,]+) views?$", rec["views_text"] or "")
    rec["views"] = int(v.group(1).replace(",", "")) if v else (0 if (rec["views_text"] or "").startswith("No views") else None)
    dm = re.search(r"([A-Z][a-z]{2} \d{1,2}, \d{4})", rec["date_text"] or "")
    rec["date"] = datetime.datetime.strptime(dm.group(1), "%b %d, %Y").date().isoformat() if dm else None
    rec["live_or_premiere_text"] = bool(re.search(r"Streamed|Premiered|live", rec["date_text"] or ""))
    if rec["views"] is None:
        rec["error"] = "no view count in /next (removed, private or age-gated?)"
    # oEmbed: original title
    o = curl(["-A", "Mozilla/5.0", "https://www.youtube.com/oembed?url=" +
              urllib.parse.quote("https://www.youtube.com/watch?v=" + vid, safe="") + "&format=json"])
    try:
        oj = json.loads(o)
        rec["title_original"] = oj.get("title")
        rec["oembed_author_url"] = oj.get("author_url")
    except Exception:
        rec["title_original"] = None
        rec["oembed_status"] = (o or "")[:40]
    return rec


def main():
    ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    out = sys.argv[2]
    done = set()
    if os.path.exists(out):
        for l in open(out):
            if l.strip():
                j = json.loads(l)
                if "error" not in j or j.get("error", "").startswith("no view count"):
                    done.add(j["id"])
    todo = [i for i in dict.fromkeys(ids) if i not in done]
    with open(out, "a") as f, ThreadPoolExecutor(8) as ex:
        for r in ex.map(one, todo):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            f.flush()
    print("fetched", len(todo), "; already had", len(done))


if __name__ == "__main__":
    main()
