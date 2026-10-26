#!/usr/bin/env python3
"""Video details (+ optional top comments) via innertube /next. Usage: vid.py <video_id> [n_comment_pages]"""
import sys, re, json, subprocess
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}
vid = sys.argv[1]; npages = int(sys.argv[2]) if len(sys.argv) > 2 else 0

def nxt(body):
    body["context"] = CTX
    out = subprocess.run(["curl", "-sS", "-m", "30", "-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
                          "https://www.youtube.com/youtubei/v1/next?prettyPrint=false", "-d", json.dumps(body)],
                         capture_output=True, text=True).stdout
    return json.loads(out)

r = nxt({"videoId": vid}); t = json.dumps(r)
def g(p):
    m = re.search(p, t); return m.group(1) if m else None
title = g(r'"videoPrimaryInfoRenderer": \{"title": \{"runs": \[\{"text": "([^"]+)"')
views = g(r'"viewCount": \{"simpleText": "([^"]+)"')
date = g(r'"dateText": \{"simpleText": "([^"]+)"')
owner = g(r'"videoOwnerRenderer": .*?"title": \{"runs": \[\{"text": "([^"]+)"')
ccount = g(r'"commentsEntryPointHeaderRenderer".*?"commentCount": \{"simpleText": "([^"]+)"')
print(f"{vid} | {title} | {owner} | {views} | {date} | comments {ccount}")
if npages:
    m = re.search(r'"sectionIdentifier": "comment-item-section".*?"token": "([^"]+)"', t)
    tok = m.group(1) if m else None
    got = 0
    for i in range(npages):
        if not tok: break
        r2 = nxt({"continuation": tok}); rt = json.dumps(r2)
        for mu in r2.get("frameworkUpdates", {}).get("entityBatchUpdate", {}).get("mutations", []):
            ce = mu.get("payload", {}).get("commentEntityPayload")
            if ce:
                pr_ = ce.get("properties", {}); a = ce.get("author", {}); tb = ce.get("toolbar", {})
                print(f"  [{tb.get('likeCountNotliked', '')} likes | {tb.get('replyCount', '')} rep] {a.get('displayName')}: {pr_.get('content', {}).get('content', '').replace(chr(10), ' ')[:450]}")
                got += 1
        conts = re.findall(r'"continuationItemRenderer": \{"trigger": "CONTINUATION_TRIGGER_ON_ITEM_SHOWN", "continuationEndpoint": .*?"token": "([^"]+)"', rt)
        tok = conts[-1] if conts else None
    print("comments fetched:", got)
