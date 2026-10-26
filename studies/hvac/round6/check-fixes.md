# Round 6 check: the round 3 fixer's changes

Checked 2026-10-26 by the round 6 check-fixes helper (CLAUDE.md working rule 3). This is a second helper's re-check of the fixes listed in `round3/check-round3.md` under "Fixes applied (2026-10-26)". Raw results are in `data/raw/round6/check-fixes-2026-10-26.json`. My scripts are in my scratch folder, and I ran every one with `python3 -I`. Web searches: 0. Thumbnails came from i.ytimg.com (direct loads, not searches). I edited nobody else's file and committed nothing.

## Summary

| Part | Sample (seed) | Checked | Mismatches | Error rate | Matters? |
|---|---|---:|---:|---:|---|
| 1. Hand fixes: tiers | 25 of 62 (2640) | 25 | 0 | 0% | no |
| 1b. D decisions (fix 1.1), all 16 | all | 16 | 0 applied wrong, 1 reason text inconsistent | 0% | no |
| 2. Types (type4) | 15 of 51 (2641) | 15 | 1 (low confidence) | 7% | no |
| 3a. New channels: HVAC view share >= 20% | 10 of 60 (2642) | 10 | 0 | 0% | no |
| 3b. New channels: is "best HVAC video" really HVAC? | same 10 | 10 | 2, plus 1 doubtful | 20-30% | **yes** |
| 4. Recent winners: floor-1,000 lists | 8 of 80 (2643) | 8 | 0 | 0% | no |

The tier hand fixes, the types and the floor-1,000 lists hold up. The weak spot is the "Best HVAC video" column and the HVAC view share in `new-channels.md`. Both come from the census title rule. The rule misses "cool our homes" and "heats a room" wordings, and it counts water filters, wind turbines and electric-bill devices as HVAC. Outside the sample, this probably lets 1 to 3 channels through the 20% share rule that should be dropped (see part 3).

## Part 1: hand fixes (25 random of the 62, seed 2640)

**Method.** I took each channel's latest 30 long-form titles from `data/raw/census-2026-10-26/<id>.json`: the Latest list, or Latest_initialpage when it is longer, with duration of 5:00 or more. For LOW-N channels I pooled them with the Popular top 10, as the build does. I read the titles myself before looking at the fixer's count and counted the HVAC, heating, cooling, bill, insulation-about-heat, outage-heat and off-grid-heat titles. Scope follows `labels.md` and the README: air purifiers, ventilation, humidity, mould and bath fans count; generators count only for warmth in an outage; insulation counts only with a heat, cooling or bill word. The tier rule is A at 50% or more; B at 10-49% (C when lane words dominate); X under 10%; D for trade-facing or company channels. Contractors teaching homeowners are A, and DIY stove-craft channels are C. "Claimed" is the fixer's count and tier in `census-handread-2026-10-26.csv`. In all 25 rows, the tier in `census-channels-2026-10-26.csv` equals the hand-fix tier.

