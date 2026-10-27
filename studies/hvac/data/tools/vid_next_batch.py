#!/usr/bin/env python3
"""Exact views + upload date for many videos via innertube /next (logged out). The watch page and /player
are blocked from the cloud (Google 'sorry' redirect / LOGIN_REQUIRED, tested 2026-10-23).
Usage: python3 -I vid_next_batch.py <ids.txt> <out.jsonl>   (skips ids already in out.jsonl)"""
import sys, re, json, subprocess, datetime, os
from concurrent.futures import ThreadPoolExecutor
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}

def one(vid):
    rec = {"id": vid, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(), "source": "innertube /next videoId=" + vid}
    for _ in range(3):
        out = subprocess.run(["curl", "-sS", "-m", "40", "-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
                              "https://www.youtube.com/youtubei/v1/next?prettyPrint=false",
                              "-d", json.dumps({"context": CTX, "videoId": vid})], capture_output=True, text=True).stdout
        try:
            t = json.dumps(json.loads(out)); break
        except Exception:
            t = None
    if not t:
        rec["error"] = "bad response"; return rec
    def g(p):
        m = re.search(p, t); return m.group(1) if m else None
    rec["title"] = g(r'"videoPrimaryInfoRenderer": \{"title": \{"runs": \[\{"text": "((?:[^"\\]|\\.)*)"')
    if rec["title"]: rec["title"] = json.loads('"' + rec["title"] + '"')
    rec["views_text"] = g(r'"videoViewCountRenderer": \{"viewCount": \{"simpleText": "([^"]+)"')
    rec["date_text"] = g(r'"dateText": \{"simpleText": "([^"]+)"')
    rec["owner"] = g(r'"videoOwnerRenderer": .*?"title": \{"runs": \[\{"text": "([^"]+)"')
    v = re.match(r'^([\d,]+) views?$', rec["views_text"] or "")
    rec["views"] = int(v.group(1).replace(",", "")) if v else (0 if (rec["views_text"] or "").startswith("No views") else None)
    dm = re.search(r'([A-Z][a-z]{2} \d{1,2}, \d{4})', rec["date_text"] or "")
    rec["date"] = datetime.datetime.strptime(dm.group(1), "%b %d, %Y").date().isoformat() if dm else None
    return rec

def main():
    ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    out = sys.argv[2]; done = set()
    if os.path.exists(out):
        done = {json.loads(l)["id"] for l in open(out) if l.strip() and "error" not in json.loads(l)}
    todo = [i for i in ids if i not in done]
    with open(out, "a") as f, ThreadPoolExecutor(6) as ex:
        for r in ex.map(one, todo):
            f.write(json.dumps(r) + "\n"); f.flush()
    print("done", len(todo), "fetched;", len(done), "already had")
main()
