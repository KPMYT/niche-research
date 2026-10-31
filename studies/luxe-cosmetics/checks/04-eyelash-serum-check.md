# Check of `04-eyelash-serum.md` (Luxe Eyelash Serum, B0C21JM5PY)

Checked by a separate helper on **2026-10-31**. I did not use the first helper's saved files as evidence. I pulled every source again myself: brand pages and Shopify catalogues with curl, the Latisse label from DailyMed, abstracts from PubMed E-utilities, the EU pages directly, and YouTube through NexLev. I made 2 web searches, both for the EU ban status. I did not load Amazon, and I did not retry revitalash.com after it returned 403.

Verdicts:
- **Confirmed**: I saw the same thing in the source.
- **Wrong**: the source says something different.
- **Partly / needs a fix**: the claim is broadly right but missing something or slightly off.
- **Unverifiable**: I could not reach the source.

---

## 1. Ingredient list and related claims

| Claim in report | Verdict | What I saw (URL, pulled 2026-10-31) |
|---|---|---|
| The full list, in this order: "Purified Water (Aqua), Glycerol, Panax Ginseng Extract, Vitamin B7 (Biotin), Vitamin E (Tocopherol), Arginine/lysine polypeptide, 1,2-hexanediol, tripeptide-1, octyl hydroxamic acid, Myristoyl Pentapeptide-4" | **Confirmed**, word for word and in the same order | https://luxe.com/products/luxe-eyelash-growth-serum-1-1-free, FAQ "What are the ingredients?" |
| The German list | **Confirmed**, word for word: "Destilliertes Wasser (Aqua), Glycerin, Panax Ginseng Extrakt, Vitamin B7 (Biotin), Vitamin E (Tocopherol), Arginin/Lysin Polypeptid, 1,2-Hexandiol, Tripeptid-1, Octylhydroxamsäure, Myristoyl Pentapeptid-4" | https://luxecosmetics.de/products/luxe-wimpernserum |
| The second US page gives a shorter marketing list that includes rosemary and magnolia | **Confirmed**: "a blend of peptides (Myristoyl Pentapeptide-4, Tripeptide-1), biotin, Panax ginseng extract, rosemary extract, magnolia bark extract, glycerin, and vitamin E. It's 100% vegan, paraben-free, fragrance-free, and prostaglandin-free." | https://luxe.com/products/lash-growth-serum |
| "Luxe is 100% prostaglandin-free" and "What we DON'T use: ✗ Prostaglandins" | **Confirmed**, both on the US page. The German product page has no prostaglandin wording | https://luxe.com/products/lash-growth-serum |
| Rosemary and magnolia are advertised as "key" ingredients but are missing from both full lists | **Confirmed**. US page: "Rosmarinus Officinalis (Rosemary) Extract" and "Magnolia Bark Extract — Reduces premature lash shedding". The second US page: "Rosmarinus Officinalis Extract — Restores natural lashes", "Magnolia Officinalis Bark Extract — Reduces hair loss". German page: "Rosmarinus Officinalis Extract", "Magnolien Rindenextrakt". Neither appears in the 10-item full list | the three pages above |
| "No preservatives", while 1,2-hexanediol and octyl hydroxamic acid are listed | **Confirmed, and now sourced.** Brand: "Our serums do not contain preservatives, so you have a shelf life of 4 months" (US, in English) and "Unsere Seren enthalten keine Konservierungsstoffe" (DE). INCIDecoder on 1,2-hexanediol: it can "boost the antimicrobial activity of preservatives". On caprylhydroxamic acid (= octyl hydroxamic acid): "A chelating agent that helps to preserve cosmetic products… also acts as a biostatic and fungistatic agent… often coupled with antimicrobial glycols… to create a 'preservative free preservative system'". Reading: these are preservative-system ingredients, so the claim is misleading, though perhaps technically defensible. The report's "doubtful" is fair. Fix: it can now cite these pages instead of "I did not pull a source page" | https://incidecoder.com/ingredients/1-2-hexanediol ; https://incidecoder.com/ingredients/caprylhydroxamic-acid |
| Myristoyl pentapeptide-4 has CosIng function "skin conditioning" and is in about 25 lash serums on INCIDecoder | **Confirmed.** It is listed as "skin conditioning". I counted 24 lash or brow products among the first 60 product listings (Peptide Labz, SheGlam, Silly George, Terez&Honor and others). "Cheap" is the report's reading | https://incidecoder.com/ingredients/myristoyl-pentapeptide-4 |
| MP-4 is "**not** myristoyl pentapeptide-17, the 'lash peptide' used by The Ordinary and GrandeLASH Peptide+" | **Confirmed, with a nuance.** The Ordinary contains MP-17 and no MP-4. GrandeLASH Peptide+ contains MP-17 and MP-8. Nuance: INCIDecoder gives MP-17 the *same* CosIng function, "skin conditioning". The real difference is that INCIDecoder describes MP-17 as known to "stimulate keratin genes" and says that, combined with myristoyl hexapeptide-16, it can "visibly increase eyelash length after two weeks" (supplier-style data). So §4's contrast of "a generic 'skin-conditioning' one" against MP-17 is a little unfair. Both are "skin conditioning" in CosIng; MP-17 simply has the lash-length marketing data | https://incidecoder.com/ingredients/myristoyl-pentapeptide-17 |
| The Ordinary Multi-Peptide Lash and Brow Serum: MP-17, biotinoyl tripeptide-1, acetyl tetrapeptide-3, caffeine; no prostaglandin; 5 mL; $14.90 | **Confirmed.** The brand's own list: "Aqua (Water), Glycerin, Butylene Glycol, Myristoyl Pentapeptide-17, Biotinoyl Tripeptide-1, Oligopeptide-2, Acetyl Tetrapeptide-3, Caffeine, Panthenol, Arginine, Glycine, Glycoproteins, Larix Europaea Wood Extract, Trifolium Pratense Flower Extract, Camellia Sinensis Leaf Extract, Dextran, Maltodextrin, Zinc Chloride, … 1,2-Hexanediol, Sodium Benzoate, Benzoic Acid, Ethylhexylglycerin, Phenoxyethanol, Chlorphenesin." It has no prostaglandin analogue. The brand page shows 5 ml and price "14.90", which upgrades the report's "size from retailer URL, snippet" to measured. The INCIDecoder list matches | https://theordinary.com/en-us/multi-peptide-lash-and-brow-serum-100111.html ; https://incidecoder.com/products/the-ordinary-multi-peptide-lash-and-brow-serum |

