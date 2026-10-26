# Round 6 check: the round 4 hand labels and the tables built from them

**Checker:** round 6 helper, 2026-10-26. No web searches. No other file was changed.
**Data:** `data/raw/round4/labels-all-2026-10-26.csv` (16,892 rows). My labels and the comparison: `data/raw/round6/check-labels-2026-10-26.csv`.
**Every label here is a reading, mine included.** "Stored" = the round 4 labeller's reading; "mine" = this checker's blind reading.

## 1. Blind re-label (200 titles)

**How the sample was drawn:** the 40 "calibration majority" rows were left out. Python `random.Random(2630)`; for each `labeller_batch` from 1 to 8 in order, `rng.sample(rows_of_that_batch, 25)`, then one shuffle. That gives 25 per batch (8 × 25 = 200, so "at least 25" means exactly 25). Only video_id, title and channel were printed. I labelled all 200 with the codes in `round4/LABEL-GUIDE.md` and saved them before reading any stored label.

**How agreement is counted:** scope is compared on all 200 rows. The other fields are compared only on the 172 rows where neither side said `n`. "Any overlap" counts as a match when the two emotion sets share at least one code, or when both are empty.

### Agreement

| Field | All | b1 | b2 | b3 | b4 | b5 | b6 | b7 | b8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| scope | 88% (177/200) | 92% | 92% | 100% | 96% | **76%** | **76%** | 88% | 88% |
| sub-niche | 90% (155/172) | **80%** | 92% | 100% | 91% | 88% | 95% | 87% | 86% |
| format | 88% (152/172) | 90% | 92% | 86% | 87% | **81%** | 95% | 87% | 86% |
| villain | 95% (164/172) | 95% | 96% | 100% | 96% | 100% | 95% | 96% | **86%** |
| first emotion | 68% (117/172) | 90% | **48%** | 73% | 61% | 81% | 62% | 65% | 73% |
| emotion sets: any overlap | 79% (136/172) | 100% | **68%** | 77% | 74% | 88% | 71% | 78% | 82% |
| emotion sets: exact | 53% (91/172) | 80% | 52% | 36% | 52% | **31%** | 57% | 52% | 59% |

Each batch has only 16 to 25 compared rows, so one title moves a batch's figure by 4 to 6 points. The per-batch columns are rough.

**Most of the emotion gap is one side leaving the emotion blank.** In 27 of the 55 first-emotion mismatches, the stored label is blank and I gave an emotion. The opposite happened only 3 times. Across the 172 rows I used 1.34 emotions per title and the labellers used 0.97. **When both sides gave an emotion, the first emotion matched in 77% (85/110) and the sets overlapped in 95% (104/110).** So the readings largely agree on *which* emotion; they disagree on *whether* a mild title carries one. The guide allows "none" for plain topic labels, so neither side is wrong here. It does mean that "has an emotion" depends on who labelled the title (section 2).

### Confusion pairs (stored → mine)

| Field | Pairs (count) |
|---|---|
| scope | ? → y (8); n → ? (5); n → y (5); y → ? (2); ? → n (2); y → n (1). Nearly all fall on three edges: DIY stove builds, history-channel heat tricks and trade-vlog titles. |
| sub-niche | drafts-insulation → energy-bill (2); noise-smell-error → boiler-oldheat (2); single cases: hvac-general → furnace, furnace → seasonal-maint, outage-heat → boiler-oldheat, humidity-air → brand-verdict, offgrid-heat → furnace, brand-verdict → drafts-insulation |
| format | symptom-fix → how-to (2); install-diy → cheap-hack (2); how-to → install-diy (2); secret → myth (2); single cases: test → x-vs-y, review → how-to, review → explainer, explainer → secret, myth → mistakes, how-to → before-you |
| villain | hvac-company → none (2); single cases: utility → none, maker-shelf → own-habit, none → maker-shelf, service-call → hvac-company |
| first emotion | blank → E13 (8), blank → E20 (6), blank → E10 (4), blank → E19 (3); E10 → E1 (2), E13 → E1 (2). The rest are mostly order swaps inside the same set. |

### 15 disagreements quoted

