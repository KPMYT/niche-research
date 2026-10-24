#!/usr/bin/env python3
"""Round 2 master channel list, step 1b: resolve handles and names to channel IDs (2026-10-24).

Handles (@x): load youtube.com/@x logged out and read channelMetadataRenderer.externalId.
Names: YouTube channel search (yt_water1.chsearch logic); accepted only when one result's title equals
the name exactly (case-insensitive). Anything else stays "not found". Paced about 1 s per request.

Usage: python3 -I master_resolve.py COLLECT.json   (adds to data/raw/channels-master-resolve-2026-10-24.json)
"""
import json, os, sys, time, urllib.parse, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import yt_water1 as yt  # noqa: E402

OUT = os.path.normpath(os.path.join(HERE, "..", "raw", "channels-master-resolve-2026-10-24.json"))
todo = json.load(open(sys.argv[1], encoding="utf-8"))["to_resolve"]
res = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
for key in todo:
    if key in res:
        continue
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = dict(pulled=now)
    try:
        if key.startswith("@"):
            d = yt.initial(yt.get("https://www.youtube.com/" + urllib.parse.quote(key)))
            md = yt.find(d, "channelMetadataRenderer")
            if md:
                r.update(channelId=md[0].get("externalId"), title=md[0].get("title"), how="YouTube @handle page, channelMetadataRenderer")
        else:
            d = yt.initial(yt.get("https://www.youtube.com/results?search_query=" + urllib.parse.quote(key) + "&sp=EgIQAg%253D%253D"))
            hits = [(c["channelId"], yt.txt(c.get("title")), yt.txt(c.get("subscriberCountText")), yt.txt(c.get("videoCountText")))
                    for c in yt.find(d, "channelRenderer")]
            r["candidates"] = hits[:8]
            exact = [h for h in hits if h[1].strip().lower() == key.strip().lower()]
            if len(exact) == 1:
                r.update(channelId=exact[0][0], title=exact[0][1], how="YouTube channel search, one exact-name match")
            elif len(exact) > 1:
                r["note"] = "several exact-name matches; not resolved"
    except Exception as e:
        r["error"] = str(e)[:200]
    res[key] = r
    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(key, "->", r.get("channelId"), r.get("title"), r.get("note", ""), flush=True)
    time.sleep(1)
