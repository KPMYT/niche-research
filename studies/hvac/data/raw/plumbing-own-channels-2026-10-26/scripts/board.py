import json,sys,statistics as st,collections,csv
P=sys.argv[1]
R=json.load(open(f"{P}/all_tagged.json"))
def board(rows,label,key="main"):
    g=collections.defaultdict(list)
    for v in rows:
        fs=[v["F_main"]] if key=="main" else [x for x in (v["F_main"],v["F_mod"]) if x]
        for f in fs: g[f].append(v)
    out=[]
    for f,l in g.items():
        ms=[v["multiple"] for v in l]
        best=max(l,key=lambda v:v["multiple"])
        out.append((f,len(l),sum(m>=2 for m in ms),sum(m<0.5 for m in ms),round(st.median(ms),2),best))
    out.sort(key=lambda x:(-x[2],-x[4]))
    print(f"\n## {label} ({len(rows)} videos)")
    print("| F | n | ≥2x | <0.5x | median x | best (x, views, channel) |")
    for f,n,w,fl,med,b in out:
        print(f"| {f} | {n} | {w} | {fl} | {med} | {b['multiple']}x · {b['views']:,} · {b['channel']} · \"{b['title']}\" |")
    return out
allm=[v for v in R if v["age"]>=14]
cur=[v for v in R if v["age"]>=14 and v["date"]>="2026-07-01"]
new=[v for v in R if v["date"]>="2026-10-01"]
o1=board(allm,"ALL-TIME, main tag, age>=14")
o2=board(cur,"CURRENT 2026-07-01..2026-10-12 uploads, main tag")
o3=board(cur,"CURRENT, any tag (main or modifier)",key="any")
o4=board(new,"NEW since 2026-10-01 (mostly <26 days old)")
with open(f"{P}/format_scoreboard.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["window","F","n","n_ge_2x","n_lt_0.5x","median_multiple","best_title","best_views","best_multiple","best_channel"])
    for lab,o in [("all-time age>=14 main",o1),("current 2026-07-01..10-12 main",o2),("current any tag",o3),("new since 2026-10-01 main",o4)]:
        for fx,n,wn,fl,med,b in o: w.writerow([lab,fx,n,wn,fl,med,b["title"],b["views"],b["multiple"],b["channel"]])
