# The six known electrical channels: re-check of the 2026-10-22 figures

Pulled 2026-10-23 by helper 3; saved by the main session as returned (the harness wouldn't let the helper write it). **Not yet re-checked** by the checker. "Reading" = the helper's judgement, not a measurement.

Files: `census.csv` (6 rows); `videos.csv` (175 rows: 133 long-form, 42 under 5:00 marked not counted; 88 rows have exact views and dates from video pages, the rest list-page values, as `views_source` says); `raw/yt/`, `raw/nexlev/`, `raw/walt-sales-page.json`; thumbnails `../../thumbnails/images/known-<channel>-<id>.jpg` (top 5 each, 30 files).

| Channel | Handle | Channel ID |
|---|---|---|
| Walt Brennan | @Walt-Brennan | UClpBI_QHhMq2_LcMMwmr6Og |
| The Apprentice's Guide | @theapprenticesguide | UCMXN-53SCPpYxmYSvFOjz2g |
| Rational Buyer | @rational_buyer | UCRKwB8DarX5_lykpnh8BolQ |
| FixItWithFil | @FixItWithFil | UCq6ZD77yzOZkm23Wr6A3jqg |
| Remote Electrician | @remoteelectrician | UCpZ1AQDdJ5moZwFlCSzFvRQ |
| The New Home Illusion | @TheNewHomeIllusion | UCUTZMtthVrdBhKfRrF0mrVg |

## 1. Re-check table

2026-10-22 figures from `findings/2026-10-22-hvac-and-electrical.md` section 2; (lane2) rows from `recovered/2026-10-22-roger-sub-brands/research/lane2-trades.md`.

| Claim | 2026-10-22 | 2026-10-23 | Source | Matches? |
|---|---|---|---|---|
| RPM base for the lane | 6.8-7.2 | Walt 7.2, Apprentice 6.8, Remote 6.8; Rational 1.8, FixItWithFil 1.8, New Home Illusion 5.0. Batch metrics give 10.32 / 4.78 / 4.66 / 4.18 / 3.60 / 3.78 | NexLev niche finder `rpm.base`; get_batch_channel_metrics_v2 | Partly: true for the three it came from, not all six; NexLev's two RPM tools disagree |
| Walt Brennan subs | 1.57K | 1,640 | NexLev get_channel_analytics; YT page | Yes (grown) |
| Walt Brennan earnings | $1,284/month | $1,283.62/month | NexLev niche finder (record of 2026-10-20) | Same record. **Caution:** its monthlyViews (215,383) exceed total views (188,856); first upload 2026-09-11. The estimate rests on an impossible figure |
| Walt Brennan persona | "Retired Utility Man" | Video: "My name is Walt Brennan. 32 years I pulled wire and read meters for the same utility that mails you the bill." Sales page: "Master electrician, central Pennsylvania · 32 years in the trade", 64 | about page; transcript p7x4nvpCoDg; walt-brennan.netlify.app | Yes, but told two ways |
| Walt Brennan "faceless" | listed as faceless | check_faceless_channel: **not faceless** (0.99); niche finder editingStyle "ai_avatar"; same AI older man in every top thumbnail | NexLev; thumbnails | **No (reading):** a named AI-avatar persona |
| "STOP Using Power Strips Like This — Retired Utility Man Explains" (p7x4nvpCoDg) | 74K | 77,920; 2026-09-29 | yt.py video = NexLev video details | Yes (grown) |
| "The 5 Outlet Habits That Start House Fires Years Later" (JsJc9JbpfvA) | 28K | 29,382; 2026-09-11 | yt.py video | Yes (grown) |
| Walt RPM base / total (lane2) | 7.2 / 5.96 | 7.2 / 5.96 | NexLev niche finder | Yes |
| Apprentice's Guide subs | 5.2K | 5,350 | NexLev; YT page | Yes (grown) |
| Apprentice's Guide created | 2026-08 | joined and first upload 2026-08-20 (MIuiZtAWm7s) | NexLev; yt.py video | Yes |
| Apprentice's Guide outlier | 9.26 | 9.26 | NexLev niche finder | Yes |
| Apprentice's Guide earnings (lane2) | $1,015/month | $1,014.77/month | NexLev niche finder | Yes |
| "Volts, Amps & Watts Explained — and Which One Kills You" (ffO4xVOU1oI) | 786K | 812,191; 2026-08-30 | yt.py video = NexLev | Yes (grown) |
| Apprentice grouped with Walt as "animated explainers" (lane2) | grouped | separate: Apprentice is 2D animation with a human voice; Walt is an AI avatar | NexLev editingStyle | lane2 merged them; the findings note keeps them apart |
| Rational Buyer "…Electric Bill in Half (The Panel Upgrade Loophole)" (ySzrVsvwuBs) | 266-282K | 284,979; 2026-03-16 | yt.py video = NexLev | Yes (grown) |
| Same video's multiple | 24.8x | NexLev video outlierScore 24.76; on our basis **828x** (284,979 ÷ median 344 of 31 long-form) | videos.csv | Different basis: 24.8x was NexLev's score |
| Rational Buyer as an electrical channel | listed | 1 of 31 videos electrical; the rest buy-it-for-life brands, tools, Home Depot; no uploads in about 5 months; France | Videos tab; NexLev | **No (reading):** a one-off hit on a buyer's-guide channel |
| FixItWithFil "This Kitchen Outlet Nearly Caught Fire — Here's What Went Wrong" (f_EvnEe4NR4) | 269K | 272,410; 2026-09-22 | yt.py video (NexLev 272,402 minutes earlier) | Yes (grown) |
| FixItWithFil "faceless" | listed | faceless true (0.98): hands-only live action, real voice, says he's a licensed electrician; not monetized ($0) | NexLev | Yes, but a real person filming hands, not a persona |
| Remote Electrician subs | 7.75K | 7,760 | NexLev; YT page | Yes |
| Remote Electrician outlier (lane2) | 4.71 | 4.71 | NexLev niche finder | Yes |
| "How to Change Electrical Outlet As a Beginner" (lUAaVwSjk3M) | 479K | 484,428; 2023-03-09 | yt.py video = NexLev | Yes; 3½ years old, not recent |
| New Home Illusion "The Modern Wiring SCAM (1920s Houses Were Wired SAFER)" (1EbXjv0kDzk) | 34K | 34,352; 2026-05-05 | yt.py video = NexLev | Yes; its bigger one is "The $2 Shortcut That's Burning Down American Homes" 46,730 |
| "No faceless veteran electrician dominates" | reading | still true: the only veteran-trade persona (Walt) is 6 weeks old with 1,640 subs; Remote (since 2022) says "I'm not a licensed electrician" | census.csv | Holds (reading) |
| "Demand is mid-sized" | reading | top long-form videos 0.27-0.81M; each hit is 76-92% of its channel's views (Apprentice 92%, Rational 81%, Fil 76%) | videos.csv; NexLev | Holds (reading): demand sits in single hits |

Spot check: six videos' views matched between the YouTube page and NexLev video details (FixItWithFil 8 views apart over a few minutes).

## 2. Channel profiles

Multiple = views ÷ the channel's median long-form views (basis given). Labels are readings.

### Walt Brennan (@Walt-Brennan): "Retired Utility Man" AI-avatar persona selling a $37 book set

- 1,640 subs; 198,553 views; 27 long-form videos, all 2026-09-11 to 2026-10-22 (channel ID dates from 2017-01-12 per NexLev; nothing visible before Sept 2026, possibly a reused account, reading). About 4.5 uploads a week, 19-25 minutes each. Basis: median of 27 = 2,052.

| Video | Views | Date | Multiple |
|---|---|---|---|
| "STOP Using Power Strips Like This   Retired Utility Man Explains" (p7x4nvpCoDg) | 77,920 | 2026-09-29 | 38.0x |
| "The 5 Outlet Habits That Start House Fires Years Later" (JsJc9JbpfvA) | 29,382 | 2026-09-11 | 14.3x |
| "STOP Running Your Dryer Like This — Retired Utility Man Explains" (JXA5_znDL6E) | 14,813 | 2026-10-14 | 7.2x |
| "The Only 3 Things in Your House That Need a Surge Protector And the One Box That Covers…" (xj2iE_Je-vk) | 14,110 | 2026-10-06 | 6.9x |
| "The 89 Cent Outlet Is the One That Burns What to Ask For Instead" (JgHUTjV9KSY) | 12,162 | 2026-10-08 | 5.9x |

- "…Habits That Start House Fires Years Later" series: 9 videos; Outlet 29,382 and Garage 5,647 best, Extension Cord 137 and Winter 886 worst. Same format, results depend on the topic.
- Labels: mostly mistakes / own habit; E4 + E17 + E9.
- Recent uploads weak: "The Outlet Behind Your Refrigerator…" 1.6K (1 day); "The Button on Your Bathroom Outlet Nobody Presses…" 1.1K.
- Persona: about page "My name is Walt Brennan. Thirty-two years I pulled wire and read meters for the same utility that mails you the bill… Plain talk, real numbers, no upsell… Tell me what year your house was built." In video: hook, a "before anybody feels careless" reassurance, then the name-and-years line; sign-off "I'm Walt Brennan. Keep the lights on and the bill down." The utility is used as insider credibility.
- Thumbnails (reading): the same AI older man in a work shirt pointing at the item; big yellow or red text ("RIP THIS OUT", "ASK FOR THE CLAMP", "FIRE STARTS YEARS LATER", "$4 vs $1,000", "BUY THIS INSTEAD").
- Sells "The Brennan Files", three PDFs: Vol. 1 "the forty-minute heat check" (60 pp.), Vol. 2 "Circuit Map Workbook" (20 pp.), Vol. 3 "The Electrician's Answers" (reporting a fault, judging a quote; 18 pp.). $37 "launch price", "the set goes back to $105"; whop.com checkout, 30-day refund. Pitch mid-video ("I put all of that in three short books. The links in the pinned comment at the top") and in the description's first line. Sales page: "One diagnostic visit, just to have somebody look, runs $120 to $250. All three guides run $37." The sales page gives a different background from the channel (master electrician, not utility).

### The Apprentice's Guide (@theapprenticesguide): animated electrician course, one 812K hit

- 5,350 subs; 886,658 views; 5 long-form plus Shorts (8 total). Joined and first upload 2026-08-20. Basis: all 5 long-form (fewer than 10), median 11,094.

| Video | Views | Date | Multiple |
|---|---|---|---|
| "Volts, Amps & Watts Explained — and Which One Kills You" (ffO4xVOU1oI) | 812,191 | 2026-08-30 | 73.2x |
| "How Electricity Actually Flows (What's Really Moving in a Wire)" (MIuiZtAWm7s) | 69,461 | 2026-08-20 | 6.3x |
| "Series vs Parallel Circuits Explained — Why One Dead Bulb Kills Everything" (pnK_OEpissI) | 11,094 | 2026-09-06 | 1.0x |
| "Half Your House Went Dark. The Dark Half Is Still Live." (LOFpw6uyYjQ) | 1,636 | 2026-09-22 | 0.15x |
| "Why Did Only One Breaker Trip?" (8nwE0Jq202o) | 1,117 | 2026-10-10 | 0.10x |

- The hit opens on homeowners, not apprentices: the doorknob spark, the bathroom outlet, "why does the kitchen go dark when you run the toaster and the space heater at the same time?" Thumbnail "WHICH ONE KILLS YOU?" over an orange glowing hand, "VOLTS · AMPS · WATTS". Later trade-focused lessons fell to 1-2K.
- No persona or name: unnamed human-voiced narrator, dark blueprint animation; credibility from the course framing ("Lesson 2 of Electrician Fundamentals") and cited sources (NEC 2026 210 and 240.4, NIOSH 98-131, UL 943, Mike Holt). Sells: none found.

### Rational Buyer (@rational_buyer): buyer's-guide channel, one electrical hit, abandoned

- 1,820 subs; 352,232 views; 31 long-form, 2026-02-23 to about May 2026; France; no upload in about 5 months. Basis: median of 31 = 344.

| Video | Views | Date | Multiple |
|---|---|---|---|
| "How Smart Homeowners Are Cutting Their Electric Bill in Half (The Panel Upgrade Loophole)" (ySzrVsvwuBs) | 284,979 | 2026-03-16 | 828x |
| "The Only 7 Tool Brands Built to Last a Lifetime (The "Grandfather's Garage" List)" (mH1nkv_Vj0I) | 25,387 | 2026-03-01 | 73.8x |
| "7 Things That Get Better The Longer You Own Them (Buy It For Life)" (H_PitCUQEeU) | 17,853 | 2026-03-04 | 51.9x |
| "Why Plumbers and Electricians Never Buy Anything at Home Depot" (j5mmiDQF1hc) | 8,415 | 2026-03-14 | 24.5x |

- The hit is money / electric bill (reading: electric-bill, dont-want-you, E1 + E10 + E18, villain bill-sender). Opens "The average American homeowner pays over $1,500 a year in electricity bills… nobody from the utility company ever calls to tell them why… Today we show you the loophole they never mention", then a 100-to-200-amp panel upgrade with stacked rebates ("$185 → $92/month"). A counter-example to "money framing is weak in electrical", from one video.
- No persona: third-person "we", stock footage, AI voice per NexLev. Thumbnails: red X vs green check, "THE 'LIFETIME' LIST", "THE PANEL LOOPHOLE". Sells: none found.

### FixItWithFil (@FixItWithFil): real licensed electrician (claimed), hands only; one 272K story video

- 1,010 subs; 359,256 views; 38 videos, 13 long-form (mostly 5-8 min). Joined 2025-10-26; first upload 2026-05-17; first long-form 2026-06-19. Not monetized per NexLev. Basis: median of 13 = 3,306.

| Video | Views | Date | Multiple |
|---|---|---|---|
| "This Kitchen Outlet Nearly Caught Fire — Here's What Went Wrong" (f_EvnEe4NR4) | 272,410 | 2026-09-22 | 82.4x |
| "3-Way Switches Explained: One Simple Rule" (31SGyvxFRAY) | 12,931 | 2026-06-27 | 3.9x |
| "3-Way Switch Not Working? Fix This Common Mistake!" (2UToUOm4Vc4) | 9,136 | 2026-09-13 | 2.8x |
| "Shared Neutral - Are they Dangerous?" (Jc1tNrmmPlI) | 8,487 | 2026-10-03 | 2.6x |

- The hit is a story (reading: E17 + E4 + E9, villain last owner). Opens "So, I got called to a friend's house, and this is what I saw." A split kitchen receptacle with the tab left on melted and banged; then the right way. Thumbnail "FIRE HAZARD OR NOT?" over a charred outlet with meter probes. The rest is plain how-to plus cars, gadgets, tool reviews.
- About page: "real-world DIY home repairs, electrical projects, tool reviews, and automotive maintenance from a licensed electrician… No clickbait. No shortcuts." Casual, real voice, hands only. Sells: none found (contact email).

### Remote Electrician (@remoteelectrician): 2022-23 how-to that still earns; says he's not licensed

- 7,760 subs; 3,403,378 views; 57 videos (46 on the Videos tab, 21 long-form). First upload 2022-11-07; 2 long-form uploads in the last 90 days. Basis: only 6 long-form in 12 months, so all 21: median 19,000.

| Video | Views | Date | Multiple |
|---|---|---|---|
| "How to Change Electrical Outlet As a Beginner" (lUAaVwSjk3M) | 484,428 | 2023-03-09 | 25.5x |
| "How to Install GFCI Outlet (4 Wires)" (-ckZDjywVPA) | 315,994 | 2023-02-27 | 16.6x |
| "GFCI Outlet Not Working 🤷‍♂️ Can't Reset It" (o82wv4cEIJk) | 306,091 | 2022-11-07 | 16.1x |
| "Outlets Lights Not Working but Breaker is ON" (Rix5A8ku10g) | 304,375 | 2022-11-17 | 16.0x |

- Labels: all how-to (outlets-switches, gfci-afci), E13 + E8 or E6, no villain. Plain thumbnails (product photo, "HOW TO INSTALL GFCI OUTLET 4 WIRES", "BEFORE / AFTER").
- "I'm not a licensed electrician. This channel shares how-to's and tips… not for beginners", plus a long liability disclaimer. Sells: Lowe's affiliate ("My Tools", shoplowes.me/4sJz0VP).

### The New Home Illusion (@TheNewHomeIllusion): "builder scam" channel; wiring videos did best; stopped

- 720 subs; 126,190 views; 36 long-form, 2026-03-23 to about June 2026; NexLev monthly views 216. Abandoned (reading). Basis: median of 36 = 574.5.

| Video | Views | Date | Multiple |
|---|---|---|---|
| "The $2 Shortcut That's Burning Down American Homes" (qva5q_Fp3mA) | 46,730 | 2026-05-14 | 81.3x |
| "The Modern Wiring SCAM (1920s Houses Were Wired SAFER)" (1EbXjv0kDzk) | 34,352 | 2026-05-05 | 59.8x |
| "Why 90% of New Home Electrical Panels Are a FIRE Waiting to Happen!" (X64XEu6kcVo) | 6,420 | 2026-04-15 | 11.2x |
| "Why 90% of 70s Homes Are Built to BURN (The Aluminum Wire Scam)" (ruq88SrYlQ8) | 6,066 | 2026-05-08 | 10.6x |

- Labels: dont-want-you / myth-bust, villain the builder (last owner / flipper), E17 + E4 + E3/E15. Thumbnails: a house with red arrows and stamps ("SCAM", "FAKE", "$2 SHORTCUT"), sometimes on fire. 20 of 36 videos electrical, including all of its top 6; the later basements and lawn-care videos got 37-375.
- No persona ("We expose…"), stock footage, human voice per NexLev; transcript not checked. Sells: none found.

## 3. Short reference (under 5:00, not counted)

| Video | Channel | Length | Views | Date |
|---|---|---|---|---|
| "How to Change Out a Light Switch Like a Pro!" (8i0GJ6-cG8k) | Remote Electrician | 3:04 | 234,285 | 2023-03-05 |
| "3 Way Light Switch Wiring (Smart Switch or Regular)" (Rq_iM2neQJI) | Remote Electrician | 2:09 | 179,370 | 2024-02-28 |
| "Non Working Electrical Outlet Troubleshooting" (_fW-42aNqdU) | Remote Electrician | 2:59 | 106,040 | 2023-02-19 |
| "GFCI Troubleshooting Non-Working Outlet" (8tuUiqEne6k) | Remote Electrician | 3:24 | 100,232 | 2023-06-07 |
| "Timer Switch Installation, Replacement Intermatic Timer" (PchFV3xfDtY) | Remote Electrician | 1:31 | 75,588 | 2023-03-02 |
| "No Neutral? No Problem! Easy DIY Dimmer Install." (mYlydW3GD2Q) | FixItWithFil | 2:59 | 10,243 | 2026-06-07 |

## 4. What didn't work and what wasn't checked

- The shared loader capped channel lists at 30 (wrong continuation token). The helper paged with its own scratch script (raw files carry `"pager": "scratchpad pager.py"`). **Fixed in `yt.py` by the main session on 2026-10-23.**
- The Apprentice's Guide has no Popular or Oldest chip (5 videos), so latest only.
- Whether Walt's AI avatar appears on screen in the videos: not watched.
- Transcripts checked: p7x4nvpCoDg (full), f_EvnEe4NR4, ffO4xVOU1oI, ySzrVsvwuBs. Not: The New Home Illusion, Remote Electrician.
- NexLev disagrees with itself (two RPM figures per channel; Walt's monthly views above his total). Earnings are NexLev estimates, not measured.
- Web searches used: 0.
