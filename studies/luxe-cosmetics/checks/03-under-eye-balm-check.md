# Check of `03-under-eye-balm.md` (Luxe Korean Under Eye Balm, ASIN B0GYK3T766)

Checked 2026-10-31 by a second helper, working independently of the original helper. All pages were re-loaded live on 2026-10-31 and none of the original helper's files were used as evidence. Its saved SellerRatings and liza.nl files only pointed me to URLs, which I then re-fetched myself.

- **Amazon was not loaded.** I made no attempt to get around the bot check.
- **Budget used:** 7 web searches and 3 WebFetch calls. Direct page loads (curl), PubMed E-utilities and NexLev are not counted.
- **My working files** (not part of the repo) are in `/tmp/claude-0/-home-user-niche-research/b5781892-4d1f-54af-adb3-1b967b21b5f7/scratchpad/chk/` and `.../scratchpad/img/`.

Verdicts: **confirmed**, **partly confirmed**, **wrong**, **unverifiable**.

---

## 1. Who sells it: Luxe Cosmetics B.V., Luxe Research LLC and the Amazon store

### 1a. The brand site at $39.95 with "Buy 1, Get 1 Free"

**Verdict: confirmed, with a domain correction.**

- **The domain has moved.** `https://luxe-cosmetics.com/` now redirects to `https://luxe.com/` (curl, HTTP 200 at luxe.com). The report calls the site "luxe-cosmetics.com" throughout; today it is **luxe.com**, and luxe-cosmetics.com is only the old address.
- **Price.** `https://luxe.com/products/luxe-korean-under-eye-balm-1.json` gives:
  - title "Luxe | Korean Under Eye Balm";
  - vendor "Luxe Research";
  - SKU "Eye-Balm-blue", price 39.95, no compare-at price, weight 0;
  - created 2026-10-26T07:49:39-07:00.
- **Banner.** The live product page `https://luxe.com/products/luxe-korean-under-eye-balm-1` shows "BUY 1, GET 1 FREE 30-Day Full Refund Ships Today 10,000+ Mature Women".

### 1b. Luxe Cosmetics B.V., Helmond

**Verdict: confirmed as the imprint, with two details to add.**

- **Imprint.** `https://luxe.com/pages/imprint` reads: "Luxe Cosmetics B.V. De Wieken 3 5708 HN HELMOND Nordbrabant KvK-number: 89968336 … E-Mail: info@luxe-cosmetics.com … Phone number: +49 17695833240". The footer reads "Copyright © 2025 Luxe Cosmetics LLC".
- **Registry.** liza.nl (`https://www.liza.nl/en/89968336/luxe-cosmetics`, fetched 2026-10-31) lists Luxe Cosmetics BV, KvK 89968336, at De Wieken 3, **5707 CW** Helmond. The imprint says 5708 HN, so the postcode differs. The company was founded **19-04-2023** and has not yet filed financial statements.
- **Detail the report missed.** The luxe.com Shopify store describes itself, at `https://luxe.com/meta.json`, as **"Luxe Cosmetics US", city "Sheridan", province "Wyoming"**, with myshopify domain `luxe-cosmetics-us.myshopify.com`. So the luxe.com store itself is registered to Sheridan, Wyoming. Only the imprint names the Dutch B.V.

### 1c. How luxe.com (Luxe Cosmetics B.V.) and luxeresearchlab.com (Luxe Research LLC) relate

**Reading: the same operators or the same business, running two Shopify stores. The evidence is strong. It does not prove the legal relationship.**

