#!/usr/bin/env python3
"""Round 3 'what it sells': classify each tier A-D channel's description links and text by domain/text rules.
Inputs: master CSV, the descriptions JSONL from sells_fetch.py, the About JSON (DESC text), and optional
review JSON (hand-checked own products, prices from landing pages). Output: census-sells CSV + a candidates JSON.
Usage: python3 -I sells_classify.py <master.csv> <desc.jsonl> <about.json> <review.json|-> <out.csv> <cands.json>
Rules (domain first, then the text on the same description line):
  amazon      amzn.to, amazon.*, a.co, link.amazon, amzn.eu ...      -> affiliate (Amazon)
  own product gumroad, payhip, stan.store, etsy (own shop), lulu, books2read, kit/teachable/thinkific/kajabi/
              podia/systeme/sellfy/lemonsqueezy, or line text says book / e-book / guide / PDF / course /
              checklist / manual / workbook / training / class  (candidates; hand-checked in review.json)
  membership  patreon, /join, 'membership', 'channel member'; tips (buymeacoffee, ko-fi, paypal.me, cash.app,
              venmo) kept as their own category 'tips'
  merch       teespring, spreadshirt, fourthwall, bonfire, redbubble, spring, 'merch', 't-shirt'
  sponsor     'sponsored by', 'sponsor', 'promo code', 'use code', 'discount code', 'paid partnership'
  contractor  phone number + strong service wording (CONTRACT_STRONG) = 'y (rule)'; strong wording alone, or phone +
              weak wording (CONTRACT) = 'possible (rule)'; review.json can set it by hand
  consulting  'consult', 'consultation', '1-on-1', 'one-on-one', 'book a call', calendly, 'virtual help'
  app         apps.apple.com, play.google.com, 'our app', 'download the app'
  newsletter  mailerlite, convertkit, substack, beehiiv, 'newsletter', 'email list'
"""
import sys, re, json, csv, collections, urllib.parse

