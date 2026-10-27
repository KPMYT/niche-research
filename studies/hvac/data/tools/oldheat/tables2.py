exec(open('/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/tables.py').read().split('print("## pool")')[0])
def t(v): return (v['orig_title'] or v['title']).replace('|', '/')
H = jsonable(res['heat']['vids'])
print("## top20 heat")
print("| # | ID | Title | Channel | Country (About tab) | Views | Age | Length |")
print("|---|---|---|---|---|---|---|---|")
for i, v in enumerate(H[:20], 1):
    print(f"| {i} | `{v['id']}` | {t(v)} | {v['channel']} | {ctry(v['channelId'])} | {fmt(v['views_n'])} | {v['age']} | {v['length']} |")
print("## top20 heat US-listed")
print("| # | ID | Title | Channel | Views | Age | Length |")
print("|---|---|---|---|---|---|---|")
for i, v in enumerate([v for v in H if ctry(v['channelId']) == 'United States'][:20], 1):
    print(f"| {i} | `{v['id']}` | {t(v)} | {v['channel']} | {fmt(v['views_n'])} | {v['age']} | {v['length']} |")
R = [v for v in H if v['recent_12mo']]
print("## recent top10")
print("| # | ID | Title | Channel | Country | Views | Age | Length |")
print("|---|---|---|---|---|---|---|---|")
for i, v in enumerate(R[:10], 1):
    print(f"| {i} | `{v['id']}` | {t(v)} | {v['channel']} | {ctry(v['channelId'])} | {fmt(v['views_n'])} | {v['age']} | {v['length']} |")
print("## channels")
by = collections.defaultdict(list)
for v in H: by[v['channelId']].append(v)
def chrow(cid, vs):
    a = A.get(cid, {})
    rec = sum(1 for v in vs if v['recent_12mo'])
    return f"| {vs[0]['channel']} | {ctry(cid)} | {a.get('subscriberCountText','not found')} | {a.get('joinedDateText','not found')} | {len(vs)} | {fmt(sum(v['views_n'] or 0 for v in vs))} | {fmt(med([v['views_n'] for v in vs if v['views_n'] is not None]))} | {rec} | {t(max(vs, key=lambda v: v['views_n'] or 0))[:60]} |"
hdr = "| Channel | Country | Subs (About) | Joined | Videos in pool | Total views in pool | Median in pool | Last 12 mo in pool | Top video in pool |\n|---|---|---|---|---|---|---|---|---|"
print("### by count"); print(hdr)
for cid, vs in sorted(by.items(), key=lambda x: (-len(x[1]), -sum(v['views_n'] or 0 for v in x[1])))[:15]: print(chrow(cid, vs))
print("### by views"); print(hdr)
for cid, vs in sorted(by.items(), key=lambda x: -sum(v['views_n'] or 0 for v in x[1]))[:15]: print(chrow(cid, vs))
print("### recent channels (last 12 mo uploads in pool) by count"); print(hdr)
rb = collections.defaultdict(list)
for v in R: rb[v['channelId']].append(v)
for cid, vs in sorted(rb.items(), key=lambda x: (-len(x[1]), -sum(v['views_n'] or 0 for v in x[1])))[:15]: print(chrow(cid, vs))
print("## all recent heat")
for v in R: print(v['views_n'], v['age'], t(v)[:80], '|', v['channel'], '|', ctry(v['channelId']), '|', A.get(v['channelId'],{}).get('subscriberCountText'), A.get(v['channelId'],{}).get('joinedDateText'))
print("## recent top10 US-listed")
print("| # | ID | Title | Channel | Views | Age | Length |")
print("|---|---|---|---|---|---|---|")
for i, v in enumerate([v for v in R if ctry(v['channelId']) == 'United States'][:10], 1):
    print(f"| {i} | `{v['id']}` | {t(v)} | {v['channel']} | {fmt(v['views_n'])} | {v['age']} | {v['length']} |")
print("## check")
chk = {}
for l in open(S + 'dates.txt'):
    p = [x.strip() for x in l.split('|')]
    m = re.search(r'\| ([\d,]+) views \|', l)
    if m: chk[p[0]] = (int(m.group(1).replace(',', '')), p[1], p[2])
ok = 0; n = 0
for v in H[:20]:
    if v['id'] in chk:
        n += 1; c = chk[v['id']]
        diff = (c[0] - v['views_n']) / v['views_n'] * 100
        ok += abs(diff) < 2 and c[2] == v['channel']
        print(f"| `{v['id']}` | {fmt(v['views_n'])} | {fmt(c[0])} | {diff:+.2f}% | {c[2]} |")
print("matched", ok, "of", n)
