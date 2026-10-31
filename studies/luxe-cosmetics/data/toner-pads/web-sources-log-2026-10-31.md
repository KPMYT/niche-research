# Web sources log: PDRN toner pads (pulled 2026-10-31)

About 21 web searches used (2 of them refused: reddit.com is not reachable by the search tool). Amazon was not loaded at all (bot check; brief says do not retry). Reddit direct load returned HTTP 403. camelcamelcamel, ubuy and desertcart returned HTTP 403 (not retried). incidecoder.com redirected to a look-alike domain (inkeedecoder.com); not followed.

## A. The Luxe product itself
| What | Source | Result |
|---|---|---|
| Luxe store catalogues | https://luxecosmetics.co/products.json, https://luxe.com/products.json (same Shopify store, 55 products) | No toner pads listed. Saved: luxecosmetics-co-products-2026-10-31.json, luxe-com-products-2026-10-31.json |
| Luxe imprint / story | https://luxe.com/pages/imprint, /pages/our-story | "Luxe Cosmetics B.V., De Wieken 3, 5708 HN Helmond, KvK 89968336"; footer "Copyright © 2025 Luxe Cosmetics LLC"; "All our products are vegan and cruelty-free." Saved as .txt |
| Toner pads product page | https://luxeresearchlab.com/products/luxe-pads (and /products/luxe-pdrn-toner-pads-sub) | Found via the brand helper's raw files (data/brand/luxeresearchlab-products-2026-10-31.json). Pulled again by this helper: luxeresearchlab-luxe-pads-2026-10-31.json, luxeresearchlab-luxe-pdrn-toner-pads-sub-2026-10-31.json, page text .txt files |
| Product JSON facts | luxe-pads.json | title "Luxe \| PDRN Toner Pads"; vendor "Luxe Cosmetics US"; created 2026-08-04T02:49:57-07:00; published 2026-08-04T12:35:33-07:00; price $59.95; SKU "Pdrn-toner-pads"; grams 388; barcode 199874943640; body_html empty |
| "-sub" variant | luxe-pdrn-toner-pads-sub.json | created 2026-09-16; published 2026-09-21; price $59.99; same SKU |
| Images (7) | cdn.shopify.com/s/files/1/0718/0379/7810/files/... | Saved in images/ (renamed .jpg; they are JPEGs). Upload stamps: 2026-08-04 09:50 UTC (4 images) and 2026-08-19 17:20 UTC (2 jar images) |
| Seller on page | luxeresearchlab.com footer | "Company Name: Luxe Research LLC, Business Address: 30 N Gould St Ste R Sheridan, WY 82801 ... info@luxeresearchlab.com ... +1 (385)-454-6193" |
| Search for the product elsewhere | 9 searches (exact ASIN, "luxe toner pads", "PDRN Revitalizing Gel Pads", TikTok, Walmart, etc.) | Nothing indexed for the Luxe pads anywhere outside luxeresearchlab.com |

## B. Anua comparison (the Luxe formula and images match Anua's)
| What | Source | Result |
|---|---|---|
| Anua product JSON | https://anua.us/products/pdrn-100-hyaluronic-acid-glow-pad.json | "PDRN 100 Hyaluronic Acid Glow Pad", created 2025-05-15, $23.00; "dual-textured design ... peptide-infused fabric side ... smooth gel side" |
| Anua images | anua.us product images (saved images/anua-us-pdrn-glow-pad-img1..8) | Same layouts, wording and claims as the Luxe images, in teal; Anua's carry study footnotes that the Luxe versions drop |
| Anua INCI with ppm | https://www.dodoskin.com/products/anua-pdrn-100-hyaluronic-acid-glow-pad-60p.json | Same INCI order as Luxe's ingredient image; "sodium DNA (100 ppm)" |

## C. Competitor data (retailer JSON, prices on 2026-10-31)
dodoskin.com product JSON files saved as dodoskin-*.json; brand stores: medicube.us, mediheal.com, glowrecipe.com, anua.us. BestReviews article (Amazon prices, updated Feb 2026): https://bestreviews.com/beauty-and-personal-care/skin-care/best-pdrn-pads

## D. Science and market
| Source | Key content |
|---|---|
| Dermatology Times, "Social Media Mythbusters: PDRN serums", Marie Bosslett, 11 Jul 2026 https://www.dermatologytimes.com/view/social-media-mythbusters-pdrn-serums | 50 to 1,500 kDa fragments; >~500 Da unlikely to penetrate intact skin; 27-person split-face Rejuran trial; one small topical plant-PDRN study |
| Kim ST, Pharmaceutics 2025;17(8):1024, https://pmc.ncbi.nlm.nih.gov/articles/PMC12388916/ | PN vs PDRN; MFDS approval of PDRN as pharmaceutical for wound healing; Placentex; cosmetics list it as "sodium DNA" or "hydrolyzed DNA"; strong injection safety record |
| Spate blog (no date; © 2026) https://www.spate.nyc/blog/pdrn-in-skincare-what-the-consumer-data-tells-beauty-brands-about-the-next-big-active | 37.2M avg monthly interactions (Google+TikTok+Instagram), +609.8% YoY; "mature skin" 15.0K, >1,000% YoY; Medicube 5.6M |
| ASINSIGHT PDRN (Amazon US, July 2026) https://www.asinsight.com/market-analysis/US/pdrn | 754,600 units, ~$15.9M, top 50 ASINs; ▼40.2% MoM |
| ASINSIGHT toner pads (Amazon US, Aug 2025 to Jul 2026) https://www.asinsight.com/market-analysis/US/toner-pads | 4,245,200 units / $86.5M over 12 months; July 2026 354K units; no PDRN pad in top 10 |
| Search snippets (not opened): Olive Young "PDRN" searches +695% (Sep 2025 report); Happi/Spate Google +169.6% YoY, TikTok +487.5% YoY; Cureus 2026 systematic review 7 RCTs / 183 participants; IMCAS appraisal of 350+ publications | Reported second-hand; not verified at source |
