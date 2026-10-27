exec(open('/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/tables.py').read().split('print("## pool")')[0])
import datetime
D = {}
for l in open(S + 'dates.txt'):
    p = [x.strip() for x in l.split('|')]
    m = re.search(r'([A-Z][a-z]{2}) (\d{1,2}), (\d{4})', l)
    if m: D[p[0]] = datetime.datetime.strptime(m.group(0), '%b %d, %Y').date()
    vm = re.search(r'\| ([\d,]+) views \|', l)
SEP_DEC = {9, 10, 11, 12}
out = {}
for side, n in (('heat', 120), ('ac', 60)):
    L = jsonable(res[side]['vids'])[:n]
    have = [v for v in L if v['id'] in D]
    mc = collections.Counter(D[v['id']].month for v in have)
    sd = [v for v in have if D[v['id']].month in SEP_DEC]; ot = [v for v in have if D[v['id']].month not in SEP_DEC]
    print(f"{side}: top {n} by views, dates found {len(have)}; by month:", " ".join(f"{datetime.date(2000,m,1):%b} {mc.get(m,0)}" for m in range(1, 13)))
    print(f"   Sep-Dec {len(sd)} ({100*len(sd)/len(have):.0f}%), median {fmt(med([v['views_n'] for v in sd]))}; other months {len(ot)}, median {fmt(med([v['views_n'] for v in ot]))}")
    out[side] = {v['id']: str(D[v['id']]) for v in have}
# rough: last 12 months from age text
R = [v for v in jsonable(res['heat']['vids']) if v['recent_12mo']]
def approx_month(age):
    a = age_months(age)
    # today 2026-10-24
    d = datetime.date(2026, 10, 24) - datetime.timedelta(days=a * 30.4)
    return d
buckets = collections.defaultdict(list)
for v in R:
    d = approx_month(v['age']); buckets[(d.year, d.month)].append(v)
print("heat last-12-month uploads by approx month (from age text):")
for k in sorted(buckets):
    vs = buckets[k]
    print(f"  {k[0]}-{k[1]:02d}: {len(vs)} videos, median {fmt(med([v['views_n'] for v in vs]))}, top {fmt(max(v['views_n'] for v in vs))}")
sd = [v for v in R if approx_month(v['age']).month in SEP_DEC]; ot = [v for v in R if approx_month(v['age']).month not in SEP_DEC]
print(f"  Sep-Dec (approx) {len(sd)} median {fmt(med([v['views_n'] for v in sd]))}; Jan-Aug {len(ot)} median {fmt(med([v['views_n'] for v in ot]))}")
# exclude last 4 weeks (too new)
sd2 = [v for v in sd if age_months(v['age']) >= 1]
print(f"  Sep-Dec excluding uploads <1 month old: {len(sd2)} median {fmt(med([v['views_n'] for v in sd2]))}")
json.dump(out, open(S + 'dates.json', 'w'))
