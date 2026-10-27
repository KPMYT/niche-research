import csv, re, json
base='/home/user/niche-research/studies/hvac/'
items={}
order=[]
def add(vid, lst, rank, views, mult, channel, title, upload):
    if vid not in items:
        items[vid]=dict(video_id=vid, lists=[], ranks=[], views=views, multiple=mult, channel=channel, title=title, upload=upload)
        order.append(vid)
    d=items[vid]
    if lst not in d['lists']: d['lists'].append(lst)
    d['ranks'].append(rank)
    if not d['multiple'] and mult: d['multiple']=mult
for r in csv.DictReader(open(base+'top-100.csv')):
    add(r['video_id'],'top100','top100#'+r['rank'],r['views'],r['multiple'],r['channel'],r['title'],r['upload_date'])
sec=None
secmap={'Last 90 days: top 30 by views':('recent-90d','90d-views'),'Last 90 days: top 30 by multiple':('recent-90d','90d-mult'),
 'Last 12 months: top 50 by views':('recent-12m','12m-views'),'Last 12 months: top 50 by multiple':('recent-12m','12m-mult')}
for line in open(base+'recent-winners.md'):
    if line.startswith('## '):
        sec=None
        for k,v in secmap.items():
            if line[3:].startswith(k): sec=v
        continue
    if sec and line.startswith('| ') and '(`' in line:
        cells=[c.strip().replace('\\|','|') for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
        m=re.search(r'\(`([A-Za-z0-9_-]{11})`\)',cells[1])
        vid=m.group(1); title=cells[1][:m.start()].strip().strip('"')
        ch=re.sub(r'\s*\(@.*\)$','',cells[2])
        add(vid,sec[0],sec[1]+'#'+cells[0],cells[3].replace(',',''),cells[6].rstrip('x'),ch,title,cells[4])
print(len(order))
json.dump([items[v] for v in order],open('list.json','w'),indent=1)
from collections import Counter
print(Counter(';'.join(items[v]['lists']) for v in order))
