# Check: pack 4, Luxe Eyelash Serum (explainer + reviews)

Checked 2026-10-31 by a checking helper, per CLAUDE.md rule 3 and `packs/PACK-BRIEF.md`.

Files checked:
- `packs/04-eyelash-serum-pack.md` (the explainer, 1,087 lines)
- `packs/reviews/04-eyelash-serum-reviews.md` (the reviews, 339 entries: 85 L-, 96 R-, 158 Y-)

How I checked:
- I parsed every entry in the reviews file with a script.
- I re-parsed all 24 saved Loox pages (`data/reviews/serum/loox-de-8422167118105-p*.html`) myself, from the raw HTML. I did not use the other helper's parsed JSON.
- I re-pulled from the live public feeds: 4 Loox pages, 2 pages of Vegamour's Okendo feed, 2 YouTube comment lists and 1 transcript (NexLev), PubMed abstracts and a PMC full text (NCBI E-utilities), and 4 INCIDecoder pages. All were normal page loads with no workarounds. Nothing was blocked or retried.
- I used 1 web search, for the EU ban status.
- I edited no pack file, changed nothing else and made no commit.

Verdicts: **confirmed** / **wrong** / **unverifiable**, with what I saw.

---

## Summary of the fixes needed

| # | File | Fix | Why |
|---|---|---|---|
| 1 | reviews | Add the Vegamour reviewers' own **Age Range** answers (an Okendo profile field) to the headers, and recount "Women 50+". Of the 41 Vegamour quotes, **11** have a 55-64 or 65+ age range in the raw feed, and **7** of those are neither labelled nor counted as 50+: R-008, R-030, R-034, R-062, R-074, R-101, R-143. Example: R-034 MaryAnn F. is "65+", confirmed live. In the whole raw Vegamour pull, 53 of 150 reviewers say 55+. | The brief asks for the reviewer's stated age. The "27 reviews from people over 50" figure is a floor, not a count. |
| 2 | explainer | §2.2 "Smell: **Not found** in any review", and the "Not found" list in §12, are **wrong**. L-59 (Manuela L., 4★, German Loox): "Es hat keinen Eigengeruch" ("it has no smell of its own"). This review is already quoted in the reviews file. | It contradicts the sister file. |
| 3 | explainer | §2.2, §5.1 and Q21 rest the stinging and burning point on "one of two reviewers". Use the reviews file's numbers instead: of 85 Luxe pieces, 2 mention burning (L-19 Cecilia K., after 3 months, with "very dry eyes in the morning"; L-Y1 Ageless), 1 an allergic reaction (L-21), 1 "didn't tolerate it well" (L-14) and 1 "sticky" lashes (L-29). 5 call it gentle. | The section is thin and understates the data that now exists. |
| 4 | explainer | §1.3 (Medicines row): "A **60+** German viewer lost most lashes after antifungal tablets". @Florence-c1f (Y-157) states no age. She only commented on a video titled "Wimpern ab 60". Also, "Medikamente… einnehmen" means "take medicines", not specifically "tablets". Suggested: "A German viewer, on a video about lashes over 60 (age not stated), lost most lashes after taking medicine for a fungal infection…". | It states an age that the source doesn't give. |
| 5 | explainer | §1.2: "Total life of one lash about 5 to 12 months [R] my sum". S5 states it directly: "Eyelashes also have a shorter life cycle of approximately **4–11 months**". Use the [M] figure. | The source gives a measured figure, so it should replace the guessed sum. |
| 6 | explainer | §1.5: "2007–2008 Latisse approved… earlier report gives 2008, not re-verified". S5 (already saved, `pmc9870835`) says "approved by the US FDA in **2008** for eyelash hypotrichosis". Dr Dray (Y4) does say "in 2007". Suggested: "2008 (S5); Dr Dray says 2007". | The year can now be marked verified. |
| 7 | explainer | §1.4, chemo trial: "46.9% improved on bimatoprost against 18.2%… By 12 months, 61.5% to 67.6%". The figures are right. But "improved" means "responders" on a combined end point (a lash grade **plus** a satisfaction-questionnaire score). And 61.5% and 67.6% are two separate groups: those who stayed on the drug, and those switched from the dummy liquid. Reword both. | The current wording reads as one range. |
| 8 | explainer | §2.3, 1,2-hexanediol: quoted as "can also **help to** boost the antimicrobial activity". The page says "it can also boost the antimicrobial activity of preservatives". Drop "help to" from inside the quote marks. | It is a misquote. |
| 9 | explainer | Prices for The Ordinary ($14.90) are said to be "pulled 2026-10-31". Their source (`04-eyelash-serum.md`) says "Amazon, ASINSIGHT Sep-2026". Give that date. | House rule: say when each figure was pulled. |
| 10 | both | Define the words listed in section 3 below the first time each appears. | The brief requires it. |
| 11 | reviews | L-14 (Kim N.) is counted under "redness, itching or irritation". She wrote "nicht so gut vertragen" ("didn't tolerate it well"), with no redness or itch. Move it to a "didn't tolerate / unspecified" note, or say so in the table. | The label says more than the source. |
| 12 | reviews | Summary point 2 says "46 of 85 worked", but the "It worked" row in table 2.3 says 45. Both are right: 46 = 45 "worked" + 1 (L-T2) counted only as "thicker / less shedding". Add one line explaining this. | Readers will see a mismatch. |
| 13 | reviews | Trim the brand red-flag material (section 4 below). | The brief excludes it. |

