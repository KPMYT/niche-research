# Round 6 check: thumbnail labels, numbers and the page (2026-10-26)

Checker for RESEARCH-BRIEF.md deliverable 5, done under CLAUDE.md rule 3. I edited no files belonging to anyone else. Row-by-row data: `studies/hvac/data/raw/round6/check-thumbnails-2026-10-26.csv`. No web searches were used.

## 1. Blind re-label of 45 thumbnails

**Sample.** I used Python `random.seed(2631)` and drew 25 rows from `thumbnails/labels-top-winners.csv` (214 rows) and 20 from `thumbnails/labels-channel-top5.csv`. The channel draw came from the 257 rows the channel helper labelled itself. I left out the 28 rows marked "SKIPPED … copied from labels-top-winners.csv".

- One drawn row, `wzAA4dlp_70`, was not blind: I had seen its stored labels in a `head` print before the draw. I dropped it and used the 26th draw from the same seeded sample, `lMhOQM5lcTU`.
- I opened each `img/<id>.jpg` and wrote my labels to a scratch file before I read the stored ones.

**Agreement, field by field (45 rows):**

| Field | Agree | Disagreements |
|---|---|---|
| face yes/no | 45/45 | none |
| person type (real / AI / none) | 43/45 (17/19 of the faces) | `y5kjluBWlEo`, `GfMNLWzaUHU` |
| text word count | 43/45 | `y5kjluBWlEo`, `mUoj_DGsOZY` (see below) |
| text words | 45/45 | none |
| text colours | 44/45 | `0AZw4BlV_3Q` (minor) |
| arrows / circles | 44/45 | `9a-Q5hl_NuQ` (minor) |
| before / after | 44/45 | `pKRWnnDpmb4` |
| red / green marks | 45/45 | none |
| **overall look (real photo vs AI)** | **39/45 (87%)** | 6 rows, all on the real-vs-AI call |
| **style group** | **38/45 (84%)** | 7 rows (40/45 if my second choices count) |

**Every disagreement, quoted:**

1. **`y5kjluBWlEo`** (Secret State Files, "Before Air Conditioning, How Did Americans Survive the Summe…")
   - Stored: person_type "AI", look "AI image (history)", group "AI history scene + red banner", word count "6".
   - Mine: real archival photos, colourised. The portrait looks like Willis Carrier, and the crowd round the ice blocks looks like an early-1900s press photo. Look "realistic photo (archival collage)", group "real face + text".
   - My confidence is medium. If I am right, the "AI history scene + red banner" group drops from 2 to 1.
   - Word count: "BEFORE AIR CONDITIONING HOW DID THEY SURVIVE?" is 7 words, so the stored 6 is wrong.
2. **`GfMNLWzaUHU`** (Craftsman Chris, "Turning a Dumpster AC Into…")
   - Stored: "real person (reading; could be AI)", look "realistic photo + text (face reaction)", group "real face + text".
   - Mine: "AI (unsure)", group "AI persona + bold text".
   - The census (`census-channels-2026-10-26.csv`) has this channel as "on camera" with "same real man in cap (Chris) in all 3". The stored label is probably right and mine wrong.
3. **`JDlPVhleV8A`** (Frugal Folks Garage)
   - Stored: "AI image (reading)", group "AI object/build + bold text".
   - Mine: "realistic photo", group "real build/product photo + text".
   - The census types the channel as faceless. Either reading could be right.
4. **`fclBeOvI7FA`** (Holic Creation)
   - Stored: "AI image (reading)", group "AI object/build, no headline".
   - Mine: "realistic photo (possibly AI, unsure)", group "real build/product photo, no text".
   - The census note for this channel says "AI-looking or staged inventions".
5. **`7RsV7F5eU-s`** (John The HVAC Guy)
   - Stored: "AI image (reading; photo-real)", group "AI object/build + bold text".
   - Mine: "realistic photo", group "real build/product photo + text".
6. **`D3s86GpsnZ4`** (John The HVAC Guy): same split as row 5.
   - Rows 5 and 6 are low-resolution 480x360 images. The census types the channel as "faceless persona" with "same AI middle-aged man". That supports the stored AI reading, but the images themselves do not show it clearly.
7. **`pqucG9p9h74`** (Ray Sutter, "EXCLUSIVE / STOCK UP NOW")
   - Stored: "AI object/build + bold text". Mine: "AI store front + list text".
   - Both say AI. This is only a question of where the boundary between the two groups sits.
8. **`mUoj_DGsOZY`**: the stored word count is "8" because it counts the "92°F" and "68°F" readouts. Mine is 6 without them.
   - The rule is not applied the same way everywhere: `auUvh-k5ja4` leaves out its tape words ("WARNING: THE REAL MATH") and is stored as 6.