| Evidence | luxe.com | luxeresearchlab.com |
|---|---|---|
| Company named on the site | Luxe Cosmetics B.V., Helmond (imprint); "© 2025 Luxe Cosmetics LLC" (footer) | "Luxe Research LLC, 30 N Gould St Ste R, Sheridan, WY 82801", +1 385-454-6193, info@luxeresearchlab.com (`/policies/refund-policy` and footer) |
| Shopify store record (`/meta.json`) | name "Luxe Cosmetics US", Sheridan, Wyoming; `luxe-cosmetics-us.myshopify.com` | name "Luxe Research", Kansas City, Missouri; **`luxe-cosmetics-denmark.myshopify.com`** |
| Vendor field on products | The eye balm on luxe.com has vendor **"Luxe Research"**. The store's vendors are Luxe Cosmetics, Luxe Cosmetics US, Luxe Cosmetics US3, Luxe Cosmetics US 4, Luxe Research and Carisma. | Products carry vendor "Luxe Research", "Luxe Research US" and **"Luxe Cosmetics US"**. The toner pads, eyelash serum and lash-lift kits all use "Luxe Cosmetics US". |
| Eye balm listings | `luxe-korean-under-eye-balm-1`: $39.95, SKU **Eye-Balm-blue**, created 2026-10-26 | Three listings, **all with SKU Eye-Balm-blue**: `luxe-balm` (created **2025-12-03**, published 2026-03-02, $34.99, was $39.95); `luxe-korean-under-eye-balm` (created 2026-03-15, $34.99, was $39.95); `luxe-balm-upsells` (created 2026-04-06, $34.95) |
| Shared image file | `Imagev4.png` (the "No More Dry Wrinkly Under Eyes Ever!" collage) | The same filename `Imagev4.png` on `luxe-balm`, uploaded 2026-02-21 |
| Shared reviews and testimonials | "Rated 4.86 (10,839 reviews)". Six "Verified Buyer" testimonials: Margaret T. 56 (Feb 11th, 2026), Diane K. 52 (Jan 24th), Susan L 47 (Feb 18th), Linda R. 51 (Jan 13th), Carol A 63 (Feb 15th), Barbara M 43 (Dec 28th, 2025) | "Rated 4.8/5 based on +10,839 Total Ratings". **The same six names, ages, purchase dates and "$34.99 $39.95" price line.** |
| Ad tracking | — | The Voluum tracking app is set to `"voluumDomain":"track.luxe-cosmetics.com"`, so luxeresearchlab.com sends its ad clicks through a **luxe-cosmetics.com** subdomain. |
| Google tags | AW-11002447260, G-LRY1DJQCR7 | AW-17842581696, G-1WJB9N88XP, G-BVXZ7XTVJF (none shared) |
| Refund terms | Buyer pays return shipping "to the Netherlands"; 30 days | 30-day money-back guarantee; "In most cases where the issue is product-related … we'll cover return shipping"; refund in 3 to 5 business days |
| Trustpilot | luxe-cosmetics.com profile: 3.8, 4,322 reviews | luxeresearchlab.com profile: **3.5, 2,485 reviews, 28% 1★** (see §3) |

[R] The two stores share a SKU, testimonials, a review count, an image file, vendor names, a tracking domain and a Wyoming registered-agent address. The Luxe Research store's internal name is even "luxe-cosmetics-denmark". They are almost certainly one business, or closely linked operators.

**The legal link between Luxe Cosmetics B.V. and Luxe Research LLC was not found.** The US-state LLC registry was not searched.

**The two sites sell different versions of the balm:**

- **luxeresearchlab.com lists five ingredients:** sodium hyaluronate, adenosine, **argan oil**, vitamin E and bisabolol. It has **no niacinamide**.
- **luxe.com lists five different ones:** adenosine, **niacinamide**, bisabolol, vitamin E and hyaluronic acid.
- The two sites also give different prices and different refund terms.

The report does not mention luxeresearchlab.com at all, which is a significant gap. The operator needs to know that the same product is sold on two stores with different refund rules.

### 1d. Who sells B0GYK3T766 on Amazon

**Verdict: Amazon seller name partly confirmed; legal entity unverifiable.**

