import json,os,re,statistics,sys
R='/home/user/niche-research/studies/electrical/data/new-channels-search/raw'
def secs(d):
    if not d: return None
    s=0
    for x in d.split(':'): s=s*60+int(x)
    return s
def num(v):
    if not v: return None
    v=v.split()[0].replace(',','')
    m={'K':1e3,'M':1e6,'B':1e9}
    try: return int(float(v[:-1])*m[v[-1]]) if v[-1] in m else int(float(v))
    except: return None
out={}
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
for cid in ids:
    f=f'{R}/ch__{cid}__latest.json'
    if not os.path.exists(f): continue
    try: d=json.load(open(f))
    except: print('BAD',cid); continue
    vids=d.get('videos',[])
    lf=[v for v in vids if (secs(v.get('dur')) or 0)>=300]
    med=statistics.median([v['views'] or 0 for v in lf]) if lf else None
    best=max(lf,key=lambda v:v['views'] or 0) if lf else None
    vc=num(d.get('videos_count')) or 0
    pf=f'{R}/ch__{cid}__popular.json'
    if os.path.exists(pf):
        try:
            pl=[v for v in json.load(open(pf))['videos'] if (secs(v.get('dur')) or 0)>=300]
            if pl:
                pb=max(pl,key=lambda v:v['views'] or 0)
                if not best or (pb['views'] or 0)>(best['views'] or 0): best=pb
        except Exception as e: print('popbad',cid,e)
    first=None
    g=f'{R}/ch__{cid}__oldest.json'
    if os.path.exists(g):
        try:
            o=json.load(open(g))['videos']
            if o: first=(o[0]['age'],o[0]['title'][:60],o[0]['id'])
        except: pass
    elif vids: first=(vids[-1]['age'],vids[-1]['title'][:60],vids[-1]['id'])
    out[cid]=dict(name=d.get('channel'),handle=(d.get('handle') or '').replace('http://www.youtube.com/',''),subs=d.get('subs'),subs_n=num(d.get('subs')),videos=vc,
        desc=(d.get('description') or '').replace('\n',' ')[:260],n_lf=len(lf),median=med,newest=vids[0]['age'] if vids else None,first=first,
        best=(best['id'],best['title'],best['views'],best['dur'],best['age']) if best else None,
        recent=[(v['id'],v['title'],v['views'],v['dur'],v['age']) for v in lf[:30]])
json.dump(out,open(sys.argv[2],'w'),indent=1)
for cid,c in out.items():
    print(f"== {c['name']} | {cid} | {c['handle']} | {c['subs']} | {c['videos']} vids | LF on page {c['n_lf']} med {c['median']} | newest {c['newest']} | first {c['first']}")
    print('   ',c['desc'][:200])
    if c['best']: print('    BEST',c['best'])