AMAZON = re.compile(r'(^|\.)(amzn\.to|amzlink\.to|amzn\.eu|amzn\.com|a\.co|amazon\.[a-z.]+|link\.amazon|amazon)$')
RETAIL = {  # domain -> label (third-party retailers / affiliate networks)
    'ebay.us': 'eBay', 'ebay.com': 'eBay', 'geni.us': 'geni.us (link wrapper, mostly Amazon)',
    'walmart.com': 'Walmart', 'homedepot.com': 'Home Depot', 'homedepot.sjv.io': 'Home Depot', 'lowes.com': "Lowe's",
    'alpinehomeair.com': 'AlpineHomeAir', 'supplyhouse.com': 'SupplyHouse', 'hvacdirect.com': 'HVACDirect',
    'filterbuy.com': 'Filterbuy', 'ecomfort.com': 'eComfort', 'acwholesalers.com': 'AC Wholesalers',
    'pexsupply.com': 'PexSupply', 'sylvane.com': 'Sylvane', 'kit.co': 'Kit.co', 'shareasale.com': 'ShareASale',
    'sjv.io': 'Impact (sjv.io)', 'pntrs.com': 'Pepperjam', 'awin1.com': 'Awin', 'linksynergy.com': 'Rakuten',
    'click.linksynergy.com': 'Rakuten', 'tubebuddy.com': 'TubeBuddy', 'vidiq.com': 'vidIQ',
    'epidemicsound.com': 'Epidemic Sound', 'temu.com': 'Temu', 'aliexpress.com': 'AliExpress',
    'acdirect.com': 'AC Direct', 'thehvacstore.com': 'The HVAC Store', 'zoro.com': 'Zoro', 'grainger.com': 'Grainger',
    'northerntool.com': 'Northern Tool', 'harborfreight.com': 'Harbor Freight', 'acpro.com': 'ACPro',
    'mrcool.com': 'MrCool', 'pioneerminisplit.com': 'Pioneer', 'signaturesolar.com': 'Signature Solar',
    'theisozone.com': 'ISO Zone', 'trutechtools.com': 'TruTech Tools', 'refrigerationtechnologies.com': 'Refrigeration Technologies',
    'skillshare.com': 'Skillshare', 'audible.com': 'Audible', 'audibletrial.com': 'Audible', 'nordvpn.com': 'NordVPN',
    'piavpn.com': 'PIA VPN', 'join.robinhood.com': 'Robinhood', 'a.webull.com': 'Webull', 'rocketmoney.com': 'Rocket Money',
    'ecoflow.com': 'EcoFlow', 'bluettipower.com': 'Bluetti', 'jackery.com': 'Jackery', 'anker.com': 'Anker',
    'sensibo.com': 'Sensibo', 'ecobee.com': 'ecobee', 'fieldpiece.com': 'Fieldpiece', 'navac.com': 'NAVAC',
    'klein.tools': 'Klein', 'kleintools.com': 'Klein', 'milwaukeetool.com': 'Milwaukee', 'dewalt.com': 'DeWalt',
    'bestbuy.com': 'Best Buy', 'target.com': 'Target', 'acehardware.com': 'Ace Hardware', 'menards.com': 'Menards',
    'costco.com': 'Costco', 'wayfair.com': 'Wayfair', 'etsy.me': 'Etsy (link)', 'theecoexperts.co.uk': 'The Eco Experts',
    'quotes.theecoexperts.co.uk': 'The Eco Experts', 'screwfix.com': 'Screwfix', 'toolstation.com': 'Toolstation',
    'bit.ly': None, 'tinyurl.com': None, 'rb.gy': None, 'goo.gl': None, 'shorturl.at': None,
}
OWNPLAT = re.compile(r'(gumroad\.com|payhip\.com|stan\.store|lulu\.com|books2read\.com|teachable\.com|thinkific\.com|'
                     r'kajabi\.com|mykajabi\.com|podia\.com|systeme\.io|sellfy\.com|lemonsqueezy\.com|ko-fi\.com/s/|'
                     r'shopify|samcart|thrivecart|clickfunnels|selz\.com|sendowl|payloadz|kdp|smashwords|draft2digital|'
                     r'skool\.com|circle\.so|udemy\.com|etsy\.com|\.etsy\.com|liibro\.com|myreads\.store)')
OWNTEXT = re.compile(r'\b(e-?books?|my (new )?books?\b|the books?\b|books? (are|is) (on sale|out|available)|(order|get|grab) (your|my|the) (copy|book)|guides?\b|pdf|course|masterclass|checklists?|manual|'
                     r'workbook|handbook|blueprint|playbook|training program|online class|cheat ?sheet|printable|'
                     r'field guide|survival guide|toolkit|templates?|manuals?|notes\b|library|vault|binder|almanac|'
                     r'in print|bible\b|my complete|method i teach|system i teach|written down|📘|📕|📖|the letter\b|plans?\b)', re.I)
OWNTEXT2 = re.compile(r'(📘|📕|📖|📗|📙|save (over )?\$[\d,]+|\bbooks?\b|wrote (it )?down|written down|get the\b|grab (the|my|it)|'
                      r'get my\b|the complete\b|in one place|one place|instant (pdf|download)|launch price|\bkit\b|my shop|our shop|'
                      r'shop\b.*(towels|products)|vault\b|ledger\b|library\b|letter\b)', re.I)
MEMBER = re.compile(r'(patreon\.com|youtube\.com/[^ ]*/join\b|channel membership|channel members?\b|become a (channel )?(member|sponsor)|'
                    r'join (this|my|our) channel|skool\.com|locals\.com|subscribestar)', re.I)
TIPS = re.compile(r'(buymeacoffee\.com|buymeacoff\.ee|ko-fi\.com|paypal\.me|paypal\.com/(donate|paypalme)|cash\.app|'
                  r'venmo\.com|\btip jar\b|donat)', re.I)