- **The seller's storefront name.** SellerRatings (`https://www.sellerratings.com/amazon/usa/luxecosmetics`, fetched 2026-10-31) lists Amazon seller **"LuxeCosmetics"** (seller ID A1E025XAV15YU7). Its product list includes "Luxe Korean Under Eye Balm – Lift & Firm 3-in-1 Multi Balm Stick, Hydrating, Smoothing, and…", which links to **B0GYK3T766**. The seller has 1,386 ratings at 4.2 of 5, has sold on Amazon.com "since 2023", and is "ranked 317th overall".
- **That one Amazon store sells both sites' ranges.** It sells luxe.com's lash-lift and tint kits and serums and also Luxe Research's products: Color Changing Foundation, Air Primer and Air Finish Setting Spray.
- **The legal business name behind the Amazon seller is not found.** It is shown only on Amazon's seller profile, which was not loaded. Searches for the seller ID and the entity names returned nothing.
- **What the report says.** Its §0 says the company is Luxe Cosmetics B.V., but in §1.1 it ties that only to the brand site. It does not claim the Amazon seller's legal entity, and that is correct, since the entity is unproven.

---

## 2. Ingredient claims

| Claim in report | Verdict | What I saw (live, 2026-10-31) |
|---|---|---|
| Five actives (adenosine, niacinamide, bisabolol, vitamin E, HA) | **Confirmed for luxe.com only** | The luxe.com page reads: "Adenosine — clinically proven to reduce fine lines … Niacinamide — brightens dark circles … Bisabolol — soothes … Vitamin E — protects … Hyaluronic Acid — deep, lasting hydration." The luxeresearchlab.com page instead lists sodium hyaluronate, adenosine, **argan oil**, vitamin E and bisabolol. |
| Adenosine is the lead active | **Confirmed** | "Luxe was formulated around Adenosine, the only anti-wrinkle active officially recognized by the Korean MFDS." Also: "the anti-wrinkle active Korea's MFDS approved back in 2014". |
| No retinol, no fragrance | **Confirmed (brand claim)** | "No retinol. No fragrance. No alcohol. No essential oils." Also: "No parabens. No artificial colors." |
| "No caffeine (brand claim)" (§0) | **Wrong as worded** | The brand never claims "no caffeine". Caffeine simply isn't named. The report's own §1.3 checklist puts it correctly ("not found / not named"), so §0 should be changed to match. |
| Current pack says "PDRN extract" | **Confirmed** | Main image `layer-z1-tun-…png` (uploaded 2026-10-26) shows a lavender stick reading "Luxe Korean under-eye balm … PDRN extract". The page text names PDRN only once, in the FAQ line "Kahi has PDRN but no adenosine". PDRN is **not** in the page's ingredient list. |
| Older pack says "collagen extract" | **Confirmed** | Images `Luxe_Eye_Balm_Wrinkle_claims.png`, `05_Imagev6_modified.webp` and `02_Imagev3_modified.webp` show a blue-grey "Luxe / Lift & Firm Multi Balm / WRINKLE CORE STICK / COLLAGEN EXTRACT / ELASTICITY". |
| Argan oil appears in an image | **Confirmed** | `05_Imagev6_modified.webp` ("Clinically Tested to Lift") names Sodium Hyaluronate, Adenosine and Argan Oil. |
| No full INCI list anywhere | **Confirmed** for both brand sites | None in the page text or the product JSON on either store. |

---

