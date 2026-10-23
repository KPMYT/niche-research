import json,re,collections
exec(open('agg.py').read().split('rows=[]')[0])
NOISE=re.compile(r"paw patrol|kids|nick jr|toys|police|gta|minecraft|roblox|cartoon|song|movie|trailer|anime|game",re.I)
rows=json.load(open('allrows.json'))
def recent(a): return bool(a) and bool(re.search(r'(mo|w|d|h|minutes?|hours?|days?|weeks?|months?) ago',a)) and not re.search(r'\by',a)
by=collections.defaultdict(list)
for r in rows:
    s=secs(r['dur'])
    if s and s>=300 and recent(r['age']) and REL.search(r['title'] or '') and not NOISE.search((r['title'] or '')+(r['channel'] or '')): by[r['channel_id']].append(r)
out=[]
for ch,v in by.items():
    u=list({x['id']:x for x in v}.values())
    best=max(u,key=lambda x:x['views'] or 0)
    out.append((best['views'] or 0,best['channel'],ch,len(u),best['id'],best['title'][:90],best['age'],best['dur'],sorted(set(x['slug'] for x in v))[:3]))
for o in sorted(out,reverse=True): print(o)
print(len(out))
