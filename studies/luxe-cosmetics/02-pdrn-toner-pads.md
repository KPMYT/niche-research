# 02. Luxe PDRN Toner Pads (140 pads), ASIN B0HM229JP6

> **Checked 2026-10-31.** A second helper re-checked a sample of this report against the sources: `checks/02-pdrn-toner-pads-check.md`. The text below is as first written; the corrections are listed in `SUMMARY.md` section 7 and in the check file.

Study date: 2026-10-31. Helper report for the Luxe Cosmetics product study (brief: `BRIEF.md`).
Raw pulls: `data/toner-pads/` (sources log: `data/toner-pads/web-sources-log-2026-10-31.md`; YouTube pulls: `data/toner-pads/youtube-pulls-2026-10-31.md`; product images: `data/toner-pads/images/`).

**How to read this report.** **Measured** means the figure was read off a page or file on 2026-10-31 and the source is given. **Reading** means it is my interpretation. Where something could not be found it says **not found**. The Amazon page was not loaded: it hit a bot check, and the brief says not to retry. As a result, every Amazon-only fact (the listing title, Amazon price, star rating, review count, Amazon reviews and the listing date) is **not found**.

**Check status.** CLAUDE.md rule 3 asks for a second helper to re-check a sample. That has not been done. The INCI match with Anua (section 1.4) is the claim that most needs checking, together with the price table.

---

## 0. The ten things the operator needs to know

1. **The product is real and sold on the brand's own US site, but nothing about the Amazon listing could be seen.** The jar reads **"Luxe PDRN Revitalizing Gel Pads, High Concentration, Salmon-Derived PDRN COMPLEX, Advanced Skin Toning, 200 g / 7.05 oz (140 pads)"** (measured: product image on luxeresearchlab.com). It sells there as "Luxe | PDRN Toner Pads" for **$59.95** (measured, 2026-10-31).
2. **It is not on luxe.com.** The seller is **Luxe Research LLC** (a Sheridan, Wyoming address) at luxeresearchlab.com. luxe.com is run by Luxe Cosmetics B.V. (Helmond, Netherlands) and says "All our products are vegan." The pads say "Salmon-Derived" on the jar.
3. **The pads appeared on 2026-08-04** (measured: Shopify created/published date and image upload stamps). They have been on sale about 3 months. A second listing of the same SKU was added on 2026-09-16.
4. **The formula looks like Anua's.** The ingredient list on the Luxe page matches **Anua PDRN 100 Hyaluronic Acid Glow Pad**: the same 45 ingredients in the same order (measured, line-by-line comparison). Anua publishes its PDRN level as **sodium DNA 100 ppm = 0.01%**.
5. **Several Luxe images are Anua's images, recoloured from teal to pink.** They carry the same headings, the same numbers ("125.39% Improvement in Skin Hydration", "100% agreed..."), the same mistake ("PDRN (Disodium EDTA)") and the same instructions. **The Luxe versions drop Anua's study footnotes**: 21 women aged 20 to 59, tested 30 to 31 Dec 2024 on *Anua's* product, with self-assessment immediately after first use. The Luxe image even uses Anua's own product name as its headline.
6. **What the brand page says and what the label says do not agree.**
   - The page FAQ says the jar holds **100 pads**; the jar says **140**.
   - The page says the exfoliation comes from **"Maltobionic Acid, a PHA"** and lists a **"Vitamin C derivative"**. Neither is in the ingredient list.
   - It claims "**99% purity PDRN**", "9 clinically validated actives" and "Tested on women 35–65". No test is published.
   - The six "Verified Buyer" reviews are the same six names, ages and purchase dates used on the Luxe eye balm page, and some are dated *before the product existed* (Dec 2025 to Feb 2026). They are shown with the eye balm's price. The brand helper found this in `data/brand/testimonial-duplication-check-2026-10-31.md`, and I confirmed it on the pads page.
7. **What the pads are, plainly:** a hydrating gel pad. It has a niacinamide, glycerin and hyaluronic acid essence, a small amount of salmon DNA, peptides and collagen, and **no exfoliating acids, no retinol and no fragrance** (reading from the INCI). It is a gentle, moisture-first product, not a resurfacing pad.
8. **The science behind PDRN is good for injections and wound healing, and thin for creams and pads.** Dermatology Times (11 Jul 2026) says PDRN fragments are 50 to 1,500 kDa, far above the ~500 Da that passes intact skin. Dr Dray (144K views) says she is "highly, highly, highly doubtful that these skincare products with PDRN do anything above and beyond moisturize the skin."
9. **Price.** At $59.95 for 140 pads the Luxe jar costs **$0.43 per pad**. The same Anua formula costs **$0.38 per pad** ($23 for 60 at anua.us). The best-selling Medicube PDRN pad is **$0.28 to $0.31 per pad**. Most K-beauty pads cost $0.20 to $0.45 per pad. The Amazon price for B0HM229JP6 is **not found**.
10. **For women 50+:** a gentle, fragrance-free, acid-free hydrating pad suits dry, thinning, easily irritated mature skin, and the "5-minute mini mask" habit is easy. The honest promise is **hydration, plumper-looking skin and a glow that lasts hours**. Fading dark spots, firming crepey neck skin and "cellular repair" cannot be promised. Anyone with a **fish allergy** should not use a salmon-derived product without asking a doctor.

---

## 1. What the product is (brief point 1)

### 1.1 Identity and where it is sold

