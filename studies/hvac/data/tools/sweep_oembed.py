#!/usr/bin/env python3
"""Original titles for the keyword-sweep videos (2026-10-24), from YouTube oEmbed.
Logged-out YouTube search auto-translates foreign titles into English (found by the old-house heat helper,
2026-10-24), so the English check in sweep_build.py is run on the ORIGINAL title that oEmbed returns
(https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<id>&format=json).
Reads raw/sweep-videos-2026-10-24.csv; biggest videos first (so every video that can appear in a table is done early).
Writes raw/sweep-oembed-2026-10-24.jsonl (id, orig_title, author, http error if any, pulled). Resumable.
Usage: python3 -I sweep_oembed.py [workers=4] [pause_s=0.25]"""
import csv, json, os, subprocess, sys, time, threading, queue
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(os.path.dirname(HERE), "raw")
OUT = os.path.join(RAW, "sweep-oembed-2026-10-24.jsonl")
workers = int(sys.argv[1]) if len(sys.argv) > 1 else 4
pause = float(sys.argv[2]) if len(sys.argv) > 2 else 0.25
done = set()
if os.path.exists(OUT):
    for l in open(OUT):
        try:
            j = json.loads(l)
            if "orig_title" in j or j.get("http") in ("401", "403", "404"): done.add(j["id"])
        except Exception: pass
rows = sorted(csv.DictReader(open(os.path.join(RAW, "sweep-videos-2026-10-24.csv"))), key=lambda r: -int(r["views"]))
ids = [r["id"] for r in rows if r["id"] not in done]
print(len(ids), "to fetch", file=sys.stderr, flush=True)
q = queue.Queue()
for i in ids: q.put(i)
lock = threading.Lock(); f = open(OUT, "a"); fails = [0]
def work():
    while True:
        try: i = q.get_nowait()
        except queue.Empty: return
        r = subprocess.run(["curl", "-sS", "-m", "20", "-w", "\n%{http_code}", f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={i}&format=json"],
                           capture_output=True, text=True).stdout
        body, _, code = r.rpartition("\n")
        rec = {"id": i, "http": code}
        try:
            d = json.loads(body); rec.update({"orig_title": d.get("title"), "author": d.get("author_name")})
        except Exception:
            rec["error"] = body[:80]
        rec["pulled"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        with lock:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n"); f.flush()
            if code in ("429", "000") or (code.startswith("5")): fails[0] += 1
            else: fails[0] = 0
            if fails[0] > 30: print("too many failures; stopping", file=sys.stderr); os._exit(1)
        if code == "429": time.sleep(30)
        time.sleep(pause)
ts = [threading.Thread(target=work) for _ in range(workers)]
for t in ts: t.start()
for t in ts: t.join()
print("done", file=sys.stderr)
