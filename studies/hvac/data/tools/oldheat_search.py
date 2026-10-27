#!/usr/bin/env python3
"""Old-house heat pool vs AC pool searches (round 2 helper, 2026-10-24).
Copies search() from sweep_round2.py (logged-out YouTube search, hl=en gl=US, 2 pages per search).
Sorts: relevance, views, year, month (sp codes as in sweep_round2.py).
Usage: python3 -I oldheat_search.py OUT.jsonl side:keyword [side:keyword ...]
Resumable: skips (keyword, sort) pairs already in OUT.jsonl. Paces ~1 s between requests."""
import sys, re, json, subprocess, urllib.parse, time, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
SORTS = {"relevance": "EgIQAQ%3D%3D", "views": "CAMSAhAB", "year": "CAMSBAgFEAE%3D", "month": "CAMSBAgEEAE%3D"}

def get(u):
    return subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
                           "-b", "CONSENT=YES+1", u], capture_output=True, text=True).stdout

def walk(o, acc, conts):
    if isinstance(o, dict):
        if "videoRenderer" in o:
            v = o["videoRenderer"]
            title = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
            runs = v.get("ownerText", {}).get("runs", [{}])
            be = runs[0].get("navigationEndpoint", {}).get("browseEndpoint", {}) if runs else {}
            acc.append({"id": v.get("videoId"), "title": title, "channel": runs[0].get("text") if runs else None,
                        "channelId": be.get("browseId"), "handle": be.get("canonicalBaseUrl"),
                        "views": v.get("viewCountText", {}).get("simpleText"),
                        "age": v.get("publishedTimeText", {}).get("simpleText"),
                        "length": v.get("lengthText", {}).get("simpleText")})
            return
        if "continuationCommand" in o:
            conts.append(o["continuationCommand"].get("token"))
        for x in o.values(): walk(x, acc, conts)
    elif isinstance(o, list):
        for x in o: walk(x, acc, conts)

def search(q, sp, pages):
    html = get("https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=" + sp + "&hl=en&gl=US")
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
    if not m: return None
    d = json.loads(m.group(1))
    cfg = re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html)
    ctx = json.loads(cfg.group(1)) if cfg else None
    acc, conts = [], []
    walk(d, acc, conts)
    for _ in range(pages - 1):
        if not conts or not ctx: break
        time.sleep(1)
        tok = conts[-1]; conts = []
        out = subprocess.run(["curl", "-sS", "-m", "30", "-A", UA, "-H", "Content-Type: application/json",
                              "https://www.youtube.com/youtubei/v1/search?prettyPrint=false",
                              "-d", json.dumps({"context": ctx, "continuation": tok})], capture_output=True, text=True).stdout
        try: walk(json.loads(out), acc, conts)
        except Exception: break
    return acc

if __name__ == "__main__":
    out = sys.argv[1]; items = [a.split(":", 1) for a in sys.argv[2:]]
    done = set()
    if os.path.exists(out):
        for l in open(out):
            try: j = json.loads(l); done.add((j["keyword"], j["sort"]))
            except Exception: pass
    fails = 0
    with open(out, "a") as f:
        for side, kw in items:
            for s in SORTS:
                if (kw, s) in done: continue
                try: res = search(kw, SORTS[s], 2)
                except Exception: res = None
                if res is None:
                    fails += 1; print("FAIL", kw, s, file=sys.stderr, flush=True)
                    if fails > 15: sys.exit("too many failures")
                    time.sleep(10); continue
                fails = 0
                f.write(json.dumps({"side": side, "keyword": kw, "sort": s, "pulled": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                    "n": len(res), "rows": res}) + "\n"); f.flush()
                print(side, kw, s, len(res), file=sys.stderr, flush=True)
                time.sleep(1)
