import json, subprocess, sys, os, time
S = "/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/"
T = "/home/user/niche-research/studies/hvac/data/tools/yt_water1.py"
ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
shard, n = int(sys.argv[2]), int(sys.argv[3])
out = S + f"about-{shard}.jsonl"
done = set()
if os.path.exists(out):
    for l in open(out): done.add(json.loads(l)["channelId"])
with open(out, "a") as f:
    for cid in ids[shard::n]:
        if cid in done: continue
        try: r = subprocess.run(["python3", "-I", T, "about", cid], capture_output=True, text=True, timeout=90).stdout
        except Exception as e: r = "ERR " + str(e)
        a = {"channelId": cid, "pulled": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        for line in r.splitlines():
            if ":" in line:
                k, v = line.split(":", 1); a[k.strip()] = v.strip()
        f.write(json.dumps(a) + "\n"); f.flush()
        time.sleep(0.5)
