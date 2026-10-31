# Web review sources tried, 2026-10-31 (normal page loads only; no retries, no workarounds)
| Source | URL | Result |
|---|---|---|
| luxeresearchlab.com products feed | https://luxeresearchlab.com/products.json?limit=250 | 200; 3 eye-balm listings (luxe-balm 2025-12-03, luxe-korean-under-eye-balm 2026-03-15, luxe-balm-upsells 2026-04-06); saved ../luxeresearchlab-products-2026-10-31.json |
| luxeresearchlab.com product pages (3) | /products/luxe-korean-under-eye-balm, /luxe-balm, /luxe-balm-upsells | 200; same page text on all three; 7 written testimonials in the page; JSON-LD "ratingValue 4.81, reviewCount 73"; Okendo/Yotpo/Loox variables present but null; no review-app reviews on the page |
| luxe.com (= luxe-cosmetics.com store) products feed | https://luxe.com/products.json?limit=250 | 200; 1 eye-balm listing (luxe-korean-under-eye-balm-1, $39.95, created 2026-10-26); same 7 testimonials as earlier pull (../../eye-balm/luxe-product-page-text-2026-10-31.txt) |
| Rival review widgets (Okendo, Yotpo, Stamped on beautyofjoseon.com, drmelaxin.us, medicube.us, us.laneige.com, rocskincare.com) | — | Not pulled. Reviews are not in the page HTML (0 JSON-LD reviews); reading them needs the widget's own data call, and an attempt to locate the widget keys was refused by the session's permission check as circumvention. Respected; not retried. |
| Trustpilot luxeresearchlab.com | https://www.trustpilot.com/review/luxeresearchlab.com | WebFetch: TrustScore 3.5, 2,485 reviews; 5★ 46%, 4★ 10%, 3★ 10%, 2★ 6%, 1★ 28%. 24 reviews on page 1, none mention the eye balm (foundation and delivery). Fetch tool would not return full text word for word. |
| Trustpilot luxe-cosmetics.com | earlier pull ../../eye-balm/trustpilot-luxe-cosmetics-com-webfetch-2026-10-31.txt | reused |
| Cult Beauty eye-balm review pages (Medik8 Illuminating Eye Balm; Versed Smooth Landing Retinol Eye Balm) | cultbeauty.com/...reviews links from a search result | 404 both; not retried |
| WebSearch "Luxe Korean Under Eye Balm" review "stars" customer | — | No verified star average; U-Buy shows 5.0 and "0 ratings" on the same page |
| Amazon | — | Not loaded (brief: bot check; no workaround) |
| Reddit | — | Not loaded (blocked) |