| # | Batch | Title (video_id) | Stored | Mine | Which I think is right |
|---|---|---|---|---|---|
| 84 | 5 | "Build 2 in 1 wood stove from red brick and cement / Serve your family meal" (`JA2tmhqMEMo`) | n ("cooking stove") | y, offgrid-heat, install-diy | **Stored.** The title sells cooking. |
| 74 | 5 | "How to make a beautiful wood stove from old drums" (`1ea0AT60fi0`) | n ("cooking stove") | y, offgrid-heat | **Unclear.** No heat word. Batches 4 and 7 put titles like this in scope (section 2). A rule is needed. |
| 51 | 4 | "The WWI Heating Hack Soldiers Used to Survive Brutal Winters" (`nYCtnphpo1o`) | n ("soldiers") | y, offgrid-heat, cheap-hack, E15/E13 | **Mine.** It sells a heating trick, like the "old ways" titles counted elsewhere. |
| 171 | 8 | "Blower Vs compressor waste oil burner conclusion" (NOBOX7, `H2k0csY3XBI`) | n ("burner") | y, offgrid-heat, x-vs-y | **Stored.** The channel is about shop and forge burners. |
| 189 | 5 | "This $400 Gravity Battery Stores Solar Energy For FREE Forever WITHOUT Lithium — Why Is It Banned?" (`iH76M34eBmA`) | y, adjacent, secret, E18 | n | **Either.** `adjacent` is a valid code, but adjacent rows are counted in the tables (caveat 1). |
| 162 | 8 | "Why Modern Heating Systems are a Scam \| modern ideas \| Here's Why" (`GBmkZLT9Uns`) | offgrid-heat, secret, E15/E12, hvac-company | scam-upsell, myth, E3/E12, maker-shelf | **Mine on format.** "Are a scam" says a belief is wrong (rule 5); there is no hidden-knowledge word. The sub-niche and villain are a toss-up. |
| 107 | 8 | "Why Every HVAC Technician Uses a Different Filter At Home — The AC Filter Lie" (`4mfEF4Nz2wA`) | secret | myth | **Mine, narrowly.** "The ... lie" is rule 5, which comes before rule 6. |
| 66 | 4 | "You're wasting money on heating! Use your AC!" (`uu7YftQlT8A`) | heat-pump, myth | energy-bill, mistakes | **Stored.** Myth comes before mistakes in the order, and "use your AC" for heat means a heat pump. |
| 36 | 1 | "$1,500 Solar Generator vs My Electric Bill" (`e4vRtDNvmgU`) | adjacent, test | energy-bill, x-vs-y | **Stored.** A stated trial is rule 1, and solar is adjacent. |
| 124 | 4 | "Mitsubishi Refrigerant Leak Repair In The BITTER COLD!" (`zyB0rtixH-8`) | how-to, no emotion | symptom-fix, E5 | **Mine.** A named failure (a leak) is symptom-fix. |
| 172 | 1 | "No Electricity, No Gas Needed 😱 This 65-Year-Old Hillbilly's 3-in-1 Stove Will Amaze You!" (`69Kt6PoLFF4`) | review | cheap-hack | **Mine.** No product is judged; it sells a substitute. |
| 144 | 4 | "Navien Power Outage. No Heat E0784 Code" (`wdgppYRZQSc`) | outage-heat | boiler-oldheat | **Unclear.** It is an error code on a combi boiler, not staying warm without power. I lean to mine, or to noise-smell-error. |
| 186 | 1 | "Biasi central heating boiler error code 01 Birmingham boiler repair specialist" (`dJQUqttoGNY`) | noise-smell-error | boiler-oldheat | **Stored.** The guide puts "error codes as the subject" in noise-smell-error. |
| 58 | 2 | "The $0 "Load" Secret That Halves Energy Bills (The Unpublicized Industry Hack)" (`hkv3cWGH0c4`) | villain utility | none | **Mine.** "Industry" is too vague; the guide wants the villain named or plainly implied. |
| 11 | 4 | "Mistakes When Buying a Heater - I Get Free Heat All Winter \| No Electricity, No Gas" (`dR5xc7Xe-Cc`) | maker-shelf, E3/E1 | own-habit, E1/E13 | **Mine.** "Mistakes when buying" is the viewer's own habit. |

Tally of these 15: stored right 6 (counting 189 as either), mine right 7, unclear 2. **Neither reader is systematically better.** The disagreements are mostly real close calls, except for the scope edge below.

## 2. Label habits per batch (full file, 16,852 non-calibration rows)

