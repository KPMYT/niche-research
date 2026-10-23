# New-channel hunt, NexLev side (2026-10-23)

Helper 6's report, saved by the main session as returned (the harness wouldn't let the helper write it). **Not yet re-checked** by the checker. Labels and types are readings.

Files: `queries.md` (every NexLev call: 47 niche-finder queries, 41 semantic and 6 filtered; latest_discovered_faceless_niches, 1,000 channels; 6 faceless_outliers queries; 8 viral-small keywords; 3 similar-channel seeds); `census.csv` (134 channels with `scope` and `new_12mo`: 28 core, 18 of them new; 106 adjacent, 83 new); `raw/` (niche-finder, faceless-outlier, viral and similar-channel JSONs; `batch-metrics.csv` 134 channels; `check-faceless.csv` 20; `analytics-about.csv` 18; `yt-pages/`, `yt-videos/`, `top-videos-exact-yt.txt`). Web searches: 0.

**Method notes:**
- "New in the last 12 months" = exact date of the oldest video on the Videos tab (`yt.py video`), not NexLev's `firstVideoDate` (rounded).
- 25 new channels joined before 2025-10: read as relaunched, repurposed, or older uploads deleted; flagged in notes.
- 18 channels found outside the niche finder have no NexLev monthly views or earnings ("not found"). 22 had no Oldest chip; the last Videos-tab item was used (source says so).
- Multi-page channel pulls redone after the loader fix (51 channels with 30+ uploads in 90 days, up to 4 pages).
- Self-check: 12 random channels' NexLev subs and video counts against YouTube pages: within about 10% (NexLev lags).

## 1. The "Frederick Barnes" channel

The helper flagged UCSf0X7Rt96r7sx0uCiDgDcA ("Frederick Barnes", joined 2026-09-15, 1,350 subs, hit 5pQAWcEsr3Q 434,775 on Sep 21) as a possible name clash. **Main session note: this is the operator's own channel** (helper 4, `../just-stop-fire/report.md`). Its type is faceless persona (the same AI firefighter in every thumbnail), not plain faceless. Its hit's title closely follows Home Hazard's "10 Things You Should NEVER Leave Plugged In at Night" (gI3SDaKj6xU, 698,054, uploaded Aug 7 2026, six weeks earlier).

## 2. New core channels taking off

Started in the last 12 months, electrical or fire safety. Views and dates exact, from video pages.

| Channel | Started | Subs | NexLev monthly views / $ / RPM / outlier | Take-off videos (ID, views, date) |
|---|---|---|---|---|
| Home Hazard (faceless; e-books "Home Hazard Files") | joined 2022, first visible upload Jun 9 2026 | 6,900 | not in niche finder; RPM 5.65 | "10 Things You Should NEVER Leave Plugged In at Night" gI3SDaKj6xU 698,054 (Aug 7); "The #1 Thing In Your Home Starting House Fires" L1ocs_Qx3Gg 215,081 (Jun 9); "10 Things You Should Never Leave Plugged In When You Leave the House" 0hVXHM_qLEI 80,806 |
| The Apprentice's Guide (animated, faceless) | Aug 20 2026 | 5,210 | 380,677 / $1,015 / 5.04 / **9.26** | "Volts, Amps & Watts Explained — and Which One Kills You" ffO4xVOU1oI 812,261 (Aug 30) |
| Hardwired YouTube (faceless explainer) | Aug 22 2026 | 9,160 | n/a / RPM 4.54 | "How a Resistor Actually Works — Ohm's Law Explained" wcsos_xH8pU 1,697,324 (Aug 22) |
| Zenthral Code (faceless, "physics graduate") | first visible Aug 26 2026 | 23,700 | 1,445,755 / $2,152 / 3.21 | "Why 3-Phase Motors Have 6 Terminals…" 2zFnPI-cMYM 259,178; "Why Does Europe Use 50 Hz…" GUF0eRC5ZrQ 188,472; "Stranded Wire vs Solid Wire" 3QVAuoydeD0 161,221 |
| Elias Mercer Method (faceless) | Aug 11 2026 | 1,140 | 304,982 / RPM 3.53 | "5 Things You Should NEVER Plug Into a Power Strip!" -gfBM2U6DxE 289,048 (Aug 29) |
| FixItWithFil (hands only, claims licensed electrician) | May 17 2026 | 995 | 166,418 / RPM 4.66 | "This Kitchen Outlet Nearly Caught Fire — Here's What Went Wrong" f_EvnEe4NR4 272,410 (Sep 22); also in NexLev's viral small-channel feed |
| Rational Buyer | Feb 23 2026 | 1,800 | 22,712 | "How Smart Homeowners Are Cutting Their Electric Bill in Half (The Panel Upgrade Loophole)" ySzrVsvwuBs 284,990 (faceless-outlier score 24.8) |
| Walt Brennan (persona, retired utility man; RPM 10.32, highest in core) | first visible Sep 11 2026 (joined 2017) | 1,570 | 215,383 / $1,284 | "STOP Using Power Strips Like This — Retired Utility Man Explains" p7x4nvpCoDg 77,931; "The 5 Outlet Habits That Start House Fires Years Later" JsJc9JbpfvA 29,382 |
| DIY Tips 24h (faceless; mostly plumbing valves, some wiring) | Apr 22 2026 | 7,660 | 2,744,915 / $3,349 / 2.85 | valve videos 1.37M-1.6M (e.g. GW5naRoG9T0 1,604,439) |

