"""Builds the thumbnail artist brief (HTML page + markdown). Usage: python3 build.py <thumbs_dir> <out_html> <out_md>"""
import sys, base64, html
sys.path.insert(0, '.')
from data import REFNAME, ITEMS
TH, OUT, MD = sys.argv[1:4]
e = html.escape
RULES = [
 "<b>Roger is in every thumbnail.</b> His look and outfit are yours to design. Once he's set, use the same Roger every time.",
 "<b>Not Ray.</b> Never Ray Dutton's face, his navy work shirt or his \"RAY\" name patch.",
 "<b>One main thing</b> in the picture, big and the brightest thing in the frame (brighter than Roger's face).",
 "<b>Text:</b> white capitals with a black outline, or white capitals on a solid red band (like Ray's). 4 words or fewer. Never cover Roger's face or hands.",
 "<b>One red arrow or one red circle</b>, never both. No check marks or X marks. No zoom circles or magnifier bubbles.",
 "<b>Looks like a real photo.</b> Bright, even light. Winter cues where it fits: frost on a window, snow outside.",
 "<b>No brand logos</b> (plain bottles and boxes).",
 "<b>Don't copy the references.</b> Take only what the \"Keep\" line says.",
]
def img(i): return 'data:image/jpeg;base64,' + base64.b64encode(open(f'{TH}/{i}.jpg','rb').read()).decode()
cards, md = [], ["# Roger the HVAC Guy — thumbnail brief for the artist (batch 1, 16 thumbnails)\n", "## Rules for every thumbnail\n"] + [f"- {html.unescape(r.replace('<b>','**').replace('</b>','**'))}" for r in RULES] + [""]
for n,(t, refs, keep, change, text, avoid) in enumerate(ITEMS, 1):
    rh, rm = [], []
    for r in refs:
        ch, rt, v = REFNAME[r]; url = f'https://www.youtube.com/watch?v={r}'
        rh.append(f'<a class="ref" href="{url}" target="_blank" rel="noopener"><img src="{img(r)}" alt="Reference thumbnail: {e(rt)}" loading="lazy" width="320" height="180"><span><b>{e(ch)}</b> · {v} views<br>{e(rt)}</span></a>')
        rm.append(f"  - {ch}, \"{rt}\" ({v} views): {url}")
    cards.append(f'''<article class="card" id="t{n}"><h2><span class="n">{n}</span>{e(t)}</h2>
<div class="refs">{''.join(rh)}</div>
<dl><dt>Keep</dt><dd>{e(keep)}</dd><dt>Change</dt><dd>{e(change)}</dd><dt>Text</dt><dd class="txt">{e(text)}</dd><dt>Don't</dt><dd>{e(avoid)}</dd></dl></article>''')
    md += [f"## {n}. {t}\n", "- **Reference:**"] + rm + [f"- **Keep:** {keep}", f"- **Change:** {change}", f"- **Text:** {text}", f"- **Don't:** {avoid}", ""]
page = open('template.html').read().replace('%%RULES%%', ''.join(f'<li>{r}</li>' for r in RULES)).replace('%%CARDS%%', '\n'.join(cards))
open(OUT,'w').write(page); open(MD,'w').write('\n'.join(md))
print(len(ITEMS), len(page)//1024, 'KB')
