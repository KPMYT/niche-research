# New-channel hunt, YouTube search side (2026-10-23)

Helper 7's report, saved by the main session as returned (the harness wouldn't let the helper write it). **Not yet re-checked** by the checker. Pulled with `yt.py` (search pages, channel tabs, video pages); subscriber counts and list-page views are rounded by YouTube. Type, persona and background are readings of thumbnails and descriptions; backgrounds are claimed. 121 channels checked by hand (plus ours); counts below cover only those.

Files: `keywords.md` (50 keywords with source, sorts run and relevant long-form results; 8 channel-name searches; a short-reference table of under-5:00 hits, not counted); `channels.csv` (563 channels: 122 checked on their channel pages, 441 from search pages only, marked "not checked"); `videos.csv` (1,740 relevant long-form videos; list-page views except 44 breakout videos with exact views and dates; 40 hand-labelled, the rest keyword-labelled "my reading"); `raw/` (117 search pages, 8 channel searches, about 220 channel tabs, 44 video pages, 214 thumbnails at 480px, `scripts/` with contact sheets). Web searches: 0. All channel pulls were 1 page (unaffected by the loader bug). The relevance filter is title-only, so a few off-topic titles (storm news) got through. Frederick Barnes (`UCSf0X7Rt96r7sx0uCiDgDcA`, ours) is left out of every count.

## 1. The big picture

1. **A wave of new channels:** 107 of 121 checked first uploaded within 12 months, most 1-3 months ago.
2. **Almost none show a real person:** 79 faceless personas (a named older man, sometimes a woman, in AI images); 27 faceless with no character; 1 on camera.
3. **24 reused accounts:** the first upload is a junk clip ("showing my cute feet in the morning light", "A walk in my Neighbourhood", a GTA clip, "Driving In Czech") or much older (2019, Frank Ross; "20 years ago", HomeSafety Report).
4. **The core niche has few breakouts; the money is in the adjacent lanes:** 2 core electrical/fire channels meet the "taking off" rule, 28 adjacent ones do (blackouts, heat without power, backup power, Amish or Mexican "tradition" hacks). Most core personas (retired firefighter, lineman, electrician) have under 200 subs and medians under 500 views.

## 2. New channels taking off