(Helper 3 found Walt Brennan's NexLev monthly views exceed his total views; treat his $1,284 with caution.)

**Small new core personas, not taken off yet:**

| Channel | Started | Subs | Best video (ID, views) |
|---|---|---|---|
| Mike Callahan's Firehouse (retired firefighter, 28 years) | Aug 24 2026 | 195 | "20 Devices That Can Catch Fire in Your House While You Sleep" 2cjRekzvBRY, 13,881 |
| Roy Dalton Electric | Aug 2026 | 480 | "7 FATAL Wire Nut Mistakes" x18gqteMBzY, 16,643 |
| Gus Tanner | Aug 2026 | 533 | "20 'Illegal' Wiring Tricks Every 1950s Electrician Knew…" qp3xyI23Qws, 11,778 |
| Sam Creel (repurposed, "Retired Firefighter" titles) | Sep 2026 | 141 | "10 Things You Should NEVER Leave Charging Overnight" b0mvwo_ueAc, 6,002 |
| SHOCKPROOF LIVING | Dec 2025 | 604 | "GFCI Outlet Won't Reset?" Lk1aHR4a4vE, 66,233 |

**Pattern (reading):** two formats break out again and again: "things you should never leave plugged in / plug into a power strip" lists (four channels at 270K-700K: Home Hazard, Frederick Barnes, Elias Mercer Method, FixItWithFil's fire story), and animated volts/amps/resistor explainers (0.8M-1.7M).

## 3. New adjacent channels taking off (selected)

- **HVAC persona: Ray Dutton's Garage** (retired HVAC pro; joined Jul 2 2026; 31,100 subs; 2.37M monthly views; $7,189/month): "Before You Shut Your AC Down This Fall, Do This" dOZ-8__G4uU 1,202,823; "The 5 Thermostat Habits That Wear Out Your AC Years Early" K2jCz3D5z_0 1,126,375; "Before You Turn On Your Heat This Fall, Do This" fHAlfm21vYw 930,252.
- **Home security for seniors:**
  - Wes Tucker (locksmith, 35 years; relaunched Aug 2026; 46,700 subs; 2.47M monthly): "35 Home-Defense Tricks Retired Cops Teach Seniors Living Alone…" SpktUJlX7fo 3,011,736.
  - Christopher Johnson (UK; persona "David Bennett"; relaunched Sep 26 2026; 2.43M monthly; $14,769/month; outlier 3.31): "15 Things Ex-MI6 Officers Teach Elderly British People Living Alone…" Phtfiy7eVBw 772,388.
  - Kate Sullivan Safer Living (Sep 2026; 627K monthly; RPM 8.37).
  - Marcy Hollis (Sep 23 2026): "15 Things Police and Firefighters Want Women Living Alone TO DO Every Night" 6pxddze1PnE 199,867.
  - Linda Bennett (Sep 14 2026; sells a book): "Seniors, Put Foil on Your Door Knob…" QcsIRQTfxMg 164,601.
- **Outages, aimed at 60+:**
  - Blackout Basics (Sep 15 2026; RPM 10.59; 673K monthly; $4,510): "12 Dollar Tree Items That Keep You WARM When the Power Goes Out" 1SzLwAGaBmA 241,916.
  - June's Kitchen Table (disclosed fictional AI grandmother; late husband restored power for the co-op for 38 years): "9 Ways I Keep My Bed Warm With No Heat" 1Oz08l8RTWg 478,084.
  - Survival Blueprint (RPM 9.8, outlier 4.12); Wes Tucker Prepping (788K monthly); Harlan Pike Prepping ("for folks over sixty"); Donna Fixes (retired building superintendent; 654K monthly).
- **Backup power:** Gary Whitaker Backup Power (Jun 2026): "5 Cheap Power Stations Everyone Ignores" G5OFL2ZaaBU 316,008, "10 Generators BANNED From American Homes in 2027" rkfvCRK5OG4 58,050; Modern Decay (relaunched Apr 2026; whole-home generator videos 221K-284K); The Sensei's Home: "No Electrician Needed: The Japanese Plug-In Solar Setup" aRNRf56rNtI 333,340.
- **Fire and firewood:** Harlan Sawyer: "5 Woodpile Dangers That Can Put You in the Hospital" BlHC-momweM 428,512, "5 Woods That Set Chimneys on Fire" jSlmEEj2x1A 126,569; The Uniform Years: "20 Things Every 1970s Firehouse Had…" N9Mi3Q6Hi8Q 267,210; Firehouse Life (195K monthly in its first month).
- **Grid / lineman explainer:** Kilowatt Nation (Sep 2026; RPM 7.85): "What Actually Moves Through a 500,000-Volt Power Line?" NGtn3dYwMeM 124,846.
- **E-bike battery safety:** E-Bike Insider: "17 Things You Should NEVER Do Charging An Electric Bike" 9Lib0V5mTAY 60,764 (RPM 8.1); The eBike Doctor: "The eBike Mistake That Can Burn Your House Down" pHwDB84BRAE 39,994.
- **"Free energy" persona cluster (a warning, not a model; improbable claims, reading):** Glen Pritchard "$12 Old TV Antenna Pulls FREE Power…" xyU2peAe-MA 1,358,266; Builds With Eli Yoder; Eli Yoder Secrets (248K subs); The Passive House Files (73.5K); Grain & Gravity. The biggest new-channel earner next to "electric bill / backup power".

## 4. Faceless personas found (Roger's model)

52 persona channels, all new or relaunched. The most relevant:

| Persona | Claimed background | Scope |
|---|---|---|
| Walt Brennan | utility lineman / meter reader, 32 years | core |
| Frederick Barnes (ours) | firefighter | core |
| Mike Callahan | retired firefighter | core |
| Roy Dalton | electrician (name only) | core |
| Eli Yoder | electrician (name only; content AC and water) | adjacent |
| Gus Tanner | none stated | core |
| Sam Creel | firefighter, titles only | core |
| Walt Harden | contractor and home inspector, 35 years (Home Guard) | adjacent |
| Ray Dutton | retired HVAC pro | adjacent |
| John | HVAC (John The HVAC Guy) | adjacent |
| Walt Brandt | appliance repair, 40 years | adjacent |
| Gene Halvorsen | heating-oil delivery, 37 winters | adjacent |
| Konrad Fischer | 40 years heating with wood | adjacent |
| Donna | building superintendent, 41 years | adjacent |
| Jack Wells | garage-door tech, 30 years | adjacent |
| Sergeant Dale Whitfield | Army quartermaster, 30 years | adjacent |
| Wes Tucker | locksmith, 35 years | adjacent |
| Tom Callahan | security technician, 35 years | adjacent |
| Curtis Hayes | security guard, 31 years | adjacent |
| Danny Vaughn | ex-burglar | adjacent |
| Wade Merrill | military | adjacent |
| June Halvorsen | lineman's widow (AI disclosed) | adjacent |
| Harlan Pike, Dan Cooper, Kate Sullivan, Marcy Hollis, Linda Bennett, Gary Whitaker, Cal Watts, Prepared Dale | none stated | adjacent |

- Most name a specific trade and years in a first-person description ("Thirty-two years I pulled wire…") (reading).
- Name clashes: two "Wes Tucker" channels; "Eli Yoder" on three; "Kate Sullivan" on two.
- Many sell an e-book or guide from the description: Home Hazard, Linda Bennett, Marcy Hollis, Wade Merrill, Exposi, Modern Decay, ELI YODER ELECTRICIAN, Roy Dalton, Sergeant Dale Whitfield, The Lumberjack.
- NexLev usually marks these persona channels "not faceless" (an AI character on screen), so isFaceless=true filters miss them.

## 5. Channels by presenter background (claimed; this census of 134)

| Background | All | Core | New personas (12 mo) | Examples |
|---|---|---|---|---|
| electrician | 8 | 6 | 2 | FixItWithFil, Cursed Controls, ElectroTest, Cory Mac, lexi abreu, Roy Dalton, ELI YODER |
| lineman / utility | 3 | 1 | 2 | Walt Brennan, June's Kitchen Table, Utility Design Simplified |
| firefighter | 3 | 2 | 2 | Frederick Barnes, Mike Callahan, Eric Hurst (real fire PIO, on camera). Home Hazard and Sam Creel only borrow "Firefighter" in titles; counted as none stated |
| fire inspector / marshal | 0 | 0 | 0 | none found in any query |
| home inspector | 5 | 1 | 1 | Morgan Inspection, gold.star, Site Inspections, Constructiva, Home Guard |
| other trade | 12 | 1 | 8 | HVAC, appliance, locksmith, building superintendent, garage door, dryer vent |
| other, non-trade | 17 | 1 | 12 | Amish, military, ex-burglar, physics graduate |
| brand | 1 | 1 | 0 | Kidde |
| none stated | 85 | 15 | 25 | |

- By type: 67 faceless, 52 faceless persona, 15 on camera. New channels: 48 faceless, 52 persona, 1 on camera.
- Open lane (reading): no retired fire marshal or fire inspector personas at all; two retired-firefighter personas (both Aug-Sep 2026, 195 and 1,350 subs); one lineman persona (Walt Brennan, RPM 10.32).

## 6. What didn't work

- NexLev's isFaceless filter misses persona channels, so filtered searches undercount them.
- No electrical or fire category in the niche finder; the DIY category with first upload after 2025-10-23 returned 4 unrelated channels.
- Viral keywords "electrician" and "wiring" returned 0 videos.
- get_channel_analytics returned only the about block (no monthly views or earnings).

## Corrections after checker B (2026-10-23)

- **Fire inspector / marshal personas exist, but are tiny and not in NexLev's database:** Earl Whitaker (UCmk_aG0OsnaP_7C5OxSSEvQ; 2 subs, 13 videos, 302 views; "32 years in the Dayton Fire Department, the last 12 as a fire inspector"; joined Sep 12 2026), Chief Reardon (UCDfUpxEwI1s0tkTAm-cNw0A; 47 subs; best RDmBGhKJvYI 1,659; "25 years as a fire marshal"; reused account from Jul 2025), Chief Miller (UCy523MhXbDch-_O2wox7xwA; 3 subs; "62, retired battalion chief and fire inspector, 34 years"; joined Oct 12 2026), Tommy Sullivan "Sully's Safety" (UChFS6J4bSxENe2IK8Ls9WEg; 19 subs; fire-marshal titles). Read "none" above as "none in NexLev; a few tiny ones on YouTube, none over 1K subs": nearly empty, not empty.
- **Zenthral Code started earlier:** first upload 2026-07-14 (-e240MMtf_Q), first long-form 2026-07-21 (SMSbci_DkIU), not Aug 26. Still new. Fixed in `census.csv`.
- **Builds With Eli Yoder is faceless** (name only; 0 of 8 thumbnails show a character), not a persona. Fixed in `census.csv`.
- NexLev subscriber counts lag 14-19% on two fast-growing channels (June's Kitchen Table, Kate Sullivan Safer Living).
- Ray Sutter (persona, 22 years Army; UCVIirwqWdBCyynoWRsld2Ug) and Ray Dutton's Garage (UCvcKEgZcY9ZgEULZouaNAOA) are two different channels; the same 31.5K subs is a coincidence.
- Home Hazard: account joined Dec 13 2022; first visible upload L1ocs_Qx3Gg on Jun 9 2026; nothing visible from 2022-2026 (reads as wiped and relaunched).
