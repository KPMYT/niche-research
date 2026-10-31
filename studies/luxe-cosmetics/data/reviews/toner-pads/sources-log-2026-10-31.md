# Sources log: reviews for product 2 (PDRN toner pads), pulled 2026-10-31

Method: normal page loads (curl, one load per page) and NexLev. Reviews were read from the review text that each page itself serves in its HTML (JSON-LD "Review" blocks, Ulta's embedded review block, Okendo/Judge.me server-rendered widgets, Lyko's page data). No review-app API was called directly: one attempt to call Okendo's public review API for anua.us was refused by this machine's permission system as a bot-check workaround, and per the brief it was not retried or worked around. That is why each store gives only its first page of reviews (usually 3 to 10) while the store's total count is higher.

| Source | URL | Product | Store total shown | Reviews read | File |
|---|---|---|---|---|---|
| luxeresearchlab.com (brand's own site) | https://luxeresearchlab.com/products/luxe-pads | Luxe PDRN Toner Pads | page badge "Rated 4.86 (10,839 reviews)"; product metafield rating 4.96 from 72 | 7 page testimonials (no review app on the page) | data/brand/luxeresearchlab-product-luxe-pads-2026-10-31.html (earlier pull) |
| anua.us (brand) | https://anua.us/products/pdrn-100-hyaluronic-acid-glow-pad | Anua PDRN 100 HA Glow Pad | 4.9 / 15 (Okendo) | 3 | anua-us-glow-pad-okendo-embedded-2026-10-31.json |
| anua.com | same store as anua.us (identical page) | | | 0 extra | |
| Ulta | https://www.ulta.com/p/pdrn-100-hyaluronic-acid-glow-pad-pimprod2052157 | Anua glow pad | 4.8 / 124 | 5 recent + 2 "most helpful" | ulta-anua-glow-pad-embedded-reviews-2026-10-31.json |
| Cult Beauty | https://www.cultbeauty.com/p/anua-pdrn-100-hyaluronic-acid-glow-pad-180ml/16674994/ | Anua glow pad | 4.67 / 18 | 10 | cultbeauty-anua-glow-pad-jsonld-reviews-2026-10-31.json |
| Lookfantastic UK | https://www.lookfantastic.com/p/anua-pdrn-100-hyaluronic-acid-glow-pad-180ml/16674994/ | Anua glow pad | 4.68 / 44 | 10 (DE site shows the same 10) | lookfantastic-anua-glow-pad-jsonld-reviews-2026-10-31.json |
| Sephora Middle East | https://www.sephora.me/qa-en/p/pdrn-100-hyaluronic-acid-glow-pad/P1000212554 | Anua glow pad | 4.11 / 19 | 10 | sephorame-anua-glow-pad-jsonld-reviews-2026-10-31.json |
| Vitacost (iHerb reviews) | https://www.vitacost.com/products/anua-pdrn-100-hyaluronic-acid-glow-pad-60-pads-155440 | Anua glow pad | 4.60 / 20 | 20 | vitacost-anua-glow-pad-jsonld-reviews-2026-10-31.json |
| iHerb | https://www.iherb.com/pr/anua-pdrn-100-hyaluronic-acid-glow-pad-60-pads/155440 | Anua glow pad | 4.7 / 127 | 0 (no text in page) | |
| Lyko (Sweden/Norway; auto-translated by Lyko) | https://lyko.com/en/k-beauty/k-beauty-skincare/face/essence/anua-pdrn-100-hyaluronic-acid-glow-pad-180ml | Anua glow pad | 5.0 / 2 shown in variant data | 3 | lyko-anua-glow-pad-reviews-2026-10-31.json |
| dodoskin | https://www.dodoskin.com/products/anua-pdrn-100-hyaluronic-acid-glow-pad-60p | Anua glow pad | 5.0 / 1 | 1 | dodoskin-anua-glow-pad-judgeme-2026-10-31.json |
| Song of Skin (Canada) | https://songofskin.com/products/anua-pdrn-100-hyaluronic-acid-glow-pad | Anua glow pad | 1 | 1 | songofskin-anua-glow-pad-judgeme-2026-10-31.json |
| StyleKorean | https://www.stylekorean.com/shop/anua-pdrn-100-hyaluronic-acid-glow-pad-60ea/1749609643/ | Anua glow pad | 4.9 / 19 | 0 (no text in page) | raw-stylekorean-2026-10-31.html |
| Sephora UK, Superdrug | | Anua glow pad | | HTTP 403, not retried | |
| John Lewis | | Anua glow pad | | transfer cut off, not retried | |
| Hwahae | https://www.hwahae.com/en/products/2133064 | | | HTTP 202 empty, not retried | |
| YesStyle, Stylevana, Olive Young Global, Target | | | | no product page found by search; not loaded | |
| Lookfantastic / Cult Beauty | /p/medicube-pdrn-pink-collagen-toning-gel-toner-pad-70ea/17748312/ | Medicube PDRN Pink Collagen Toning Gel Toner Pad | LF 4.63 / 8; CB 5 / 1 | 8 + 1 | lookfantastic-/cultbeauty-medicube-pdrn-... |
| Ulta | /p/pdrn-pink-collagen-toning-gel-toner-pad-pimprod2056605 | Medicube PDRN pad | 3.5 / 6 | 5 | ulta-pdrn-pink-collagen-... |
| medicube.us (brand) | https://medicube.us/products/pdrn-pink-collagen-gel-toner-pad | Medicube PDRN pad | 4.77 / 78 (Stamped) | 0 (no text in page) | brand-medicube.us_...html |
| dodoskin | | Medicube PDRN pad | 1 | 1 | dodoskin-medicube-pdrn-pads-judgeme-2026-10-31.json |
| mediheal.com (brand) | https://mediheal.com/products/pdrn-lifting-pad | Mediheal PDRN Lifting Pad | 4.76 / 72 (Yotpo) | 0 (no text in page) | brand-mediheal.com_...html |
| Ulta | /p/pdrn-tension-toner-pad-pimprod2056429 | VT PDRN Tension Toner Pad | 5 / 6 | 5 | ulta-pdrn-tension-... |
| glowrecipe.com (brand) | https://www.glowrecipe.com/products/pdrn-repair-and-soothe-korean-toner-pads | Glow Recipe PDRN+ Repair + Soothe Korean Toner Pads | 122 reviews (Okendo); reviewer ages 35-44: 46, 25-34: 28, 45-54: 20, 65+: 8, 55-64: 6 | 5 | glowrecipe-pdrn-pads-okendo-embedded-2026-10-31.json |
| Lookfantastic | Biodance Collagen / Cera-nol / Sea Kelp / Vita Niacinamide Gel Toner Pads | 4.58/12, 5/7, 5/3, 5/3 | 10 + 7 + 3 + 3 | lookfantastic-biodance-... |
| Cult Beauty | Biodance Collagen Gel Toner Pads | 5 / 2 | 2 | cultbeauty-biodance-... |
| Lookfantastic | Mediheal Collagen Ampoule Pad; Watermide Moisturise Pad | 4.73 / 11; 4.8 / 5 | 10 + 5 | lookfantastic-mediheal-... |
| Ulta | Mediheal Collagen Ampoule Pad; Retinol Collagen Lifting Pad; Watermide Moisture Pad | 4.7/594; 4.6/321; 4.6/229 | 7 + 7 + 7 | ulta-collagen-ampoule-..., ulta-retinol-..., ulta-watermide-... |
| Lookfantastic / Ulta | Anua Heartleaf 77 Clear Pad | LF 4.63/8; Ulta 4.7/162 | 8 + 7 | |
| Lookfantastic / Ulta | Medicube Zero Pore Pad (Mild / original) | LF 4.72/98; Ulta 3.9/209 | 10 + 7 | |
| Ulta | Mixsoon Collagen Hydrating Toner Pad; Sungboon Editor Deep Collagen Retinol Pad; Round Lab Birch Juice Pad; belif Aqua Bomb PHA Pads; SKIN1004 Jelly-Fit Pads; numbuzin No.5+ Pads | 5/2; 4.2/5; 5/48; 5/8; 5/1; 5/1 | 2+5+5+5+1+1 | ulta-*.json |
| dodoskin | Isntree PDRN pad; Mixsoon collagen pad; Rejuran pore pad; SNP PDRN pad | 1; 1; 2; 1 | 5 | dodoskin-*-judgeme-*.json |
| dodoskin | Biodance Caviar PDRN, COSRX peptide collagen, Mediheal PDRN, SKINFOOD carrot PDRN, VT PDRN pads | 0 reviews each | 0 | |
| YouTube (NexLev) | see youtube-comments-batch1/2 and ../../toner-pads/youtube-pulls-2026-10-31.md | | | | |

Web searches used by this helper: 5.
