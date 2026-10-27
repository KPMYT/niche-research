#!/usr/bin/env python3
"""Build ideation/titles-50.html (2026-10-26): 50 titles that put a measured topic (topic-heat.csv) into a recent winning
title format (recent-formats.csv, or the cross-niche bank). Each card shows the topic's heat and the format's source video.
Source: ideation/titles-50.csv."""
import base64, csv, html, io, os
from collections import Counter
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "..", "..")
E = html.escape

def img(vid):
    p = os.path.join(S, "thumbnails", "images", f"{vid}.jpg")
    if not vid or not os.path.exists(p): return ""
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if h > w * 9 / 16 + 2:
        nh = int(w * 9 / 16); t = (h - nh) // 2; im = im.crop((0, t, w, t + nh))
    im.thumbnail((280, 158))
    b = io.BytesIO(); im.save(b, "JPEG", quality=64, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def fmtv(v):
    try: v = int(float(str(v).replace(",", "")))
    except Exception: return str(v)
    return f"{v/1e6:.1f}M" if v >= 1e6 else (f"{v/1e3:.0f}K" if v >= 1e3 else str(v))

rows = list(csv.DictReader(open(os.path.join(S, "ideation", "titles-50.csv"))))
fid = {r["example_title"]: r["video_id"] for r in csv.DictReader(open(os.path.join(S, "ideation", "recent-formats.csv")))}
HEAT = {r["n"]: r for r in csv.DictReader(open(os.path.join(S, "ideation", "topic-heat.csv")))}
LOOK = {"Board": "Character + explainer board", "Point": "Character pointing at the problem"}
ORDER = ["Hot", "Hot, few uploads", "Warm", "Quiet", "Cold"]
rows.sort(key=lambda r: (ORDER.index(r["heat"]), int(r["n"])))
counts = Counter(r["heat"] for r in rows)

cards = ""
for g in ORDER:
    L = [r for r in rows if r["heat"] == g]
    if not L: continue
    cards += f'<section class="group"><h2>{E(g)} topics <span class="count">{len(L)}</span></h2><div class="list">'
    for r in L:
        hk = r["heat"].split(",")[0].lower()
        h = HEAT[r["topic_n"]]
        bestline = f"Best in 12 months: “{E(h['last12_best_title'])}”, {E(h['last12_best_channel'])}, {fmtv(h['last12_best_views'] or 0)} ({E(h['last12_best_age'])})" if h["last12_best_title"] else ""
        vid = fid.get(r["format_example"], "")
        mult = f" · {float(r['format_example_multiple']):.0f}× its channel's usual" if r["format_example_multiple"] else ""
        when = f" · {E(r['format_example_when'])}" if r["format_example_when"] else ""
        ch = f" · {E(r['format_example_channel'])}" if r["format_example_channel"] else ""
        thumb = f'<img loading="lazy" src="{img(vid)}" alt="">' if vid else '<div class="noimg">Format from the cross-niche bank</div>'
        link_open = f'<a class="fmt" href="https://www.youtube.com/watch?v={E(vid)}" target="_blank" rel="noopener">' if vid else '<div class="fmt">'
        link_close = "</a>" if vid else "</div>"
        part = " <span class='partial'>(partial count)</span>" if r["partial"] else ""
        cards += f'''<article class="t" id="t{r["n"]}">
  <div class="num">{r["n"]}</div>
  <div class="main">
    <h3>{E(r["title"])}</h3>
    <div class="chips"><span class="words">{E(r["thumb_text"])}</span><span class="look look-{r["thumb_look"].lower()}">{E(LOOK[r["thumb_look"]])}</span><span class="emo">{E(r["emotion"])}</span></div>
    <div class="heat heat-{hk}"><span class="hlabel">Topic: {E(HEAT[r["topic_n"]]["topic"])} · {E(r["heat"])}</span>{part}
      <span>Last 12 months: <b>{r["last12_uploads"]}</b> uploads, typically <b>{fmtv(r["last12_typical"])}</b>, {r["last12_over_100k"]} over 100K. Last 90 days: <b>{r["last90_uploads"]}</b>.</span>
      <span class="hbest">{bestline}</span></div>
  </div>
  {link_open}
    {thumb}
    <span class="flabel">Format {E(r["format_code"])}: {E(r["format_name"])}</span>
    <span class="ft">“{E(r["format_example"])}”</span>
    <span class="fm"><b>{fmtv(r["format_example_views"])}</b>{ch}{when}{mult}</span>
    <span class="fm">From: {E(r["format_from"])}</span>
  {link_close}
</article>'''
    cards += "</div></section>"

summary = " · ".join(f"{k} {counts[k]}" for k in ORDER if counts[k])
page = f"""<title>Electrical Titles 50</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Layout: grouped by topic heat (hottest first); each row is our title + topic heat on the left, the format's source video on the right. Blueprint blue structure, safety yellow only for thumbnail words, red and amber for heat. */
:root {{
  --bg: #f6f7f9; --panel: #ffffff; --fg: #17202b; --muted: #5a6573; --rule: #d9dee5;
  --accent: #1f5fae; --accent-soft: #e3edf9; --point: #8a4b00; --point-soft: #fbeedd; --hl: #ffd400; --hl-fg: #17202b; --hot: #c0361f; --warm: #a8670a;
  --display: "Barlow Condensed", "Arial Narrow", sans-serif; --body: "Source Sans 3", system-ui, sans-serif; --mono: "IBM Plex Mono", ui-monospace, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --accent-soft: #1a2a40; --point: #f0b46a; --point-soft: #34260f; --hot: #ff7a5c; --warm: #e8a94a; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --accent-soft: #1a2a40; --point: #f0b46a; --point-soft: #34260f; --hot: #ff7a5c; --warm: #e8a94a; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 var(--body); padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 64px }}
.wrap {{ max-width: 1100px; margin: 0 auto; display: grid; gap: 36px }}
.read {{ max-width: 72ch; display: grid; gap: 12px }}
h1, h2, h3 {{ font-family: var(--display); text-wrap: balance; margin: 0; line-height: 1.1 }}
h1 {{ font-size: clamp(2.2rem, 5vw, 3.2rem); font-weight: 800; text-transform: uppercase }}
h2 {{ font-size: 1.8rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: .02em; border-top: 3px solid var(--accent); padding-top: 10px }}
h3 {{ font-size: 1.45rem; font-weight: 700 }}
p {{ margin: 0 }}
.eyebrow, .count {{ font: 500 .78rem var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }}
.group, .list {{ display: grid; gap: 14px }}
.t {{ background: var(--panel); border: 1px solid var(--rule); display: grid; grid-template-columns: auto minmax(0, 1fr) 250px; gap: 16px; padding: 16px; align-items: start }}
.num {{ font: 800 2rem/1 var(--display); color: var(--accent); min-width: 2ch; font-variant-numeric: tabular-nums }}
.main {{ display: grid; gap: 10px; min-width: 0 }}
.chips {{ display: flex; gap: 8px; flex-wrap: wrap; align-items: center }}
.words {{ font: 700 1.1rem/1.1 var(--display); text-transform: uppercase; background: var(--hl); color: var(--hl-fg); padding: 3px 8px }}
.look, .emo {{ font: 500 .72rem var(--mono); text-transform: uppercase; letter-spacing: .05em; padding: 4px 8px }}
.look-board {{ background: var(--accent-soft); color: var(--accent) }}
.look-point {{ background: var(--point-soft); color: var(--point) }}
.emo {{ color: var(--muted); padding-left: 0 }}
.heat {{ display: grid; gap: 4px; padding: 10px 12px; border-left: 4px solid var(--hc); background: var(--bg); font-size: .9rem }}
.hlabel {{ font: 700 1rem var(--display); text-transform: uppercase; letter-spacing: .03em; color: var(--hc) }}
.heat-hot {{ --hc: var(--hot) }} .heat-warm {{ --hc: var(--warm) }} .heat-quiet {{ --hc: var(--accent) }} .heat-cold {{ --hc: var(--muted) }}
.hbest {{ color: var(--muted); font-size: .85rem }} .partial {{ font: 500 .72rem var(--mono); color: var(--muted) }}
.fmt {{ display: grid; gap: 4px; color: inherit; text-decoration: none; min-width: 0 }}
.fmt img {{ width: 100%; aspect-ratio: 16/9; object-fit: cover; display: block; max-width: 100% }}
.noimg {{ aspect-ratio: 16/9; max-width: 100%; display: grid; place-items: center; text-align: center; padding: 8px; background: var(--accent-soft); color: var(--accent); font: 500 .75rem var(--mono); text-transform: uppercase; letter-spacing: .05em }}
.flabel {{ font: 500 .7rem var(--mono); text-transform: uppercase; letter-spacing: .06em; color: var(--muted) }}
.ft {{ font-size: .88rem; line-height: 1.3 }}
.fm {{ font-size: .82rem; color: var(--muted) }} .fm b {{ font: 500 .92rem var(--mono); color: var(--fg) }}
a.fmt:hover .ft {{ text-decoration: underline }}
a:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px }}
.legend {{ display: grid; gap: 6px; font-size: .92rem }} .legend b {{ font-family: var(--display); text-transform: uppercase; letter-spacing: .03em }}
@media (max-width: 760px) {{ .t {{ grid-template-columns: auto minmax(0, 1fr) }} .fmt {{ grid-column: 1 / -1 }} }}
</style>
<div class="wrap">
<header class="read">
  <div class="eyebrow">Electrical · ideation · 50 combined titles · 2026-10-26</div>
  <h1>50 titles: hot topics × winning formats</h1>
  <p>Each title puts a topic we measured into a title format that has won recently. On the left: the title, thumbnail words, which of your two looks, and how hot the topic is. On the right: where the format comes from, the video that proves it, with its views and how far it beat its channel's usual video. Grouped hottest first. {summary}.</p>
  <div class="legend"><p><b>Topic heat</b> counts long-form uploads on the topic found in YouTube search and on the source channel (2026-10-26), each title checked by a helper as really on topic. Search shows a sample, so counts are a floor; “partial count” means some page loads failed.</p>
  <p><b>Hot</b>: a 100K+ upload in 12 months and new uploads typically 1,000+. <b>Hot, few uploads</b>: 5 or fewer new uploads, typically 10,000+. <b>Warm</b>: one of the two. <b>Quiet</b>: 5 or fewer new uploads, smaller views. <b>Cold</b>: many new uploads, none over 100K, typically under 1,000 (no titles here).</p>
  <p><b>Formats</b> R1–R33 come from this niche's recent winners (last 12 months, at least 3× the channel's usual video, 20K+ views). F-numbers come from your cross-niche format bank. The “× its channel's usual” figures come from search and run high, so compare them with each other.</p></div>
</header>
{cards}
</div>
"""
open(os.path.join(S, "ideation", "titles-50.html"), "w").write(page)
print("written", len(page) // 1024, "KB,", len(rows), "titles")
