# Known HVAC channels: re-check of the 2026-10-22 list

Pulled 2026-10-23 by a helper in the HVAC study. This re-checks the 8 channels the 2026-10-22 chat named (`findings/2026-10-22-hvac-and-electrical.md` section 1; `recovered/2026-10-22-roger-sub-brands/research/lane2-trades.md`). The old figures were not taken as true.

Raw pulls: `studies/hvac/data/raw/known-channels-2026-10-23.json`. New script: `studies/hvac/data/tools/latest_all.py`, which pages a channel's Videos tab and counts uploads by age.

**Sources and how to read them**
- **YT**: a YouTube page loaded directly on 2026-10-23 (About tab, Videos tab, video page). These are measured, and they are the freshest numbers.
- **NF**: NexLev `search_niche_finder_channels`, pulled 2026-10-23. Its stats are NexLev's own stored snapshot, updated 2026-10-07 to 2026-10-20 depending on the channel (the date is in the table). Monthly views and monthly $ are NexLev estimates, not measurements. "RPM total" is NexLev's blended RPM, and it is the one that matches monthly $ ÷ monthly views. "RPM base" is a niche-level base figure, not the channel's own RPM.
- **BV2**: NexLev `get_batch_channel_metrics_v2`, 2026-10-23 03:28 UTC. It is a different model and gives a different RPM and a different faceless flag.
- **FC**: NexLev `check_faceless_channel` (cached), 2026-10-23.
- Upload counts come from YouTube's rounded ages ("3w ago", "1mo ago"). "Last 30 days" counts videos showing days or weeks; "last 90 days" adds "1mo ago" and "2mo ago".
- **Type** is my reading of the thumbnails, the titles and the About text, given next to NexLev's flags. Contact sheet of 15 thumbnails: scratchpad only, not kept.

---

## 1. Summary table