**How I judged them:** each batch covers different channels, so raw shares are expected to differ. For format and emotion I computed an *expected* share for each batch: the other 7 batches' share within each sub-niche, weighted by this batch's sub-niche mix. A big gap between observed and expected that comes from one or two channels is **channel mix**. A gap that runs across a whole kind of title, which other batches label differently, is a **labeller habit**. The blind check (section 1) is the test that channel mix can't affect.

| Batch | Rows | Channels | Scope n | Scope ? | No emotion (in scope): observed / expected | Emotions per title | Villain not none |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1,502 | 66 | 10.7% | 9.7% | 28% / 37% | 1.12 | 16% |
| 2 | 1,604 | 68 | 10.8% | **11.4%** | 30% / 33% | 1.07 | 12% |
| 3 | 1,887 | 78 | 7.3% | 4.1% | 31% / 34% | 1.04 | 13% |
| 4 | 2,515 | 87 | 11.4% | 4.1% | 31% / 33% | 1.07 | 13% |
| 5 | 2,377 | 84 | **20.2%** | 3.1% | **41% / 30%** | 0.89 | 9% |
| 6 | 2,020 | 94 | 8.4% | 6.0% | 41% / 37% | 0.83 | 12% |
| 7 | 2,511 | 74 | 6.0% | 3.2% | 32% / 33% | 0.99 | 9% |
| 8 | 2,436 | 71 | 10.3% | 3.7% | 42% / 40% | 0.85 | 18% |

The full grid of format and emotion shares (observed / expected given the sub-niche mix, 16 formats and 14 emotions × 8 batches) can be recomputed with the method above. Only the large gaps are listed below.

### Flags

1. **Habit (clear): which DIY stove builds count as in scope.** I took titles with "stove" or "heater" plus a build word (DIY, make, build, brick, cement, drum, can, 3-in-1), leaving out water heaters. Where the title names heat, warmth, winter or cold, every batch puts 79-100% in scope. **Where there is no heat word, batches 4 and 7 put 89% and 100% in scope** (DIY mr.T, Creative DIY365, Tips Clever). **Batches 1, 2, 3, 5, 6 and 8 put 2-38% in scope.** Batch 5 marks them `n` "cooking stove" (249 rows: Garden Design 102, Creative Project 60, Creative Cement Ideas 43, Creative Craft 38). Batches 2 and 6 mark them `?` (Creative Cement 54, Penpen vn 1 36, Homemade 27). It's the same kind of title read two ways, so channel mix doesn't explain it. The effect: 398 such titles are out of scope, with a median of 105K views and a median multiple of 6.73x. Counting them would lift offgrid-heat's **all-time** median multiple from 1.89x to 2.17x and its median views from 8.7K to 13K. In the **last 12 months** only 47 rows are affected (1.25x becomes 1.23x). The ones batches 4 and 7 kept in scope supply many of the E13 and E20 "best examples" (for example Creative DIY365's "No Gas, No Wood 😱 This DIY Tin Can Mini Stove Will Surprise You!", 5.50M, 458x). **Suggestion:** put one rule to the operator (for example, "a stove build is offgrid-heat only when the title or thumbnail promises heat"), then relabel this one kind of title, about 750 rows.
2. **Habit (clear): batch 2 almost never uses `brand-verdict`.** It has 4 brand-verdict rows; the others have 29 to 233. It files "Top 5 best X" lists under the equipment instead (only-x in humidity-air 40, ac-portable 19, ac-window 13, offgrid-heat 12). Its only-x share is 8.6% against 2.5% expected from its sub-niche mix. `labels.md` section 4 puts "which brands or models to buy, across a category" in brand-verdict, so this makes brand-verdict too small and humidity-air too big. **Suggestion:** move batch 2's only-x "best N" rows to brand-verdict, or accept both readings and note it.
3. **Habit (moderate): batch 5 gives fewer emotions.** 41% of its in-scope titles have no emotion, against 30% expected from its sub-niche mix. E19 is 4.7% against 10.0% expected, and E20 3.1% against 7.3%. Batch 1 goes the other way: 28% with no emotion against 37% expected, and E20 at 11.2% against 4.9% (Holic Creation 42, DIY Top Tricks 17, so partly its channels). The blind sample doesn't confirm a strong batch 5 habit (only 1 of its 16 rows was "stored blank, mine has one"), but n is small. Emotion counts are a soft measure in every batch (section 1).
4. **Channel mix, not habit: the format gaps.** `plain` in batch 8 (6.8% against 2.8% expected) is Air Conditioners Exposed's 104 model-name titles. In batch 6 it's Andrew Bdish's 99. `explainer` in batch 2 (15.2% against 9.4%) is mostly Hartzell's Heat & Air (58). `install-diy` in batch 1 (14.5% against 8.5%) is Holic Creation, Advantage Heating & Cooling and T&N Services. Batch 3's low symptom-fix in the equipment sub-niches (16% against 22-38% elsewhere) is the one gap I can't pin on channels; the blind check found no symptom-fix confusion in batch 3, so I'd call it mild. **No batch is clearly off on format.**
5. Scope `?` is high in batch 1 (9.7%) and batch 2 (11.4%). In batch 1 it comes from Ryan Hughes HVAC (59) and D2D NY (28), both trade-vlog titles. In batch 2 it's the stove rows (flag 1). The trade-vlog edge also splits between batches: batch 8 marks OnemanHVAC's "running calls" vlogs `n`, and batch 6 marks "Busted my head open today on an hvac install!!" `n`, where I said `?`. That one is small.