Everything else I checked held up. Details follow.

---

## 1. Reviews

### 1.1 The 25 random quotes

Picked with a fixed random seed across sources: 7 German Loox, 4 other Luxe shops, 2 Luxe YouTube, 7 rival brand widgets, 5 YouTube comments. The second part of the table lists 2 more YouTube comments and 1 transcript, re-pulled live, that are quoted in both files. "Live" = re-pulled from the public source on 2026-10-31.

| Code | Source | What I checked | Verdict |
|---|---|---|---|
| L-16 Carola G. | Loox DE p6 | Wording, 1★, refund theme. Translation "doesn't work for me… Klarna… return label" is faithful. **Live: same text, 1★.** | Confirmed |
| L-62 Jasmine G. | Loox DE p21 + full-text file | Wording, 5★. "[cut off on the site]" is true: the single-review page also ends at "…" (`loox-de-review-Qg7Cd5P5fMC`). Translation faithful. **Live: same.** Note: "worked" and "photos" are a fair reading of a cut-off text that only implies success. | Confirmed |
| L-50 Lütfiye D. | Loox DE p17 | "Merke keinen so großen Unterschied…" = "Don't notice such a big difference…". 3★. | Confirmed |
| L-10 Kim F. | Loox DE p4; English from UK Judge.me | German original matches. The English text matches UK Judge.me word for word. 5★ on both. Date 2022-06-12 is from Judge.me. | Confirmed |
| L-64 Louisa E. | Loox DE p22 | Wording, 5★, "erst seit 3 Wochen" → "only 3 weeks", time-to-results 3-5 weeks. Translation faithful. | Confirmed |
| L-03 Anna L. | Loox DE p1; UK Judge.me | German original and English version match. 5★. **Live: same.** | Confirmed |
| L-28 Doris R. | Loox DE p10; Trustoo DE | Wording, 5★. Date 2024-12-18 is the Trustoo `commented_at`. "lidrand" → "lid rim" is fine. **Live: same.** | Confirmed |
| L-T7 Birgül O. | Trustoo DE p1 | "Nach 6 Wochen habe ich das Ergebnis plötzlich gemerkt" = "After 6 weeks I suddenly noticed the result". 5★, 2023-01-07. | Confirmed |
| L-S3 Desiree A. | luxe.com Judge.me | "So far, so good! It's only been a week. Nice brush." 5★, 2024-11-29. | Confirmed |
| L-N1 "W" | Trustoo NL p1 | "Kun je het gebruiken met wimperextensions?" = "Can you use it with lash extensions?". 4★, 2025-03-13, author "W", country NL. | Confirmed |
| L-S1 Shania H. | luxe.com Judge.me | "absolutely love this". 5★, 2024-12-28. | Confirmed |
| L-Y1 Ageless | Transcript 12dTKpvKhyw | Every quoted phrase is in the saved transcript. **Live transcript (NexLev): identical**, including "probably 10 years", "only 5 days… because it burned", "five nights in a row… Didn't start to taper down", "I wouldn't spend my money on this one". | Confirmed |
| L-Y3 Delaney | `data/serum/youtube-pulls-2026-10-31.json` | The only source is the round-1 note "mentions 'currently I'm loving the lash serum from Lux cosmetics'", taken from search-result text. 63,078 views matches. I did not re-pull the transcript. | Confirmed against raw; live unverifiable |
| R-034 MaryAnn F. | Vegamour Okendo p2 | Wording, 3★, title "Neutral?", 2025-06-20, 6 helpful, survey answers all match. **Live (Okendo feed): same.** But her profile says **Age Range "65+"**, and the header gives no age (fix 1). | Confirmed; age missing |
| R-044 Jenna P. | Vegamour Okendo p2 | Wording, 1★, "Nope", 2025-03-12, 9 helpful. **Live: same.** Age range 35-44 (not over 50, so no age problem). | Confirmed |
| R-198 Cindy S. | Babe Essential Yotpo p1 | Wording, 5★, title "Lovely Lashescindy", 2025-12-08, "a woman over 50". | Confirmed |
| R-233 Jennifer C. | Babe Essential Yotpo p2 | Wording, 5★, "Amazing", 2025-04-12. | Confirmed |
| R-462 Laura P. | Babe Renewing Yotpo p4 | Wording, 4★, "Lashes did get longer", 2025-06-14. | Confirmed |
| R-389 Patricia J. | Babe Renewing Yotpo p2 | "I'm 71 years old…", 5★, 3 votes up, 2025-09-28. | Confirmed |
| R-504 Maile | neuLASH Yotpo p1 | Wording, 5★, 1 vote up, 2022-11-02. | Confirmed |
| Y-101 @marystewart5555 | Y2 tiRLNc6_A0E | Text and 334 likes. **Live: 334 likes, "5 years ago".** | Confirmed |
| Y-051 @marinaa.acosta-saucedo686 | batch03, zZQiphx37d0 | Text and 26 likes match raw. | Confirmed (raw) |
| Y-003 @nikkipowell3385 | batch01, BHfB8_Jnb_8 | Text and 13 likes. **Live: 13 likes, same text.** | Confirmed |
| Y-082 @msluvtodraw2 | batch05, 5s86NGOVsQ0 | Text and 0 likes match. The label "generic Latisse (bimatoprost)" is the helper's reading. The video's tags (live) include "Latisse", "Careprost" and "Bimatoprost", which supports it. | Confirmed; the label is a reading, so mark it [R] |
| Y-013 @fionacai3786 | batch01, 9ehrWmpxQZQ | Text and 4 likes match. | Confirmed (raw) |
| Also live: Y-002 @marshagonzales9510 | BHfB8_Jnb_8 | "I'm 71!!", 12 likes. **Live: same.** | Confirmed |
| Also live: @isie. (51), @carynnoah1961 (128), @jazzogbonnie (295), @PanDeSal.28 (all Y2, quoted in the explainer) | tiRLNc6_A0E | **Live: text and likes all match.** | Confirmed |
| Also: Elke L. (L-17) | Loox DE p6 + full-text file | 5★. "ich bin 68Jahre und werde oft gefragt ob ich künstliche Wimpern habe". Translation faithful ("Schwung" → "curl" is fair). **Live: same.** | Confirmed |