| # | Channel | Handle / ID | Type: NexLev flags; my reading | Persona / claimed background | Subs (YT 10-23) | Total views (YT) | Joined (YT) / first upload (YT) | Videos (YT): long ≥300 s / Shorts | Uploads last 30 / 90 days (YT) | Monthly views (NF) | Monthly $ (NF) | RPM: NF total / NF base / BV2 | NexLev outlier (NF) | NF snapshot date | Sells |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ray Dutton's Garage | @RayDuttonsGarage · UCvcKEgZcY9ZgEULZouaNAOA · youtube.com/@RayDuttonsGarage | NF faceless=true, AI=false, style ai_avatar; FC **faceless=false** (0.99); BV2 faceless=false. **Mine: faceless persona.** The same grey-haired man appears in every thumbnail with a "RAY" name patch on navy work shirt, and he looks AI-made. Voice not checked. | "Hi, I'm Ray Dutton, a retired HVAC pro… For twenty-five years I worked in attics, basements and crawlspaces for the same companies I now expose" | 31.5K (NF 31,100) | 6,227,051 | Jul 1, 2026 / Jul 29, 2026 | 51: 51 long / no Shorts tab (NexLev hasShorts=false) | 15 / 51 | 2,366,426 | $7,188.73 | 3.04 / 6.8 / 5.08 | 1.45 | 2026-10-20 | E-book "The HVAC Survival Guide", raydutton.com, $27 one-time PDF (landing page 10-23; NexLev promotions also $27) |
| 2 | HVAC Exposed | @HVACExposed · UCZ1IwSV46bb09fMvqHn6_2A | NF faceless=true, AI=**true**; FC faceless=false (0.97); BV2 false. **Mine: faceless "exposé" brand.** Early thumbnails show only objects. Recent ones show an older man, likely AI, who is not named on the channel. | About: "We're here to change that. Real research. No contractor kickbacks." No named persona there, but the e-book domain is askfrankhvac.com, and one video is titled "7 Things a Retired HVAC Tech Does Every Winter…" | 9.59K | 2,016,579 | Feb 27, 2026 / Feb 28, 2026 (oldest listed video) | 79: 79 long / no Shorts tab | 10 / 30 | 59,532 | $158.69 | 2.67 / 5 / 4.03 | 0.6 | 2026-10-19 | E-book "THE HVAC OWNER'S BIBLE", askfrankhvac.com, "$27 instead of $60", instant PDF |
| 3 | Vent Exposed | @VentExposed · UCTDbUAjE9Ab_wwvuV7cgtvQ | NF faceless=true; FC faceless=false (0.92); BV2 false, **not monetized**. **Mine: faceless.** Object-only thumbnails (price tags on AC units). | "your consumer advocate for home climate". No person. | 1.93K | 696,224 | Mar 31, 2026 / Mar 31, 2026 | 12: 11 long, 1 under 300 s / no Shorts tab | 0 / 0 (**last upload May 30, 2026**) | 35,147 | $0 | 2.95 / 6.6 / 4.1 | 0.28 | 2026-10-19 | Nothing found (no About links; no link in the top video's description) |
| 4 | John The HVAC Guy | @JohnTheHVACGuy · UCOyYTw-deou3ax6gvCmX2dg | NF faceless=true, style ai_avatar; FC faceless=false (0.98); BV2 false. **Mine: faceless persona.** A middle-aged man, likely AI, in a white polo with a lapel mic appears on recent thumbnails; older thumbnails show only objects. | "Hey, I'm John. I've spent years around HVAC systems" | 7.13K (NF 7,020) | 986,134 | Sep 30, 2020 / **first HVAC video Aug 13, 2026** (older uploads are personal clips, e.g. "Taking a walk with my dog", 8 months ago) | 69: 69 long / no Shorts tab | **29 / 67** (about one a day, 25-32 min each) | 253,680 | $524.58 | 2.07 / 7.2 / 3.75 | 0.59 | 2026-10-20 | Guide "The 30-Year HVAC Bible" (174 pages), liibro.com/l/hvac/john-the-hvac-guy. Price on the page not pinned: $25 and $27 both appear. |
| 5 | Exposi | @Exposerosi34 · UCQCRIhHQ__ncUxtOHiIXI4A | NF faceless=true, style reused_footage; FC **faceless=true** (0.98); BV2 true. **Mine: faceless.** Thumbnails show hands and equipment, no face. | No persona. Its About copies HVAC Exposed's lines word for word ("Your HVAC system is the most expensive thing in your home you know nothing about. We're here to change that." / "Real research. No contractor kickbacks. No brand deals. Just the facts."). | 2.52K (NF 2,490) | 744,853 | Jun 8, 2026 / Jun 23, 2026 | 43: 43 long / no Shorts tab | 13 / 34 | 473,642 | $1,262.59 | 2.67 / 6.8 / 4.68 | 0.2 | 2026-10-19 | 3 PDF "field manuals", exposi.pages.dev/s/main: $34.99, $49.99, $97 bundle |
| 6 | Hank Cole | @HankColeUS · UC5NJ3yYhsZFkfWLJJJVoxMA | NF faceless=true; FC faceless=false (0.98); BV2 false. **Mine: faceless persona.** The same weathered older man, likely AI, on every thumbnail. | "Forty years in heating and cooling. Now I tell you what the companies won't." | 1.37K | 246,171 | Jul 20, 2026 / Jul 29, 2026 | 31: 31 long / no Shorts tab | 6 / 31 | 36,731 | $96.12 | 2.62 / 4 / 5.99 | 0.1 | 2026-10-20 | hanksheatguide.com, which now sells "Hank's Shop Notes — The Car Checks That Save You Thousands", $19 PDF (car, not HVAC) |
| 7 | Gus Whitaker | **@GusWhitakerr** · UCLdI4EbF3WcHS_oyhjSvwDw (name is ambiguous, see notes) | NF faceless=true, AI=**true**, style ai_avatar; FC faceless=false (0.99); BV2 false, **not monetized**. **Mine: faceless persona.** A white-bearded older man in overalls, likely AI. | Empty About. In video descriptions: "I've kept the same old Ohio house warm through forty winters." | 822 (NF 648) | 201,227 | Aug 27, 2026 / Oct 3, 2026 | 19: 19 long / no Shorts tab | 19 / 19 | 147,783 (snapshot 10-07, before his two hits) | $0 | 2.71 / 1.8 / 5.78 | 0 | 2026-10-07 | Nothing found |
| 8 | The DIY HVAC Guy | @diyhvacguy · UC2w60mhlxFmAhoi2oSDcEng | NF faceless=false; FC faceless=false (0.98); BV2 false. **Mine: on camera.** A real presenter ("Dave") in real workshop footage. | "My name is Dave and I am an HVAC Contractor in the beautiful state of Utah" | 527K | 102,187,575 | Mar 22, 2017 / not checked | 362 uploads (About, includes Shorts). Has a Shorts tab; Shorts count not found. Of 120 Videos-tab items pulled, 119 are ≥300 s. | 5 / 19 (Videos tab only) | 3,733,370 | $7,902.42 | 2.12 / 6.8 / 3.72 | 0.53 | 2026-10-19 | Affiliate links: HVAC Direct (code DIYHVAC, 5% off), Amazon store, Filterbuy (10%), GWIN assisted-DIY installs. A "Courses" tab exists; diyhvac.org is linked but was blocked when loaded, so not read. |

**Reading (mine):** Six of the eight are 2026 HVAC launches: Ray, HVAC Exposed, Vent Exposed, Exposi, Hank Cole and Gus Whitaker. John The HVAC Guy is a 2020 account that started HVAC in August 2026. Only Ray Dutton and Exposi are earning real money among the 2026 entrants ($7.2K and $1.26K a month on NexLev estimates). One more caution: NexLev's faceless checker calls 7 of the 8 "not faceless", including the AI-persona channels, so its flag can't be used to separate "persona with an AI face" from "on camera".

---

## 2. Per-channel notes

Views are YT, pulled 2026-10-23 with `vid.py`. All are long-form (≥300 s).

### 1. Ray Dutton's Garage
Top 3:
1. "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)": dOZ-8__G4uU, 1,202,740 views, Sep 11, 2026, 11:49
2. "The 5 Thermostat Habits That Wear Out Your AC Years Early": K2jCz3D5z_0, 1,126,365 views, Aug 18, 2026, 14:28
3. "Before You Turn On Your Heat This Fall, Do This (Or Pay for It the First Cold Night)": fHAlfm21vYw, 930,187 views, Sep 14, 2026, 14:42

The next three on the Popular tab (YT): "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" 763K; "5 AC Mistakes HVAC Companies Hope You Keep Making" 589K; "5 Energy Bill Mistakes Utility Companies Hope You Keep Making" 398K. Recent heating videos are still hitting: "What to Set Your Thermostat To This Winter (68 Is Not for Everyone)" 165K (2 weeks); "Why 70 Degrees Feels Cold in Your House Every Winter…" 153K (3 weeks). The newest, "Upstairs Hot, Downstairs Cold? Flip This Lever First" (Oct 21), has 9,073. The median of its latest 30 is 9,000 (YT), so the channel lives on a few big hits.

Every description opens with "🔧 Everything I learned fixing HVAC for 25 years, in one plain-English book. / 📘 THE HVAC SURVIVAL GUIDE - get it here: https://raydutton.com".

**Old vs now:**
| Figure | 2026-10-22 | 2026-10-23 | Note |
|---|---|---|---|
| Subs | 31.4K | 31.5K (YT) | |
| Total views | 6.17M | 6,227,051 (YT). NexLev analytics still says 6,167,742. | The old figure was NexLev's, slightly behind YouTube. |
| Joined | 2026-07-02 | Jul 1, 2026 (YT About, NexLev analytics). 2026-07-02 is NF's creation date. | **First upload Jul 29, 2026** (oldest video, sMMZZiiD4NI). So 6.2M views came in under 3 months of uploading, not "under 4 months". |
| Videos | 51 | 51 | |
| Monthly $ / views | $7,189 / 2.37M | $7,188.73 / 2,366,426 | Same NexLev snapshot, so this is not an independent re-measure. |
| RPM | "RPM base 6.8" | NF total 3.04; base 6.8; BV2 5.08 | **The old headline used the base figure.** The channel's own blended RPM in NexLev is 3.04, as the old auditor panel also noted. |
| Hits | 1.1M / 1.1M / 926K / 761K / 589K / 397K | 1.20M / 1.13M / 930K / 763K / 589K / 398K | Correct and correctly attributed. |
| Type | "faceless retired HVAC pro" | NF faceless; FC not faceless | Mine: faceless persona with an AI-looking face. The old label holds if "faceless" means "no real person". |
| Product | "HVAC Survival Guide" e-book | Same, $27 | Price added. |

### 2. HVAC Exposed
Top 3:
1. "The Only 5 HVAC Brands Worth Buying (The Lifetime List)": QKPPm6M0__o, 577,619 views, Feb 28, 2026
2. "How Smart Homeowners Are Beating the HVAC Industry (The 15-Year Loophole)": wz-06sf2Dy0, 382,132 views, Mar 6, 2026
3. "Why the $30 Filter Is Destroying Your HVAC System (The Airflow Lie)": l2yyfYpcwpQ, 350,862 views, Mar 30, 2026

All its big videos are 6-7 months old. The latest 30 uploads average 1,170 views, median 548 (YT). The best recent one is "The 5 Things Every HVAC Company Tries to Put in Your House…" at 6.6K (1 month).

**Old vs now:** 9.6K subs vs 9.59K now: same. The hits are right and rightly attributed: 571-576K is now 577,619, and 381K is now 382,132. **What the old chat left out:** the hits are from February and March, and the channel has faded since (now about $159 a month on NF). It is not a live 230-670K performer. The title "The Only 5 HVAC Brands Worth Buying (The Lifetime List)" has since been copied word for word by John The HVAC Guy (102,265 views) and HVAC Mike (5.2K, NF lastUploadedVideos). The old chat also did not note the $27 e-book.

### 3. Vent Exposed
Top 3:
1. "The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You)": 86S3ITbfzQY, 669,737 views, May 25, 2026, 8:12
2. "5 Water Heater Brands Designed to Die at Year 6 (And the 2 That Last 20+ Years)": uTHHV98zlpw, 13,035 views, May 29, 2026
3. "Why the $30 Air Filter Is Destroying Your HVAC System (The MERV Rating Lie)": RSd0zscPMDs, 5,372 views, May 26, 2026

**Old vs now:** 1.9K subs vs 1.93K now; the hit was 666K and is now 669,737. **What the old chat missed:**
- The 669K video is a **4-channel collaboration video.** YouTube's "Collaborators" panel lists Vent Exposed (1.93K), Prime Rundown (23.8K), Grill Verdict by Matt Garrison (11.4K) and Hull Honest (14.1K). The views can't be credited to Vent Exposed's own audience.
- The channel is dormant. Its last upload was May 30, 2026.
- It is not monetized (BV2), and NF shows $0.
- It started as a pest-control channel ("Why Raid Is a Waste of Money", "The Only Mouse Trap Worth Buying…", 6 months ago).

### 4. John The HVAC Guy
Top 3:
1. "Do THIS Once a Month and Your AC Will Last 25 Years": CJhglI70jw8, 232,657 views, Aug 15, 2026, 28:53
2. "Do THIS Before Winter and Your Furnace Will Last 30 Years": D3s86GpsnZ4, 177,032 views, Aug 25, 2026, 28:17
3. "The Only 5 HVAC Brands Worth Buying (The Lifetime List)": wbZYQQSCmNU, 102,265 views, Aug 31, 2026. This is a 2-channel collaboration with Nixon The Appliance Guy (1.91K).

Its recent uploads copy Ray Dutton's and HVAC Exposed's titles almost word for word:
- "Before You Shut Your AC Down This Fall, Do This (Or Pay for It N…", 1.8K
- "The $30 Furnace Filter Is Destroying Your Heating System (Here's Why)", 614
- "5 Furnace Mistakes HVAC Companies Hope You Keep Making", 342
- "The 5 Thermostat Habits That Wear Out Your Furnace Years Early", 2.1K
- "The Furnace Blacklist: 7 Brands Technicians Refuse to Install", 441

Most get 300 to 2,000 views. The latest-30 median is 1,000 (YT).

**Old vs now:**
- Subs were 7K; now 7.13K.
- The money matches because it is the same NexLev snapshot: $525 then, $524.58 now.
- **RPM was given as "7.2". That is the NF base figure; NF's blended figure is 2.07, and BV2 gives 3.75.**
- The hits are right: 232K is now 232,657, and 176K is now 177,032.
- The old chat gave no start date. The account dates from Sep 30, 2020, but HVAC videos began Aug 13, 2026. In practice it is a 2026 entrant on a re-used account.
- The old "peroxide video 54K" is "13 Things HVAC Technicians Don't Want You to Know About Hydrogen Peroxide – #7 Saves $900", still about 54K (YT Popular tab).

### 5. Exposi
Top 3:
1. "Doing This Will Make Your AC Run Like NEW Again!": ExzlvE5GfX8, 329,473 views, Sep 20, 2026
2. "This SECRET AC Trick is Only Known by 1% of HVAC Technicians (USE THEM NOW)": F0ENEEqAyaE, 196,987 views, Aug 9, 2026
3. "This SECRET Fall AC Trick Is Only Known by 1% of HVAC Technicians (DO IT BEFORE WINTER)": HfELRedGjpQ, 42,991 views, Oct 8, 2026

**Old vs now:**
- Subs: 2.5K then, 2.52K now.
- Money: $1,263 then, $1,262.59 now (same NF snapshot).
- The hit was 321K and is now 329,473.
- The old chat did not give the handle, which is @Exposerosi34. Searching "Exposi" also finds several unrelated channels with that name.
- The old chat did not note the product: $34.99 / $49.99 / $97 PDF field manuals.
- The old chat did not note that its About text copies HVAC Exposed's.
- Exposi is the only one of the 8 that NexLev's checker calls faceless.

### 6. Hank Cole ("40 Years In")
Top 3:
1. "The $5 Fix That Makes Your AC Blow 9° Colder — 40 Years In, Nobody Tells You This": HPYZfXWGzjQ, 156,562 views, Aug 5, 2026
2. "Avoid The One AC Mistake That Costs You Hundreds And Gets You Colder Air": KTpHJJTL3I0, 25,161 views, Aug 19, 2026
3. "The $16 Fix For The Hottest Room In Your House — Why Don't HVAC Guys Tell You?": AV6p0TCj3nA, 16,205 views, Aug 8, 2026

**Old vs now:** 1.37K subs (same); the best video was 156K and is now 156,562. **New:** the channel has **pivoted to cars**. Of the five uploads in the last 2 weeks, four have car titles and the fifth is titled "video"; for example "7 Things Shops Sell You That Your Car Doesn't Actually Need" (10 views) and "Your Car AC Is Blowing 55°. It Should Be 40°. Here's the $5 Fix" (27 views). Its book site now sells a car book. Its last HVAC video was "The Furnace Scam That Costs Homeowners Thousands Every Winter" (4 weeks ago, 19 views). The old reading ("failed or too-new clone") holds.

### 7. Gus Whitaker
**Name ambiguity (YT channel search, 2026-10-23):**
- **@GusWhitakerr** (UCLdI4EbF3WcHS_oyhjSvwDw): 822 subs, 19 home-heating videos. **This is the channel with the old chat's video.**
- @GusWhitakerGarage (UCEDyyeIEJi_c0yIqUOoYdrQ): 5 subs, 13 videos on Australian tools and UK/US cars. Not HVAC.

Top 3 (@GusWhitakerr):
1. "Turning Your Heat Up Past 70 Is NOT Warming Your House. Do This Instead": dBPrCiISyX0, 96,251 views, Oct 14, 2026
2. "Turning Your Heat Down Is NOT Saving You Money. Do This Instead And Your Bill Drops": sVWHA3YY-NU, 78,361 views, Oct 12, 2026
3. "The One Install Everyone Should Consider Before It's Too Late! (Whole House For Under $500)": SgviAoQ2Gfo, 6,230 views, Oct 10, 2026

Several of its titles copy other channels' titles. Measured title matches:
- Gus's "Why Buy A Generator? You Have One Parked In Your Driveway (A…" matches The DIY HVAC Guy's 2.4M video "Why Buy A Generator? You Have One Parked In Your Driveway."
- "Keep Your Family Warm During A Power Outage With This $3 Part…" matches DIY HVAC Guy's "…By Installing This $5 Part" (4.27M).
- "Do These 3 Things Now! (Or Pay For It During The Next Power Outage)" matches DIY HVAC Guy's "Do These 3 Things Now! (Or Regret It During The Next Power Outage)".
- "Before You Turn On Your Heat This Fall, Watch This (Or Pay Repair Bills All Winter)" follows the Ray / DIY HVAC Guy formula.

**Old vs now:** the hit was 74K and is now 78,361. A newer one is bigger (96,251). "Faceless, Oct 2026": the channel joined Aug 27, 2026, and its first upload was Oct 3. That is 19 videos in 20 days, all ~13-15 min. **Not monetized** (BV2; NF $0).

### 8. The DIY HVAC Guy
Top 3 (NexLev `youtube_channel_videos` popular sort; exact views YT):
1. "Keep Your Family Warm During A Power Outage By Installing This $5 Part": y07w1hiKIrI, 4,266,302 views, Oct 15, 2023, 11:47
2. "3 Things HVAC Contractors Don't Want You To Know About.": SkLMRM9NnBY, 2,769,956 views, Aug 5, 2022, 13:17
3. "This Could Keep Your Family Warm During An Emergency Power Outage.": 1JNuovFpCpQ, 2,744,903 views, Dec 2, 2022, 16:38

**New and relevant:** "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" (mP0IjyvQtxw) has 1,191,896 views since Sep 26, 2026. It is the channel's biggest video this year, and it is Ray Dutton's formula, used 12-15 days after Ray's "Before You Shut Your AC Down…" (Sep 11) and "Before You Turn On Your Heat This Fall, Do This…" (Sep 14). Measured dates; that it was copied is my reading. On a 527K on-camera channel the format did about 1.2M, against a latest-30 median of 46K (YT).

**Old vs now:** 527K subs (same); the hit was 4.2M and is now 4,266,302; $7,902 a month is the same NF snapshot ($7,902.42). The old "RPM base 6.8" is a base figure; NF's blended RPM is 2.12 and BV2's is 3.72. On camera: confirmed.

---

## 3. What the old (2026-10-22) chat got wrong or left out

1. **RPM.** It quoted the NexLev "base" (6.8 / 7.2) as the channels' RPM. NexLev's own blended RPM (NF rpm.total) is 2.07-3.04 for all 8. For Ray it is 3.04, and $7,188.73 ÷ 2,366,426 views matches that. BV2 gives 3.72-5.99. The findings line "the best RPM (NexLev base 6.8-7.2)" describes the niche base, not what these channels earn.
2. **"8 faceless competitors."** The DIY HVAC Guy is on camera (it is labelled "face" in the old table, but it is still counted in the 8). NexLev's own faceless checker calls 7 of the 8 "not faceless"; only Exposi passes. The old chat used the niche-finder flag only.
3. **Vent Exposed's 666K hit** is a 4-channel collaboration video. The channel has been dormant since May 30, 2026, is not monetized, and started as a pest-control channel.
4. **HVAC Exposed** was shown as an active 2026 entrant "reaching 230-670K". Its hits are from February and March 2026; recent uploads get 114-6.6K views.
5. **John The HVAC Guy's RPM** was given as "7.2" (the base). Its account is from 2020, but HVAC content only started Aug 13, 2026.
6. **Hank Cole** has since moved to car videos and a car e-book.
7. **Gus Whitaker**: two channels share the name; the right one is @GusWhitakerr. It joined Aug 27, 2026, first uploaded Oct 3, and is not monetized.
8. **Ray Dutton's start.** He joined Jul 1 (YouTube), not Jul 2, and **first uploaded Jul 29**: 6.2M views in under 3 months of uploads.
9. **The money figures were never re-measured.** NexLev's monthly views and $ are the same stored snapshot (updated Oct 7-20) in both chats, so "$7.2K a month" is one NexLev estimate, not two confirmations.
10. **Nothing was attributed to the wrong channel.** Every quoted title and view count was found on the channel the old chat named. The title "The Only 5 HVAC Brands Worth Buying (The Lifetime List)" exists on three channels, and the 576K version is HVAC Exposed's.

---

## 4. Leads (other HVAC / energy-bill channels seen on 2026-10-23)

From NexLev `get_similar_channels` for Ray Dutton (level 2, 120 channels), the NF query above and YT channel search. Subs are YT or NexLev as marked. Top videos come from the YT Popular tab (`yt.py`, 2026-10-23).

| Channel | Handle / ID | Subs | Joined | What it is / top video (views) | Source |
|---|---|---|---|---|---|
| Ramón Delgado | UC6nh_16KkkMHjccUXBNPEfQ | 33.4K (YT) | 2026-08-15 | "(The Mexican Way)" lens: "This Is How We Cool Our House Without AC (The Mexican Way)" 958K; "How to Clean Your Dryer Vent (The Mexican Way)" 372K | NexLev similar (79) |
| Earl Knows How | @EarlKnowsHow00 · UCPba1zh0V9QQAVju7D--SzA | 43.6K (YT) | 2026-06-12 | AI-avatar old-ways home: "This Cheap Window Trick Keeps Heat Inside All Winter" 536K; "This is How We COOL Our HOUSE Without AC — CANADIAN WELL" 473K. NF $2,237.68/mo | NexLev similar (57), NF |
| Passive House Technology | UCntW8YWdZzyvj8cVLeyki1A | 15.9K (YT) | 2026-08-12 | Energy and heat storage: "The $600 Tank That Beats a $10,000 Powerwall" 2.6M | NexLev similar (56) |
| HVAC Mike | @HVAC-Mike · UCgFpqO9vKw4HvjhnN6moalQ | 2.43K (YT) | 2026-05-23 | AI avatar (NF): "The Only 4 AC Brands Worth Buying in 2026 (The 20-Year List)" 86K. Sells "The Real HVAC Guide" (payhip). NF $33.96/mo | NexLev similar (73), NF |
| Hvac Insider | handle not checked · UC0FlY2puWKptIB7yZ_riKBg | 1.49K (YT) | 2020-01-21 | "The Only 6 HVAC Brands Worth Buying in 2026" 75K; "STOP Buying $30 Filters… They're Destroying Your HVAC (Airflow Lie)" 40K | NexLev similar (60) |
| Coil Exposed | @CoilExposed · UCt47_v_207fZOLrHhwXpIdA | 667 (YT) | 2026-04-20 | "Exposed" family, 32 videos, last upload 2026-08-19 (NF). NF $1.21/mo | YT search, NF |
| Home Systems Exposed | @HomeSystemsExposed · UCbLxS9ZtFptl1rHVYn9oouA | 175 (YT) | 2026-03-23 | "Exposed" family, last upload 4 months ago (NexLev) | YT search, NexLev similar |
| HVAC Uncovered | @HVACUncovered · UCczJ6EU5aLBogQOzFZ_W0HQ | 197 (NF) | 2026-03-23 | 7 videos, inactive since 2026-05-19 (NF) | NF |
| Hank Álvarez | UCUTNzI3fg3q2-sOGI827VvA | not shown | 2026-06-29 | Persona clone of Ray's titles: "5 Winter Energy Bill Mistakes Utility Companies Hope You Keep Making" 12; best "5 BIGGEST Winter HVAC Mistakes…" 1.7K | NexLev similar (67) |
| Home Fix Garage | UCqCKKYsi9U37xNIBgOZdflg | not shown | 2026-09-21 | Clone of Ray: "5 Electrical Mistakes That Kill Your AC Every Storm Season" 163 (Ray's version is 28K) | NexLev similar (80) |
| Hal's Boiler Room | UChM1RxTctTXapgVSLqIh1uA | not shown | 2026-10-12 | **Boiler / old-heat name** (the old chat's suggested angle), but its titles are Ray-style general HVAC; best 64 views | NexLev similar (52) |
| Richard Nakamura Secrets | @richnakasecret · UClcy6Bt3jTQZDPtxXa-lxSw | 3.92K (NexLev) | 2026-06-22 | AI-avatar "secrets" persona; NF $1,114.31/mo, RPM total 5.72 | NF, NexLev similar |
| Walt Brandt | @WaltBrandt · UCqCz10_64ISJCoc1xV1a8-w | 461 (YT) | 2026-04-30 | Appliance "worth buying": "The Only 3 Water Heaters Worth Buying in 2026…" 52K | NF |
| Backyard Low Tech | @BackyardLowTech · UCSedPjb56LMeiq_VV8164OA | 12.1K (NF) | 2018-10-25 | Low-tech heat and cool; NF $985.26/mo, 4.5 uploads a week | NF, NexLev similar |
| Old Ways Restored | UCVkVhwXnattecHEyw7xSIJA | 2.95K (NexLev) | 2026-05-28 | 392,499 total views; oldwaysrestored.com | NexLev similar (55) |
| Atlas AC | UCWtuOnlW7BeXLgr6M1_Z49g | 32.7K (NexLev) | 2021-01-19 | HVAC company channel, 8.45M views | NexLev similar (50) |
| HVAC Guide for Homeowners | UCp_5AZlvvW9jn6L4EZuCbNQ | 169K (NexLev) | 2013-06-04 | 18.9M views; newhvacguide.com | NexLev similar (50) |
| Anti DIY HVAC | @TedCookHVAC · UCFxf3hjNRSQ706L3jgDYnBw | 78.4K (YT) | not checked | On camera, old: "New Construction HVAC Hack Job…" 1.1M (4 years ago) | YT search |
| HVAC GUY | @HVACGUY · UCiz21FXLOV65NTgiUfJsxTg | 103K (YT) | 2015-07-03 | On camera, 2,227 videos | YT search, NexLev similar |
| AC Service Tech LLC | UCOZR-1IqsAer9wzlvFgb4mA | 689K (NexLev) | 2016-02-27 | On camera; sells HVAC courses and an AC book | NexLev similar (55) |
| Fix This House | UCjhwaa5Ufj-l_5JGFwfp98Q | 731K (NexLev) | 2019-02-19 | Home DIY, 155M views | NexLev similar (60) |
| Prime Rundown / Hull Honest / Grill Verdict | @PrimeRundown / @HullHonest / @GrillVerdict | 23.8K / 14.1K / 11.4K (YT) | not checked | Co-publishers of Vent Exposed's 669K collaboration video; own content not checked | YT Collaborators panel |
| Nixon The Appliance Guy | @NixonTheApplianceGuy · UCuUIbw0cEPRHXK8Hjyp43Zw | 1.91K (YT) | not checked | Co-publisher with John The HVAC Guy | YT Collaborators panel |

**Reading (mine):**
- Since mid-September, Ray Dutton's titles have been copied by at least John The HVAC Guy, Gus Whitaker, Hank Álvarez, Home Fix Garage, Hal's Boiler Room and, on a large on-camera channel, The DIY HVAC Guy. Measured: matching titles and dates.
- Most of the copies get 10 to 2,000 views. Only the DIY HVAC Guy's version broke out (1.19M).
- Hal's Boiler Room is the only boiler-named channel seen, and it is 11 days old.

## Checker notes (2026-10-23, `seeds/check-round1.md`)

All 8 rows passed. Two type notes: Vent Exposed's older pest-control thumbnails show a man, and 1 of 9 Exposi thumbnails shows a face in profile, so "faceless" for these two is mostly, not fully.