Rule: first upload within 12 months (or a switch of niche in that window) and either a long-form video over 100K or a median at least 2x the subscriber count (median of long-form on the Latest tab's first page).

**Core niche:**

| Channel | Subs | First upload | Breakout videos |
|---|---|---|---|
| Home Hazard (`UCAx9qFU1CRRcx2mMFTV9Png`), faceless, no character; sells a "Home Hazard Files" PDF | 6.9K | 4 months ago | "10 Things You Should NEVER Leave Plugged In at Night" (`gI3SDaKj6xU`) **698,054** exact, 8:31, Aug 7 2026; "The #1 Thing In Your Home Starting House Fires" (`L1ocs_Qx3Gg`) 215K; "10 Things You Should Never Leave Plugged In When You Leave the House" 80K |
| SHOCKPROOF LIVING (`UCHhiS7OziiRgZ7wmZM4GKsw`), faceless graphics | 613 | 10 months ago; no uploads for 3 months | "GFCI Outlet Won't Reset? FIX IT in 5 Minutes" (`Lk1aHR4a4vE`) 66,233; "How to Replace a GFCI Outlet Safely" 57K |

Just under the rule: **Walt Brennan, "Retired Utility Man"** (`UClpBI_QHhMq2_LcMMwmr6Og`, 1.64K subs, first upload 1 month ago, median 2,000; "STOP Using Power Strips Like This Retired Utility Man Explains" `p7x4nvpCoDg` 77,924). **Elias Mercer Method** (1.14K subs, general home tips): "5 Things You Should NEVER Plug Into a Power Strip!" (`-gfBM2U6DxE`) **289,048**, counted below as adjacent.

**Adjacent** (exact views where checked):

| Channel | Subs | First upload | Breakout video | Views |
|---|---|---|---|---|
| Ray Sutter (persona, Army veteran) | 31.5K | 1mo | "20 Heating Sources That Don't Need Electricity" | 919,426 |
| Ray Sutter | | | "7 Things You MUST Do The Moment The Power Goes Out" | 714K |
| Rhett Callahan Prepping | 41.5K | 3mo | "11 Dollar Tree Heating Items That'll Be WORTH GOLD in a Winter Blackout" | 855,451 |
| Builds With Eli Yoder (Amish) | 58.1K | 6mo | "This $60 AutoZone Alternator Powers a Whole Cabin All Winter" | 754,925 |
| Glen Pritchard | 20.7K | 2mo | "$30 TESLA ROOF ANTENNAS Generate Power From Thin Air?!" | 823,342 |
| Weirdward Bound (faceless history) | 62.5K | 5mo | "Why Does America Use 60 Hz While Europe Uses 50 Hz?" | 1,341,644 |
| Weirdward Bound | | | "Before Circuit Breakers, Early Electricity Turned Homes Into Fire Traps" | 207,595 |
| Ramón Delgado "(The Mexican Way)" | 33.4K | 2mo | "How to Clean Your Dryer Vent (The Mexican Way)" | 372,444 |
| Ramón Delgado | | | best overall: "This Is How We Cool Our House Without AC" | 958K |
| June's Kitchen Table (AI grandmother, late husband a lineman) | 1.69K | 1mo | "9 Ways I Keep My Bed Warm With No Heat" | 477,834 |
| Modern Decay | 4.35K | 6mo (reused) | "5 Cheap Whole Home Generators Everyone Ignores (But They're Absolute Goldmines)" | 284,240 |
| Gary Whitaker Backup Power | 7.14K | 4mo (reused) | "5 Cheap Power Stations Everyone Ignores (But They're Absolute Goldmines)" | 316K |
| Cal Watts | 8.46K | 3mo | "Tesla's New Powerwall 3 Has Ended the Standby Generator Business Forever!" | 287K |
| Wes Tucker Prepping | 4.02K | 1mo | "No Gas, No Wood — This DIY Stove Heats Your Home All Winter" | 298,987 |
| Elias Mercer (frontiersman) | 585 | 2mo | "Old-Timers Never Heated the House When the Power Died" | 153,083 |
| Jiro Araki (Japanese) | 508 | 4mo | "If a Blizzard Hits Tomorrow, Every Japanese Home Already Has These 7 Things" | 114,304 |
| E-Bike Insider | 605 | 1mo | "Most E-Bike Owners Get This Wrong About Charging" | 62,167 |
| Kate Sullivan Ready Living | 792 | 12 days | "35 Winter Survival Items Seniors should Stockpile" | 43,774 |
| Ralph Harmon | 1.19K | 1mo | "Blackout? This $299 Backup Keeps Your Food Frozen" | 35,066 |

Also meeting the rule: Silas Mercer, Forgotten American Survival, Elias Yoder, Caleb Greer, Built To Fail, HVAC Exposed, Ray Dutton's Garage, Jerry Davis, DISCOVER US STATE (first upload "1y ago", on the edge). Weak (tiny subs only): Earl Knows Engines, Ray Tolliver, Gus Tanner.

**Small personas with views far above their subs:**

| Channel | Subs | Best video | Views |
|---|---|---|---|
| Earl The Electrician | 34 | "Whole-Home Generators Are Expensive on a Fixed Income—Seniors, Do This Instead!" | 14,860 |
| Mitch the Lineman | 97 | "12 Things Power Company Workers Keep When the Grid Dies" | 17,581 |
| Fire Radar | 103 | "10 Things You Should Never Leave Plugged In When You Leave the House" | 32,727 |
| Mark Ellison | 151 | "Why Your Generator Won't Save You This Winter" | 21,943 |
| Mike Callahan's Firehouse | 195 | "20 Devices That Can Catch Fire in Your House While You Sleep" | 13,881 |
| Frank Kessler | 64 | "5 Things I Unplug When I Leave for Vacation" | 10,130 |
| Lyle Brannock | 26 | "$60 AutoZone Alternator vs $2,000 Generator? A Retired Lineman Answers" | 8,232 |

Gus Whitaker (823 subs; HVAC): "Turning Your Heat Up Past 70 Is NOT Warming Your House" 96,362 in 8 days.

## 3. Faceless personas found (79 checked)

In every case checked: a named man aged about 55-70 in AI images, usually pointing at the hazard, 2-4 bold words on the thumbnail. A few women (June Halvorsen, Kate Sullivan, Rose, Martha Graves).

- **Firefighter:** Frank The Firefighter, Gus Delaney, Mike Callahan, Sam Creel, Frank Kessler, Frank Malone, Gary Hutchins, James Walker, Tom Brennan, Cal Brennan, Callahan's Firehouse.
- **Fire inspector or marshal:** Earl Whitaker (every title "Seniors: 12 … (Retired Fire Inspector's Warning)"), Chief Reardon, Chief Miller.
- **Lineman or utility:** Walt Brennan, Lyle Brannock, Harlan, Mitch, Lineman Earl, Earl Mabry, Hank Miller, Walt Hensley.
- **Electrician:** Earl The Electrician, Backyard Hank, Roy Dalton, Gary the Electrician, Mr. Voltage.
- **Home inspector:** Gus Harlan, Hal Brennan, Vernon Sloane, Frank Mercer, Ray Tolliver.

June's Kitchen Table says in its description that she is a fictional AI character.

## 4. Presenter background, 107 new channels (claimed)

| Background | All new | Core niche only (50) |
|---|---|---|
| None stated | 53 | 16 |
| Firefighter | 12, plus 2 in titles only | 12, plus 2 |
| Lineman or utility (incl. 1 grid operator, 1 lineman's widow) | 11 | 8 |
| Home inspector | 6 | 1 |
| Electrician | 5, plus 1 in titles only | 5 |
| Fire inspector or marshal | 3, plus 1 in titles only | 3, plus 1 |
| Other trade or job (HVAC, handyman, maintenance, appliance repair, hardware store, generator tech, small engines, plumber, interior designer, Army) | 13 | 2 |

## 5. Formats repeated in this year's winners (reading)

1. **"N Things You Should NEVER Leave Plugged In (at Night / When You Leave / Overnight)":** 65 long-form videos on 36 channels, near word-for-word. Only Home Hazard (698K), ours (435K) and Elias Mercer Method's power-strip version (289K) broke out; copies after September mostly sit under 1K.
2. **A cheap item that "replaces" expensive backup power or heat:** "$60 AutoZone alternator" (754K, copied by Lyle Brannock), "$30 Tesla roof antennas" (823K), "Dollar Tree heating items" (855K), "No Gas, No Wood DIY stove" (299K).
3. **Winter blackout and heat-without-power lists of 20+ items, 20-40 minutes:** Ray Sutter 919K and 714K, Forgotten American Survival 1.6M, Silas Mercer 480K, June 478K.
4. **Product exposé templates reused across channels:** "5 Cheap ___ Everyone Ignores (But They're Absolute Goldmines)" on 2 channels (284K, 316K); "The Only 4 … Brands Worth Buying"; "… BANNED From American Homes in 2027".
5. **A persona tag in the title:** "Retired Utility Man Explains", "A Retired Lineman Answers", "Seniors: 12 … (Retired Fire Inspector's Warning)".
6. **Tradition keys:** "(The Mexican Way)", "Amish", "Every Japanese Home"; among the biggest adjacent winners.
7. **Electrical-history explainers:** "Why Does America Use 60 Hz" 1.34M; "Why the US is Stuck on 120V" 255K; "Before Circuit Breakers…" 207K.
8. **Myth-bust with "Do This Instead":** Gus Whitaker 96K and 78K.

Many target seniors ("Seniors", "Over 60" in titles); none of those passed 50K in this pull.

Found again from the brief's list: Walt Brennan; The New Home Illusion ("The $2 Shortcut That's Burning Down American Homes" 46,730); Ray Dutton's Garage ("Before You Shut Your AC Down This Fall, Do This" 1,202,799); Gus Whitaker; HVAC Exposed. Ramón Delgado was mentioned in an earlier operator chat.

Not checked, worth a follow-up: "Eli Yoder Secrets" (814K, 6 months old), a second Amish channel.