**Result:** 25 of 25 quotes are correct in wording, stars or likes, date and product. 14 were re-pulled live: 7 Loox, 2 Okendo, 4 YouTube comments, 1 transcript. One problem: the age is left out where Okendo shows it (R-034, see fix 1).

**Translations:** I checked 16 German and Dutch translations: L-16, L-50, L-62, L-64, L-28, L-T7, L-N1, L-17, L-19, L-21, L-25, L-29, L-59, Y-155, Y-157 and Y-158. All are faithful. The only slip is in the explainer's own paraphrase of Y-157 ("tablets", and an age not stated: fix 4).

### 1.2 The Luxe tallies

| Claim | What I found | Verdict |
|---|---|---|
| 85 Luxe pieces in total | My parse gives 85 L- entries: 67 Loox DE, 7 Trustoo DE, 3 NL, 1 UK-only (Taylor M.), 3 luxe.com, 4 YouTube. | Confirmed |
| German Loox: 4.0 from 67, with 13 one-star | Raw HTML header `data-dist="13,1,2,11,40"`, "67 Bewertungen", "Average rating: 4.0". My own parse of all 24 pages gives 67 unique review IDs: 40×5, 11×4, 2×3, 1×2, 13×1, mean 3.96. **Live re-pull of p1 shows the same distribution and total.** All 67 star ratings in the pack match the raw data. | Confirmed |
| 46 worked | 45 entries are tagged "worked", plus L-T2, tagged only "thicker / less shedding" = 46. The table row says 45 (fix 12). | Confirmed, but explain the 45 vs 46 |
| 12 nothing happened | Exactly 12 tagged "no result": L-14, 15, 16, 18, 19, 20, 22, 23, 24, 29, 35, 50. I checked 5 against raw (L-16, L-19, L-29, L-35, L-50). | Confirmed |
| Elke L., 68 | Raw and live both match. She is the only Luxe entry tagged 50+. | Confirmed |
| "When they give a time, usually 3-5 weeks (11 of 13)" | 11 × 3-5 weeks, 1 × ≤2 weeks, 1 × 6-12 weeks = 13. | Confirmed |
| Trustoo DE 4.72 / 64 (46 five, 18 four) | Saved DE product-page HTML: `"rating":"4.72","total_reviews":64,…star4":18,"total_star5":46`. | Confirmed |
| Trustoo NL 4.61 / 46 (34, 10, 2 one-star) | Saved NL HTML has the same figures. | Confirmed |
| UK Judge.me "25 entries (13 different reviews)" | Parsed file: 25 rows, 13 distinct authors. 12 of them are the cross-posted German reviews plus Taylor M. | Confirmed |
| luxe.com "5.0 from 6 (3 have text)" | 6 rows, 3 with text, 3 blank duplicates. | Confirmed |
| All theme counts in table 2.3, Luxe column | My script recount matches every Luxe cell: ease 11, short praise 11, ordering 10, others noticed 9, too early 7, extensions 5, thicker 5, price 5, gentle 5, burning 2, and 1 each for allergy, redness, dry eye, after stopping and 50+. | Confirmed |

