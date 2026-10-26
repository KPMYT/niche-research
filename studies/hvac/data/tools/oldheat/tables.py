exec(open('/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/build.py').read().split('if __name__')[0])
import glob
A = {}
for f in glob.glob(S + 'about-*.jsonl'):
    for l in open(f): j = json.loads(l); A[j['channelId']] = j
def ctry(cid):
    c = A.get(cid, {}).get('country')
    return c if c and c != 'None' else 'not stated'
def fmt(x):
    if x is None: return 'not found'
    if isinstance(x, float): x = round(x)
    return f"{x:,}"
def srow(name, kw, s):
    return f"| {name} | {kw} | {s['videos']:,} | {s['channels']:,} | {fmt(s['median'])} | {fmt(s['p75'])} | {fmt(s['p90'])} | {s['n_100k']:,} | {s['n_1m']:,} | {s['recent_n']:,} | {fmt(s['recent_median'])} | {s['recent_100k']:,} |"
print("## pool")
print("| Set | Keywords | Videos | Channels | Median views | 75th pct | 90th pct | >=100K | >=1M | Last 12 mo: videos | Last 12 mo: median | Last 12 mo: >=100K |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
print(srow("Old-house heat, all", 38, res['heat']['summary']))
print(srow("Old-house heat, matched 10", 10, res['heat_matched']['summary']))
print(srow("AC, matched 10", 10, res['ac']['summary']))
for side, key in (("Old-house heat, all", 'heat'), ("Old-house heat, matched 10", 'heat_matched'), ("AC, matched 10", 'ac')):
    us = {k: v for k, v in res[key]['vids'].items() if ctry(v['channelId']) == 'United States'}
    print(srow(side + " - US-listed channels only", "", summary(us)))
print()
print("## funnel")
for key in ('heat', 'heat_matched', 'ac'): print(key, res[key]['funnel'])
print()
print("## country mix (videos)")
for key in ('heat', 'heat_matched', 'ac'):
    c = collections.Counter(ctry(v['channelId']) for v in res[key]['vids'].values())
    n = sum(c.values())
    print(key, "; ".join(f"{k} {v} ({100*v/n:.0f}%)" for k, v in c.most_common(6)))
print()
print("## per keyword")
print("| Side | Keyword | Rows pulled (4 sorts) | Distinct videos | Kept (long, English, on topic) | Channels | Median views | Top views | >=100K | Last 12 mo kept | Last 12 mo median |")
print("|---|---|---|---|---|---|---|---|---|---|---|")
for side in ('heat', 'ac'):
    for k, v in res[side]['per_kw'].items():
        m = " (matched)" if side == 'heat' and k in MATCHED_HEAT else ""
        print(f"| {side} | {k}{m} | {v['raw_rows']} | {v['distinct_any']} | {v['distinct_topical']} | {v['channels']} | {fmt(v['median'])} | {fmt(v['max'])} | {v['n_100k']} | {v['recent_n']} | {fmt(v['recent_median'])} |")
