#!/usr/bin/env python3
"""Round 2 checker (2026-10-24): re-run stored PRIORITY keyword searches and compare with the stored results.
Loads search() from sweep_round2.py without running its main block.
Usage: python3 -I check_round2_search.py <priority.jsonl> <out.json> "keyword|sort" ..."""
import sys, json, os, re, time
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sweep_round2.py")
if not os.path.exists(SRC): SRC = "/home/user/niche-research/studies/hvac/data/tools/sweep_round2.py"
code = open(SRC).read().split("kwfile, out, mode")[0]
ns = {}; exec(compile(code, SRC, "exec"), ns)
def secs(t):
    if not t: return None
    p = [int(x) for x in t.split(":")]; s = 0
    for x in p: s = s * 60 + x
    return s
stored = {}
for l in open(sys.argv[1]):
    j = json.loads(l); stored[(j["keyword"], j["sort"])] = j
res = []
for arg in sys.argv[3:]:
    kw, sort = arg.split("|")
    new = ns["search"](kw, ns["SORTS"][sort], 2) or []
    old = stored[(kw, sort)]["rows"]
    def longids(rows): return [r["id"] for r in rows if (secs(r.get("length")) or 0) >= 300]
    o_all = [r["id"] for r in old]; n_all = [r["id"] for r in new]
    o_l = longids(old); n_l = longids(new)
    top = lambda L, k: set(L[:k])
    rec = {"keyword": kw, "sort": sort, "pulled": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "stored_pulled": stored[(kw, sort)]["pulled"], "stored_n": len(old), "new_n": len(new),
           "overlap_all": len(set(o_all) & set(n_all)), "overlap_top10": len(top(o_all, 10) & top(n_all, 10)),
           "stored_long": len(o_l), "new_long": len(n_l), "overlap_long": len(set(o_l) & set(n_l)),
           "stored_top5": [(r["id"], r["title"], r["views"]) for r in old[:5]],
           "new_top5": [(r["id"], r["title"], r["views"]) for r in new[:5]], "new_rows": new}
    res.append(rec); time.sleep(1)
    print(kw, sort, {k: rec[k] for k in ("stored_n", "new_n", "overlap_all", "overlap_top10", "stored_long", "new_long", "overlap_long")})
    for a, b in zip(rec["stored_top5"], rec["new_top5"]): print("   S:", a, "\n   N:", b)
json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False)
