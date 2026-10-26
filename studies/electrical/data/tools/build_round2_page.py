#!/usr/bin/env python3
"""Build ideation/round-2.html (2026-10-26): everything carried into the round where the operator finalises ideas.
A. Round-1 ideas the operator kept (1, 2, 7, 12, 14, 29, 30, 31, 33).
B. Silver Cymbal's 1M+ electrical videos with lightly altered titles (silver-cymbal-copies.csv).
C. 50 titles on proven topics in proven formats (titles-50-v2.csv).
Every topic shows its proof under the operator's rule (topic-proof.csv: 300K+ faceless or 1M+ real) and its heat (topic-heat.csv)."""
import base64, csv, html, io, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "..", "..")
I = os.path.join(S, "ideation")
E = html.escape
KEEP = ["1", "2", "7", "12", "14", "29", "30", "31", "33"]
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def img(vid, w=280):
    p = os.path.join(S, "thumbnails", "images", f"{vid}.jpg")
    if not vid or not os.path.exists(p): return ""
    im = Image.open(p).convert("RGB"); W, H = im.size
    if H > W * 9 / 16 + 2:
        nh = int(W * 9 / 16); t = (H - nh) // 2; im = im.crop((0, t, W, t + nh))
    im.thumbnail((w, int(w * 9 / 16)))
    b = io.BytesIO(); im.save(b, "JPEG", quality=64, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def fmtv(v):
    try: v = int(float(str(v).replace(",", "")))
    except Exception: return str(v)
    return f"{v/1e6:.1f}M" if v >= 1e6 else (f"{v/1e3:.0f}K" if v >= 1e3 else str(v))

def when(d):
    try: y, m, dd = d[:10].split("-"); return f"{MON[int(m)-1]} {int(dd)}, {y}"
    except Exception: return d

heat = {r["n"]: r for r in csv.DictReader(open(os.path.join(I, "topic-heat.csv")))}
proof = {r["n"]: r for r in csv.DictReader(open(os.path.join(I, "topic-proof.csv")))}
ideas = {r["n"]: r for r in csv.DictReader(open(os.path.join(I, "round-1-ideas.csv")))}
sc = list(csv.DictReader(open(os.path.join(I, "silver-cymbal-copies.csv"))))
t50 = list(csv.DictReader(open(os.path.join(I, "titles-50-v2.csv"))))
LOOK = {"Board": "Character + explainer board", "Point": "Character pointing at the problem"}

def proofline(n):
    p = proof.get(str(n))
    if not p or p["proven"] != "yes": return '<span class="pf no">Topic not proven</span>'
    b = p["best_proof"].split(" | ")
    t = f"“{E(b[0])}”, {E(b[1])}, {fmtv(b[2])}, {E(when(b[3]))}" if len(b) == 4 else E(p["best_proof"])
    return f'<span class="pf yes">Proven</span> <span class="pft">{p["proof_videos"]} video{"s" if p["proof_videos"] != "1" else ""} over the bar. Biggest: {t}</span>'

def heatline(n):
    h = heat.get(str(n))
    if not h: return ""
    hk = h["heat"].split(",")[0].lower()
    part = " (partial count)" if h["partial"] else ""
    return (f'<span class="hl heat-{hk}">{E(h["heat"])}</span> <span class="pft">Last 12 months: {h["last12_uploads"]} upload{"" if h["last12_uploads"] == "1" else "s"}, typically '
            f'{fmtv(h["last12_typical_views"] or 0)}, {h["last12_over_100k"]} over 100K{part}.</span>')

def topicbox(n, name):
    return f'<div class="topic"><div class="tname">Topic: {E(name)}</div><div>{proofline(n)}</div><div>{heatline(n)}</div></div>'

def side(vid, label, title, meta):
    return (f'<a class="src" href="https://www.youtube.com/watch?v={E(vid)}" target="_blank" rel="noopener"><img loading="lazy" src="{img(vid)}" alt="">'
            f'<span class="slabel">{label}</span><span class="st">{E(title)}</span><span class="sm">{meta}</span></a>') if vid else \
           f'<div class="src"><div class="noimg">From the cross-niche bank</div><span class="slabel">{label}</span><span class="st">{E(title)}</span><span class="sm">{meta}</span></div>'

A = ""
for k in KEEP:
    r = ideas[k]; h = heat[k]
    A += f'''<article class="row"><div class="num">{k}</div><div class="main"><h3>{E(r["our_title"])}</h3>
  <div class="chips"><span class="words">{E(r["thumb_text"])}</span><span class="look look-{r["thumb_look"].lower()}">{LOOK[r["thumb_look"]]}</span><span class="emo">{E(r["emotion"])}</span></div>
  {topicbox(k, h["topic"])}</div>
  {side(r["source_id"], "Based on", r["source_title"], f'<b>{fmtv(h["source_views_now"] or r["source_views"])}</b> · {E(r["source_channel"])} · posted {E(when(h["source_date"]))}')}
</article>'''

B = ""
for r in sc:
    short = '<span class="flag">Original under 5 min: ours is the long-form version</span>' if r["sc_long_form"] != "y" else ""
    notes = " · ".join(x for x in [r["demo_note"], r["note"]] if x)
    B += f'''<article class="row"><div class="num">{r["n"]}</div><div class="main"><h3>{E(r["our_title"])}</h3>
  <div class="chips">{short}</div>
  {f'<p class="note">{E(notes)}</p>' if notes else ""}</div>
  {side(r["sc_video_id"], "Silver Cymbal original", r["sc_title"], f'<b>{fmtv(r["sc_views"])}</b> · posted {E(when(r["sc_upload_date"]))} · {E(r["sc_length"])}')}
</article>'''

C = ""
for r in t50:
    vid = r["format_video_id"]
    meta = f'<b>{fmtv(r["format_views"])}</b> · {E(r["format_channel"])} ({E(r["format_channel_type"])}) · {E(when(r["format_date"]))}'
    C += f'''<article class="row"><div class="num">{r["n"]}</div><div class="main"><h3>{E(r["title"])}</h3>
  <div class="chips"><span class="words">{E(r["thumb_text"])}</span><span class="look look-{r["thumb_look"].lower()}">{LOOK[r["thumb_look"]]}</span><span class="emo">{E(r["emotion"])}</span></div>
  {topicbox(r["topic_n"], r["topic"])}</div>
  {side(vid, f'Format {E(r["format_code"])}: {E(r["format_name"])}', r["format_example"], meta)}
</article>'''

page = f"""<title>Electrical Ideas Round 2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Layout: three numbered lists (kept ideas, Silver Cymbal copies, 50 titles); each row is our title + topic proof on the left, the proving video on the right. Blueprint blue structure, safety yellow only for thumbnail words, green for proven. */
:root {{
  --bg: #f6f7f9; --panel: #ffffff; --fg: #17202b; --muted: #5a6573; --rule: #d9dee5;
  --accent: #1f5fae; --accent-soft: #e3edf9; --point: #8a4b00; --point-soft: #fbeedd; --hl: #ffd400; --hl-fg: #17202b;
  --hot: #c0361f; --warm: #a8670a; --ok: #1d7a43; --ok-soft: #e2f3e8; --no: #9b2c2c;
  --display: "Barlow Condensed", "Arial Narrow", sans-serif; --body: "Source Sans 3", system-ui, sans-serif; --mono: "IBM Plex Mono", ui-monospace, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --accent-soft: #1a2a40; --point: #f0b46a; --point-soft: #34260f; --hot: #ff7a5c; --warm: #e8a94a; --ok: #5fcf8c; --ok-soft: #173325; --no: #ff8a8a; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --accent-soft: #1a2a40; --point: #f0b46a; --point-soft: #34260f; --hot: #ff7a5c; --warm: #e8a94a; --ok: #5fcf8c; --ok-soft: #173325; --no: #ff8a8a; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 var(--body); padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 64px }}
.wrap {{ max-width: 1100px; margin: 0 auto; display: grid; gap: 36px }}
.read {{ max-width: 72ch; display: grid; gap: 12px }}
h1, h2, h3 {{ font-family: var(--display); text-wrap: balance; margin: 0; line-height: 1.1 }}
h1 {{ font-size: clamp(2.2rem, 5vw, 3.2rem); font-weight: 800; text-transform: uppercase }}
h2 {{ font-size: 1.8rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: .02em; border-top: 3px solid var(--accent); padding-top: 10px }}
h3 {{ font-size: 1.4rem; font-weight: 700 }}
p {{ margin: 0 }}
.eyebrow {{ font: 500 .78rem var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }}
nav {{ display: flex; gap: 10px; flex-wrap: wrap }} nav a {{ font: 600 .95rem var(--body); color: var(--accent) }}
section, .list {{ display: grid; gap: 14px }}
.row {{ background: var(--panel); border: 1px solid var(--rule); display: grid; grid-template-columns: auto minmax(0, 1fr) 250px; gap: 16px; padding: 16px; align-items: start }}
.num {{ font: 800 2rem/1 var(--display); color: var(--accent); min-width: 2ch; font-variant-numeric: tabular-nums }}
.main {{ display: grid; gap: 10px; min-width: 0 }}
.chips {{ display: flex; gap: 8px; flex-wrap: wrap; align-items: center }}
.words {{ font: 700 1.1rem/1.1 var(--display); text-transform: uppercase; background: var(--hl); color: var(--hl-fg); padding: 3px 8px }}
.look, .emo, .flag {{ font: 500 .72rem var(--mono); text-transform: uppercase; letter-spacing: .05em; padding: 4px 8px }}
.look-board {{ background: var(--accent-soft); color: var(--accent) }} .look-point {{ background: var(--point-soft); color: var(--point) }}
.emo {{ color: var(--muted); padding-left: 0 }} .flag {{ background: var(--point-soft); color: var(--point) }}
.note {{ color: var(--muted); font-size: .9rem }}
.topic {{ display: grid; gap: 4px; padding: 10px 12px; background: var(--bg); border-left: 4px solid var(--ok); font-size: .9rem }}
.tname {{ font: 700 1rem var(--display); text-transform: uppercase; letter-spacing: .03em }}
.pf {{ font: 500 .72rem var(--mono); text-transform: uppercase; letter-spacing: .05em; padding: 2px 6px }}
.pf.yes {{ background: var(--ok-soft); color: var(--ok) }} .pf.no {{ color: var(--no) }}
.hl {{ font: 500 .72rem var(--mono); text-transform: uppercase; letter-spacing: .05em; color: var(--hc) }}
.heat-hot {{ --hc: var(--hot) }} .heat-warm {{ --hc: var(--warm) }} .heat-quiet {{ --hc: var(--accent) }} .heat-cold {{ --hc: var(--muted) }}
.pft {{ color: var(--fg) }}
.src {{ display: grid; gap: 4px; color: inherit; text-decoration: none; min-width: 0 }}
.src img {{ width: 100%; aspect-ratio: 16/9; object-fit: cover; display: block; max-width: 100% }}
.noimg {{ aspect-ratio: 16/9; max-width: 100%; display: grid; place-items: center; text-align: center; padding: 8px; background: var(--accent-soft); color: var(--accent); font: 500 .75rem var(--mono); text-transform: uppercase }}
.slabel {{ font: 500 .7rem var(--mono); text-transform: uppercase; letter-spacing: .06em; color: var(--muted) }}
.st {{ font-size: .88rem; line-height: 1.3 }} .sm {{ font-size: .82rem; color: var(--muted) }} .sm b {{ font: 500 .92rem var(--mono); color: var(--fg) }}
a.src:hover .st {{ text-decoration: underline }}
a:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px }}
.legend {{ display: grid; gap: 6px; font-size: .92rem }} .legend b {{ font-family: var(--display); text-transform: uppercase; letter-spacing: .03em }}
@media (max-width: 760px) {{ .row {{ grid-template-columns: auto minmax(0, 1fr) }} .src {{ grid-column: 1 / -1 }} }}
</style>
<div class="wrap">
<header class="read">
  <div class="eyebrow">Electrical · ideation round 2 · 2026-10-26</div>
  <h1>Round 2: ideas to finalise</h1>
  <p>Everything carried into this round, checked against your rule: a topic counts only if a video on it has at least 300K views on a faceless channel (AI personas included) or 1M on a real, on-camera channel. Any upload date; the date is shown. Formats in part C pass the same bar and come from the last 12 months.</p>
  <div class="legend"><p><b>Proven</b>: the topic clears your bar; the biggest proving video is named. <b>Heat</b> shows whether new uploads on the topic still do well (last 12 months): Hot, Hot with few uploads, Warm, Quiet (few new uploads) or Cold (many new uploads, small views).</p></div>
  <nav><a href="#a">A. Kept from round 1 (9)</a><a href="#b">B. Silver Cymbal copies ({len(sc)})</a><a href="#c">C. 50 titles</a></nav>
</header>
<section id="a"><h2>A. Kept from round 1</h2><div class="list">{A}</div></section>
<section id="b"><h2>B. Silver Cymbal copies</h2><p class="read">His electrical videos over 1M views (he's a real, on-camera channel), titles lightly altered, as you asked (like idea 32). Generator and power-station product reviews are left out (scope). Most originals are under 5 minutes, so ours would be the long-form version; where the original is a demonstration, we explain the result instead of filming it.</p><div class="list">{B}</div></section>
<section id="c"><h2>C. 50 titles: proven topics × proven formats</h2><div class="list">{C}</div></section>
</div>
"""
open(os.path.join(I, "round-2.html"), "w").write(page)
print("written", len(page) // 1024, "KB")