MERCH = re.compile(r'(teespring|spreadshirt|fourthwall|bonfire\.com|redbubble|creator-spring|\.myspreadshop|printify|'
                   r'\bmerch\b|merchandise|\bt-?shirts?\b|\bhoodies?\b|swag store|gear store)', re.I)
SPONSOR = re.compile(r'(sponsored by|(this|today\'s) (video|episode)( is| was)? (kindly )?sponsored|thanks to \S+ for sponsoring|'
                     r'(today\'s|our|series|this week\'s) sponsor|paid partnership|in partnership with|'
                     r'promo code|discount code|coupon code|use (my |the )?code\b|with (my )?code\b|code at checkout)', re.I)
NOTSPONSOR = re.compile(r'not (a )?sponsored|no sponsors?|isn\'t sponsored|is not sponsored|unsponsored', re.I)
AFFTEXT = re.compile(r'(affiliate|commission|as an amazon associate|i earn from qualifying)', re.I)
CONTRACT = re.compile(r'(serving\b|service area|free estimate|free quote|licensed and insured|licensed & insured|'
                      r'call us|call today|schedule (service|an appointment|your)|we service|our technicians|'
                      r'request service|book (a|your) (service|appointment)|service call|our team|family[- ]owned|'
                      r'locally owned|hvac company|heating and (air|cooling) (company|service)|license #|lic\.? ?#)', re.I)
CONTRACT_STRONG = re.compile(r'(service area|free (estimate|quote)s?|licensed (and|&) insured|schedule (service|an appointment|your (service|appointment))|'
                             r'request (service|an appointment)|book (online|your visit|a visit|an appointment|your appointment)|housecallpro|'
                             r'servicetitan|license ?#|lic\.? ?#|we service|\bServing [A-Z][a-z]+|proudly serving|call (us )?today)', re.I)
PHONE = re.compile(r'(\(\d{3}\)\s?\d{3}[-.\s]\d{4}|\b\d{3}[-.]\d{3}[-.]\d{4}\b|\b0\d{3,4}\s?\d{3}\s?\d{3,4}\b)')
CONSULT = re.compile(r'(consultations?\b|consulting services|we consult|1-on-1|one-on-one|1:1 |book a call|calendly\.com|virtual (help|diagnos|call)|'
                     r'video call|coaching|zoom call|hire me)', re.I)
APP = re.compile(r'(apps\.apple\.com|play\.google\.com|our app\b|download the app|my app\b)', re.I)
NEWS = re.compile(r'(mailerlite|convertkit|substack\.com|beehiiv|kit\.com/|newsletter|email list|mailing list|'
                  r'eepurl\.com|mailchi\.mp|flodesk)', re.I)
PRICE = re.compile(r'(?:US)?\$\s?\d[\d,]*(?:\.\d\d)?|\d+(?:\.\d\d)?\s?(?:USD|dollars)|£\s?\d+(?:\.\d\d)?|€\s?\d+(?:[.,]\d\d)?')
SOCIAL = re.compile(r'(^|\.)(facebook\.com|fb\.com|instagram\.com|twitter\.com|x\.com|tiktok\.com|youtube\.com|youtu\.be|'
                    r'linkedin\.com|pinterest\.com|threads\.net|reddit\.com|discord\.gg|discord\.com|snapchat\.com|'
                    r'linktr\.ee|beacons\.ai|google\.com|goo\.gl|maps\.app\.goo\.gl|g\.page|yelp\.com|nextdoor\.com|'
                    r'bbb\.org|wikipedia\.org|spotify\.com|spoti\.fi|apple\.co|podcasts\.apple\.com)$')


SOURCE_SITES = {'redcross.org', 'wikipedia.org', 'en.wikipedia.org', 'commons.wikimedia.org', 'archive.org', 'creativecommons.org',
                'energystar.gov', 'nfpa.org', 'ul.com', 'consumerreports.org', 'ashrae.org', 'propane.com', 'who.int'}


def host(u):
    if not re.match(r'^[a-z]+://', u):
        u = 'http://' + u
    h = urllib.parse.urlparse(u).netloc.lower()
    return h[4:] if h.startswith('www.') else h


