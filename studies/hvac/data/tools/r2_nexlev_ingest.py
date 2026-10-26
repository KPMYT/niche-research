#!/usr/bin/env python3
"""Round 2 (2026-10-24) NexLev channel widening: ingest one saved NexLev tool result.
Usage: python3 -I r2_nexlev_ingest.py <scratchdir> <kind> <label> <saved_result_file_or_->
kind: nf (niche finder), sim (similar channels status), vir (viral small channels), fo (faceless outliers), lat (latest faceless)
Copies the saved result into <scratchdir>/raw/<n>-<kind>.json, appends to <scratchdir>/index.json,
and prints channels NOT in <scratchdir>/known.json whose name/description/last titles have an HVAC word."""
import json, sys, os, re, shutil
sd, kind, label, src = sys.argv[1:5]
os.makedirs(sd + '/raw', exist_ok=True)
idx_p = sd + '/index.json'
idx = json.load(open(idx_p)) if os.path.exists(idx_p) else []
n = len(idx) + 1
dst = f"{sd}/raw/{n:03d}-{kind}.json"
if src == '-':
    open(dst, 'w').write(sys.stdin.read())
else:
    shutil.copy(src, dst)
idx.append({"n": n, "kind": kind, "label": label, "file": dst, "src": src})
json.dump(idx, open(idx_p, 'w'), indent=1)
known = json.load(open(sd + '/known.json'))
kids = set(known['ids']); kh = set(known['handles']); kn = set(known['names'])
seen_p = sd + '/seen_new.json'
seen = json.load(open(seen_p)) if os.path.exists(seen_p) else {}
raw = json.load(open(dst))
js = None
if isinstance(raw, list):
    for p in raw:
        t = p.get('text', '') if isinstance(p, dict) else ''
        if t.strip().startswith('{') or t.strip().startswith('['):
            try: js = json.loads(t)
            except Exception: pass
else:
    js = raw
KW = re.compile(r"hvac|air.?condition|\bac\b|a/c|furnace|heat|cool|thermostat|filter|duct|boiler|radiator|insulat|draft|energy|electric bill|bill|humid|mini.?split|stove|propane|outage|winter|warm|capacitor|coil|refrigerant|freon|vent|attic|weatherstrip|chimney|fireplace|pellet|kerosene|off.?grid|cold|freez|frost", re.I)
CAR = re.compile(r"\b(car|cars|auto|automotive|vehicle|honda|toyota|chevy|chevrolet|ford|nissan|dodge|bmw|engine|truck|refrigerator|washer|dryer|dishwasher|iphone|tv)\b", re.I)
HV = re.compile(r"hvac|furnace|heat pump|boiler|radiator|thermostat|mini.?split|home heating|house warm|insulat|energy bill|heating bill|electric bill", re.I)
def chans(js):
    if js is None: return []
    if isinstance(js, list): return js
    for k in ('channels', 'results', 'data', 'similarChannels', 'videos', 'items'):
        v = js.get(k)
        if isinstance(v, list): return v
        if isinstance(v, dict):
            r = chans(v)
            if r: return r
    return []
rows = chans(js)
print(f"#{n} {kind} '{label}': {len(rows)} rows; total={js.get('totalResults') if isinstance(js,dict) else ''}")
newhits = 0
for c in rows:
    if 'about' in c and isinstance(c['about'], dict):
        a = c['about']
        c = dict(c, ytChannelId=a.get('channelId'), title=a.get('channelName'), description=(a.get('description') or '') + ' ' + ' '.join(c.get('tags') or []), stats={'subscribers': a.get('subscriberCount')}, channelCreationDate=(a.get('joinedDate') or '')[:10], editingStyle='sim%s' % c.get('similarityScore'), outlierScore=None, channelLanguage=a.get('country'))
    cid = c.get('ytChannelId') or c.get('channelId') or c.get('channel_id') or c.get('ytChannelID')
    name = c.get('title') if kind in ('nf', 'sim', 'lat') else (c.get('channelTitle') or c.get('channelName') or c.get('channel_title'))
    name = name or c.get('channelTitle') or c.get('title')
    uname = (c.get('username') or c.get('channelHandle') or '').lower().lstrip('@')
    if cid in kids or ('@' + uname) in kh or (name or '').lower() in kn: continue
    titles = ' | '.join(v.get('video_title', '') for v in (c.get('lastUploadedVideos') or [])[:5])
    vt = c.get('videoTitle') or c.get('video_title') or c.get('title') if kind in ('vir', 'fo') else ''
    blob = f"{name} {c.get('description','')[:400]} {titles} {vt}"
    if not KW.search(blob): continue
    if os.environ.get('STRICT') and not HV.search(blob): continue
    if CAR.search(blob) and not HV.search(blob): continue
    newhits += 1
    st = c.get('stats', {})
    first = cid not in seen
    seen.setdefault(cid, {"name": name, "found_by": []})
    if label not in seen[cid]['found_by']: seen[cid]['found_by'].append(label)
    if not first: continue
    if kind in ('vir', 'fo'):
        print(f"  {'NEW ' if first else '    '}{cid} | {name} | subs {c.get('channelSubCount') or c.get('subscribers')} | VID {c.get('videoId') or c.get('ytVideoId')} {c.get('videoViews') or c.get('views')} v | o{round(c.get('outlierScore') or 0,1)} | {(c.get('videoPublishedAt') or c.get('publishedAt') or '')[:10]} | {vt[:85]}")
    else:
        print(f"  {cid} | {name} | {st.get('subscribers')} | {c.get('channelCreationDate')} | {c.get('editingStyle')} | o{c.get('outlierScore')} | {c.get('channelLanguage')} | {titles[:75]}")
json.dump(seen, open(seen_p, 'w'), indent=1)
print(f"  -> {newhits} new HVAC-word rows; {len(seen)} new candidates so far")