| # | Channel | Field | Claimed | Found (my count, my tier) | OK/MISMATCH |
|---:|---|---|---|---|---|
| 1 | Bailey Line Road | tier | 2/30, X | 2/30 (2 wood-boiler titles), X | OK |
| 2 | brother Q | tier | 4/5, A (LOW-N) | 4/5, A (2 boiler no-heat titles certain; "Pilot assy replacement" x2 read as boiler parts) | OK (the pool is only 5: the Popular list is empty in the pull) |
| 3 | DIY WISCO | tier | 2/30, X | 2/30 (2 mini-split installs), X | OK |
| 4 | Healthy Home Guide | tier | 19/30, A | 18-22/30 (purifiers, ventilation, ERV/HRV, humidity, mould), A | OK |
| 5 | World of HVAC | tier | 21/30, A | 20-21/30, A | OK (many tech-tool titles: "Want To Be An HVAC Tech?", "Ultimate HVAC Packout"; A vs D is a judgment call) |
| 6 | Miillers Construction | tier | 2/30, X (COMPANY) | 2/30 (2 Tosot mini-split installs), X | OK |
| 7 | desertsun02 | tier | 15/30, C (STOVE-CRAFT) | 13-16/30 (DIY heaters and air coolers), C | OK |
| 8 | andyfireblade | tier | 29/30, A | 29/30 (only the gas welding set out), A | OK |
| 9 | Michigan Heating Guy | tier | 18/30, A | 18/30, A | OK |
| 10 | CP Utility Solutions | tier | 19/30, A (contractor) | 18-19/30, A (contractor) | OK |
| 11 | Powlas HVAC | tier | 18/30, A | 16-20/30, A | OK |
| 12 | Prime Rundown | tier | 1/30, X | 1/30 (air-filter brands only), X | OK |
| 13 | Sam | tier | 15/30, A | 15/30 with the 2 bath-fan titles (in scope), A | OK (exactly 50%) |
| 14 | Ecohome Insulation | tier | 0/16, X (COMPANY) | 0/16, X | OK |
| 15 | BlueTex Insulation | tier | 2/13, D | 2/13, D | OK (both HVAC titles are Shorts, 1:24 and 3:48, from the Popular pool; long-form alone is 0/6) |
| 16 | Jesse Muller | tier | 2/30, X | 2/30 (radiant slab, hydronic diesel heater), X | OK |
| 17 | Missouri Wind and Solar | tier | 0/30, X (COMPANY) | 0/30 ("Solar Pool Heating Myths" is a pool, not the home), X | OK |
| 18 | Handyman Land | tier | 2/30, X | 2/30 (2 Cadet wall-heater titles), X | OK |
| 19 | Everyday Home Repairs | tier | 2/30, X | 2-3/30, X | OK |
| 20 | Everyday Solar | tier | 2/30, X | 2/30 (furnace in an outage, sand-battery heater), X | OK |
| 21 | HVAC Life | tier | 19/30, D | 19-20/30, trade-facing (VRF, Trane controls, loadouts), D | OK |
| 22 | Everything Electric TECH | tier | 1/30, X | 1-2/30, X | OK |
| 23 | OffGrid Secrets | tier | 15/30, A | 15/30, A | OK (exactly 50%) |
| 24 | Brantley Blended | tier | 2/30, X | 2/30 (dehumidifier, fresh-air return), X | OK |
| 25 | Forever Tech English | tier | 20/30, A | 19-20/30, A | OK |

**Error rate: 0/25.** Four calls are borderline and worth a line in the round 7 report:
- Sam and OffGrid Secrets sit at exactly 15/30. One title either way changes the tier.
- brother Q is A on 5 titles.
- World of HVAC and Forever Tech English are A rather than D on a reading of who the titles are for.

**1b. The 16 fix-1.1 D decisions (all checked).** Every one is applied in `census-channels-2026-10-26.csv`: 12 D (Zach of All Trades then X by hand fix); Xavier_HVAC A with the contractor flag; Heatable D with the contractor flag (11/30, under 50%; my count 8-11/30); AB HVAC A by hand fix; The Engineering Mindset B (4/30). There is one inconsistency, and it is trivial. **AwesomeFramers**' `D_CONFIRM` reason says "HVAC 2 of 30 titles", but the hand-read row says "my count 3/30 ... stays D". At 2/30 the channel would be X, the same treatment Zach of All Trades got. My count is 2-3/30: crawl-space venting, "Full House Construction Designed for Maximum Utility Savings", and a blower-door title. It is borderline either way.

## Part 2: types (15 random of the 51 rows whose type4 differs from type, seed 2641)

**Method.** I downloaded the hqdefault thumbnails of each channel's 3 newest long-form videos (from the census Latest list, 2026-10-26). I built my own contact sheets and judged on camera / faceless / AI avatar / faceless persona from them. **Caveat:** my sample listing printed the fixer's type4 before I looked, so the check is not fully blind. I used my own thumbnails, not the fixer's sheets.