## 3. Red flags

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| a | "Rated 4.86 (10,839 reviews)" but the review widget reports 0 | **Confirmed** | The luxe.com page HTML contains `data-number-of-reviews='0'` and `data-average-rating='0.00'` (Judge.me), and the text "Rated 4.86 (10,839 reviews)" is stored as translatable static text (with Arabic and other copies). The Loox and Okendo count variables are `null`. The same "10,839" appears on luxeresearchlab.com as "Rated 4.8/5 based on +10,839 Total Ratings". |
| b | Testimonial dates come before the first images (2026-03-16) | **Partly confirmed; the framing needs correcting** | The purchase dates are confirmed: Dec 28th 2025 to Feb 18th 2026. "First images 16 Mar 2026" is the `?v=` file-version stamp (1773667362 = 2026-03-16 13:22 UTC). But on luxe.com, `Imagev4.png` has created_at **2026-03-13**. On the sister store luxeresearchlab.com, the balm product `luxe-balm` was **created 2025-12-03**, its first image is dated **2026-02-21**, and it was published **2026-03-02**. So a product record existed before every testimonial date. All six purchase dates still come before the earliest image (2026-02-21) and the first publication (2026-03-02) found anywhere. "Before the product existed" is too strong. "Purchase dates before the product was on sale" is supported. The **stronger** red flag, which the report missed in this file, is that the same six people, ages and dates appear on the other store (and, per another helper, on the toner-pad page). |
| c | Two study sizes, 2,431 vs 2,844 | **Confirmed** | The page reads "Based on a 2,431-customer satisfaction survey, Q1 2026." Gallery image `02_Imagev3_modified.webp` reads "92% of users noticed reduced puffiness, dark circles, and signs of tired eyes within hours. peer-reviewed study (2,844 women, ages 35-62, NY)". |
| d | 30-day vs 90-day guarantee | **Confirmed** | "✓ 30-Day Refund", "30-Day Free-Risk Guarantee" and "30-day money-back guarantee" appear 10 times. One line reads "Less than 1% of our customers have claimed their 90 day Money Back Guarantee". |
| e | Refund policy: return shipping to the Netherlands | **Confirmed (luxe.com)** | `https://luxe.com/policies/refund-policy`: "The customer is responsible for the direct cost of return shipping. Return shipping will be to the Netherlands as that is where our warehouse is located. … Shipping costs are not refundable." The product page says "send the tube back (even empty), get every dollar back. No questions. No restocking fee." The contradiction stands. Add: luxeresearchlab.com's policy is different and kinder (it covers return shipping when the issue is product-related). |
| f | The "44.9%" images show a different blue "WRINKLE CORE STICK" | **Confirmed in substance; wording overstated** | `Luxe_Eye_Balm_Wrinkle_claims.png` (uploaded 2026-07-09) shows "Reduced the total wrinkle area around the eyes by 44.9%" next to a blue-grey stick. That stick **is branded "Luxe"** and reads "Lift & Firm Multi Balm / WRINKLE CORE STICK / COLLAGEN EXTRACT". So it is an older or other Luxe pack, not another brand's product. "Wrinkle Core Stick" is a generic name: many eBay and Walmart listings sell "Calcium Volume Multi Balm Wrinkle Core Stick" at about $3 to $8 (WebSearch, 2026-10-31; e.g. `https://www.ebay.de/itm/136710031335`, `https://www.walmart.com/ip/18422051039`). **"Chinese-made" was not verified** by me. One copycat Amazon listing (B0GZ42VBFP) is said in a search summary to give China as country of origin, but that is not Luxe's product. Also note `07_Imagev8_modified.webp`, where the stick in the model's hand has garbled, unreadable label text, a common sign of an AI-generated image [R]. |
| g | At least 9 copycat Amazon listings | **Confirmed (at least 9; probably more)** | One `amazon.com`-restricted web search (2026-10-31) returned the report's B0H65Q3LWY and B0GZ42VBFP. It also returned five copycats **not** in the report: B0GY5PM1Y8 ("Luxe Korean Under Eye Balm … Collagen Extract, 0.38 oz"), B0GZV92LJ1 ("Magic Luxe Korean Under Eye Balm Stick"), B0GY6NJ15B ("Luxe Korean Balm … 0.32 oz"), B0GYDLZ134 ("Coellyo Lipstick Luxe Korean Under Eye Balm") and B0H1VFKL3T ("Tasunte Luxe Korean Under Eye Balm … 2PCS"). The other seven ASINs in the report (B0H6M6FWS1, B0HHJ6VHWQ, B0HFMCH8BB, B0H13QG48Z, B0GY13Z859, B0GVNWYQL3, B0GZTZHXGK) are **unverifiable**: a search naming four of them returned none. Amazon was not loaded. |
| h | Trustpilot 3.8 from 4,322 reviews, 17% one-star: which company? | **Confirmed; the company is clarified** | `https://www.trustpilot.com/review/luxe-cosmetics.com` (WebFetch, 2026-10-31): name "Luxe Cosmetics", domain luxe-cosmetics.com (now redirecting to luxe.com, the B.V. imprint), country shown "United States", claimed January 2023, TrustScore 3.8, **4,322 reviews**; stars 5★ 60%, 4★ 13%, 3★ 7%, 2★ 3%, **1★ 17%**. It is the luxe.com / Luxe Cosmetics profile, not Luxe Research's. Luxe Research has its own profile (`https://www.trustpilot.com/review/luxeresearchlab.com`): **3.5, 2,485 reviews, 5★ 46%, 1★ 28%**, claimed November 2025, with no eye-balm reviews on page 1. The report should give both, because the balm is sold on both stores. |

