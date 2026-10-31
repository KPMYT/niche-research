# Web review sources, round 2 (2026-10-31)

Normal page loads with plain `curl -L` (no browser automation, no header changes, no retries, no review-widget data feeds). Each page was loaded once.

| Site | Page(s) | Result | What was kept |
|---|---|---|---|
| iherb.com | `/r/dr-melaxin-cemenrete-calcium-volume-multi-balm-0-31-oz-9-g/153305` pages 1–5 | 200. Review text is in the page HTML (10 per page; pages overlap a little) | `iherb-reviews-2026-10-31.json` (stars, title, date, country, text, review link) |
| iherb.com | `/r/d-alba-double-serum-all-in-one-multi-balm-0-35-oz-10-g/137646` pages 1–3 | 200, as above | same file |
| iherb.com | `/r/beauty-of-joseon-revive-eye-serum-ginseng-retinal-1-01-fl-oz-30-ml/115901` pages 1–4 | 200, as above | same file |
| iherb.com | product pages `/pr/...` for the three products | 200, but reviews there load from the review app (`/ugc/api`), not used | listing counts only: Dr.Melaxin 4.5/5 from 731 reviews; d'Alba 4.8/5 from 241; BoJ eye serum 4.6/5 from 33,940 (iHerb search page, 2026-10-31) |
| lookfantastic.com | product pages for The Ordinary Caffeine Solution 5% + EGCG (11396686), Beauty of Joseon Revive Eye Serum (14866956), Kiehl's Creamy Eye Treatment (12916107), The INKEY List Caffeine Eye Cream (14272888) | 200. The 10 newest reviews are in the page's structured data (JSON-LD) | `lookfantastic-reviews-2026-10-31.json` |
| lookfantastic.com | Medicube PDRN Pink Collagen Volume Multi Balm 10 g (18011209) | 200, no reviews in the page | nothing |
| vitacost.com | `/products/kahi-multi-balm-0-31-oz-9-g-136978` and `/products/kahi-eye-balm-9-g-136981` | 200. 30 reviews each in the page's structured data; reviewer shown as "iHerb Customer". Aggregate: Multi Balm 4.56 from 243 reviews, $24.99 (price field 2499 cents); Eye Balm 4.85 from 47 reviews, $24.80 | `vitacost-reviews-2026-10-31.json` |
| cultbeauty.com | search "kahi multi balm" | redirected to "zero results" | nothing |
| ulta.com | one product URL tried | 404 | nothing (not retried) |
| Brand sites (CeraVe, The Ordinary, Beauty of Joseon, Kahi, Medicube) | — | Not loaded this round: the first round found their review text is not in the page HTML (it comes from the review app's data feed, which is not used) | nothing |

The raw HTML pages (about 2 MB each) are not saved; the JSON files hold every field read from them.

Web searches used this round: 0.
