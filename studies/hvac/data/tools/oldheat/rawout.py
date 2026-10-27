exec(open('/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/tables.py').read().split('print("## pool")')[0])
import glob
searches = [json.loads(l) for l in open(S + 'search.jsonl')]
oe = [json.loads(l) for l in open(S + 'oembed.jsonl')]
tabs = {}
for f in glob.glob(S + 'tabs/*.json'): d = json.load(open(f)); tabs[d['id']] = d
dates = []
for l in open(S + 'dates.txt'):
    p = [x.strip() for x in l.split('|')]
    dates.append({"id": p[0], "line": l.strip()})
def pool(key):
    out = []
    for v in jsonable(res[key]['vids']):
        d = {k: v[k] for k in ('id','title','orig_title','translated','channel','channelId','handle','views','views_n','age','recent_12mo','length','secs','keywords','sorts')}
        d['collab'] = v.get('collab'); d['channel_country'] = ctry(v['channelId'])
        out.append(d)
    return out
raw = {
 "pulled": "2026-10-24 (UTC timestamps on each record)",
 "helper": "round 2 old-house heat helper",
 "source": "Logged-out YouTube search (hl=en, gl=US) via studies/hvac/data/tools/oldheat_search.py (search() copied from sweep_round2.py); 2 result pages per search; sorts relevance, views, year, month. Original titles from youtube.com/oembed. Channel country/subs/joined from each channel's About panel (yt_water1.py about). Channel Videos tabs from yt_allsorts.py (5 pages per chip). Upload dates for the top 120 heat and top 60 AC videos from innertube /next (vid.py). No NexLev data used.",
 "filters": {
   "long_form": "length text >= 5:00",
   "english": "original (oEmbed) title, search title and channel name all pass a script/diacritic/foreign-word check (search titles are auto-translated for logged-out hl=en; oEmbed gives the original)",
   "on_topic_heat": "title matches radiator/boiler/steam heat/hydronic/baseboard (hot-water)/circulator/zone valve/expansion tank (with heating context)/oil furnace-burner-boiler-tank/heating oil/gravity or octopus furnace/old-house heating; excludes cars and motorbikes, sleep sounds, industrial and power-plant boilers, waste-oil and off-grid DIY heaters, wood boilers, radiant floor/slab, garage/shop/van heat, electric baseboard, water-heater expansion tanks, gaming, music",
   "on_topic_ac": "title matches AC / A/C / HVAC / air condition* / mini split / ductless / condenser / evaporator / capacitor (with AC context) / central air / thermostat / heat pump / compressor / air or furnace filter / refrigerant; excludes cars, electronics capacitors, fridges",
   "last_12_months": "age text in hours/days/weeks/months (YouTube shows 12+ months as '1 year ago')",
   "matched_heat_keywords": MATCHED_HEAT},
 "keywords": {"heat": res['heat']['keywords'], "ac": res['ac']['keywords']},
 "funnel": {k: res[k]['funnel'] for k in ('heat','heat_matched','ac')},
 "summary": {k: res[k]['summary'] for k in ('heat','heat_matched','ac')},
 "per_keyword": {"heat": res['heat']['per_kw'], "ac": res['ac']['per_kw']},
 "pool_heat": pool('heat'), "pool_heat_matched_ids": [v['id'] for v in jsonable(res['heat_matched']['vids'])], "pool_ac": pool('ac'),
 "channel_about": A,
 "channel_multiples": json.load(open(S + 'mult.json')),
 "channel_tabs": tabs,
 "upload_dates_innertube": dates,
 "oembed_titles": oe,
 "searches": searches,
}
p = '/home/user/niche-research/studies/hvac/data/raw/round2-oldheat-2026-10-24.json'
json.dump(raw, open(p, 'w'), indent=0, ensure_ascii=False)
import os; print(os.path.getsize(p))
