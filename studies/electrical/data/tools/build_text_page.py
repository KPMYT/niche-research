#!/usr/bin/env python3
"""Build thumbnails/thumbnail-text.html (walkthrough with the operator, 2026-10-26): the words on the recent winners'
thumbnails, sorted by text type, plus the two looks the operator picked (character + explainer board; a person
reacting or pointing at the problem) and the winning close-ups with no character. Source: data/thumb-text/recent-thumb-text.csv
(text from thumbnails/labels-top-recent.csv; text type and lane are the main session's readings) and the round 5 label files."""
import base64, csv, html, io, os, statistics
from collections import defaultdict
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "..", "..")
T = os.path.join(S, "thumbnails")
E = html.escape

def img(vid):
    p = os.path.join(T, "images", f"{vid}.jpg")
    if not os.path.exists(p): return ""
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if h > w * 9 / 16 + 2:  # hqdefault letterbox: crop to 16:9
        nh = int(w * 9 / 16); t = (h - nh) // 2; im = im.crop((0, t, w, t + nh))
    im.thumbnail((360, 203))
    b = io.BytesIO(); im.save(b, "JPEG", quality=64, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def fmtv(v):
    return f"{v/1e6:.1f}M" if v >= 1e6 else (f"{v/1e3:.0f}K" if v >= 1e3 else str(v))

def vint(s):
    try: return int(float(str(s).replace(",", "")))
    except: return 0

recent = list(csv.DictReader(open(os.path.join(S, "data", "thumb-text", "recent-thumb-text.csv"))))
for r in recent: r["_v"] = vint(r["views"])

labels = {}
for fn in ["labels-top-recent.csv", "labels-extra.csv", "labels-channel-top5.csv"]:
    for r in csv.DictReader(open(os.path.join(T, fn))):
        r["_v"] = vint(r["views"])
        labels.setdefault(r["video_id"], r)

TYPES = [  # key, name, what it is
    ("command", "Command", "Tells the viewer to do or stop something"),
    ("question", "Question", "Asks the question the video answers"),
    ("warning", "Warning", "Names the danger or the bad result"),
    ("insider", "Insider", "A thing most people miss"),
    ("mistake", "Mistake", "The word MISTAKE"),
    ("reaction", "Reaction", "An exclamation: surprise or annoyance"),
    ("tease", "Tease", "Holds the point back"),
    ("money", "Money", "A bill or price figure"),
    ("label", "Topic label", "Names the job or topic plainly"),
    ("none", "No text", "Picture only"),
    ("xvsy", "X vs Y", "Two things compared"),
    ("tag", "Tag", "A series tag"),
    ("list", "List", "A numbered list"),
]
TNAME = {k: n for k, n, _ in TYPES}

def card(r, words=None, note=""):
    words = r.get("thumb_text", r.get("text_words", "")) if words is None else words
    words = "" if words.strip().lower() == "none" else words
    src = img(r["video_id"])
    t = r.get("title", "")
    return (f'<figure class="card"><a href="https://www.youtube.com/watch?v={E(r["video_id"])}" target="_blank" rel="noopener">'
            f'<img loading="lazy" src="{src}" alt="{E(t)}"></a><figcaption>'
            f'<div class="words">{E(words) if words else "<span class=\'nowords\'>no text</span>"}</div>'
            f'<div class="meta"><span class="views">{fmtv(r["_v"])}</span><span class="ch">{E(r.get("channel",""))}</span></div>'
            f'<div class="title">{E(t)}</div>{f"<div class=note>{E(note)}</div>" if note else ""}</figcaption></figure>')

inlane = [r for r in recent if r["lane"] == "in"]
out = [r for r in recent if r["lane"] != "in"]
by = defaultdict(list)
for r in inlane: by[r["text_type"]].append(r)
order = [k for k, _, _ in TYPES if k in by]
order.sort(key=lambda k: (k in ("none",), -statistics.median([r["_v"] for r in by[k]]) if len(by[k]) >= 3 else 1, -len(by[k])))

rows_html = ""
for k in order:
    L = by[k]; med = statistics.median([r["_v"] for r in L])
    ex = " · ".join(f"“{E(r['thumb_text'].split(' / ')[0])}”" for r in sorted(L, key=lambda r: -r["_v"])[:3] if r["thumb_text"] != "none")
    small = ' <span class="small">(too few to rank)</span>' if len(L) < 3 else ""
    rows_html += (f'<tr><td><a href="#t-{k}">{TNAME[k]}</a>{small}</td><td class="num">{len(L)}</td>'
                  f'<td class="num">{fmtv(med)}</td><td>{ex or "–"}</td></tr>')

withtext = [r for r in inlane if r["text_type"] != "none"]
wc = [int(r["words"]) for r in withtext if str(r["words"]).isdigit()]
rep = [r["_v"] for r in withtext if r["text_vs_title"] == "repeats title"]
add = [r["_v"] for r in withtext if r["text_vs_title"] == "adds to title"]

gal = ""
for k in order:
    L = sorted(by[k], key=lambda r: -r["_v"])
    gal += f'<section class="group" id="t-{k}"><h3>{TNAME[k]} <span class="count">{len(L)} · typical {fmtv(statistics.median([r["_v"] for r in L]))}</span></h3><div class="grid">'
    gal += "".join(card(r, note=r["text_vs_title"]) for r in L) + "</div></section>"

outgal = "".join(card(r, note=r["lane"].replace("out: ", "out of lane: ")) for r in sorted(out, key=lambda r: -r["_v"]))

# The operator's two looks, from every labelled thumbnail (rounds 5, top 100 + recent + 50 channels' top 5)
def grp(names): return sorted([r for r in labels.values() if r["style_group"] in names], key=lambda r: -r["_v"])
diag = grp({"diagram/animated explainer", "J diagram / 3D / animated explainer"})
hybrid_ids = ["yBHdCsVRle0", "Jbk-26ZM2tY", "4q_bWXjBmLo", "zNFdOF12UY0"]
hybrid = [labels[i] for i in hybrid_ids if i in labels]
react = grp({"real person reacting/pointing at problem", "B real face reaction"})
close = [r for r in grp({"object close-up + big text", "D object close-up + text"})][:16]

def gl(L, n=None):
    return '<div class="grid">' + "".join(card(r) for r in (L[:n] if n else L)) + "</div>"

def med(L): return fmtv(statistics.median([r["_v"] for r in L])) if L else "–"

page = f"""<title>Electrical Thumbnail Text</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Layout: one reading column for the findings, then wide thumbnail grids grouped by text type; blueprint blue for structure, safety yellow only on the thumbnail words. */
:root {{
  --bg: #f6f7f9; --panel: #ffffff; --fg: #17202b; --muted: #5a6573; --rule: #d9dee5;
  --accent: #1f5fae; --hl: #ffd400; --hl-fg: #17202b;
  --display: "Barlow Condensed", "Arial Narrow", sans-serif; --body: "Source Sans 3", system-ui, sans-serif; --mono: "IBM Plex Mono", ui-monospace, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --hl: #ffd400; --hl-fg: #17202b; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg: #0f141b; --panel: #171e27; --fg: #e6ebf1; --muted: #9aa6b4; --rule: #2a3440; --accent: #6ea8ef; --hl: #ffd400; --hl-fg: #17202b; color-scheme: dark }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 var(--body); padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 64px }}
.wrap {{ max-width: 1180px; margin: 0 auto; display: grid; gap: 36px }}
.read {{ max-width: 70ch }}
h1, h2, h3 {{ font-family: var(--display); text-wrap: balance; margin: 0; line-height: 1.05 }}
h1 {{ font-size: clamp(2.2rem, 5vw, 3.2rem); font-weight: 800; text-transform: uppercase; letter-spacing: .01em }}
h2 {{ font-size: 1.9rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: .02em; border-top: 3px solid var(--accent); padding-top: 10px }}
h3 {{ font-size: 1.45rem; font-weight: 700 }}
.eyebrow {{ font: 500 .78rem var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }}
p {{ margin: 0 }} .stack {{ display: grid; gap: 12px }}
ol.find {{ margin: 0; padding-left: 1.3em; display: grid; gap: 8px }}
.tablebox {{ overflow-x: auto }}
table {{ border-collapse: collapse; width: 100%; min-width: 560px; background: var(--panel) }}
th, td {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--rule); vertical-align: top }}
th {{ font: 500 .75rem var(--mono); text-transform: uppercase; letter-spacing: .06em; color: var(--muted) }}
td.num {{ font-family: var(--mono); font-variant-numeric: tabular-nums; text-align: right; white-space: nowrap }}
td a, .read a {{ color: var(--accent) }}
.small, .count {{ font: 500 .78rem var(--mono); color: var(--muted); letter-spacing: 0; text-transform: none }}
.group {{ display: grid; gap: 12px }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px }}
.card {{ margin: 0; background: var(--panel); border: 1px solid var(--rule); display: grid; grid-template-rows: auto 1fr; min-width: 0 }}
.card img {{ display: block; width: 100%; aspect-ratio: 16/9; object-fit: cover; max-width: 100% }}
.card figcaption {{ padding: 10px 12px 12px; display: grid; gap: 6px; align-content: start; min-width: 0 }}
.words {{ font: 700 1.15rem/1.15 var(--display); text-transform: uppercase; background: var(--hl); color: var(--hl-fg); padding: 3px 7px; justify-self: start; overflow-wrap: anywhere }}
.nowords {{ font-weight: 600; opacity: .55 }}
.meta {{ display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; font-size: .85rem; color: var(--muted) }}
.views {{ font: 500 .95rem var(--mono); color: var(--fg); font-variant-numeric: tabular-nums }}
.title {{ font-size: .88rem; line-height: 1.35 }}
.note {{ font: 500 .72rem var(--mono); color: var(--muted); text-transform: uppercase; letter-spacing: .05em }}
details > summary {{ cursor: pointer; font-weight: 600; color: var(--accent) }}
details[open] > summary {{ margin-bottom: 14px }}
a:focus-visible, summary:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px }}
.callout {{ background: var(--panel); border-left: 4px solid var(--accent); padding: 12px 14px }}
</style>
<div class="wrap">
<header class="read stack">
  <div class="eyebrow">Electrical study · thumbnails · 2026-10-26</div>
  <h1>The words on the thumbnails</h1>
  <p>The text on the 82 recent winners' thumbnails (the top 50 of the last 90 days and the top 50 of the last 12 months, in scope, English, 5:00+). {len(inlane)} of them are in your lane. The other {len(out)} are fire or money videos, shown at the bottom for reference. The words were read off each image by a helper and re-checked by the main session against all 82 images. The text types are readings. A second helper sorted the same text blind and agreed on 65 of 73 (40 of 43 in your lane); with its calls the order below barely moves.</p>
</header>

<section class="read stack">
  <h2>What the text does</h2>
  <ol class="find">
    <li><b>Short.</b> The typical thumbnail with text has {statistics.median(wc):.0f} words. Most use 2 to 5.</li>
    <li><b>Commands and questions lead.</b> Among your-lane videos, “STOP DOING THIS”, “This Needs To STOP!”, “START HERE!” and questions like “WHICH ONE KILLS YOU?” or “Why 120V?” typically get about twice the views of a plain topic label (“RUN ELECTRICAL TO A SHED”).</li>
    <li><b>Plain topic labels are the most common and the weakest.</b> {len(by.get('label', []))} of {len(inlane)}, typical {med(by.get('label', []))}. They work for real teachers with a following (Smarter Sparky, The Wiring Guide) more than for new channels.</li>
    <li><b>Repeating the title or adding to it makes little difference.</b> Text that repeats the title: {len(rep)} videos, typical {fmtv(statistics.median(rep))}. Text that adds something new: {len(add)}, typical {fmtv(statistics.median(add))}.</li>
    <li><b>The very biggest have no text at all</b> (hack channels: “99% of People Connect Wires WRONG”, 10.8M). The picture does the work: a red X and a green check over two wires.</li>
  </ol>
  <p class="callout">Samples are small (2 to 15 videos per type), so treat the order as a direction, not a rule. Views here are raw views, not compared with each channel's typical video.</p>
</section>

<section class="stack">
  <h2>Text types in your lane</h2>
  <div class="tablebox"><table><thead><tr><th>Type</th><th>Videos</th><th>Typical views</th><th>Examples</th></tr></thead><tbody>{rows_html}</tbody></table></div>
</section>

<section class="stack">
  <h2>Every your-lane thumbnail, by text type</h2>
  {gal}
  <details><summary>Show the {len(out)} out-of-lane recent winners (fire and money)</summary><div class="grid">{outgal}</div></details>
</section>

<section class="stack">
  <h2>Your look 1: character + explainer board</h2>
  <p class="read">Nobody in this niche pairs a presenter with a blue blueprint board the way your two examples do. The nearest are below: diagram-only thumbnails ({len(diag)} labelled, typical {med(diag)}), and a few that put a person beside a drawn diagram. The Wiring Guide's “Live Neutral Ground EXPLAINED” (1.0M) is the closest real example. Sparky Steve's AI man beside panel diagrams got 17K and 2.6K. So the look is open, and it isn't proven here yet.</p>
  <h3>A person beside a diagram</h3>{gl(hybrid)}
  <h3>Diagram or explainer only</h3>{gl(diag)}
</section>

<section class="stack">
  <h2>Your look 2: a person reacting or pointing at the problem</h2>
  <p class="read">{len(react)} labelled, typical {med(react)}. Several of these are AI personas, and they did well in the last 90 days: Bertha's Clean Home “NOBODY CLEANS THIS” 710K, Frederick 439K, Ray Dutton's Garage 406K, Ramón Delgado 375K. So a character pointing at the problem can work. The small persona channels in the census mostly used dark AI scenes with something burning.</p>
  {gl(react)}
</section>

<section class="stack">
  <h2>Winning close-ups with no character</h2>
  <p class="read">The top object close-ups with text. These are the ones to borrow from by adding Frederick beside the object.</p>
  {gl(close)}
</section>
</div>
"""
open(os.path.join(T, "thumbnail-text.html"), "w").write(page)
print("written", len(page) // 1024, "KB;", len(inlane), "in lane,", len(out), "out;", len(diag), "diagram,", len(react), "react,", len(close), "close-ups")