| Row | Channel | Field | Claimed (type4) | Found | OK/MISMATCH |
|---|---|---|---|---|---|
| B029 | Structure Tech Home Inspections | type4 | on camera | on camera (2 real men, 3 of 3) | OK |
| A044 | Bright Air Duct Cleaning - Florida | type4 | faceless | faceless (workers from behind, logo templates) | OK |
| A152 | Ductless Plus HVAC | type4 | on camera | on camera (same real man, 3 of 3) | OK |
| A114 | RetroFoamofMichigan | type4 | on camera (low) | faceless: 2 of 3 are foam graphics, and the 3rd is a customer couple holding a rebate cheque | MISMATCH (low confidence both ways) |
| A002 | Hartzell's Heat & Air | type4 | faceless | faceless (cartoon podcast cover, logo ad) | OK |
| A216 | Advantage HVAC, Plumbing, and Electrical | type4 | on camera (low) | on camera (low; 1 thumbnail, a real woman by the van) | OK |
| A010 | Barton Oil Burner Services | type4 | faceless | faceless (staff with no face, text cards) | OK |
| B207 | Rise | type4 | on camera | on camera | OK |
| A209 | Insulwise Energy & Comfort Solutions | type4 | on camera | on camera (same man in attics, 3 of 3) | OK |
| A038 | True Blue Heating & Cooling | type4 | on camera | on camera (low; a real tech side-on in 2) | OK |
| A027 | The Smart Way to Buy HVAC with Doug Cross | type4 | on camera | on camera (same real man, 3 of 3) | OK |
| A105 | Birmingham Boiler Fix | type4 | on camera | on camera (same engineer, 3 of 3) | OK |
| A049 | American Veteran Air & Heat | type4 | on camera (low) | on camera (low; a real man in 1 of 3) | OK |
| A107 | Fire & Ice Home Services | type4 | on camera | on camera (uniformed staff, 3 of 3) | OK |
| A045 | Monkey Wrench Plumbing, Heating, Air & Electric | type4 | on camera | on camera (2 of 3) | OK |

**Error rate: 1/15 (7%), low confidence.** I saw no AI avatar. Several "on camera (low)" company channels show a person in only 1 of 3 or 4 thumbnails. For a company channel that is a thin basis for "on camera".

## Part 3: new channels (10 random of the 60 "well above", seed 2642)

**Method.** I recomputed long-form views since the start, HVAC views and the share from `census-videos-2026-10-26.csv`, using the same since-start rule as `new_channels_build.py`. All 10 match the CSV exactly. Then I read every title myself, judged which are HVAC, and checked the "best HVAC video" shown.

| Rank | Channel | Field | Claimed | Found | OK/MISMATCH |
|---:|---|---|---|---|---|
| 44 | Construction Odyssey with Eddie | share / best HVAC | 90.0% / "This $300 Tunnel Keeps Your Home 55°F Forever..." (2.2M) | over 90% (the rule misses "Heates", "Heats a Home") / same | OK / OK |
| 47 | Hank Cole | share / best HVAC | 95.5% / "The $5 Fix That Makes Your AC Blow 9° Colder..." (156K) | ~97% / same | OK / OK |
| 15 | Harlan Sawyer | share / best HVAC | 78.1% / "5 Woodpile Dangers That Can Put You in the Hospital..." (438K) | 44% without the woodpile video, up to ~63% with the missed chimney-fire and split-size titles / doubtful | OK / **DOUBTFUL** |
| 24 | Exposi | share / best HVAC | 97.1% / "Doing This Will Make Your AC Run Like NEW Again!" (335K) | ~97% / same | OK / OK |
| 64 | Eli Forgotten Ways | share / best HVAC | 39.7% / "These 6 Wind Turbines Are The Future Of Home Energy" (42K) | ~62% / "Why Did We Stop Using Ammonia To Cool Our Homes?" (87K, `D7UKnOB0lPo`) | OK / **MISMATCH** |
| 31 | Repara Fácil USA | share / best HVAC | 83.0% / "Before Turning On Your Heater This Fall, Do This..." (135K) | ~95% (Spanish AC titles missed) / same | OK / OK |
| 6 | OffGrid Secrets | share / best HVAC | 55.3% / "This 3,000-Year-Old Layout Cools For $0..." (648K) | over 58% / same | OK / OK |
| 67 | TheUnknownMarks | share / best HVAC | 42.2% / "This $8 Walmart Pad Keeps Your Bed Warm With No Heat..." (30K) | ~98% / "This $4 Can of Crisco Heats a Room for 45 Days — Zero Electricity, Zero Gas" (74K, `_eNzYpPztj0`) | OK / **MISMATCH** |
| 10 | Craftsman Chris | share / best HVAC | 99.9% / "Turning a Dumpster AC Into a Super-Efficient Geothermal Heat Pump" (781K) | 99.9% / same | OK / OK |
| 54 | Earl Sizemore | share / best HVAC | 85.0% / "STOP Paying for Heat This Winter. Fill This $10 SALT BUCKET..." (123K) | ~85% / same | OK / OK |

