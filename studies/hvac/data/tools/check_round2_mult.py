#!/usr/bin/env python3
"""Round 2 checker (2026-10-24): recompute a channel multiple from a yt_allsorts.py tab pull.
Baseline = median tab views of Latest-tab uploads >= 5:00 with age below "1y". Usage: python3 -I check_round2_mult.py <tab.json> <video_id>"""
import json,re,statistics,sys
d=json.load(open(sys.argv[1])); vid=sys.argv[2]
L=d['sorts']['Latest']
def secs(t):
    s=0
    for x in (t or '0').split(':'): s=s*60+int(x)
    return s
def age(a):
    m=re.match(r'(\d+)\s*(y|mo|w|d|h|min)',a or '')
    if not m: return None
    return (m.group(2), int(m.group(1)))
rows=[]
for v in L:
    a=[p for p in v['meta'] if 'ago' in p]; a=a[0] if a else None
    rows.append((v['id'],v['title'],secs(v['dur']),age(a),v.get('views_tab'),a))
from collections import Counter
print('latest',len(rows),Counter(r[3][0] for r in rows if r[3]))
last12=[r for r in rows if r[3] and r[3][0]!='y']
base=[r for r in last12 if r[2]>=300]
vals=[r[4] for r in base]; med=statistics.median(vals)
print('last12 all',len(last12),'long-form',len(base),'median',med)
oldest_in_latest=[r for r in rows if r[3]][-1]; print('oldest row in Latest pull:',oldest_in_latest[5])
for s in d['sorts']:
    for v in d['sorts'][s]:
        if v['id']==vid: print(s, v['title'], v['views_tab'], v['dur'], '-> multiple', round(v['views_tab']/med,2)); break
