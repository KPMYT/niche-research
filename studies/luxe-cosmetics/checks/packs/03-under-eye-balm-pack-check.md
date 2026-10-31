# Check of pack 3: the under-eye balm explainer and reviews

Files checked:
- `packs/03-under-eye-balm-pack.md` (the explainer)
- `packs/reviews/03-under-eye-balm-reviews.md` (253 reviews)

Checked 2026-10-31 by a second helper, working on its own. Rules from `packs/PACK-BRIEF.md` were kept:
- No bot check or permission refusal was worked around. Amazon and Reddit were not touched.
- **Budget used:** 0 web searches and 0 WebFetch calls.
  - NexLev: 7 comment pulls, 1 video-details call, 1 transcript.
  - PubMed E-utilities: 2 direct loads.
- **Working files** (not in the repo) are in `/tmp/claude-0/-home-user-niche-research/b5781892-4d1f-54af-adb3-1b967b21b5f7/scratchpad/chk/`. They hold `v.py` (the quote matcher), `m.py` and `meta.txt` (the like/date/age comparison), `allabs.txt` and `thick.txt` (abstracts).

Verdicts: **confirmed**, **partly confirmed**, **wrong**, **unverifiable**.

---

## Summary

| Area | Verdict |
|---|---|
| Quote wording (all 253, by script; 25 by hand; 14 re-pulled live) | **Confirmed.** Every quote matches its raw file word for word, once line breaks are evened out. |
| Likes | **Wrong in 11 places.** "0 likes" was written where the raw file had no like count. Re-pulling showed 4 of these are not 0. |
| Dates, ages, product labels | **Confirmed**, with 3 small label points. |
| Theme counts (§2.3) and group counts (§0) | **Confirmed.** All 18 theme totals match the tagging file, and the 3 themes I re-counted by hand come out close. |
| Product table (§2.2) | **Wrong in 2 rows.** 3 eye-cream comments are filed under "RoC under-eye balm stick". |
| Explainer facts (24 checked) | 18 confirmed, 4 partly confirmed, 1 wrong (Bankson "searches" should be "sales"), 1 unverifiable |
| Source notes (§12.1, §12.3) | **Wrong.** They say the files were not saved, but most are in the repo. Two transcripts are saved nowhere. |
| Plain English | About 30 words are used without being explained (list in part 3) |
| Red-flag and extra content | No channel-fit or video ideas. Some brand red-flag material goes past the brief's one-line exceptions (part 4). |

---

## 1. Reviews file

### 1.1 Method

- **All 253 quotes, by script.** `v.py` split each quote at "..." and checked every piece against all the raw files:
  - `data/reviews/eye-balm/*.md`
  - `data/eye-balm/youtube/youtube-comments-2026-10-31.md`
  - the brand page text files
  - the Trustpilot pull