**Problem in §6.1's buyer-statement table.** I re-checked the three Trustpilot 1★ reviews on `?stars=1` (WebFetch, 2026-10-31):

- **Shari (2026-10-30):** names the eye balm. **Confirmed.**
- **Jeanne Laughlin (2026-10-25):** the full text is "I did not like the product..when applied, it streaked with black and red lines.. I felt it was a matt finish and made my wrinkles more prominent". "Streaked … matt finish" describes a foundation, not a balm.
- **Carrianne Kuss (2026-10-29):** the full text is "This is translucent to my skin. It does nothing whatsoever!!!!!so disappointed". "Translucent to my skin" also describes a foundation.

The report's quotes are accurate, and it says "product not named". But placing these two in a table of "independent buyer statements … about the Luxe eye balm" is **misleading**. [R] They are almost certainly about the colour-changing foundation and should come out of the eye-balm table. They are not counted in the report's theme table, so the counts are unaffected.

---

## 4. Rival prices per gram or mL, and the two studies

### 4a. Rival prices (sample of 5, loaded live from brand Shopify JSON and pages, 2026-10-31)

| Rival | Report | What I saw | Verdict |
|---|---|---|---|
| Dr.Melaxin Calcium Multi Balm | $19, 9 g, $2.11/g | `drmelaxin.us/products/calcium-multi-balm.json`: $19.00 (3-pack $49, 5-pack $75). Image alt "Calcium Multi Balm 9g". $19 ÷ 9 = $2.11/g | **Confirmed.** The product title on the site is "Calcium Multi Balm"; "Cemenrete" appears only in the Amazon and affiliate title. |
| d'Alba Double Serum All In One Multi Balm Stick | $21 (was $22), 10 g, $2.10/g | `dalba.com/products.json`: "d'Alba Double Serum All In One Multi Balm Stick 10g", $21.00, compare-at $22.00 | **Confirmed** |
| Beauty of Joseon Revive Eye Serum: Ginseng + Retinal | $17, 30 mL, $0.57/mL | `beautyofjoseon.com/products/revive-eye-serum-ginseng-retinal.json`: "30ml" $17.00 | **Confirmed** |
| RoC Retinol Correxion Line Smoothing Eye Cream | $21.99, 15 mL, $1.47/mL | `.json`: $21.99. Page reads "15 mL / 0.5 fl oz" | **Confirmed** |
| Medicube PDRN Pink Collagen Volume Multi Balm | $22 (was $26), 10 g, $2.20/g | `.json`: $22.00, compare-at $26.00. **No size found on the medicube.us page.** The report sources 10 g to a StyleKorean listing title, which I did not re-check. | **Price confirmed; size unverifiable from the brand page** |

### 4b. Adenosine trial (PMID 18489289)

**Verdict: confirmed, with one nuance.**

- The PubMed abstract (E-utilities, 2026-10-31) is Abella ML, L'Oréal Recherche, *Int J Cosmet Sci* 2006;28(6):447-51. It reads: "One hundred twenty-six female volunteers between 45 and 65 years of age … blind, randomised, placebo-controlled … applied twice daily for 2 months … evaluation … at 0, 3 and 8 weeks … Both adenosine-containing products led to significant improvements in skin smoothness in the periorbital area."
- **Nuance:** the design was split-face. Each woman used two of three products (adenosine cream, adenosine film or placebo), "84 subjects per product". So 84 women, not 126, used the adenosine cream.

### 4c. Korean dark-circle study (PMID 26346687)

**Verdict: confirmed.**

