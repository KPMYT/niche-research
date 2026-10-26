#!/usr/bin/env python3
"""Round 3 'what it sells': tables for round3/sells.md from census-sells CSV + review JSON + descriptions.
Usage: python3 -I sells_report.py <sells.csv> <review.json> <desc.jsonl> > fragments.md"""
import sys, csv, json, re, collections

rows = list(csv.DictReader(open(sys.argv[1])))
review = json.load(open(sys.argv[2]))['channels']
descs = collections.defaultdict(list)
for l in open(sys.argv[3]):
    j = json.loads(l)
    descs[j['channel_id']].append(j)
by = {r['channel_id']: r for r in rows}
CATS = ['own_product', 'book_ebook_guide', 'course', 'free_lead_magnet', 'membership', 'tips', 'merch', 'affiliate',
        'sponsor', 'consulting', 'app', 'newsletter', 'contractor', 'affiliate_disclosure', 'not found', 'not pulled']


def cats(r):
    return set(r['sells_categories'].split(' ; '))


def persona(r):
    return r['persona_flag'] == 'yes' or r['type'] in ('faceless persona', 'AI avatar')


def subs(r):
    try:
        return int(r['subs'])
    except ValueError:
        return -1


print('## Counts per category\n')
print('| Category | All A-D (1,122) | A | B | C | D | Personas* |')
print('|---|---|---|---|---|---|---|')
tiers = collections.Counter(r['tier'] for r in rows)
npers = sum(persona(r) for r in rows)
for c in CATS:
    n = [sum(c in cats(r) for r in rows)] + [sum(c in cats(r) for r in rows if r['tier'] == t) for t in 'ABCD'] + \
        [sum(c in cats(r) for r in rows if persona(r))]
    print(f'| {c} | ' + ' | '.join(str(x) for x in n) + ' |')
print(f'| (channels) | {len(rows)} | ' + ' | '.join(str(tiers[t]) for t in 'ABCD') + f' | {npers} |')
print()
print('## Own products (paid), every channel\n')
print('| Tier | Channel | Type | Subs | Product (as written) | Kind | Price (as shown) | Link domain |')
print('|---|---|---|---|---|---|---|---|')
own_rows = []
for cid, v in review.items():
    r = by.get(cid)
    if not r:
        continue
    for p in v.get('own_products_detail', []):
        if p.get('free'):
            continue
        own_rows.append((r['tier'], -subs(r), r['name'], r['type'] + (' (persona flag)' if r['persona_flag'] == 'yes' else ''),
                         r['subs'], p))
own_rows.sort(key=lambda x: (x[0], x[1], x[2]))
BOOKISH = re.compile(r'book|guide|manual|pdf|journal|playbook|binder|course|class|workshop|coaching|community|price book', re.I)
esc = lambda s: str(s).replace('|', '/')
main = [x for x in own_rows if BOOKISH.search(x[5]['kind'])]
other = [x for x in own_rows if not BOOKISH.search(x[5]['kind'])]
for t, _, n, ty, sb, p in main:
    print(f"| {t} | {esc(n)} | {esc(ty)} | {sb} | {esc(p['name'])} | {esc(p['kind'])} | {esc(p['price'])} | {esc(p['domain'])} |")
print(f'\n{len(main)} book/e-book/guide/course products on {len(set(x[2] for x in main))} channels.\n')
print('## Other own products (plans, physical, spreadsheets, apps, music)\n')
print('| Tier | Channel | Product | Kind | Price | Domain |')
print('|---|---|---|---|---|---|')
for t, _, n, ty, sb, p in other:
    print(f"| {t} | {esc(n)} | {esc(p['name'])} | {esc(p['kind'])} | {esc(p['price'])} | {esc(p['domain'])} |")
