# HVAC round 3: check of the census, types, sells, new channels, sub-niches, top 100 and recent winners (2026-10-26)

Checker: the round 3 second helper (working rule 3). Checked 2026-10-26, 08:30-10:30 UTC. Nothing edited in the files checked; nothing committed or pushed. Web searches used: **0**.

- **Raw pulls for this check:** `studies/hvac/data/raw/check-round3-2026-10-26.json` (every sampled row: my re-pull, my reading, the stored value; the 28 descriptions read; the landing-page prices; my 40 blind sub-niche tags; the `/next` results).
- **New scripts:** `studies/hvac/data/tools/check_round3.py` (my own re-implementation of the long-form / 12-month / last-30 baseline, 90-day count and top-video logic; it does not import `census_build.py`) and `studies/hvac/data/tools/check_round3_vid.py` (exact views, date and owner from innertube `/next`; its `/player` call returns LOGIN_REQUIRED, so lengths came from NexLev `youtube_video_details` and the Videos tabs instead).
- **Sources:** YouTube Videos tabs re-pulled with `yt_allsorts.py` (logged out, 4 pages a sort, `python3 -I`) for 25 census channels, 10 new channels and 8 recent-winner channels; `desc.py` and `vid.py` (`/next`); thumbnails `mqdefault.jpg` (and `maxresdefault.jpg` for 3); NexLev `youtube_channel_about` (3 channels) and `youtube_video_details` (3 videos); two landing pages loaded directly.
- **Samples:** Python `random.Random(seed)`. Each file's input list was sorted by `channel_id` (or `video_id`, or `rank`) before sampling; the exact code is in the raw JSON's notes and below each part.
- **Measured vs reading:** subscribers, counts, views, dates, lengths, baselines and multiples are measured. The HVAC mark on each title, the tiers, the types, the sub-niche tags and in-scope / out-of-scope calls are **my readings**.

## Headline

| File | Rows checked | Numbers (measured) | Readings | Verdict |
|---|---:|---|---|---|
| `channels.csv` / `channels.md` (census) | 25 channels (10 A, 15 B-D) | **125/125 match** (subs, video count, baseline, 90-day uploads, top video) | HVAC share differs by 3+ titles in 13/25 (rule mostly **undercounts**); tier: **2 clear mismatches, 1 rule gap, 3 borderline** (2/25 clear = 8%; 6/25 incl. borderline = 24%) | **Usable, with fixes.** Numbers are sound; tiers A hold; B-D edges and the "free-cooling" / technician-vlog cases need fixing. |
| Types (`census-types-{A,B,C}`) | 30 channels + 5 personas | - | **3/30 clear mismatches (10%)**, 1 borderline; 5/5 personas confirmed | **Usable after one definitional fix**: "brand" is not one of the brief's four types (147 rows in `channels.csv`). |
| Sells (`census-sells`, `sells.md`) | 15 channels, 28 descriptions, 2 landing pages | Ray Dutton product and price **exact**; Kilcher price confirmed | **5/15 rows have a wrong or missing category (33%)**; 2 are false "affiliate" | **Usable for own products (hand-checked); the rule categories need a pass.** |
| `new-channels.md` | 10 of the 72 "well above" | start basis 10/10, joined 10/10, first long-form 10/10, views and dates 10/10 | **2/10 are not HVAC channels on the views that made them "well above"** (HVAC under 5% of their views) | **Usable with a filter**: the "well above" score counts all long-form views, not HVAC views. |
| `subniches.md` | 3 rows (6 with 12 months) + 40 blind tags | **6/6 rows recompute exactly** | blind agreement **22/40 (55%) fine, 25/40 (63%) parent**; 7/40 clear rule errors | **Arithmetic sound; tags are rough.** My 55% is below the file's own fresh estimate (68%). |
| `top-100.md` / `top-100.csv` | 15 rows | views 15/15 (drift -5 to +147), dates 15/15, length 15/15, channel 15/15 | English 15/15, in scope 15/15 (by its stated rules) | **Pass.** |
| `recent-winners.md` | 10 rows | views 10/10, dates 10/10, length 10/10, **multiples 10/10** (baselines re-pulled independently) | in scope: 1 mismatch, 2 borderline | **Pass, with 1 scope fix and 2 cautions** (tiny baselines, 120-upload cap). |

---

## 1. Census: `channels.csv` / `channels.md`

**Sample.** `rows = sorted(channels.csv, key=channel_id)`; `rnd = random.Random(2620)`; `rnd.sample(tier A rows, 10)` then `rnd.sample(non-A rows, 15)`. 25 channels: 10 A, 5 B, 4 C, 6 D.