## 3. Table check (recomputed independently from labels-all, scope_ok = y; last 12 months = last12m yes/1/true)

| Table | Row | File says (n, channels, median views, median multiple, 2x+) | My recompute | |
|---|---|---|---|---|
| emotions.md, overall (12 months; all-time n / median) | E18 | 212, 80, 3.3K, 1.50x, 41%; 311 / 1.82x | 212, 80, 3,300, 1.50, 41; 311 / 1.82 | match |
| | E1 | 2,256, 299, 1.7K, 1.17x, 37%; 2,987 / 1.45x | same | match |
| | E7 | 49, 34, 878, 0.82x, 15%; 161 / 1.31x | 49, 34, 877.5, 0.82, 15; 161 / 1.31 | match |
| | E10 | 1,351, 219, 2.1K, 1.15x, 35%; 1,758 / 1.33x | same | match |
| | E19 | 770, 217, 1.2K, 1.21x, 37%; 1,187 / 1.56x | same | match |
| subniches.md, last 12 months | offgrid-heat | 1,452, 180, 4.5K, 1.25x, 38% | 1,452, 180, 4,450, 1.25, 38 | match |
| | brand-verdict | 438, 55, 421, 1.44x, 41% | same | match |
| | ac-window | 28, 15, 1.7K, 2.80x, 54% | same | match |
| | furnace | 198, 71, 702, 1.00x, 25% | 198, 71, 702.5, 1.00, 25 | match |
| | ac-central | 531, 107, 1.2K, 1.08x, 31% | same | match |
| formats.md, formats 12 months | test | 190, 79, 7.5K, 1.52x, 42% | same | match |
| | secret | 1,271, 188, 2.4K, 1.19x, 37% | same | match |
| | plain | 67, 22, 2.7K, 0.92x, 15% | same | match |
| | cheap-hack | 1,116, 170, 2.7K, 1.17x, 37% | same | match |
| formats.md, villains 12 months | own-habit | 266, 109, 694, 1.27x, 35% | 266, 109, 694.5, 1.27, 35 | match |
| | none | 4,900, 425, 1.9K, 1.13x, 34% | same | match |
| | service-call | 50, 37, 542, 0.89x, 27% | 50, 37, 541.5, 0.89, 27 | match |
| | utility | 156, 66, 3.1K, 1.13x, 39% | same | match |

**All 18 rows match.** One small gap: 52 rows have a blank `last12m`. Only one of them is dated after 2026-10-26 minus 12 months, so the 12-month tables miss at most 1 video. 56 in-scope rows have no multiple.

## 4. Read as a skeptic: what could mislead, and a fix for each