| Item | Finding | Source, date pulled |
|---|---|---|
| Amazon ASIN | B0HM229JP6 (URL slug "PDRN-Toner-Pads-Face-140"); the top organic result for "luxe toner pads" (per the caller) | Amazon page **not loaded** (bot check) |
| Amazon full title, price, rating, review count, "bought in past month", listing date | **not found** | Amazon blocked; no search engine, price tracker or reseller had it indexed (9 searches, 2026-10-31). camelcamelcamel, ubuy and desertcart returned HTTP 403 |
| Name on the jar | "Luxe / PDRN REVITALIZING GEL PADS / High Concentration, Salmon-Derived PDRN COMPLEX, Advanced Skin Toning / 200 g / 7.05 oz (140 pads)" | Product images `tonnerfixed_2` and `tonnerfixed_6`, https://luxeresearchlab.com/products/luxe-pads, pulled 2026-10-31 (saved in `images/`) |
| Name on the brand site | "Luxe \| PDRN Toner Pads" | https://luxeresearchlab.com/products/luxe-pads.json, 2026-10-31 |
| Brand-site price | **$59.95** (no compare-at price). The second listing `/products/luxe-pdrn-toner-pads-sub` is **$59.99** | Product JSON, 2026-10-31 |
| Other prices on the same page | FAQ: "With the Buy 1 Get 1 Free offer, you get 100 days of treatment for $39.99". The six testimonials show "$34.99 $39.95", which is the eye balm's price | Page text, 2026-10-31 |
| Seller | "Company Name: Luxe Research LLC, Business Address: 30 N Gould St Ste R Sheridan, WY 82801 United States, info@luxeresearchlab.com, +1 (385)-454-6193" | luxeresearchlab.com footer, 2026-10-31 |
| Shopify vendor field | "Luxe Cosmetics US" (the same vendor name used on luxe.com products) | Product JSON |
| SKU / barcode / weight | SKU "Pdrn-toner-pads"; barcode 199874943640; shipping weight 388 g | Product JSON |
| On luxe.com (Luxe Cosmetics B.V.)? | **No.** Neither the luxe.com nor the luxecosmetics.co catalogue (55 products) has toner pads, and eight guessed product URLs returned 404 | luxe.com/products.json, 2026-10-31 |
| Other retailers (Walmart, Target, TikTok Shop, eBay) | **not found** | Searches, 2026-10-31 |
| YouTube or TikTok videos about this exact product | **not found** (the YouTube search "luxe pdrn toner pads" returned only other brands) | NexLev youtube_search, 2026-10-31 |

### 1.2 When it launched

| Evidence | Date | Source |
|---|---|---|
| Shopify product created / published (`luxe-pads`) | 2026-08-04 02:49 / 12:35 (Pacific) | Product JSON |
| First four product images uploaded | 2026-08-04 09:50 UTC | Image URL version stamps (`v=1785837007`) |
| Jar images uploaded | 2026-08-19 17:20 UTC | `v=1787160017` |
| Second listing (`luxe-pdrn-toner-pads-sub`) created / published | 2026-09-16 / 2026-09-21 | Product JSON |
| Amazon listing date | **not found** | |

**Reading:** the product went on sale in early August 2026, so it is about 3 months old. The Amazon ASIN starts "B0HM", later than the eye balm's "B0GY". That fits a recent Amazon listing, but ASINs cannot be dated exactly.

### 1.3 Format, pad, texture and how to use it (measured from the Luxe images)

- **Pad:** "7cm Dual-Sided Pad for Rich Hydration". One side is the "Soft & Hydrating Gel Side: Peptide-Infused Fabric, Hydration Delivery with Mask Pack Effect"; the other is the "Gentle Plain Side: Low-irritation Vegan Fabric, Lock-in Moisture after wiping" (image `Luxe_GelPad_Imagev5`).
- **Essence:** a clear pink gel (images).
- **How to use** (image `tonnerfixed_6`), quoted:
  1. "After cleansing, apply the "Peptide Gel Side" to your skin."
  2. "Leave it on for 5 minutes like a mini sheet mask"
  3. "Use the "Plain Side" to wipe along your skin texture"
  4. "Lightly pat in the remaining essence."
  - "Can be used every day, both AM & PM." Tip: "Use as a quick morning mask while drying your hair!"
- **Page copy:** "One jar. Twice a day." Also: "Each pad works on your face, neck, chest, hands, elbows, knees, and underarms."
- **How long a jar lasts:** 140 pads ÷ 2 a day = **70 days**; at 1 a day, 140 days. The page's own FAQ says "One jar contains 100 pads ... a 50-day supply", which contradicts the jar (measured contradiction).

### 1.4 Full ingredient list (INCI) and what it means

Transcribed from the Luxe "Ingredient List" image (`images/luxeresearchlab-Luxe_GelPad_Imagev8-2026-10-31.jpg`; text in `luxe-pads-inci-transcribed-from-image-2026-10-31.txt`):

> Aqua (Water), Butylene Glycol, Glycereth-26, Niacinamide, Glycerin, 1,2-Hexanediol, Diethoxyethyl Succinate, Hydroxyethyl Urea, Hydroxyacetophenone, Glycereth-25 PCA Isostearate, Glycosyl Trehalose, Hydrogenated Starch Hydrolysate, Melia Azadirachta Leaf Extract, Ethylhexylglycerin, Xanthan Gum, Propanediol, Adenosine, Melia Azadirachta Flower Extract, Coccinia Indica Fruit Extract, Disodium EDTA, **Sodium DNA**, Hydrolyzed Collagen, Aloe Barbadensis Flower Extract, Solanum Melongena (Eggplant) Fruit Extract, Coptis Japonica Root Extract, Ocimum Sanctum Leaf Extract, Zea Mays (Corn) Kernel Extract, Corallina Officinalis Extract, Curcuma Longa (Turmeric) Root Extract, Sodium Hyaluronate, Hyaluronic Acid, Hydrolyzed Hyaluronic Acid, Terminalia Ferdinandiana Fruit Extract, Fructan, Glucose, Lecithin, Acetyl Glutamine, Collagen Extract, Bacillus/Soybean Ferment Extract, Caprylyl Glycol, Folic Acid, Hexapeptide-11, Oligopeptide-1, Oligopeptide-2, Oligopeptide-3

**Match with Anua (measured).** This is the same 45-ingredient list, in the same order, as **Anua PDRN 100 Hyaluronic Acid Glow Pad** (dodoskin.com product JSON, pulled 2026-10-31). The only differences are translated common names (dodoskin writes "indigo plant", "ivy gourd", "holy basil" and "kakadu plum" where Luxe uses Latin names). Side-by-side table: `data/toner-pads/luxe-vs-anua-inci-comparison-2026-10-31.txt`.

Anua's listing gives the amounts: **sodium DNA (100 ppm)**, sodium hyaluronate (5.002 ppm), hyaluronic acid (5 ppm) and hydrolyzed hyaluronic acid (5 ppm).