**Extra points the report missed:**
- The "safe for cancer patients" claim is also on the **US English** page: "Our formula is specially formulated to be gentle and safe for everyone, including cancer patients!" (luxe.com/products/luxe-eyelash-growth-serum-1-1-free). The report attributes it only to luxecosmetics.de. The same applies to "no preservatives", which is also in English on luxe.com.
- luxe.com says "Each package contains the Luxe Eyelash Serum and instructions." Ashley Barfuss's Amazon box "does not come with instructions". This is a small inconsistency between the brand's claim and an Amazon buyer.

## 2. Marketing red flags (all on luxe.com unless stated)

| Claim in report | Verdict | Quote seen |
|---|---|---|
| Customer counts of 97K, 197K and 1,197K | **Confirmed**, with context. "1,197,000+ Happy Customers" (top banner) and "Join over 1,197,000+ members" (newsletter footer). "97,000+ orders processed", "How 97,000+ Women Are Growing…", "Rated 4.8/5 by more than 97,000 REAL customers". "✓ 197,000+ orders processed since 2021 / ✓ Less than 1% refund rate (195,030+ women kept their kits) / ✓ 7,871 verified 5-star reviews / ✓ 4.97 out of 5". Context: the 197K block mentions "kits", "whether the curl isn't dramatic enough" and "better than my salon lifts", so it is lash-lift-kit copy pasted onto the serum page. That is a further red flag. German page: "97.000+ Zufriedene Kunden" |
| "Zero side effects" | **Confirmed**: "Zero side effects" (under the price box); also "Zero reported side effects" and "Zero reported injuries across 97,000+ uses" (lash-growth-serum page) |
| "Clinically proven" | **Confirmed**: "Clinically proven / To deliver real results" (1-1-free page); "Klinisch nachgewiesen" (DE). No study is cited on either page |
| "70% more length by week 12" | **Confirmed**: "70% more length by week 12"; "Up to 70% more visible length" (lash-growth-serum); "up to 70% more length and 40% more thickness by week 8-12" (1-1-free); "bis zu 70% mehr Länge und 40% mehr Dicke in Woche 8-12" (DE) |
| "Safe for cancer patients" (German page) | **Confirmed** on DE ("sicher für jeden zu sein, auch für Krebspatienten!") **and also on the US page in English** (see section 1) |
| "⏰ LIVE: 2,847 orders yesterday \| Low inventory" | **Confirmed**: " ⏰ LIVE: 2,847 orders yesterday \| Low inventory \| Limited Offer", with a countdown "02 d 00 h 00 m 00 s". Also "Free Lashlift Set included for the next 100 orders!" and "Eyebrow Serum included for the next 11 orders!". The report's quotes are accurate |
| Three guarantee lengths on one page | **Confirmed, and there is a fourth.** lash-growth-serum page: "30-day money back guarantee", "60-Nights Risk Free Trial… full refund for up to 60 days" and "Less than 1% of our customers have claimed their 90 day Money Back Guarantee". The 1-1-free page (and DE) adds a fourth condition: "If you don't achieve any results after consistent use of 12 weeks you have right to claim for money-back guarantee" |
| Reviews: "Based on 6 reviews" on the second page; structured data says 5.0 from 49 on the first page | **Confirmed**: "Based on 6 reviews" (1-1-free); JSON-LD `"ratingValue": 5.0`, `"reviewCount": 49` (lash-growth-serum) |
| Prices: $29.95 (crossed-out $49.95), $44.95 for 2, $59.95 for 3; body text "$29.99"; DE €29.95 | **Confirmed** for luxe.com, including "Luxe Eyelash Growth Serum — $29.99" in the body. I did not re-check the € price |