**Error rate:**
- Share at 20% or more: **0/10**. Every sampled channel passes, often by more than the rule says.
- Best HVAC video: **2/10 wrong, plus 1 doubtful.**

**Harlan Sawyer.** The same video, `BlHC-momweM`, is dropped from the recent and top lists in `topvideos-exact-2026-10-26.json` as "woodpile hazards (firewood handling), not heating the home". Yet it is Harlan Sawyer's best HVAC video and takeoff 15.1 (HVAC "yes") in `new-channels.md`. Takeoff 15.2, "5 Woods That Set Chimneys on Fire", is marked HVAC "no". The two deliverables disagree.

**Found outside the sample** (while scoping the problem). In 17 of the 60 well-above rows, "best video, any topic" differs from "best HVAC video". I read all 17 pairs and the full title lists of three suspect channels:

| Rank | Channel | What I found | Matters? |
|---:|---|---|---|
| 11 | Historia Prime | The best HVAC video is "Connecting Two Metals Purifies ANY Water — The "Earth Filter" Secret They Buried" (1.6M, `tSFizbjaCBo`), which is water purification. The same video is dropped as "water purification, not HVAC" in `topvideos-exact`. Without it the share is 15.4%, not 29.4%. Adding the missed warmth titles ("Vikings Beat Winter Without Fire — The Ancient Floor Hack...", 338K; "The Overnight Warmth Rule Grandparents Never Broke", 146K; "Salt + Aluminum Foil = Free Heat Forever", 84K; possibly the heat-candle and bed-insulation titles) gives about 20-25%. | **yes**, borderline on the 20% line |
| 45 | Grain & Gravity | The 32.7% share rests on "This Plug-In Battery Cuts Home Energy Bills By 60% WITHOUT Solar" (444K) and "Plug-In Solar Cuts Home Energy Costs..." (167K). The recent-winners review drops electric-bill devices as out of scope (`40zFRH-mb-o`, `JJDOg6Zmtk8`). Judged the same way, the share is about 5%. | **yes**, would fail 20% |
| 71 | WiseMoney | The 28.9% share rests on "This $8 Trick Cuts Your Electricity Bill in Half..." (332K) and "35 CHEAP Items That REPLACE Electricity..." (98K). Without them it is about 11%. | **yes**, needs a hand read |
| 65 | Backyard Low Tech | The best HVAC video is "Don't Buy Solar Yet — This $18 Thermoelectric Chip Powers My Gear From Attic Heat" (142K), which is power. The share is still about 28% without it. | display only |
| 48 | Hidden Systems | The hand share was fixed (90%), but the best HVAC column still shows the rule's pick (19K). "Best any", "The $12 Norwegian Stove That Heats a House for 18 Hours on One Log" (347K), is HVAC. | display only |
| 59 | Elias Mercer | The hand share was fixed (95%), but the best HVAC column shows 7.1K. "Best any", "Old-Timers Never Heated the House When the Power Died. They Did This ($0)" (160K), is outage heat. | display only |

## Part 4: recent winners, floor-1,000 lists (8 random of the 80 rows, seed 2643)

**Method.** I parsed both floor-1,000 tables in `recent-winners.md` and drew 8 rows. For each row:
- I took views and date from the exact `/next` pull in `topvideos-exact-2026-10-26.json`.
- I recomputed the baseline from the raw tab pulls: the median of long-form Latest-list videos certainly inside 12 months, from `census-2026-10-26/` or `top-channels-2026-10-26/`.
- I computed multiple = views / baseline and checked the baseline is at least 1,000 and the upload date falls in the window.