- Park SR et al., *Skin Res Technol* 2016;22(3):276-83. It classified "100 subjects with dark circles". The abstract reads: "Dark circles of vascular type (35%) and mixed type (54%) … were the most common."
- The report's "about 11% purely pigmented or other" is its own arithmetic and is correctly marked [R].

---

## 5. YouTube items (NexLev, 2026-10-31)

**Item 1: video cG7_XwI-vUU. Verdict: comments confirmed; one date in §1.2 slightly off.**

- **The video.** "Luxe Under Eye Balm Review - Does it Work or Scam?", channel Verify Beta, **2,798 views**, published **2026-04-09**, 159 s long. It has 6 comments in all.
- **The quotes are word-for-word correct:**
  - @hollyeubanks4207 (about 2026-10-01): "Oh no I just paid $38 for this product and I just received it today! I'm 45 yrs old my skin isn't that bad I'm using it as a preventative measure but now I feel like I wasted my $ I'm asking for a refund!…"
  - @josephinal (about 2026-10-30): "I tried this. It did take care of the bags and still worked when I woke from my nap"
  - @Maureen-d9y: "Wow! Thank you. I almost ordered."
  - @JAGPabst: "Thank you for doing the research and saving me money!"
  - @lindarusick4402: "Cancelled my order."
  - @sadiebernal939: "I just bought it."
- **Small error in §1.2.** The report says the first "scam or legit" videos appeared "2026-04-10 to 04-12". This one was published 2026-04-09. Comment dates come from YouTube's relative "x months ago" text, so they are approximate.

**Item 2: video hAc7jewvVWE (Laura Fagelman). Verdict: confirmed.**

- **The video.** "I Can't Take The Lies Anymore!😠", **96,031 views** (the report says 96,022, pulled earlier the same day), 4,932 likes, published 2026-02-12, about 1K comments.
- **The top comments and like counts match the report exactly:**
  - "I'm 64, and it drives me nuts when the advertisements show some youngster talking about lines and wrinkles." (601)
  - "Misleading advertizing should be a crime punished by law" (485)
  - "…62, no amount of collagen creams or fancy serums are going to make my skin bounce back to the skin of a 20 year old." (257)
  - "I am NOT a fan of AI at all. I think it's so deceptive." (214)
  - "Any time there is a very young person showing something for mature skin, I block not even watching." (145)
  - "…botox in a stick. All lies." (96)
  - "I'm tired of all the lies too and I'm tired of the prices and it doesn't do anything" (94)
  - "If creams & serums make us younger, there would be no plastic surgery. Moisturiser nice & feel good factor. Full stop" (70)
  - "Remember any "difference" will last a few minutes" (26)

---

## Summary of what to fix in the report

1. Rename the site to **luxe.com** (luxe-cosmetics.com now redirects there). Add that the luxe.com Shopify store is itself registered as "Luxe Cosmetics US, Sheridan, Wyoming".
2. Add **luxeresearchlab.com (Luxe Research LLC, Sheridan WY)**. It sells the same balm (SKU Eye-Balm-blue) at $34.99, with the same testimonials and "10,839" count, a different five-ingredient list (argan oil, no niacinamide) and kinder refund terms. Its balm record dates from 2025-12-03.
3. Name the Amazon seller as storefront **"LuxeCosmetics"** (A1E025XAV15YU7, since 2023, per SellerRatings). Say plainly that its legal entity is not found.
4. Change §0 "no caffeine (brand claim)" to "caffeine not named".
5. Reword red flag 2 from "before the product existed" to "before any image or publication found". Add the cross-store duplicated testimonials.
6. Reword red flag 5: the claim images show an older **Luxe-branded** "Wrinkle Core Stick" pack. The generic name is confirmed on eBay and Walmart; "Chinese-made" is unverified.
7. Remove the Jeanne Laughlin and Carrianne Kuss quotes from the eye-balm table (they are almost certainly about the foundation). Add Luxe Research's Trustpilot (3.5, 2,485 reviews, 28% 1★).
8. Add five more copycat ASINs. Seven of the report's nine are unverified by me.
9. Note that the adenosine trial's cream arm was 84 women (split-face design out of 126).
10. Correct the earliest scam video date to 2026-04-09.