## 3. Rival ingredients and prices

| Rival | Claim in report | Verdict | What I saw |
|---|---|---|---|
| GrandeLASH-MD | Isopropyl cloprostenate; $68 / $36 / $125 for 2 / 1 / 4 mL | **Confirmed**. The list includes "Isopropyl Cloprostenate (an analog of prostaglandin)", and the page warns "This cosmetic product contains (a small amount of) isopropyl cloprostenate, an analog of prostaglandin". Prices from Shopify: 2 mL $68.00, 4 mL $125.00, 1 mL $36.00 | https://www.grandecosmetics.com/products/grandelash-md ; /products.json |
| GrandeLASH Peptide+ | Prostaglandin-free; MP-17, MP-8, biotinoyl tripeptide-1, sh-oligopeptides; $48 / $28 for 4 / 2 mL | **Confirmed**. The page says "clinically tested, prostaglandin-free formula" and "Formerly GrandeLASH…". The list includes Biotinoyl Tripeptide-1, Sh-Oligopeptide-10, Sh-Oligopeptide-2, Myristoyl Pentapeptide-8 and Myristoyl Pentapeptide-17, with no analogue. 4 mL $48.00, 2 mL $28.00 | https://www.grandecosmetics.com/products/grandelash-peptide |
| Babe Essential Lash Serum | Isopropyl cloprostenate; $49 / $89 / $29 for 2 / 4 / 1 mL | **Confirmed**. The list includes "Isopropyl Cloprostenate (an analog of prostaglandin)", and the page says "This product contains a small amount of isopropyl cloprostenate, a synthetic prostaglandin analog". The words "Prostaglandin-Free" also appear on this page, but only in the site menu (a "Peptide Formulas / Prostaglandin-Free" nav link), not about this product. Prices: 2 mL $49, 4 mL $89, 1 mL $29 | https://babelash.com/products/essential-eyelash-serum |
| Babe Renewing | Prostaglandin-free; copper tripeptide-1, MP-8; $49 / $29 for 6 / 3 mL | **Confirmed**. "Prostaglandin-Free Peptide Lash Serum"; the list includes Myristoyl Pentapeptide-8 and Copper Tripeptide-1. It also contains Myristoyl Pentapeptide-17, Myristoyl Hexapeptide-16 and Biotinoyl Tripeptide-1, which the report does not mention but which does not make it wrong. 6 mL $49, 3 mL $29 | https://babelash.com/products/renewing-serum |
| neuLASH | Isopropyl cloprostenate; $95 for 3.2 mL; quoted warning | **Confirmed**. The list includes "Isopropyl Cloprostenate", and the warning reads word for word: "This cosmetic product contains isopropyl cloprostenate, a synthetic prostaglandin analog". 3.2 mL $95.00 | https://neulash.com/products/neulash-lash-enhancing-serum |
| RevitaLash Advanced | DDDE | **Confirmed** on INCIDecoder: "Aqua, Glycerin, Biotin, Cellulose Gum, Phenoxyethanol, Chlorphenesin, Disodium Phosphate, Phosphoric Acid, Dechloro Dihydroxy Difluoro Ethylcloprostenolamide, …". revitalash.com returned 403 (not retried), so the brand's own list and the $100 / $152 prices are **unverifiable** and stay snippet-grade, as the report says | https://incidecoder.com/products/revitalash-advanced-eyelash-conditioner |

