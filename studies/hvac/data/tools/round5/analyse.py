import json, statistics as st, re
from collections import Counter, defaultdict
O=json.load(open('out.json'))
for o in O:
    o['v']=int(o['views']); o['m']=float(o['multiple'])
    o['r']={}
    for x in o['rank'].split('; '):
        k,n=x.split('#'); o['r'][k]=int(n)
def med(xs,f='{:,.0f}'): return f.format(st.median(xs)) if xs else '-'
def fmtm(xs): return ('{:,.1f}x'.format(st.median(xs))) if xs else '-'
groups=[g for g,_ in Counter(o['style_group'] for o in O).most_common()]
T=[o for o in O if 'top100' in o['r']]
R=[o for o in O if any(k.startswith(('90d','12m')) for k in o['r'])]
print('T',len(T),'R',len(R))
def table(sets,names):
    print('| Style group | '+' | '.join(f'{n}: n' for n in names)+' | All: median views | All: median multiple | Top 100: median views | Recent: median views | Recent: median multiple |')
    print('|---|'+'---:|'*(len(names)+5))
    for g in groups:
        a=[o for o in O if o['style_group']==g]; t=[o for o in T if o['style_group']==g]; r=[o for o in R if o['style_group']==g]
        cnt=[str(len([o for o in s if o['style_group']==g])) for s in sets]
        print(f"| {g} | "+' | '.join(cnt)+f" | {med([o['v'] for o in a])} | {fmtm([o['m'] for o in a])} | {med([o['v'] for o in t])} | {med([o['v'] for o in r])} | {fmtm([o['m'] for o in r])} |")
    print(f"| **Total** | "+' | '.join(str(len(s)) for s in sets)+f" | {med([o['v'] for o in O])} | {fmtm([o['m'] for o in O])} | {med([o['v'] for o in T])} | {med([o['v'] for o in R])} | {fmtm([o['m'] for o in R])} |")
print('\n### TABLE1'); table([O,T,R],['All','Top 100','Recent'])
def tiers(key,label,bounds=(10,25)):
    S=[o for o in O if key in o['r']]
    a=[o for o in S if o['r'][key]<=bounds[0]]; b=[o for o in S if bounds[0]<o['r'][key]<=bounds[1]]; c=[o for o in S if o['r'][key]>bounds[1]]
    print(f'\n### TIERS {label} (n={len(S)})')
    print(f'| Style group | Ranks 1-{bounds[0]} | Ranks {bounds[0]+1}-{bounds[1]} | Ranks {bounds[1]+1}+ |'); print('|---|---:|---:|---:|')
    for g in groups:
        x=[len([o for o in s if o['style_group']==g]) for s in (a,b,c)]
        if sum(x): print(f'| {g} | {x[0]} | {x[1]} | {x[2]} |')
    print(f'| **Total** | {len(a)} | {len(b)} | {len(c)} |')
    return a,b,c
ta=tiers('top100','top 100 all-time, by views')
ra=tiers('12m-views','last 12 months, top 50 by views')
tiers('90d-views','last 90 days, top 30 by views')
tiers('12m-mult','last 12 months, top 50 by multiple')
tiers('90d-mult','last 90 days, top 30 by multiple')
# top 10 lists
for key in ('top100','12m-views','90d-views'):
    S=sorted([o for o in O if key in o['r']],key=lambda o:o['r'][key])[:10]
    print(f'\n### TOP10 {key}')
    for o in S: print(f"| {o['r'][key]} | `{o['video_id']}` | {o['channel']} | {o['v']:,} | {o['m']:,.1f}x | {o['style_group']} | {o['text_words'][:70]} |")
# features
def feat(S,name):
    n=len(S)
    def p(f): k=sum(1 for o in S if f(o)); return f'{k} ({100*k/n:.0f}%)'
    return dict(name=name,n=n,
      face=p(lambda o:o['face']=='yes'),
      real=p(lambda o:o['person_type']=='real'), ai=p(lambda o:o['person_type']=='AI'), cart=p(lambda o:o['person_type']=='cartoon'),
      look_real=p(lambda o:o['overall_look'].lower().startswith('realistic')), look_ai=p(lambda o:o['overall_look'].lower().startswith('ai')),
      look_cart=p(lambda o:o['overall_look'].lower().startswith(('cartoon','3d animation'))), look_gr=p(lambda o:o['overall_look'].lower().startswith(('graphic','3d render','clean'))),
      text=p(lambda o:o['text_word_count']>0), arrows=p(lambda o:o['arrows_circles'].startswith('yes')),
      red_arrow=p(lambda o:'red' in o['arrows_circles'] and o['arrows_circles'].startswith('yes')),
      ba=p(lambda o:o['before_after'].startswith('yes')),
      redx=p(lambda o:'red X' in o['red_green_marks'] or 'crossed' in o['red_green_marks'].lower()),
      check=p(lambda o:'check' in o['red_green_marks']),
      medw=st.median([o['text_word_count'] for o in S if o['text_word_count']>0]) if any(o['text_word_count']>0 for o in S) else 0)
