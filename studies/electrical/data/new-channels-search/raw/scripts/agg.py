import json,glob,os,re,collections,sys
R='/home/user/niche-research/studies/electrical/data/new-channels-search/raw'
REL=re.compile(r"electric|electrician|outlet|breaker|panel|wiring|wire|romex|gfci|afci|plug|cord|power strip|surge|generator|backfeed|blackout|power outage|power goes out|outage|grid|lineman|linemen|fire|smoke|carbon monoxide|\bco\b|detector|alarm|dryer|lint|battery|batteries|lithium|e-?bike|power bank|charger|space heater|heater|electric bill|electricity|utility|inspector|inspection|knob|aluminum|zinsco|federal pacific|fpe|volt|amp|unplug|appliance|storm|light|extension|burn|lamp|solar|power station|ecoflow",re.I)
def secs(d):
    if not d: return None
    p=[int(x) for x in d.split(':')]; s=0
    for x in p: s=s*60+x
    return s
rows=[]
for f in sorted(glob.glob(R+'/search__*.json')):
    b=os.path.basename(f)[8:-5]; slug,sort=b.rsplit('__',1)
    try: d=json.load(open(f))
    except Exception: print('BAD',f); continue
    for i,x in enumerate(d):
        if x.get('type')!='VIDEO': continue
        rows.append(dict(slug=slug,sort=sort,rank=i+1,**{k:x.get(k) for k in ['id','title','channel','channel_id','views','age','dur']}))
json.dump(rows,open('/tmp/claude-0/-home-user/bd54f07e-8fa6-5773-8636-91dde80d17df/scratchpad/h7/allrows.json','w'))
print(len(rows),'rows')
