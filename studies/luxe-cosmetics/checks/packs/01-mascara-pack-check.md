# Check: pack 1, mascara (explainer + reviews)

Checked 2026-10-31 by a checking helper (house rule 3). Files checked:
- `packs/01-mascara-pack.md` (the explainer, 998 lines)
- `packs/reviews/01-mascara-reviews.md` (the reviews, 278 entries)
- against the raw files in `data/reviews/mascara/` and `data/mascara/`, and against live re-pulls made today.

How I worked: no bot check was touched. Live re-pulls used only the public feeds the product pages load (Judge.me `reviews_for_widget`, Yotpo `api-cdn.yotpo.com/v1/widget/…/reviews.json`), NexLev `youtube_video_comments` / `youtube_video_details`, PubMed `efetch`, and one normal page load of Beauty Independent. **Web searches used: 0.** My scripts and live pulls sit in the session scratchpad, not in the repo.

Verdict words: **confirmed** = I saw it in the source. **wrong** = the source says something else. **unverifiable** = I could not see the source.

---

## Summary

**What held up**
- All 278 quotes match their raw files word for word (a script compared every one; 0 differences). The reviews file's section 5 matches the coded JSON exactly (text, date, stars), and every theme list in section 4 matches the JSON codes.
- The total (278) and every by-source number (80 / 70 / 58 / 43 / 12 / 9 / 6) and by-product number are right.
- 25 random quotes checked against raw: 25 match. **23 re-pulled live**: wording, stars or likes, dates and age boxes all match, with the small exceptions listed in part 1.
- Star tables for Thrive, Grande, Tarte, Blinc and the Luxe 77×5★ / 6×4★ split re-pulled live: all match. Age table checked for Thrive, Tarte and Grande: matches.
- Explainer: 15 of 15 sampled facts confirmed in substance (lash biology, Glaser, Fukami, the serum trial, both ingredient lists, the FDA lines, makeup artists' how-to quotes, rival prices). Three need small wording fixes.

**What needs fixing** (exact fixes in part 5)
1. Theme P6 (hooded lids, hands, eyesight) is over-counted: **11 claimed, about 6 real**.
2. Four explainer quotes write an age as if it were likes ("@teddyroon, 66"). Two FAQ questions are pinned to comments that say something else.
3. Two Luxe-page reviews mention a **brown / "black-brown"** shade, but the explainer says "Black only. No brown found."
4. The reviews summary (item 3) is a fake-review red flag, which the operator asked to leave out. The explainer has five lines of video ideas or on-camera advice, and four lines that are brand red flags.
5. 53 reused YouTube comments have no date and 23 have no likes. The brief requires both, and NexLev gives them free.
6. The explainer says its raw transcripts were saved "to the session scratchpad only". In fact 19 of 20 are in the repo. Several explainer comment quotes (the Y9c, Y17c and Y21c pulls) have **no raw file** in the repo.

---

## 1. Reviews

### 1a. Total and by-source counts [M]

| Claim | Verdict | What I saw |
|---|---|---|
| 278 in total, numbered #1–#278 | **confirmed** | `selected-reviews-coded-2026-10-31.json`: 278 records, n = 1…278, no gaps; section 5 of the .md has 278 entries. |
| By source: Luxe Judge.me 80, YouTube new 70, YouTube round-1 58, Thrive 43, Blinc 12, Grande 9, Tarte 6 | **confirmed** | Counted from the JSON `source` field: exactly these numbers. |
| Luxe 80 = 78 (US waterproof listing, with text) + 1 (US conditioning) + 1 (AU conditioning) | **confirmed** | Live Judge.me pull: US waterproof listing 83 reviews (30 + 30 + 23 over three pages), 78 with text, 5 with only an invisible mark (`‎`). US conditioning: 2 reviews, the second has no text. AU conditioning: the same review twice. |
| By product (Luxe 80, Thrive 62, Category 46, Sky High 18 …) | **confirmed** | JSON `family` counts match table 2b exactly. |
| Luxe stars 77×5★, 6×4★; "only 1 of the 80 marked verified" | **confirmed** | Live: 77/6. Of the 80 used, only #80 (AU) is verified. (The 5 verified US ones are the 5 with no text.) |
| Thrive 50,508 reviews, 4.46, 39,366/3,329/2,544/2,138/3,131 | **confirmed** | Live Yotpo bottomline: total 50,508, average 4.4584, the same distribution. |
| Grande 993, 4.86; Tarte 2,630, 4.60; Blinc 317, 4.68 (with star splits) | **confirmed** | Live Yotpo: 993/4.856, 2,630/4.601, 317/4.675; star splits identical. |
| Grande 61 incentivised; Tarte 158 of 500 | **confirmed** | Raw files: 61 and 158. |
| Age table (Thrive 5★: 34/81/158/272/423/32; 1★: 8/32/48/72/100/40; Tarte; Grande) | **confirmed** | Raw counts match for Thrive 5★, Thrive 1★, Tarte (24+57 / 109 / 115 / 122 / 57 / 16) and Grande (295+113 / 104 / 94 / 130 / 111 / 146). |
| "Amazon star averages … search snippets taken in round 1 (date of capture unknown)" | **confirmed** | `data/mascara/websearch-snippets-2026-10-31.md` header: "Snippet capture dates are unknown". |

### 1b. 25 random quotes (seed 20261031; 7 Luxe, 6 rival shops, 6 new YouTube, 6 round-1 YouTube)

"Raw" = matched against the raw file. "Live" = matched against today's re-pull.

| # | Product label | Source | Raw | Live | Notes |
|---|---|---|---|---|---|
| 6 | Luxe | Judge.me US WP | ✓ | ✓ text, 5★, 2026-02-08 | |
| 10 | Luxe | Judge.me US WP | ✓ | ✓ 5★, 2026-01-29 | |
| 27 | Luxe | Judge.me US WP | ✓ | ✓ 5★, 2025-12-16 | |
| 31 | Luxe | Judge.me US WP | ✓ | ✓ 5★, 2025-12-06 | |
| 40 | Luxe | Judge.me US WP | ✓ | ✓ 4★, 2025-11-13 | |
| 49 | Luxe | Judge.me US WP | ✓ | ✓ 4★, 2025-10-21 | |
| 66 | Luxe | Judge.me US WP | ✓ | ✓ 4★, 2025-09-09 | |
| 85 | Thrive | Yotpo 5★ | ✓ | ✓ 5★, 2026-10-21, 65+, verified | |
| 94 | Thrive | Yotpo 5★ | ✓ | ✓ 5★, 2026-10-24, 55-64 | |
| 101 | Thrive | Yotpo 5★ | ✓ | ✓ 5★, 2026-10-14, 65+ | |
| 109 | Thrive | Yotpo 1★ | ✓ | ✓ 1★, 2026-05-10, 55-64 | |
| 112 | Thrive | Yotpo 1★ | ✓ | ✓ 1★, 2026-04-01, 55-64 | **Wrongly coded P6** (no hooded / hands / sight content) |
| 141 | Blinc | Yotpo | ✓ | ✓ 3★, 2021-07-11 | |
| 161 | Thrive | YT tXlNLaq0y6Q @jennyblankenship1419 | ✓ | ✓ 29 likes, "8 years ago" | |
| 174 | Several brands | YT 33Bqpi6h37Y @suzihazlove4979 | ✓ | ✓ 3 likes, "2 years ago" | |
| 180 | Sky Tubes | YT P52cMKaQmII @barbaragrelik6746 | ✓ | ✓ 1 like, "2 days ago" | |
| 185 | Sky Tubes | YT P52cMKaQmII @lostribe5130 | ✓ | not on page 1 | unverifiable live; matches raw |
| 211 | Several brands | YT 6IPLVHE19F0 @Itsmemommio | ✓ | ✓ 5 likes, "2 years ago" | |
| 219 | Several brands | YT IJ2u4Zl4Drw @MusicLover-sb7mo | ✓ | not re-pulled | matches raw |
| 244 | Other brands | YT K72lJWqP_Co @nedamm5677 | ✓ | ✓ 18 likes | Live is "Never tried **Clinque** as their products used to irritate my eyes". The quote silently corrects the spelling to "Clinique", so it is not word for word. Date missing: live says "4 months ago". |
| 245 | Category | YT K72lJWqP_Co @theasullivan4227 | ✓ | ✓ 17 likes | date missing (live "4 months ago") |
| 263 | Other brands | YT mALJZ4f8lCc @Rachierooh | ✓ | ✓ text | File says "likes not recorded". Live: **2 likes, "4 months ago"**. Quote stops before "I hate it. Waste of money" with no "…". |
| 270 | Category | YT WAR60jvd5jY @phyllistallent4149 | ✓ | ✓ 57 likes | date missing (live "2 years ago") |
| 272 | Category | YT WAR60jvd5jY @jackielambes7208 | ✓ | ✓ 39 likes | date missing (live "2 years ago") |
| 276 | Category | YT WAR60jvd5jY @adriennekushner1968 | ✓ | ✓ 42 likes | date missing; quote stops before "It is a game changer for me." with no "…" |

Extra live checks outside the sample: #79 and #80 (Luxe conditioning US/AU) ✓; #183 @juliebridge7590 (5 likes, 2 months) ✓; #197 @freden9234 (140, 1 year) ✓; #200 @jenniezarna1959 (166, 2 years) ✓; #249 @teddyroon ✓ text. Live shows **0 likes and "4 months ago"**, and the quote stops before "if no foundation, just moisturiser. Any suggestions ?" with no "…".

**Result:** 25/25 match raw; 23 re-pulled live (9 Judge.me, 6 Yotpo, 10 YouTube incl. extras = more than the 8 asked). No wording, star, date or age errors in the shop reviews. The YouTube round-1 entries have small faults: missing dates and likes, two unmarked cuts and one silent spelling fix.

### 1c. Three themes re-counted

| Theme | Claimed | My count | Verdict |
|---|---|---|---|
| P1 Smudging / staying put | 85 (Luxe 39, rivals 38, category 8) | 84 by my own keyword list; 81 overlap. Theirs adds #80, #182, #183, #254; mine adds #81, #91, #117 | **confirmed** (about 85) |
| P6 Hooded lids, shaky hands, poor eyesight | 11 | Real ones: #35, #53, #57, #66, #273, #276 (6), plus #121 ("puffy eyelids", borderline). **False hits:** #112, #150, #171, #191 have no such content. #94 (riding glasses) and #55 ("hide behind my glasses") are borderline. | **wrong**: about 6–7, not 11 |
| T6 Side effects caused by the product | 5 (#113, #118, #120, #142, #228) | Read every review with itch/burn/swell/irritate/break words: these 5 are right; no missed ones | **confirmed** |
| (bonus) T12 Gave up mascara | 15 | 13 clear; #83 ("going bare as usual") and #226 (switched to extensions) are borderline | **roughly confirmed** |

The summary's "8. … Side effects … are rare in this sample (5)" holds. Summary items 2 and 9 lean on P6 ("skinny wand … shaky hands", "hooded lids"); their wording still holds with 6.

---

## 2. Explainer: 15 factual claims

| # | Claim (section) | Verdict | What the source says |
|---|---|---|---|
| 1 | Upper lid 90–160 lashes in 5–6 rows; lower 75–80 in 3–4 (1.2) | **confirmed** | Aumond & Bitton 2018 (`pack-sources/aumond.txt`): exactly so. |
| 2 | 0.12–0.14 mm a day; growing phase 4–10 weeks; full cycle 4–11 months; rarely over 12 mm (1.2) | **confirmed** | Aumond: "daily growth rate … 0.12–0.14 mm", "four to ten weeks", "four to eleven months", "rarely exceeds 12 mm". |
| 3 | Optimal lash length one-third of eye width; "halved dust landing on the eye and slowed tear drying" (1.2) | **confirmed, wording loose** | Aumond: "reduced tear evaporation and deposition of particles on lashes by half". It was a model-eye/animal study, and the source says "on lashes", not "on the eye". |
| 4 | Glaser 2014: 179 women; 7.98 mm (22–29) → 6.39 mm (50–65); thickness 1.62 → 1.17; an Allergan co-author; darkness numbers contradict "lighter" (1.2) | **confirmed** | PubMed 25347452: all figures exact; Allergan is among the affiliations (the abstract doesn't say which author, so "one co-author" is a reading). Intensity 118.2 (30–39) → 129.4 (50–65), on a scale where 255 = black, so older lashes measured darker. The pack's caution is right. |
| 5 | Fukami 2014: 36 Japanese women aged 20–70; more mascara = more cracking and porosity; curler no significant effect (1.2, 3.2, 9) | **confirmed** | PubMed 25423741 (pulled live): exactly so. The abstract is not saved in the repo; only Aumond's citation of it is. |
| 6 | Serum trial: 30 women, no comparison group, maker's staff, +8.3% length at 12 weeks (2.3) | **confirmed** | PubMed 38572527: "open-label", 30 women aged 25–65, authors from "Medical Affairs Department, Cantabria Labs", +8.3% at 12 weeks. |
| 7 | Lens study: 0.9–7.1% mascara left after an hour's soak (Problem 7) | **confirmed** | PubMed 40066296: 3.1 / 6.0 / 7.1 / 0.9%, "one-hour soak in saline". It was a lab test on lenses, not on eyes. |
| 8 | Thrive ingredient list, 26 items in that order; $26; 10.7 g; "water-resistant" (2.3A) | **confirmed** | `competitors/thrivecausemetics…txt` line 1015 (black shade): the same 26 in the same order; "$26"; "NET WT. 0.38 oz / 10.7 g"; "water resistant formula". |
| 9 | Grande list, 31 items; $25; "Made in Italy"; "water resistant"; "soap & water"; beeswax/carnauba quote; 31-subject consumer study, 97% (2.3B) | **confirmed** | `competitors/grandecosmetics…txt`: list identical (31), all quotes present word for word. |
| 10 | Chemist (Y8): acrylate copolymer "makes tubing mascaras tube"; waterproof "anhydrous"; "oil loves oil"; "borrowed from hairspray"; one product turned to "mush" (1.3, 1.5, 2.3A) | **confirmed** | `mascara-tx/X4WoL8hdaXw.txt`: all present. |
| 11 | FDA: discard mascara 2–4 months after purchase; never apply in a moving vehicle; "Even a slight scratch…"; "If neither the package nor the display rack…"; no saliva or water; don't share (S9) | **confirmed** | `science/fda-eye-cosmetic-safety-2026-10-31.txt`: all word for word; "Content current as of 06/28/2022". |
| 12 | FDA: "hypoallergenic" has no legal definition (S10) | **confirmed** | FDA page: "There are no Federal standards or definitions that govern the use of the term 'hypoallergenic.'" |
| 13 | How-to steps: Dominique "little wiggle and then pull"; Mindful Midlife "don't pump it… rummage it around", primer "30 seconds", "looking down"; Aran P "pushes air in there"; "looking up my nose"; Nina Ubhi "let it sit a few seconds"; Glow Audit "curl… before… never after it dries"; Michelle Spieler "hollow spaghetti", "one coat only", "hollowed out" (3.2) | **confirmed** | All found word for word in `mascara-tx/` (jDRz2xUsHpg, 0-DGxAoMB2A, mpQJfwfJ6a8, mALJZ4f8lCc, K72lJWqP_Co, oDqUrZhtqsU). Two notes: Spieler's "one coat only" is said about **Blinc** specifically, and her "micellar water" is auto-captioned "solar water". |
| 14 | Rival prices: Essence Lash Princess $4.97 (4.3★, 401.1K); Sky High $10.82 (4.5★, 187.9K); PrimeLash $22.40 (4.0★, 25.4K); Tarte $28 (4.4★, 4K); Lash Paradise $13.99 (sections 5.4 and 7.1) | **confirmed** | `asinsight-mascara-2026-10-31.txt`, `asinsight-mascara-for-older-women…`, `asinsight-tubing-mascara…` ("As of July 2026"); L'Oréal page `$13.99`. |
| 15 | Beauty Independent (6 Feb 2026): $6.4bn in 2022; tubing $1.42bn in 2024; Google +35.2%; +9.1% Oct 2024–Sep 2025; 51% "confusion"; Sephora $14–$34 (1.4) | **confirmed, attribution loose** | Live page: all figures present. But "data from Spate and Quilt AI" is only half right: the $6.4bn is from **Allied Market Research** and the $1.42bn from **Market Intelo**. Spate gives the search figures; Quilt AI gives the 51%. |

Also spot-checked and confirmed: the Luxe page prices ($39.95 / $59.95 / $54.95 / $69.95, "BUY 1, GET 1 FREE"); the tagline; "Water Resistant" + "Waterproof (showers, pools, workouts)" + "Warm water dissolves it cleanly"; "four to six weeks"; "Heals your lashes"; Amazon UK £14.99 / 4.0★ (73) in the snippet file; Dr Dray's "about three months", nickel, "stab your eye", the 25-year case and baby shampoo; Dr Rupa's "send me a product in the mail", "a thousand times", biphasic/"lash loss… wrinkles", and prostaglandins in some mascaras (caption: "isopropyl proprestinate"); Face Value's "start wearing mascara again" and "gave up on lower lashes"; Cassi Short f4uAyWYG5dQ: 1,102 views, 18 Oct 2026 (NexLev details today).

**Small explainer faults found while checking**
- Glossary, "Prostaglandin": "can darken the iris" is not in the cited Y15. Dr Rupa cites redness and stinging. Source it (pack 4) or mark it [R].
- 1.2: "Curl is stronger … in white people than in East Asians". Aumond says "Caucasians as compared to Asians".
- 2.1 / 5.2 / Problem 12: "Black only. No brown found." But Luxe-page reviews **#37** ("i got the brown and it is so pretty", 2025-11-21) and **#68** ("this black-brown color is perfect", 2025-09-05) mention a brown shade. The shop lists Black only, so say both.
- Header line "Everything was pulled on 2026-10-31": the Amazon snippet figures have **unknown capture dates** (snippet file header). Say so next to S4.
- Section 12, last line: "Raw transcripts of Y1–Y20 were saved to the session scratchpad only (not to the repo)" is **wrong**. 19 transcripts are in `data/mascara/pack-sources/mascara-tx/`, committed in b67dd41. Y20 (f4uAyWYG5dQ) is missing; NexLev says that video has no captions.
- Comment quotes with **no raw file in the repo**: everything marked Y9c, Y17c and Y21c, plus @Pamela-B, @lorainemcgillivray77, @meowwaffles6040, @SwampSagacity1014, @DreamJeanneee1111, @LisaIsHappyToBeSane, @granjmy, @Madilyn-sh5pd, @NaamaRonen and @apatheticowl3461. Live I confirmed @Pamela-B (7 likes), @HurshRoad, @errrkt, @coltdaggabuzzbuzzify, @lorainemcgillivray77 (2 likes), @meowwaffles6040, @SwampSagacity1014 and @granjmy (82 likes) word for word. @DreamJeanneee1111, @LisaIsHappyToBeSane and the three Y21 handles are not on page 1: **unverifiable** today. Save these pulls to `data/mascara/` so the figures have a source.

**Quote attributions that are wrong**
- **Age written as if it were likes.** The pack's own format is "(@handle, N likes)" or "(@handle, N)", so these read as like counts:
  - Problem 2, "(@teddyroon, 66)": live has **0 likes**; "66" is her age ("Im 66").
  - Problem 12, "(@lindap.p.1337, 77)": live has **30 likes**; 77 is her age.
  - Section 10, "(@MmeO, 67)": the raw file has **11 likes**; 67 is her age.
  - Section 10, "(@jamiebrennan5779, 64)": the raw file has **76 likes**; 64 is her age.
- **Q15, "Will a curler pull my lashes out?" (@SwampSagacity1014).** Her comment says curlers "can make the mascara smudging problem worse … They can also make your eyelashes look shorter". It does not ask about pulling lashes out.
- **Q21, "Does it work for hooded eyes?" (@meowwaffles6040).** Her comment is about **deep-set** eyes ("because of how deep set they are").

---

## 3. Plain English: words used without being explained

**Explainer** (the reader "has never worn makeup")
- Make-up basics in 4.1 and routine B: **foundation, concealer, tinted moisturiser, blush, eyeshadow, eyeliner, brows, loose powder, eyeshadow primer**. None is explained, and Routine B depends on them.
- Eye and face words: **crease, brow bone, moving lid, deep-set (eyes), cornea, iris, cataract, artificial tears, lid wipes**.
- Science words: **keratin** (2.3B), **cuticle** (implied in 1.2), **pH** (only "(pH)" in 2.3A), **isododecane** (named, not plainly explained), **FDA** (never spelt out), **ASIN** (never explained), **Shopify feed** (in 2.1, 2.3).
- Cultural references the reader may not know: **"Baby Jane" / Bette Davis, "Tammy Faye"**.
- Names used as if known: **Spate, Quilt AI, asinsight** (asinsight is explained in 7.1 but used earlier in 5.4), **Latisse / bimatoprost** (half explained).
- Comment words quoted without a gloss: **fallout** (mascara bits falling), **cluster lashes**.

**Reviews file** (its glossary covers 13 words)
- Used in the summary or headings without explanation: **drugstore** (item 10), **verified buyer**, **review widget / Judge.me / Yotpo** (say "the review box on the shop page"), **lash extensions** (in quotes and table 2b), **incentivised** (it is explained in 2c, but item 3 uses "verified" first), **eye makeup remover / micellar / oil-based remover** (in quotes).
- Inside quotes: **LLE** (= Thrive Liquid Lash Extensions, #82), **carmine** (a red dye made from insects, #176), **EWG** (a US ingredient-rating site), **spoolie**. A one-line "words inside the quotes" table would cover them.

## 4. Brief sections missing or thin

**Explainer.** All 12 sections are there, and section 8 has 32 questions (25 needed). Thin spots:
- **Section 6, "what people have already tried and why that failed"**: missing for Problems 6, 7, 9, 10, 11, 12, 13, 14 and 15.
- **Section 6, "why it happens"**: missing for Problems 12, 13, 14 and 15.
- Problems 12–15 are only 2–3 lines each.
- **2.2 Smell and feel**: "not found" is correct, but the reviews file has texture words in theme T3 (77 reviews, 18 Luxe) that the explainer does not use.
- **5.1 By age**: there is no row under 20 (minor).

**Reviews.** Every theme the brief names is present, and 278 is well over 150. Thin spots:
- **"Prefer long ones that tell a story"**: none of the 80 Luxe reviews is over 300 characters (average 162). That is the source's limit, not the helper's, but say so.
- **Date**: missing for 53 entries and likes missing for 23 (all round-1 reuse). NexLev returns both free; today's live pull gave them for every one I checked.
- **Amazon review text in search snippets**: the brief lists it, the file says only star averages were taken, and the explainer quotes one such PrimeLash snippet. So it exists and was not collected.
- **Ulta, Target, Walmart, Cult Beauty, Trustpilot**: "not tried this round (time)".
- **PrimeLash**: only 2 entries.
- **Luxe's shop-wide review feeds were not mined.** The UK store's shop-wide Judge.me feed loads normally (`judge.me/reviews/all_reviews_js_based?...shop_domain=luxecosmetics-uk-ireland.myshopify.com`) and holds **4,631** product reviews, including 1–3★ ones. The US shop-wide figure in round 1 was 11,790. Mascara reviews may sit there beyond the per-listing feeds. Worth one pass; I did not page through it.

## 5. Channel fit, video ideas and brand red flags (operator doesn't want them)

The brief allows only two one-line exceptions: what can't be said on camera, and real safety points.

**Reviews file**
- **Summary item 3** (whole item): "only 1 of the 80 is marked 'verified buyer' … 73 of them were posted one to three days apart … almost all in the same lower-case style … Treat them as the brand's own page text, not as checked buyer opinion." This is a fake-review red flag. **Remove it**, or cut it to the neutral label the brief already asks for: "All 80 are from Luxe's own shop pages." The point that 78 of 80 sit on the waterproof listing is fine to keep as a plain fact.
- Per-entry "(not marked verified)" is a plain data field and can stay.

**Explainer: video ideas and on-camera advice**
- 3.3: "[R] Testing Luxe's warm-water removal on camera is the single most useful thing the operator can show." **Delete.**
- Problem 2: "so test a full day on a hooded lid." **Delete those words.**
- Problem 6: "Say so honestly." **Delete.**
- 7.2: "(only after the operator's own test confirms it)." **Delete.**
- Q31: "[R] It can't really be both; test it." Keep "It can't really be both" and drop "test it".
- 2.4 table, "Testable on camera" (row 2). Change to "Visible straight away".

**Explainer: brand red flags**
- 2.2: "Two full-face 'BEFORE / AFTER 2 COATS' photos also change the rest of the makeup (skin, lips, brows)… These images can't be used to judge the mascara". This is an altered-image red flag. **Delete.**
- 2.2: "No ad disclosure was seen." and S12 row Y20: "reads as affiliate". **Delete both.**
- 4.1: "The Luxe-linked creator". Change to "A creator (Cassi, Y20)".
- Section 10 heading "The brand's mirror-language (what the ad copies from them)" and the note "almost the same line opens Glow Audit's video". Change the heading to "The brand's own words" and delete the Glow Audit note.
- 2.4 "Status" column: "No study found" ×2, "Not believable as a measurement", "'Natural' implausible…; cruelty-free uncertified", "No lab or doctor named". The claims list itself is required by the brief, but these verdicts go past the one-line "can't say" exception. Shorten to the drug-claim flag already in section 11, or to "not checked".
- Section 11, "Don't present the brand's 'clinical' numbers … no study was found". This is borderline but sits inside the allowed "can't say" section. Fine if kept to one line.

**No channel-fit or title content** was found in either file.

---

## 6. Exact fixes, in order

1. **Reviews, table 4 and section P6:** recount P6 to about 6. Drop #112, #150, #171 and #191; decide #94, #55 and #121. Fix the P6 counts (All / Luxe / Rivals / Category) and the "All reviews in this theme" list.
2. **Reviews, summary item 3:** remove it (red flag), or cut it to a neutral source line.
3. **Reviews, 53 round-1 YouTube entries:** fill in date labels and likes from NexLev. For example: K72lJWqP_Co entries "4 months ago"; @teddyroon 0 likes; @Rachierooh 2 likes, "4 months ago"; WAR60jvd5jY entries "2 years ago".
4. **Reviews #244, #249, #263, #276:** mark the cuts with "…". Restore "Clinque" in #244, or add "[sic]" to the quote instead.
5. **Explainer, Problem 2, Problem 12 and section 10:** change "(@teddyroon, 66)" to "(@teddyroon, age 66)", "(@lindap.p.1337, 77)" to "(@lindap.p.1337, age 77, 30 likes)", "(@MmeO, 67)" to "(@MmeO, age 67, 11 likes)" and "(@jamiebrennan5779, 64)" to "(@jamiebrennan5779, age 64, 76 likes)".
6. **Explainer Q15 and Q21:** re-source them. Q21 should cite a comment about hooded eyes (e.g. @Kim-ek7xy). Reword Q15, or cite @SwampSagacity1014 for "Can a curler make smudging worse?".
7. **Explainer 2.1, 5.2 and Problem 12:** add "Two reviews on Luxe's own page mention a brown / black-brown shade (#37, #68); the shop lists Black only."
8. **Explainer 1.4:** change the attribution to "Allied Market Research ($6.4bn), Market Intelo ($1.42bn), Spate (search), Quilt AI (51%), via Beauty Independent".
9. **Explainer, glossary "Prostaglandin":** source "darken the iris" (pack 4) or mark it [R]. In 1.2, change "East Asians" to "Asians". In 1.2, change "halved dust landing on the eye" to "halved particles landing on the lashes (model study)".
10. **Explainer, section 12, last line:** replace it with "Transcripts Y1–Y19 are saved in `data/mascara/pack-sources/mascara-tx/`; Y20 has no captions." Save the Y9c, Y17c and Y21c comment pulls (and the other quotes listed in part 2) to a raw file. Note at S4 that Amazon snippet capture dates are unknown.
11. **Explainer:** delete the five video-idea and on-camera lines and the four red-flag lines listed in part 5.
12. **Both files:** explain the words in part 3, or add them to the glossaries. Most needed: the make-up basics in routine B (foundation, concealer, blush, eyeshadow, eyeliner, powder, primer), drugstore, verified buyer and review widget.
13. **Explainer section 6:** add "tried and failed" to Problems 6, 7 and 9–15, and "why" to Problems 12–15. The reviews file already has the quotes: for example T12 for Problem 15, T9 for Problem 12 and #82 for Problem 7.
