import json,csv,glob,os,re,collections,statistics
H='/tmp/claude-0/-home-user/bd54f07e-8fa6-5773-8636-91dde80d17df/scratchpad/h7'
OUT='/home/user/niche-research/studies/electrical/data/new-channels-search'
R=OUT+'/raw'
exec(open(H+'/tag.py').read()); exec(open(H+'/cls.py').read())
def secs(d):
    if not d: return None
    s=0
    for x in d.split(':'): s=s*60+int(x)
    return s
kw={}
for l in open(H+'/kw.tsv'):
    k,src,core=(l.rstrip('\n').split('\t')+['',''])[:3]
    kw[k.lower().replace(' ','_').replace('-','-')]=k
def kwname(slug):
    for k,v in kw.items():
        if re.sub(r'[^a-z0-9_-]','',k)==slug: return v
    return slug
summ=json.load(open(H+'/summ.json'))
rows=json.load(open(H+'/allrows.json'))
exact={}
for f in glob.glob(R+'/videos/*.json'):
    d=json.load(open(f)); exact[os.path.basename(f)[:-5]]=d
def months(age):
    if not age: return None
    m=re.search(r'(\d+)\s*(h|d|w|mo|y)',age)
    if not m: return None
    n=int(m.group(1)); u=m.group(2)
    return {'h':0,'d':n/30,'w':n/4.3,'mo':n,'y':12*n}[u] if u!='h' else 0
# channel -> keywords
chkw=collections.defaultdict(set); chname={}
for r in rows:
    s=secs(r['dur'])
    if s and s>=300 and relevant(r['title']):
        chkw[r['channel_id']].add(kwname(r['slug'])); chname[r['channel_id']]=r['channel']
