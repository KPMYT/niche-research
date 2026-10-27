import json,sys,statistics as st,collections
P=sys.argv[1]
R=json.load(open(f"{P}/all_tagged.json")); o=json.load(open(f"{P}/built.json"))
def tg(v): return v["F_main"]+("×"+v["F_mod"] if v["F_mod"] else "")
for k in o:
    c=o[k]; vs=[v for v in R if v["channel"]==k]
    print(f"\n### {k} normal={c['normal']} n={c['n']} subs={c['subs']} long-form={len(vs)} collab-normal={c['norm_collab']} solo={c['norm_solo']}")
    print("TOP by multiple")
    for v in sorted(vs,key=lambda v:-v["multiple"])[:25]:
        print(f"| {v['multiple']}x | {v['views']:,} | {v['date']} | {tg(v)} | {'C' if v['collab'] else ''} | {v['title']} | xmonth {v['x_month']}")
    print("Under-60-day views/day top 12")
    for v in sorted([v for v in vs if v['age']<60],key=lambda v:-v["vpd"])[:12]:
        print(f"| {v['vpd']}/d | {v['views']:,} | {v['date']} | {v['multiple']}x | {tg(v)} | {v['title']}")
