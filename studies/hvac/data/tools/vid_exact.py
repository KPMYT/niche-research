#!/usr/bin/env python3
"""Exact video details from the watch page (ytInitialPlayerResponse + ytInitialData), logged-out curl.
Usage: python3 -I vid_exact.py <outfile.jsonl> <id> [<id> ...]   (or ids on stdin with '-')
Per video: id, title, channelId, viewCount (exact, videoDetails), lengthSeconds, publishDate, uploadDate,
isShortsEligible/isLiveContent flags, thumbnail URLs, viewCount text from primary info, error if any."""
import sys, re, json, subprocess, datetime
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url):
    return subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1", url], capture_output=True, text=True).stdout

def one(vid):
    rec = {"id": vid, "pulled": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "source": f"https://www.youtube.com/watch?v={vid} (ytInitialPlayerResponse)"}
    for attempt in range(3):
        html = get(f"https://www.youtube.com/watch?v={vid}&hl=en&gl=US")
        m = re.search(r'var ytInitialPlayerResponse = (\{.*?\});(?:var meta|</script>)', html)
        if m: break
    if not m:
        rec["error"] = "no player response"; return rec
    try:
        pr = json.loads(m.group(1))
    except Exception as e:
        rec["error"] = "json " + str(e); return rec
    vd = pr.get("videoDetails", {}); mf = pr.get("microformat", {}).get("playerMicroformatRenderer", {})
    rec.update({"title": vd.get("title"), "channelId": vd.get("channelId"), "author": vd.get("author"),
                "viewCount": int(vd["viewCount"]) if vd.get("viewCount", "").isdigit() else None,
                "lengthSeconds": int(vd["lengthSeconds"]) if vd.get("lengthSeconds", "").isdigit() else None,
                "isLiveContent": vd.get("isLiveContent"),
                "publishDate": mf.get("publishDate"), "uploadDate": mf.get("uploadDate"),
                "mf_viewCount": mf.get("viewCount"), "mf_lengthSeconds": mf.get("lengthSeconds"),
                "category": mf.get("category"), "playability": pr.get("playabilityStatus", {}).get("status"),
                "thumbs": [t.get("url") for t in vd.get("thumbnail", {}).get("thumbnails", [])][-2:]})
    return rec

def main():
    out = sys.argv[1]; ids = sys.argv[2:]
    if ids == ["-"]: ids = [l.strip() for l in sys.stdin if l.strip()]
    with open(out, "a") as f:
        for i, v in enumerate(ids):
            r = one(v); f.write(json.dumps(r) + "\n"); f.flush()
            print(i, v, r.get("viewCount"), r.get("lengthSeconds"), r.get("publishDate"), r.get("error", ""), (r.get("title") or "")[:50], flush=True)
main()