def line_of(desc, text):
    i = desc.find(text) if text else -1
    if i < 0:
        return ''
    s = desc.rfind('\n', 0, i) + 1
    e = desc.find('\n', i)
    e = len(desc) if e < 0 else e
    ln = desc[s:e].strip()
    if len(re.sub(r'https?://\S+', '', ln).strip(' :-|>•*')) < 4:  # link on its own line: take the line above too
        s2 = desc.rfind('\n', 0, max(s - 1, 0)) + 1
        ln = (desc[s2:s].strip() + ' ' + ln).strip()
    return ln[:300]


def plain_links(text):
    return re.findall(r'(?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:com|net|org|to|co|io|shop|store|ly|us|'
                      r'uk|ca|au|app|dev|site|info|biz|me|link|pages\.dev|netlify\.app|vercel\.app)(?:/[^\s)]*)?', text, re.I)


def main():
    master, descp, aboutp, reviewp, outp, candp = sys.argv[1:7]
    rows = [r for r in csv.DictReader(open(master)) if r['tier'] in ('A', 'B', 'C', 'D')]
    vids = collections.defaultdict(list)
    for l in open(descp):
        if l.strip():
            j = json.loads(l)
            vids[j['channel_id']].append(j)
    about = json.load(open(aboutp))['channels']
    review = json.load(open(reviewp))['channels'] if reviewp != '-' else {}
    out, cands = [], {}
    for r in rows:
        cid = r['channel_id']
        cats = collections.OrderedDict()
        def add(cat, ev):
            cats.setdefault(cat, [])
            if ev and ev not in cats[cat] and len(cats[cat]) < 6:
                cats[cat].append(ev)
        aff = collections.Counter()
        own_c, spons, merch_e, mem_e, contr_e, cons_e = [], [], [], [], [], []
        srcs, errs, pulled = [], [], []
        texts = []
        for v in vids.get(cid, []):
            if 'error' in v:
                errs.append(v['id'] + ':' + v['error'])
                continue
            srcs.append(v['id'] + '(' + v['role'].split()[0] + ')')
            pulled.append(v['pulled'][:10])
            d = v.get('description') or ''
            texts.append(('video ' + v['id'], d))
            for lk in v.get('links', []):
                u = lk['url']
                if u.startswith('/') or 'youtube.com/redirect' in u:
                    continue
                h = host(u)
                ln = line_of(d, lk['text'])
                handle_link(u, h, ln, 'video ' + v['id'], add, aff, own_c)
        a = about.get(cid)
        if a:
            ad = a.get('DESC') or ''
            texts.append(('About', ad))
            for u in plain_links(ad):
                handle_link(u, host(u), line_of(ad, u), 'About', add, aff, own_c)
        own_domains = set()
        for src, t in texts:
            low = t
            for m in SPONSOR.finditer(t):
                ln_ = t[t.rfind('\n', 0, m.start()) + 1: (t.find('\n', m.end()) if t.find('\n', m.end()) >= 0 else len(t))]
                if NOTSPONSOR.search(ln_):
                    continue
                s = t.rfind('\n', 0, m.start()) + 1; e = t.find('\n', m.end()); e = len(t) if e < 0 else e
                add('sponsor', (t[s:e].strip()[:200] + ' [' + src + ']'))
            for m in MEMBER.finditer(t):
                s = t.rfind('\n', 0, m.start()) + 1; e = t.find('\n', m.end()); e = len(t) if e < 0 else e
                add('membership', t[s:e].strip()[:160] + ' [' + src + ']')
            for m in TIPS.finditer(t):
                s = t.rfind('\n', 0, m.start()) + 1; e = t.find('\n', m.end()); e = len(t) if e < 0 else e
                add('tips', t[s:e].strip()[:160] + ' [' + src + ']')
            for m in MERCH.finditer(t):
                s = t.rfind('\n', 0, m.start()) + 1; e = t.find('\n', m.end()); e = len(t) if e < 0 else e
                add('merch', t[s:e].strip()[:160] + ' [' + src + ']')
            for m in CONSULT.finditer(t):
                s = t.rfind('\n', 0, m.start()) + 1; e = t.find('\n', m.end()); e = len(t) if e < 0 else e
                add('consulting', t[s:e].strip()[:160] + ' [' + src + ']')
            for m in APP.finditer(t):
                s = t.rfind('\n', 0, m.start()) + 1; e = t.find('\n', m.end()); e = len(t) if e < 0 else e
                add('app', t[s:e].strip()[:160] + ' [' + src + ']')
            for m in NEWS.finditer(t):
                s = t.rfind('\n', 0, m.start()) + 1; e = t.find('\n', m.end()); e = len(t) if e < 0 else e
                add('newsletter', t[s:e].strip()[:160] + ' [' + src + ']')
            if AFFTEXT.search(t):
                add('affiliate_disclosure', AFFTEXT.search(t).group(0) + ' [' + src + ']')
            ph = PHONE.search(t)
            cm = CONTRACT.search(t)
            if ph or cm:
                add('contractor_signal', ((ph.group(0) + ' ') if ph else '') + ((cm.group(0)) if cm else '') + ' [' + src + ']')
        if aff:
            add('affiliate', '')
        rv = review.get(cid, {})
        # hand review (review.json) overrides the own-product candidates, adds categories, and can set contractor
        reviewed = bool(rv)
        prods = rv.get('own_products_detail')
        own_final = rv.get('own_products')
        cats.pop('own_product', None)
        if prods:
            paid = [p for p in prods if not p.get('free')]
            if paid:
                cats['own_product'] = []
            if any(p.get('free') for p in prods):
                cats['free_lead_magnet'] = []
            if any(re.search(r'course|class|workshop', p['kind'], re.I) for p in paid):
                cats['course'] = []
            if any(re.search(r'book|guide|manual|pdf|journal|playbook', p['kind'] + ' ' + p['name'], re.I) for p in paid):
                cats['book_ebook_guide'] = []
        for k in rv.get('add', []):
            cats.setdefault(k, [])
        txt_all = ' '.join(t for _, t in texts)
        strong = CONTRACT_STRONG.search(txt_all)
        weak = CONTRACT.search(txt_all)
        phone = PHONE.search(txt_all)
        contractor = rv.get('contractor')
        if contractor is None:
            if strong and phone:
                contractor = 'y (rule)'
            elif strong or (phone and weak):
                contractor = 'possible (rule)'
            else:
                contractor = 'n'
        cats.pop('contractor_signal', None)
        if own_c:
            cands[cid] = {'name': r['name'], 'tier': r['tier'], 'type': r['type'], 'persona_flag': r['persona_flag'],
                          'candidates': own_c[:12]}
        order = ['own_product', 'book_ebook_guide', 'course', 'free_lead_magnet', 'membership', 'tips', 'merch', 'affiliate',
                 'sponsor', 'consulting', 'app', 'newsletter', 'own_website', 'affiliate_disclosure']
        sells = [c for c in order if c in cats] + [c for c in cats if c not in order]
        if contractor.startswith('y'):
            sells.append('contractor')
        ev = []
        if phone: ev.append('phone ' + phone.group(0))
        if strong: ev.append('"' + strong.group(0) + '"')
        if weak and not strong: ev.append('weak: "' + weak.group(0) + '"')
        out.append({
            'channel_id': cid, 'name': r['name'], 'tier': r['tier'], 'type': r['type'], 'persona_flag': r['persona_flag'],
            'subs': r['subs'],
            'sells_categories': ' ; '.join(sells) if sells else ('not found' if srcs else 'not pulled'),
            'own_products': ' | '.join(own_final) if own_final else ('candidates unchecked: ' + ' | '.join(
                x['line'][:120] for x in own_c[:3]) if own_c and not reviewed else 'not found'),
            'affiliate_domains': ' ; '.join(f'{k} ({n})' for k, n in aff.most_common()) or 'not found',
            'sponsors': ' || '.join(cats.get('sponsor', [])) or 'not found',
            'membership': ' || '.join(cats.get('membership', []) + cats.get('tips', [])) or 'not found',
            'merch': ' || '.join(cats.get('merch', [])) or 'not found',
            'contractor': contractor,
            'contractor_evidence': ('hand-checked; ' if rv.get('contractor') else '') + (' ; '.join(ev) or 'not found'),
            'consulting_app_newsletter': ' || '.join(cats.get('consulting', []) + cats.get('app', []) + cats.get('newsletter', [])) or 'not found',
            'own_website': ' ; '.join(cats.get('own_website', [])) or 'not found',
            'source_video_ids': ' ; '.join(srcs) + ((' ; errors: ' + ' ; '.join(errs)) if errs else ''),
            'about_used': 'yes (DESC text only, no link list)' if a else 'no About record',
            'reviewed': 'hand-checked' if reviewed else 'rules only',
            'review_note': rv.get('note', ''),
            'pulled': (max(pulled) if pulled else 'not pulled') + ' (innertube /next); About 2026-10-24',
        })
    with open(outp, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    json.dump(cands, open(candp, 'w'), indent=1, ensure_ascii=False)
    print(len(out), 'rows;', len(cands), 'own-product candidate channels')


def handle_link(u, h, ln, src, add, aff, own_c):
    if not h or h in ('gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'aol.com') or '@' in u:
        return
    if re.search(r'(\.gov|\.gov\.[a-z]{2}|\.edu|\.mil|\.ac\.uk|\.nhs\.uk)$', h) or h in SOURCE_SITES:
        return  # public/source references, not something sold
    if SOCIAL.search(h):
        if 'youtube.com' in h and '/join' in u:
            add('membership', u + ' [' + src + ']')
        return
    if AMAZON.search(h):
        aff['Amazon'] += 1
        if re.search(r'\b(my|our) (new )?(e-?)?book\b', ln, re.I):
            own_c.append({'src': src, 'url': u, 'line': ln, 'why': 'amazon + "my book"'})
        return
    if OWNPLAT.search(u.lower()):
        own_c.append({'src': src, 'url': u, 'line': ln, 'why': 'platform ' + OWNPLAT.search(u.lower()).group(0)})
        return
    if re.search(r'patreon\.com', u, re.I):
        add('membership', u + ' [' + src + ']'); return
    if TIPS.search(u):
        add('tips', u + ' [' + src + ']'); return
    if MERCH.search(h):
        add('merch', u + ' [' + src + ']'); return
    if APP.search(u):
        add('app', u + ' [' + src + ']'); return
    lab = RETAIL.get(h, 'unknown')
    if lab is None:  # shortener: decide on line text
        if OWNTEXT.search(ln):
            own_c.append({'src': src, 'url': u, 'line': ln, 'why': 'shortener + product word'})
        else:
            aff[h + ' (shortener)'] += 1
        return
    if lab != 'unknown':
        aff[lab] += 1
        return
    for k, v in RETAIL.items():
        if v and h.endswith('.' + k):
            aff[v] += 1
            return
    # unknown domain: own product if the line says so, else note as website (own or third-party)
    if OWNTEXT.search(ln) or OWNTEXT2.search(ln):
        own_c.append({'src': src, 'url': u, 'line': ln, 'why': 'site + product word'})
    elif (SPONSOR.search(ln) or re.search(r'(discount|% off|off with)', ln, re.I) or re.search(r'\b[Cc]ode:? [A-Z0-9]{4,}\b', ln)) \
            and not NOTSPONSOR.search(ln):
        add('sponsor', ln[:200] + ' [' + src + ']')
    elif AFFTEXT.search(ln) or re.search(r'\b(buy|get|check (out|price)|link|shop|recommended|tools? i use|gear)\b', ln, re.I):
        aff[h] += 1
    else:
        add('own_website', h)


main()
