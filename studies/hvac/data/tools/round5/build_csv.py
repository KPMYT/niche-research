import json, csv, re, statistics as st
L=json.load(open('list.json'))
rows=[l.rstrip('\n').split('|') for l in open('labels.txt') if not l.startswith('#')]
F=['face','person','object','words','colours','text','arrows','before_after','red_green','background','look']
logo_only={'ozaw9QhxkQU':'none (show logo "This Old House")','PqrZWd_CQIE':'none (show logo "This Old House")'}
out=[]
CUT={'--bKaRdZGO4','C5DRPlNLZVU','XJzM-fcrFck','ZWEY07bi4vs','nPf7eZfpVxw','qqevEiBIDUQ','cDvXL6yCSfw','H8-QNBd7MIo'}
for d,r in zip(L,rows):
    lab=dict(zip(F,r[1:]))
    vid=d['video_id']
    if vid in logo_only: lab['words']='0'; lab['text']=logo_only[vid]; lab['colours']='none (logo white on blue)'
    p=lab['person'].lower()
    ptype='real' if p.startswith('real') else 'AI' if (p.startswith('ai') or p.startswith('unclear')) else 'cartoon' if p.startswith('cartoon') else 'none'
    look=lab['look'].lower(); obj=lab['object']; w=int(lab['words'])
    ba=lab['before_after'].lower().startswith('yes')
    if vid in CUT: g='AI cut-away house / buried pipe + claim text'
    elif 'cartoon' in look or 'animation' in look: g='cartoon / sketch / 3D animation'
    elif 'diagram' in look or '3d render' in look or 'text slide' in look: g='diagram / 3D render explainer'
    elif ba: g='before/after or hot-vs-cold split'
    elif 'store front' in obj: g='AI store front + list text'
    elif 'history' in look: g='AI history scene + red banner'
    elif look.startswith('ai image'):
        if ptype=='AI': g='AI persona + bold text (+ red arrow)' if w>0 else 'AI persona + object, no text'
        else: g='AI object/build + bold text' if w>0 else 'AI object/build, no headline'
    elif look.startswith('graphic (bold text panel'): g='bold text panel + product cut-out'
    else:
        if ptype=='real': g='real face + text' if w>0 else 'real person on the job, no text'
        else: g='real build/product photo + text' if w>0 else 'real build/product photo, no text'
    out.append(dict(video_id=vid,list=';'.join(d['lists']),rank='; '.join(d['ranks']),views=d['views'],multiple=d['multiple'],channel=d['channel'],title=d['title'],upload_date=d['upload'],
        face=lab['face'],person_type=ptype,person=lab['person'],object_shown=lab['object'],text_word_count=w,text_colours=lab['colours'],text_words=lab['text'],
        arrows_circles=lab['arrows'],before_after=lab['before_after'],red_green_marks=lab['red_green'],background=lab['background'],overall_look=lab['look'],style_group=g,
        thumb_file='img/'+vid+'.jpg',label_note='reading by eye, 2026-10-26'))
json.dump(out,open('out.json','w'),indent=1)
dst='/home/user/niche-research/studies/hvac/thumbnails/labels-top-winners.csv'
with open(dst,'w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=list(out[0].keys())); wr.writeheader(); wr.writerows(out)
from collections import Counter
c=Counter(o['style_group'] for o in out)
for g,n in c.most_common():
    vs=[int(o['views']) for o in out if o['style_group']==g]; ms=[float(o['multiple']) for o in out if o['style_group']==g]
    print(f"{n:3d} {g:45s} medV={st.median(vs):>12,.0f} medM={st.median(ms):.1f}")
