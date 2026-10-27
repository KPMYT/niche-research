#!/usr/bin/env python3
"""Round 2 (2026-10-24) NexLev channel widening: build the outputs.
Usage: python3 -I r2_build.py <scratch> <out_csv> <out_raw_json>
Joins kept.json (readings), the NexLev records (candidates.json), the YouTube About/Videos pull (pages_summary.json),
examples.json and r2_types.py, and writes the CSV and a compact raw JSON of every NexLev call. Prints tables for the .md."""
import json, sys, csv, re, os, glob
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from r2_types import T, LABEL
sd, out_csv, out_raw = sys.argv[1:4]
kept = json.load(open(sd + '/kept.json')); dropped = json.load(open(sd + '/dropped.json'))
cands = {e['cid']: e for e in json.load(open(sd + '/candidates.json'))}
pages = json.load(open(sd + '/pages_summary.json')); ex = json.load(open(sd + '/examples.json'))
idx = json.load(open(sd + '/index.json'))
def num(t):
    m = re.match(r'([\d.,]+)\s*([KM]?)', (t or '').replace(',', ''))
    if not m: return None
    v = float(m.group(1)); return int(round(v * {'': 1, 'K': 1e3, 'M': 1e6}[m.group(2)]))
def short(lbl):
    return lbl.replace('similar: ', 'similar-of ').replace('[videoType=long; total None]', '[long]')
rows = []
for cid, p in kept.items():
    e = cands.get(cid) or {}; nf = e.get('nf') or {}; st = nf.get('stats') or {}
    a = (pages.get(cid) or {}).get('about') or {}
    title = a.get('TITLE', '')
    handle = (re.search(r'youtube\.com/(@[^\s|]+)', title) or [None, None])[1] or (('@' + nf['username']) if nf.get('username') else '') or e.get('handle') or ''
    v = ex.get(cid) or {}
    top = ((pages.get(cid) or {}).get('top') or [{}])[0]
    joined = (a.get('joinedDateText') or '').replace('Joined ', '')
    fb = e.get('found_by') or [p.get('src')]
    rows.append({
        'name': p['name'].strip(), 'handle': handle, 'channel_id': cid, 'link': f'https://www.youtube.com/channel/{cid}',
        'type': LABEL.get(T[p['name'].strip()], T[p['name'].strip()]) + ' (my reading)',
        'nexlev_faceless_flag': nf.get('isFaceless', 'not in NexLev niche-finder results'), 'nexlev_ai_flag': nf.get('isAiChannel', ''),
        'nexlev_editing_style': nf.get('editingStyle') or '', 'nexlev_editing_voice': nf.get('editingVoice') or '',
        'persona_background': p['note'], 'audience': p['audience'] + ' (reading)', 'fit': p['fit'] + ' (reading)',
        'subs': num(a.get('subscriberCountText')) if a.get('subscriberCountText') else (st.get('subscribers') if st.get('subscribers') is not None else 'not found'),
        'subs_source': 'YouTube About 2026-10-24 (rounded as shown)' if a.get('subscriberCountText') else ('NexLev 2026-10-24' if st.get('subscribers') is not None else ''),
        'total_views': num(a.get('viewCountText')) if a.get('viewCountText') else (st.get('totalViews') or 'not found'),
        'joined': joined or (nf.get('channelCreationDate') or 'not found'), 'video_count': num(a.get('videoCountText')) if a.get('videoCountText') else (st.get('totalVideos') or 'not found'),
        'country': a.get('country') or nf.get('location') or '', 'nexlev_first_video': st.get('firstVideoDate') or '', 'nexlev_created': nf.get('channelCreationDate') or '',
        'nexlev_outlier_score': nf.get('outlierScore') if nf else 'not found', 'nexlev_monthly_views': st.get('monthlyViews') or '',
        'nexlev_monthly_revenue_usd_estimate_RPM_based_NOT_USED': st.get('monthlyRevenue') or '',
        'example_title': v.get('title', 'not found'), 'example_id': v.get('id', ''), 'example_views': v.get('views', ''), 'example_duration': v.get('dur', ''), 'example_source': v.get('src', ''),
        'top_video_title': top.get('title', ''), 'top_video_id': top.get('id', ''), 'top_video_views': top.get('views', ''),
        'long_videos_loaded': (pages.get(cid) or {}).get('n_long', ''), 'long_heat_cool_videos_loaded': (pages.get(cid) or {}).get('n_long_hvac', ''),
        'found_by': ' ; '.join(short(x) for x in fb), 'date_pulled': '2026-10-24'})
