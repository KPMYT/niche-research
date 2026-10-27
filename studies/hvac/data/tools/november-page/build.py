import base64, html, sys
sys.path.insert(0, sys.argv[1])
import data
D = sys.argv[1]
def b64(i): return 'data:image/jpeg;base64,' + base64.b64encode(open(f'{D}/th/{i}.jpg','rb').read()).decode()
def fmt(v):
    return f'{v/1e6:.1f}M' if v >= 1e6 else (f'{round(v/1000)}K' if v >= 1000 else str(v))
KIND = {'Ray':'Ray Dutton','yours':'Your channel','competitor':'Competitor','real person':'Real person'}
thumbs = {i: b64(i) for i in data.R}
css_imgs = ''.join(f'.t-{k.replace("-","_").replace(" ","")}{{background-image:url({v})}}\n' for k,v in [])  # unused
out = []
n = 0
for gi,(name, blurb, items) in enumerate(data.G):
    out.append(f'<section class="grp" id="g{gi}"><header class="gh"><h2>{html.escape(name)}</h2><p>{html.escape(blurb)} <span class="cnt">{len(items)} titles</span></p></header><ol class="list">')
    for (bn, title, refs) in items:
        n += 1
        rs = []
        for r in refs:
            t, ch, v, d, k = data.R[r]
            rs.append(f'<a class="ref" href="https://www.youtube.com/watch?v={r}" target="_blank" rel="noopener"><img src="{thumbs[r]}" alt="" loading="lazy" width="160" height="90"><span class="rt"><b class="views">{fmt(v)}</b><span class="pill k-{k.replace(" ","")}">{KIND[k]}</span><span class="src">{html.escape(t)}</span><span class="ch">{html.escape(ch)} · {d}</span></span></a>')
        out.append(f'<li class="row" data-id="{bn}"><label class="pick"><input type="checkbox" id="p{bn}" data-title="{html.escape(title)}"><span class="no">{n}</span><span class="title">{html.escape(title)}</span></label><div class="refs">{"".join(rs)}</div></li>')
    out.append('</ol></section>')
total = n
page = open(f'{D}/template.html').read().replace('%%BODY%%', '\n'.join(out)).replace('%%TOTAL%%', str(total))
open(sys.argv[2],'w').write(page)
print(total, len(page)//1024, 'KB')
