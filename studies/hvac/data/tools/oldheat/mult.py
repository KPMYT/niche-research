exec(open('/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/build.py').read().split('rows = [json.loads')[0])
import glob
out = {}
for f in sorted(glob.glob(S + 'tabs/*.json')):
    d = json.load(open(f))
    seen = {}; 
    for chip in ('Latest_initialpage', 'Latest', 'Popular', 'Oldest'):
        for v in (d['sorts'].get(chip) or []):
            if v['id'] not in seen: seen[v['id']] = dict(v, chip=chip)
    lat = []
    ids = set()
    for chip in ('Latest_initialpage', 'Latest'):
        for v in (d['sorts'].get(chip) or []):
            if v['id'] in ids: continue
            ids.add(v['id']); lat.append(v)
    def age(v):
        for p in v['meta']:
            a = age_months(p)
            if a is not None: return a, p
        return None, None
    def lf(v): s = secs(v.get('dur')); return s is not None and s >= 300
    lflat = [v for v in lat if lf(v)]
    last12 = [v for v in lflat if (age(v)[0] is not None and age(v)[0] < 12)]
    if len(last12) >= 10: base, rule = last12, 'long-form uploads in last 12 months (Latest tab)'
    else: base, rule = lflat[:30], 'last 30 long-form uploads (fewer than 10 in last 12 months)'
    bm = med([v['views_tab'] for v in base if v['views_tab'] is not None])
    allv = list(seen.values())
    heat = [v for v in allv if lf(v) and topical('heat', v['title'] or '', d['channel'])]
    heat_in_base = [v for v in base if topical('heat', v['title'] or '', d['channel'])]
    nonheat_in_base = [v for v in base if not topical('heat', v['title'] or '', d['channel'])]
    rows = sorted([(v['views_tab'] / bm if bm and v['views_tab'] is not None else None, v) for v in heat], key=lambda x: -(x[0] or 0))
    out[d['channel']] = dict(channelId=d['id'], subs=d['subs'], videos=d['videos'], pulled=d['pulled'], rule=rule, base_n=len(base), base_median=bm,
        latest_n=len(lat), latest_longform=len(lflat), last12_longform=len(last12),
        heat_in_base_n=len(heat_in_base), heat_in_base_median=med([v['views_tab'] for v in heat_in_base if v['views_tab'] is not None]),
        nonheat_in_base_n=len(nonheat_in_base), nonheat_in_base_median=med([v['views_tab'] for v in nonheat_in_base if v['views_tab'] is not None]),
        heat_all_n=len(heat), heat_multiples=[dict(id=v['id'], title=v['title'], views_tab=v['views_tab'], age=age(v)[1], dur=v.get('dur'), multiple=round(m, 2) if m else None) for m, v in rows])
    o = out[d['channel']]
    hm = [x['multiple'] for x in o['heat_multiples'] if x['multiple'] is not None]
    hb = [v['views_tab'] / bm for v in heat_in_base if bm and v['views_tab'] is not None]
    o['heat_all_median_multiple'] = round(med(hm), 2) if hm else None
    o['heat_all_share_2x'] = f"{sum(x >= 2 for x in hm)}/{len(hm)}"
    o['heat_in_base_median_multiple'] = round(med(hb), 2) if hb else None
    o['heat_in_base_share_2x'] = f"{sum(x >= 2 for x in hb)}/{len(hb)}"
    print(d['channel'], {k: o[k] for k in ('subs','videos','rule','base_n','base_median','latest_n','latest_longform','last12_longform','heat_in_base_n','heat_in_base_median','nonheat_in_base_n','nonheat_in_base_median','heat_all_n','heat_all_median_multiple','heat_all_share_2x','heat_in_base_median_multiple','heat_in_base_share_2x')})
    for x in o['heat_multiples'][:6]: print('   ', x['multiple'], x['views_tab'], x['age'], x['dur'], x['title'][:70])
json.dump(out, open(S + 'mult.json', 'w'), indent=1)
