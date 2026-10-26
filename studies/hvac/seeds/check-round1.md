# HVAC round 1: checker's re-check (2026-10-23)

**By:** the round 1 checker (working rule 3; `RESEARCH-BRIEF.md` section 4, step 6). I re-pulled every figure myself from the source. I did not reuse the helpers' numbers and did not edit their files. Nothing is committed.

**When:** 2026-10-23, about 03:55 to 04:10 UTC, about 25 to 35 minutes after the helpers' pulls. Small view gains over that time are expected.

**Sources:**
- YouTube, loaded directly and logged out (hl=en, gl=US):
  - channel Videos tabs, paged through the Latest, Popular or Oldest chip
  - the About panel
  - innertube `/next`, for exact title, views, date and owner, and for the up-next lists
  - autocomplete (`suggestqueries.google.com`, `ds=yt`)
- NexLev `youtube_video_details` (`lengthSeconds`) for the edge lengths.
- Web searches used: 0.

**Tool:** `studies/hvac/data/tools/check_round1.py`. It is new and written separately from the helpers' scripts.

**Raw pulls:** `studies/hvac/data/raw/check-round1-2026-10-23.json`.

**Sampling:** Python `random.seed(23)`.
- Seeds: `random.sample(range(1,23),15)`.
- Borderline rows: `random.sample(range(1,20),3)`, drawn next from the same generator.
- Each other file: a fresh `random.seed(23)`.

**How to read "OK":**
- Views: OK when the difference is small and goes the expected way (up, since my pull is later). The difference is given.
- Titles: exact, character for character.
- Dates: exact.
- Length class: 300 s or more counts as long-form.

---

## 1. `silver-cymbal.md`

Rows drawn: seeds #1, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 19, 20, 21, 22. Borderline rows #1, 8 and 15, counted in the borderline table's own order: `sHL4lBAhklA`, `3x5t4Zvkqms`, `k8hK9duZIGo`.

### 1a. Channel-level claims