### 1.3 Two themes re-counted roughly

1. **"Women who say they are 50+, menopausal or older" (27).** A keyword sweep of all 339 entries ("I'm 6x", "over 50/60", "menopaus", "older", "senior", ages 50-89) found 17 hits not tagged 50+. Almost all are false hits on **video titles** (for example "Over 50! My Favorite Serums"), so the hand tagging of the text is sound. The real gap is the Okendo **Age Range** field: 7 more quoted Vegamour reviewers are 55-64 or 65+ (fix 1). **Verdict:** 27 is too low. It should be at least 34, plus any 45-54 reviewers the writer chooses to include.
2. **"Afraid of side effects, or asking which serum is safe" (37).** A keyword sweep (scared, afraid, terrified, nervous, hesitant, "safe", "which one") found 20 hits, 14 of them already tagged. The other 23 tagged entries are fair readings of distrust ("not going to trust any kind of lash serum", "decided my lashes were ok as is"). 4 rival-site reviews say "I was afraid / terrified / hesitant… then it worked" and are not tagged: R-018, R-265, R-421, R-523. **Verdict:** roughly right. With those 4 it would be about 41. Not an error, but worth one line.

---

## 2. Explainer: 15 factual claims checked against their cited sources

| # | Claim (section) | Source checked | Verdict |
|---|---|---|---|
| 1 | Upper lid 90-160 lashes in 5-6 rows; lower 75-80 in 3-4 rows; rows "so that eyelashes can be shed without leaving unprotected gaps" (1.1) | S5 full text, saved | Confirmed, word for word |
| 2 | Anagen 4-10 weeks; catagen about 15 days; telogen 4-9 months; 0.12-0.14 mm a day; scalp anagen 2-8 years; "limited by the short anagen phase" (1.2) | S5 | Confirmed. But S5 also gives a lash life cycle of "approximately 4–11 months", which the explainer replaces with its own sum of "5 to 12" (fix 5) |
| 3 | Glaser 2014: 179 women; length 7.98 mm (22-29) against 6.39 mm (50-65); thickness 1.62 (20-29) against 1.17 (50-65); the darkness figures contradict the abstract's own conclusion; one Allergan author (1.3, 5.4) | PubMed 25347452, **re-pulled live** | Confirmed. The darkness point is right: intensity is 129.4 at 50-65 against 118.2 at 30-39, where 255 = black, so older women's lashes measured darker, yet the conclusion says darkness fell |
| 4 | Demodex in Warsaw: 1,499 patients; 8% (1-25), 36%, 50%, 67%, 77% (over 70); suspected cases, not a random sample (1.3, 5.4) | PMC5868666, **re-pulled live** (Medical University of Warsaw) | Confirmed. The abstract's wording "(8% of infected subjects)" is ambiguous, but the methods say "percentage of infected patients, broken down into age subgroups", which supports the explainer's reading |
| 5 | Latisse trial: 278 adults; at least 1 grade better at weeks 4/8/12/16/20 = 15/50/69/78/79% against 8/15/20/18/21%; at week 16, +25% length, +106% fullness, +18% darkness against 2/12/3% (1.4) | S7, saved label | Confirmed, all figures |
| 6 | Chemo trial: 130 people; 46.9% against 18.2% at 6 months; 61.5% and 67.6% at 12 months; redness 16.7%; punctate keratitis 9.4%; Allergan co-authors (1.4) | PubMed 26060513, **re-pulled live** | Numbers confirmed. Wording needs a fix (fix 7) |
| 7 | Alopecia universalis: 41 people, once daily for a year, "slight, moderate, or complete eyelash growth in about 70.3%"; brow trial of 357 people (1.4) | S5 | Confirmed |
| 8 | Latisse label quotes: "Additional applications… will not increase"; "return to its pre-treatment level"; "likely to be permanent"; elderly sentence (8.5); lenses back in after 15 minutes; 3 mL box comes with 70 applicators, so about 35 nights (1.4, 2.1) | S7 | Confirmed ("3 mL in a 5 mL bottle with 70 applicators") |
| 9 | "About 60 nights per tube" / "60 applications" (2.1, 3.2) | S2 "60 applications"; S3 "approximately 60 applications (2 months of daily use)"; S2 also "lasts for 1-2 months" | Confirmed as the brand's figure. The [R] "6 tubes, about $78 a year" follows from it. Not independently measured |
| 10 | Ingredient list (10 items, in order) and the brand quotes "do not contain preservatives… shelf life of 4 months", "2 times a day for the first 2 months", "once a day for 12 weeks", "70% more length", "Zero side effects", "including cancer patients", rosemary and magnolia advertised but not listed (2.3, 2.5) | S2, S3 saved text | Confirmed, word for word |
| 11 | Ingredients, 4 of 10. **Glycerin:** "super common, safe, effective and cheap molecule used for more than 50 years", "protects against irritation, helps to restore barrier". **Biotin:** "When you do not take it as a supplement its effects are a bit more questionable". **1,2-hexanediol:** antimicrobial booster. **Octyl hydroxamic (caprylhydroxamic) acid:** chelating; "preservative free preservative system" | INCIDecoder (now inkeedecoder.com), **re-pulled live** | Glycerin, biotin and caprylhydroxamic acid confirmed (the chemical name "Octanamide, N-Hydroxy-" confirms it is the same thing as "octyl hydroxamic acid"). 1,2-hexanediol has a small misquote (fix 8). The S15 saved file covers only the peptides, so the explainer's "read by this helper" pages were not saved: [R] save them |
| 12 | EU: the SCCS found none of the three "can be considered safe… for promoting the growth of eyelashes and eyebrows" (Feb 2026); a ban was sent to the Council on 22 Sep 2026; **not yet law** on 2026-10-31 (1.4, 1.5) | Saved SCCS page (adopted 2 Feb, published 10 Feb 2026); earlier check's Council document; 1 web search on 2026-10-31 (results: CIRS https://www.cirs-group.com/en/cosmetics/eu-cosmetics-regulation-updated-involving-annexes-ii-iii-and-v ; Council https://data.consilium.europa.eu/doc/document/ST-13462-2026-ADD-1/en/pdf ; Critical Catalyst https://criticalcatalyst.com/?p=10506) | Confirmed. No Official Journal publication found; adoption is still described as "expected Q4 2026" |
| 13 | Doctors' quotes, against `data/transcripts/`. Y1 Rupa Wong: "tremendous growth", "doesn't matter what lash serum you use", "excellent conditioner". Y2 Sam Ellis: "you don't get new hair follicles", "not a matter of if", "wiggle room", "four to six weeks… reversal". Y4 Dray: "theoretical possibility but I'm not aware of any cases", "older age". Y6 Dray: "rarely… longer than 12 mm", "4 to 10 weeks", "0.12". Y7 Dray: "4 to 10 months" slip, "conditioning those hairs". Y10: "five to seven days", "permanent dry eye". Y12: "couldn't find a single study", "about three months", "60 to 90 days". Y17: "baseline". Y18: "probably doesn't do too much". Y8: "same exact side effects" | Saved transcripts (9ehrWmpxQZQ, tiRLNc6_A0E, pwgJzhK_uo0, sQqlbHpfBzw, MC4gZn2xjWc, hd4RszTi-3Q, SsPZ0HYV6JI, cGIkskWfMuI, i45uolSjJLc, ugIVUGBgxoA) | All confirmed. The note that Dray says "months" in Y7 but "weeks" in Y6 is right. Y1 biotin: the captions say "myotin"; the explainer's "[biotin]" bracket is a fair correction |
| 14 | Amazon: $13.00, typical price $15.99 (90-day median), Subscribe & Save $11.70 / $11.05, 4.0 stars, 495 ratings, "1K+ bought", Amazon's Choice (2.1) | `data/amazon-B0C21JM5PY-2026-10-31.txt` | Confirmed |
| 15 | Latisse approved "2007–2008… 2008 not re-verified" (1.5) | S5: "approved by the US FDA in 2008"; Y4 Dray: "in 2007 we had Latisse" | Each source is quoted correctly, but 2008 is now verified in S5 (fix 6) |