| List, # | Video | Field | Claimed | Found | OK/MISMATCH |
|---|---|---|---|---|---|
| 90d #26 | "Before Central Heating, How Did Americans Survive Freezing Winters?" (`9-eQiEQOhyo`, Secret State Files) | views / baseline / multiple / date | 1,224,700 / 15,000 (n=105) / 81.6x / 2026-09-05 | 1,224,700 / 15,000 (n=105) / 81.6x / 2026-09-05 | OK |
| 90d #13 | "15 Cheap Walmart Items That Become WORTH GOLD When Your Furnace Dies" (`rX4eyZaHAjw`, Lost Survival Knowledge) | same | 1,327,280 / 10,000 (n=31) / 132.7x / 2026-10-14 | same | OK |
| 12m #18 | "FREE Heat All Winter😱!! Millions of people don't know this secret – Free Energy For Winter" (`sngNQIbfZxo`, Tips Clever) | same | 1,631,013 / 5,150 (n=120, capped) / 316.7x / 2025-12-02 | same | OK |
| 12m #7 | "No Gas, No Wood 😱!! This Simple DIY Stove Heats for FREE All Winter" (`H2SrcFJ8g6s`, Creative DIY365) | same | 7,535,159 / 12,000 (n=120, capped) / 627.9x / 2025-12-30 | same | OK |
| 90d #17 | "Do THIS Once a Month and Your AC Will Last 25 Years" (`CJhglI70jw8`, John The HVAC Guy) | same | 232,795 / 2,000 (n=72) / 116.4x / 2026-08-15 | same | OK |
| 12m #44 | "Millions Don't Know This 😱 Turn Charcoal Into a DIY Heat Source..." (`hJNFA6oxbA8`, Creative DIY365) | same | 2,045,436 / 12,000 (n=120, capped) / 170.5x / 2026-06-09 | same | OK |
| 12m #47 | "Millions Don't Know This! DIY 3-in-1 Heating Stove..." (`EU89zAZS970`, Unknowns Lab 101) | same | 1,183,500 / 7,600 (n=120, capped) / 155.7x / 2025-12-10 | same | OK |
| 90d #22 | "Do THIS Before Winter and Your Furnace Will Last 30 Years" (`D3s86GpsnZ4`, John The HVAC Guy) | same | 177,794 / 2,000 (n=72) / 88.9x / 2026-08-25 | same | OK |

**Error rate: 0/8.**

**Full rebuild.** I also rebuilt both floor-1,000 lists independently from the exact JSON: decision "keep", exact date in the window, baseline at least 1,000, n at least 10, length at least 5:00. The order is identical, 30/30 and 50/50. No unreviewed video sits above either list's cut-off. The 9 and 14 non-kept videos above the cuts are all hand drops with reasons. A reading, not an error: 5 of the 8 sampled rows (and much of the 12-month list) come from DIY "free heat" craft channels (Creative DIY365, Tips Clever, Unknowns Lab 101). They pass `top-100.md` step 5 because they carry a heating word.

## Mismatches that matter

1. **Wrong "best HVAC video" in `new-channels.md`.** Two in the sample:
   - Eli Forgotten Ways shows "These 6 Wind Turbines Are The Future Of Home Energy" (42K); the real best HVAC video is "Why Did We Stop Using Ammonia To Cool Our Homes?" (87K).
   - TheUnknownMarks shows "This $8 Walmart Pad Keeps Your Bed Warm..." (30K); the real one is "This $4 Can of Crisco Heats a Room for 45 Days" (74K).

   Outside the sample: Historia Prime (a water filter, 1.6M), Backyard Low Tech (a thermoelectric power chip), and the stale picks for Hidden Systems and Elias Mercer.