chsearch={'UC8BFayzSWQxJiSG-6Zpxv4Q':'channel search: retired electrician','UCiXvccIJUXTioQ-b4EwMd8w':'channel search: retired electrician','UCyyCHAOboxY4gcYKCyvUR4A':'channel search: retired lineman','UCrVWzxmdDxvquFwU8xpuT_Q':'channel search: retired lineman','UCnvA17kCklEUs3jtmRz8lrA':'channel search: retired lineman','UCZRL67xg3oz1uRi7E8BD1AQ':'channel search: retired lineman','UCmbkEO_gaZZ_pbrAZAo2yWw':'channel search: retired home inspector','UCt1o6dCpRDLkLWpxkNURnSA':'channel search: retired home inspector','UCmk_aG0OsnaP_7C5OxSSEvQ':'channel search: retired home inspector','UCyzN9txpAFKqcI0-w3DaZyA':'channel search: retired home inspector','UCSxYUWVbK-Cbwna63eOdxWQ':'channel search: retired firefighter'}
# hand labels for breakout videos: id -> (format, emotions, villain)
HL={'gI3SDaKj6xU':('mistakes','E17;E16;E9','own habit'),'-gfBM2U6DxE':('mistakes','E17;E9','own habit'),'p7x4nvpCoDg':('mistakes','E17;E11;E9','insider'),
'TlnC-EVdohU':('only-x','E3;E1;E10','maker / shelf'),'qva5q_Fp3mA':('dont-want-you','E4;E17;E18','last owner / flipper'),'1Oz08l8RTWg':('cheap-hack','E5;E15;E13','none'),
'-Qp1au1u6fQ':('cheap-hack','E1;E5;E11','maker / shelf'),'o4oM6pBG1pw':('mistakes','E17;E9','own habit'),'6R9Tehl7JiY':('cheap-hack','E5;E10;E11','insider'),
'YB-yom19YKo':('mistakes','E9;E17;E10','own habit'),'tAHUsitbSzs':('myth-bust','E5;E12;E6','maker / shelf'),'JLVw2IlK7Zo':('cheap-hack','E15;E5;E13','none'),
'2cjRekzvBRY':('mistakes','E17;E16;E4','own habit'),'cOoEzcdsnd0':('mistakes','E17;E16','own habit'),'8Nh34wXH25I':('cheap-hack','E5;E16;E13','none'),
'MJ2kvs8fbBQ':('dont-want-you','E3;E10;E11','maker / shelf'),'yhzJBGhKUJI':('test','E10;E1;E13','maker / shelf'),'Lk1aHR4a4vE':('how-to','E6;E8;E13','none'),
'CxDyHLLkQi4':('how-to','E17;E13;E15','none'),'ZEkLqBYLRIE':('cheap-hack','E2;E13;E17','service call'),'imYSfX1FdQc':('explainer','E15;E10;E17','none'),
'7voH3cm2h1M':('explainer','E10','none'),'b0mvwo_ueAc':('mistakes','E17;E9','own habit'),'w2WKm5qQLj0':('myth-bust','E17;E12','own habit'),
'IkAbSFWpZhc':('mistakes','E10;E11','insider'),'zvWn7iTVVt4':('dont-want-you','E4;E2;E10','company'),'5pQAWcEsr3Q':('mistakes','E17;E11;E9','insider'),
'4QAyLUhJYng':('cheap-hack','E5;E13;E15','none'),'H1qCDI9DJmY':('cheap-hack','E5;E13','none'),'Y4-bRHrhfnY':('cheap-hack','E1;E13;E3','bill-sender'),
'uuUhLulG83Y':('test','E10;E18;E13','bill-sender'),'eD0e_YWTNlY':('cheap-hack','E15;E13;E5','none'),'yM1Zp0KSZ0U':('cheap-hack','E1;E13','bill-sender'),
'dBPrCiISyX0':('myth-bust','E12;E1;E9','own habit'),'dOZ-8__G4uU':('before-you','E1;E2','service call'),'k1HGyewDZ_k':('cheap-hack','E1;E15;E13','bill-sender'),
'CJYzgRySnow':('dont-want-you','E3;E4;E18','last owner / flipper'),'Qb25KrQdpaQ':('cheap-hack','E5;E15','none'),'V3rTmNcXB5I':('only-x','E3;E1','maker / shelf'),
'bZeu29qOVm8':('cheap-hack','E5;E1','none'),'-4s6efcxQH8':('mistakes','E1;E9','own habit'),'9oF08pgotBo':('cheap-hack','E5;E13','none'),'YYnvit8NGxU':('cheap-hack','E5;E15;E16','none')}
LF=lambda d:(secs(d) or 0)>=300
crow=[]; vrows={}
def addv(vid,ch,cid,title,views,vsrc,age,length,note,mult='',mbasis=''):
    if vid in vrows: return
    ex=exact.get(vid)
    date=age; dsrc='YT list page relative age'
    if ex and ex.get('views'):
        views=ex['views']; vsrc='yt.py video (exact)'; date=ex['date']; dsrc='yt.py video (exact)'
    sub=subniche(title) or 'not-electrical'
    f,e,vl=HL.get(vid,(fmt(title),'',''))
    lab = 'hand' if vid in HL else 'auto keyword tag'
    th = f'raw/thumbs/{vid}.jpg' if os.path.exists(f'{R}/thumbs/{vid}.jpg') else ''
    vrows[vid]=dict(video_id=vid,channel=ch,channel_id=cid,title=title,views=views,views_source=vsrc,upload_date=date,date_source=dsrc,length=length,long_form='yes' if LF(length) else 'no',
        subniche=sub,format=f,emotions=e,villain=vl,multiple=mult,multiple_basis=mbasis,thumbnail_file=th,notes=(note+f'; labels: {lab} (my reading)').strip('; '))