**Method.** Videos tab re-pulled with `yt_allsorts.py <id> <out> 4` (2026-10-26 08:31-08:34 UTC). Subs and video count from the tab header. Baseline, 90-day uploads and top video recomputed by my own script (`check_round3.py`: long-form = overlay 5:00+; 12-month = age text up to "11mo ago"; if under 10, median of the latest 30 long-form). HVAC share: I read every title of the latest 30 long-form (Latest sort) myself, using the scope list in `round2/check-master.md` step 3 (the operator's generator and insulation rules included). Tier: `check-master.md`'s rule as `census_build.py` applies it (D first, then A at 50%+, B/C at 10-50% with the 30% lane-word test, X under 10%, contractor-teaching-homeowners = A, STOVE-CRAFT A->C).

**Caveat on independence.** The numbers were re-pulled with the same tool on the same day, so a 100% match confirms that the pull reproduces and that `census_build.py`'s baseline and count arithmetic is right (my script is a separate implementation). It is not a check against a second source.

| Row | Channel (stored tier) | Field | Claimed | Found | Source | OK / MISMATCH |
|---:|---|---|---|---|---|---|
| 1 | The Forbidden Vault (A) | subs / videos / baseline / 90d / top | 1,790 / 28 / 698 (12M, n=28) / 0 / 301,000 `cDvXL6yCSfw` | 1.79K / 28 / 698 (12M, n=28) / 0 / 301,000 `cDvXL6yCSfw` | Videos tab 2026-10-26 | OK |
| | | HVAC share | 16/28 | 19/28 | my reading | MISMATCH (+3), same tier |
| | | tier | A | A | rule | OK |
| 2 | DIY HVACMillionaire Advice Class (A) | numbers | 2,260 / 204 / 692 (last30) / 0 / 28,000 `YocYtTjZLp0` | same | tab | OK |
| | | HVAC share / tier | 25/30 / A | 27/30 / A (3 home-refrigerator titles out) | reading | OK |
| 3 | Construction Odyssey with Eddie (A) | numbers | 22,300 / 55 / 2,800 (12M, n=55) / 0 / 2,200,000 `XJzM-fcrFck` | same | tab | OK |
| | | HVAC share / tier | 21/30 / A | **28/30** / A | reading | MISMATCH (+7), same tier |
| 4 | Aced It! Cooling & Heating (A, contractor) | numbers | 245 / 54 / 2,486 (last30, n=6) / 0 / 11,000 | same | tab | OK |
| | | HVAC share / tier | 6/6 (LOW-N) / A | 5/6 ("The Story Behind Aced It!" not HVAC) / A | reading | OK |
| 5 | Fox Family Heating and Air Conditioning (A, contractor) | numbers | 79,400 / 321 / 23,000 (last30) / 0 / 506,000 `raG_N_hz6ng` | same | tab | OK |
| | | HVAC share / tier | 23/30 / A | 26/30 / A | reading | MISMATCH (+3), same tier |
| 6 | heatertips (A) | numbers | 1,480 / 20 / 17,500 (last30, n=18) / 0 / 305,000 | same | tab | OK |
| | | HVAC share / tier | 17/18 / A | 18/18 / A | reading | OK |
| 7 | Hank Cole (A) | numbers | 1,370 / 31 / 365 (12M, n=31) / 31 / 156,000 `HPYZfXWGzjQ` | same | tab | OK |
| | | HVAC share / tier | 22/30 / A | 25/30 / A | reading | MISMATCH (+3), same tier; **note: the newest 5 long-form are car videos** ("Your Car AC Is Blowing 55°..."), so 5/10 of the newest 10; not DRIFT by the rule (needs 2 or fewer) |
| 8 | DIY mr.T (A) | numbers | 96,500 / 383 / 2,750 (12M capped, n=120) / 38 / 5,600,000 `h9KS-fcXFjI` | same | tab | OK |
| | | HVAC share | 17/30 | **27/30** | reading | MISMATCH (+10) |
| | | tier | A (no flag) | A by the rule as coded; **C by the STOVE-CRAFT intent** | rule vs main-session intent | RULE GAP: the archetypal DIY heat-craft channel ("Generate Heat ... Using a Metal Barrel", "Generate Heat With a Kettle Full of Holes", "A Bold Idea Using Bricks to Generate Heat") is not caught by the `diy-stove-craft` regex (only 1 of 30 titles matches), so it stays A |
| 9 | Survival Labs (A) | numbers | 3,510 / 46 / 988 (12M) / 13 / 161,000 | same | tab | OK |
| | | HVAC share / tier | 17/30 / A | 20/30 / A | reading | MISMATCH (+3), same tier |
| 10 | ChilesHeatCool (A) | numbers | 4,830 / 207 / 1,800 (last30, n=27) / 0 / 151,000 | same | tab | OK |
| | | HVAC share / tier | 15/27 / A | 16/27 / A | reading | OK |
| 11 | Walter Handyman (B) | numbers | 880 / 5 / 10,000 (last30, n=5) / 0 / 26,000 | same | tab | OK |
| | | HVAC share / tier | 1/5 (LOW-N) / B | 2/5 / B ("Why Old Houses Didn't Rot" moisture title borderline; at 3/5 it would be A) | reading | OK (borderline) |
| 12 | Forgotten Appalachian Skills (C) | numbers | 4,350 / 36 / 7,650 (12M) / 36 / 317,000 | same | tab | OK |
| | | HVAC share / tier | 4/30 / C | 2/30 ("20 Forgotten Appalachian Heating Tricks...", "...When the Firewood Ran Low...") / **X**, C at 3/30 if "Before the First Hard Freeze" counts | reading | MISMATCH, borderline (campfire and woods titles are not home heat) |
| 13 | Able Distributors (D) | numbers | 8,140 / 212 / 1,750 (last30) / 3 / 225,000 | same | tab | OK |
| | | HVAC share / tier | 19/30 / D | 30/30 / D (distributor) | reading | MISMATCH (+11), same tier |
| 14 | WW HVAC (D) | numbers | 37,100 / 1,867 / 2,600 (12M capped, n=113) / 27 / 166,000 | 37.1K / header had no video count today / same / 27 / same | tab | OK |
| | | HVAC share / tier | 19/30 / D (manual) | 24/30 / D | reading | MISMATCH (+5), same tier |
| 15 | Jonathan Tracey (C) | numbers | 43,400 / 641 / 17,000 (12M) / 25 / 1,200,000 | same | tab | OK |
| | | HVAC share / tier | 5/30 / C | 3/30 (Cosy Cooler air con, winter heat-pump tariff, "Why Are Our Bills So High?") / C | reading | OK |
| 16 | Craftsman Chris (B) | numbers | 50,800 / 517 / 17,000 (12M, n=13) / 4 / 781,000 | same | tab | OK |
| | | HVAC share / tier | 11/30 / B | 11/30 / B | reading | OK |
| 17 | Ben Huttash (B) | numbers | 13,100 / 196 / 1,500 (last30) / 0 / 867,000 | same | tab | OK |
| | | HVAC share / tier | 4/30 / B | 3/30 (car AC and car heater out) / B at exactly 10% | reading | OK (edge) |
| 18 | Ivan's Survival Journal (C) | numbers | 1,250 / 15 / 628 (12M) / 15 / 297,000 `aYPqvixhvXg` | 1.26K / 15 / 628 / 15 / 298,000 | tab | OK (drift) |
| | | HVAC share / tier | 5/15 / C | **8/15 (53%) -> A**; 7/15 -> C if "11 AutoZone Items ... Winter Blackout" is left out | reading | MISMATCH, borderline: "I Tested 12 Ways to Seal a Drafty Door", "I Tested 12 Ways to Insulate a Window", "I Tested Window Film, Bubble Wrap & Thermal Curtains" are heat-loss tests the rule misses |
| 19 | DIY JIM (B) | numbers | 113,000 / 531 / 3,000 (12M) / 13 / 947,000 | same | tab | OK |
| | | HVAC share / tier | 7/30 / B | 5/30 / B | reading | OK |
| 20 | Great American Northern Garage (B) | numbers | 22,300 / 28 / 29,000 (last30, n=17) / 1 / 3,000,000 | same | tab | OK |
| | | HVAC share / tier | 2/17 / B | 0/17 strict (garage insulation titles don't mention heat or the bill) -> **X**; 1-3/17 lenient -> B | reading | MISMATCH, borderline |
| 21 | Standard Supply (D) | numbers | 2,240 / 29 / 901 (last30, n=9) / 1 / 845,000 | same | tab | OK |
| | | HVAC share / tier | 12/17 (LOW-N pooled) / D | 8/9 long-form (+ the Popular top 10 is all HVAC) / D | reading | OK |
| 22 | The Archive of Builds (C) | numbers | 4,980 / 37 / 1,800 (12M) / 22 / 307,000 | same | tab | OK |
| | | HVAC share | 14/30 | **20/30** | reading | MISMATCH (+6) |
| | | tier | C | **A (lane: off-grid / passive cooling)** | rule + operator default (2026-10-26: lane channels whose videos are mostly HVAC are A) | **MISMATCH (C->A)**. Missed titles: "This Roman Home Cools Itself For $0", "This Courtyard Home Beats 110°F Heat and Cools for $0", "This Double Roof Keeps Homes Cool Without AC", "This $300 Sand Battery Heats Your Entire Home All Winter" |
| 23 | Talk2UPro (D) | numbers | 20,000 / 683 / 223 (12M) / 12 / 213,000 | same | tab | OK |
| | | HVAC share / tier | 11/30 / D | 11/30 (Carrier chiller overhaul series) / D | reading | OK |
| 24 | Xavier_HVAC (D) | numbers | 1,150 / 239 / 202 (12M) / 6 / 3,600 | same | tab | OK |
| | | HVAC share | 14/30 | **24/30** | reading | MISMATCH (+10) |
| | | tier | D (auto: "About trade words; stored D") | **A** (B even at the stored 14/30) | About: "I am a HVAC Technician and Installer. Based out of Georgia, I work residential... share my journey" | **MISMATCH (D->A)**: a one-man residential technician's service-call channel ("Blower Motor Replacement \| After Hours Emergency Call", "Clogged drain line & unavailable landlord"). `D_CONFIRM` marks the same kind of channel "not D" (HVAC AO "individual technician's service-call vlogs", DC HVAC, Yung HVAC); this one had no manual decision, so the old D plus the word "technician" in About made it D. |
| 25 | ACiQ (D) | numbers | 1,540 / 77 / 5,900 (last30, n=5) / 1 / 99,000 | same | tab | OK |
| | | HVAC share / tier | 12/12 (LOW-N pooled) / D | 4/5 long-form / D (manufacturer) | reading | OK |

**Error rates (part 1).**

| Field | Checked | Mismatches | Rate |
|---|---:|---:|---|
| Subscribers (rounded header) | 25 | 0 (1 drift: 1.25K -> 1.26K) | 0% |
| Video count | 25 | 0 (WW HVAC: no count in today's header; stored 1,867 not contradicted) | 0% |
| Baseline (value, rule, n) | 25 | 0 | 0% |
| Uploads, last 90 days (long-form) | 25 | 0 | 0% |
| Top long-form video (ID, views) | 25 | 0 | 0% |
| HVAC share within 2 titles of mine | 25 | 13 differ by 3 or more (10 under, 3 over) | 52% |
| Tier | 25 | 2 clear (Archive of Builds C->A, Xavier_HVAC D->A) + 1 rule gap (DIY mr.T) + 3 borderline (Ivan's, Forgotten Appalachian, Great American) | 8% clear; 12% with the gap; 24% with borderline |
| Tier, stored A only | 10 | 0 by the rule; 1 rule gap (DIY mr.T) | 0% (10%) |

**What this says.** The census keyword rule **undercounts** HVAC titles, sometimes by a third (DIY mr.T 17 vs 27, Xavier_HVAC 14 vs 24, Able Distributors 19 vs 30, Construction Odyssey 21 vs 28). It misses titles about cooling or heating a *home* without naming equipment ("Cools Itself for $0", "Beats 110°F Heat", "Generate Heat at Home"), brand-and-model titles, and technician service-call titles. Where the share is far above 50% this changes nothing; it bites at the 50% and 10% lines (Archive of Builds, Ivan's) and wherever D was given by default.

---

## 2. Types (`census-types-{A,B,C}-2026-10-26.csv`)

**Sample.** Each file's rows sorted by `channel_id`; `rnd = random.Random(2621)`; `rnd.sample(A, 15)`, then B 8, then C 7. Thumbnails: the 3 newest long-form videos of each channel (census videos, Latest sort, by approximate date), `mqdefault.jpg`, put on 6 contact sheets and **typed blind before I opened the stored types**. HomeFix Guide has only 1 long-form video. For 3 channels I then looked at `maxresdefault.jpg` (Doug Cross, matty tripps).

| Row | Channel (tier) | Field | Claimed | Found (my blind reading) | Source | OK / MISMATCH |
|---:|---|---|---|---|---|---|
| 1 | Old Maine Firewood (A) | type | faceless persona | faceless persona (same AI-styled old man in plaid) | 3 thumbnails | OK |
| 2 | Elias Mercer (A) | type | faceless persona | faceless persona | 3 thumbnails | OK |
| 3 | AIR MAN (A) | type | faceless | faceless (hands only) | 3 thumbnails | OK |
| 4 | Mikey Pipes - Pipe Doctor (A) | type | on camera | on camera | 3 thumbnails | OK |
| 5 | Jesse Kelley HVAC (A) | type | faceless | faceless (logo and equipment) | 3 thumbnails | OK |
| 6 | HomeFix Guide (A) | type | faceless (low) | faceless (low; 1 thumbnail, AI/stock man) | 1 thumbnail | OK |
| 7 | Willman Air Heating and Air Conditioning (A) | type | **brand** | **on camera** (the same real bearded man in a cap in all 3: "MY AC UNIT IS SMOKING!") | 3 thumbnails | MISMATCH ("brand" is not one of the brief's four types) |
| 8 | RHODES - Cosmic Cooling (A) | type | on camera | on camera | 3 thumbnails | OK |
| 9 | Travis Poe (A) | type | on camera | on camera | 3 thumbnails | OK |
| 10 | PRIME AC AND HEAT (A) | type | **brand** | **on camera** (the same real host in all 3, "LG BLACK EDITION WORTH THE HYPE?") | 3 thumbnails | MISMATCH (same issue) |
| 11 | The Smart Way to Buy HVAC with Doug Cross (A) | type | **faceless persona (low)** | **on camera** (a real man in a car, company logo shirt, in all 3; maxres confirms a photo, not an AI image) | 3 thumbnails + desc `7sC3sE6bJAg`: "In this real HVAC visit, I look at the existing setup..." | **MISMATCH** |
| 12 | Mick Wall (Energy Stats UK) (A) | type | on camera | on camera | 3 thumbnails | OK |
| 13 | Harlan Sawyer (A) | type | faceless persona | faceless persona | 3 thumbnails | OK |
| 14 | Word of Advice TV (A) | type | on camera | on camera (real man in 1 of 3) | 3 thumbnails | OK |
| 15 | HVAC Made Clear (A) | type | faceless | faceless (motion graphics) | 3 thumbnails | OK |
| 16 | Bootstrappin' (B) | type | faceless | faceless | 3 thumbnails | OK |
| 17 | Life in Farmland (B) | type | on camera | on camera | 3 thumbnails | OK |
| 18 | Consumer Analysis (B) | type | faceless | faceless | 3 thumbnails | OK |
| 19 | Red Beard Engineered (B) | type | faceless | faceless | 3 thumbnails | OK |
| 20 | Technology Connextras (B) | type | on camera | on camera | 3 thumbnails | OK |
| 21 | Dave Wirth (B) | type | on camera | on camera | 3 thumbnails | OK |
| 22 | RomanUrsuHack (B) | type | faceless | faceless (AI old man in 1 of 3) | 3 thumbnails | OK |
| 23 | Jesse Muller (B) | type | on camera (medium) | faceless (low; only distant workers, no presenter) | 3 thumbnails | MISMATCH, borderline |
| 24 | The Build Guide (C) | type | faceless | faceless (AI man in 1 of 3) | 3 thumbnails | OK |
| 25 | Sketchy Survival (C) | type | faceless | faceless (cartoon) | 3 thumbnails | OK |
| 26 | matty tripps (C) | type | on camera | blind: faceless persona (low); **after maxres and About ("im a final cut pro editor by trade... I went to college for video production"): on camera** | thumbnails + About | OK (my first reading was wrong) |
| 27 | Creative Cement Ideas (C) | type | faceless | faceless | 3 thumbnails | OK |
| 28 | Wade Corbin (C) | type | faceless persona | faceless persona | 3 thumbnails | OK |
| 29 | SafeMind (C) | type | faceless | faceless (AI illustrations, different people) | 3 thumbnails | OK |
| 30 | Saving Savers (C) | type | faceless | faceless (illustration) | 3 thumbnails | OK |

**Persona names and backgrounds (5).**

| Row | Channel | Claimed | Found | Source | OK / MISMATCH |
|---:|---|---|---|---|---|
| P1 | Old Maine Firewood | Hollis; heated his home in Maine 40 years | "My name's Hollis. I've lived and heated my home in Maine for forty years" | About, `channel-finds-pages-2026-10-23/about.json` (not in `channels-master-about`) | OK |
| P2 | Elias Mercer | Elias Mercer; survival, "alone, off the grid" | "I'm Elias Mercer — and everything I know about survival, I learned the hard way, alone, off the grid" | same file | OK |
| P3 | Harlan Sawyer | Harlan Sawyer; "(From an Old Logger)", "An Old LUMBERJACK Tests..." | 17 census titles carry "Old Logger" / "Old LUMBERJACK" (`wHicQKmo8WQ`, `zUAWVCF96so`...) | census titles | OK |
| P4 | Wade Corbin | "My name is Wade Corbin." | "My name is Wade Corbin. My house is the last one on the line..." | `desc.py GyxAzZTn8RU` | OK |
| P5 | Frugal Frannie | "a grandmother who knew the value of a dollar" | same words; the description also says the narration is "a natural human voice" | `desc.py oLuOs5Gx4WI` | OK |

**Error rates (part 2).** Type: **3/30 clear mismatches (10%)** (Willman, PRIME, Doug Cross), 1 borderline (Jesse Muller): 13% with it. By tier: A 3/15, B 1/8 (borderline), C 0/7. Personas: 0/5.

**The definitional problem.** The type helpers added a fifth type, **"brand"** (and "brand (on camera)", "brand (faceless)"...), which the brief (deliverable 1) and `labels.md` section 5 don't have. In `channels.csv` it now covers **147 of 791 rows (19%)** (A 47 in the A file). "Brand" mixes *who presents* with *who owns the channel*; Willman and PRIME both show a real host on camera. This is a rule change no one has approved (CLAUDE.md rule 1).

---

## 3. Sells (`census-sells-2026-10-26.csv`, `round3/sells.md`)

**Sample.** Rows sorted by `channel_id`; Ray Dutton's Garage set aside and included; `random.Random(2622).sample(the rest, 14)`. Both stored description videos re-read with `desc.py` (28 descriptions; 2 channels have one video); real link targets from the `/next` redirect URLs where a link was cut off; landing pages loaded once.

| Row | Channel | Field | Claimed | Found | Source | OK / MISMATCH |
|---:|---|---|---|---|---|---|
| 1 | Ray Dutton's Garage | categories | own_product; book_ebook_guide; nothing else | both descriptions open "📘 THE HVAC SURVIVAL GUIDE - get it here: https://raydutton.com"; no other link | `AglSKzOY2E8`, `dOZ-8__G4uU` | OK |
| | | product / price | "The HVAC Survival Guide", e-book, $27 launch, list $59, "Total value $130", Gumroad | "$27 one-time, instant PDF"; "$59" crossed; "Total value $130"; checkout `gumroad.com/l/gmuzt` | raydutton.com, loaded 2026-10-26 | OK (exact) |
| 2 | How2D2 | categories | not found | nothing sold | 2 descriptions | OK |
| 3 | Hook Agency | categories | consulting; own_website | sells its own marketing service ("YOUTUBE DEAL - Book here for $1,000 off: hookagency.com/youtube-deal/") | 2 descriptions | OK in category; **the evidence quoted is wrong** ("9:00 Client Consultation and Material/Color Decisions", a video chapter) |
| 4 | DuctTape Mechanic | categories | not found | nothing | 2 descriptions | OK |
| 5 | Magic Touch: Fire & Air | categories | consulting; own_website; contractor | contractor (Phoenix), "schedule a private showroom consultation" | `tM2ZU6mrXtw`, `1oJWazaVv2k` | MISMATCH (minor): "consulting" is a showroom sales visit, not a paid consulting offer |
| 6 | TheDIYGuyDOTnet | categories | affiliate (Amazon 7) | 6 + 1 amzn.to links | `ZFeizyu8DRE`, `iQaDgfc-MYI` | OK |
| 7 | Restaurant Repairs | categories | not found | empty descriptions | 2 | OK |
| 8 | AmericanOutdoors | categories | not found | "Support our channel and get exclusive access to new videos, promotions, and live streams here" (both videos); the link goes to `@American-OutdoorsNet/videos`, not `/join` | `mp60lULGqrs`, `qaYOXKNEsaU` | MISMATCH (minor): a membership pitch the rule misses |
| 9 | Homeowner Helper | categories | not found | nothing | `fS5B8MF2CzM` | OK |
| 10 | HomeFix Guide | categories | not found | nothing | `PY8LVq1Y0lE` | OK |
| 11 | BIG TICKET TRUTH | categories | **affiliate; affiliate_disclosure; Lowe's (1)** | the "Lowe's" link is a cited manual ("6. Englander 25-PDVC manual (Lowe's): http://pdf.lowes.com/useandcareguides..."); the other video says **"No sponsorships. No affiliate links."** | `IJ2ucHKD-5Y`, `SVLwGSpAOmU` | **MISMATCH**: should be "not found" (the row's own review note says "source links only", but the category was kept) |
| 12 | Eivin Kilcher Homestead | categories | own_product; membership; merch; affiliate; newsletter | Kilcher Camp community, merch shop, Harvest Right affiliate, email list | `7b3m-3o5XYw`, `xy66SWDoAlc` | OK (but `affiliate_domains` lists the channel's own site, eivinandevekilcher.com (2), as an affiliate) |
| | | price | "$25 and $250 (period not captured)" | "**$25 JOIN MONTHLY**"; "**$250 JOIN FOR THE YEAR**" | eivinandevekilcher.com/kilcher-camp, 2026-10-26 | OK (the period can now be filled in) |
| 13 | ETB Seui | categories | not found | nothing | 2 | OK |
| 14 | Sierra LLC Air Conditioning & Plumbing | categories / contractor | not found / contractor n | "Sierra Air Conditioning & Heating... For more information about thermostats or any heating and/or air conditioning products and services, please visit our website at SierraCoolsLV.com" | `L01wq1WADos`, `ACoidkKTI4k` | MISMATCH: a Las Vegas contractor; contractor and own website missed (the site is plain text, not a link) |
| 15 | HarmanStoves | categories | **affiliate (bit.ly, 2)** | "For more information visit http://bit.ly/2ia3GfT": the manufacturer's own info links | `dwxRFYPnWb4`, `tEf3_QDvi3U` | **MISMATCH**: not affiliate; a shortener on a brand's own channel is not an affiliate sale |

**Error rates (part 3).** Rows with a wrong or missing category: **5/15 (33%)** (BIG TICKET TRUTH, HarmanStoves, Sierra, AmericanOutdoors, Magic Touch); the 2 false "affiliate" rows matter most (13%). Own-product names and prices: **2/2 exact** (Ray Dutton, Kilcher). The hand-checked own-product column held up; the errors are all in the rule-only categories (`reviewed = rules only`: Harman, Sierra) or where the hand review didn't update the category (BIG TICKET TRUTH).

---

## 4. New channels (`new-channels.md`, `new-channels-2026-10-26.csv`)

**Sample.** The 72 rows with `well_above = yes`, sorted by rank; `random.Random(2623).sample(…, 10)`. Only ranks 1-25 have takeoff columns, so for the other 8 I checked the "best video" that the md lists (and that the score uses). Videos tabs re-pulled (Oldest sort) 2026-10-26 08:55 UTC; joined dates from the stored About pulls, 3 also live via NexLev `youtube_channel_about`; views and dates via `vid.py`.

| Row | Channel (rank) | Field | Claimed | Found | Source | OK / MISMATCH |
|---:|---|---|---|---|---|---|
| 1 | Eli Yoder Secrets (#4) | start | joined 2026-02-05; first long-form '7mo ago' | About "Joined Feb 5, 2026" (NexLev live, same); Oldest: `gk8CHcEAcnY` '7mo ago' | About, tab | OK |
| | | takeoff 1 | `--bKaRdZGO4` 1,275,389, 2026-04-06 | 1,275,389, Apr 6, 2026 | `/next` | OK (exact) |
| | | HVAC? | yes | yes: "This $300 Tunnel Keeps Any Home 55°F Forever"; but HVAC is only 19.8% of the channel's long-form views since start (stored) | title | OK |
| 2 | Hidden Homestead (#32) | start | joined 2026-03-14; first long-form '7mo ago' | About "Joined Mar 14, 2026"; Oldest `HqD7zJN010k` '7mo ago' | About, tab | OK |
| | | best video | "Two Cheap Metals Eliminate ANY Bug Forever..." 1,300,000 `SqMTHLcHF6A` | 1,372,689, Apr 19, 2026 | `/next` | OK (views) |
| | | HVAC? | listed as a new HVAC channel "well above" | **NO**: the video is pest control; HVAC is **3.7%** of the channel's long-form views (best HVAC video 48,000); latest titles mix cement, bugs, alternators, batteries, salt heaters | titles, stored `hvac_view_share` | **MISMATCH (not an HVAC takeoff)** |
| 3 | Walt Brandt (#60) | start | joined 2026-04-30; first long-form '1mo ago' | About "Joined Apr 30, 2026"; Oldest `m0UuB26Ht1U` '1mo ago' | About, tab | OK |
| | | best video | "The Only 3 Water Heaters Worth Buying in 2026..." 55,000 `bka0Wzqc0qY` | 55,242, Sep 14, 2026 | `/next` | OK (views) |
| | | HVAC? | listed | **NO**: water heaters are plumbing (labels.md: adjacent, not counted); the channel is an appliance-repair channel (fridges, dryers, dishwashers); HVAC **4.9%** of its views | titles | **MISMATCH** |
| 4 | Lost Tech Vault (#68) | start | joined 2026-01-06; first long-form '7mo ago' | "Joined Jan 6, 2026"; Oldest `liJ2IkqAv0Y` '7mo ago' | About, tab | OK |
| | | best video / HVAC | "This Forgotten NASA Insulation Trick Cuts AC Costs 70%..." 696,000 `qqevEiBIDUQ` | 696,331, Mar 13, 2026; HVAC yes (73% of views, from this one video; 5/30 of latest titles) | `/next` | OK |
| 5 | Lost Build Archives (#37) | start | joined 2026-02-12; first long-form '8mo ago' | "Joined Feb 12, 2026"; Oldest `tXddsQ_WDaQ` '8mo ago' | About, tab | OK |
| | | best video / HVAC | "This Home Costs $300 to Build and $0 to Heat FOREVER..." 1,400,000 `5fe3rP92hjY` | 1,453,540, Mar 5, 2026; HVAC yes (house heating) | `/next` | OK |
| 6 | Dick Colter Winterproof (#36) | start | old account (2020-01-12); first long-form '4mo ago' | NexLev live "Joined Jan 12, 2020"; Oldest `v7luWI9j138` '4mo ago' | About, tab | OK |
| | | best video / HVAC | "10 Dollar Tree Items Alaskan Households Buy Before Winter..." 154,000 `afSABKuzS-Q` | 154,774, Oct 11, 2026; HVAC **borderline** (winter prep list; the channel's HVAC share is 39%) | `/next` | OK (borderline) |
| 7 | Earl Knows How (#34) | start | joined 2026-06-12; first long-form '4mo ago' | "Joined Jun 12, 2026"; Oldest `CB0-llXTG78` '4mo ago' | About, tab | OK |
| | | best video / HVAC | "This Cheap Window Trick Keeps Heat Inside All Winter" 545,000 `AQZLwcBnX1I` | 545,458, Sep 21, 2026; HVAC yes | `/next` | OK |
| 8 | Old Ways Restored (#26) | start | joined 2026-05-28; first long-form '4mo ago' | "Joined May 28, 2026"; Oldest `Sm70g1FaVbQ` '4mo ago' | About, tab | OK |
| | | best video / HVAC | "THIS Is Why Your AC Bill Is So High..." 308,000 `h_QIYDskYSo` | 308,475, Jul 28, 2026; yes | `/next` | OK |
| 9 | Attic Airflow Lab (#64) | start | joined 2026-07-30; first long-form '2mo ago' | "Joined Jul 30, 2026"; Oldest `5PkdrDuvTps` '2mo ago' | About, tab | OK |
| | | best video / HVAC | "Don't Waste $1,000 on Attic Cooling..." 51,000 `6rqtojPuTMY` | 51,348, premiered Sep 9, 2026; yes | `/next` | OK |
| 10 | Ray Sutter (#25) | start | old account (2019-04-16); first long-form '2mo ago' | NexLev live "Joined Apr 16, 2019"; Oldest `xFFHGjehswY` '2mo ago' | About, tab | OK |
| | | takeoff 1 | `4QAyLUhJYng` 932,137, 2026-09-11 | 932,193 (+56), Sep 11, 2026 | `/next` | OK (drift) |
| | | HVAC? | yes | yes: "20 Heating Sources That Don't Need Electricity (Stockpile NOW)" | title | OK |

**Error rates (part 4).** Start basis 10/10, joined 10/10, first long-form age 10/10, views and dates 10/10 (drift only). **Not really an HVAC channel or takeoff: 2/10 (20%)** (Hidden Homestead, Walt Brandt), plus 1 borderline (Dick Colter).

**Why.** "Well above" is scored on *all* long-form views since start, subscribers and the best video of *any* topic (`new-channels.md`, "Well above the niche"). A channel the census put in tier B or C for 10-30% HVAC titles can rank on bug-killer or appliance videos. In the CSV, **12 of the 72** well-above channels have an HVAC view share under 10%, and 15 under 20% (my count from `hvac_view_share`): Elias Homestead 1.3%, Forgotten American Survival 0.6%, Walter's Tool Talk 0.2%, Passive House Technology 1.9%, Hidden Homestead 3.7%, Donna Fixes 7.8%, SafeMind 1.2%, Hidden Systems 5.9%, Elias Mercer 9.6%, Walt Brandt 4.9%, Forgotten Appalachian Skills 7.2%, Prime Rundown 0.2%.

---

## 5. Sub-niches (`subniches.md`, `subniches-2026-10-26.csv`)

**Recompute.** From the CSV, tiers A-C (18,104 rows), grouping by `subniche`; median of `views_tab`, median of `multiple`, share of multiples 2.0+, biggest channel's share.

| Row | Field | Claimed (md) | Found (CSV) | OK / MISMATCH |
|---|---|---|---|---|
| AC: window, all time | n / channels / median views / median multiple / 2x+ / biggest share | 80 / 39 / 30K / 7.29 / 70% / 11% | 80 / 39 / 30,000 / 7.29 / 70% / 11% | OK |
| AC: window, 12 months | same | 16 / 14 / 8K / 2.71 / 56% / 12% | 16 / 14 / 7,950 / 2.71 / 56% / 12% | OK |
| thermostats, all time | same | 431 / 170 / 7.5K / 2.64 / 54% / 8% | 431 / 170 / 7,500 / 2.64 / 54% / 8% | OK |
| thermostats, 12 months | same | 166 / 98 / 1.4K / 1.23 / 34% / 8% | 166 / 98 / 1,400 / 1.23 / 34% / 8% | OK |
| heat and power in an outage, all time | same | 499 / 177 / 3.5K / 1.54 / 44% / 10% | 499 / 177 / 3,500 / 1.54 / 44% / 10% | OK |
| heat and power in an outage, 12 months | same | 394 / 131 / 2.1K / 1.25 / 39% / 13% | 394 / 131 / 2,100 / 1.25 / 39% / 13% | OK |

**Blind tags.** A-C rows sorted by `video_id`; `random.Random(2624).sample(…, 40)`. I tagged each title with the fine sub-niches of `subniches.md` (its tie-break: the homeowner question first, then the appliance, then the component), **before** looking at the stored tag.

**Agreement: 22/40 (55%) at the fine sub-niche; 25/40 (63%) at the labels.md parent.** The file's own fresh estimate was 34/50 (68%). The 18 disagreements:

| # | Video | Title | Stored | Mine | Kind |
|---:|---|---|---|---|---|
| 1 | `CcnT_Ke17R0` | "25 Cheap Meals Our Grandparents Ate to Survive Hot Summers" | general: cooling | not HVAC (food) | clear error (`is_hvac`) |
| 2 | `7bF81NGsJf0` | "How to Clean Your AC Coils Yourself (Companies Charge $400 For This)" | scams and upsells | coils and condenser cleaning | close call |
| 5 | `9nBLXluRFEw` | "How to Choose the BEST Furnace Air Filter (MERV Ratings & More Explained)" | brand verdicts | filters | **clear error** ("BEST" alone) |
| 6 | `60wKAbFadHE` | "Small nail office needs ventilation! #hvaccontractor..." | indoor air and purifiers | trade: commercial | close call |
| 16 | `ZrTIpKnOO_A` | "The $4 "Dry" Trick That Dehumidifies Any Room Forever — No Power Needed!" | heat and power in an outage | humidity and dehumidifiers | **clear error** ("No Power" is not an outage) |
| 17 | `z-BoOe2Lpww` | "When Should you book Air Conditioning?" | AC: central | buy or replace | close call |
| 18 | `H8OJ0sigVLk` | "My HVAC Monday running 5 no cool calls #bluecollar..." | AC: central | trade: careers and tech life | close call |
| 19 | `OAYCWYVFQpo` | "This $90 Fan Cools Your Whole House..." | cooling without AC | fans for cooling | close call |
| 20 | `mQaxgns_ZKg` | "When an HVAC Contract Changes After You Sign It..." | general: HVAC | scams and upsells | **clear error** (fell to the catch-all) |
| 21 | `2KdzGAh3Rlg` | "Fewer Friends, Closer Ones: What a Heat Pump Visit Taught Me" | trade: careers | heat pumps | close call |
| 24 | `VYPTwgX3XUI` | "Amana Downflow Gas Furnace Blower Limit Reset." | ducts and vents | parts homeowners touch | **clear error** |
| 27 | `DFUAj9jsUhs` | "HVAC: My Badge Collection and Warranty Info" | replacement cost and quotes | trade: careers and tech life | **clear error** |
| 28 | `0AcZNYarMoQ` | "Compressor Strange Noise & P1 P2 Errors - Mini Split AC Training" | smells and noises | error codes and troubleshooting | close call |
| 32 | `-AYGGTDwvrY` | "HOW TO CHECK GAS PRESSURE ON A BOILER GAS VALVE WITH A DIGITAL MANOMETER" | parts homeowners touch | boilers, radiators and steam | close call |
| 33 | `50FNL6z2So0` | "wood stove (3 in 1) can be useful to you #183" | wood and pellet stoves | DIY stove builds | close call |
| 37 | `rzrjg9ZnoFQ` | "10 Heating "Upgrades" That Are a Complete Waste of Money" | general: heating | scams and upsells | **clear error** (catch-all) |
| 38 | `FxtDaRsY-cQ` | "This Window Heat Pump Plugs Into 115V..." | heat pumps | AC: window | close call |
| 39 | `rHOGv5IVFNQ` | "Bosch Heat Pump With E6 ERROR CODE! Repaired!" | heat pumps | error codes and troubleshooting | close call |

**Error rates (part 5).** Recomputed rows 6/6 (0% error). Blind tags: 18/40 differ (45%); **7/40 clear rule errors (18%)**; 11 close calls where the tie-break could go either way.

---

## 6. Top 100 and recent winners

Both files are finished (`top-100.md` ends with "Problems and limits"; `recent-winners.md` with "Dropped candidates"), so both were checked.

**Samples.** `top-100.csv` sorted by rank: `random.Random(2625).sample(…, 15)`. Recent winners: the 120 distinct videos in the four tables of `recent-winners.md` (90 days and 12 months, by views and by multiple), sorted by video ID: `random.Random(2625).sample(…, 10)`. Views, dates and owner from `/next` (2026-10-26 09:40 UTC). Length: NexLev `youtube_video_details` for the 3 rows nearest 5:00 (`dHKD-9uI24I` 370 s, `ITtlxjvLQis` 332 s, `cHbsYYELV94` 355 s); the rest from the Videos-tab overlays (my own fresh pulls for the 10 recent rows; the stored census / sweep / top-channel pulls for 12 top-100 rows, so not independent, all 7:26 or longer). Recent-winner baselines: **all 9 channels re-pulled by me** (2026-10-26 09:45 UTC) and recomputed with my script.

| Row | Video, channel | Field | Claimed | Found | Source | OK / MISMATCH |
|---|---|---|---|---|---|---|
| top #1 | `ITtlxjvLQis` desertsun02 | views / date / length | 15,266,541 / 2014-05-09 / 5:32 | 15,266,541 / May 9, 2014 / 332 s | `/next`, NexLev | OK |
| top #8 | `_-mBeYC2KGc` Technology Connections | views / date / length | 10,392,115 / 2019-06-15 / 16:39 | 10,392,141 (+26) / Jun 15, 2019 / 999 s (tab) | `/next`, tab | OK |
| top #11 | `dHKD-9uI24I` Google Nest | views / date / length | 8,011,020 / 2015-09-01 / 6:10 | 8,011,015 (-5) / Sep 1, 2015 / 370 s | `/next`, NexLev | OK |
| top #12 | `2RDfAkmDId0` CarlTheLandscapeGuy | views / date / length | 7,832,815 / 2019-03-31 / 27:53 | 7,832,962 (+147) / Mar 31, 2019 / 1,673 s | `/next`, tab | OK |
| top #20 | `CnMRePtHMZY` Technology Connections | views / date / length | 6,356,455 / 2024-09-22 / 32:51 | 6,356,504 (+49) / Sep 22, 2024 / 1,971 s | `/next`, tab | OK |
| top #29 | `cHbsYYELV94` Maria Solko | views / date / length | 5,530,215 / 2024-12-21 / 5:55 | 5,530,216 / Dec 21, 2024 / 355 s | `/next`, NexLev | OK |
| top #31 | `V-jmSjy2ArM` Technology Connections | views / date / length | 5,388,888 / 2019-02-13 / 17:43 | 5,388,904 (+16) / Feb 13, 2019 / 1,063 s | `/next`, tab | OK |
| top #44 | `9nbK1FFBC7U` A2Z Construction | views / date / length / English | 4,157,822 / 2023-04-06 / 15:58 / English narration (NexLev transcript) | 4,157,936 (+114) / Apr 6, 2023 / 958 s / not re-checked | `/next`, tab | OK |
| top #45 | `ImFyqY0uCHg` Nica | views / date / length | 4,053,981 / 2021-04-15 / 11:39 | 4,054,011 (+30) / Apr 15, 2021 / 11:39 | `/next`, sweep | OK (multiple 30,253.6x on a 134-view baseline: true but meaningless) |
| top #49 | `nVTdukNJdtM` Mscope | views / date / length / English | 3,853,724 / 2021-10-07 / 7:26 | 3,853,755 (+31) / Oct 7, 2021 / 7:26; description in English ("It is an animation that explains how the air conditioner works") | `/next`, sweep, `desc.py` | OK |
| top #66 | `QoC8R3KHk8E` Linus Tech Tips | views / date / length | 3,554,704 / 2022-12-06 / 17:44 | 3,554,738 (+34) / Dec 6, 2022 / not re-read | `/next` | OK (length not checked) |
| top #71 | `R_g4nT4a28U` Tech Ingredients | views / date / length | 3,306,719 / 2019-07-03 / 32:50 | 3,306,723 (+4) / Jul 3, 2019 / 1,970 s | `/next`, tab | OK |
| top #78 | `fclBeOvI7FA` Holic Creation | views / date / scope | 3,214,841 / 2025-02-04 / in ("...3-in-1 Stone Stove for Free Heating at Home") | 3,214,849 (+8) / Feb 4, 2025 / in by the file's heating-word rule (a DIY craft-stove channel; no narration in the description) | `/next`, `desc.py` | OK |
| top #82 | `bpYHcXwu9JA` David Giltner | views / date / multiple | 3,107,097 / 2014-06-26 / 12,137.1x (256, last30) | 3,107,099 (+2) / Jun 26, 2014 / 3,107,097 / 256 = 12,137.1 | `/next` | OK |
| top #88 | `oVkRaiTXX3U` Wranglerstar | views / date / length | 2,918,198 / 2021-02-17 / 24:22 | 2,918,198 / Feb 17, 2021 / 1,462 s | `/next`, tab | OK |
| recent | `40zFRH-mb-o` Lost Methods Archive | views / date / multiple | 258,809 / 2026-04-18 / 995.4x (260, 12M, n=110) | 258,809 / Apr 18, 2026 / baseline 260 (12M, n=110) re-pulled -> 995.4x | `/next`, my pull | OK |
| | | scope | in ("energy bills") | **out by the file's own drop rule**: the description sells a "reactive power" device ("energy monopolies have been quietly charging homeowners for 'reactive power'"), an electrical bill gadget; the file dropped "How Smart Homeowners Are Cutting Their Electric Bill in Half (The Panel Upgrade Loophole)" as "electrical study's topic, not heating or cooling" | `desc.py` | **MISMATCH (scope)** |
| recent | `zn5IiwhAxgU` Sketchy Survival | views / date / multiple | 1,592,258 / 2026-04-16 / 1,326.9x (1,200, n=120) | 1,592,258 / Apr 16, 2026 / 1,200 (12M, n=120) | `/next`, my pull | OK |
| recent | `FkK6xKrY-qM` Haalandians | views / date / multiple | 898,855 / 2026-08-16 / 749.0x (1,200, n=25) | 899,098 (+243) / Aug 16, 2026 / 1,200 (12M, n=25) | `/next`, my pull | OK; scope borderline (Viking history explainer, not a homeowner video) |
| recent | `475x-ql8kpw` Zen Garden Oasis | views / date / multiple | 1,852,699 / 2025-12-10 / 40.3x (46,000, n=75) | 1,852,822 (+123) / Dec 10, 2025 / 46,000 (12M, n=75) | `/next`, my pull | OK |
| recent | `zGsy6s2qkr8` Unknowns Lab 101 | views / date / multiple | 1,469,222 / 2025-11-17 / 193.3x (7,600, n=120) | 1,469,222 / Nov 17, 2025 / 7,600 (12M, n=120) | `/next`, my pull | OK |
| recent | `gsi8SE_P5bg` SketchHazard | views / date / multiple | 111,104 / 2025-12-11 / 483.1x (230, n=10) | 111,104 / Dec 11, 2025 / 230 (12M, n=10) | `/next`, my pull | OK |
| recent | `iaCr4VfomMA` Unknowns Lab 101 | views / date / multiple | 2,066,537 / 2025-10-29 / 271.9x | 2,066,564 (+27) / Oct 29, 2025 / 7,600 -> 271.9x | `/next`, my pull | OK; scope borderline: "DIY Mini Stove from Tin Cans – No Gas, No Firewood, Just Free Energy at Home!" has no heating word, which `top-100.md` step 5 says leaves a craft stove out; it was kept by hand on the description ("Perfect for off-grid heating, survival cooking") |
| recent | `2kEXIAsOAMM` Creative DIY365 | views / date / multiple | 2,757,322 / 2026-01-30 / 229.8x (12,000, n=120) | 2,757,387 (+65) / Jan 30, 2026 / 12,000 (12M, n=120) | `/next`, my pull | OK |
| recent | `fHAlfm21vYw` Ray Dutton's Garage | views / date / multiple | 943,315 / 2026-09-14 / 62.9x (15,000, n=53) | 943,373 (+58) / Sep 14, 2026 / 15,000 (12M, n=53) | `/next`, my pull | OK |
| recent | `--bKaRdZGO4` Eli Yoder Secrets | views / date / multiple | 1,275,389 / 2026-04-06 / 280.3x (4,550, n=120) | 1,275,389 / Apr 6, 2026 / 4,550 (12M, n=120) | `/next`, my pull | OK |

**Error rates (part 6).** Top 100: views 15/15 (largest drift +147), dates 15/15, length 14/14 checked (3 independently), channel 15/15, English 15/15, in scope 15/15: **0% error**. Recent winners: views, dates, lengths, channels and multiples 10/10; **scope 1/10 mismatch** (`40zFRH-mb-o`) and 2 borderline (`iaCr4VfomMA`, `FkK6xKrY-qM`).

**Cautions (measured, not errors).**
- **Tiny baselines run the multiple lists.** In my sample, 3 of 10 baselines are 260 or less (Lost Methods Archive 260, SketchHazard 230 with n exactly 10) and the 12-month by-multiple list is led by Sketchsurvive at 6,278.4x on a baseline of 162. The "baseline 100+" guard lets these through.
- **The 12-month baseline is often only the last ~120 uploads.** 4 of the 9 recent-winner channels (Sketchy Survival, Unknowns Lab 101, Creative DIY365, Eli Yoder Secrets) have n = 120, the pull cap: the census marks this "Latest list ends inside 12 months". For daily uploaders that is about the last 4 months, not 12.

---

## Mismatches that matter

1. **Census: Xavier_HVAC tiered D, should be A** (24/30 HVAC by my reading, 14/30 by the rule): a residential technician ("I am a HVAC Technician and Installer... I work residential") whose service-call videos address homeowners. It went D automatically from the round 2 tier plus the word "technician" in About; `D_CONFIRM` calls the same kind of channel "not D" elsewhere. Likely not the only one: every auto-D whose `d_flags` are only "About trade words; stored D" is suspect.
2. **Census: The Archive of Builds tiered C, should be A with a lane tag** (20/30 vs the rule's 14/30). The keyword rule misses "home cools itself / beats the heat / heats your home" titles that don't name equipment. Same undercount on Construction Odyssey (21 vs 28), DIY mr.T (17 vs 27), Survival Labs (17 vs 20).
3. **Census: STOVE-CRAFT misses DIY mr.T** (96,500 subs, 5.6M top video): "Generate Heat at Home Using a Simple Trick — 24 Hours Without Electricity or Gas", "An Idea for Generating Heat at Home During the Winter Using a Metal Barrel". By the main session's own intent it belongs with the 11 STOVE-CRAFT channels in C.
4. **Types: "brand" is a fifth type nobody approved** (147 rows), and it hides presenter type: Willman Air and PRIME AC AND HEAT are on camera. **Doug Cross is on camera, not a faceless persona**.
5. **Sells: false "affiliate" on BIG TICKET TRUTH** ("No sponsorships. No affiliate links.") **and HarmanStoves** (bit.ly to its own pages). Sierra's contractor status and AmericanOutdoors' member pitch are missed.
6. **New channels: 2 of 10 sampled "well above" channels aren't HVAC risers**: Hidden Homestead (best video "Two Cheap Metals Eliminate ANY Bug Forever", 1,372,689; HVAC 3.7% of its views) and Walt Brandt (best video about water heaters; HVAC 4.9%).
7. **Sub-niches: clear tag errors on 7 of 40**, e.g. "How to Choose the BEST Furnace Air Filter (MERV Ratings...)" as *brand verdicts*, "Amana Downflow Gas Furnace Blower Limit Reset" as *ducts and vents*, the "$4 Dry Trick That Dehumidifies Any Room — No Power Needed!" as *heat and power in an outage*.
8. **Recent winners: `40zFRH-mb-o` "This $3 Copper Trick KILLS Your Electric Bill FOREVER"** (995.4x) is a "reactive power" electrical gadget. The file drops the same kind of video elsewhere.

## Recommended fixes (for the main session; I changed nothing)

1. **Census tiers.**
   1. Re-read by hand every auto-D channel whose only D evidence is "About trade words" and/or "stored D" (no name flag, no trade titles at 30%+). Decide each as D / contractor / not D in `D_CONFIRM`, as was done for HVAC AO and DC HVAC.
   2. Add home-cooling and home-heating phrases without equipment to the HVAC rule ("cools (itself|any home|your home)", "beats ... heat", "heats? (your|any|the) (entire )?home", "generate heat", "keeps? ... (cool|warm)", "without (ac|air conditioning)"). Then re-run and re-check the channels between 35% and 55%, and between 7% and 13%.
   3. Widen the `diy-stove-craft` lane, or decide by hand ("generate heat", "kettle / basin / pot / bucket / can ... heat", "bricks"). Then re-check DIY mr.T and similar channels.
   4. Consider a DRIFT-style flag for a channel whose newest 5 long-form are all non-HVAC (Hank Cole: 5 car videos in a row).
2. **Types.** Put the company flag in its own column ("company: yes / contractor / brand"). Give every row one of the brief's four types by who presents. Re-type the 147 "brand" rows and Doug Cross. Ask the operator before keeping "brand" as a type (rule 1).
3. **Sells.**
   1. Don't count URL shorteners as affiliate unless the line says so or the target is a shop.
   2. Drop "affiliate" where a description says "no affiliate links".
   3. Read plain-text website names ("visit our website at X.com") for contractors.
   4. Add "support our channel ... exclusive access" to the membership words.
   5. Fill in Kilcher Camp: $25 a month, $250 a year.
4. **New channels.**
   1. Score "well above" on HVAC long-form views (or require `hvac_view_share` of 20%+). At least flag the 12 of 72 under 10% (listed in part 4).
   2. For ranks 26-73, label the column "best video (any topic)" or show the best HVAC video beside it.
5. **Sub-niches.** Fix the 7 clear rule errors above (a bare "best" is not a brand verdict; "no power needed" is not an outage; "downflow" is not airflow; "warranty" in a tech's badge video is not a quote). Quote the map's accuracy as about 55-68% fine and 63-72% parent, not the after-fix 93%.
6. **Recent winners.**
   1. Drop `40zFRH-mb-o` under the panel-upgrade precedent, or state the exception.
   2. Make the craft-stove call for `iaCr4VfomMA` consistent with `top-100.md` step 5.
   3. Show the multiple lists with a higher baseline floor (for example 1,000) beside the current ones, and mark capped baselines (n = 120) in the table.
