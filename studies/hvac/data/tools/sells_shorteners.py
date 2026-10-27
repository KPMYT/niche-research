#!/usr/bin/env python3
"""Round 3 fix 3.1 (round 3 fixer, 2026-10-26): resolve the URL-shortener links (bit.ly, tinyurl, rb.gy, goo.gl,
shorturl.at) found in the what-it-sells descriptions, so a shortener counts as affiliate only when its line says so
or its TARGET is a shop. Follows up to 4 redirect hops with curl (no page body fetched), records every hop.
Usage: python3 -I sells_shorteners.py <desc.jsonl> <out.json>   (re-uses targets already in <out.json>)"""
import sys, json, subprocess, urllib.parse, concurrent.futures, time, os

SHORT = ('bit.ly', 'tinyurl.com', 'rb.gy', 'goo.gl', 'shorturl.at')


def host(u):
    if '://' not in u:
        u = 'http://' + u
    h = urllib.parse.urlparse(u).netloc.lower()
    return h[4:] if h.startswith('www.') else h


def resolve(u):
    hops, cur = [], u
    for _ in range(4):
        try:
            r = subprocess.run(['curl', '-sS', '-o', '/dev/null', '-m', '20', '-w', '%{http_code} %{redirect_url}', cur],
                               capture_output=True, text=True, timeout=30)
            code, _, loc = r.stdout.strip().partition(' ')
        except Exception as e:  # noqa: BLE001
            hops.append({'url': cur, 'error': str(e)[:120]})
            break
        hops.append({'url': cur, 'status': code, 'location': loc})
        if code.startswith('3') and loc:
            cur = loc
            if host(cur) not in SHORT and host(cur) not in ('amzn.to', 'geni.us', 'a.co', 'amzlink.to'):
                break
        else:
            break
        time.sleep(0.3)
    final = hops[-1].get('location') or hops[-1].get('url')
    return {'url': u, 'final': final, 'final_host': host(final) if final else '', 'hops': hops}


def main():
    descp, outp = sys.argv[1:3]
    urls = set()
    for line in open(descp):
        j = json.loads(line)
        for lk in j.get('links', []):
            if host(lk['url']) in SHORT:
                urls.add(lk['url'])
    done = json.load(open(outp))['links'] if os.path.exists(outp) else {}
    todo = sorted(u for u in urls if u not in done)
    with concurrent.futures.ThreadPoolExecutor(4) as ex:
        for res in ex.map(resolve, todo):
            done[res['url']] = res
    json.dump({'pulled': '2026-10-26', 'by': 'round 3 fixer (curl redirect hops, logged out, no page bodies)',
               'note': 'final = the last Location seen; a 200 on the first hop means the shortener did not redirect',
               'links': done}, open(outp, 'w'), indent=1)
    print(len(urls), 'shortener links;', len(todo), 'resolved now')


if __name__ == '__main__':
    main()