Also spot-checked and confirmed: the thyroid "lateral third of the eyebrow" and "Severe hypothyroidism… eyelash alopecia" quotes (S5); the S6 quote "Identifying the underlying condition… is the mainstay of the correct management"; the chemo figures "approximately 1 week to 1 month" and "permanent in approximately 5%" (S5); and "Younger patients may regrow hair sooner" (S5).

**Unverifiable from saved files:** the S10 wind-tunnel, S12 biotin, S13 FDA biotin, S14 ginseng, S19-S22 and S24-S25 figures. All are search snippets, and the explainer already marks them as snippets. Also the dry-eye "about 7% of US women over 50" (S21 snippet). These were not re-checked, to stay inside the search budget.

---

## 3. Plain English: words used without an explanation

The reader has never worn makeup. These appear without a plain explanation where they are first used:

**Explainer**
- §1.1: "tear film" (the thin layer of tears over the eye).
- §1.3, extensions row: "allergic blepharitis", "keratoconjunctivitis" (inflamed eyelid edges / inflamed eye surface from an allergy).
- §1.3: "estrogen" (the main female hormone); "eczema" (dry, itchy, inflamed skin); "taxanes, doxorubicin and cyclophosphamide" (say "common chemotherapy drugs"); "prednisone" is explained, so this one is fine.
- "dermatologist": used from §1.1 onward and never defined (skin doctor). Add it to the glossary next to ophthalmologist and optometrist.
- "lash curler": §1.3 and later (a small clamp that bends lashes upward). Add it to the glossary.
- §1.4: "FDA" (the US government body that approves drugs).
- §1.4 PAP row: "lid crease" (the fold in the upper eyelid).
- §1.4 macular edema row: "retina" (the light-sensing layer at the back of the eye), "cataract surgery" (an operation to replace a cloudy lens in the eye) and "lens capsule".
- §1.4 / §2.3: "INCIDecoder" (a free website that explains cosmetic ingredients).
- §2.3: "paraben" (a common type of preservative); "glycols" in the octyl hydroxamic acid row.
- §2.3: "GHK-Cu", "AHK-Cu": say "copper-carrying peptides".
- §2.1: "Subscribe & Save" (Amazon's repeat-delivery discount). Minor.

**Reviews file**
- "Careprost" (summary point 7): explained only at Y-074, far below. Define it at first use: "an Indian-made generic of Latisse's drug, bimatoprost".
- "castor oil" (table 2.1, line 29): never explained (a thick plant oil people paint on lashes).
- "blepharitis" and "stye" (table 2.3): not defined in this file. The explainer defines them, but the files are read separately until joined.
- "Loox, Trustoo, Judge.me, Okendo, Yotpo": these are review-box app names. One line would help: "the review apps the shops use".
- Inside quotes (leave as quoted, but gloss once): "falsies" (false lashes), "HG" (holy grail = favourite ever), "concealer" (skin-coloured makeup that hides marks), "lash tech" (the person who applies extensions), "Klarna" (a pay-later service).

**Brief sections that are missing or thin**
- Explainer §2.2 (looks, feels, smells): thin, and partly wrong (fixes 2 and 3). The reviews file has texture notes it could use: "sticky" (L-29), "no smell" (L-59), "easy, like eyeliner" (L-59, L-Y2).
- Explainer §5 ("by… skin… type"): skin type is covered only as "very sensitive eyes or skin". Add a line on oily or dry lids and darker skin (irritation can leave darker marks, which Q6 already says).
- Explainer §6.13-6.17: these lack the brief's "why it happens" and "what people tried and why it failed" lines (6.13, 6.14 and 6.15 have only "how it feels" and "does Luxe help").
- Reviews: the brief's "before-and-after stories" theme exists only merged into "Other people noticed, or before-and-after photos" (13). Thin, but true to the data (Amazon photos are unreachable). Say so.

---

## 4. Channel-fit, video-idea and brand red-flag content beyond the allowed one-liners

**Explainer**
- No channel fit, video ideas or titles found. Section 11 ("can't say on camera") is allowed.
- §1.5 lists the view counts of the most-watched doctor videos ("539,359 views… 401,543"). It reads as channel research. [R] Keep it only if it explains "why people are buying now". Otherwise drop the numbers.
- §2.4 "the operator should photograph the box's ingredient list before repeating 'prostaglandin-free'". This is close to an on-camera instruction. Acceptable under the "can't say" exception, but it belongs in §11.
- §2.5's "Evidence found" column ("No study cited. Not found", "no certificate found") and §2.3's "the marketing names two ingredients the list leaves out… either the list is incomplete or the marketing is wrong" are brand-credibility points. They support §11's "can't say" list, so they are borderline. [R] Fold them into §11 as one line: "No published study backs the 4-week / 70% / clinically-proven claims."

**Reviews file** (the brief says leave out the brand's red flags, such as fake reviews, copied content and company issues)
- §2.5: "The two German boxes show the same product with very different star mixes; the Loox box is the one that includes the complaints." This hints that the Trustoo box is filtered. **Remove it.**
- §2.1 notes: "12 of the German reviews also appear on the UK shop in English and on the Dutch shop in Dutch, with the same names", together with the identical "2022-06-12" date on every one. As a de-duplication note it is fine. The repeated "(date shown on another Luxe review box for the same review)" on each header is neutral. [R] Keep the de-dup line, but don't comment on it.
- Summary point 3 and the theme "Ordering, delivery or refund problems (not the formula)" (10), with quotes such as "Total rip-off", "it is actually a fraud" (L-14), "IT'S A SCAM… HAVEN'T RECEIVED ANYTHING" (L-Y4) and the long refund saga of Jasmin H. (L-20): these are customer-service red flags, not product feedback. [R] Keep the count in one line and cut the refund-only quotes (L-08's DHL note, L-16, L-20, L-25, L-31, L-Y4), or move them to a short "not about the serum" list without the full text.
- L-Y2 "(Amazon affiliate link in the description)" and the explainer's Y19 "(Amazon affiliate)": a fair one-word disclosure. Fine.

---

## 5. What held up

- All 25 sampled quotes: wording, stars or likes, dates, product labels. 14 of them confirmed live.
- Every German and Dutch translation I checked.
- Every Luxe tally (85; 45 + 1 worked; 12 nothing; German Loox 4.0 from 67 with 13 one-star; Elke L., 68; the Trustoo and Judge.me figures). The full Luxe column of the theme table.
- The explainer's core science: lash counts, the growth cycle, Glaser 2014, the Demodex age gradient, every Latisse trial figure, 70.3% in alopecia, the chemo numbers, the label quotes, the 70 applicators.
- The brand's own claims and ingredient list, quoted correctly.
- The EU status (not yet law on 2026-10-31).
- All 20+ doctors' quotes, against the saved transcripts.

## 6. Sources used by this check (all pulled 2026-10-31)

- Loox DE widget, live: https://loox.io/widget/nunhYUdVC2/reviews/8422167118105?total=67&language=de&page=1 (also page=6, 10, 21).
- Vegamour Okendo, live: https://api.okendo.io/v1/stores/9e65baea-5deb-4e8a-ac91-a1200eb60a01/products/shopify-6555775169/reviews?limit=25&orderBy=date%20desc (and its next page).
- NexLev `youtube_video_comments` for tiRLNc6_A0E and BHfB8_Jnb_8 (sort: top); `get_video_transcript` for 12dTKpvKhyw; `youtube_video_details` for 5s86NGOVsQ0.
- PubMed efetch for 25347452 and 26060513: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=25347452,26060513&rettype=abstract&retmode=text
- PMC efetch for 5868666: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5868666&retmode=xml
- INCIDecoder: https://incidecoder.com/ingredients/glycerin , /biotin , /1-2-hexanediol , /caprylhydroxamic-acid (all redirect to inkeedecoder.com).
- 1 web search: "EU regulation prostaglandin analogues cosmetics Annex II adopted Official Journal 2026".
- Saved raw files in `data/reviews/serum/`, `data/serum/` and `data/transcripts/`, as named above.
