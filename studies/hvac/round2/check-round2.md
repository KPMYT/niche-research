# HVAC round 2: the check (2026-10-24)

The second-helper check that `CLAUDE.md` working rule 3 and `RESEARCH-BRIEF.md` section 4 (step 6) ask for. Written by the round 2 checker on 2026-10-24, pulls 08:20-08:45 UTC. I re-pulled every figure myself from the original sources. I did not reuse the helpers' numbers, and I did not edit their files. Nothing has been committed or pushed.

**Sources** (every one loaded directly, logged out; web search used: 0):
- YouTube innertube `/next` (`data/tools/vid_next_batch.py`): exact views, upload date and owner.
- YouTube oEmbed: the original title, before any auto-translation.
- NexLev `youtube_video_details`: `lengthSeconds` and `publishDate`.
- YouTube About panels and Videos tabs (`about_batch.py`, `yt_water1.py about`, `yt_allsorts.py`).
- YouTube search (the `search()` function of `sweep_round2.py`, run through my `data/tools/check_round2_search.py`).
- Thumbnails (`i.ytimg.com/vi/<id>/hqdefault.jpg`), downloaded and looked at by me on contact sheets.

**Raw pulls:** `studies/hvac/data/raw/check-round2-2026-10-24.json`. **New scripts:** `data/tools/check_round2_search.py` (re-runs stored searches and compares them) and `data/tools/check_round2_mult.py` (recomputes a channel multiple from a tab pull). My scratch work is in the scratchpad folder `chk-r2/`.

**Samples** (Python `random`; the exact calls are in the raw file under `sampling`):

| File | Sample |
|---|---|
| `nexlev-channels.md` | `random.seed(24)`, 12 of the 164 table rows. **6 of these 12 are the same rows the helper used for its own self-check** (same seed), so I added 6 more with `random.seed(124)` (excluding those 12). 18 rows in all. |
| `old-house-heat.md` | `random.seed(24)`, 10 of the 79 video rows in sections 3-5. Re-ran 2 keywords (seed 24 over the 48), and recomputed 1 channel multiple. |
| `keyword-sweep.md` + `sweep-videos-2026-10-24.csv` | `random.seed(24)`, 20 CSV rows. Re-ran 4 PRIORITY searches, one per sort (seed 24 over the 150), plus one extra `month` search. Checked 5 table rows (`random.seed(124)`) against `priority.jsonl`. |
| `formats.md` | `random.seed(26)`, 60 CSV rows. I tagged them **before** opening any stored tag (my tags were saved at 08:22 UTC, then compared). Recomputed 12 reported figures from the CSV. |

---

## Summary