- **Result.** All 246 YouTube quotes, the 7 brand texts and the 1 Trustpilot quote were found. The 15 the script first flagged differed only by line breaks: the raw file writes them as "\n", the pack as "/" or a space.
- **Likes, dates and ages, by script.** `m.py` compared each entry in `reviews-coded-2026-10-31.json` with its raw line.
- **Live re-pulls (NexLev `youtube_video_comments`, top sort, 2026-10-31):**
  - eA_1gxIFJXk
  - cG7_XwI-vUU
  - hVadCZUeLzg
  - G59y1UO5Lgw
  - bQuVtFwFOA0
  - iwyLM5aJ7mE
  - hql6k88BKP8 (the explainer's comments)

### 1.2 The 25-quote sample

"Raw" means checked against the saved file. "Live" means re-pulled from YouTube today.

| # | Who / source | Checked | Wording | Likes, date, age | Product label | Verdict |
|---|---|---|---|---|---|---|
| 2 | @YulieJ2012, eA_1gxIFJXk | live | exact | 0 (" "), ~2026-07-01 | Luxe: yes, names "Luxe" | confirmed |
| 5 | @hollyeubanks4207, cG7_XwI-vUU | live | exact up to the cut; the full comment ends "Thank you for your video!! Wish I had found it sooner😂❤" | 0, ~2026-10-01, 45 | Luxe: yes ("paid $38 for this product") | confirmed |
| 7 | @JAGPabst, cG7_XwI-vUU | live | exact | **2 likes, not 0** | Under a Luxe video, but it thanks the creator and says nothing about the balm | **wrong (likes)** |
| 8 | @lindarusick4402, cG7_XwI-vUU | live | exact | **1 like, not 0** | Under a Luxe video; she cancelled, so she never used it | **wrong (likes)** |
| 12 | @debbiecook3203, hVadCZUeLzg | live | exact. The trailing "2:39 2:39" (timestamps) was dropped without a "..." | 4, ~2026-07-01, edited | Luxe: yes. She thinks hers was "a fake" | confirmed |
| 16 | @LoriJones-o9x, hVadCZUeLzg | live | exact | 1, ~2026-07-01 | Luxe: yes | confirmed |
| 20 | @sadiebernal939, cG7_XwI-vUU | live | exact | **1 like, not 0** | "I just bought it." No review content | **wrong (likes)** |
| 21 | Shari, Trustpilot luxe-cosmetics.com | raw (`data/eye-balm/trustpilot-...txt`) | exact | 1★, Oct 30 2026 | Names "this eye balm" | confirmed |
| 23 | "Margaret T., 56", brand page | raw (luxeresearchlab.com HTML and text) | exact | Purchased Feb 11 2026; 5 filled stars in the HTML | Luxe | confirmed |
| 27 | "Carol A, 63", brand page | raw | exact | Feb 15 2026, 63 | Luxe | confirmed |
| 29 | @jeanie.....5209, HxsOvh5HVzQ | raw | exact | 17, ~2026-08-31 | Medicube | confirmed |
| 55 | @Gina_Love444, TaEBEUMs6js | raw | exact | 1, ~2026-10-17 | Medicube: yes. "Volufiline" appears in medicube.us's own text, so "this" is the Medicube stick | confirmed |
| 61 | @peanut9725, ExYS5rRTxCM | raw | exact | 58, ~2023-10-31, 60 | Kahi | confirmed |
| 81 | @kathleenmartin5264, kih_Rb5JQYs | raw | exact | 4, ~2026-07-31 | Dr.Melaxin ("collagen stick", in a Dr.Melaxin video) | confirmed |
| 94 | @MsSarahP, G59y1UO5Lgw | live | exact | 8, ~2026-03-31 | "RoC under-eye balm stick". The video is a Dr Dray Short. rocskincare.com sells a stick, "Revive + Glow Eye Balm", at $26.99, which fits her "$27" | confirmed |
| 104 | @Fyctiongal, G59y1UO5Lgw | live | exact (there is a line break after "put") | 8, ~2026-03-03, 59 | RoC stick | confirmed |
| 106 | @gailmcgrath, G59y1UO5Lgw | live | exact | 3, ~2026-03-03 | RoC stick | confirmed |
| 115 | @paulinesvisuals, ShE3IVbZRbo | raw | exact | 4.3K, ~2021, 64 | The Ordinary caffeine | confirmed |
| 143 | @shari247peace, si9l1VZtzvQ | raw | exact | 59, eyelid eczema | CeraVe Skin Renewing (plus Avène) | confirmed |
| 166 | @fionafrazer8820, h8ln13JgSCs | raw | exact | 6 | Bobbi Brown / Pixi | Age label **"60+" is a reading.** She writes "one of your older subs" and "might appeal to those 60+", but never states her own age. **Partly confirmed.** |
| 205 | @maxie-q4r, QbvzKn9GG_w | raw | exact | 292, ~2024, 58 | SPF and sunglasses | confirmed |
| 219 | @lynnp6942, bQuVtFwFOA0 | live | exact | 119, ~2026-01-31. "55+" is a fair reading of "around age 55" | Korean skincare vs. surgery | confirmed |
| 221 | @MF-se1zl, bQuVtFwFOA0 | live | exact up to the cut | 58, ~2026-01-31, 63 | blepharoplasty | confirmed |
| 231 | @anarey-oktay2683, iwyLM5aJ7mE | live | exact up to the cuts | 662. The date "not recorded" can now be filled: ~2024-10-31 | caffeine AM / retinol PM | confirmed |
| 235 | @j.a.1239, iwyLM5aJ7mE | live | exact. The rest ("It shocks me how few doctors mention this.!") was cut without a "..." | **18 likes, ~2025-12-01** (written as "not recorded") | retinol warning | confirmed; gap can be filled |

The live re-pull also confirmed these, in wording, likes and dates:
- #1, 3, 4, 6, 9 to 11, 13 to 15, 17
- #95 to 103, 105, 107, 109, 110, 112
- #220, 224 to 227, 229 (#222, #223 and #228 were not in this top-20 pull)
- #230, 232 to 234, 236, 237

The iwyLM5aJ7mE dates the pack marks as missing are all ~2024-10-31.

### 1.3 Likes written as "0" where none were recorded: wrong

The earlier-round raw file (`data/eye-balm/youtube/youtube-comments-2026-10-31.md`) gives **no like counts** for:
- eA_1gxIFJXk and cG7_XwI-vUU (#1 to #8, #20)
- the two kih_Rb5JQYs comments #84 and #85

The reviews file still shows "0 likes" for all 11. That fills a gap with a number (house rule 2).

The live re-pull gives:

| # | Pack says | Live, 2026-10-31 |
|---|---|---|
| 1, 2, 3, 4, 5 | 0 | 0 (blank) |
| 6 @Maureen-d9y | 0 | **1** |
| 7 @JAGPabst | 0 | **2** |
| 8 @lindarusick4402 | 0 | **1** |
| 20 @sadiebernal939 | 0 | **1** |
| 84, 85 | 0 | not re-pulled: write "likes not recorded" |

### 1.4 The product table (§2.2): two rows wrong

In `reviews-coded-2026-10-31.json`, #168 (La Roche-Posay / IT Cosmetics), #171 (Medik8...) and #172 (La Roche-Posay Cicaplast) have the product family "RoC under-eye balm stick". This looks like "Roche" being read as "RoC". Their group letter (D, eye creams) is correct, so §0, §2.3 and §3 are not affected. Only the §2.2 table is.

| Row | Pack | Should be |
|---|---|---|
| RoC under-eye balm stick | 22 quoted, 7 worked, 6 no change, 1 aged 50+ | **19, 4, 6, 1** (#94 to #112) |
| Other eye creams (Hada Labo, Tatcha...) | 26, 16, 2, 7 | **29, 19, 2, 7** |

The column totals stay the same: 253, 84, 32, 28.

### 1.5 Theme re-counts (rough, my own keyword search and reading)

| Theme | Pack | My count | Verdict |
|---|---|---|---|
| Side effects | 30 | 28 by keyword. After reading the differences, about 26 to 31 genuine. | **Confirmed roughly.** The pack counts some borderline ones, such as "#57 safe while pregnant?" and "#206 afraid of new products". My keyword search wrongly caught figurative ones, such as #14 "burned before". |
| Under concealer and makeup | 33 | 33 by keyword (30 shared) | **Confirmed** |
| Price and value | 42 | 43 by keyword (39 shared) | **Confirmed** |

- All 18 theme totals in §2.3 match the tags in the JSON.
- The group split in §0 matches the JSON: 28 Luxe, 84 sticks, 77 eye creams, 64 general, and 28 aged 50+.
- The §0 sub-counts are right:
  - 4 compare it to Vaseline or lip balm (#2, 11, 12, 16)
  - 10 distrust ads
  - 8 are about ordering

### 1.6 Product labels: three wording points

1. **§0 point 1 says "21 independent comments about it".** About 9 of them are from people who bought or used it (#1, 2, 4, 5, 11, 12, 16, 17, 20). The rest react to the review video, for example:
   - #6 to 10 and #13: thanks or "scam"
   - #15: about fakes in general
   - #18: "You have no lines", said to the creator
   - #19: "It makes you stop and think"
   - #21: an ordering complaint

   **Suggested wording:** "21 comments under Luxe review videos and on Trustpilot; 9 of them from people who bought it."
2. **#18, #19 and #20 add nothing a reader can use.** Neither do several rival entries:
   - no tag: #39, #213
   - one-line questions: #60 "Does this actually work"

   The brief asks for "long ones that tell a story". Consider not counting these toward the 253.
3. **The RoC stick (G59y1UO5Lgw).** Name the channel (Dr Dray). The likely product is "Revive + Glow Eye Balm", $26.99 on rocskincare.com (in `data/eye-balm/rivals/rocskincare.com-products-2026-10-31.json`). Keep the "as named in video title" caveat.

---

## 2. Explainer: factual claims

| # | Claim (section) | Source checked | Verdict |
|---|---|---|---|
| 1 | Thinnest facial dermis is the upper inner eyelid, 758.9 µm; lower nasal sidewall 1,969 µm, 2.6× (§0.1, §1.2) | Chopra 2015, PMID 26508650 (abstract fetched today) | **Partly confirmed.** The numbers are right. But the study's thinnest spot is the **upper** medial eyelid, so the headline "**Under-eye** skin is the thinnest skin on the face" is not what it found. Also, §1.2's title says "thinnest skin **on the body**", while the study covered the face only. "Body" comes from Dr Chua's quote, and should be marked as his words. |
| 2 | 320 µm near the lashes, 1,127 µm under the brow (§1.2) | Hwang 2006, PMID 16432408 | **Partly confirmed.** The figures are right, but they are for the **upper** eyelid of 10 Korean cadavers (9 men). The figures are also **whole-skin** thickness, while Chopra's 759 µm is **dermis only**, so "thinner still" compares two different measures. |
| 3 | "Tired eyes" is up to six problems (§0.2) | c6G0kjKQNGw transcript, 1:23 | **Confirmed.** Dr Idriss lists exactly six: pigment, vessels, hollows, temporary puffiness, structural bags, crepey thin skin. Doctorly (74eZe8KsHsw, transcript pulled today) gives **three** causes (shadowing, thin skin, true pigment), so cite Idriss for "six". |
| 4 | After menopause skin collagen, thickness and bone fall 1–2% a year (§5.3) | Brincat 1987, PMID 3120067 (`pack-sources/pm/abs1.txt`) | **Confirmed** |
| 5 | Fall in collagen "preventable" with HRT (§5.3) | PMID 3828252 (fetched today) | **Confirmed.** It was measured in thigh skin; worth saying. |
| 6 | CT: orbital aperture area +91 mm², 96 adults, ~11 years apart (§5.3 point 5) | Sifil & Kahn, PMID 40658792 (`abs2.txt`) | **Partly confirmed.** The figure is right, but it sits under "after 50 and 60". The group's average starting age was 34.7, they were all Caucasian (56 men), and "most changes were most pronounced in participants aged 30 to 50 years". Say so. |
| 7 | MRI: soft tissue 99 / 103 / 131 mm², fat 28 / 31 / 43, 40 people (§5.3 point 3) | Darcy 2008, PMID 18766060 | **Confirmed** |
| 8 | 240 orbits: female orbit expands, eyeball sits further forward (§5.3) | PMID 35749164 | **Confirmed.** This compared ages 20–30 with 60–75. |
| 9 | Adenosine: 126 women aged 45–65, twice a day, smoother at 3 and 8 weeks, L'Oréal (§0.5, §2.3) | Abella 2006, PMID 18489289 | **Partly confirmed.** "An adenosine cream (or film) on one side and a dummy on the other" is not quite right. Each woman got **two of three** products (adenosine cream, adenosine film, dummy), one per side, 84 women per product. Some had no dummy side. |
| 10 | Niacinamide 5%, 50 women, 12 weeks, half-face (§2.3) | Bissett 2005, PMID 16029679 | **Confirmed** |
| 11 | Eye cream with niacinamide, peptides and caffeine smoother at 4 weeks (§2.3) | Kaczvinsky 2009, PMID 19735523 | **Confirmed.** It was compared with no treatment, not a dummy. |
| 12 | HA 0.1%, 76 women, 60 days; only 50 and 130 kDa reduced wrinkle depth (§2.3) | Pavicic 2011, PMID 22052267 | **Confirmed** |
| 13 | Korean study of 100: 35% vascular, 54% mixed (§6.0; myth "89%") | Park 2016, PMID 26346687 | **Confirmed** |
| 14 | Retinoid review: 89 studies, 10,794 people; odds of pain 6.37×, dryness 2.69×, burning 2.44×; non-prescription strengths not linked to more harm (§2.3, §9) | PMID 42708560 | **Confirmed** |
| 15 | Filler meta-analysis: 2,556 people, 91.0% satisfied, swelling 19.2%, bruising 18.4%, blue tint 0.9% (§6.7) | Liu 2024, PMID 37684413 | **Confirmed** |
| 16 | 500-dalton rule, "Larger molecules cannot pass the corneal layer" (§1.4) | PMID 10839713 | **Confirmed** |
| 17 | AAO allergens with ≥10% positives (§2.3, §6.13) | PMID 40119863 | **Confirmed** |
| 18 | Caffeine + vitamin K pad, 11 women, single-blind, 4 weeks (§6.3) | PMID 25625116 | **Confirmed** |
| 19 | Doctors' quotes | Transcripts in `data/eye-balm/pack-sources/tx/`, plus 74eZe8KsHsw pulled today | **Confirmed, 22 of 24 word for word.** Checked: Dr Dray ×5, Dr Sam Ellis ×5, Dr Chua ×2, Dr Rupa Wong ×2, Dr Karam ×3, Dr Idriss ×2, Lisa Eldridge, Wayne Goss, Renée Rouleau, Dr Dray chicken-skin, and Doctorly ×8. **Small change:** Dr Dray a2Hot5ZsYU8 says "probably **is** your best bet"; the pack drops "is". |
| 20 | Bankson: "searches went from a hundred thousand to 12 million" (§1.5 point 1) | `data/eye-balm/youtube/transcript-LmP5MWmL8cs-plain.txt` | **Wrong.** She says "**sales** literally went from about a hundred thousand [balms] to 12 million". Change "searches" to "sales". |
| 21 | Doctor Eye Health (hql6k88BKP8) doctor quotes, e.g. "only temporary as a fix", "the true number one cause" (§6.5, §6.6) | No transcript saved anywhere; not pulled | **Unverifiable.** The six hql6k88BKP8 **comments** the pack quotes were re-pulled and are exact, with right likes: @hartsickdisciple 5.5K, @alanmorris7669 3.3K, @apb38 1.9K, @PigeonsPie1 164, @lindamarie8308 517, @rtbrain 267. @petebailey1652 (95) and @boblossie3192 (56) are also exact. |
| 22 | Rival prices (§1.6, §7.1) | rival JSON and pages in `data/eye-balm/rivals/` | **Confirmed:** Medicube $22 (was $26), 10 g not on its page; Dr.Melaxin $19 for 9 g; d'Alba $21 for 10 g, with "signature aromatic floral citrus fragrance"; Beauty of Joseon $17 for 30 mL; RoC Retinol Correxion $21.99 for 15 mL. **Unverifiable:** Kahi $21–24 (only in the earlier report). |
| 23 | Medicube contains retinol plus geranium, ylang-ylang, bergamot and rose oils (§0.6, §2.3) | medicube.us page | **Confirmed.** Retinol, Pelargonium Graveolens, Cananga Odorata, Bergamot and Rosa Damascena oils are all listed. |
| 24 | Luxe facts: $39.95 / $34.99 (was $39.95) / $34.95; weight 0; the three "lasts" answers; "Cost per month $15"; "back in 2014"; "only anti-wrinkle active"; 2,431-customer survey (§2.1, §2.4) | shop JSON and page text | **Confirmed.** The 44.9% and 20.7% figures are on images and can't be checked as text. |

**Also partly wrong: the launch timing** (§1.5 point 6). The pack says the stick appeared in March to April 2026, with first images on 16 March. The shop data shows something earlier:
- the luxeresearchlab.com listing `luxe-balm` was **created 2025-12-03** and **published 2026-03-02**;
- `luxe-korean-under-eye-balm` was created 2026-03-15.

**Suggested wording:** "first published on the shop on 2 March 2026 (listing created 3 December 2025)".

### 2.1 Source notes that are wrong (§12.1 and §12.3)

- **§12.1** says the transcripts are only in the helper's scratchpad and "not part of the repository". In fact:
  - 21 transcripts are in the repo at `data/eye-balm/pack-sources/tx/`;
  - **74eZe8KsHsw** (Doctorly, dark circles) and **hql6k88BKP8** (Doctor Eye Health) are saved **nowhere**.

  Save those two, and change the path.
- **§12.3** says the new abstracts were "read live and not saved". In fact:
  - most are saved in `data/eye-balm/pack-sources/pm/abs1.txt` and `abs2.txt`;
  - Chopra (26508650), Hwang (16432408), Brincat (3828252) and LactMed (30000867) are not saved.

  Save those four. My copies of the first three are in the scratchpad file `chk/thick.txt`.
- **The hql6k88BKP8 comments** in §6.5, §6.6 and §10 have no saved raw pull. Save the pull.

---

## 3. Plain English

### 3.1 Words used without explanation

**Explainer:**
- Botox: it's not in the glossary, and it is used about 15 times.
- meta-analysis, systematic review, randomised, single-blind, "pooled", "odds"
- kDa (§2.3, HA)
- PMID: used everywhere, never said to mean "the study's number in the US medical library"
- hydroquinone, kojic acid, azelaic acid, tranexamic acid, alpha arbutin (§6.2)
- AHA / AHAs (§3.2, §6.8; §4.3 says "exfoliating acids" but doesn't link the two)
- chemical peel, microneedling, radiofrequency, resurfacing, CO2 laser, pulsed dye laser, nano-fat
- acrylate allergy (§6.6)
- "pigmentary demarcation lines" (§6.2)
- tear film (§6.14), and "goblet cells" in Dr Wong's quote
- esters (§1.4 table), cross-linked (§2.3)
- esthetician / medical esthetician: it's not in the glossary
- Spate (§1.5)
- BOGO (§2.1)
- INCI: used in §0.6 before the glossary explains it
- retinyl palmitate, polyethoxylated retinamide (§1.5)
- LactMed (§2.3)
- eczema and rosacea: they're not in the glossary, and both appear in quotes

**Reviews file** (its glossary in §1 is short):
- Botox, filler, PRP/PRF, syringoma
- hyaluronic acid, niacinamide, centella
- eczema, rosacea, periocular dermatitis
- perimenopause, herniation, retinaldehyde
- T-zone, glass skin, double cleanse
- setting spray/powder, bronzer
- Volufiline, Upneeq, EGCG
- TrustScore
- "derm" (slang for dermatologist)

### 3.2 Brief sections that are thin or missing

| Brief item | What's there | Gap |
|---|---|---|
| Explainer §8: "at least 25 [questions], taken from real comments and searches" | 35 questions | Only Q1 to Q5 name a real comment. Q6 to Q35 give no source. Add the comment or search behind each, or mark it [R]. |
| Explainer §6: for each problem, "how it feels (with real quotes), what people have already tried and why that failed" | Mostly done | The "what people try" part is missing in 6.9 (lines), 6.10 (dryness), 6.12 (milia), 6.14 (dry eye) and 6.15 (loose skin). 6.15 also has no "how it feels" quote. 6.1 uses a clinicians' survey instead of viewers' words. |
| Explainer §2.2: look, feel and smell | Smell and colour "not found" | Acceptable, as nothing was found. |
| Explainer §11: "short" | 5 safety points plus the can't-say paragraph | Fine in spirit, but the brief allows one short line each. |
| Reviews: "prefer long ones that tell a story" | 253 quotes | Many are one-liners. See 1.6 point 2. |
| Reviews: all 9 required themes | All present | No gap. |

---

## 4. Channel fit, video ideas, brand red flags

- **Channel fit, video ideas, titles:** none found in either file. Viewers' own "please make a video on..." requests appear in explainer §10.3 and reviews §3 "Questions". That is fine: they are quotes, not suggestions.
- **Brand red-flag content beyond the allowed one-liners.** These go past "what can't be said" and "safety". Recommend cutting or reducing:
  1. **Explainer §1.5 point 3:** "Dozens of unbranded 'Wrinkle Core Stick' copies sell on eBay and Walmart." This points at an unbranded, mass-made product. It is a sourcing red flag; cut it.
  2. **Explainer §2.1 "Where it is made"** and **Q30** ("names no maker"; "maker and country of manufacture were not found"). This is company-structure material. Keep at most "where it is made: not stated".
  3. **Explainer §2.2 "Packaging detail"** (the back of the stick "totally blank"). Borderline; it duplicates the size row. Could go.
  4. **Explainer §2.4, the right-hand column.** "Likely untrue", "No test report was found", "A customer survey, not a clinical trial", "No study details given". This judges the brand's honesty. Keeping the plain meaning is fine; trim the verdicts to what a viewer needs ("not measured for this product").
  5. **Explainer §7.1, Dr.Melaxin:** "Heavy 'Botox' marketing drew criticism (James Welsh)". This is a rival's red flag; cut it.
  6. **Reviews §0 point 1, §2.1 and §4.2:**
     - Trustpilot TrustScores and star splits
     - "Rated 4.8/5 based on +10,839 Total Ratings" set against "ratingValue 4.81, reviewCount 73"
     - "the review-app slots ... are empty"

     Side by side, these read as a fake-review flag. Keep "no independent reviews could be read" and drop the rest.
  7. **Reviews theme "Buying, shipping and refund problems" (9).** This covers #2's refund saga, #16 "charged for 2 received one", #17 "giving me the run around" and #12 "I got a fake". These are customer-service and authenticity red flags, which the operator said to leave out. Drop the theme, or keep it as one line ("8 Luxe comments are about orders and refunds, not the balm"). Keep only the product parts of the quotes ("glorified Vaseline", "feels like chapstick", "definitely is hydrating").

---

## 5. Exact fixes needed

**Reviews file**
1. Correct the likes:
   - #6 → 1, #7 → 2, #8 → 1, #20 → 1
   - #84 and #85 → "likes not recorded"
2. Fill the gaps the re-pull found:
   - #231 and #230 to #237 dates: ~2024-10-31, except #235
   - #235: 18 likes, ~2025-12-01
3. §2.2 table: RoC row → 19 / 4 / 6 / 1; "Other eye creams" row → 29 / 19 / 2 / 7. In the JSON, set the `fam` of #168, #171 and #172 to "Other eye creams...".
4. §0 point 1: "21 independent comments about it" → "21 comments under Luxe review videos and on Trustpilot; 9 from people who bought it".
5. #166: change the age label to "not stated (calls herself 'one of your older subs')", and drop her from the 50+ count (28 → 27), or mark it [R].
6. Name G59y1UO5Lgw as a Dr Dray Short, and add the likely product (RoC Revive + Glow Eye Balm, $26.99).
7. Add the missing words to the §1 glossary (part 3.1).
8. Cut or reduce the red-flag material (part 4, items 6 and 7).

**Explainer**
1. §0.1 and §1.2: say the thinnest measured skin is the **upper** inner eyelid. Mark "thinnest on the body" as Dr Chua's words. Say Hwang measured whole upper-eyelid skin, not dermis.
2. §1.5 point 1: "searches" → "sales".
3. §1.5 point 6: give the launch as "published on the shop 2 March 2026 (listing created 3 December 2025)".
4. §2.3 adenosine and §0.5: each woman got two of three products (adenosine cream, adenosine film, dummy), one per side.
5. §5.3 point 5: add that the CT group's average starting age was 35, and that most change happened at 30 to 50.
6. §6.12 a2Hot5ZsYU8 quote: "probably is your best bet".
7. §0.2: cite Dr Idriss for the six types; Doctorly gives three.
8. §12.1 and §12.3: correct the save locations. Save the transcripts for 74eZe8KsHsw and hql6k88BKP8, the hql6k88BKP8 comment pull, and the 4 unsaved abstracts.
9. Add Botox, meta-analysis, PMID, AHA, esthetician, eczema and rosacea to the glossary. Explain the other words in part 3.1 where they first appear.
10. §8: give a source, or [R], for Q6 to Q35. Fill "what people tried" in 6.9, 6.10, 6.12, 6.14 and 6.15.
11. Cut red-flag items 1 to 5 in part 4.