1. **`adjacent` is counted and ranks #2 in the last-12-months sub-niche table** (111 videos, 1.48x). `labels.md` section 4 says adjacent rows are "recorded ... so they can be seen but not counted". Builds With Eli Yoder supplies 21 of them, The Passive House Files 11 and Wild Line 10. **Fix:** leave adjacent out of the ranking, or show it on its own line below the table.
2. **Tiny n at the top of rankings.** ac-window is ranked #1 in the 12-month table at 2.80x on 28 videos from 15 channels. Its top 3 channels hold 54% of those, and all time 115 of its 209 videos are Air Conditioners Exposed. parts (41 videos), noise-smell-error (49), E9 (19), E7 (49) and E8 (86) also rank on small n. The by-type columns go down to n = 2 ("ac-window faceless persona 11.15x (2)"). **Fix:** raise MIN_N from 15 to about 50 videos and 10 channels for ranking, and grey out the rest.
3. **brand-verdict and only-x lead on multiples over tiny baselines.** brand-verdict is #3 in the 12-month table at 1.44x, but its median is **421 views**, the lowest of any large sub-niche. The top 3 channels give 33% (TempTrends 79, NextGadget 33, Homey Vibe 32), and 144 of its 438 videos come from channels whose baseline is under 100 views. only-x is #2 in the 12-month formats (1.44x, 567 median views), with 156 of 516 from channels with baselines under 100. **Fix:** print median views next to the multiple in every ranking, and add a "channels with baseline 500+" column (the examples already use that filter).
4. **Absurd multiples and broken baselines.** 509 in-scope videos sit at 100x or more and 38 at 1,000x or more. 52 channels have baselines under 100 views; together they make up 10% of the 12-month in-scope rows. Hartzell's Heat & Air's baseline is about 2 views, which turns a 94K-view video into 47,000x. Medians resist this; "share at 2x+" is weaker against it. **Fix:** flag baselines under 100 (or under 500) as unreliable in `channels.md`, and report the tables both with and without them.
5. **Each sub-niche's scope depends on the batch** (section 2, flags 1 and 2). offgrid-heat (all time) and brand-verdict / humidity-air are the ones moved. **Fix:** as in section 2.
6. **Concentration in the 5 biggest sub-niches (last 12 months).** The table shows the top 3 channels' share and the median with them removed. Most medians barely move, so they are **not** single-channel artefacts. brand-verdict is the exception, partly.

| Sub-niche (12 months) | n | Top 3 channels | Top 3 share | Median | Without top 3 | Median of channel medians |
|---|---:|---|---:|---:|---:|---:|
| offgrid-heat | 1,452 | Creative DIY365 145; Tips Clever 120; Unknowns Lab 101 108 | 26% | 1.25x | 1.22x | 1.33x |
| cooling-no-ac | 540 | Builds With Eli Yoder 32; Passive Survival 26; Sketchy Survival 19 | 14% | 1.16x | 1.17x | 1.06x |
| ac-central | 531 | Drewdriskle 45; JustintimeHVAC 35; Exposi 19 | 19% | 1.08x | 1.10x | 1.27x |
| brand-verdict | 438 | TempTrends 79; NextGadget 33; Homey Vibe 32 | 33% | 1.44x | 1.34x | 1.52x |
| drafts-insulation | 374 | Attic Airflow Lab 29; Passive Survival 16; SecretLab 13 | 16% | 1.31x | 1.29x | 1.32x |

7. **own-habit's #1 villain spot in the last 12 months rests on 3 channels.** It drops from 1.27x to 1.05x without Forgotten Materials, Winter Farmstead and Ask Rose, which puts it below "none" (1.13x). **Fix:** say so in the table, or rank on the channel-weighted median (1.32x, which still leads).
8. **Rows in the 12-month tables sit only 1.0x to 1.5x apart, and the emotions are a soft reading.** Labellers leave 28% to 42% of titles with no emotion, a title can sit under three emotions at once, and two readers agree on the first emotion only 68% of the time (section 1). **Fix:** call gaps under about 0.2x "no clear difference". Present the emotion ranking as a reading to test, not a finding.
9. **All-time tables mostly measure video age.** noise-smell-error goes from #1 all time (3.55x) to 1.08x in the last 12 months, thermostat from 2.89x to 1.08x, and boiler-oldheat from 2.53x to 0.99x. "Videos with no emotion" has a 2.40x median all time, above every emotion, because old plain titles have had years to gather views. emotions.md already says "read the last-12-months columns first", but subniches.md and formats.md put all-time first. **Fix:** put the 12-month table first in all three files and label the all-time one "includes the age effect".
10. Smaller points. `plain` in the last 12 months is 46% Andrew Bdish (31 of 67). `test` in the last 12 months is 17% Ryan's Fireplace Diaries (33 of 190); without it the median rises from 1.52x to 1.64x. Neither changes a conclusion, but both are worth a footnote.