2. **The 20% share rule probably passes channels it should drop.** Grain & Gravity (about 5% by the study's own bill-device standard), WiseMoney (about 11%, needs a read) and Historia Prime (15-25%, borderline) are all outside the sample. The fixer hand-read only the channels the rule *dropped*, not the ones it passed.
3. **The two deliverables disagree on `BlHC-momweM`** ("5 Woodpile Dangers..."): it is HVAC in `new-channels.md` but dropped from the top and recent lists.

## Recommended fixes

1. In `new_channels_build.py`, hand-read the titles behind "best HVAC video" and the share for every well-above channel the rule *passes*: at least the 17 where best-any differs from best-HVAC, plus any whose share depends on one or two big titles. Add them to `HVAC_SHARE_HAND`, with a field that also corrects the best HVAC pick. Apply the same drops as `top_review.py` (water filters, power and electric-bill devices, woodpile handling) so the two deliverables agree. Re-run, and report which channels leave "well above". Grain & Gravity and WiseMoney are the likely ones, with Historia Prime borderline.
2. Decide `BlHC-momweM` once, as HVAC or not, and apply it in both `new-channels.md` (Harlan Sawyer's best HVAC video and takeoff 15.1) and `top_review.py`. If it is dropped, Harlan Sawyer's best HVAC video becomes "5 Woods That Set Chimneys on Fire..." (133K) if chimney safety counts, otherwise "5 Cheap Wood Stove Tricks..." (113K). Either way Harlan stays well above.
3. AwesomeFramers: make the `D_CONFIRM` reason ("HVAC 2 of 30") match the hand read (3/30), or move it to X. This is minor.
4. RetroFoamofMichigan type4: mark it "on camera / faceless (low)" or look at more thumbnails. More broadly, "on camera (low)" on a company channel that rests on 1 of 3 or 4 thumbnails should say so in the round 7 report.
5. Round 7 report: list the 50%-exactly A calls (Sam, OffGrid Secrets), the 5-title A (brother Q) and the A-vs-D tech channels (World of HVAC, Forever Tech English) as borderline.

## Hand read (2026-10-26)

Round 6 fixer, 2026-10-26. This replaces the title rule in the "well above" test of `new-channels.md` (recommended fix 1 above; fix 2, `BlHC-momweM`, is covered on the new-channels side). Scripts were run with `python3 -I`. Web searches: 0. No new exact (`/next`) pulls were needed. Nothing was committed. Files written: `data/raw/new-channels-handread-2026-10-26.csv` (new), `data/tools/new_channels_build.py` (edited), this section, and the build's own outputs `data/raw/new-channels-2026-10-26.csv` and `data/raw/new-channels-exact-2026-10-26.json`. The exact JSON is byte-identical: its build inputs were rebuilt from the JSON itself, and an unchanged re-run first reproduced both outputs exactly. **`new-channels.md` is not edited.** Its summary lines below are drafted for the main session to apply.

### What was read

There are **103 channels** and **6,807 long-form titles** (all of each channel's titles in `census-videos-2026-10-26.csv`). 6,662 of them are since the start. The other 145 are pre-start titles of 4 pivot or restart channels, read but not used. The 103 channels are:

- the 60 well above;
- every other channel scoring 2.4 or more (0.8x the threshold of 3): 18 channels, the 11 that the 20% rule already dropped plus 7 that fail the score rule;
- every other new channel with an HVAC view share of 10-30%: 25 channels, all scoring under 2.4, so they can't become well above.

Each title is marked in scope y / n by `round4/LABEL-GUIDE.md`. I read every title in a listing that showed the round 4 label or the census rule beside it, and I changed the mark wherever my reading differed. The `source` column records where each mark came from:

| Source | Titles |
|---|---:|
| round 4 label, kept | 2,125 |
| my reading where round 4 said y | 160 |
| my reading where round 4 said n | 1 |
| my reading where round 4 has no label or said "?" | 4,521 |

Result: 2,484 y, 4,323 n. These are readings.

**How I drew the lines** (round 4 guide, README scope decisions and the drops in `top_review.py`):

- **Out:**
  - power, solar, batteries, wind, alternators and "free electricity", including "propane tank stores solar" and "earth battery grid", even where round 4 said y;
  - electric-bill gadgets: device, wire, copper, sticker, plug and reactive-power titles, as `40zFRH-mb-o` and `JJDOg6Zmtk8` in `top_review.py`;
  - utility-bill news;
  - water purification, water heaters and hot water;
  - cooking stoves and gas-cylinder replacement, and craft "free energy" stoves with no heat word, as `iaCr4VfomMA`;
  - firewood handling: woodpile and woodshed hazards, splitting, hauling, chainsaws and axes;
  - outdoor, car, tent, soldier-gear and body warmth;
  - mould-cleaning tricks;
  - insulation and windows with no heat, cooling or bill word;
  - garages, barns, greenhouses and coops;
  - commercial and trade-only titles;
  - Spanish titles (not English).
- **In:**
  - home heating and cooling tricks, home designs sold on heating or cooling cost ("cools for $0");
  - stoves, chimneys and burn time;
  - firewood bought or stored for burning;
  - outage heat, and bed-warming "with no heat";
  - damp, humidity, condensation and ventilation;
  - bill-cutting tricks and habits with no named device. This keeps WiseMoney's "$8 Trick Cuts Your Electricity Bill in Half" (round 4 y, kept in `top_review.py`);
  - residential service-call titles on HVAC tech channels.

### Build change

`new_channels_build.py` now reads the hand-read file (`HANDREAD`). For a channel in the file:

- its HVAC view share, best HVAC video and takeoff "HVAC" column come from the hand read;
- the hand read replaces `HVAC_SHARE_HAND`, whose 8 channels are all in the file;
- the 20% rule is unchanged.

Other channels keep the census rule. Ranking, score and the top 25 are unchanged. New CSV columns are `best_hvac_video_source`, `hvac_lf_since_start_hand` and `hvac_lf_views_since_start_hand`. The rule-based `hvac_view_share` is kept, and `hvac_view_share_hand` now holds the hand share.

### Results

**Well above: 60 → 58** (A 32, B 10, C 16; C was 18). The score rule still passes 71. The 20% rule now drops 13 (was 11).

| # | Channel | Share before → after | Why |
|---:|---|---|---|
| 18 | **The Passive House Files** (C) | 27.4% → 15.6%: **drops** | Round 4 labelled 4 power-storage titles y. I read them n, as the guide says (batteries or solar for the bill): "STOP Buying $10,000 Home Batteries. Fill This $150 PROPANE TANK With Solar Power..." (315K), "This $90 PROPANE TANK Stores SOLAR Power For 30 YEARS" (290K), "...Bury This 12-CELL EARTH BATTERY GRID..." (236K) and "This $600 SEPTIC TANK Holds 16 Powerwalls of Energy" (115K). |
| 45 | **Grain & Gravity** (C) | 32.7% → 2.3%: **drops** | Plug-in battery and plug-in solar bill titles are out. Best HVAC video is now "This $3 HOME DEPOT OUTLET Heats Your Whole House..." (20K). |
| 11 | Historia Prime | 29.4% → 24.0%: stays | The water filter is out. "Vikings Beat Winter Without Fire — The Ancient Floor Hack..." (338K), "The Overnight Warmth Rule..." (146K) and "Salt + Aluminum Foil = Free Heat Forever" (84K) are in. |
| 71 | WiseMoney | 28.9% → 23.2%: stays | Rests on "This $8 Trick Cuts Your Electricity Bill in Half" (332K). Without it the share is 9.6%. |
| 2 | Elias Yoder | 20.6% → 20.4%: stays | Rests on "The $4 Amish Fix for a Deadly Hot House" (1.9M). Without it the share is 10.6%. |

- **Entered: none.** The highest of the 13 dropped channels is Silas Mercer at 15.7% (17% before). The "Woodpile Dangers" copy and "Firewood Myth" titles are out.
- **Other borderline passes** (share; share without the single biggest HVAC title): Ray Sutter 25.4% (8.5%), Frugal Frannie 26.8% (10.1%), Caleb Greer 27.8% (4.5%), Patina 26.3% (7.1%), Survival Blueprint 27.4% (0.3%), Sylvie Mercer 30.5% (22.0%).

**The checks asked for:**

- **Eli Forgotten Ways:** best HVAC video is now "Why Did We Stop Using Ammonia To Cool Our Homes?" (87K). Share 39.7% → 61.5%.
- **TheUnknownMarks:** best HVAC video is now "This $4 Can of Crisco Heats a Room for 45 Days — Zero Electricity, Zero Gas" (74K). Share 42.2% → 98.4%.
- **"5 Woodpile Dangers..." (`BlHC-momweM`) no longer counts,** which agrees with `top_review.py`:
  - Harlan Sawyer's share is now 60.9% (78.1% before);
  - his best HVAC video is now "5 Woods That Set Chimneys on Fire..." (133K; chimney fires from stove burning are in);
  - takeoff 15.1 is HVAC "no" and 15.2 is HVAC "yes".

**Other best-HVAC changes:**

- Hidden Systems: "The $12 Norwegian Stove That Heats a House for 18 Hours on One Log" (347K).
- Elias Mercer: "Old-Timers Never Heated the House When the Power Died..." (160K).
- Backyard Low Tech: "A Box Fan in Your Attic Hatch Moves More Air Than Your AC Does" (89K).
- Builds With Eli Yoder: "Stop Running Your AC This Summer. Build This $40 Underground Pipe..." (727K). This replaces the alternator video; the share is 45.2%, down from 75.9%.
- Forgotten Materials: "Americans Forgot This Old Wood Stove Trick..." (120K). This replaces the splitting video; the share is 58.7%, down from 95.0%.

**Takeoff "HVAC" column: 39 → 42 of the 75 top-25 takeoff videos.**

- Now HVAC:
  - Why Am I Green, "EMERGENCY HEAT, Light & Cooking for 4 Months? Crisco Candle" (1.3M);
  - JustintimeHVAC's two service-call videos;
  - Passive House Technology's 1,000-gallon heat tank;
  - Harlan Sawyer 15.2.
- Now not HVAC: Historia Prime 11.1 (the water filter) and Harlan Sawyer 15.1.

**Top 25 lane split** (the top 25 is by score, so it is unchanged):

| Lane | All 25 | Well above |
|---|---:|---:|
| off-grid | 11 | 7 |
| outage | 5 | 4 |
| HVAC repair | 4 | 4 |
| brand verdicts | 1 | 1 |
| other (3 mixed, 1 bills) | 4 | 3 |

19 of the top 25 are well above (was 20). Of the 58 well above: off-grid 26 (was 28), HVAC repair 13, outage 12, bills 4, mixed 2, brand verdicts 1.

### Drafted summary lines for `new-channels.md` (not applied)

- "**58 of them are "well above" the median new channel of their tier** (A 32, B 10, C 16; definition below). 71 pass the score rule, but 13 of those have under 20% of their views on HVAC titles and are not counted (fix 4.1; round 6 hand read of every title of 103 channels, `data/raw/new-channels-handread-2026-10-26.csv`)."
- "Of the top 25, 11 are off-grid / old-ways / free-heat channels, 5 outage and winter-prep channels, 4 HVAC repair channels, 1 brand-verdict channel (HVAC Exposed), 1 frugal-bills channel and 3 mixed. ... 6 of the top 25 rank on score but are not well above, because under 20% of their views are on HVAC titles: Passive House Technology (#7), Elias Homestead (#13), Silas Mercer (#14), Forgotten American Survival (#17), The Passive House Files (#18) and Walter's Tool Talk (#22)."
- Lanes table, "well above" column: off-grid 26, HVAC repair 13, outage 12, bills 4, mixed 2, brand verdicts 1 (58).
- Takeoff formats: "42 of the 75 takeoff videos have HVAC titles (hand read; 39 by the rule)".
- The "Biggest by HVAC-title views" bullet uses the rule. By the hand read: Unknowns Lab 101 18.4M, Why Am I Green 8.2M, Wild Line 7.8M, Eli Yoder Secrets 6.6M, Ray Dutton's Garage 6.4M, Elias Yoder 4.0M.
- The dropped table moves The Passive House Files and Grain & Gravity in. The Hidden Systems and Elias Mercer best-HVAC cells change. Harlan Sawyer's takeoff 15.1 and 15.2 HVAC cells change.

### Cautions

- Every mark is my reading. Under working rule 3 a second helper should re-check a sample of the hand-read file before this goes to the operator, especially:
  - the 160 round 4 y labels I overrode;
  - WiseMoney's $8 trick;
  - Elias Yoder's Hot House video.
- The bill line (trick y / device n) and the firewood line (burning y / handling n) are judgment calls.
- Moving either line would change WiseMoney, and possibly Historia Prime and Forgotten Materials, but no other well-above call.
- Spanish titles are out by the guide. That keeps Repara Fácil USA at 83%, where the earlier check estimated about 95% with them counted.
