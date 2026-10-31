# Check: 01-mascara.md (checking helper, 2026-10-31)

I re-checked `studies/luxe-cosmetics/01-mascara.md` against the sources myself. I did not just read the other helper's raw files. Everything below was pulled on **2026-10-31**. I did not load Amazon (bot check): Amazon figures come from my own web-search snippets. I used 10 web searches.

**Verdicts:** **confirmed** (I saw the same thing at the source) · **partly confirmed** (the main point holds, a detail differs) · **wrong** · **unverifiable** (I could not reach a source that settles it).

---

## 1. The product

| # | Claim in the report | Verdict | What I saw (source, 2026-10-31) |
|---|---|---|---|
| 1.1 | Full Amazon title for B0GSXJCZ93: "Luxe Cosmetics Conditioning Peptide Mascara, Buildable Volume & Length, Long-Lasting Clump-Free Black, Lash Extension Friendly" | **confirmed** (snippet) | The same title appears on the US, UK and CA result pages: https://www.amazon.com/Luxe-Cosmetics-Conditioning-Long-Lasting-Clump-Free/dp/B0GSXJCZ93 · https://www.amazon.co.uk/Cosmetics-Conditioning-Buildable-Long-Lasting-Clump-Free/dp/B0GSXJCZ93 · https://www.amazon.ca/Luxe-Cosmetics-Conditioning-Long-Lasting-Clump-Free/dp/B0GSXJCZ93. A search for the bare ASIN in quotes found nothing. |
| 1.2 | Brand-site tagline "Built For Sensitive Eyes & Fine Lashes Over 50" | **confirmed** | Live page https://luxecosmetics.us/products/conditioning-mascara: "Luxe Conditioning Peptide Mascara / Built For Sensitive Eyes & Fine Lashes Over 50". |
| 1.3 | Water-based, pH balanced, removable with warm water | **confirmed** | Same page: "because the formula is water-based and pH balanced, it doesn't sting…"; "5. It comes off with warm water — no damage."; "Warm water dissolves it cleanly."; FAQ: "The formula dissolves cleanly with warm water and slides off." |
| 1.4 | Contradiction on one page: "Water Resistant" badge, "Waterproof (showers, pools, workouts)", and "comes off with warm water" | **confirmed** | All on the same live page: badges "pH Balanced / Hypoallergenic / **Water Resistant**"; slide text "**Waterproof (showers, pools, workouts)**"; "No waterproof formulas that require harsh removers…". The page also calls the product "Luxe Waterproof Mascara" twice ("97,000+ mature women have been using the Luxe Waterproof Mascara…"). The Amazon CA snippet also calls it "water-resistant". |
| 1.5 | $39.95 shown against "$59.95"; 2 for $54.95; 3 for $69.95 | **confirmed** | Live `.json` https://luxecosmetics.us/products/conditioning-mascara.json: variants "1 Set" 39.95 / compare-at 59.95; "2 Sets" 54.95 / 74.95; "3 Sets" 69.95 / 89.95; SKUs Con-mascara-1/2/3-bottle. The page shows "$59.95 $39.95" with the label "Normaler Preis". |
| 1.6 | The "waterproof" page uses the same SKU and title; compare-at $29.95 is below the $39.95 price | **confirmed** | https://luxecosmetics.us/products/luxe-waterproof-mascara.json: title "Luxe Conditioning Peptide Mascara", one variant "Black" 39.95, compare-at 29.95, SKU "Con-mascara-1-bottle", tag static_reviews_267. That product was created 2023-12-11 and re-published 2026-10-26. |
| 1.7 | Other stores: UK £24.95 vs £49.95; AU A$39.95 vs A$69.95; luxecosmeticslashes.com $29.95 vs $49.95 | **confirmed** | luxe-cosmetics.uk `.json` (both handles): 24.95 / 49.95. AU `.json`: 39.95 / 69.95. lashes store `.json`: 29.95 / 49.95. The UK *non-waterproof* page also lists £24.95, so the report's "(waterproof)" label is incomplete but not wrong. |
| 1.8 | On Luxe stores since 2023-12-06. **How was that date found?** | **confirmed, with a caveat** | The date is the Shopify `created_at` field in the product feed: `"created_at":"2023-12-06T11:33:21-08:00"`, `"published_at":"2023-12-14T12:18:14-08:00"` (luxecosmetics.us/products/conditioning-mascara.json; product id 8265320202498, the same id on luxe.com and luxe-cosmetics.com). UK record: 2023-12-20; AU: 2023-12-21 (local time); lashes store: 2026-08-04. **Caveat [reading]:** `created_at` dates the store's product record, not necessarily the formula. A record can be renamed or re-used, and the over-50 copy is dated 2026-08-26. I tried the Wayback Machine to see what the page showed in 2023, but the connection was reset (proxy) and I did not retry, so this is **unverifiable**. |
| 1.9 | Amazon UK: £14.99, list £18.99 | **confirmed** (snippet) | Snippet: "£14.99 with 21 percent savings" (14.99/18.99 = 21% off). |
| 1.10 | Size: "not found" | **confirmed, plus one new clue** | The live Shopify feed gives only grams 23 / 45 / 68 per 1/2/3 sets (shipping weight). **New:** an Amazon snippet says the UK listing gives **"29.57 ml"** and the US listing **"1 fl oz"**. 29.57 ml is exactly 1 fl oz, so both are one entry. That size is implausible for a mascara (Grande 5.6 g, Thrive 10.7 g) and looks like a listing placeholder. "Not found" stays correct; the report could add that the listing itself says 1 fl oz. |
| 1.11 | Amazon "Date First Available": not found | **new data, uncertain** | One amazon.ca snippet: "One listing gives a first-available date of **March 17 2026**". The snippet did not make clear which of the two CA listings (B0GSXJCZ93 or B0G65JT2QJ) it came from. This supports the report's reading that the Amazon listing dates from 2026. Not confirmed for this ASIN. |
| 1.12 | **Ingredient list (INCI): not found** | **confirmed: still not found** | Tried again: the `/products/<handle>.json` feed for both handles on luxecosmetics.us, luxe.com, luxe-cosmetics.com, luxe-cosmetics.uk, luxecosmetics-australia.com and luxecosmeticslashes.com. The UK/AU `body_html` is an empty `<p>`; the US/luxe.com body is empty. Image alt text is empty on every store. I loaded the full HTML of the UK, AU and lashes product pages (both handles) and searched for "ingredient", "aqua", "acrylates", "phenoxyethanol", "CI 77499" and "iron oxide": no ingredient list. The only "ingredient" lines are marketing ("Luxe's ingredients hydrates and strengthens…"; the advertorial's "castor oil and a salad of vitamins"). luxecosmetics.de, luxe-cosmetics.us and luxecosmetics.nl return 404; .ca and .fr don't resolve. eBay itm/397981263430 returned 403 (not retried). Two ingredient web searches returned only Grande's INCI. |

## 2. Ratings

| # | Claim | Verdict | What I saw |
|---|---|---|---|
| 2.1 | Amazon UK 4.0 (73) | **confirmed** (snippet) | "an average rating of 4.0 out of 5 from 73 reviews" (amazon.co.uk listing above). |
| 2.2 | Amazon Canada 3.6 (93) | **confirmed** (snippet) | "3.6 out of 5 star rating from 93 ratings" (amazon.ca/…/B0GSXJCZ93). The same summary says an Amazon.ca *search page* showed CA$20.99 and "3.9 rating from 164 reviews". It is unclear which listing that was; the report doesn't use it. |
| 2.3 | CA waterproof B0G65JT2QJ 2.6 (16), unavailable | **confirmed** (snippet) | "lower 2.6 rating from 16 reviews, and it is currently unavailable". |
| 2.4 | "#489 in Mascara" (with #19,833 in Beauty) | **partly confirmed: rank differs** | I could not reproduce "#489"; an exact-phrase search found nothing. My snippet for B0GSXJCZ93 reads "**#19,833** in Beauty & Personal Care … **#197** in Mascara". The waterproof B0GSXFHPNT shows "#44,354 in Beauty … #356 in Mascara". The Beauty rank matches; the Mascara rank is #197 in my snapshot. Either way the listing is **not #1**, so the report's conclusion ("Amazon's Choice / #1 Best Seller" doesn't hold up) stands. The report should give the rank as "#197–#489 in Mascara depending on snapshot", not "#489". |
| 2.5 | Brand widget: 11,790 reviews, zero 1–3 star, average 4.97 | **confirmed** | Live page HTML (Judge.me "all-reviews" widget): `data-number-of-reviews='11790' data-average-rating='4.97'`; histogram 5★ 11,478 (97%), 4★ 312 (3%), 3★/2★/1★ 0. The JSON reads `"number_of_shop_reviews":0,"number_of_product_reviews":11790`. It is an all-products total, as the report says, not mascara only. The same page also says "4.6/5 (11,000+ reviews)" and "87 verified reviews with 4.93 out of 5 average": **confirmed**. |
| 2.6 | UK widget: 4,636 reviews, 83 one-star | **confirmed** | luxe-cosmetics.uk/products/conditioning-mascara (and the waterproof page): "4636 reviews … 90% (4164) · 8% (375) · 0% (8) · 0% (8) · 2% (83)". The visible reviews include a one-star lash-lift review ("DO NOT BUY! … I had to go to A&E for treatment", Monica A.). The UK mascara pages themselves say "No reviews". |
| 2.7 | 60- vs 90-day guarantee on the same page | **confirmed** | The live US page has "60 day/60-Day" five times and "90 day" once. |

## 3. James Charles

| # | Claim | Verdict | What I saw |
|---|---|---|---|
| 3.1 | Luxe says "James Charles … officially partnered with Luxe" | **confirmed (that Luxe says it)** | https://luxe.com/pages/10-reasons-why-luxe-mascara (Last Updated August 26, 2026): "Officially partnered with Luxe / Even James Charles Is Behind the Korean-Formulated Brand Bringing Lash-Casting to Life / One of beauty's most recognizable names officially partnered with Luxe. Tap to watch James try the brand for himself." The link is `youtube.com/watch?v=Ga1pzxWUtOs&t=628s`. The US product page also shows "James Charles and 11,000+ customers love Luxe". |
| 3.2 | The video shows the Luxe **foundation**, not the mascara; "A nightmare. It's literally a nightmare." then "I like it." | **confirmed** | NexLev `youtube_video_details` Ga1pzxWUtOs: "I Bought Every BEST-SELLING Makeup Product On Amazon!", James Charles, **1,425,567 views**, 18,035 likes, published 2026-08-28. The report's 1,425,543 was a slightly earlier pull. Transcript (NexLev, auto captions; I read every Luxe and mascara mention): 1:57 "…buy the number one bestselling product, and that does happen to be the Luxe Color Changanging Foundation"; 10:34 "This is from the brand Luxe and is a colorchanging foundation. A nightmare. It's literally a nightmare." (said in the context of his dislike of colour-changing products: "Spoiler alert, they are never my favorite"); two tubes both say "light to medium" with "two different shade stickers" on the back; then "I like it. I do like it. It took me a second." The link's t=628s (10:28) lands on this foundation segment. |
| 3.3 | The mascara he used was Essence | **confirmed** | 7:59 "For mascara, we already know which one's the top seller. Essence."; 24:18 "Essence Lash Princess Mascara has made it into one of these challenge videos". |
| 3.4 | No sponsor/partner wording | **confirmed** | My keyword counts over the full 812-segment transcript: "luxe" 3, "mascara" 7, "sponsor" 0, "partner" 0, "gifted" 0, "#ad" 0. "Paid" appears twice, both about prices ("You paid four bucks"). The description has no Luxe mention (only Painted links). He frames the products as bought by him ("I bought the #1 best selling makeup products…"). [reading] Nothing in the video supports "officially partnered" for the mascara. Whether any private deal existed is **unverifiable**. |

## 4. Rival rows, Glaser 2014 and FDA

| # | Claim | Verdict | What I saw |
|---|---|---|---|
| 4.1 | **PrimeLash** $22.40–$28.00, 4.0★, 25.4K–27K reviews, est. 30K units/mo (asinsight "mascara for older women", Jun 2026) | **confirmed** | https://www.asinsight.com/report/US/mascara-for-older-women ("As of June 2026"): B0BG6FXQCC $22.40, 4.0, (25.4K), 30,000 units/mo. https://www.asinsight.com/report/US/mascara (Aug 2026): $28.00, 4.0, (27K), 20,000 units/mo. The thrive-mascara report (Jul 2026): $28.00, 4.0, (25.9K). |
| 4.2 | **Grande GrandeMASCARA**: $25, Myristoyl Pentapeptide-17, own site 4.86 (993), Walmart 4.8 (938) | **confirmed** | https://www.grandecosmetics.com/products/grandemascara(.json): Black/Brown/Waterproof all 25.00; the page lists "Peptides (Myristoyl Pentapeptide-17)" and the INCI ends "…Benzoic Acid, Myristoyl Pentapeptide-17, Sodium Benzoate, Glyoxal"; "Overall rating: 4.855992 / 5 from 993 reviews". The site's own claim rests on "a consumer study with 31 subjects". Walmart 4.8 from 938 (my snippet, walmart.com/ip/646949680 family). |
| 4.3 | **Thrive** Liquid Lash Extensions: $26, 0.38 oz / 10.7 g, castor seed oil, shea, Orchid Stem Cell Complex, "Dermatologist + ophthalmologist tested", Amazon 4.4 (4.4K) [asinsight Aug 2026] | **confirmed, review count varies** | https://thrivecausemetics.com/products/liquid-lash-extensions-mascara: "$26.00", "NET WT. 0.38 oz / 10.7 g", castor seed oil and shea butter, "Orchid Stem Cell Complex™", "Dermatologist + ophthalmologist tested and approved!". asinsight: **4.4 (4.4K)** appears in the *grande-mascara* report (Aug 2026); the *mascara* report (Aug 2026) shows 4.4 (4.6K); thrive-mascara and tubing-mascara (Jul 2026) show 4.4 (4.1K). The figure is real; the report should say which report it came from or give the range 4.1K–4.6K. |
| 4.4 | **Maybelline Sky High** $10.82, 4.5 (187.9K), est. 70K/mo (Aug 2026) | **confirmed** | asinsight "mascara" (Aug 2026): B08H3JPH74, $10.82, 4.5, (187.9K), 70,000 units/mo. |
| 4.5 | **Essence Lash Princess** $4.97, 4.3 (401.1K), 90K/mo, #1 | **confirmed** | asinsight "mascara" (Aug 2026): $4.97, 4.3, 401.1K reviews, 90,000 units/mo, ranked first. |
| 4.6 | **Glaser 2014**: 179 women; lash length 7.98 mm (22–29) → 6.39 mm (50–65); thickness 1.62 → 1.17; darker lashes decrease with age; Dermatol Surg 2014;40(11):1208-13, PMID 25347452 | **confirmed, two caveats** | PubMed efetch PMID 25347452: "upper natural eyelashes of 179 subjects"; "Mean eyelash length ranged from 6.39 (±1.02) to 7.98 (±1.15) mm (subjects aged 50-65 years and 22-29 years, respectively)"; thickness 1.17 to 1.62 (ages 50–65 and **20**–29); "length, thickness, and darkness decreased significantly with increasing age". **Caveat 1:** the report says "**Funded** and co-authored by Allergan". The abstract shows only an Allergan *affiliation* among the authors; no funding statement is in the abstract or the helper's saved file. "Co-authored" is **confirmed**; "funded" is **unverifiable** from what was pulled. **Caveat 2 [reading]:** the abstract's intensity figures (0 = white, 255 = black) run from 118.2 (ages 30–39) to 129.4 (ages 50–65), which on the face of it would be *darker* with age. That clashes with its own conclusion, so the "lighter with age" point is the authors' stated conclusion, not something the quoted numbers show. Better not to lean on "lighter" on camera. |
| 4.7 | FDA: "hypoallergenic" has no federal definition | **confirmed** | https://www.fda.gov/cosmetics/cosmetics-labeling-claims/hypoallergenic-cosmetics (content current as of 02/25/2022): "There are no Federal standards or definitions that govern the use of the term 'hypoallergenic.' The term means whatever a particular company wants it to mean." |
| 4.8 | FDA: discard mascara 2–4 months after purchase; rare blinding infections | **confirmed** | https://www.fda.gov/cosmetics/cosmetic-products/eye-cosmetic-safety (content current as of 06/28/2022): "Manufacturers usually recommend discarding mascara two to four months after purchase."; "…women have been temporarily or permanently blinded by an infection from an eye cosmetic." |

## 5. Comment re-count (2 of the 7 videos)

I pulled the first page of top-sorted comments with NexLev `youtube_video_comments` (sort = top) for:
- **WAR60jvd5jY** "Why I Gave Up Wearing Mascara as a Woman Over 60": 692 comments in total; 20 returned, none by the channel owner.
- **xsQWIs5AWMg** "If your Mascara Smudges: TRY THESE." (Glam Girl Gabi): 131 comments in total; 20 returned, one by the channel owner (excluded), so 19.

These are the same comments the helper listed for these videos; every author they quoted from them is in my pull.

**Quotes (verbatim check):**

| Quote in the report | Verdict | What the comment says |
|---|---|---|
| "I am 69 and just recently decided to ditch masacra. Its a bit scary but I am sick of the mess!" (@loftonrudolph7586, 57 likes) | **confirmed** | Full text begins "So timely! I am 69…". 57 likes, 6 replies. The typo "masacra" is the original. |
| "it made my hooded eyes look smaller and I really couldn't see my eyelashes anymore to apply it and got more on my eyelids than lashes" (@Kim-ek7xy) | **confirmed** | Exact words; 30 likes; she is "almost 70" and stopped wearing mascara. |
| "Tubing mascaras smudge and run down my face from May-December in the heat and humidity of Florida" (@Corrine919) | **confirmed** | Exact words; 4 likes. |
| Also checked: @robiness5344 "I will never give up my mascara.EVER!" 125 likes / 29 replies; @phyllistallent4149 "Bette Davis as Baby Jane look" 57 likes; @juStb4u, @VictoriaBC610, @Ros5477, @donkiml5805, @michelleyork7647, @bethirwin7445 | **confirmed** | All match word for word, with the same like counts where the report gives them. |

**Theme counts, my own hand-coding of these 39 comments** (a comment can count under more than one theme):

| Theme | WAR60jvd5jY | xsQWIs5AWMg | Report's total (all 7 videos) | Consistent? |
|---|---|---|---|---|
| Gave up or is giving up mascara | 7 explicit (lofton, jackielambes, rebeccaholley, Iamlois2, kalo924, Kim-ek7xy, sukapsc), 10 if you count "I don't [like mascara]" (patwagner), "usually skip" (PlantPerson58) and not allowed after an infection (veronicafullford) | 0 | 10, "mostly on the Why I Gave Up video" | **Yes.** On the broad reading all 10 come from this one video, so "mostly" undersells how one-video the theme is. |
| Hard or messy removal | 3 (rebeccaholley "dread removing", patwagner "messy to remove", sukapsc "(and remove)") | 2 (Ros5477 had to scrub; susanmcf1 easy removal as a plus) | 19 | Plausible; can't be reproduced exactly |
| Smudging / transfer / raccoon eyes | 0–1 (lofton's "mess", unclear) | 3 (Corrine919, donkiml5805, queendivaamy; jenniemcwhirter is about eyeliner) | 14 | Plausible |
| Praise for tubing | 0 | 5–6 (karenelizabeth, CarolZone8A, kima229, kimberlygriffin, susanmcf1; Ros5477 likes e.l.f.'s) | 20 | Plausible |
| Complaints about tubing | 0 | 3 (Corrine919 humidity, bethirwin7445 eye drops, Ros5477 warm-water smear), plus VictoriaBC610 if Thrive flaking counts | 9 | Plausible |
| Hooded lids / can't see to apply | 1 (Kim-ek7xy); adriennekushner's 10x mirror is eyesight | 0 | 5 | Plausible |
| Sensitive / dry eyes / drops / infection | 1 (veronicafullford infection) | 3 (susanmcf1, bethirwin7445, donkiml5805) | 8 | Plausible |
| Won't hold a curl / short lashes | 0 | 1 (michelleyork7647) | 7 / 6 | Plausible |
| Waterproof for | 1 (lindap.p.1337) | 0 | 4 | Plausible |
| Off-topic | 5 (gusmonster59 on makeup in general, jkorzechowski, basedwaifu69, lindabohl2454, juliw6435) | 6 (fallmax, jenniemcwhirter3622, cocog458, Patti-1962, salmakhan6498; MusicLover-sb7mo is a product tip) | "about 60" of 159 | 11 of 39 (28%) here vs 38% overall: plausible |

**Verdict on the theme counts: unverifiable as exact numbers, consistent in direction.** The helper's data file holds the quotes but **no per-comment coding sheet**, so the totals (19, 14, 11, 10…) cannot be re-added. Nothing in my two videos contradicts them. Two loose ends:
- The sample sizes in the data file add up to 39+25+20+20+20+20+20 = **164**, while the report says **159 unique**. Owner comments probably explain the gap (I found one on the Gabi video); the file doesn't say.
- The comments' `publishDate` fields are synthetic (every comment on a video carries the identical timestamp, e.g. 2024-10-31T04:47:50Z). They are YouTube's relative "2 years ago" labels turned into dates, so they must not be quoted as real comment dates. The report doesn't quote them.

---

## Summary

**Held up:** the product identity and title; the over-50 tagline; the water-based / pH / warm-water copy; the Water Resistant + Waterproof + warm-water contradiction; every US, UK, AU and lashes-store price; the 2023-12-06 date (Shopify `created_at`); the ingredient list still not found anywhere; Amazon UK 4.0 (73) and CA 3.6 (93); the 11,790-review widget with zero 1–3 star against the UK widget's 83 one-star; the "officially partnered" wording and that the James Charles video covers the foundation (and Essence mascara) with no sponsor wording; the PrimeLash, Grande, Thrive, Sky High and Lash Princess rows; Glaser's 179 women and 7.98→6.39 mm; both FDA quotes; all the comment quotes I checked.

**Needs correcting:**
1. **"#489 in Mascara"**: my snippet shows **#197 in Mascara** (same #19,833 in Beauty). Give it as a range or a dated snapshot. The "not #1" conclusion stands.
2. **Glaser "funded by Allergan"**: only an Allergan co-author is shown; the funding is not shown in what was pulled. Say "co-authored by Allergan staff". Also, the abstract's own darkness numbers seem to point the other way, so don't stress "lighter".
3. **Thrive "4.4K"**: real, but from the *grande-mascara* asinsight report; other reports show 4.1K–4.6K.
4. **Comment theme counts**: no coding sheet is saved, so they can't be re-checked exactly; the 164 vs 159 sample gap is unexplained; the "gave up" theme is essentially one video.

**New since the report (for the author to add if wanted):** the Amazon listing gives the size as 1 fl oz / 29.57 ml (implausible, probably a placeholder); one amazon.ca snippet gives a first-available date of 17 March 2026 (listing unclear); the US product page itself also says "James Charles and 11,000+ customers love Luxe" and twice calls the product "Luxe Waterproof Mascara".
