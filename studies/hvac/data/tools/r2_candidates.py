#!/usr/bin/env python3
"""Round 2 (2026-10-24): merge every saved NexLev result in <scratch>/index.json into one record per channel
that is NOT in round 1's lists (<scratch>/known.json), score HVAC relevance from name, description and recent titles,
and write <scratch>/candidates.json. Usage: python3 -I r2_candidates.py <scratch>"""
import json, sys, re
sd = sys.argv[1]
idx = json.load(open(sd + '/index.json'))
known = json.load(open(sd + '/known.json')); kids = set(known['ids']); kn = set(known['names']); kh = set(known['handles'])
HV = re.compile(r"hvac|furnace|heat pump|boiler|radiator|thermostat|mini.?split|air.?condition|\ba/?c\b|insulat|energy bill|heating|electric bill|power bill|utility bill|heat(ing)? bill|dehumidif|humidif|duct|refrigerant|freon|capacitor|condenser|wood stove|pellet stove|space heater|keep(s)? (you|your house|the house|a room|any room) (warm|cool)|stay warm|without (heat|power|electricity)|power outage|blackout|draft|weatherstrip|cool(s|ing)? (your|the|a) (house|home|room)|heat(s|ing)? (your|the|a|any) (house|home|room)|swamp cooler|evaporative|whole.house fan|attic fan|home energy|energy audit|propane|heating oil|oil burner|kerosene", re.I)
OFF = re.compile(r"ancient|medieval|viking|inuit|igloo|samurai|roman|pirate|tartarian|cold case|gaming|\bpc\b|laptop|gpu|car|truck|engine|vehicle|motorcycle|tesla|audi|honda|toyota|chevy|ford|jeep|rv\b|camper|van life|homeless|blizzard story|mocked|laughed|widow|she built|he built|until winter|bushcraft|camping|tent", re.I)
recs = {}
def add(cid, kind, label, rec):
    if not cid: return
    e = recs.setdefault(cid, {"cid": cid, "found_by": [], "nf": None, "sim": None, "vids": []})
    if label not in e['found_by']: e['found_by'].append(label)
    if kind in ('nf',) and not e['nf']: e['nf'] = rec
    if kind == 'sim' and not e['sim']: e['sim'] = rec
    if kind in ('fo', 'vir'): e['vids'].append(rec)
for it in idx:
    raw = json.load(open(it['file']))
    js = None
    for p in raw if isinstance(raw, list) else []:
        t = p.get('text', '')
        if t.strip()[:1] in '{[':
            try: js = json.loads(t)
            except Exception: pass
    if not js: continue
    rows = js.get('channels') or js.get('videos') or []
    for c in rows:
        if 'about' in c:
            add(c['about'].get('channelId'), 'sim', it['label'], c)
        elif it['kind'] == 'nf':
            add(c.get('ytChannelId'), 'nf', it['label'], c)
        elif it['kind'] in ('fo', 'vir'):
            add(c.get('ytChannelId'), it['kind'], it['label'], c)
# viral rows recorded by hand from inline results
for line in open(sd + '/viral_rows.jsonl'):
    r = json.loads(line)
    if r.get('ytChannelId'): add(r['ytChannelId'], 'vir', 'viral_small: ' + r['query'], {"videoId": r['videoId'], "videoTitle": r['title'], "videoViews": r['videoViews'], "videoPublishedAt": r['publishedAt'], "channelTitle": r['channelTitle'], "channelUsername": r['channelUsername'], "channelSubCount": r['channelSubCount'], "isAiContent": r['isAiContent']})
out = []
for cid, e in recs.items():
    nf, sim = e['nf'], e['sim']
    name = (nf or {}).get('title') or ((sim or {}).get('about') or {}).get('channelName') or (e['vids'][0].get('channelTitle') if e['vids'] else '')
    handle = ('@' + nf['username']) if nf and nf.get('username') else (e['vids'][0].get('channelUsername') if e['vids'] else '')
    if cid in kids or (name or '').lower() in kn or (handle or '').lower() in kh: continue
    desc = (nf or {}).get('description') or ((sim or {}).get('about') or {}).get('description') or ''
    titles = [v.get('video_title', '') for v in (nf or {}).get('lastUploadedVideos') or []] + [v.get('videoTitle', '') for v in e['vids']]
    tags = ' '.join((sim or {}).get('tags') or [])
    blob_t = ' | '.join(titles)
    hits_t = sum(1 for t in titles if HV.search(t))
    hit_name = bool(HV.search(name or ''))
    hit_desc = len(HV.findall(desc + ' ' + tags))
    off = len(OFF.findall((name or '') + ' ' + desc[:500] + ' ' + blob_t))
    score = hits_t * 2 + (3 if hit_name else 0) + min(hit_desc, 5) - off
    e.update(name=name, handle=handle, desc=desc, titles=titles, score=score, hits_t=hits_t, hit_desc=hit_desc, off=off)
    out.append(e)
out.sort(key=lambda e: -e['score'])
json.dump(out, open(sd + '/candidates.json', 'w'), indent=1)
print(len(out), 'new channels in raw results;', sum(1 for e in out if e['score'] >= 3), 'with score >= 3')
