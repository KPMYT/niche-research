import json,sys,os
d=json.load(open(sys.argv[1])); out=sys.argv[2]
for r in d['transcripts']['results']:
    vid=r['videoId']
    if not r.get('success'): print(vid,'FAILED'); continue
    segs=r['data']['transcript']
    # keep every other line approx since overlapping? segments are sequential lines
    lines=[]; 
    for i,s in enumerate(segs):
        if i%10==0: lines.append('\n['+s['startTime']+'] ')
        lines.append(s['text']+' ')
    open(os.path.join(out,vid+'.txt'),'w').write(''.join(lines))
    print(vid, len(segs))
