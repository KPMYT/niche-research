import json,statistics,datetime,sys,csv
P=sys.argv[1]
TODAY=datetime.date(2026,10,26)
out={}
for k in ["roger","mark","vintage","werner"]:
    d=json.load(open(f"{P}/tab_{k}.json")); tab={}
    for s,l in d["sorts"].items():
        for v in l or []: tab.setdefault(v["id"],v)
    rs=[json.loads(l) for l in open(f"{P}/exact_{k}.jsonl")]
    vids=[]
    for r in rs:
        dt=datetime.date.fromisoformat(r["date"])
        if k=="vintage" and dt<datetime.date(2026,3,1): continue
        t=tab[r["id"]]
        collab=[m for m in t["meta"] if m.startswith("and ")]
        age=(TODAY-dt).days
        vids.append(dict(id=r["id"],title=r["title"] or t["title"],date=r["date"],views=r["views"],age=age,dur=t["dur"],collab="; ".join(collab),pulled=r["pulled"][:16]))
    win=[v["views"] for v in vids if 14<=v["age"]<=90]
    norm=statistics.median(win) if win else None
    for v in vids:
        v["multiple"]=round(v["views"]/norm,2) if norm else None
        v["vpd"]=round(v["views"]/max(v["age"],1)) if v["age"]<60 else ""
    out[k]=dict(normal=norm,n=len(win),vids=vids,subs=d["subs"],nvid=d["videos"],chid=d["id"],name=d["channel"])
    # collab-split normals
    wc=[v["views"] for v in vids if 14<=v["age"]<=90 and v["collab"]]
    ws=[v["views"] for v in vids if 14<=v["age"]<=90 and not v["collab"]]
    out[k]["norm_collab"]=(statistics.median(wc) if wc else None,len(wc))
    out[k]["norm_solo"]=(statistics.median(ws) if ws else None,len(ws))
json.dump(out,open(f"{P}/built.json","w"),indent=1)
for k,o in out.items():
    print(k,o["name"],o["chid"],o["subs"],o["nvid"],"long-form kept",len(o["vids"]),"normal",o["normal"],"n",o["n"],"collab",o["norm_collab"],"solo",o["norm_solo"])