print('\n### FEATURES')
sets=[(T,'Top 100'),(ta[0],'Top 100 ranks 1-10'),(ta[0]+ta[1],'Top 100 ranks 1-25'),(ta[2],'Top 100 ranks 26-100'),(R,'Recent (all lists)'),(ra[0],'12m views ranks 1-10'),(ra[0]+ra[1],'12m views ranks 1-25'),(ra[2],'12m views ranks 26-50')]
F=[feat(s,n) for s,n in sets]
keys=[('face','Face shown'),('real','Real person'),('ai','AI person'),('cart','Cartoon person'),('look_real','Look: realistic photo'),('look_ai','Look: AI image'),('look_cart','Look: cartoon/animation'),('look_gr','Look: graphic/diagram/render'),('text','Any headline text'),('medw','Median words (when text)'),('arrows','Arrow or circle'),('red_arrow','Red arrow or circle'),('ba','Before/after or split'),('redx','Red X / crossed out'),('check','Check mark')]
print('| Feature | '+' | '.join(f"{f['name']} (n={f['n']})" for f in F)+' |'); print('|---|'+'---:|'*len(F))
for k,lab in keys: print(f'| {lab} | '+' | '.join(str(f[k]) for f in F)+' |')
# text length buckets
print('\n### WORDS')
B=[('0 (no headline)',0,0),('1-3',1,3),('4-6',4,6),('7-10',7,10),('11+',11,999)]
print('| Words | Top 100: n | Top 100: median views | Recent: n | Recent: median views | Recent: median multiple |'); print('|---|---:|---:|---:|---:|---:|')
for lab,a,b in B:
    t=[o for o in T if a<=o['text_word_count']<=b]; r=[o for o in R if a<=o['text_word_count']<=b]
    print(f"| {lab} | {len(t)} | {med([o['v'] for o in t])} | {len(r)} | {med([o['v'] for o in r])} | {fmtm([o['m'] for o in r])} |")
# colours
print('\n### COLOURS')
C=[('white',r'white'),('yellow',r'yellow'),('red',r'\bred\b'),('black',r'black'),('blue / cyan',r'blue|cyan'),('green',r'green'),('orange',r'orange')]
print('| Text colour (mentioned) | Top 100 with text | Recent with text |'); print('|---|---:|---:|')
Tt=[o for o in T if o['text_word_count']>0]; Rt=[o for o in R if o['text_word_count']>0]
for lab,rx in C:
    a=sum(1 for o in Tt if re.search(rx,o['text_colours'])); b=sum(1 for o in Rt if re.search(rx,o['text_colours']))
    print(f'| {lab} | {a} of {len(Tt)} ({100*a/len(Tt):.0f}%) | {b} of {len(Rt)} ({100*b/len(Rt):.0f}%) |')
yw=lambda S: sum(1 for o in S if 'white' in o['text_colours'] and 'yellow' in o['text_colours'])
print('white+yellow', yw(Tt), yw(Rt))
box=lambda S: sum(1 for o in S if re.search(r' on (red|black|white|yellow|blue)',o['text_colours']))
print('boxed', box(Tt), box(Rt))
# examples
print('\n### EXAMPLES')
for g in groups:
    S=sorted([o for o in O if o['style_group']==g],key=lambda o:-o['v'])
    picks=S[:3]
    print(f"- **{g}** ({len(S)}): "+'; '.join(f"`{o['video_id']}` ({o['channel']}, {o['v']:,} views, {o['m']:,.1f}x, {'/'.join(sorted(set(k.split('-')[0] if k!='top100' else 'top100' for k in o['r'])))}{', text: '+o['text_words'][:60] if o['text_word_count'] else ', no text'})" for o in picks))
# channels repeating
print('\n### CHANNELS per group')
for g in groups:
    c=Counter(o['channel'] for o in O if o['style_group']==g)
    print(g, c.most_common(4))
