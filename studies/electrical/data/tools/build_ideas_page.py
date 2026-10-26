#!/usr/bin/env python3
"""Build ideation/round-1-ideas.html (2026-10-26): each round-1 idea beside the niche video it improves on.
Source: ideation/round-1-ideas.csv; source thumbnails from thumbnails/images/ (shrunk and embedded)."""
import base64, csv, html, io, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "..", "..")
E = html.escape

def img(vid):
    p = os.path.join(S, "thumbnails", "images", f"{vid}.jpg")
    if not os.path.exists(p): return ""
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if h > w * 9 / 16 + 2:
        nh = int(w * 9 / 16); t = (h - nh) // 2; im = im.crop((0, t, w, t + nh))
    im.thumbnail((320, 180))
    b = io.BytesIO(); im.save(b, "JPEG", quality=66, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def fmtv(v):
    v = int(float(v)); return f"{v/1e6:.1f}M" if v >= 1e6 else (f"{v/1e3:.0f}K" if v >= 1e3 else str(v))

rows = list(csv.DictReader(open(os.path.join(S, "ideation", "round-1-ideas.csv"))))
groups = []
for r in rows:
    if not groups or groups[-1][0] != r["group"]: groups.append((r["group"], []))
    groups[-1][1].append(r)

LOOK = {"Board": "Character + explainer board", "Point": "Character pointing at the problem"}
body = ""
for g, L in groups:
    body += f'<section class="group"><h2>{E(g)} <span class="count">{len(L)}</span></h2><div class="list">'
    for r in L:
        vil = f'<div><dt>Villain</dt><dd>{E(r["villain"])}</dd></div>' if r["villain"] else ""
        body += f'''<article class="idea" id="i{r["n"]}">
  <div class="num">{r["n"]}</div>
  <div class="main">
    <h3>{E(r["our_title"])}</h3>
    <div class="chips"><span class="words">{E(r["thumb_text"])}</span><span class="look look-{r["thumb_look"].lower()}">{E(LOOK.get(r["thumb_look"], r["thumb_look"]))}</span></div>
    <dl><div><dt>Format</dt><dd>{E(r["format"])}</dd></div><div><dt>Emotion</dt><dd>{E(r["emotion"])}</dd></div>{vil}<div><dt>What we improve</dt><dd>{E(r["what_we_improve"])}</dd></div></dl>
  </div>
  <a class="src" href="https://www.youtube.com/watch?v={E(r["source_id"])}" target="_blank" rel="noopener">
    <img loading="lazy" src="{img(r["source_id"])}" alt="{E(r["source_title"])}">
    <span class="srclabel">Based on</span>
    <span class="srct">{E(r["source_title"])}</span>
    <span class="srcm"><b>{fmtv(r["source_views"])}</b> · {E(r["source_channel"])}</span>
  </a>
</article>'''
    body += "</div></section>"

page = f"""<title>Electrical Ideas Round 1</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Layout: a numbered list of idea rows; our title leads on the left, the source video it improves on sits on the right. Blueprint blue for structure, safety yellow only for thumbnail words. */
:root {{
  --bg: #f6f7f9; --panel: #ffffff; --fg: #17202b; --muted: #5a6573; --rule: #d9dee5;
  --accent: #1f5fae; --accent-soft: #e3edf9; --point: #8a4b00; --point-soft: #fbeedd; --hl: #ffd400; --hl-fg: #17202b;
  --display: "Barlow Condensed", "Arial Narrow", sans-serif; --body: "Source Sans 3", system-ui, sans-serif; --mono: "IBM Plex Mono", ui-monospace, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --accent-soft: #1a2a40; --point: #f0b46a; --point-soft: #34260f; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --accent-soft: #1a2a40; --point: #f0b46a; --point-soft: #34260f; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 var(--body); padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 64px }}
.wrap {{ max-width: 1100px; margin: 0 auto; display: grid; gap: 36px }}
.read {{ max-width: 70ch; display: grid; gap: 12px }}
h1, h2, h3 {{ font-family: var(--display); text-wrap: balance; margin: 0; line-height: 1.1 }}
h1 {{ font-size: clamp(2.2rem, 5vw, 3.2rem); font-weight: 800; text-transform: uppercase }}
h2 {{ font-size: 1.8rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: .02em; border-top: 3px solid var(--accent); padding-top: 10px }}
h3 {{ font-size: 1.5rem; font-weight: 700 }}
p {{ margin: 0 }}
.eyebrow, .count {{ font: 500 .78rem var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }}
.group, .list {{ display: grid; gap: 14px }}
.idea {{ background: var(--panel); border: 1px solid var(--rule); display: grid; grid-template-columns: auto minmax(0, 1fr) 280px; gap: 16px; padding: 16px; align-items: start }}
.num {{ font: 800 2rem/1 var(--display); color: var(--accent); min-width: 2ch; font-variant-numeric: tabular-nums }}
.main {{ display: grid; gap: 10px; min-width: 0 }}
.chips {{ display: flex; gap: 8px; flex-wrap: wrap; align-items: center }}
.words {{ font: 700 1.1rem/1.1 var(--display); text-transform: uppercase; background: var(--hl); color: var(--hl-fg); padding: 3px 8px }}
.look {{ font: 500 .74rem var(--mono); text-transform: uppercase; letter-spacing: .05em; padding: 4px 8px }}
.look-board {{ background: var(--accent-soft); color: var(--accent) }}
.look-point {{ background: var(--point-soft); color: var(--point) }}
dl {{ margin: 0; display: grid; gap: 4px }}
dl div {{ display: grid; grid-template-columns: 8.5em minmax(0, 1fr); gap: 8px }}
dt {{ font: 500 .74rem/1.9 var(--mono); text-transform: uppercase; letter-spacing: .05em; color: var(--muted) }}
dd {{ margin: 0; font-size: .95rem }}
.src {{ display: grid; gap: 4px; color: inherit; text-decoration: none; min-width: 0 }}
.src img {{ width: 100%; aspect-ratio: 16/9; object-fit: cover; display: block; max-width: 100% }}
.srclabel {{ font: 500 .7rem var(--mono); text-transform: uppercase; letter-spacing: .06em; color: var(--muted) }}
.srct {{ font-size: .9rem; line-height: 1.3 }}
.srcm {{ font-size: .85rem; color: var(--muted) }} .srcm b {{ font: 500 .95rem var(--mono); color: var(--fg) }}
.src:hover .srct {{ text-decoration: underline }}
a:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px }}
@media (max-width: 760px) {{ .idea {{ grid-template-columns: auto minmax(0, 1fr) }} .src {{ grid-column: 1 / -1 }} dl div {{ grid-template-columns: 1fr; gap: 0 }} }}
</style>
<div class="wrap">
<header class="read">
  <div class="eyebrow">Electrical · ideation round 1 · 2026-10-26</div>
  <h1>Ideas, round 1</h1>
  <p>{len(rows)} ideas, each built on a proven video from this niche in the formats and topics you chose. Each one shows our title, the thumbnail words, which of your two looks it uses, and the video it improves on, with its views. Pick by number: “keep 1, 4, 10” or “drop 7”.</p>
  <p>The plan is channel-neutral. The two generator ideas (7 and 31) suit Jack Redfield best.</p>
</header>
{body}
</div>
"""
open(os.path.join(S, "ideation", "round-1-ideas.html"), "w").write(page)
print("written", len(page) // 1024, "KB,", len(rows), "ideas")