print(f'\n{len(other)} other products on {len(set(x[2] for x in other))} channels.\n')
print('## Free lead magnets\n')
for cid, v in review.items():
    r = by.get(cid)
    for p in v.get('own_products_detail', []):
        if p.get('free') and r:
            print(f"- {r['tier']} {r['name']}: {p['name']} ({p['domain']})")
print()
# platforms
plat = collections.Counter()
for t, _, n, ty, sb, p in own_rows:
    d = p['domain'].lower()
    for k in ['gumroad', 'payhip', 'stan.store', 'netlify', 'vercel', 'pages.dev', 'liibro', 'etsy', 'thinkific', 'teachable',
              'skool', 'shopify', 'stripe', 'amazon', 'amzn', 'a.co', 'kajabi', 'systeme', 'myreads']:
        if k in d:
            plat[k] += 1
print('## Checkout / hosting seen in product links:', dict(plat.most_common()), '\n')
# prices (USD, first $ figure) for persona-type e-books
pp = []
for t, _, n, ty, sb, p in own_rows:
    m = re.search(r'\$\s?(\d+(?:\.\d\d)?)', p['price'])
    if m and re.search(r'book|guide|manual|journal|playbook|binder', p['kind'], re.I):
        pp.append((float(m.group(1)), n, 'persona' in ty or 'faceless' in ty or 'AI' in ty))
if pp:
    v = sorted(x[0] for x in pp)
    print(f'## E-book prices (first $ figure shown, {len(v)} products): min {v[0]}, median {v[len(v)//2]}, max {v[-1]}')
    c = collections.Counter(v)
    print('Most common:', c.most_common(8), '\n')
# affiliate retailers
aff = collections.Counter()
for r in rows:
    for part in r['affiliate_domains'].split(' ; '):
        m = re.match(r'(.*) \((\d+)\)$', part)
        if m:
            aff[m.group(1)] += 1
print('## Affiliate domains (channels with at least one link):', aff.most_common(30), '\n')
RET = ['alpinehomeair', 'supplyhouse', 'hvacdirect', 'ecomfort', 'acwholesalers', 'filterbuy', 'sylvane', 'trutechtools',
       'hvactactical', 'pexsupply', 'pexuniverse', 'homedepot', 'home depot', 'lowes', "lowe's", 'walmart', 'ebay', 'signaturesolar',
       'signature solar', 'ecoflow', 'jackery', 'bluetti', 'mrcool', 'pioneer', 'fieldpiece', 'navac', 'klein', 'milwaukee',
       'harbor freight', 'harborfreight', 'acpro', 'amazon', 'amzn', 'geni.us', 'kit.co', 'tubebuddy', 'vidiq', 'epidemic sound',
       'epidemicsound', 'incogni', 'nordvpn', 'skillshare', 'audible', 'raycon', 'squarespace', 'coursecareers', 'getjobber', 'jobber']
men = collections.Counter()
for cid, vs in descs.items():
    t = ' '.join((v.get('description') or '') + ' ' + ' '.join(k['url'] for k in v.get('links', [])) for v in vs).lower()
    for k in RET:
        if k in t:
            men[k] += 1
print('## Retailer/brand names mentioned anywhere in the pulled descriptions (channels):', men.most_common(), '\n')
# persona summary
print('## Personas (persona_flag yes or type faceless persona / AI avatar)\n')
pc = collections.Counter()
for r in rows:
    if persona(r):
        for c in cats(r):
            pc[c] += 1
print('Category counts:', pc.most_common(), '\n')
print('| Tier | Channel | Type | Subs | Sells | Own product(s) |')
print('|---|---|---|---|---|---|')
for r in sorted([r for r in rows if persona(r)], key=lambda r: (r['tier'], -subs(r))):
    c = ' ; '.join(x for x in r['sells_categories'].split(' ; ') if x not in ('own_website', 'affiliate_disclosure'))
    print(f"| {r['tier']} | {r['name']} | {r['type']} | {r['subs']} | {c or 'not found'} | {r['own_products'].replace('|', '/')[:220]} |")