9. **`0AZw4BlV_3Q`**: stored colours "white on black; red; black on white". In the image, lines 1 and 3 are black text with a white outline.
10. **`9a-Q5hl_NuQ`**: stored arrows "no". The pipes have small flow arrows drawn on them. Minor.
11. **`pKRWnnDpmb4`**: stored before/after "yes (reading: rusty vs cleaned band on one pipe)". I read "no".

**Where I was wrong, not the helpers.** On recount, my blind word counts were wrong on 6 rows and the stored counts were right: `JZ4vlMZlCj8` 6, `0AZw4BlV_3Q` 9, `7RsV7F5eU-s` 8, `UY80tZeju0o` 11, `pqucG9p9h74` 4, `jSlmEEj2x1A` 6.

**My reading of the pattern:** the labels hold up well on everything except one judgement: whether a photo-like image is real or AI. In 5 of the 6 look disagreements the helper said AI where I said real. The helpers marked most of those calls "(reading)". The 480x360 images make the call hard. An image check cannot settle it; checking each channel's other thumbnails can.

## 2. Number checks

**labels-top-winners.csv: 10 rows match.** The rows came from a second seeded draw (`random.Random(26312)`).

- Views equal `exact.views` in `data/raw/topvideos-exact-2026-10-26.json` on all 10.
- The 4 rows that are in `top-100.csv` also match its views and multiple exactly.
- The 6 recent-winner rows store the multiple rounded to 1 decimal, for example 51.6 against 51.57 in the JSON. The top-100 rows use 2 decimals.

**labels-channel-top5.csv: 10 rows match.**

- Views equal `views_tab` in `census-videos-2026-10-26.csv`.
- The baseline equals `baseline` in `census-channels-2026-10-26.csv`.
- Views divided by baseline gives the stored multiple to 2 decimals. Example: `9lg_OWQ282o`, 419,000 / 930 = 450.54.

## 3. The page (`thumbnails/thumbnail-styles.html`, opened in Chromium through Playwright)

The screenshots are in my scratch folder: `/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/page-desk-full.png` (1280px wide, 46,186px tall) and `/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/page-phone-full.png` (400px wide).

**What works:**

- 755 image tags, 0 broken (each video appears in both a style shelf and its channel row).
- No console errors.
- No page-wide sideways scroll at 1280px or at 400px.
- The header strip reads Thumbnails 471, Top 100 100, Recent winners 120, Channels 57. All four agree with the CSVs.

**Problems:**

1. **One thumbnail is missing.** `tSFizbjaCBo` (Historia Prime, "Connecting Two Metals Purifies ANY Water…", 1.6M) is in `labels-channel-top5.csv` with style group "not labelled yet" and the note "SKIPPED here (in the recent-winners set)".
   - It was never labelled, because `recent-winners.md` dropped it by hand as "water purification, not HVAC".
   - It has no `img/` file and is not on the page, so Historia Prime's channel row shows 4 thumbnails instead of 5.
   - The two CSVs hold 472 unique videos; the page shows 471.
2. **Stray backslashes on 2 cards.** They show `"\"COOLEST\" AC EVER?"` (`hux4BEKiu6k`) and `\"Kickstart\"` (`bpYHcXwu9JA`). The backslashes are in the stored `text_words` field itself.
3. **Garbled "Â·" when the file is opened directly from disk.** It appears in "79 shown Â· median" and in the "channel Â· year" lines, because the file has no `<meta charset>`. When I re-rendered it with `<meta charset="utf-8">` added, it was clean. The published Artifact gets a charset when it is published, so this probably affects only the local file. I did not check the published URL.
4. **At 400px the summary table shows only two columns.** "Style group" and "Thumbnails" fit; median views, top 10, top 25, top 100 and the rest are reachable only by scrolling the table sideways (995px of table in a 350px box), and nothing tells the reader to scroll.
5. **Off-niche content (not broken):**
   - The top card on the first shelf is Silver Cymbal's "How to SOLDER WIRES TOGETHER" (15.0M, channel top 5).
   - Homey Vibe, a faceless tier-A channel, has a row of 5 Bengali beauty-product thumbnails (face wash, hair oil).
   - Both are true to the data. A reader may still ask why they are on an HVAC page.

## 4. Summary table recomputed from the CSVs

I recomputed all 15 groups, not just 3: unique video IDs, with the group taken from `labels-top-winners.csv` where a video is in both files. Every cell of the page's table matches: thumbnails, median views, top 10, top 25, top 100, 12 months, 90 days and channel top 5. The three groups I was asked for:

| Style group | Thumbnails | Top 10 | Top 25 | Top 100 |
|---|---|---|---|---|
| real build/product photo + text | 79 | 2 | 9 | 36 |
| AI persona + bold text (+ red arrow) | 98 | 0 | 0 | 2 |
| AI object/build + bold text | 49 | 0 | 1 | 2 |

Column totals check out: top 100 = 100, 12 months = 89, 90 days = 51 (the CSV `list` field gives 63+20+6 and 31+20). The only CSV row the table does not count is the unlabelled `tSFizbjaCBo`.
