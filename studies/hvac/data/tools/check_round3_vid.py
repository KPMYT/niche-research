#!/usr/bin/env python3
"""Round 3 checker (2026-10-26): exact views, date, owner (innertube /next) and length (innertube /player
videoDetails.lengthSeconds) for a list of video IDs. Usage: python3 -I check_round3_vid.py out.json id1 id2 ..."""
import sys, re, json, subprocess, datetime
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20241001.00.00", "hl": "en", "gl": "US"}}


def call(ep, body):
    body["context"] = CTX
    out = subprocess.run(["curl", "-sS", "-m", "30", "-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
                          f"https://www.youtube.com/youtubei/v1/{ep}?prettyPrint=false", "-d", json.dumps(body)],
                         capture_output=True, text=True).stdout
    try:
        return json.loads(out)
    except Exception:
        return {}


res = {}
for vid in sys.argv[2:]:
    r = call("next", {"videoId": vid}); t = json.dumps(r)
    g = lambda p: (re.search(p, t).group(1) if re.search(p, t) else None)
    p = call("player", {"videoId": vid}); vd = p.get("videoDetails", {})
    mf = p.get("microformat", {}).get("playerMicroformatRenderer", {})
    res[vid] = {"title": g(r'"videoPrimaryInfoRenderer": \{"title": \{"runs": \[\{"text": "([^"]+)"'),
                "views_text": g(r'"viewCount": \{"simpleText": "([^"]+)"'),
                "date_text": g(r'"dateText": \{"simpleText": "([^"]+)"'),
                "owner": g(r'"videoOwnerRenderer": .*?"title": \{"runs": \[\{"text": "([^"]+)"'),
                "player_status": p.get("playabilityStatus", {}).get("status"),
                "length_s": vd.get("lengthSeconds"), "player_views": vd.get("viewCount"),
                "author": vd.get("author"), "channel_id": vd.get("channelId"),
                "publish_date": mf.get("publishDate"), "upload_date": mf.get("uploadDate"),
                "default_audio_lang": None, "desc_head": (vd.get("shortDescription") or "")[:300],
                "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    print(vid, res[vid]["views_text"], res[vid]["date_text"], res[vid]["length_s"], res[vid]["author"], res[vid]["player_status"], flush=True)
json.dump(res, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