rows.sort(key=lambda r: -(r['subs'] if isinstance(r['subs'], int) else -1))
with open(out_csv, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
# compact raw JSON of every NexLev call
calls = []
def compact_nf(c):
    st = c.get('stats') or {}
    return {k: c.get(k) for k in ('ytChannelId', 'title', 'username', 'location', 'channelLanguage', 'channelCreationDate', 'isFaceless', 'isAiChannel', 'editingStyle', 'editingVoice', 'outlierScore', 'quality', 'tags')} | {
        'stats': {k: st.get(k) for k in ('subscribers', 'totalViews', 'totalVideos', 'avgViewsPerVideo', 'medianViewsPerVideo', 'avgVideoLength', 'uploadsPerWeek', 'firstVideoDate', 'lastVideoDate', 'monthlyViews')},
        'monthlyRevenue_NexLev_estimate_RPM_based_not_used': st.get('monthlyRevenue'), 'description': (c.get('description') or '')[:600],
        'lastUploadedVideos': [{k: v.get(k) for k in ('video_id', 'video_title', 'video_view_count', 'video_upload_date', 'length_text')} for v in (c.get('lastUploadedVideos') or [])]}
def compact_sim(c):
    a = c.get('about') or {}
    return {'similarityScore': c.get('similarityScore'), 'tags': c.get('tags'), 'about': {k: a.get(k) for k in ('channelId', 'channelName', 'channelUrl', 'country', 'subscriberCount', 'viewCount', 'videoCount', 'joinedDate', 'avgVideoLength', 'avgVideoLengthSeconds', 'lastVideoUploadDate', 'hasShorts')} | {'description': (a.get('description') or '')[:600]}}
for it in idx:
    raw = json.load(open(it['file'])); js = None
    for prt in raw if isinstance(raw, list) else []:
        t = prt.get('text', '')
        if t.strip()[:1] in '{[':
            try: js = json.loads(t)
            except Exception: pass
    tool = {'nf': 'search_niche_finder_channels', 'sim': 'get_similar_channels (+_status)', 'fo': 'faceless_outliers_videos', 'lat': 'latest_discovered_faceless_niches'}[it['kind']]
    rec = {'n': it['n'], 'tool': tool, 'label': it['label'], 'filters': (js or {}).get('filters'), 'pulled': '2026-10-24'}
    rs = (js or {}).get('channels') or (js or {}).get('videos') or []
    rec['n_results'] = len(rs); rec['totalResults'] = (js or {}).get('totalResults') or (js or {}).get('total')
    if it['kind'] == 'nf': rec['results'] = [compact_nf(c) for c in rs]
    elif it['kind'] == 'sim': rec['results'] = [compact_sim(c) for c in rs]
    elif it['kind'] == 'fo': rec['results'] = [{k: c.get(k) for k in ('videoId', 'videoTitle', 'videoViews', 'videoPublishedAt', 'videoLengthSeconds', 'outlierScore', 'avgViews', 'channelTitle', 'channelUsername', 'ytChannelId', 'channelSubCount', 'channelVideoCount', 'isAiContent', 'isFaceless', 'country', 'language', 'score')} for c in rs]
    elif it['kind'] == 'lat': rec['results'] = [{k: c.get(k) for k in ('title', 'url', 'subscribers', 'daysSinceStart', 'outlierScore', 'isFaceless', 'isAiChannel', 'avgMonthlyViews')} | {'titles': [v.get('video_title') for v in (c.get('lastUploadedVideos') or [])[:5]]} for c in rs]
    calls.append(rec)
viral = [json.loads(l) for l in open(sd + '/viral_rows.jsonl')]
yts = json.load(open(sd + '/ytsearch_rows.json')) if os.path.exists(sd + '/ytsearch_rows.json') else []
raw_out = {'pulled': '2026-10-24', 'note': 'Round 2 NexLev channel widening (HVAC). Compact copy of every NexLev call: niche finder, similar channels, faceless outliers and latest faceless niches saved from the tool results; viral-small-channel rows were returned inline and are transcribed (in-scope rows in full, the rest summarised). NexLev monthly revenue is an RPM-based estimate and is NOT used (operator 2026-10-24: "ignore nexlev rpm its wrong"). Channel-page data (YouTube About, Videos tab) for kept channels is in round2-nexlev-pages-2026-10-24/.',
           'calls': calls, 'viral_small_channels': viral, 'youtube_search_channels': yts,
           'kept': {cid: kept[cid] for cid in kept}, 'dropped_after_page_check': dropped}
json.dump(raw_out, open(out_raw, 'w'), indent=0)
print(len(rows), 'rows;', os.path.getsize(out_raw) // 1024, 'KB raw')
