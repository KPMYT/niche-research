#!/usr/bin/env python3
"""Round 2: summarise the channel-page pull (about_batch.py output) for each pick.
Usage: python3 -I r2_pages_summary.py <scratch>  -> writes <scratch>/pages_summary.json and prints one block per pick."""
import json, sys, glob, re, os
sd = sys.argv[1]
picks = json.load(open(sd + '/picks.json'))
about = {}
for f in glob.glob(sd + '/pages0*/about.json'): about.update(json.load(open(f)))
HV = re.compile(r"hvac|furnace|heat pump|boiler|radiator|thermostat|mini.?split|air.?condition|\ba/?c\b|insulat|energy bill|heating|electric bill|power bill|heat bill|dehumidif|humidif|duct|refrigerant|freon|capacitor|condenser|coil|compressor|wood stove|pellet stove|space heater|warm|heat(s|ing)?\b|cool(s|ing)?\b|blackout|power outage|draft|weatherstrip|swamp cooler|attic|propane|kerosene|filter|vent", re.I)
def secs(d):
    try:
        p = [int(x) for x in (d or '').split(':')]
        s = 0
        for x in p: s = s * 60 + x
        return s
    except Exception: return None
out = {}
for cid, p in picks.items():
    a = about.get(cid, {})
    pg = None
    for f in glob.glob(sd + f'/pages0*/{cid}.json'):
        try: pg = json.load(open(f))
        except Exception: pass
    vids = {}
    for k in ('popular', 'latest'):
        for v in (pg or {}).get(k) or []:
            v = dict(v); v['tab'] = k; vids.setdefault(v['id'], v)
    vl = list(vids.values())
    lf = [v for v in vl if (secs(v.get('dur')) or 0) >= 300]
    hv = [v for v in lf if HV.search(v.get('title') or '')]
    best = max(hv, key=lambda v: v.get('views') or 0) if hv else None
    out[cid] = {"about": a, "n_loaded": len(vl), "n_long": len(lf), "n_long_hvac": len(hv), "best_hvac": best,
                "top": sorted(vl, key=lambda v: -(v.get('views') or 0))[:4], "pop_loaded": bool((pg or {}).get('popular'))}
json.dump(out, open(sd + '/pages_summary.json', 'w'), indent=1)
for cid, s in out.items():
    p = picks[cid]
    if len(sys.argv) > 2 and sys.argv[2] == 'undecided' and p['fit'] != '?': continue
    a = s['about']
    b = s['best_hvac']
    print(f"{cid}|{p['name'][:30]}|{p['fit']}|{a.get('subscriberCountText','')}|{a.get('viewCountText','')}|{a.get('joinedDateText','')}|{a.get('videoCountText','')}|{a.get('country','')}|long {s['n_long']}/{s['n_loaded']} hvac {s['n_long_hvac']}")
    print("   top:", ' || '.join(f"{v['title'][:50]} ({v.get('views')}, {v.get('dur')})" for v in s['top'][:3]))
    if b: print("   best HVAC:", b['title'][:80], b.get('views'), b.get('dur'), b['id'])