**Price-per-mL spot checks (arithmetic from the prices above):**

| Row | Report | My calculation | Verdict |
|---|---|---|---|
| GrandeLASH-MD 2 mL | 34 | $68 / 2 = 34.00 | Confirmed |
| neuLASH 3.2 mL | 29.69 | $95 / 3.2 = 29.69 | Confirmed |
| Babe Renewing 6 mL | 8.17 | $49 / 6 = 8.17 | Confirmed |
| The Ordinary 5 mL | about 2.98 | $14.90 / 5 = 2.98 | Confirmed |
| Babe Essential 2 mL | 24.50 | $49 / 2 = 24.50 | Confirmed |
| Luxe, Amazon / brand site | 4.33 / 9.98 | $13 / 3 = 4.33; $29.95 / 3 = 9.98 | Confirmed. The $13 Amazon price itself was not re-checked: no Amazon load |

## 4. Latisse label and the studies

**Source:** DailyMed SPL for LATISSE (Allergan), setid 34f83d9d-2c64-463e-8a90-9a460fedfead, version 25, published 23 Dec 2025 (https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34f83d9d-2c64-463e-8a90-9a460fedfead). The report cites the rxabbvie PDF "Revised 7/2024". The figures below are the same in the current DailyMed version.

| Claim | Verdict | Label text |
|---|---|---|
| 278 adults, 4 months | **Confirmed** | "parallel study including 278 adult patients for four months of treatment" |
| 78% vs 18% at week 16 (plus 15/8, 50/15, 69/20, 79/21) | **Confirmed**: "16 \| 107 (78%) \| 26 (18%)". Every row of the week table matches. Week 1 (5% vs 2%) is omitted in the report, which is fine |
| Length +25% (vehicle 2%); fullness +106% (12%); darkness +18% (3%) | **Confirmed**: "1.4; 25%" vs "0.1; 2%"; "0.7; 106%" vs "0.1; 12%"; "-20.2; -18%" vs "-3.6; -3%" (a negative value means darker lashes) |
| Iris darkening likely permanent; may take "several months to years" | **Confirmed**: "Iris pigmentation is likely to be permanent" (5.2); "may not be noticeable for several months to years" |
| Glaucoma interaction (5.1) | **Confirmed**: section 5.1 "Effects on Intraocular Pressure": "exposure of the eye to more than one dose of bimatoprost daily may decrease the intraocular pressure lowering effect" |
| Cataract / macular edema caution (5.6) | **Confirmed**: section 5.6 "Macular Edema": "used with caution in aphakic patients, in pseudophakic patients with a torn posterior lens capsule, or in patients with known risk factors for macular edema" |
| Common side effects in "less than 4% of patients" | **Confirmed** |
| "Upon discontinuation… return to its pre-treatment level" | **Confirmed** |
| Contact lenses (5.8) | **Confirmed**: section 5.8 is "Use with Contact Lenses" |
| French study: about 30% of 79 lash cosmetics contained a prostaglandin analogue | **Confirmed**, with a framing note. Abstract: "A qualitative study was carried out on 79 cosmetic products… About 30% of them contain a prostaglandin analogue. Six prostaglandin analogues were found, including bimatoprost and norbimatoprost. The most common are ethyl tafluprostamide… (DDDE), and isopropyl cloprostenate." Couteau & Coiffard, Ann Pharm Fr 2026;84(5):889-898, PMID 42269767. Note: this reads like a review of formulas or labels ("formulated with"), not a lab test for hidden ingredients. Listing it in §7.6 under "Hidden prostaglandins" overstates it slightly. It shows how common these analogues are, not that they are hidden |
| Japan study: 64 serums, 4 with bimatoprost, 3 undeclared, plus 8 with other analogues | **Confirmed**: "64 eyelash serum samples were purchased from 34 websites… four were found to contain bimatoprost, among which, three did not indicate their contents on their package labels… eight products contained other PGF2α analogs". Rahman et al., J Pharm Biomed Anal 2022;219:114940, PMID 35882176 |
| SCCS Final Opinion on 10 Feb 2026 | **Confirmed**, with a detail. The EC page shows "Final Opinion" dated **10 February 2026** (publication). The citation line reads: "preliminary version of 28 May 2025, final version of 2 February, SCCS/1680/25". So the opinion was adopted on 2 Feb 2026 and published on 10 Feb. The conclusion quote is on the EC page itself, so it is measured, not only a snippet: "none of them can be considered safe for use in cosmetic products intended for promoting the growth of eyelashes and eyebrows". https://health.ec.europa.eu/publications/sccs-prostaglandin-analogues-methylamido-dihydro-noralfaprostal-mdn-isopropyl-cloprostenate-ipcp_en |
| No EU restriction adopted ("not found") | **Confirmed that nothing is adopted yet, but the report is incomplete: a ban is in progress.** (1) WTO notification G/TBT/N/EU/1219 was filed on 8 July 2026. The draft amends Annex II to prohibit "prostaglandins and their analogues"; comments closed 6 Sep 2026; "the Regulation is expected to be adopted in Q4 2026" (CIRS, 2026-07-16, https://www.cirs-group.com/en/cosmetics/eu-cosmetics-regulation-updated-involving-annexes-ii-iii-and-v). (2) Council document 13462/26 ADD 1, dated 22 Sep 2026, carries the draft Commission Regulation D(2026) 117774 with a new Annex II entry, "Prostaglandines and their analogues". From [12 months after entry into force] such products "shall not be placed on the Union market", and from [24 months] they "shall not be made available" (https://data.consilium.europa.eu/doc/document/ST-13462-2026-ADD-1/en/pdf). I found no Official Journal publication (2 web searches). Fix: the report's §7.5 and §9 should say "draft EU ban in progress (WTO-notified July 2026, sent to Council Sept 2026, adoption expected Q4 2026); not yet in force" |

## 5. YouTube (NexLev, pulled 2026-10-31)

| Claim | Verdict | What NexLev returned |
|---|---|---|
| "Ageless!…" review 12dTKpvKhyw: 47 views, published 2026-09-15 | **Confirmed**: viewCount 47, likes 0, publishDate 2026-09-15, title "Luxe Eyelash Serum" | `youtube_video_details` |
| Quote "it burned every time I put it on… I wouldn't spend my money on this one" | **Confirmed.** The transcript has "But it burned every time I put it on" (1:26) and "So, again, I wouldn't spend my money on this one" (2:28). The ellipsis joins two separate lines about a minute apart, which is acceptable. Also confirmed word for word: "So I tried this for only 5 days. And the reason only 5 days is because it burned", "This is way more of a burn", "I would also pass on this one", "Didn't start to taper down", "probably 10 years". Extra detail: she poured the product out and now uses the tube "as a travel case for my Latisse" | `get_video_transcript` |
| Ashley Barfuss JW3zXgn1hgU: 701 views, 6 likes, 2026-03-30, Amazon affiliate | **Confirmed**: viewCount 701, likeCount 6, published 2026-03-30. The description says "Buy it here (affiliate link)… As an Amazon Associate". Quotes confirmed: "It does not come with instructions", "I don't have any stinging in my eyes. I don't have any um tenderness there", "gentle enough for somebody that has sensitive eyes and sensitive skin" | `youtube_video_details`, `get_video_transcript` |
| 1.5K-like comment (@Hopeful-w7h) | **Confirmed** on Dr Dray ugIVUGBgxoA: likesCount "1.5K", "I've considered a lash serum, but when I did my research and read about the side effects, I decided my lashes were ok as is." Also confirmed on the same video: @pinkpeony5302 737, @sharischmidt4712 862, @loreej2479 307 | `youtube_video_comments` (top) |
| 334-like comment (@marystewart5555) | **Confirmed in the report's saved pull, but it was not in my live top-20 for tiRLNc6_A0E.** My top-20 (sorted "top", 1.1K comments) had @jazzogbonnie at **295** (matching the report) and @carynnoah1961 at 128, but no @marystewart5555. The report's saved JSON puts it on tiRLNc6_A0E at 334 likes. YouTube's "top" order can change between calls, so this is probably still real, but I could not see it myself. Verdict: **unverifiable in this check**. The 295-like "safe brands" request and the @isie. light-blue-eyes comment (51) are confirmed | `youtube_video_comments` |
| Barbara Formann "Wimpern ab 60 - voll und schön?" (-CkalOVFWn8): 116,582 views in 5 days | **Confirmed**, allowing for time. Now 116,592 views and 1,282 likes, published 2026-10-25. So it is 6 days old on 2026-10-31; "5 days" was right at the first pull | `youtube_video_details` |

---

## Summary

**Held up:** the full ingredient list (both languages, exact order); the prostaglandin-free wording; rosemary and magnolia advertised but missing from the full list; "no preservatives" alongside 1,2-hexanediol and caprylhydroxamic acid; every marketing quote (97K / 197K / 1,197K, "Zero side effects", "Clinically proven", "70% more length by week 12", "LIVE: 2,847 orders yesterday", 30-day / 60-night / 90-day guarantees, 6 vs 49 reviews); all five rival ingredient checks and all price-per-mL spot checks; every Latisse label figure and section; the French and Japan study numbers; the SCCS opinion; the two Luxe YouTube reviews and their quotes; the 1.5K comment; Barbara Formann's views.

**Needs fixing in the report:**
1. **EU status is out of date.** A ban is drafted, WTO-notified (8 Jul 2026) and sent to the Council (22 Sep 2026), with adoption expected Q4 2026. "Not found" should become "draft ban in progress, not yet adopted".
2. "Safe for cancer patients" and "no preservatives" are on the **US English** page too, not only the German one.
3. There is a **fourth** guarantee condition (the 12-week "no results" money-back rule). The 197K block is lash-lift-kit copy reused on the serum page.
4. MP-4 and MP-17 have the *same* CosIng function ("skin conditioning"). The difference is that MP-17 has supplier lash data, so §4's "generic skin-conditioning" contrast is slightly unfair.
5. The French 2026 study looks like a formula or label review, not a hidden-ingredient lab test. It is placed under "Hidden prostaglandins" (§7.6).
6. The preservative point can now cite INCIDecoder instead of "I did not pull a source page".
7. The Ordinary's 5 mL and $14.90 can be upgraded to measured (brand page).

**Unverifiable here:** the @marystewart5555 334-like comment (not in my live top-20); RevitaLash prices and the brand's own list (revitalash.com 403); anything on Amazon.