# checked channels
for cid,c in summ.items():
    if cid not in C: continue
    typ,persona,bg,scope,notes=C[cid]
    vids=[]
    for tab in ('latest','popular'):
        f=f'{R}/ch__{cid}__{tab}.json'
        if os.path.exists(f):
            try: vids+= [(v,tab) for v in json.load(open(f))['videos']]
            except: pass
    lfl=[v for v,t in vids if t=='latest' and LF(v.get('dur'))]
    med=c['median']
    for v,t in vids:
        if not LF(v.get('dur')): continue
        isbest = c['best'] and v['id']==c['best'][0]
        if relevant(v['title']) or isbest:
            m=round(v['views']/med,1) if med and v['views'] is not None else ''
            addv(v['id'],c['name'],cid,v['title'],v['views'],f'YT channel {t.capitalize()} tab (rounded)',v.get('age'),v.get('dur'),'from channel tab',m,f'median of long-form on Latest tab p1 (up to 30 newest uploads) = {med}' if med else '')
    fa=c['first'][0] if c['first'] else None
    mo=months(fa)
    repurposed = 'repurposed' in notes or 'pivot' in notes
    if mo is None: new='not found'
    elif mo>=12 and not repurposed: new='no'
    elif mo<12: new='yes' + (' (repurposed account, first niche upload later)' if repurposed else '')
    elif repurposed: new='yes (pivot: old account, niche uploads 2026)'
    else: new='no'
    best=c['best']
    bv=best[2] if best else None
    if best and best[0] in exact and exact[best[0]].get('views'): bv=exact[best[0]]['views']
    subs=c['subs_n']
    take = cid!='UCSf0X7Rt96r7sx0uCiDgDcA' and new.startswith('yes') and bv is not None and (bv>=100000 or (med and med>=1000 and subs and med>=2*subs))
    found = '; '.join(sorted(chkw.get(cid,[]))) or chsearch.get(cid,'')
    crow.append(dict(name=c['name'],channel_id=cid,handle=c['handle'],subs=c['subs'] or 'hidden/not found',type=typ,persona=persona,claimed_background=bg,
        first_upload=(f"{fa} ({c['first'][1]}, {c['first'][2]}) [Oldest tab]" if c['first'] and c['videos']>30 else (f"{fa} ({c['first'][1]}, {c['first'][2]}) [last item on Latest tab]" if c['first'] else 'not found')),
        videos_count=c['videos'],scope=scope,new_12mo=new,best_video_id=best[0] if best else '',best_video_title=best[1] if best else '',best_video_views=bv,
        best_video_length=best[3] if best else '',best_video_age=(exact[best[0]]['date'] if best and best[0] in exact and exact[best[0]].get('date') else (best[4] if best else '')),
        found_via_keyword=found,notes=('TAKING OFF; ' if take else '')+notes+f'; LF median on Latest p1 = {med}; type from thumbnails+description (my reading)'))
# search-only channels
for r in rows:
    s=secs(r['dur'])
    if not(s and s>=300 and relevant(r['title'])): continue
    addv(r['id'],r['channel'],r['channel_id'],r['title'],r['views'],f"YT search list page ({r['sort']}, exact count as shown)",r['age'],r['dur'],f"found via '{kwname(r['slug'])}' {r['sort']} rank {r['rank']}")
checked={r['channel_id'] for r in crow}
best_by=collections.defaultdict(list)
for v in vrows.values(): best_by[v['channel_id']].append(v)
for cid,vs in best_by.items():
    if cid in checked or not cid: continue
    b=max(vs,key=lambda v:v['views'] or 0)
    crow.append(dict(name=b['channel'],channel_id=cid,handle='',subs='not checked',type='not checked',persona='not checked',claimed_background='not checked',first_upload='not checked',videos_count='not checked',
        scope='not checked',new_12mo='not checked',best_video_id=b['video_id'],best_video_title=b['title'],best_video_views=b['views'],best_video_length=b['length'],best_video_age=b['upload_date'],
        found_via_keyword='; '.join(sorted(chkw.get(cid,[]))),notes=f'search page only; {len(vs)} relevant long-form video(s) in results'))
order={'yes':0}
crow.sort(key=lambda r:(r['subs']=='not checked', -(r['best_video_views'] or 0) if isinstance(r['best_video_views'],int) else 0))
cols='name,channel_id,handle,subs,type,persona,claimed_background,first_upload,videos_count,scope,new_12mo,best_video_id,best_video_title,best_video_views,best_video_length,best_video_age,found_via_keyword,notes'.split(',')
with open(OUT+'/channels.csv','w',newline='') as f:
    w=csv.DictWriter(f,cols); w.writeheader(); w.writerows(crow)
vc='video_id,channel,channel_id,title,views,views_source,upload_date,date_source,length,long_form,subniche,format,emotions,villain,multiple,multiple_basis,thumbnail_file,notes'.split(',')
vl=sorted(vrows.values(),key=lambda v:-(v['views'] or 0))
with open(OUT+'/videos.csv','w',newline='') as f:
    w=csv.DictWriter(f,vc); w.writeheader(); w.writerows(vl)
json.dump(crow,open(H+'/crow.json','w'))
print(len(crow),'channels',len(checked),'checked',len(vl),'videos')
