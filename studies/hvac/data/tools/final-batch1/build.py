"""Builds the batch 1 sign-off pack for Roger the HVAC Guy: per video, the idea, the thumbnail
instructions and the brief, in that order. Reads the greenlit log, the briefs TSV and the artist-brief data.
Usage (from this folder): python3 build.py   -> writes ../../../ideation/batch1-final-2026-10-27.{html,md,xlsx}"""
import sys, csv, base64, html, os, re
sys.path.insert(0, '../artist-brief')
from data import REFNAME, ITEMS
H = '../../..'; IDE = f'{H}/ideation'; TH = f'{H}/thumbnails/artist-refs'
OUT = f'{IDE}/batch1-final-2026-10-27'
e = html.escape
# the idea: format and source from the greenlit log
LOG = {}
for line in open(f'{IDE}/greenlit-log.md'):
    m = re.match(r'\| (\d+) \| (.+?) \| (.+?) \| (.+?) \|$', line.strip())
    if m: LOG[int(m.group(1))] = (m.group(2), m.group(3), m.group(4))
BR = list(csv.reader(open(f'{IDE}/batch1-briefs-2026-10-26.tsv'), delimiter='\t'))[1:]
assert len(LOG) == len(BR) == len(ITEMS) == 16
for n in range(16): assert LOG[n+1][0] == BR[n][0] == ITEMS[n][0], n
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
cards, toc, md = [], [], ["# Roger the HVAC Guy — batch 1, final (16 videos)\n",
  "For each video: 1. the idea, 2. the thumbnail instructions, 3. the video brief. Built 2026-10-27 from `greenlit-log.md`, `batch1-thumbnail-brief.md` and `batch1-briefs-2026-10-26.tsv`.\n",
  "## Thumbnail rules for every video\n"] + [f"- {html.unescape(r.replace('<b>','**').replace('</b>','**'))}" for r in RULES] + [""]
rows = []
for n,(t, refs, keep, change, text, avoid) in enumerate(ITEMS, 1):
    _, fmt, src = LOG[n]; _, ref, brief = BR[n-1]
    rh, rm = [], []
    for r in refs:
        ch, rt, v = REFNAME[r]; url = f'https://www.youtube.com/watch?v={r}'
        rh.append(f'<a class="ref" href="{url}" target="_blank" rel="noopener"><img src="{img(r)}" alt="Reference thumbnail: {e(rt)}" loading="lazy" width="320" height="180"><span><b>{e(ch)}</b> · {v} views<br>{e(rt)}</span></a>')
        rm.append(f"  - {ch}, \"{rt}\" ({v} views): {url}")
    toc.append(f'<li><a href="#v{n}">{e(t)}</a></li>')
    cards.append(f'''<article class="card" id="v{n}"><h2><span class="n">{n}</span>{e(t)}</h2>
<section class="step"><h3>1 · Idea</h3><dl><dt>Format</dt><dd>{e(fmt)}</dd><dt>Built from</dt><dd>{e(ref)}</dd></dl></section>
<section class="step"><h3>2 · Thumbnail</h3><div class="refs">{''.join(rh)}</div>
<dl><dt>Keep</dt><dd>{e(keep)}</dd><dt>Change</dt><dd>{e(change)}</dd><dt>Text</dt><dd class="txt">{e(text)}</dd><dt>Don't</dt><dd>{e(avoid)}</dd></dl></section>
<section class="step"><h3>3 · Video brief</h3><p class="brief">{e(brief)}</p></section></article>''')
    md += [f"## {n}. {t}\n", "**1. Idea**", f"- Format: {fmt}", f"- Built from: {ref}", "",
           "**2. Thumbnail**", "- Reference:"] + rm + [f"- Keep: {keep}", f"- Change: {change}", f"- Text: {text}", f"- Don't: {avoid}", "",
           "**3. Video brief**", "", brief, ""]
    thumb = "Reference: " + "; ".join(f'{REFNAME[r][0]}, "{REFNAME[r][1]}" ({REFNAME[r][2]}) https://www.youtube.com/watch?v={r}' for r in refs) + \
            f"\nKeep: {keep}\nChange: {change}\nText: {text}\nDon't: {avoid}"
    rows.append([n, t, fmt, ref, thumb, brief])
page = open('template.html').read().replace('%%RULES%%', ''.join(f'<li>{r}</li>' for r in RULES)) \
    .replace('%%TOC%%', ''.join(toc)).replace('%%CARDS%%', '\n'.join(cards))
open(OUT+'.html','w').write(page); open(OUT+'.md','w').write('\n'.join(md))
import openpyxl
from openpyxl.styles import Alignment, Font
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'Batch 1 final'
ws.append(['#','Title','Format','Reference','Thumbnail','Brief'])
for c in ws[1]: c.font = Font(bold=True)
for r in rows: ws.append(r)
for col,wid in zip('ABCDEF',(4,44,22,40,60,110)): ws.column_dimensions[col].width = wid
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical='top')
ws2 = wb.create_sheet('Thumbnail rules')
for r in RULES: ws2.append([html.unescape(re.sub('</?b>','',r))])
ws2.column_dimensions['A'].width = 120
wb.save(OUT+'.xlsx')
print(len(rows), len(page)//1024, 'KB')
