#!/usr/bin/env python3
"""Round 2 master channel list, step 2: YouTube About panels for channels no source gave subs / joined / video count.

Same method as yt_water1.py about (logged out, hl=en, gl=US), but returns a dict and saves it with a UTC
timestamp. Pace: about 1 s between channels. Resumable.

Usage: python3 -I master_about.py IDS.txt OUT.json
"""
import json, os, sys, time, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import yt_water1 as yt  # noqa: E402


def about(cid):
    html = yt.get(f"https://www.youtube.com/channel/{cid}")
    d = yt.initial(html)
    key, ver = yt.cfg(html)
    a = {}
    md = yt.find(d, "channelMetadataRenderer")
    if md:
        a["TITLE"] = f'{md[0].get("title")} | {md[0].get("vanityChannelUrl", "")}'
        a["DESC"] = (md[0].get("description") or "")[:400].replace("\n", " ")
    for t in [c.get("token") for c in yt.find(d, "continuationCommand")]:
        try:
            r = yt.post("browse", {"continuation": t}, key, ver)
        except Exception:
            continue
        av = yt.find(r, "aboutChannelViewModel")
        if av:
            av = av[0]
            for k in ("subscriberCountText", "viewCountText", "videoCountText", "joinedDateText", "country"):
                v = av.get(k)
                if isinstance(v, dict):
                    v = v.get("content", yt.txt(v))
                a[k] = v
            return a
    a["note"] = "about panel not found"
    return a


ids = [l.strip() for l in open(sys.argv[1]) if l.strip().startswith("UC")]
out = sys.argv[2]
res = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
for i, cid in enumerate(ids):
    if cid in res and "error" not in res[cid]:
        continue
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        a = about(cid)
    except Exception as e:
        a = {"error": str(e)[:200]}
    a["pulled"] = now
    res[cid] = a
    if i % 10 == 0 or i == len(ids) - 1:
        json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(i, cid, a.get("TITLE", a.get("error", "?"))[:60], a.get("subscriberCountText"), flush=True)
    time.sleep(1)
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done", len(res))
