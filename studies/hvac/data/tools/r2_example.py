#!/usr/bin/env python3
"""Round 2: pick one example HVAC/heat video per kept channel from its channel-page pull (5 min+, strict topic words,
highest views); falls back to NexLev lastUploadedVideos or outlier/viral rows. Usage: python3 -I r2_example.py <scratch> -> <scratch>/examples.json"""
import json, sys, glob, re
sd = sys.argv[1]
kept = json.load(open(sd + '/kept.json')); cands = {e['cid']: e for e in json.load(open(sd + '/candidates.json'))}
STRICT = re.compile(r"hvac|furnace|heat pump|boiler|radiator|thermostat|mini.?split|air.?condition|\ba/?c\b|ac unit|insulat|\bbills?\b|dehumidif|humidif|duct|refrigerant|freon|capacitor|condenser|compressor|evaporator|coil|stove|heater|heat(s|ing)?\b|warm|cool(s|ing)? (our|your|the|a|any|an)|without (ac|a\.c|air|power|electricity|heat)|blackout|power outage|power goes out|grid (dies|fails|goes)|draft|weatherstrip|attic|propane|kerosene|chimney|firewood|wood\b|filter|vent", re.I)
NOT = re.compile(r"water heater|tankless|refrigerator|fridge|freezer|dryer|washer|dishwasher|\bcar\b|truck|engine|lexus|mercedes|\btv\b|remote|pool heater|livestock|barn", re.I)
def secs(d):
    try:
        s = 0
        for x in (d or '').split(':'): s = s * 60 + int(x)
        return s
    except Exception: return 0
out = {}
for cid in kept:
    vids = {}
    for f in glob.glob(sd + f'/pages0*/{cid}.json'):
        pg = json.load(open(f))
        for k in ('popular', 'latest'):
            for v in pg.get(k) or []: vids.setdefault(v['id'], dict(v, src=f'YouTube Videos tab ({k}), loaded 2026-10-24'))
    ok = [v for v in vids.values() if secs(v.get('dur')) >= 300 and STRICT.search(v['title']) and not NOT.search(v['title'])]
    if not ok: ok = [v for v in vids.values() if secs(v.get('dur')) >= 300 and re.search(r'\bwinter\b', v['title'], re.I) and not NOT.search(v['title'])]
    best = max(ok, key=lambda v: v.get('views') or 0) if ok else None
    if not best:
        e = cands.get(cid) or {}
        rows = [dict(id=v.get('video_id'), title=v.get('video_title'), views=v.get('video_view_count'), dur=v.get('length_text'), src='NexLev lastUploadedVideos, pulled 2026-10-24') for v in ((e.get('nf') or {}).get('lastUploadedVideos') or [])]
        rows += [dict(id=v.get('videoId'), title=v.get('videoTitle'), views=v.get('videoViews'), dur=str(v.get('videoLengthSeconds') or ''), src='NexLev faceless_outliers / viral_small, pulled 2026-10-24') for v in e.get('vids') or []]
        rows = [r for r in rows if r['title'] and STRICT.search(r['title']) and not NOT.search(r['title'])]
        best = max(rows, key=lambda v: v.get('views') or 0) if rows else None
    out[cid] = best
json.dump(out, open(sd + '/examples.json', 'w'), indent=1)
print(sum(1 for v in out.values() if v), 'of', len(out), 'with an example')
for cid, v in out.items():
    if not v: print('NO EXAMPLE', kept[cid]['name'])