| File | Checked | Mismatches that matter | Error rate | Verdict |
|---|---|---|---|---|
| `nexlev-channels.md` | 18 channels, 198 field checks, 90 thumbnails viewed | 3 wrong types, 1 wrong example video, 1 example view count 5.9% low | 5 of 198 fields (2.5%); **4 of 18 rows (22%)** | **Fix before use.** The About figures are all correct. But the type reading, made from **one** thumbnail per channel, is wrong for 3 of the 7 "faceless, real footage" channels I checked: all 3 are on camera. |
| `old-house-heat.md` | 10 videos, 60 field checks; 2 searches re-run; 1 multiple recomputed | none in the sample; 3 problems found outside it | 0 of 60 | **Sound.** Needs 3 small text fixes. One on-topic video was wrongly left out (`z80WspC4Nmg`, 2,050,577 views; it would be the #1 US video). |
| `keyword-sweep.md` + CSV | 20 videos, 120 field checks; 5 searches re-run; 5 table rows (35 cells) | 1 non-English video kept | 1 of 120 (0.8%) | **Sound.** The English rule lets through Hindi titles that carry an English keyword tail. |
| `formats.md` | 60 titles hand-tagged blind; 12 figures recomputed | **agreement 38 of 60 (63%)**; 25 of 38 (66%) on HVAC-word titles; 8 clear rule errors | 22 of 60 disagree | **Use with care.** The counts and medians compute correctly. But the rule tags agree with a careful reader less often than the helper's 74% (37 of 50), and the "3 biggest" examples include obvious mis-tags. |

### Every mismatch that matters

1. **`nexlev-channels.md` row 24, Adrian Garcia (`@ReliableHVACR`): wrong type.** The file says "faceless, real footage". The channel is **on camera**: Adrian's face is on "Best Apps for HVAC Business Owners in 2026" (`25krU2a8BNk`), and the About text says "I'm Adrian, owner of Reliable Kitchen Services", with a weekly podcast.
2. **Same row: wrong example video.** The example is "VETO Super Store Exclusive | SP-MD Blackout First Look (FINAL)" (`wLrB8I0At5A`, 12,405 views), which is a **tool-bag video**. "Blackout" (the bag's colour) matched the outage word in `r2_example.py`'s `STRICT` pattern. The CSV also says the example came from the "Videos tab (popular)", but that channel's stored Popular list is identical to its Latest list: the chip did not load. The same is true for **6 of the 162 rows** labelled "popular": Forever Tech English, Zach Of All Trades, WW HVAC, Adrian Garcia, Stay Ready. Urban Survival., and Drewdriskle.
3. **Row 53, Stephen Shares HVAC Tips at Goettl: wrong type.** The file says "faceless, real footage". He is **on camera**: his face, in a uniform with a "Stephen" name patch, is on 3 of 5 recent thumbnails.
4. **Row 17, HVACTIME: wrong type.** The file says "faceless, real footage". The channel is **on camera**: the same bearded presenter ("Chiller Academy") is on 4 of 5 recent thumbnails.
   - *Why items 1, 3 and 4 happened:* the method typed each channel from its single example thumbnail ("one example thumbnail each plus the description"). `labels.md` section 5 asks for "no face in 3 recent videos". So the table's split of 39 faceless-real-footage channels against 27 on camera is probably tilted toward faceless.
5. **Row 2, Creative inventions LMTN: example views 5.9% low.** The file has 14,000,000; `/next` gives 14,876,685 for "Millions of people do not know this knowledge! 3 in 1 waste oil heater!" (`UawMGmg87ho`). The cause is that example views are the Videos tab's rounded text ("14M"). YouTube cuts the figure down, so a count of 10K-99K or 1M+ can read up to about 9% low. **74 of the 164 examples** are in those ranges. Other rounded examples in my sample were 0.2-3.3% low (Adrian Garcia 12,000 against 12,405; Kate Sullivan 14,000 against 14,472). None of this is flagged in the file.
6. **`sweep-videos-2026-10-24.csv` row `iMyniW0gJcQ`: kept as English, but it is a Hindi video.** The title is "बिजली विभाग ने मेरे साथ किया धोखा । Wrong electricity bill problem solution । Wrong Electricity Bill" (INFORMATION TYAGI, 1,312 views). Its description is Hinglish ("Namaskar - Mai hu apka dost RAMRAJ...") and ends with "#hindi". It passes rule (a) because the Devanagari letters are under 30% of the title's letters, and the English tail is SEO.
7. **`old-house-heat.md`, outside the sample: the on-topic rule dropped "How To Remove Air From Your Heating System"** (`z80WspC4Nmg`, TheDIYGuyDOTnet, United States, 2,050,577 views, 5:24, 12y ago). Nine heat searches returned it, including three matched keywords ("how to bleed radiators", "boiler no heat" and "hot water baseboard heat"). The title has no radiator or boiler word, so the rule missed it. It would be **#6 in the top 20 and #1 in the US-listed top 20** (above askmediy's 1,625,468). The conclusions don't change: it is 12 years old and US-listed, and the old US top 20 gets older still. I checked the 40 most-viewed long-form videos the rule dropped from the matched-10 searches, and this was the only clear miss; the rest are car radiators, oil-industry and fuel videos, AC, gas furnaces, insulation, industrial boilers and off-grid heaters.
8. **`old-house-heat.md` section 3 note: a wrong date.** It says grayfurnaceman's three oil-furnace troubleshooting videos are from "(2012)". `/next` gives **2013-11-23, 2013-11-24 and 2013-11-25** (`cog7MaShR7M`, `TfPnLUz1Vh4`, `LyHy2En9iF0`). 2012 is the year the channel joined.

### Smaller points (not errors in the figures)

- **`old-house-heat.md` Files section is stale.** It says the analysis scripts are "in this helper's scratch folder ... and are not in the repo". They are now in `data/tools/oldheat/`: `build.py`, `tables.py`, `tables2.py`, `season.py`, `mult.py`, `oembed.py`, `about.py` and others.
- **The old-house heat type for Halden Row is doubtful** (my reading). The file calls it a "faceless persona, AI old man". The one thumbnail shows an AI-made frightened old man, but the channel has no named character; the description calls it "a history explainer ... Hand-drawn explanations". Under `labels.md` section 5 that is "faceless, AI images", not a persona. This weakens slightly the list of seven old-house heat personas in section 5.
- **`nexlev-channels.md`, Ivan's Survival Journal:** the example "I Tested 12 Ways to Insulate a Window" (216,000) is not the channel's most-viewed heat video. "I Tested Window Film, Bubble Wrap & Thermal Curtains — Not Even Close" has 243K, but "thermal" and "curtain" are not in the `STRICT` word list. The figures for the example itself are correct.
- **The CSV's `approx_upload_date` runs late, as the file says.** In my 20 rows the real upload was 1 to 361 days earlier (median about 200 days for the 16 shown in years). Don't use it for month-level seasonality on videos older than a year.
- **The format tables lead with off-topic videos.** For example, the "3 biggest" examples include "Masha And The Bear" (the only X), "Big & Deadly ELECTRIC EELS" and "Why Cocaine Is So Incredibly Dangerous" (news-warning), and "Why I left Linus Tech Tips" (how-to). Show the HVAC-word tables first, or show only them to the operator.

### Recommended fixes

1. **Re-type the channels in `nexlev-channels.md` with the `labels.md` rule** (3+ recent thumbnails each): at least all 39 "faceless, real footage" and 15 "faceless, graphics" rows, then recount the type and HVAC-main splits. Re-pick the Adrian Garcia example, and drop "blackout" from `STRICT` unless "power" or "outage" is also in the title. Add "thermal" and "curtain".
2. **Mark the example views as "tab-rounded"** in the `nexlev-channels.md` table and CSV, or replace them with exact `/next` counts (the 74 in the truncation ranges at least). Fix "popular" in `example_source` for the 6 channels whose Popular chip did not load.
3. **Tighten the English rule in `sweep_build.py`:** drop a title that contains a run of 3 or more Devanagari, Bengali, Arabic or other non-Latin letters, whatever the share. That catches `iMyniW0gJcQ`. Re-run, and log how many videos drop.
4. **`old-house-heat.md`:** add "heating system" (with "air", "bleed" or "remove air") to the on-topic heat rule and re-run the tables, change "(2012)" to "(November 2013)", reword the Files section, and re-read Halden Row's type.
5. **`formats.md`:** state the checker's agreement figure (63%; 66% on HVAC-word titles) beside the helper's. Fix these regex failures:
   - "Don't Want You To See" (rule 6), which is missing, so `wDTJ8bVcx84` falls through to install/DIY;
   - bare "noises" read as a symptom (a guitar pedal, `JpBImUDzw5E`);
   - "install" in "Install Van Tour" (`yhWfXqmhmzQ`);
   - "difference between A and B" (rule 2);
   - "how long will X power my furnace? let's find out" (rule 1);
   - "top N ... AC" read as the only X ("Top 5 Things AC Companies Don't Want You To Know How To Do!", `AQQH9QwC46A`, which is a list and rule 6);
   - bare "best", which tags "Best episodes cartoon" and "Bengali Best Funny Video".

   Keep treating format counts as rough, and only compare formats with big gaps.

---
## 1. `round2/nexlev-channels.md`

18 rows. Rows 99, 150, 47, 56, 43 and 50 are the helper's own self-check rows (seed 24). Rows 44, 24, 39, 73, 4 and 113 complete the seed-24 sample. Rows 81, 153, 2, 53, 17 and 118 are the extra seed-124 rows.

- **About figures** are from each channel's About panel, pulled 2026-10-24 about 08:33-08:40 UTC (Caleb Vance's panel failed in the batch and was re-pulled singly).
- **Type** is my reading from the channel's 4 most recent long-form thumbnails plus the example thumbnail, viewed on contact sheets (90 thumbnails in all).
- **Example views** are from `/next` at about 08:38 UTC, and the example length is the Videos tab overlay.

Size of differences: "drift" means the channel changed between the helper's pull and mine (a new upload, or a few views).

| Row (# in file) | Field | Claimed | Found | Source | Result |
|---|---|---|---|---|---|
| 99 HVAC Technician Sales Secrets | handle / ID | @hvactechsecrets / `UCRmPv4sdRiPqyWXqPDVWNKg` | @hvactechsecrets at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 2,240 / 207,833 / Nov 12, 2022 / 1,258 | 2.24K / 207,833 / Nov 12, 2022 / 1,258 | About panel | OK |
| | type | on camera | on camera: Scott Sylvan Bell's face in all 5 thumbnails | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | trade | trade (agree, reading) | About text + titles | OK |
| | example | "Is HVAC A Good Career - Is A Job In HVAC Worth It To Start In Today" `ngIQgDaz8n8` 7,200, 5:59 | 7,232 views, uploaded 2024-07-08, 5:59 | innertube /next + Videos tab duration | OK |
| 150 Homeowner Money | handle / ID | @HomeownerMoney / `UCunyH0ECKaODq7PMSmtTI9w` | @HomeownerMoney at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 14 / 9,351 / Sep 23, 2026 / 104 | 14 / 9,351 / Sep 23, 2026 / 104 | About panel | OK |
| | type | AI avatar | AI avatar: same AI-made unnamed man in all 5 | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "Repair or Replace Your 15-Year-Old AC? Do This Math First" `2ZCcGhN9VuU` 221, 18:04 | 221 views, uploaded 2026-09-27, 18:04 | innertube /next + Videos tab duration | OK |
| 47 OnemanHVAC | handle / ID | @Onemanhvac / `UCCfVNgkRrgMzNPrb8nOKigA` | @Onemanhvac at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 12,500 / 2,037,938 / Feb 24, 2023 / 515 | 12.5K / 2,037,938 / Feb 24, 2023 / 515 | About panel | OK |
| | type | on camera | on camera: Rolando's face in the example thumbnail; 4 recent are hands/equipment | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | trade | trade (agree, reading) | About text + titles | OK |
| | example | "MY HVAC Sunday running 5 no cool calls #hvac #bluecollar #electrical #" `7FC32AxZuPs` 69,000, 41:59 | 69,641 views, uploaded 2026-06-14, 41:59 | innertube /next + Videos tab duration | OK |
| 56 Tactical Psychology | handle / ID | @TheTacticalPsychology / `UC_CwREV-kbR5br6lKc55A8w` | @TheTacticalPsychology at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 9,550 / 257,052 / Nov 28, 2025 / 8 | 9.55K / 257,052 / Nov 28, 2025 / 8 | About panel | OK |
| | type | faceless, graphics | faceless (AI-style illustrations): sketch-style AI illustrations, different characters each time | thumbnails viewed (4 recent long-form + example) | OK (sub-type close call: graphics vs AI images) |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "Stop Heating the Air — Do This Instead (Physics)" `aPyqmS_eqRk` 167,000, 6:23 | 167,903 views, uploaded 2026-01-25, 6:23 | innertube /next + Videos tab duration | OK |
| 43 Tim & Kat's Green Walk | handle / ID | @TimAndKatsGreenWalk / `UCxT6jy59i_38H3Zy04VXzbg` | @TimAndKatsGreenWalk at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 15,900 / 2,232,997 / Jul 31, 2022 / 180 | 15.9K / 2,232,997 / Jul 31, 2022 / 181 | About panel | OK (drift: new upload) |
| | type | on camera | on camera: Tim's face in 3 of 5 | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "A tour of our air-to-air heat pump system - heating AND cooling" `PIgrN9uJfHY` 62,000, 23:53 | 62,464 views, uploaded 2022-12-03, 23:53 | innertube /next + Videos tab duration | OK |
| 50 Lost Methods Archive | handle / ID | @LostMethodsArchive / `UCg8siJ7AyKyCyNJiWvSY_UA` | @LostMethodsArchive at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 11,600 / 440,819 / Mar 20, 2026 / 110 | 11.6K / 440,819 / Mar 20, 2026 / 110 | About panel | OK |
| | type | faceless, AI images | faceless, AI images: AI scenes; one AI-made man in the example only | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "This $3 Copper Trick KILLS Your Electric Bill FOREVER — Why Did Power " `40zFRH-mb-o` 258,000, 21:38 | 258,783 views, uploaded 2026-04-18, 21:38 | innertube /next + Videos tab duration | OK |
| 44 HVAC Tech Knowledgy | handle / ID | @HVACTechKnowledgy / `UCSbqV46NJaeIkQAoQmDv8Jw` | @HVACTechKnowledgy at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 15,600 / 2,974,690 / Mar 25, 2021 / 381 | 15.6K / 2,974,690 / Mar 25, 2021 / 381 | About panel | OK |
| | type | faceless, real footage | faceless, real footage: hands and equipment in all 5 | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | trade | trade (agree, reading) | About text + titles | OK |
| | example | "I wasn't going to let this nasty drain beat me!!  How to backwash a cl" `MPoPFT13MAY` 124,000, 13:00 | 124,236 views, uploaded 2021-08-02, 13:00 | innertube /next + Videos tab duration | OK |
| 24 Adrian Garcia | handle / ID | @ReliableHVACR / `UCKDkGhLRlzs1bV1tmeokcNQ` | @ReliableHVACR at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 30,400 / 5,026,567 / Sep 28, 2011 / 1,202 | 30.4K / 5,026,567 / Sep 28, 2011 / 1,202 | About panel | OK |
| | type | faceless, real footage | on camera: Adrian's face in "Best Apps for HVAC Business Owners in 2026" (`25krU2a8BNk`); About: "I'm Adrian, owner of Reliable Kitchen Services"; weekly podcast | thumbnails viewed (4 recent long-form + example) | MISMATCH (wrong type) |
| | audience | trade | trade (agree, reading) | About text + titles | OK |
| | example | "VETO Super Store Exclusive / SP-MD Blackout First Look (FINAL)" `wLrB8I0At5A` 12,000, 18:25 | 12,405 views, uploaded 2026-08-15, 18:25 | innertube /next + Videos tab duration | MISMATCH (not a heating/cooling video: "Blackout" is the tool-bag colour; source says Popular tab but that chip returned the Latest list) |
| 39 HVAC Training 101 | handle / ID | @HVACTraining101 / `UCWhFqsrrNfGWQnXSAVEAaZg` | @HVACTraining101 at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 17,100 / 6,682,860 / Dec 27, 2019 / 302 | 17.1K / 6,682,860 / Dec 27, 2019 / 302 | About panel | OK |
| | type | faceless, graphics | faceless, graphics: product photos + cartoon mascot logo in all 5 | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | trade | trade (agree, reading) | About text + titles | OK |
| | example | "How To Recharge a Window Air Conditioner ⚡ / HVAC Training 101" `ozdPRdhYlb0` 326,000, 6:10 | 326,761 views, uploaded 2021-04-25, 6:10 | innertube /next + Videos tab duration | OK |
| 73 HVAC Service Technician Talk | handle / ID | @HVACServiceTechnicianTalk / `UCWM8W1bB5cLCVEXfGF0_vMg` | @HVACServiceTechnicianTalk at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 5,090 / 1,521,568 / Jan 7, 2019 / 215 | 5.09K / 1,521,568 / Jan 7, 2019 / 215 | About panel | OK |
| | type | faceless, real footage | faceless, real footage: rooftop units and text, no face in 5 | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | trade | trade (agree, reading) | About text + titles | OK |
| | example | "Is my Thermostat Broken? How to use Honeywell Pro4000 Thermostat" `21OpzMkQhlY` 48,000, 6:11 | 48,564 views, uploaded 2019-08-13, 6:11 | innertube /next + Videos tab duration | OK |
| 4 HVACR VIDEOS | handle / ID | @HVACRVIDEOS / `UC5Pnrxqqg4BLTsfsUzWw5Pw` | @HVACRVIDEOS at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 210,000 / 67,629,736 / Nov 16, 2017 / 1,269 | 210K / 67,629,736 / Nov 16, 2017 / 1,269 | About panel | OK |
| | type | faceless, real footage | faceless, real footage: equipment and text, no face in 5 | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | mixed | mixed (agree, reading) | About text + titles | OK |
| | example | "THE AC KEEPS TRIPPING THE BREAKER" `bP3GwusUtok` 533,000, 35:03 | 533,741 views, uploaded 2020-09-24, 35:03 | innertube /next + Videos tab duration | OK |
| 113 Ivan’s Survival Journal | handle / ID | @IvansSurvivalJournal / `UCJox5gru6jh_N65CnJ0JAfQ` | @IvansSurvivalJournal at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 1,050 / 451,457 / Sep 13, 2026 / 14 | 1.05K / 451,457 / Sep 13, 2026 / 14 | About panel | OK |
| | type | faceless persona | faceless persona (reading): the same older man in all 4; photoreal, AI-made not provable from thumbnails; named "Ivan" | thumbnails viewed (4 recent long-form + example) | OK (not provable) |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "I Tested 12 Ways to Insulate a Window — Only 3 Were Worth It" `aYPqvixhvXg` 216,000, 22:52 | 217,851 views, uploaded 2026-10-19, 22:52 | innertube /next + Videos tab duration | OK |
| 81 Forgotten Appalachian Skills | handle / ID | @ForgottenAppalachianSkills / `UCfzv1WtntHSfF9kdEGIVm6w` | @ForgottenAppalachianSkills at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 4,330 / 1,195,056 / Aug 5, 2026 / 35 | 4.33K / 1,195,056 / Aug 5, 2026 / 35 | About panel | OK |
| | type | faceless, AI images | faceless, AI images: AI cabin/snow scenes, hands only | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "18 Winter Methods That Kept Appalachian Cabins Warm Without Electricit" `15vA3pcgqOw` 20,000, 27:14 | 20,155 views, uploaded 2026-08-12, 27:14 | innertube /next + Videos tab duration | OK |
| 153 Caleb Vance | handle / ID | @CalebVanceWisdom / `UCSFLAggE1woOWwYAvHS3ULA` | @CalebVanceWisdom at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 9 / 5,162 / Sep 19, 2026 / 13 | 9 / 5,162 / Sep 19, 2026 / 13 | About panel | OK |
| | type | faceless persona | faceless persona: same AI-made old man in a flat cap in all 5; named persona | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "Don't Turn On Your Furnace Until You Do These 5 Things (Replacement Co" `n-Vg3MOKOkI` 91, 10:45 | 91 views, uploaded 2026-10-10, 10:45 | innertube /next + Videos tab duration | OK |
| 2 Creative inventions LMTN | handle / ID | @lmtn / `UC9l8eLzvmuj-LMTNcWQgHeA` | @lmtn at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 448,000 / 119,059,711 / Oct 18, 2021 / 247 | 448K / 119,059,711 / Oct 18, 2021 / 247 | About panel | OK |
| | type | faceless, real footage | faceless: no face in 5 (staged / AI-looking product shots) | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | mixed | mixed (agree, reading) | About text + titles | OK |
| | example | "Millions of people do not know this knowledge! 3 in 1 waste oil heater" `UawMGmg87ho` 14,000,000, 12:14 | 14,876,685 views, uploaded 2024-11-13, 12:14 | innertube /next + Videos tab duration | MISMATCH (views -5.9%) |
| 53 Stephen Shares HVAC Tips at Goettl | handle / ID | @StephenShares / `UCcrs-w2r-S3VR7pe8t9DIew` | @StephenShares at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 10,600 / 2,693,604 / Aug 22, 2013 / 65 | 10.6K / 2,693,633 / Aug 22, 2013 / 65 | About panel | OK (drift <0.01%) |
| | type | faceless, real footage | on camera: Stephen's face (uniform with "Stephen" name patch) in 3 of 5 recent thumbnails | thumbnails viewed (4 recent long-form + example) | MISMATCH (wrong type) |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "How To Test & Replace A Thermostat, Step By Step tutorial." `PCGr16IqOtY` 817,000, 6:46 | 817,700 views, uploaded 2015-07-25, 6:46 | innertube /next + Videos tab duration | OK |
| 17 HVACTIME | handle / ID | @HVACTIME / `UCRdNcv3g_4rpbNEyFopZwDg` | @HVACTIME at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 60,700 / 10,227,617 / Feb 16, 2014 / 892 | 60.7K / 10,227,617 / Feb 16, 2014 / 892 | About panel | OK |
| | type | faceless, real footage | on camera: the same bearded presenter's face in 4 of 5 ("Chiller Academy") | thumbnails viewed (4 recent long-form + example) | MISMATCH (wrong type) |
| | audience | trade | trade (agree, reading) | About text + titles | OK |
| | example | "YK Overview Centrifugal Chiller York HVAC Training" `flAMZUK3f18` 259,000, 27:47 | 259,070 views, uploaded 2021-12-21, 27:47 | innertube /next + Videos tab duration | OK |
| 118 Kate Sullivan Ready Living | handle / ID | @katesullivanreadyliving / `UClVbW933G0LhpQcqfE-2Pqg` | @katesullivanreadyliving at that ID | About panel (yt_water1.py about), 2026-10-24 08:3x UTC | OK |
| | subs / total views / joined / videos | 810 / 95,668 / Oct 1, 2026 / 11 | 811 / 95,668 / Oct 1, 2026 / 11 | About panel | OK |
| | type | faceless persona | faceless persona: same AI-made woman "Kate" in all 5 | thumbnails viewed (4 recent long-form + example) | OK |
| | audience | homeowner | homeowner (agree, reading) | About text + titles | OK |
| | example | "15 Wallmart Items Every Woman Living Alone Needs When the Furnace Dies" `p3DWnEKIUOI` 14,000, 18:42 | 14,472 views, uploaded 2026-10-10, 18:42 | innertube /next + Videos tab duration | OK |
**File 1 tally:** 198 field checks (per row: handle and ID, subs, total views, joined, videos, type, audience, and the example's title, views, length and heat/cool topic). 5 mismatches: 3 types, 1 example that is not a heat/cool video, and 1 example view count 5.9% low. All 18 handles resolve to the stated channel ID. All subscriber counts, joined dates and video counts match (one video-count change is a new upload). All total views match to within 0.01%.

---

## 2. `round2/old-house-heat.md`

### 10 sampled videos

| Row (table, #) | Field | Claimed | Found | Source | Result |
|---|---|---|---|---|---|
| sections 3-4, #7 `0vNHIvf8zzE` | title / channel | "No Heat! Burnham Boiler Pilot Won’t Stay Lit — Watch Mikey P" / Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | "No Heat! Burnham Boiler Pilot Won’t Stay Lit — Watch Mikey P" / Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | innertube /next | OK |
| | views | 24,277 | 24,286 (+0.04%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 23:11 | 23:11 (1391 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "No Heat! Burnham Boiler Pilot Won’t Stay Lit — Watch Mikey P" | oEmbed | OK |
| | age | 11mo ago | uploaded 2025-11-06 | innertube /next dateText | OK |
| faceless table `RZOnKKmE1V8` | title / channel | "Before Fans, This Octopus Furnace Heated a House by Itself" / Halden Row | "Before Fans, This Octopus Furnace Heated a House by Itself" / Halden Row | innertube /next | OK |
| | views | 48 | 48 (+0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 14:49 | 14:48 (888 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "Before Fans, This Octopus Furnace Heated a House by Itself" | oEmbed | OK |
| | age | 4w ago | uploaded 2026-09-25 | innertube /next dateText | OK |
| sections 3-4, #9 `HNnUO3-fj8Q` | title / channel | "How to Replace a Steam Radiator / Ask This Old House" / This Old House | "How to Replace a Steam Radiator / Ask This Old House" / This Old House | innertube /next | OK |
| | views | 536,527 | 536,526 (-0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 8:30 | 8:30 (510 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "How to Replace a Steam Radiator / Ask This Old House" | oEmbed | OK |
| | age | 8y ago | uploaded 2017-11-05 | innertube /next dateText | OK |
| sections 3-4, #13 `Y-8EWK1Moh0` | title / channel | "Hydronics System Components" / Tec Tube | "Hydronics System Components" / Tec Tube | innertube /next | OK |
| | views | 447,543 | 447,548 (+0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 12:31 | 12:30 (750 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "Hydronics System Components" | oEmbed | OK |
| | age | 8y ago | uploaded 2018-02-28 | innertube /next dateText | OK |
| sections 3-4, #7 `es478xgCHEw` | title / channel | "How to Repair a Leaking Boiler Relief Valve Easy DIY" / DIYeasycrafts | "How to Repair a Leaking Boiler Relief Valve Easy DIY" / DIYeasycrafts | innertube /next | OK |
| | views | 624,597 | 624,604 (+0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 7:04 | 7:03 (423 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "How to Repair a Leaking Boiler Relief Valve Easy DIY" | oEmbed | OK |
| | age | 10y ago | uploaded 2016-06-10 | innertube /next dateText | OK |
| sections 3-4, #10 `yCZqfnlBYW8` | title / channel | "Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" / Silver Cymbal | "Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" / Silver Cymbal | innertube /next | OK |
| | views | 470,689 | 470,690 (+0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 5:18 | 5:18 (318 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "Fix & Repair Stuck Circulator Pump Before Replacing NO HEAT" | oEmbed | OK |
| | age | 8y ago | uploaded 2017-12-31 | innertube /next dateText | OK |
| faceless table `FllsHYw4nKs` | title / channel | "STOP Heating Your Walls — This $0 Foil Trick Doubles Your Ra" / Walt's Workshop | "STOP Heating Your Walls — This $0 Foil Trick Doubles Your Ra" / Walt's Workshop | innertube /next | OK |
| | views | 11 | 11 (+0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 12:00 | 12:00 (720 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "STOP Heating Your Walls — This $0 Foil Trick Doubles Your Ra" | oEmbed | OK |
| | age | 8d ago | uploaded 2026-10-15 | innertube /next dateText | OK |
| sections 3-4, #12 `voS7Url50M4` | title / channel | "Remove Air from your Boiler and Heating System / How To" / Fix It With Zim | "Remove Air from your Boiler and Heating System / How To" / Fix It With Zim | innertube /next | OK |
| | views | 1,153,868 | 1,153,872 (+0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 16:25 | 16:24 (984 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "Remove Air from your Boiler and Heating System / How To" | oEmbed | OK |
| | age | 7y ago | uploaded 2019-01-12 | innertube /next dateText | OK |
| sections 3-4, #20 `LyHy2En9iF0` | title / channel | "Troubleshoot the oil furnace part 3.  Fire comes on but shut" / grayfurnaceman | "Troubleshoot the oil furnace part 3.  Fire comes on but shut" / grayfurnaceman | innertube /next | OK |
| | views | 760,474 | 760,465 (-0.00%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 8:35 | 8:35 (515 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "Troubleshoot the oil furnace part 3.  Fire comes on but shut" | oEmbed | OK |
| | age | 12y ago | uploaded 2013-11-25 | innertube /next dateText | OK |
| sections 3-4, #3 `WfXTAcRNPzk` | title / channel | "This New Heat Pump Could Finish Boilers" / Heatable | "This New Heat Pump Could Finish Boilers" / Heatable | innertube /next | OK |
| | views | 260,426 | 260,519 (+0.04%) | innertube /next, 08:27 UTC | OK |
| | length >= 5:00 | 17:23 | 17:22 (1042 s) | NexLev youtube_video_details | OK |
| | English original title | yes | "This New Heat Pump Could Finish Boilers" | oEmbed | OK |
| | age | 1mo ago | uploaded 2026-09-03 | innertube /next dateText | OK |
All 10 match on title, channel, views (within 0.04%), length class, English and upload age. The "/" in two titles is the file's stand-in for "|" inside a table, not an error. Lengths differ by up to 1 second (the search page rounds).

**Type readings in the sample** (thumbnails viewed): Walt's Workshop, "faceless persona, AI old man in flannel": **OK** (a named "Walt", an AI old man, and a first-person description). Halden Row, "faceless persona, AI old man": **doubtful** (the thumbnail is an AI old man, but there is no named character, and the description says "history explainer ... Hand-drawn explanations"; see the summary).

### 2 keywords re-run (`check_round2_search.py`, same `search()`, 2 pages, `hl=en&gl=US`)

| Keyword / sort | Stored pull | My pull | Rows stored / mine | Same videos | Same top 10 | Long-form stored / mine / both | Result |
|---|---|---|---|---|---|---|---|
| steam radiator not getting hot / relevance | 06:58:48Z | 08:28:35Z | 21 / 21 | 12 | 7 of 10 | 13 / 14 / 7 | OK for a relevance sort, but less stable: #2-#3 changed ("Steam Heating Systems Basics hvacr" 621,207 and "Radiator NOT Heating Up? Expert DIY Fixes" 1,246,905 dropped out of my top 5). View counts of the shared videos agree (for example `9Bgq0Bhf1kI` 30,501 against 30,508). |
| hot water baseboard heat / views | 07:02:07Z | 08:28:37Z | 20 / 20 | 20 | 10 of 10 | 14 / 14 / 14 | OK, same list in the same order. Top: "How Amish Heat Their Living Room Without Gas/Electricity" 2,533,993 both times. |

Reading: view-count sorts reproduce exactly an hour later. Relevance moves a lot between pulls, so any per-keyword relevance count is a snapshot.

### 1 channel multiple recomputed

Boiler Room Detective (`UCBcvJZZwIKcm6i0UsBX2LBA`). I pulled the Videos tab again with `yt_allsorts.py` (6 pages; Latest 180 rows) and recomputed with `check_round2_mult.py`.

| Field | Claimed (section 7 and raw JSON) | Found | Result |
|---|---|---|---|
| Baseline rule | long-form uploads in the last 12 months, Latest tab | same rule: dur >= 5:00, age below "1y" | OK |
| Baseline n | 38 | 38 (of 54 uploads under 1 year) | OK |
| Baseline median | 478 | 478 | OK |
| "How to set & adjust steam boiler pressure controls" (`3RT5IGboBCM`) | 44K, 92.05x | 44,000 (tab "44K"), 3y ago, 6:28: 44,000 / 478 = **92.05x** | OK |

**File 2 tally:** 60 field checks in the sample, 0 mismatches. Searches: 1 of 2 identical; the relevance sort moved, which is expected. Multiple: exact. Outside the sample: 1 wrong video exclusion, 1 wrong year in a note, 1 stale Files section, 1 doubtful type (all in the summary).

---

## 3. `round2/keyword-sweep.md` and `data/raw/sweep-videos-2026-10-24.csv`

### 20 sampled videos

Views and dates are from `/next`, 08:23 UTC, and lengths from NexLev. The CSV title equals the oEmbed title in all 20. 7 of the 20 are off-topic (rows 5, 7, 11, 14, 16, 17 and 19): two car thermostats, two car filters, a metal-melting furnace, Windows error reporting and Furnace Creek. That is expected: the CSV is every long-form English result, and the HVAC-word cut is separate.

| Row | Video | Field | Claimed (CSV) | Found | Source | Result |
|---|---|---|---|---|---|---|
| 1 | `lHEf_gY9ifU` | exists / title / channel | "HVAC Millionaire: Huntington Beach Interview Series #1" / HVACmillionaire | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 488 | 488 (+0.00%) | /next | OK |
| | | length class | 691 s (long) | 690 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2023-10-25 (3y ago) | 2023-02-13 | /next | OK (inside the stated one-unit window) |
| 2 | `13iswBoGYKY` | exists / title / channel | "Part 2 - Vapor Barrier Bubble Foil Insulation Is JUNK For Me" / BlueTex Insulation | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 36,183 | 36,183 (+0.00%) | /next | OK |
| | | length class | 371 s (long) | 370 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2024-10-24 (2y ago) | 2023-10-29 | /next | OK (inside the stated one-unit window) |
| 3 | `RJpw3rlKkP8` | exists / title / channel | "No Cool Call. Outdoor Unit Keeps Tripping the Breaker EP99" / Nighthawk HVAC | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 5,429 | 5,430 (+0.02%) | /next | OK |
| | | length class | 549 s (long) | 548 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2022-10-24 (4y ago) | 2022-09-18 | /next | OK (inside the stated one-unit window) |
| 4 | `mxEGafgwjQw` | exists / title / channel | "How to Install Google Nest Thermostat Step - By - Step Guide" / Tech Talk | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 193,905 | 193,906 (+0.00%) | /next | OK |
| | | length class | 869 s (long) | 868 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2021-10-24 (5y ago) | 2021-09-14 | /next | OK (inside the stated one-unit window) |
| 5 | `9IxovryIb4E` | exists / title / channel | "Watch This BEFORE You Buy A Melting Furnace!" / Lakehousebeach | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 137,235 | 137,246 (+0.01%) | /next | OK |
| | | length class | 929 s (long) | 928 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2024-10-24 (2y ago) | 2023-11-14 | /next | OK (inside the stated one-unit window) |
| 6 | `TtjddFyfM4M` | exists / title / channel | "HOW TO FIRE UP & USE YOUR WOOD COOK-STOVE - HOMESTEADING FAM" / Homesteading Family | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 224,563 | 224,553 (-0.00%) | /next | OK |
| | | length class | 1084 s (long) | 1084 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2020-10-24 (6y ago) | 2020-02-15 | /next | OK (inside the stated one-unit window) |
| 7 | `eA6YAOX1WOM` | exists / title / channel | "Toyota/Lexus V6 thermostat replacement. (3MZ-FE engine)" / Helping Hand Auto Repair | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 172,028 | 172,032 (+0.00%) | /next | OK |
| | | length class | 1748 s (long) | 1747 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2020-10-24 (6y ago) | 2020-06-13 | /next | OK (inside the stated one-unit window) |
| 8 | `I-EFnAeYMzs` | exists / title / channel | "How to change the oil filter on your boiler or furnace" / askmediy | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 220,076 | 220,076 (+0.00%) | /next | OK |
| | | length class | 605 s (long) | 605 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2008-10-24 (18y ago) | 2008-02-04 | /next | OK (inside the stated one-unit window) |
| 9 | `iMyniW0gJcQ` | exists / title / channel | "बिजली विभाग ने मेरे साथ किया धोखा । Wrong electricity bill p" / INFORMATION TYAGI | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 1,312 | 1,312 (+0.00%) | /next | OK |
| | | length class | 418 s (long) | 417 s | NexLev | OK |
| | | English original title | kept as English | Devanagari opening + English SEO tail | oEmbed + NexLev description | MISMATCH (not English: Hindi title, description in Hinglish, #hindi) |
| | | approx upload date | 2026-03-25 (7mo ago) | 2026-03-14 | /next | OK (inside the stated one-unit window) |
| 10 | `2mL_P0nDoIk` | exists / title / channel | "HVAC: The Effects Of Saltwater On the Condenser" / Up and Coming HVAC Johnnie | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 1,046 | 1,046 (+0.00%) | /next | OK |
| | | length class | 533 s (long) | 533 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2019-10-25 (7y ago) | 2019-04-07 | /next | OK (inside the stated one-unit window) |
| 11 | `daQ72uxjvLE` | exists / title / channel | "There's a Fifth Filter In Your Car Nobody Talks About — And " / Tom's Garage | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 557,999 | 558,650 (+0.12%) | /next | OK |
| | | length class | 916 s (long) | 916 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2026-08-25 (2mo ago) | 2026-08-19 | /next | OK (inside the stated one-unit window) |
| 12 | `USaEYuyM60o` | exists / title / channel | "Bajaj Room Heater Vs Local(Ordinary) Room Heater / Full Comp" / Electro Expert | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 586 | 586 (+0.00%) | /next | OK |
| | | length class | 336 s (long) | 336 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2023-10-25 (3y ago) | 2022-11-25 | /next | OK (inside the stated one-unit window) |
| 13 | `X_jkXpdqq28` | exists / title / channel | "This Plug-In Dehumidifier Setup Stops Mold Growth Cheaper Th" / Dean Explains | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 70 | 70 (+0.00%) | /next | OK |
| | | length class | 527 s (long) | 527 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2026-10-03 (3w ago) | 2026-10-02 | /next | OK (inside the stated one-unit window) |
| 14 | `hhhTytyvWuM` | exists / title / channel | "2018 F150 Cabin Air Filter Install" / Smackey's Garage | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 264,092 | 264,113 (+0.01%) | /next | OK |
| | | length class | 339 s (long) | 338 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2022-10-24 (4y ago) | 2022-10-06 | /next | OK (inside the stated one-unit window) |
| 15 | `DIKEN4GWMfY` | exists / title / channel | "The WORST Home Warranty Companies in 2025" / HomeMembership | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 578 | 578 (+0.00%) | /next | OK |
| | | length class | 344 s (long) | 343 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2025-10-24 (1y ago) | 2025-05-29 | /next | OK (inside the stated one-unit window) |
| 16 | `_s1ysfr4VX8` | exists / title / channel | "How to Replace Thermostat with Housing Assembly 2011-2023 Do" / TRQ | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 80,162 | 80,140 (-0.03%) | /next | OK |
| | | length class | 630 s (long) | 629 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2025-10-24 (1y ago) | 2025-04-01 | /next | OK (inside the stated one-unit window) |
| 17 | `rzxBcRbVu_o` | exists / title / channel | "How to Disable Windows Error Reporting Without Causing Probl" / Izoate | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 339 | 339 (+0.00%) | /next | OK |
| | | length class | 346 s (long) | 345 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2025-10-24 (1y ago) | 2025-03-04 | /next | OK (inside the stated one-unit window) |
| 18 | `tWmOd0l0EFI` | exists / title / channel | "Home Weatherproofing 101: Draft-Proof Your House in One Week" / Healthy Wealthy Life Hack Picks | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 33 | 33 (+0.00%) | /next | OK |
| | | length class | 452 s (long) | 452 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2026-10-10 (2w ago) | 2026-10-07 | /next | OK (inside the stated one-unit window) |
| 19 | `-Xt46GrPSAY` | exists / title / channel | "FURNACE CREEK - The Hottest Town On Earth - Why Do 136 Peopl" / From Here to There | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 4,566,268 | 4,566,317 (+0.00%) | /next | OK |
| | | length class | 3935 s (long) | 3934 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2024-10-24 (2y ago) | 2024-07-29 | /next | OK (inside the stated one-unit window) |
| 20 | `kX5oymrQFBc` | exists / title / channel | "This Outdated AC Finally Failed — Here’s the New R 454B Upgr" / Tri-Delta Mechanical | same / same (oEmbed title identical) | /next + oEmbed | OK |
| | | views | 22,453 | 22,458 (+0.02%) | /next | OK |
| | | length class | 1262 s (long) | 1262 s | NexLev | OK |
| | | English original title | kept as English | English | oEmbed + NexLev description | OK |
| | | approx upload date | 2025-10-24 (1y ago) | 2025-07-20 | /next | OK (inside the stated one-unit window) |
### Searches re-run (one per sort, plus one extra `month` search)

| Keyword / sort | Stored pull | My pull | Rows stored / mine | Same videos | Same top 10 | Long-form stored / mine / both | Result |
|---|---|---|---|---|---|---|---|
| mini split mistakes / relevance | 07:06:17Z | 08:25:34Z | 22 / 22 | 21 | 9 of 10 | 11 / 12 / 11 | OK. One new video: "Mini Split - 3 Things I Wish I Knew Before Installing" (`b67w0gEqHe8`, 1,526,472) came into #4. |
| wood stove mistakes / views | 07:12:18Z | 08:25:36Z | 21 / 21 | 21 | 10 of 10 | 19 / 19 / 19 | OK, same list. Note: the results are mostly not about wood stoves ("7 FATAL Wiring Mistakes..." 12,129,104; "Dangers of Essential Oils..." 3,525,901), so this keyword's `views` figures (n, median) describe off-topic videos. |
| heating bill / year | 07:00:08Z | 08:25:38Z | 20 / 20 | 20 | 10 of 10 | 17 / 17 / 17 | OK, same list. |
| ac filter destroying / month | 07:01:19Z | 08:25:49Z (retry) | 2 / 2 | 2 | 2 of 2 | 2 / 2 / 2 | OK. My first try at 08:25:40Z got no results page (a fetch failure; the retry 9 s later matched). |
| heating bill / month (extra) | 07:00:10Z | 08:25:51Z | 20 / 20 | 20 | 10 of 10 | 17 / 17 / 17 | OK. |

### 5 rows of the per-keyword table against `priority.jsonl`

Recomputed from the raw rows for each search:
- **kept** = length >= 5:00, has a view count, the video is in the CSV (that is, it passed the English rules), and, for `year` and `month`, the age is inside the stated window;
- **median** of those rows' view counts on that search page;
- **rises** = adjacent rows in the `views` sort where the next one has more views;
- **in win** = dated rows inside the window.

"No views" counts as 0, as `parse_views` does.

| # | Keyword | Column | Claimed | Recomputed | Result |
|---|---|---|---|---|---|
| 2 | air conditioner | relevance / views / year / month | 17 / 2,414,166; 11 / 9,356,062; 7 / 3,707,997; 7 / 110,263 | same | OK |
| | | views rises / year in win / month in win | 3/19; 20/20; 19/20 | 3/19; 20/20; 19/20 | OK |
| 16 | best portable air conditioner | relevance / views / year / month | 19 / 32,847; 16 / 2,022,724; 20 / 592,636; 15 / 15,204 | same (year median 592,635.5) | OK |
| | | rises / year win / month win | 3/19; 20/20; 16/20 | same | OK |
| 46 | electric bill | relevance / views / year / month | 13 / 253,815; 7 / 3,026,380; 14 / 1,142,596; 7 / 281,836 | same | OK |
| | | rises / year win / month win | 3/19; 20/20; 19/20 | same | OK |
| 72 | dehumidifier | relevance / views / year / month | 11 / 356,231; 11 / 946,439; 12 / 266,601; 10 / 5,722 | same (month median 5,722.5) | OK |
| | | rises / year win / month win | 4/19; 20/20; 20/20 | same | OK |
| 141 | thermostat habits | relevance / views / year / month | 19 / 257; 12 / 16,050; 14 / 2,212; 17 / 238 | same (19 once "No views" `Pzdr9_26y84` counts as 0; views median 16,050.5) | OK |
| | | rises / year win / month win | 5/19; 20/20; 19/20 | same | OK |

35 of 35 cells reproduce. (Halves are rounded down in the file; that is not an error.)

**File 3 tally:** 120 video-field checks, 1 mismatch (the Hindi video). 5 of 5 searches reproduce, and 35 of 35 table cells.

---

## 4. `round2/formats.md`

### Blind hand-tag of 60 titles (seed 26)

I tagged every title from `labels.md` section 3, going down the rules and taking the first that matches, from the title only (as the stored rules do), with "plain topic/other" when none applies. I saved my tags before reading the stored column. "Note" is my reason, or the close call.

| # | ID | Title | My tag (blind) | Stored tag | Agree? | Note |
|---|---|---|---|---|---|---|
| 1 | `sKs4mmMsgck` | "I INSTALLED ZIP SYSTEM INSULATED SHEATHING: It's a Game Changer" | install/DIY project | install/DIY project | yes | close: review ("game changer") |
| 2 | `qa3YnWhzPsw` | "#288 Raspberry Pi 4 Coolers: Which one is best? (Quickie)" | the only X | test | NO | "which one is best" |
| 3 | `XfcFTVEUvpg` | "I Tested Every Auction Draft Strategy (Here's What Wins)" | test | test | yes |  |
| 4 | `yhWfXqmhmzQ` | "Ultimate HVAC Service/Install Van Tour!!" | plain topic/other | install/DIY project | NO |  |
| 5 | `ndZHpxiPVuU` | "No Heat ⚡️Electric Furnace. Replacing Heater Kit!" | symptom-fix | symptom-fix | yes |  |
| 6 | `ctcNkuYbumg` | "Robinson R22 Preflight: Tips from Robinson’s Chief Pilot" | how-to | how-to | yes | close: other |
| 7 | `fGH7l8r3vKo` | "UK Warm Homes Plan Explained: Heat Pump Costs, Grants & Real Savings in 202" | news-warning | explainer | NO | grants/plan; close: explainer |
| 8 | `Pt5qRltu8MI` | "THE LOUDEST TRIO IN MM2 😂 (Funny Moments)" | plain topic/other | plain topic/other | yes |  |
| 9 | `i6lebY2bNC0` | "Don’t throw away your old fan stator – it’s perfect for this project!" | cheap hack | plain topic/other | NO | close: before you do X |
| 10 | `jz4hbU7nPcQ` | "ECOPOOLTECH Ultra Inverter Pool Heat Pump Review – Heating & Cooling, Best " | the only X | the only X | yes | "Best Pool Heater 2026?" before review |
| 11 | `6niKkbt_KfA` | "Iceland-Waterfalls,Rivers,Streams,Geothermal phenomena,sand storm,Primordia" | plain topic/other | plain topic/other | yes |  |
| 12 | `bulasTEc11s` | "Carrier Vs Goodman: The Brutal Truth About AC!" | X vs Y | X vs Y | yes |  |
| 13 | `UVWzoZg0T1w` | "McCarthy, GOP Reps slam Biden's executive orders on oil and gas" | news-warning | plain topic/other | NO | close: other |
| 14 | `n1jzBh7vsUk` | "Yahama Mt 15 v2 radiator guard installation 🔥🔥" | install/DIY project | install/DIY project | yes | close: how-to |
| 15 | `gz9hvCHvo4Y` | "TBP Converting / 3M Attaching Insulation" | plain topic/other | install/DIY project | NO |  |
| 16 | `aM8xtcn5wnE` | "Bring Me The Horizon live @ Furnace Fest Birmingham, AL 10/11/26 (Partial S" | plain topic/other | plain topic/other | yes |  |
| 17 | `5abHgZp11C4` | "Insulating Timber Floors In An Old House" | install/DIY project | how-to | NO | close: how-to |
| 18 | `b3PHcHfqEsQ` | "Chimney Pipe Installation for Wood Stove through roof" | install/DIY project | install/DIY project | yes |  |
| 19 | `JpBImUDzw5E` | "AC Noises Respira Shimmer Reverb + Tremolo // Demo" | review | symptom-fix | NO | demo of one product |
| 20 | `weHjQ_Y6594` | "Common Causes of a Cycling Well Pump" | symptom-fix | plain topic/other | NO | close: explainer |
| 21 | `Map8n_rc0-A` | "Motorcycle Tech Tips: Replacing Radiators and Coolant" | how-to | how-to | yes |  |
| 22 | `0fxiSvSsDVQ` | "Portable AC vs Window AC – Which Cools Better? – Full Side-by-Side Test" | test | test | yes | side-by-side test; rule 1 before vs |
| 23 | `JLbuShjUiwo` | "How Much CO2 is Healthy in my Home? Carbon Dioxide Targets Planned and Prov" | explainer | explainer | yes |  |
| 24 | `hNZm2dTDnSE` | "HVAC OVERTIME #290" | plain topic/other | plain topic/other | yes |  |
| 25 | `QhXMKA9hli0` | "Best Air Cooler Buying Guide 2026⚡ Save Money, Get Better Cooling!" | the only X | the only X | yes |  |
| 26 | `4_FYrDuVyhI` | "I Tested 20+ Fans: Why The Dreo 712S Is My New Favorite!" | test | test | yes |  |
| 27 | `Hpn8wekIOK0` | "🌧️ 2 Days Solo Camping in Heavy Rain with My Dog / Cozy Tent, Wood Stove & " | story | plain topic/other | NO |  |
| 28 | `Ny4-YOAz2Eg` | "Watch This Before You Buy a Home Warranty" | before you do X | before you do X | yes |  |
| 29 | `DslCH4b0ibA` | "DIY Convection Woodstove (Plans Available)" | install/DIY project | how-to | NO |  |
| 30 | `z0vWv2Jwn3A` | "2004 Honda Element/CRV Thermostat Replacement" | how-to | how-to | yes |  |
| 31 | `hxnfRiq23Zg` | "HVAC HACK SCAM IN MY AREA TAKING ADVANTAGE OF OLDER COUPLE EXPOSED" | Y doesn't want you to know | Y doesn't want you to know | yes | close: story |
| 32 | `gfD1l4lOEQs` | "This Is How I Troubleshoot with Confidence After 16 Years in HVAC" | how-to | how-to | yes |  |
| 33 | `qutUW83hLUQ` | "How to Remove Daikin MiniSplit Blower Wheel" | how-to | how-to | yes |  |
| 34 | `yzzzir74fQw` | "New Home, Old Boiler. £5/Day WASTED" | story | plain topic/other | NO |  |
| 35 | `WGk9RgmoqJA` | "Buying a Laundromat? The Gas Bill Shows What the Dryers Really Make" | explainer | plain topic/other | NO | low confidence |
| 36 | `CBSUCMyvZ0g` | "The Truth about Home Warranty Companies - Contractor's Perspective" | Y doesn't want you to know | Y doesn't want you to know | yes | "the truth about" |
| 37 | `J4bKiv0uiE4` | "How to use - Philips EVO home mechanical ventilation" | how-to | how-to | yes |  |
| 38 | `oKgDiJoV94I` | "5 HVAC Installation Mistakes!" | mistakes | mistakes | yes |  |
| 39 | `BFpRbYMdxBw` | "Air conditioner capacitor troubleshooting and replacement." | how-to | how-to | yes | close: symptom-fix |
| 40 | `Ylgb8FFMgd4` | "Electric generator (A.C. & D.C.) / Magnetic effects of current / Khan Acade" | explainer | plain topic/other | NO |  |
| 41 | `Yb2D4QkIKFU` | "Hot vs Cold Secret Room Under the Bed! 24 Hours Challenge!" | test | X vs Y | NO | 24 hours challenge; rule 1 before vs |
| 42 | `wPVdGDiGRf0` | "Is There a "Wemby Stopper" In the 2026 NBA Draft? / The Hoops HQ Show with " | plain topic/other | explainer | NO |  |
| 43 | `gcUj_hyhHI0` | "DIY Air Duct Cleaning Tools, part 5 - Aggressive Wire Brush for Drills - To" | how-to | how-to | yes |  |
| 44 | `wDTJ8bVcx84` | "Big HVAC Brands Don’t Want You To See This ACiQ Install" | Y doesn't want you to know | install/DIY project | NO |  |
| 45 | `megF-PvJgfY` | "3 DIY Spray Foam Skull Pumpkins (Last One Got Weird)" | install/DIY project | how-to | NO |  |
| 46 | `D01GZX1QuoQ` | "How to Get Spray-Quality Baseboards With a Brush" | how-to | how-to | yes |  |
| 47 | `9RF4YFBzPCI` | "Florida HVAC Exam Preparation - Business And Finance Exam // Adam FUSE MAN" | plain topic/other | plain topic/other | yes |  |
| 48 | `GoThAlOvSts` | "Thermostat Wiring to a Furnace and AC Unit!  Color Code, How it Works, Diag" | explainer | how-to | NO |  |
| 49 | `NrFcYZ2xnBY` | "Snatch It! Quickly change a thermostatic radiator valve - TRV. No need to d" | how-to | how-to | yes | close: cheap hack |
| 50 | `0Is5SY3x3x0` | "How to Clean an Oven FAST with NO Harsh Chemicals" | how-to | how-to | yes |  |
| 51 | `AFfdctC4oJg` | "How Much Does a Ductless Mini Split Cost in 2025?" | explainer | explainer | yes |  |
| 52 | `sU9pR7Y_gXs` | "Full Review Lasko Motion X Portable Room Heater   COSTCO" | review | review | yes |  |
| 53 | `CuKvxlyr5ow` | "YAMAHA R1 RN12 Air Filter Replacement" | how-to | how-to | yes |  |
| 54 | `Tk1sAmQFsdI` | "How I Repaired My Refrigerant Leak and Recharge AC On My 2000 F-150" | symptom-fix | symptom-fix | yes | close: how-to |
| 55 | `yjEEdKlZn0g` | "Difference Between Faced and Unfaced Insulation & How To Install It (Philli" | X vs Y | install/DIY project | NO |  |
| 56 | `VF33p73KEgs` | "How To: Replace The Thermostat And Reseal The Housing On A 2002-2009 Lexus " | how-to | how-to | yes |  |
| 57 | `jXKA1kprp_c` | "Top 50 HVAC Design Engineer Interview Questions and Professional Answers fo" | plain topic/other | explainer | NO |  |
| 58 | `5s2ZTU6BZNE` | "How to do a Quick Blower Wheel Cleaning" | how-to | how-to | yes |  |
| 59 | `ERnMte2ZJQY` | "How Long Will The JACKERY EXPLORER 1500 PRO Power My Furnace? Lets Find Out" | test | explainer | NO |  |
| 60 | `m0WHl2pUQwQ` | "HVAC Insights with Doug Widenmann: Daikin's Journey to the Top" | plain topic/other | plain topic/other | yes |  |
**Agreement: 38 of 60 (63%).** On the 38 titles that pass the HVAC-word cut: 25 of 38 (66%). The helper's own out-of-sample figure was 37 of 50 (74%).

**Confusion pairs** (stored tag -> my tag, count):

| Stored -> mine | n | Titles |
|---|---:|---|
| how-to -> install/DIY project | 3 | `5abHgZp11C4` "Insulating Timber Floors In An Old House" (close); `DslCH4b0ibA` "DIY Convection Woodstove (Plans Available)"; `megF-PvJgfY` "3 DIY Spray Foam Skull Pumpkins" |
| install/DIY project -> plain topic/other | 2 | `yhWfXqmhmzQ` "Ultimate HVAC Service/Install Van Tour!!"; `gz9hvCHvo4Y` "TBP Converting / 3M Attaching Insulation" |
| plain topic/other -> story | 2 | `Hpn8wekIOK0` "2 Days Solo Camping in Heavy Rain with My Dog..."; `yzzzir74fQw` "New Home, Old Boiler. £5/Day WASTED" |
| plain topic/other -> explainer | 2 | `WGk9RgmoqJA` "Buying a Laundromat? The Gas Bill Shows What the Dryers Really Make" (close); `Ylgb8FFMgd4` "Electric generator (A.C. & D.C.) / Magnetic effects of current / Khan Academy" |
| explainer -> plain topic/other | 2 | `wPVdGDiGRf0` "Is There a "Wemby Stopper" In the 2026 NBA Draft?"; `jXKA1kprp_c` "Top 50 HVAC Design Engineer Interview Questions..." |
| install/DIY project -> Y doesn't want you to know | 1 | `wDTJ8bVcx84` "Big HVAC Brands Don't Want You To See This ACiQ Install" (rule 6 comes before rule 12) |
| install/DIY project -> X vs Y | 1 | `yjEEdKlZn0g` "Difference Between Faced and Unfaced Insulation & How To Install It" (two named options; rule 2 first) |
| explainer -> test | 1 | `ERnMte2ZJQY` "How Long Will The JACKERY EXPLORER 1500 PRO Power My Furnace? Lets Find Out" (a stated trial) |
| symptom-fix -> review | 1 | `JpBImUDzw5E` "AC Noises Respira Shimmer Reverb + Tremolo // Demo" (a guitar pedal demo; "noises" read as a symptom) |
| X vs Y -> test | 1 | `Yb2D4QkIKFU` "Hot vs Cold Secret Room Under the Bed! 24 Hours Challenge!" (close: "24 hours" trial against "vs") |
| test -> the only X | 1 | `qa3YnWhzPsw` "Raspberry Pi 4 Coolers: Which one is best?" (close; the rule deliberately reads "which one is best" as a test) |
| explainer -> news-warning | 1 | `fGH7l8r3vKo` "UK Warm Homes Plan Explained: Heat Pump Costs, Grants..." (close: a new government grant scheme; rule 9 comes before rule 14) |
| plain topic/other -> news-warning | 1 | `UVWzoZg0T1w` "McCarthy, GOP Reps slam Biden's executive orders on oil and gas" (close) |
| plain topic/other -> cheap hack | 1 | `i6lebY2bNC0` "Don't throw away your old fan stator – it's perfect for this project!" |
| plain topic/other -> symptom-fix | 1 | `weHjQ_Y6594` "Common Causes of a Cycling Well Pump" |
| how-to -> explainer | 1 | `GoThAlOvSts` "Thermostat Wiring to a Furnace and AC Unit! Color Code, How it Works, Diagram!" (close) |

**Of the 22 disagreements, 8 are clear rule errors** (my strict reading): `wDTJ8bVcx84`, `yjEEdKlZn0g`, `ERnMte2ZJQY`, `JpBImUDzw5E`, `yhWfXqmhmzQ`, `gz9hvCHvo4Y`, `DslCH4b0ibA` and `megF-PvJgfY`. The other 14 are close calls or "no rule word" misses that a title-only rule can't easily see. Counting the close calls as agreements gives at best about 52 of 60. **A fair range for the rule's accuracy is 63-87%.** The helper's "about three titles in four" sits inside it, but the strict figure is lower.

### Reported figures recomputed from the CSV

| Figure (`formats.md`) | Claimed | Recomputed | Result |
|---|---|---|---|
| All time, all videos: n / channels / median | 25,618 / 13,708 / 33,924 | 25,618 / 13,708 (channel ID, or the name where the ID is blank) / 33,924 | OK |
| Last 12 months, all: n / median | 7,902 / 6,206 | 7,902 / 6,206.5 | OK |
| All time, install/DIY project: n / median | 2,017 / 58,390 | 2,017 / 58,390 | OK |
| Last 12 months, install/DIY project: n / median | 348 / 10,047 | 348 / 10,047 | OK |
| All time, news-warning: n / channels / median | 156 / 144 / 44,664 | 156 / 144 / 44,664.5 | OK |
| Last 12 months, news-warning: median | 9,275 | 9,275 | OK |
| All time, how-to / symptom-fix: median | 42,259 / 29,733 | 42,259 / 29,733 | OK |
| Last 12 months, how-to / symptom-fix: median | 4,959 / 3,275 | 4,959 / 3,275 | OK |
| HVAC-word, all time, all: n / channels / median | 16,270 / 8,793 / 24,330 | 16,270 / 8,793 / 24,330.5 | OK |
| HVAC-word, all time, how-to: n / channels / median | 4,028 / 2,646 / 37,902 | 4,028 / 2,646 / 37,902 | OK |

12 of 12 reproduce: the arithmetic is right, and the weak point is the tags themselves.

**File 4 tally:** 22 of 60 tags disagree (8 clearly wrong); 0 of 12 figures wrong.