**Reading:** the Luxe pads are either made to Anua's formula by the same contract manufacturer, or the listing copied Anua's ingredient list. Which one cannot be proven from here. Either way, if the formula is Anua's, the PDRN is **0.01%**.

**Key ingredients, plainly:**

| Question from the brief | Answer | Basis |
|---|---|---|
| PDRN source | **Salmon**: the jar says "Salmon-Derived PDRN COMPLEX" and an image says "Salmon DNA-infused formula". The INCI name is Sodium DNA | Luxe images (measured) |
| PDRN concentration | **Not stated by Luxe.** Sodium DNA sits *after* Disodium EDTA, a chelator normally used at about 0.05 to 0.1%, so it is below that. Anua's identical list states **100 ppm (0.01%)**. The jar's "High Concentration" claim is unsupported | INCI order (reading); Anua figure measured on dodoskin |
| "99% purity PDRN" | This describes the purity of the raw material, not how much is in the pad. Medicube uses the same phrase and lists 1 ppm. One Eye Beauty called Medicube's 99% claim "far from the truth" for a 10 ppm cleanser | Luxe page; dodoskin Medicube INCI; One Eye Beauty transcript |
| Niacinamide | **Yes**, 4th ingredient (likely 2 to 5%; reading, not stated) | INCI |
| Hyaluronic acid | Yes, three forms, each about 5 ppm per Anua's listing (tiny) | INCI + Anua ppm |
| Peptides | Yes: hexapeptide-11 and oligopeptide-1, -2 and -3 (last on the list) | INCI |
| Collagen | Hydrolyzed collagen and collagen extract (source not stated). The image claims "Patented 7D vita collagen", copied from Anua | INCI, image |
| Centella | **No** | INCI |
| Exfoliating acids (AHA, BHA, PHA) | **None.** No gluconolactone, lactobionic, maltobionic, glycolic, lactic or salicylic acid. **This contradicts the page's "Maltobionic Acid, a PHA" claim** | INCI vs page FAQ |
| Vitamin C derivative (page claim) | No vitamin C derivative is listed. The only possible link is Terminalia ferdinandiana (Kakadu plum) extract, a fruit naturally rich in vitamin C, placed low on the list | INCI (reading) |
| Retinol, fragrance, drying alcohol | None listed. Butylene glycol and propanediol are glycols, not drying alcohols | INCI |
| Hydrators and soothers | Glycerin, butylene glycol, hydroxyethyl urea, glycosyl trehalose, adenosine (Korea's registered anti-wrinkle cosmetic ingredient), aloe | INCI |
| Allergy flags | **Salmon DNA** (fish), **collagen of unstated source** (could be fish or animal), **soybean** ferment, **corn** extract, turmeric, neem and Coptis extracts | INCI (reading) |

### 1.5 Claims made for it (quoted, luxeresearchlab.com, pulled 2026-10-31)

Page headlines: "Better-Looking Skin in 30 Days or You Don´t Pay", "One Pad Replaces Your Entire Treatment Step", "Every Day Results — Without Peeling".

FAQ and body copy:
- "By week 4–8, dark spots fade, fine lines soften, and firmness improves visibly."
- "PDRN (99% purity) — the regenerative ingredient Korean dermatologists use in-clinic"
- "PDRN targets the cellular repair your skin needs now."
- "PDRN rebuilds underneath."
- "No retinol. No harsh acids. No synthetic fragrances. No drying alcohols. The exfoliation comes from Maltobionic Acid — a PHA ... Hypoallergenic and dermatologist-tested."
- "9 clinically validated actives"
- "Tested on women 35–65"
- "10,000+ Mature Women"
- "Rated 4.86 (10,839 reviews)" (a site-wide badge; the same number appears on the eye balm page)
- "One Pad Replaces Your Whole Routine. Toner. Exfoliator. Serum. Treatment mask."

The survey block reads "**0%** saw visibly brighter, more even skin within the first two weeks" and "**0%** noticed dark spots fading by week four". The counters were left unfilled.

Images:
- "125.39% Improvement in Skin Hydration Immediately After Use (Temporary Effect)"
- "100% agreed the product improved skin elasticity in the eye area, cheeks, smile lines, and forehead*"
- "100% agreed ... improved inner skin hydration lasting up to 12 hours*"
- "*Individual results may vary."

**Where those image numbers come from (measured).** Anua's US product images show the same numbers with these footnotes:
- "*Clinical study on ANUA PDRN 100 HYALURONIC ACID GLOW PAD for Radiance (Glow) Effect | Test Institution: P&K Skin Clinical Research Center Co., Ltd. | 30/12/2024 – 31/12/2024 | Subjects: 21 adult women (20-59)"
- "*Based on results from a consumer self-assessment conducted immediately after first use in a clinical study on 21 participants aged 20-59"

The Luxe images keep the numbers and drop the footnotes. They also swap Anua's young model for an older, grey-haired woman.

Pre-order urgency on the page: "Pre-order to get the next available items. Next batch ships: October 8th Sold out | Ships next October 30th 70% sold | November 11th Just opened". There is also a 30-day money-back guarantee: "If your skin doesn't improve, you get every penny back. No forms."

---

## 2. Where it fits in a routine (brief point 2)

**What toner pads are.** A jar of pre-soaked cotton, viscose or gel-fabric rounds sitting in a liquid (an "essence" or toner). They are a Korean format: you take a pad out with tweezers and either **wipe** the face or **lay it on** as a mini mask. The pad replaces a separate toner plus cotton pad. Some pads exfoliate (acid pads), and some only hydrate and soothe (essence pads). The Luxe pad is the second kind.

**Where it sits in the Korean routine:** after cleansing and before serum, moisturiser and (in the morning) sunscreen. Medicube's instructions say the same: "After washing your face, gently wipe your entire face ... in the first step of your basic care" (dodoskin, 2026-10-31).

**Wipe or "pad mask":** almost every PDRN pad is now sold for both uses. Leave the pad on the cheeks for about 5 minutes, then wipe with the other side.
- Anua and Luxe: 5-minute gel side, then wipe.
- Medicube: "Apply it like a pack to areas that require intensive care".
- Mediheal: "leave it on like a mini mask for 5–10 minutes".
- BestReviews (Feb 2026) lists four ways to use them: as a toner, as a mini sheet mask, for exfoliating (textured, acid or retinol pads) and as a hydration boost.

**What it pairs with:** a moisturiser after it (the pad alone is not a moisturiser) and sunscreen in the morning. Because it has no acids or retinol, it can sit in the same routine as a retinoid without doubling up on irritation (reading from the INCI). Anua's own image claims more glow "when used with serum". The Luxe page's line "One Pad Replaces Your Whole Routine" is not a sound recommendation.

---

## 3. Who it is for, and how it fits women 50+ (brief point 3)

- **Positioning (measured):** the page aims squarely at women 40+: "Most formulas were designed for 25-year-old skin. This one wasn't"; "Built For Skin That's Changed"; "skin concerns that actually show up after 40"; "10,000+ Mature Women". The testimonials name women aged 42 to 63, but these are template testimonials (see 0.6).
- **Who it suits (reading from the INCI):** dry, dehydrated, dull or easily irritated skin; people who cannot tolerate retinol or acids; anyone who wants a quick, no-fuss hydration step.
- **Who it suits less:** people wanting real exfoliation or pore clearing (no acids), oily or acne-prone skin (BestReviews: the Anua pad is "Not the best option for more oily skin types"), vegans, and anyone with a fish allergy.
- **Budget:** a premium price for this format. $0.43 per pad at the brand price, against $0.20 to $0.45 for most rivals (section 5).

**Women 50+ in particular:**
- After menopause, skin holds less water and the barrier weakens. A glycerin, niacinamide and hyaluronic acid pad answers **dryness, tightness and dullness** directly, and the effect shows within minutes (plumper, dewier, smoother make-up). That is the honest win.
- Mature viewers often have a history of bad reactions to retinol, vitamin C and acids. The Luxe page builds its pitch on exactly that pain ("Retinol made my skin peel for three weeks straight"). Acid-free, fragrance-free pads are a real fit for that viewer.
- Demand signal (measured): Spate reports the consumer concern "**mature skin**" linked to PDRN at **15.0K average monthly interactions, ">1,000% year-over-year growth"**, and "fine lines" at 12.9K, also >1,000% (spate.nyc blog, © 2026, pulled 2026-10-31).
- On YouTube, the mature-skin K-beauty coverage is led by One Eye Beauty: "Best & Worst PDRN Skincare 2025 - What Actually Works for Mature Skin?" (39,117 views) and "Top 5 Affordable Korean Skincare Brands That ACTUALLY Work for Mature Skin" (89,986). There is also "Ultimate Korean Skincare Routine for 40s, 50s, 60s, and Beyond!" from Sun-Hee Kim (4,429). Figures are NexLev, 2026-10-31.
- Limits: the pads will not lift sagging skin, fade age spots in weeks or firm a crepey neck. Niacinamide can lighten spots slowly over 8 to 12 weeks, so a modest "more even-looking tone with daily use" is defensible. Dark spots on hands and chest need sunscreen first.
- Practical: tweezers or clean fingers to lift a slippery gel pad; big jars (Cult Beauty buyer: "the packaging takes up a lot of space"); some buyers find dual-sided pads confusing ("Finds the two-sided pad confusing", Cult Beauty review, 2026-05-05, paraphrased by the fetch tool).

---

## 4. Problems it solves and how; what is different (brief point 4)

| Buyer problem | What in the pad addresses it | Strength of support | Reading |
|---|---|---|---|
| Dry, tight, dehydrated skin | Glycerin, butylene glycol, hydroxyethyl urea, trehalose, HA, gel mask time | Strong: humectants work; Anua's test showed +125.39% hydration *immediately* (temporary) on 21 women | The core, honest benefit |
| Dullness, wanting a "glow" or "glass skin" | Water in the outer skin plus a film-forming gel gives a dewy look | Strong for the look, short-lived | Show it on camera right after use |
| Uneven tone, dark spots | Niacinamide (4th ingredient) | Niacinamide has evidence for gradual brightening; the PDRN contribution is unproven | "Helps even the look of tone over weeks", not "fades spots" |
| Fine lines | Temporary plumping from hydration; adenosine; peptides at the end of the list | Weak beyond the plumping | "Fine lines look softer" (temporary) |
| Rough texture | No exfoliant. Wiping with fabric gives only mild mechanical smoothing | Weak | Do not sell it as an exfoliator |
| Enlarged pores | Hydration can make pores look smaller for a while | Weak | Avoid pore claims |
| Redness, sensitivity | Fragrance-free, acid-free; aloe, niacinamide | Moderate (niacinamide helps the barrier; low-irritation formula) | "Gentle enough for sensitive skin": patch test first |
| Firmness, sagging, "cellular repair" | Claimed for PDRN | **Not supported** for topical PDRN at 0.01% | Do not claim |
| Too many steps | One pad acts as toner plus mini mask | True for that step | "Replaces your toner and sheet mask", not the whole routine |

**What is different from rivals (reading):** very little in the formula, since it appears identical to Anua's. The differences are the **pad count** (140, against 60 for Anua and 70 for Medicube), **marketing aimed at women 40+**, and the **price**, which is higher per pad than the identical Anua product.

---

## 5. Competitors (brief point 5)

All prices measured 2026-10-31 unless dated otherwise. "dodoskin" means dodoskin.com (a US K-beauty retailer) product JSON. "BR" means BestReviews "Best PDRN pads", updated Feb 2026, Amazon prices at that time (https://bestreviews.com/beauty-and-personal-care/skin-care/best-pdrn-pads). PDRN amount is shown where the retailer INCI gives ppm (1 ppm = 0.0001%). Amazon star ratings and review counts are **not found** for every pad, because Amazon could not be loaded.

### 5.1 PDRN pads

| Brand / product | Pads | Price (source) | $/pad | PDRN source and amount | Other actives of note | Rating (reviews) | Positioning |
|---|---|---|---|---|---|---|---|
| **Luxe PDRN Toner Pads** | 140 (jar); page says 100 | $59.95 (luxeresearchlab.com); Amazon not found | **$0.43** (140) or $0.60 (100) | Salmon; amount not stated (same INCI as Anua: 100 ppm) | Niacinamide, HA, peptides, collagen; no acids | Amazon not found; site badge 4.86 (10,839), unverified | "Built for skin after 40", "one pad replaces your routine" |
| Anua PDRN 100 Hyaluronic Acid Glow Pad | 60 (180 ml) | $23.00 (anua.us); $21.78 (dodoskin); $22 Amazon (BR) | $0.36 to $0.38 | Salmon (BR); **100 ppm** | Same formula as Luxe | Cult Beauty 4.67 (18) | Hydration and glow, dual-sided gel pad |
| Medicube PDRN Pink Collagen Toning Gel Toner Pad | 70 | $21.51 (dodoskin); $19.89 Amazon (BR) | $0.28 to $0.31 | Salmon "99% purity"; **1 ppm** | Collagen 2 ppm, niacinamide, retinol, centella actives | Life Pharmacy 4.9 (53) | Ultra-thin 0.5 mm gel pad, tone correction; the category leader |
| Medicube PDRN Pink Collagen Jelly Pad (DIY: pour the essence in) | not stated on page | $26.00 (compare $33, medicube.us) | not found | Salmon | Ultra-low-molecular collagen | not found | Bouncy jelly, 5-minute mask |
| Mediheal (Derma 365) PDRN Lifting Pad | 100 | $26.40 (mediheal.com); $27.42 (dodoskin); $19.80 Amazon (BR) | $0.20 to $0.27 | BR: plant-based. The dodoskin INCI lists **no sodium DNA** (possibly an incomplete list) | Niacinamide, ceramide, centella; **contains fragrance** | not found | Lifting, de-puffing; BR "Best Bang for the Buck" |
| VT PDRN Tension Toner Pads | 60 (170 ml) | $22.75 (dodoskin); $15 Amazon (BR) | $0.25 to $0.38 | Ginseng (plant); sodium DNA second to last | Niacinamide, ceramide, 8 hyaluronic acids, shea | not found | Dry skin, elasticity, unscented |
| Biodance Caviar PDRN Dual Gel Toner Pads | 60 | $24.09 (dodoskin) | $0.40 | Sodium DNA **1,000 ppm** + salmon egg extract | Lactic, salicylic and PHA acids, LHA (exfoliating side) | not found | Dual texture, exfoliate plus calm |
| Isntree Gim PDRN Boosting Glow Pad | 70 | $23.01 (dodoskin) | $0.33 | Seaweed (gim); **100 ppm** | Peptides, gluconolactone (PHA) | not found | Glow, elasticity |
| Rejuran Derma Healer Pore Tightening Toner Pad | 60 | $26.78 (dodoskin) | $0.45 | "c-PDRN" (hydrolyzed DNA) | AHA, BHA, PHA, LHA | not found | Pores; from the Rejuran injection brand |
| Skinfood Carrot PDRN Pad | 100 | $30.69 (dodoskin) | $0.31 | Carrot; **10 ppb** | Essential oils | not found | Moisture, elasticity |
| SNP Glutathione PDRN Bright Turn-On Pad | 60 | $18.32 (dodoskin) | $0.31 | "Vegetable PDRN" | Glutathione, vitamin C, fragrance | not found | Brightening |
| Glow Recipe PDRN+ Repair + Soothe Korean Toner Pads | 60 | $30.00 (glowrecipe.com) | $0.50 | "Vegan PDRN+" | Centella, panthenol, beta glucan | not found | Redness, barrier; Sephora |
| Dear Doer Break PDRN Retinol Serum Pad | 70 | $20 Amazon (BR) | $0.29 | Plant (BR) | Retinol, centella | not found | Deep pore exfoliation |
| mixsoon Collagen Toner Pad | 110 | $24.82 (dodoskin) | $0.23 | Sodium DNA (no ppm) | Collagen, hyaluronic acid | not found | Collagen hydration |

### 5.2 Non-PDRN K-beauty pads (price anchors, dodoskin, 2026-10-31; formulas not checked except COSRX)

| Product | Pads | Price | $/pad |
|---|---|---|---|
| COSRX One Step Original Peptide Collagen Lifting Glow Pad (no sodium DNA in INCI; "especially mature and dull skin") | 100 | $24.58 | $0.25 |
| numbuzin No.3 Radiance Glowing Jumbo Essence Pad | 70 | $29.90 | $0.43 |
| Abib Jericho Rose Collagen Pad Firming Touch | 60 | $19.01 | $0.32 |
| Torriden Dive-In Low Molecule Hyaluronic Acid Multi Pad | 80 | $18.71 | $0.23 |
| SKIN1004 Madagascar Centella Quick Calming Pad | 70 | $14.85 | $0.21 |
| Round Lab Birch Juice Moisturizing Pad | 80 | $23.56 | $0.29 |
| Dr.Ceuracle PLC Calming Solution Pad | 130 | $36.40 | $0.28 |
| Medicube Zero Pore Pad 2.0 (Amazon #1 toner pad: 100K units in Jul 2026, 4.6 stars, 30.3K reviews, $18.90; ASINSIGHT) | 70 | $19.80 | $0.28 |

**Reading:** the Luxe jar's 140 pads are generous, but the price per pad sits at the top of the market. The same formula costs less as Anua. The Luxe PDRN level (0.01%, if it is Anua's) is far below Biodance (0.1%), and Rejuran's injection-brand pedigree beats any "Korean clinic" claim.

### 5.3 Market size (measured, third-party estimates)
- **Toner pads on Amazon US:** 4,245,200 units and about $86.5M over Aug 2025 to Jul 2026 (top 50 ASINs); July 2026 alone was 354K units (▼29.8% month on month). Medicube holds 5 of the top 10; no PDRN pad is in the top 10 (ASINSIGHT, https://www.asinsight.com/market-analysis/US/toner-pads, pulled 2026-10-31).
- **PDRN products on Amazon US:** 754,600 units and about $15.9M in July 2026 (▼40.2% month on month); Medicube holds 5 of the top 10 (ASINSIGHT, https://www.asinsight.com/market-analysis/US/pdrn).
- **JIYU** is #3 among toner pads ($43.99, 30K units, 4.3 stars, 5.1K reviews). It is a TikTok-ad brand aimed at older women, and James Welsh called it "The Fakest Skincare Brand On Tiktok?" (249,607 views). It is the closest business-model match to Luxe (reading).

---

## 6. User feedback (brief point 6)

### 6.1 For the Luxe pads themselves
- **Amazon reviews:** **not found** (page not loadable).
- **Brand-site reviews:** the six "Verified Buyer" stories are **template testimonials**, reused across Luxe products with the same names, ages and dates, and dated before the product launched (see 0.6 and `data/brand/testimonial-duplication-check-2026-10-31.md`). **They must not be quoted as real reviews.**
- **YouTube, TikTok, Reddit:** nothing found for the Luxe pads.

### 6.2 For the identical Anua formula (the most relevant real feedback)
Cult Beauty, 4.67/5 from 18 reviews (12 five-star, 6 four-star). Page 1 read, 2026-10-31: https://www.cultbeauty.com/p/anua-pdrn-100-hyaluronic-acid-glow-pad-180ml/16674994/. Words in quotes were returned verbatim; the rest was paraphrased by the fetch tool.

| Reviewer, stars, date | What they said |
|---|---|
| Zuz, 5, 2026-10-30 | "leaves the skin nice and hydrated" (just started) |
| Coco, 4, 2026-10-30 | "I've been using it for 2 weeks now and it's very hydrating" |
| Sunny, 4, 2026-06-23 | very hydrating, visible results |
| Emilia, 5, 2026-05-07 | third purchase; more radiant skin, fewer visible fine lines |
| Qwendy, 4, 2026-05-05 | serum "lovely and hydrating"; two-sided pad confusing; jar too big for a small bathroom |
| Luci, 5, 2026-05-02 | "Skin is left very well hydrated, I am already repurchising." |
| Maria_London, 4, 2026-04-30 | hydrating, but prefers the shape of sheet masks and eye patches |
| Lyssa, 5, 2026-04-21 | dehydrated skin; fresh water-based hydration; glass-skin effect |
| Lucia, 5, 2026-04-14 | hydrates, calms redness, sits well under make-up |
| kovesdii, 5, 2026-03-10 | moisturises well; does not irritate sensitive skin |

Themes across these 10: **hydration 10/10**; glow or glass skin 2; calms redness or suits sensitive skin 2; fewer fine lines 1; **complaints 3** (pad confusing, jar size, pad shape). Nobody reported breakouts or irritation. Other retailers: Sephora Bahrain shows 4.4 (15) and Hwahae about 4.07 (search snippet, not opened).

### 6.3 For PDRN pads and PDRN in general: YouTube comments (NexLev, 2026-10-31)
46 substantive comments read across 5 videos (full text in `data/toner-pads/youtube-pulls-2026-10-31.md`). A comment can fall into more than one theme.

| Theme | Count | Example (verbatim) |
|---|---|---|
| PDRN helped (hydration, calm, "skin never better") | 11 | "My skin is super dry, and PDRN really helps keep it moisturized without any irritation." (@chojiae-f2e, 50 likes, Dr Dray video) |
| Skeptical: no evidence, hype, tiny amounts | 7 | "Summary: No clinical data in support of this product, but she would repurchased as a quality moisturiser." (@1984musicman, **541 likes**) |
| "Looks the same", no visible change in a demo | 6 | "Looks the same to me" (@Mimi0427-c6h, **921 likes**, Medicube pad Short, 846K views) |
| Questions on use (dry or oily mature skin, with retinol, before make-up, adding serum) | 6 | "I use retinal but I'm scared to add a toner pad in my routine." (@habsign4355) |
| Vegan, sensitive or fragrance concerns | 4 | "the one thing that i so relieved is a VEGAN, because my skin is very sensitive." (@skinloverishere) |
| Influencer honesty, undisclosed ads | 3 | "oh how i love undisclosed ads!" (@haveyoufoundClosure, **2.1K likes**) |
| Collagen can't absorb | 2 | "collagen cannot be absorbed through the skin, so the collagen is not what's soothing your skin." (@jbeandip, 103 likes) |
| Pads dry out in the jar | 2 | "i think EVERY toner pad should come with a seperate serum or toner for when it becomes dry" (@Aasya_10_Reads, 29 likes) |
| Waste or environment | 1 (+ a 3.6M-view Short) | "toner pads are bad for enviroment, just use toner" (@1ndonlykatz) |
| Pores worse | 1 | "No me gustan, me deja los poros abiertos. Dinero tirado a la basura" (@vanessaperez5492, ~Oct 2026) |
| PDRN injection did nothing | 1 | "I had PDRN injected under my eyes and it did absolutely nothing beyond the temporary swelling." (@Criticalbeauty411, 161 likes) |
| Low PDRN level in VT | 2 | "But VT has only 0.5ppm of Pdrn , they just market it as 10% on their packaging." (@Neha_bajetha, ~Oct 2026) |

The dermatologist Short "DOWN WITH TONER PADS!!!" (#dermreacts, **3,600,000 views**) says in full: "I stopped using toner pads I don't think anybody should use them because they're bad for the environment microfibers ... facial sprays are a much better option."

### 6.4 Complaints and failures seen in the category
- Breakouts: BestReviews cons, Medicube: "Some users had issues with breaking out after just a couple of days of use." VT: "more consistent acne flare-ups when using these on a daily basis."
- Pads too thin (Mediheal, BR).
- Pads dry out near the bottom of the jar (YouTube, 2 comments).
- No visible change (6 comments).
- Value: "per-use cost is significantly higher than the liquid toner equivalent" (dermfnd.org on the Anua pad, search snippet).
- Glow Recipe: a Sephora reviewer "felt other toner pads gave better results" (search snippet).

### 6.5 Not reachable
- **Reddit** (r/AsianBeauty, r/SkincareAddiction, r/30PlusSkinCare, r/Skincare_Addiction): **not found**. Direct loads return HTTP 403, and the search tool cannot reach reddit.com.
- **TikTok comments:** not pulled. No Luxe TikTok video was found to analyse.

---

## 7. The category as a whole (brief point 7)

### 7.1 What PDRN is, plainly
- **PDRN = polydeoxyribonucleotide:** short pieces of DNA, mostly purified from **salmon or trout sperm**. That is where the "salmon sperm facial" nickname comes from. On labels it appears as **Sodium DNA** or **Hydrolyzed DNA** (Kim, *Pharmaceutics* 2025;17(8):1024).
- **How it is thought to work:** it acts on the adenosine A2A receptor, which in lab and wound studies calms inflammation and pushes repair cells (fibroblasts) to make collagen (Dr Dray transcript; Kim 2025).
- **Medical use:** Korea's MFDS approved PDRN as a **pharmaceutical injection for tissue regeneration and wound healing** (skin grafts), and Italy's **Placentex** has been sold since the early 1990s (Kim 2025). Dr Dray cites a trial of salmon PDRN **injected** around diabetic foot ulcers that showed faster healing than placebo.
- **PN vs PDRN:** "PN" (polynucleotide) means longer, heavier DNA chains. **Rejuran**, the "salmon sperm" injection Kim Kardashian had, is classed in Korea as a PN **medical device**. The terms are used loosely, and "no standardized criteria have been established to delineate molecular weight thresholds" (Kim 2025).
- **Safety of the injections:** "PDRN injections have not been clinically associated with serious adverse effects" (Kim 2025).

### 7.2 Injections vs creams, serums and pads: what the evidence shows
- **Injected PDRN or PN for the face:** small trials only. In a 27-person split-face trial, the Rejuran side scored higher on a global aesthetic scale at 16 weeks (Dermatology Times, 11 Jul 2026). Dr Dray: "Injecting salmon derived PDRN for anti-aging benefit purely anecdotal at this point."
- **Topical PDRN:** "PDRN fragments range from 50 to 1,500 kilodaltons"; "molecules larger than approximately 500 Daltons are unlikely to penetrate intact human skin"; "PDRN applied topically without an active delivery mechanism is unlikely to reach the fibroblasts in the viable dermis." The only topical human data cited is "a single small study using a specific low-MW plant-derived PDRN that is not representative of the majority of products on the market." Verdict: "Is this a myth? Yes, but there is some truth to it!" (Dermatology Times, Marie Bosslett, 11 Jul 2026).
- **Dr Dray** ("PDRN Skincare: The Science Behind the Hype", 144,164 views): "applying salmon derived PDRN to human skin for anti-aging benefit. Nothing there." Also: "I'm highly, highly, highly doubtful that these skincare products with PDRN do anything above and beyond moisturize the skin." She still liked the VT essence "as a really nice moisturizer" because of its niacinamide, ceramides and humectants.
- **Reviews (search snippets, not opened):** a 2026 Cureus systematic review found only 7 randomized trials (183 participants) across rejuvenation, scars and wounds. An IMCAS appraisal of 350+ papers says PDRN "should not be positioned as a gold-standard regenerative solution".
- **Dose in pads (measured from retailer INCIs):** Medicube 1 ppm; Anua and Isntree 100 ppm; Biodance 1,000 ppm; Skinfood 10 ppb. One Eye Beauty cites 0.1 to 0.2% (1,000 to 2,000 ppm) as the level used in clinical work (her statement, not verified). By that yardstick, most pads, Luxe's likely included, carry 10 to 1,000 times less.

**Reading:** a PDRN pad works as a hydrating pad. Any benefit you can see comes from the humectants, niacinamide and mask time. The PDRN is a story ingredient at cosmetic doses.

### 7.3 Plant "PDRN" vs real
- "Vegan PDRN" from ginseng (VT), carrot (Skinfood), seaweed (Isntree), rose (numbuzin), matcha (TirTir) or peony is **DNA extracted from plants**, sold under the same INCI "Sodium DNA". Dr Dray: there is "no actual clinical data on it". One expert quoted in the press says its "purity and molecular weight differ from fish-derived PDRN" and that there is not enough evidence yet (search snippet).
- Some brands quote huge "ppm" figures for the *extract* rather than the DNA. One Eye Beauty cites VT at "100,000 ppm of ginseng-derived PDRN", while a commenter says VT lists the PDRN "only 0.5ppm" and at the bottom of the INCI. **Reading:** marketing percentages for PDRN are not comparable across brands.
- **Luxe uses salmon**, which is the "original" source, but at a cosmetic dose.

### 7.4 Salmon PDRN, fish allergy and vegan concerns
- BestReviews (Feb 2026): "People with fish or seafood allergies should avoid salmon-derived PDRN pads."
- Press dermatologists disagree about whether purification removes fish proteins. One retailer blog says it does; others say it depends on each brand's process and that topical PDRN is not regulated like a medical device (search snippet, 2026-10-31). No clinical study compares allergic reactions to salmon and plant PDRN (not found).
- **Luxe-specific:** salmon DNA plus collagen of unstated source plus soy. Anyone with fish, shellfish or soy allergies should not use it without a doctor's advice. **The pads are not vegan**, although luxe.com says "All our products are vegan".

### 7.5 Toner pads: irritation, purging, sensitive skin
- **Purging** (a short spell of breakouts as cell turnover speeds up) happens with exfoliating acids and retinoids. **The Luxe pad has neither**, so a breakout from it would be a reaction or clogging, not purging (reading from the INCI). The user should stop and patch test.
- Irritation risk is low for this formula: no fragrance, alcohol or acids. Botanical extracts (neem, Coptis, turmeric) and niacinamide can still sting very reactive skin.
- Rubbing hard with a textured pad can irritate thin mature skin. Pressing, or using the mask method, is gentler.
- Hygiene: use tweezers, close the lid (Medicube: "Keep the lid closed and sealed to prevent the pad from drying out").

### 7.6 The TikTok and search trend: how fast PDRN rose
| Figure | Source | Date |
|---|---|---|
| Olive Young searches for "PDRN" **+695%** | Olive Young report via search snippet (themonodist.com) | Sep 2025 |
| PDRN: 37.2M avg monthly interactions (Google, TikTok, Instagram), **+609.8% YoY**; forecast +34.4% next year; Medicube 5.6M interactions (+161.3%), Rejuran 830.2K, Anua 381.5K | Spate blog (measured) | © 2026, pulled 2026-10-31 |
| Google +169.6% YoY, TikTok +487.5% YoY | Happi citing Spate (search snippet) | 2025/26 |
| Vegan PDRN TikTok interest +414% | Search snippet (BeautyMatter) | 2026 |
| PDRN in 33 of the Top 50 "skin longevity" products on Olive Young (Oct 2025 to Mar 2026) | Search snippet | 2026 |
| Medicube "Mix & Match Toner Pad Set" top TikTok Shop video: 37,006,521 views | sellthetrend tracker (search snippet) | Aug 2026 |
| YouTube Shorts: Medicube DIY salmon gel pads 846K views; "My favourite toner pads!" 353K; Medicube PDRN jelly pads 241K | NexLev | 2026-10-31 |
| Amazon PDRN units **▼40.2%** month on month in July 2026 | ASINSIGHT | Jul 2026 |

**Reading:** PDRN went from niche to mainstream between mid-2025 and early 2026, led by Medicube and Rejuran. Interest is still high, but Amazon unit sales were already falling in summer 2026. The market is crowded, and every K-beauty brand now has a PDRN pad.

### 7.7 Myths viewers hold, and the facts
| Myth | Fact |
|---|---|
| "It's the same as the salmon-sperm injection" | Injections put PN or PDRN into the dermis. A pad leaves it on the surface, at a far lower dose |
| "99% PDRN" | That is the raw material's purity. Pads hold 1 to 1,000 ppm |
| "Plant PDRN is the same thing" | Different source and size; no clinical data |
| "Collagen in the pad builds collagen" | Topical collagen is a humectant and does not join your skin's collagen (commenters said this too) |
| "One pad replaces your routine" | You still need moisturiser and, by day, sunscreen |
| "PDRN repairs at the cellular level" | Shown in cells, wounds and injections, not for topical cosmetics |

### 7.8 What viewers search for and ask (measured from search and comment data)
- YouTube titles that perform: "Which Korean Toner Pads Suit Your Skin?", "Korean toner pads for each skin type" (167K), "Toner Pad Tips You Need To Try!" (407K), "2 ways to use toner pads" (90K), "When Should You Use Toner Pads? Dermatologist Explains" (58K), "PDRN Skincare: The Science Behind the Hype" (144K), "What Actually Works for Mature Skin?" (39K).
- Comment questions: Do they dry out? Can I use them with retinol? Which suits dry or oily mature skin? Do I need serum after? Before make-up? What is the difference between salmon, rose and aloe PDRN? Is it vegan?

---

## 8. Selling it honestly on YouTube (brief point 8)

### 8.1 Claims that are reasonable (cosmetic, supported by the formula)
- "A hydrating gel pad: skin looks plumper, dewier and smoother right after use" (Anua-tested formula: an immediate, temporary hydration boost).
- "Use it two ways: as a 5-minute mini mask, then wipe."
- "Fragrance-free and acid-free, so it's gentle for most mature skin. Patch test first."
- "With niacinamide, which can help the look of uneven tone with daily use over weeks."
- "Contains salmon-derived PDRN, the K-beauty ingredient everyone's talking about." Say plainly that topical PDRN's evidence is early.

### 8.2 Claims to avoid
- "Repairs skin at the cellular level", "rebuilds underneath", "regenerative", "the same as Korean clinic treatments". These describe injections, not this pad, and sound like drug claims.
- "Fades dark spots in 4 weeks", "firms crepey neck skin", "lifts". These are not shown for this product.
- "Clinically proven", "125% more hydration", "100% saw firmer skin". **Those figures come from Anua's test on Anua's pad (21 women, one self-assessment).** Quoting them for Luxe would repeat borrowed data.
- "99% pure PDRN" or "high concentration": the PDRN is likely 0.01%.
- "Exfoliates" or "has PHA": there is no acid in the INCI.
- "Vegan": it is salmon-derived.
- "Dermatologist-tested, hypoallergenic": no evidence published (not found).
- Reading out the brand-site testimonials or the "10,839 reviews" badge: these are template content and a site-wide number.
- Under FTC rules, any affiliate or sponsored relationship must be disclosed. "Undisclosed ad" comments got 2.1K likes on one Short.

### 8.3 Who should not use it, and warnings to say on air
- Fish or seafood allergy (salmon DNA; collagen source unstated), soy allergy (soybean ferment).
- Vegans.
- Very reactive skin, rosacea or eczema: patch test on the jaw for 2 to 3 days.
- Stop if it stings, burns or causes breakouts. That is not "purging", because there are no acids in it.
- Keep it out of the eyes. Medicube ("excluding the area around your eyes and mouth"), Mediheal and Biodance say to avoid the eye area when wiping. Luxe's "underarms, elbows, knees" use is unusual but harmless (reading).
- Use sunscreen by day if the goal is dark spots.

### 8.4 Red flags for the operator to weigh before selling (reading)
1. The listing reuses **another brand's images, product name and clinical numbers** (Anua), without the footnotes.
2. **The page and the label conflict**: 100 vs 140 pads; a PHA and a vitamin C derivative that are not in the INCI; vegan brand vs salmon product.
3. **Template "Verified Buyer" reviews** shared with another product and dated before launch. Survey counters show "0%".
4. **Two different companies**: Luxe Cosmetics B.V. (NL) runs luxe.com, and Luxe Research LLC (WY) runs luxeresearchlab.com. Both use the vendor name "Luxe Cosmetics US".
5. **Pre-order and scarcity banners** ("Sold out", "70% sold"), and a price on the same page that runs from $59.95 to $39.99 for two jars.
6. The JIYU parallel: a TikTok-ad K-beauty pad brand aimed at older women, publicly called "fake" (James Welsh, 249,607 views). Viewers in this space are alert to that pattern.

If the operator still promotes it, the Amazon listing should be checked by hand (title, INCI photo, price, reviews) to see whether it repeats these issues.

---

## 9. Not found / open items
- Amazon: full title, price and price history, star rating, review count, review text, Q&A, listing date and seller name for B0HM229JP6.
- The exact PDRN concentration in the Luxe pads (Luxe states none; 100 ppm is inferred from Anua's identical list).
- The manufacturer or country of manufacture (the page says "Born in Korean Labs"; no maker is named).
- Any clinical test of the Luxe product itself.
- Reddit threads (blocked) and TikTok videos or comments on the Luxe pads (none found).
- Amazon ratings and review counts for competitor PDRN pads (Amazon blocked; retailer ratings given where found).
- Pad count for Medicube's medicube.us jelly pad listing.
