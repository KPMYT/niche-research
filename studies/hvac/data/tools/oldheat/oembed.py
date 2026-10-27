import json, subprocess, sys, time, os, re
S = "/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/"
side = sys.argv[1]
out = S + "oembed.jsonl"
done = set()
if os.path.exists(out):
    for l in open(out): done.add(json.loads(l)["id"])
def secs(t):
    if not t: return None
    s = 0
    for x in t.split(":"): s = s * 60 + int(x)
    return s
ids = []
for l in open(S + "search.jsonl"):
    j = json.loads(l)
    if j["side"] != side: continue
    for v in j["rows"]:
        s = secs(v["length"])
        if s and s >= 300 and v["id"] not in done and v["id"] not in ids: ids.append(v["id"])
print(len(ids), file=sys.stderr)
with open(out, "a") as f:
    for i in ids:
        r = subprocess.run(["curl", "-sS", "-m", "20", f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={i}&format=json"], capture_output=True, text=True).stdout
        try: d = json.loads(r); rec = {"id": i, "orig_title": d.get("title"), "author": d.get("author_name"), "thumb": d.get("thumbnail_url")}
        except Exception: rec = {"id": i, "error": r[:80]}
        rec["pulled"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        f.write(json.dumps(rec) + "\n"); f.flush()
        time.sleep(0.4)
