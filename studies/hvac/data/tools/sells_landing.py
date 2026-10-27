#!/usr/bin/env python3
"""Round 3 'what it sells': load each own-product candidate link once (direct page load, logged out, no search)
and keep the page title, og:title/description, any prices shown, outbound checkout hosts and the first text.
Usage: python3 -I sells_landing.py <cands.json> <out.jsonl>   (skips URLs already saved)"""
import sys, os, re, json, html, subprocess, datetime, time
from concurrent.futures import ThreadPoolExecutor

SKIP = re.compile(r'(cpsc\.gov|familyhandyman\.com|energy\.gov|epa\.gov|\.gov/|wikipedia|housecallpro|calendly|forms\.gle)', re.I)
PRICE = re.compile(r'(?:US)?\$\s?\d[\d,]*(?:\.\d\d)?|£\s?\d+(?:\.\d\d)?|€\s?\d+(?:[.,]\d\d)?')


def one(job):
    cid, url = job
    rec = {'channel_id': cid, 'url': url, 'pulled': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
           'source': 'direct page load (curl, logged out)'}
    time.sleep(0.6)
    u = url if url.startswith('http') else 'https://' + url
    p = subprocess.run(['curl', '-sS', '-L', '-m', '30', '--max-filesize', '5000000', '-A', 'Mozilla/5.0',
                        '-w', '\n__END__ %{http_code} %{url_effective}', u], capture_output=True, text=True, errors='ignore')
    out = p.stdout
    m = re.search(r'\n__END__ (\d+) (\S+)$', out)
    rec['http'] = m.group(1) if m else None
    rec['final_url'] = m.group(2) if m else None
    t = out[:m.start()] if m else out
    if not t.strip():
        rec['error'] = (p.stderr or 'empty')[:200]
        return rec
    def g(rx):
        x = re.search(rx, t, re.I | re.S)
        return html.unescape(x.group(1)).strip()[:300] if x else None
    rec['title'] = g(r'<title[^>]*>(.*?)</title>')
    rec['og_title'] = g(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']*)')
    rec['og_desc'] = g(r'<meta[^>]+(?:property|name)=["\'](?:og:)?description["\'][^>]+content=["\']([^"\']*)')
    body = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S | re.I)
    txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', body))).strip()
    rec['text_start'] = txt[:1200]
    rec['prices_in_text'] = PRICE.findall(txt)[:25]
    ctx = []
    for m in PRICE.finditer(txt):
        win = txt[max(0, m.start() - 90): m.end() + 60]
        if re.search(r'(price|one[- ]time|today|launch|instant|pdf|download|buy|get (it|the|my|instant)|order|bundle|'
                     r'regular|only|now|checkout|add to cart|pay|yours|lifetime|ebook|e-book|book|guide|manual|course)', win, re.I):
            ctx.append(win.strip())
        if len(ctx) >= 6:
            break
    rec['price_context'] = ctx
    # Gumroad / Payhip / Shopify structured prices
    rec['structured_price'] = list(dict.fromkeys(re.findall(
        r'"(?:price|formatted_price|price_cents|priceAmount|display_price)"\s*:\s*"?([^",}]{1,20})', t)))[:8]
    rec['checkout_hosts'] = sorted(set(re.findall(
        r'https?://([a-z0-9.-]*(?:gumroad\.com|payhip\.com|stripe\.com|paypal\.com|lemonsqueezy\.com|buy\.stripe\.com|'
        r'stan\.store|etsy\.com|amazon\.com|amzn\.to|shopify\.com|kajabi\.com|teachable\.com|thinkific\.com|podia\.com|'
        r'sellfy\.com|payhip\.com|skool\.com))', t)))
    return rec


def main():
    cands = json.load(open(sys.argv[1]))
    outp = sys.argv[2]
    done = set()
    if os.path.exists(outp):
        done = {(json.loads(l)['channel_id'], json.loads(l)['url']) for l in open(outp) if l.strip()}
    jobs = []
    for cid, v in cands.items():
        seen = set()
        for c in v['candidates']:
            u = c['url'].split('?')[0]
            if 'amazon' in u or 'amzn' in u or SKIP.search(u) or u in seen:
                continue
            seen.add(u)
            if (cid, u) not in done and len(seen) <= 4:
                jobs.append((cid, u))
    print(len(jobs), 'pages to load', flush=True)
    with open(outp, 'a') as f, ThreadPoolExecutor(3) as ex:
        for r in ex.map(one, jobs):
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
            f.flush()
    print('done', flush=True)


main()
