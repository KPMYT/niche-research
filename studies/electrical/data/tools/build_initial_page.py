#!/usr/bin/env python3
"""Build ideation/initial-ideas.html (2026-10-26): the operator's 17 initial ideas (round-2 picks A all, B 3 6 7 10 11, C 2 12 15)
with reference video, topic heat and the main session's thumbnail advice. Source: ideation/initial-ideas.csv.
Old docstring follows: (2026-10-26): everything carried into the round where the operator finalises ideas.
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


rows = list(csv.DictReader(open(os.path.join(I, "initial-ideas.csv"))))
LOOK = {"Board": "Character + explainer board", "Point": "Character pointing at the problem"}
body, cur = "", None
for r in rows:
    if r["group"] != cur:
        if cur: body += "</div></section>"
        cur = r["group"]; n = sum(1 for x in rows if x["group"] == cur)
        body += f'<section><h2>{E(cur)} <span class="cnt">{n}</span></h2><div class="list">'
    hk = r["heat"].split(",")[0].lower() if r["heat"] else ""
    heatl = (f'<div><span class="hl heat-{hk}">{E(r["heat"])}</span> <span class="pft">Topic: {E(r["topic"])}. Last 12 months: {r["last12_uploads"]} '
             f'upload{"" if r["last12_uploads"] == "1" else "s"}, typically {fmtv(r["last12_typical"] or 0)}, {r["last12_over_100k"]} over 100K.</span></div>') if r["heat"] else ""
    words = f'<span class="words">{E(r["thumb_text"])}</span>' if r["thumb_text"] else '<span class="words nowords">No text</span>'
    emo = f'<span class="emo">{E(r["emotion"])}</span>' if r["emotion"] else ""
    ov = f'<span class="flag">{E(r["overlap"])}</span>' if r["overlap"] else ""
    body += f'''<article class="row"><div class="num">{E(r["key"])}</div><div class="main"><h3>{E(r["title"])}</h3>
  <div class="chips">{words}<span class="look look-{r["thumb_look"].lower()}">{LOOK[r["thumb_look"]]}</span>{emo}{ov}</div>
  <div class="topic"><div><span class="pf yes">Proven</span> <span class="pft">Reference clears your bar: {fmtv(r["ref_views"])} on {E(r["ref_channel"])} ({E(r["ref_type"])} channel, needs {"300K" if r["ref_type"] in ("faceless", "AI persona") else "1M"}).</span></div>{heatl}<div class="pft fm2">{E(r["format_line"])}</div></div>
  <div class="advice"><div class="alabel">Thumbnail: how to improve it</div><p>{E(r["thumb_advice"])}</p></div></div>
  <a class="src" href="https://www.youtube.com/watch?v={E(r["ref_id"])}" target="_blank" rel="noopener"><img loading="lazy" src="{img(r["ref_id"])}" alt="">
  <span class="slabel">Reference</span><span class="st">{E(r["ref_title"])}</span><span class="sm"><b>{fmtv(r["ref_views"])}</b> · {E(r["ref_channel"])} · posted {E(when(r["ref_date"]))}</span></a>
</article>'''
body += "</div></section>"
STYLE = r'''<style>
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
</style>'''
STYLE = STYLE.replace("{{", "{").replace("}}", "}") + "<style>.advice{display:grid;gap:4px;padding:10px 12px;border:1px dashed var(--accent);font-size:.92rem}.alabel{font:500 .72rem var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--accent)}.cnt{font:500 .78rem var(--mono);color:var(--muted)}.nowords{background:var(--accent-soft);color:var(--accent)}.fm2{color:var(--muted);font-size:.85rem}</style>"
page = ("<title>Electrical Initial Ideas</title>\n<meta name=\"claude:viewport-fit-sides\" content=\"cover\">\n"
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n"
        "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@500&display=swap\">\n"
        + STYLE + f'''<div class="wrap"><header class="read"><div class="eyebrow">Electrical · initial ideas · 2026-10-26</div><h1>Our initial ideas</h1><p><b>All 17 titles confirmed (2026-10-26).</b> Five were reworded by you: A2, A12, A14, B3, B6.</p>
<p>The {len(rows)} ideas you picked: the 9 kept from round 1, 5 Silver Cymbal copies and 3 of the 50 titles. Each shows the title, the thumbnail words and look, the reference video with its views and posting date, how hot the topic is now, and how to make the thumbnail better than the reference.</p>
<p>Overlaps are flagged: A2 and C2 share a topic, as do A12 and C12; A31 and B11 are close. Each pair gets a different thumbnail so both can run, or you can drop one.</p></header>{body}</div>''')
open(os.path.join(I, "initial-ideas.html"), "w").write(page)
print("written", len(page) // 1024, "KB,", len(rows), "ideas")