| Claim | Claimed | Found | Source | Result |
|---|---|---|---|---|
| Videos on the Videos tab | 538 | 538 (18 pages under the Latest chip) | YT Videos tab | OK |
| Shorts | 1 (`EpGDf1jp0vA`) | 1 (`EpGDf1jp0vA`) | YT Shorts tab | OK |
| Header count | 539 videos, 1.09M subs | 539 videos, 1.09M subs, joined Jun 26, 2012 | YT About | OK |
| Long-form (>= 300 s) | 321 | 321 by tab text. The only video at tab 5:00 (`JyZgGSmtCRY`, a weed-killer video) is 300 s in NexLev, so it stays in. | YT tab + NexLev | OK |
| Under 5 minutes | 217 | 217 | YT tab | OK |
| Baseline window and n | 2025-10-23 to 2026-10-23, n = 18 | 18 long-form videos dated 2025-10-31 to 2026-10-13. `TVkQ_aU2cWQ` (2025-10-22) falls 1 day outside. | YT `/next` exact dates | OK |
| Baseline median | 79,807 (mean of 78,736 and 80,878) | **79,807**: 9th = 78,736 (`VuQwtq7v0pk`), 10th = 80,878 (`iyQk6K8ABlw`) | YT `/next` exact views | OK, exact |
| All-time long-form median | 243,780 | The 161st of 321 by tab views is `l9HcFSMS6lc`, whose exact count is 243,780 | YT tab + `/next` | OK |
| Long-form at 2x or more | 195 of 321 | 195 of 321 (from rounded tab views) | YT tab | OK |
| Seed median, median multiple | 515,816; 6.46x | 515,816; 6.465x (recomputed from the file's own seed table) | arithmetic | OK |
| Multiples (all 22 seeds) | views / 79,807 | all 22 agree to within 0.01 | arithmetic | OK |

### 1b. Sampled rows

Title, date, channel and the length class matched on every sampled row, so the table below gives one line per video. It shows views and length in full. Every one of the 18 videos also passes these checks:
- **Channel:** owner Silver Cymbal, `UC67dKTEwpAhKv2oYDATwR8g`.
- **Not a Short:** it is on the Videos tab, not the Shorts tab, and NexLev gives `isShortsEligible: false` on the 8 of them checked there.
- **English:** title in English, US channel.

| Row | Video | Title exact? | Views claimed | Views found (`/next`) | Diff | Date claimed = found | Length claimed | Length found | >= 300 s | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| seed 1 | `_b6p0fkWhCY` | yes | 4,307,728 | 4,307,733 | +5 | 2018-07-20 | 8:52 | 532 s NexLev (tab 8:53) | yes | OK |
| seed 3 | `Wejop_Rjpv0` | yes (incl. the double space) | 3,087,177 | 3,087,177 | 0 | 2021-06-12 | 10:13 | 613 s NexLev | yes | OK |
| seed 4 | `o8KQu_MlpoY` | yes | 2,363,606 | 2,363,606 | 0 | 2020-06-08 | 6:09 | 369 s NexLev | yes | OK |
| seed 5 | `DSNUyxZtrmo` | yes | 1,859,343 | 1,859,476 | +133 (+0.007%) | 2023-06-23 | 7:06 | 426 s NexLev | yes | OK |
| seed 6 | `nsRHhU6q5RY` | yes | 1,454,183 | 1,454,183 | 0 | 2019-07-26 | 8:04 | 484 s NexLev (tab 8:05) | yes | OK |
| seed 8 | `5GbXgEYw5TE` | yes | 820,639 | 820,705 | +66 | 2018-02-10 | 22:18 | 1338 s NexLev | yes | OK |
| seed 9 | `leEsPGaaru8` | yes | 698,976 | 698,976 | 0 | 2022-05-17 | 6:29 | tab 6:29 | yes | OK |
| seed 10 | `BP1iDvKpNZA` | yes | 631,905 | 631,905 | 0 | 2024-01-17 | 5:30 | tab 5:31 | yes | OK |
| seed 12 | `uObGbs4sGQY` | yes | 503,681 | 503,681 | 0 | 2024-05-08 | 5:00 | **300 s** NexLev (tab 5:01) | yes, just | OK |
| seed 13 | `yCZqfnlBYW8` | yes | 470,352 | 470,352 | 0 | 2017-12-31 | 5:18 | tab 5:18 | yes | OK |
| seed 14 | `ED3bfesbE_Y` | yes | 388,617 | 388,617 | 0 | 2023-01-18 | 5:18 | tab 5:19 | yes | OK |
| seed 19 | `yZavrHJsBAw` | yes | 163,415 | 163,415 | 0 | 2023-05-17 | 7:33 | tab 7:33 | yes | OK |
| seed 20 | `S8XO4wFhrPU` | yes | 117,116 | 117,116 | 0 | 2025-04-25 | 6:06 | tab 6:06 | yes | OK |
| seed 21 | `OGVXmIZtEG8` | yes | 65,273 | 65,274 | +1 | 2026-08-06 | 5:39 | tab 5:39 | yes | OK |
| seed 22 | `cC-J0ZCUH28` | yes | 32,326 | 32,326 | 0 | 2025-08-06 | 5:01 | **301 s** NexLev (tab 5:02) | yes, just | OK |
| borderline 1 | `sHL4lBAhklA` | yes | 1,519,132 | 1,519,182 | +50 | 2026-08-30 | 5:34 (tab) | tab 5:34 | yes | OK |
| borderline 8 | `3x5t4Zvkqms` | yes | 353,981 | 353,981 | 0 | 2024-01-07 | 8:26 (tab) | tab 8:26 | yes | OK |
| borderline 15 | `k8hK9duZIGo` | yes | 123,405 | 123,405 | 0 | 2021-11-27 | 5:54 (tab) | tab 5:54 | yes | OK |

**File 1 result: 0 mismatches in 18 rows (about 110 field checks) and 11 channel-level claims.** The largest view gap is +133 (0.007%). The Videos tab shows a length 1 s longer than NexLev on 6 of the 18, as the helper noted. Only seeds #12 and #22 sit at the 300 s edge, and both pass on NexLev's exact seconds.

---

## 2. `known-channels-recheck.md` (all 8 channels)

Each handle was checked by loading the ID's About panel: its `canonicalChannelUrl` must equal the claimed handle. The video title and owner come from `/next`. The type is my own look at a contact sheet: 4 thumbnails per channel (the top one plus 3 at random from the Popular tab), and the 5 newest for John, Exposi and Vent Exposed.

| # | Channel | Field | Claimed | Found | Source | Result |
|---|---|---|---|---|---|---|
| 1 | Ray Dutton's Garage | handle ↔ ID | @RayDuttonsGarage · UCvcKEgZcY9ZgEULZouaNAOA | same | YT About | OK |
| | | subs / views / videos | 31.5K / 6,227,051 / 51 | 31.5K / 6,227,051 / 51 | YT About | OK |
| | | joined / first upload | Jul 1, 2026 / Jul 29, 2026 (`sMMZZiiD4NI`) | Jul 1, 2026 / `sMMZZiiD4NI` dated 2026-07-29 (Oldest chip, `/next`) | YT | OK |
| | | long / Shorts | 51 long / no Shorts | 51 of 51 >= 300 s | YT tab | OK |
| | | type | faceless persona, same AI-looking grey-haired man with a "RAY" patch | same man with a "RAY" patch on all 4 | thumbnails | OK |
| | | top-3 #2 | "The 5 Thermostat Habits That Wear Out Your AC Years Early", 1,126,365, Aug 18, 2026, 14:28 | same title, 1,126,383 (+18), 2026-08-18, tab 14:28; #2 on the Popular tab | YT `/next` | OK |
| 2 | HVAC Exposed | handle ↔ ID | @HVACExposed · UCZ1IwSV46bb09fMvqHn6_2A | same | YT About | OK |
| | | subs / views / videos / joined | 9.59K / 2,016,579 / 79 / Feb 27, 2026 | same | YT About | OK |
| | | long | 79 long | 79 of 79 | YT tab | OK |
| | | type | faceless "exposé"; objects, plus an older man (likely AI) on recent ones | objects on 3, an older man on 1 ("STOPS CEILING FLOODS") | thumbnails | OK |
| | | top-3 #1 | "The Only 5 HVAC Brands Worth Buying (The Lifetime List)", 577,619, Feb 28, 2026 | same, 577,619 (0), 2026-02-28 | YT `/next` | OK |
| 3 | Vent Exposed | handle ↔ ID | @VentExposed · UCTDbUAjE9Ab_wwvuV7cgtvQ | same | YT About | OK |
| | | subs / views / videos / joined | 1.93K / 696,224 / 12 / Mar 31, 2026 | same | YT About | OK |
| | | long | 11 long, 1 under 300 s | 11 + 1 | YT tab | OK |
| | | type | faceless, "object-only thumbnails" | Faceless holds. The HVAC thumbnails are object-only, but 2 of the older pest-control thumbnails ("STOP BUYING THIS" Raid, "THE $8 SECRET") show a man. | thumbnails | OK (wording) |
| | | top-3 #1 | "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)", 669,737, May 25, 2026, 8:12 | same, 669,765 (+28), 2026-05-25, tab 8:12. `/next` names no single owner, and the tab shows "Vent Exposed and 3 more", which fits the collaboration claim. | YT | OK |
| 4 | John The HVAC Guy | handle ↔ ID | @JohnTheHVACGuy · UCOyYTw-deou3ax6gvCmX2dg | same | YT About | OK |
| | | subs / videos / joined | 7.13K / 69 / Sep 30, 2020 | same | YT About | OK |
| | | total views | 986,134 | 987,611 | YT About | OK (+1,477, +0.15%, drift) |
| | | long | 69 long | 69 of 69 | YT tab | OK |
| | | type | faceless persona, a man (likely AI) in a white polo with a lapel mic on recent thumbnails; older ones object-only | 4 older Popular thumbnails: objects only. 5 newest: the same man in a white polo with a lapel mic. | thumbnails | OK |
| | | top-3 #3 | "The Only 5 HVAC Brands Worth Buying (The Lifetime List)", 102,265, Aug 31, 2026, a 2-channel collaboration with Nixon The Appliance Guy | same, 102,265 (0), 2026-08-31; the tab shows "John The HVAC Guy and Nixon The Appliance Guy" | YT | OK |
| 5 | Exposi | handle ↔ ID | @Exposerosi34 · UCQCRIhHQ__ncUxtOHiIXI4A | same | YT About | OK |
| | | subs / views / videos / joined | 2.52K / 744,853 / 43 / Jun 8, 2026 | same | YT About | OK |
| | | long | 43 long | 43 of 43 | YT tab | OK |
| | | type | faceless: hands and equipment, no face | 8 of 9 show hands and equipment only. 1 (`hu8dyLILtko`, "THE AC REPAIR BYPASS") shows a technician's face in profile. | thumbnails | OK (wording: "no face" is nearly, not strictly, true) |
| | | top-3 #2 | "This SECRET AC Trick is Only Known by 1% of HVAC Technicians (USE THEM NOW)", 196,987, Aug 9, 2026 | same, 196,990 (+3), 2026-08-09 | YT `/next` | OK |
| 6 | Hank Cole | handle ↔ ID | @HankColeUS · UC5NJ3yYhsZFkfWLJJJVoxMA | same | YT About | OK |
| | | subs / views / videos / joined | 1.37K / 246,171 / 31 / Jul 20, 2026 | same | YT About | OK |
| | | long | 31 long | 31 of 31 | YT tab | OK |
| | | type | faceless persona, the same weathered older man | same man on all 4 | thumbnails | OK |
| | | top-3 #2 | "Avoid The One AC Mistake That Costs You Hundreds And Gets You Colder Air", 25,161, Aug 19, 2026 | same, 25,161 (0), 2026-08-19 | YT `/next` | OK |
| 7 | Gus Whitaker | handle ↔ ID | @GusWhitakerr · UCLdI4EbF3WcHS_oyhjSvwDw | same | YT About | OK |
| | | subs | 822 | 824 | YT About | OK (+2, +0.2%) |
| | | views / videos / joined | 201,227 / 19 / Aug 27, 2026 | same | YT About | OK |
| | | first upload | Oct 3, 2026 | `X4wLpfiedwo`, 2026-10-03 (Oldest chip, `/next`) | YT | OK |
| | | type | faceless persona, a white-bearded older man (likely AI) | the same white-bearded man in a plaid shirt and work apron on all 4 | thumbnails | OK |
| | | top-3 #2 | "Turning Your Heat Down Is NOT Saving You Money. Do This Instead And Your Bill Drops", 78,361, Oct 12, 2026 | same, 78,415 (+54, +0.07%), 2026-10-12 | YT `/next` | OK |
| 8 | The DIY HVAC Guy | handle ↔ ID | @diyhvacguy · UC2w60mhlxFmAhoi2oSDcEng | same | YT About | OK |
| | | subs / views / videos / joined | 527K / 102,187,575 / 362 / Mar 22, 2017 | same | YT About | OK |
| | | type | on camera, a real presenter | a real man in a cap on camera | thumbnails | OK |
| | | top-3 #3 | "This Could Keep Your Family Warm During An Emergency Power Outage.", 2,744,903, Dec 2, 2022, 16:38 | same, 2,744,903 (0), 2022-12-02, tab 16:38 | YT `/next` | OK |
| | | top-3 order | from NexLev popular sort | My Popular-chip pull for this channel came back in upload order (chip not applied), so I sorted its 317 tab items by views myself. The top 3 match: 4.2M, 2.7M, 2.7M. | YT tab | OK |

**File 2 result: 0 mismatches that matter in 8 channels (about 45 field checks).**
- Drift only: Gus subs +2; John total views +0.15%; video views +0 to +54.
- Two wording nits on type (the type itself holds):
  - Vent Exposed is "object-only" only in its HVAC era; its pest-era thumbnails show a man.
  - Exposi shows a face in profile on 1 of 9 thumbnails.

---

## 3. `leads-channels.md`

### 3a. Five videos from the top-40 table

Rows drawn: 2, 6, 19, 20 and 38. The file's views are YouTube's rounded up-next text, so the test here is whether that text is a fair rounding of the exact count.

| Row | Video | Field | Claimed | Found (`/next`) | Result |
|---|---|---|---|---|---|
| 2 | `U6QPw6H_yMc` | title | "A stove that saves 50% of firewood and heats the house for 50 hours without a fire" | same | OK |
| | | channel | Bezdymne Piece | **Smokeless Stoves**, same ID `UC_eTsy7fL7l2ZXUUTiT3ShQ` (the file's own channel table notes the rename) | MISMATCH (name only, channel right) |
| | | views | 3.4M | 3,415,336 | OK (+0.5%) |
| 6 | `AQ4EYHNCDzg` | title / channel | "How To Install A Mini Split Air Conditioner – Complete Step-By-Step Guide" / Fer's Reviews | same / Fer's Reviews `UCj4ILMwnfh-fmMk6Fg1BynA` | OK |
| | | views | 663K | 663,976 | OK (+0.1%) |
| 19 | `7LV5wY-iM34` | title | "UNLIMITED Heat For Your Home / NO ELECTRIC NEEDED" | "UNLIMITED Heat For Your Home **\|** NO ELECTRIC NEEDED" | MISMATCH (a "\|" was swapped for "/", presumably to keep the markdown table intact; not exact) |
| | | channel | Zen Garden Oasis | Zen Garden Oasis `UCq0fxytZwEYul4AmfEiXL_w` | OK |
| | | views | 12M | **12,933,357** | MISMATCH: the rounded text understates by 7.2% (YouTube cuts 12.9M down to "12M") |
| 20 | `k7PSzi7NSyc` | title | "How To Clean Your AC and Coils Like the Pros Do / WILL Make Air Blow Colder" | "...Like the Pros Do **\|** WILL Make Air Blow Colder" | MISMATCH ("\|" swapped for "/", as above) |
| | | channel / views | How To Home / 5.6M | How To Home `UCpb-xu6Oun_d41RjztUgFWA` / 5,630,689 | OK (+0.5%) |
| 38 | `9U_a_6pBnkA` | title / channel / views | "ULTIMATE Mini Split Install Guide to Save You THOUSANDS" / LRN2DIY / 79K | same / LRN2DIY `UCPKAKrjoMz7POptCloy7AIQ` / 79,507 | OK (+0.6%) |

### 3b. Up-next re-pull for 2 seeds

The 2 seeds were drawn at random from the 22: `ED3bfesbE_Y` (Furnace Filter) and `yCZqfnlBYW8` (Circulator Pump). For each I pulled the up-next list again: the first page plus 2 continuations, 60 videos, about 20 minutes after the helper. "Claimed top channels" means the top 20 rows of the file's channel table.

| Seed | Videos also in the helper's list | Channels also in the helper's list | Top-20 channels in the helper's list | Top-20 channels in mine |
|---|---|---|---|---|
| `ED3bfesbE_Y` | 45 of 60 | 32 of 43 (mine has 44) | 14: #1-6, 8, 11, 13-17, 20 | 11: #1-3, 6, 11, 13-17, 20. All 11 are also in the helper's list. Missing this time: #4 DIY JIM, #5 Snowstead, #8 Greenhill Forge. |
| `yCZqfnlBYW8` | 29 of 60 | 29 of 53 (mine has 54) | 5: #7, 8, 10, 12, 19 | 2: #7 This Old House, #10 AC Service Tech LLC |

Reading: 45 of 60 for the furnace-filter seed is the same 75% stability the helper measured in its own repeat check. The circulator-pump seed moved much more (29 of 60). That supports the file's warning that one logged-out pull is a sample. None of the channels I found contradicts the file's channel list.

**File 3 result: 5 videos, about 15 field checks, 4 mismatches.**
- 2 titles have "\|" replaced by "/".
- 1 channel name is out of date (right channel ID).
- 1 rounded view count is 7.2% under the exact figure.

None is a wrong video or a wrong channel.

---

## 4. `keywords-round2.md` (10 PRIORITY keywords)

Rows drawn: 5, 22, 34, 50, 75, 79, 92, 98, 109 and 136. For each autocomplete source I re-ran the stated query: `client=firefox&ds=yt&hl=en&gl=us`, at about 04:00 UTC.

| # | Keyword | Stated source | Found | Result |
|---|---|---|---|---|
| 5 | unclog ac drain line | Silver Cymbal title `qAxJb0J1HH0` (3,772,025); autocomplete of "unclog ac drain line" | The title and figure are in `silver-cymbal.md`. Autocomplete returns the keyword as suggestion #1. | OK |
| 22 | do heat pumps save money | autocomplete of "heat pump save money", "save money heat pump", "heat save money" | all 3 return it, as the only suggestion | OK |
| 34 | steam radiator | brief topic list ("boilers, radiators and steam"); autocomplete of "steam radiator" | brief line present; autocomplete returns it as #2 | OK |
| 50 | do air filters really work | autocomplete of "the only air filter" | **Not returned** in 2 live pulls (04:00 and 04:02 UTC): only "the other stuff air filter", "air purifier dirty filter", "air filters in cars" (the second pull gave just the first two). The helper's raw file does show it as suggestion #4 at 03:30:57Z. | NOT REPRODUCED (autocomplete moved; the raw supports the helper; the query matches only weakly) |
| 75 | lower your electric bill | known title "Can This Device Actually Lower Your Electric Bill By 30%??" (2.6M); autocomplete of "lower your electric bill" | Autocomplete returns it as #1. The title is on The DIY HVAC Guy's Videos tab (`SWc0StyZiJs`, 2.6M); the source label leaves out the channel. | OK (label incomplete) |
| 79 | spray foam alternative | Silver Cymbal title, borderline (`sHL4lBAhklA`, 1,519,132) | The title is "Spray Foam is Expensive. Use THIS Instead!"; the keyword is a hand-cut paraphrase, as the method says. Views measured 1,519,182. | OK |
| 92 | indoor air quality | brief topic list ("indoor air"); autocomplete of "indoor air quality", "...hack", "...winter" (3 of the 10 stated checked) | all 3 return it | OK |
| 98 | best ac brands | brief topic list ("brand verdicts"); autocomplete of "best hvac brands", "best ac brands" | returned as #3 and #2 | OK |
| 109 | why is my ac freezing up | autocomplete of "why is my ac", "ac freezing up mistakes", "how to ac freezing up", "ac freezing up doesn't want you to know" | all 4 return it | OK |
| 136 | ceiling fan winter | **brief topic list**; autocomplete of "ceiling fan winter" | Autocomplete returns it as #1. But `RESEARCH-BRIEF.md` section 1 lists "ceiling fans" under the **electrical** study, not HVAC. The label may come from the helper's own longer brief, which I can't see. | MISMATCH (source label / scope) |

**File 4 result: 10 keywords, 1 not reproduced (#50), 1 wrong source label (#136).** Every other autocomplete source was reproduced live.

---

## 5. `channel-finds-round1.md` (10 rows)

The file is finished: it has a "Result" summary at the top, a methods section with its own self-check, and all 174 table rows. So I checked it.

Rows drawn from the 174: 5, 22, 34, 75, 79, 92, 98, 109, 136 and 152.
- **Handle:** the ID's About `canonicalChannelUrl`.
- **Example video:** `/next` for title, views and owner; the tab duration for length.
- **Type:** my look at 4 thumbnails per channel (the 2 newest and 2 from the Popular tab).

| Row | Channel | Field | Claimed | Found | Result |
|---|---|---|---|---|---|
| 5 | This Old House | handle / subs / views / joined / videos | @thisoldhouse / 2.34M / 864.05M / Jun 7, 2006 / 3186 | same / 2.34M / 864,048,747 / Jun 7, 2006 / 3,187 | OK (+1 video) |
| | | type | on camera | real presenters on camera | OK |
| | | example | "How to Install a Ductless Mini-Split Air Conditioner / This Old House" `ozaw9QhxkQU`, 5.27M | "...Air Conditioner **\|** This Old House", 5,270,398, owner This Old House, 7:09 | MISMATCH (title: "\|" swapped for "/"); views OK |
| 22 | AC Service Tech LLC | handle / subs / views / joined / videos | @acservicetechchannel / 689.0K / 139.29M / Feb 26, 2016 / 883 | same / 689K / 139,291,524 / same / 883 | OK |
| | | type | on camera | a real presenter | OK |
| | | example | "Electric Expansion Valve (EEV) Operation and Testing! HVAC Metering Device Training!" `LzvVjvUpOVM`, 2.56M | same, 2,560,293, owner matches, 16:34 | OK |
| 34 | Frugal Solutions | handle / subs / views / joined / videos | @FrugalSolutionsTV / 270.0K / 36.64M / May 26, 2023 / 437 | same / 270K / 36,639,008 / same / 437 | OK |
| | | type | not checked | AI-image style: an Amish woman and two white-bearded old men; no real presenter seen. Reads as faceless (AI images). | GAP (fill in) |
| | | example | "How Amish Heat Their Living Room Without Gas/Electricity" `SrC3wms8pQ8`, 2.53M | same, 2,532,406, owner matches, 18:43 | OK |
| 75 | Earl Knows How | handle / subs / views / joined / videos | @EarlKnowsHow00 / 43.6K / 3.12M / Jun 12, 2026 / 152 | same / 43.6K / 3,121,099 / same / 152 (About country: Spain) | OK |
| | | type | faceless persona (AI-image presenter) | the same older man (AI-looking) on all 4 | OK |
| | | example | "This Cheap Window Trick Keeps Heat Inside All Winter" `AQZLwcBnX1I`, 536.7K | same, 536,762, owner matches, 21:30 | OK |
| 79 | alpinehomeair | handle / subs / views / joined / videos | @alpinehomeair / 39.6K / 34.19M / Feb 23, 2009 / 175 | same / 39.6K / 34,190,306 / same / 175 | OK |
| | | type | not checked | a retailer/brand channel (Blueridge, AlpineHomeAir logos) with a real presenter and installer footage. Reads as on camera, brand. | GAP (fill in) |
| | | example | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" `DzVJiSQNbew`, 13.03M | same, 13,031,694, owner matches, 9:16 | OK |
| 92 | The Apprentice Survival Guide | handle / subs / views / joined / videos | @theapprenticesurvivalguide / 22.4K / 5.68M / Feb 14, 2018 / 176 | same / 22.4K / 5,680,314 / same / 176 | OK |
| | | type | on camera | a real man on camera | OK |
| | | example | "Fix Air Conditioner Fan Not Spinning" `2mtKTEE7QtQ`, 306.0K | same, 306,672, owner matches, 5:56 | OK |
| 98 | hackfreehvac | handle / subs / views / joined / videos | @hackfreehvac / 17.7K / 8.61M / Jan 4, 2008 / 1323 | same / 17.7K / 8,610,318 / same / 1,323 | OK |
| | | type | on camera (my reading) | 4 thumbnails show electronics benches and car interiors, and no presenter. Real footage, but "on camera" is not shown. | UNCONFIRMED |
| | | example | "Discharging Run Capacitors - Or NOT to discharge? :)" `Jz3DyCSKGB4`, 150.0K | same, 150,411, owner matches, 9:57 | OK |
| 109 | andyfireblade | handle / subs / views / joined / videos | @andyfireblade / 10.1K / 1.90M / Nov 1, 2022 / 115 | same / 10.1K / 1,899,080 / same / 115 (UK) | OK |
| | | type | on camera | a real man on 2 of 4; real footage | OK |
| | | example | "DIESEL HEATER HEATING MY HOME For The 4th year" `XR-E7PNCTKQ`, 221.0K | same, 221,244, owner matches, 6:08 | OK |
| 136 | Donna Fixes | handle / subs / views / joined / videos | @donnafixes / 1.9K / 328.5K / Sep 18, 2026 / 25 | same / 1.89K / 328,463 / same / 25 | OK |
| | | type | faceless persona (AI-image presenter) | the same older woman (AI-looking) on all 4 | OK |
| | | example | "9 Things Quietly Running Up Your Electric Bill This Winter (and the Free Fix for Each)" `zXvpZicp5WY`, 11.9K | same, 11,925, owner matches, 16:51 | OK |
| 152 | Walt Brandt | handle / joined / videos | @WaltBrandt / Apr 30, 2026 / 25 | same | OK |
| | | subs | 461 | **464** | MISMATCH, small (+0.65%). The file's own self-check (method section 6) found 464, but the table still says 461. |
| | | total views | 149.3K | 152,141 | OK (+1.9%, drift) |
| | | type | faceless persona (AI-image presenter) | the same older man (AI-looking) on all 4 | OK |
| | | example | "The Only 3 Gas Furnaces Worth Buying in 2026 — Before You Get Talked Into Junk" `MZ9QmbcVu6A`, 3.8K | same, 3,863; `/next` names no single owner, so it is likely a collaboration upload, but the channel ID matches; 22:40 | OK |

**File 5 result: 10 rows, about 60 field checks.**
- Handle and ID right in 10 of 10, joined date 10 of 10, example-video owner 10 of 10.
- Example videos: all 5 minutes or longer, and every view count within 1%.
- Mismatches: 1 title with "\|" swapped for "/"; 1 stale subscriber count (461, measured 464).
- Type: 6 of 6 confirmed where given. hackfreehvac's "on camera" is unconfirmed. 2 rows are "not checked" and can now be filled in: Frugal Solutions looks faceless (AI images); alpinehomeair is a brand channel, on camera.

---

## Summary

| File | Rows checked | Field checks (about) | Mismatches | Error rate | Verdict |
|---|---|---|---|---|---|
| `silver-cymbal.md` | 15 seeds + 3 borderline + 11 channel-level claims | 120 | 0 | 0% | **Pass.** Baseline 79,807 (n = 18), 538 / 321 / 217 and the Short reproduced exactly. |
| `known-channels-recheck.md` | 8 channels | 45 | 0 that matter (2 wording nits on type) | 0% | **Pass.** |
| `leads-channels.md` | 5 videos + 2 up-next re-pulls | 15 | 4 minor (2 titles, 1 channel name, 1 rounded count 7.2% low) | about 27% of fields, 0 wrong video or channel | **Pass with fixes.** |
| `keywords-round2.md` | 10 PRIORITY keywords | 25 query checks | 1 not reproduced, 1 wrong source label | 10% of rows each | **Pass with fixes.** |
| `channel-finds-round1.md` | 10 rows | 60 | 2 minor (1 title, 1 subs) + 1 type unconfirmed + 2 type gaps | about 3% | **Pass with fixes.** |

**Mismatches that matter (over 5% on views, wrong date, wrong type, wrong channel, wrong length class):**
1. `leads-channels.md` row 19, `7LV5wY-iM34`: "12M" is really 12,933,357, 7.2% low. This is YouTube's truncated text, not a helper error, but any figure carried forward from this table should use exact counts.
2. No wrong dates, no wrong channels, no wrong length class anywhere in the sample.
3. Type: 1 unconfirmed. `channel-finds-round1.md` row 98 hackfreehvac is "on camera", but none of the 4 thumbnails shows a presenter.

**Other mismatches (exactness):**
- Titles with "\|" turned into "/":
  - `leads-channels.md` `7LV5wY-iM34` and `k7PSzi7NSyc`
  - `channel-finds-round1.md` `ozaw9QhxkQU`

  Rule 2 asks for exact quotes; a markdown table can show "\|" escaped.
- `leads-channels.md`: "Bezdymne Piece" is now titled "Smokeless Stoves" (same ID).
- `channel-finds-round1.md`: Walt Brandt subs 461, measured 464. The file's own self-check already found 464.
- `keywords-round2.md` #136 "ceiling fan winter": "brief topic list", but ceiling fans are in the electrical study's list (`RESEARCH-BRIEF.md` section 1). The ceiling-fan topic (and space heaters, `space-heater`, 243 keywords) may overlap the electrical study's scope.
- `keywords-round2.md` #50: the autocomplete source is no longer returned live; it is supported only by the helper's raw file.

**Fixes I recommend (for the operator to approve; I changed nothing):**
1. Titles: keep the real "\|" (written `\|` inside tables) instead of "/", or add a note that "/" stands for "\|". Affects the leads and channel-finds tables, and probably more rows than the 3 sampled.
2. `leads-channels.md`: say in the top-40 table that views are truncated text (YouTube's "12M" can mean up to 12.99M). Give exact `/next` counts before any multiple or ranking is made from them.
3. `leads-channels.md` row 2: show the current channel title, "Smokeless Stoves (was Bezdymne Piece)".
4. `channel-finds-round1.md`:
   - Update Walt Brandt to 464 subs.
   - Fill in the types: Frugal Solutions as faceless (AI images), alpinehomeair as on camera / brand.
   - Re-look at hackfreehvac's type.
5. `keywords-round2.md`:
   - Relabel #136's source (not the HVAC brief list), and ask the operator whether ceiling fans and space heaters belong in the HVAC sweep or the electrical one.
   - Add "seen 03:30Z, not returned 04:00Z" to #50, or swap it for a reproducible keyword.
6. `known-channels-recheck.md`: optional wording only.
   - Vent Exposed: "object-only on HVAC thumbnails; its older pest-control thumbnails show a man".
   - Exposi: "almost no faces (1 profile in 9)".
7. Tool note for later helpers: on The DIY HVAC Guy the Popular chip came back in upload order for me. Check the sort before using a Popular pull on that channel, as `RESEARCH-BRIEF.md` section 4 says.
