#!/usr/bin/env python3
"""Build thumbnails/thumbnail-styles.html (deliverable 5): every labelled thumbnail grouped by style, with views,
plus the counts of which styles and elements go with the biggest videos. Images are shrunk and embedded (the page can't load YouTube)."""
import base64, csv, html, io, os, statistics
from collections import defaultdict, Counter
from PIL import Image
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "thumbnails")
rows = []
for fn, setname in [("labels-top-recent.csv", None), ("labels-extra.csv", None), ("labels-channel-top5.csv", "channel-top5")]:
    p = os.path.join(T, fn)
    if not os.path.exists(p): continue
    for r in csv.DictReader(open(p)):
        r["_set"] = r.get("set") or r.get("sets") or setname or ""
        try: r["_v"] = int(float(str(r.get("views", "0")).replace(",", "")))
        except: r["_v"] = 0
        rows.append(r)
seen = {}
for r in rows:  # a video in both files: keep one card, join the sets
    k = r["video_id"]
    if k in seen: seen[k]["_set"] += ";" + r["_set"]
    else: seen[k] = r
rows = sorted(seen.values(), key=lambda r: -r["_v"])
def img(vid):
    p = os.path.join(T, "images", f"{vid}.jpg")
    if not os.path.exists(p): return ""
    im = Image.open(p).convert("RGB"); im.thumbnail((320, 180))
    b = io.BytesIO(); im.save(b, "JPEG", quality=62, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()
def fmtv(v):
    return f"{v/1e6:.1f}M" if v >= 1e6 else (f"{v/1e3:.0f}K" if v >= 1e3 else str(v))
E = html.escape
q75 = sorted([r["_v"] for r in rows])[int(len(rows) * 0.75)] if rows else 0
# The two labellers named style groups differently; both are mapped to one shared list (main session, 2026-10-26).
UNIFY = {"real person presenting": "Real person, calm, with subject and text", "A real face + subject + text": "Real person, calm, with subject and text",
         "real person reacting/pointing at problem": "Real person reacting or pointing at the problem", "B real face reaction": "Real person reacting or pointing at the problem",
         "object close-up + big text": "Object close-up with text (no face, or hands only)", "C hands + object + text": "Object close-up with text (no face, or hands only)",
         "D object close-up + text": "Object close-up with text (no face, or hands only)",
         "product/hands close-up, little or no text": "Product, hands or work scene, little or no text", "E frame grab / work scene, little or no text": "Product, hands or work scene, little or no text",
         "L product shot / brand layout": "Product, hands or work scene, little or no text",
         "diagram/animated explainer": "Diagram or animated explainer", "J diagram / 3D / animated explainer": "Diagram or animated explainer",
         "right/wrong or before/after split": "Before/after or right/wrong split", "F before/after or comparison split": "Before/after or right/wrong split",
         "fire/explosion/spark test": "Real fire, sparks or burn close-up", "G hazard close-up (fire/burn), no face": "Real fire, sparks or burn close-up",
         "AI person or persona": "AI person or persona", "H AI person + hazard/object": "AI person or persona",
         "AI hazard scene + text": "AI scene, no person", "I AI scene, no person": "AI scene, no person",
         "news/footage still": "News or footage still", "K text slide / screenshot": "Text slide or screenshot"}
groups = defaultdict(list)
for r in rows:
    sg = (r.get("style_group") or "unlabelled").strip()
    groups[UNIFY.get(sg, sg)].append(r)
order = sorted(groups, key=lambda g: -statistics.median([r["_v"] for r in groups[g]]))
def share(L, f): return f"{100*sum(1 for r in L if f(r))/len(L):.0f}%" if L else ""
top = [r for r in rows if r["_v"] >= q75]; rest = [r for r in rows if r["_v"] < q75]
els = [("Real face", lambda r: "real face" in (r.get("face") or "").lower()),
       ("AI face", lambda r: "ai face" in (r.get("face") or "").lower()),
       ("Hands only", lambda r: "hands" in (r.get("face") or "").lower()),
       ("AI-made image", lambda r: "ai" in (r.get("look") or "").lower()),
       ("Any arrow", lambda r: (r.get("arrows") or "none").lower() not in ("none", "", "n")),
       ("Red X / green check", lambda r: (r.get("red_green_marks") or "none").lower() not in ("none", "")),
       ("Fire or sparks", lambda r: (r.get("fire_or_sparks") or "").lower().startswith("y")),
       ("No text", lambda r: str(r.get("text_word_count") or "0").strip() in ("0", "")),
       ("1-3 words", lambda r: str(r.get("text_word_count") or "0").strip().isdigit() and 1 <= int(r["text_word_count"]) <= 3),
       ("4+ words", lambda r: str(r.get("text_word_count") or "0").strip().isdigit() and int(r["text_word_count"]) >= 4)]
sets = Counter(s for r in rows for s in r["_set"].split(";") if s)
css = """
:root{--paper:#f3f4f2;--panel:#ffffff;--ink:#1d2328;--muted:#5d6872;--rule:#d5d9dc;--amber:#a86a00;--amber-soft:#f6e7c8;--chip:#e9ecee;
--display:'Barlow Condensed',ui-sans-serif,'Arial Narrow',sans-serif;--body:'Source Sans 3',ui-sans-serif,system-ui,sans-serif;--mono:'IBM Plex Mono',ui-monospace,Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#15191c;--panel:#1d2226;--ink:#e6e9eb;--muted:#9aa4ac;--rule:#30373c;--amber:#f0b440;--amber-soft:#3a2f17;--chip:#262c31;color-scheme:dark}}
:root[data-theme="dark"]{--paper:#15191c;--panel:#1d2226;--ink:#e6e9eb;--muted:#9aa4ac;--rule:#30373c;--amber:#f0b440;--amber-soft:#3a2f17;--chip:#262c31;color-scheme:dark}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.5}
.wrap{max-width:1240px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px;display:grid;gap:28px}
h1{font-family:var(--display);font-weight:700;font-size:clamp(34px,5vw,52px);line-height:1;letter-spacing:.01em;margin:0;text-wrap:balance}
h2{font-family:var(--display);font-weight:600;font-size:26px;margin:0;text-wrap:balance}
.lede{max-width:68ch;color:var(--muted);margin:8px 0 0}
.lede b{color:var(--ink)}
.tables{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:20px}
.tbl{background:var(--panel);border:1px solid var(--rule);border-radius:6px;padding:14px 16px;min-width:0;overflow-x:auto}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}
th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--rule);font-size:14px;vertical-align:top}
th{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:500}
td.n{text-align:right;white-space:nowrap}
.filters{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.filters span{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-right:4px}
.filters button{font:inherit;font-size:13px;border:1px solid var(--rule);background:var(--panel);color:var(--ink);border-radius:999px;padding:4px 12px;cursor:pointer}
.filters button[aria-pressed="true"]{background:var(--amber-soft);border-color:var(--amber);color:var(--ink)}
.filters button:focus-visible{outline:2px solid var(--amber);outline-offset:2px}
section.g{display:grid;gap:12px}
.ghead{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:baseline;border-top:3px solid var(--ink);padding-top:10px}
.ghead .stat{font-family:var(--mono);font-size:12px;color:var(--muted)}
.ghead .stat b{color:var(--amber);font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,230px),1fr));gap:14px}
.card{background:var(--panel);border:1px solid var(--rule);border-radius:6px;overflow:hidden;display:flex;flex-direction:column;min-width:0}
.card img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;background:var(--chip)}
.card .b{padding:8px 10px 10px;display:grid;gap:4px;min-width:0}
.views{font-family:var(--display);font-weight:700;font-size:22px;line-height:1}
.views small{font-family:var(--mono);font-weight:400;font-size:11px;color:var(--muted);margin-left:6px;letter-spacing:.04em}
.t{font-size:13px;line-height:1.3;overflow-wrap:anywhere}
.t a{color:var(--ink);text-decoration:none}.t a:hover{text-decoration:underline}
.ch{font-size:12px;color:var(--muted);overflow-wrap:anywhere}
.tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:2px}
.tags i{font-style:normal;font-family:var(--mono);font-size:10.5px;background:var(--chip);border-radius:3px;padding:1px 5px;color:var(--muted)}
.tags i.txt{background:var(--amber-soft);color:var(--ink)}
.note{font-size:13px;color:var(--muted);max-width:80ch}
@media (prefers-reduced-motion:no-preference){.card{transition:transform .15s}.card:hover{transform:translateY(-2px)}}
"""
o = ["<title>Electrical Thumbnail Styles</title>", '<meta name="claude:viewport-fit-sides" content="cover">',
     '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
     '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Sans+3:wght@400;600&display=swap">',
     f"<style>{css}</style>", '<div class="wrap">', "<header>", "<h1>Electrical Thumbnail Styles</h1>",
     f'<p class="lede">{len(rows)} thumbnails from the electrical and fire-safety study for Frederick Barnes\'s new channel: the all-time top 100, the top winners of the last 90 days and 12 months, and the five biggest videos of 50 main channels. Grouped by style, biggest style first; views are under each picture (exact or rounded YouTube counts, 2026-10-26). <b>Every label is a reading of the picture.</b> AI-made pictures appear almost only in recent uploads, so compare recent with recent.</p>',
     "</header>", '<div class="tables">', '<div class="tbl"><table><thead><tr><th>Style</th><th>Thumbnails</th><th>Median views</th><th>In the top 25%</th></tr></thead><tbody>']
for g in order:
    L = groups[g]; o.append(f"<tr><td>{E(g)}</td><td class='n'>{len(L)}</td><td class='n'>{fmtv(int(statistics.median([r['_v'] for r in L])))}</td><td class='n'>{share(L, lambda r: r['_v'] >= q75)}</td></tr>")
o.append(f"</tbody></table><p class='note'>Top 25% = {fmtv(q75)} views or more.</p></div>")
o.append('<div class="tbl"><table><thead><tr><th>Element</th><th>Top 25%</th><th>The rest</th></tr></thead><tbody>')
for name, f in els: o.append(f"<tr><td>{name}</td><td class='n'>{share(top, f)}</td><td class='n'>{share(rest, f)}</td></tr>")
o.append(f"</tbody></table><p class='note'>{len(top)} thumbnails in the top 25%, {len(rest)} in the rest. The top 25% are mostly older videos, before AI pictures were common.</p></div></div>")
o.append('<div class="filters" role="group" aria-label="Show"><span>Show</span><button type="button" data-set="all" aria-pressed="true">All</button>')
for s, n in sets.most_common(): o.append(f'<button type="button" data-set="{E(s)}" aria-pressed="false">{E(s)} ({n})</button>')
o.append("</div>")
for g in order:
    L = groups[g]
    o.append(f'<section class="g"><div class="ghead"><h2>{E(g)}</h2><span class="stat"><b>{len(L)}</b> thumbnails · median <b>{fmtv(int(statistics.median([r["_v"] for r in L])))}</b> views</span></div><div class="grid">')
    for r in L:
        tags = []
        tw = (r.get("text_words") or "").strip()
        if tw and tw.lower() != "none": tags.append(f'<i class="txt">“{E(tw[:60])}”</i>')
        for k, lab in (("face", ""), ("arrows", "arrow "), ("red_green_marks", ""), ("look", "")):
            v = (r.get(k) or "").strip()
            if v and v.lower() not in ("none", "n", ""): tags.append(f"<i>{E(lab + v)}</i>")
        if (r.get("fire_or_sparks") or "").lower().startswith("y"): tags.append("<i>fire/sparks</i>")
        src = img(r["video_id"])
        o.append(f'<article class="card" data-sets="{E(r["_set"])}">' + (f'<img loading="lazy" src="{src}" alt="Thumbnail: {E((r.get("who_or_what") or "")[:80])}">' if src else "")
                 + f'<div class="b"><div class="views">{fmtv(r["_v"])}<small>{E(r["_set"])}</small></div>'
                 + f'<div class="t"><a href="https://www.youtube.com/watch?v={E(r["video_id"])}" target="_blank" rel="noopener">{E(r.get("title") or "")}</a></div>'
                 + f'<div class="ch">{E(r.get("channel") or "")}</div><div class="tags">{"".join(tags)}</div></div></article>')
    o.append("</div></section>")
o.append("""<p class="note">Sources: thumbnails/labels-top-recent.csv and thumbnails/labels-channel-top5.csv in the niche-research repository (studies/electrical). Views and labels as of 2026-10-26.</p></div>
<script>
const btns=[...document.querySelectorAll('.filters button')];
btns.forEach(b=>b.addEventListener('click',()=>{btns.forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));
const s=b.dataset.set;document.querySelectorAll('.card').forEach(c=>{c.hidden=!(s==='all'||c.dataset.sets.split(';').includes(s))});
document.querySelectorAll('section.g').forEach(g=>{g.hidden=![...g.querySelectorAll('.card')].some(c=>!c.hidden)})}));
</script>""")
out = os.path.join(T, "thumbnail-styles.html")
open(out, "w").write("\n".join(o))
print(len(rows), "thumbnails;", round(os.path.getsize(out) / 1e6, 1), "MB ->", out)
