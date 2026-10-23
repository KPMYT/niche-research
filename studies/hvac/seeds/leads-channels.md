# Leads from YouTube's "up next" and similar videos (Silver Cymbal HVAC seeds)

**Pulled:** 2026-10-23, 03:38 to 03:52 UTC, by the round 2 up-next helper. **Not yet re-checked by a second helper (working rule 3).**
**Raw data:** `data/raw/upnext-2026-10-23.json`. **Scripts:** `data/tools/upnext.py` (pull), `data/tools/upnext_build.py` (merge, counts, these tables).

## Method

| Step | What was pulled | Count | Tool / source | Worked? |
|---|---|---|---|---|
| Hop 1 | Up-next list of the 22 seeds + the 5 biggest borderline videos (`sHL4lBAhklA`, `9d9TL02idO4`, `pPMm0reEBPM`, `yNBXE3BszEM`, `EjLJm0g4whg`) | 27 videos x 60 items = 1,620 items (1,618 videos, 2 playlists); 1,023 different videos, 666 channels | innertube `POST /youtubei/v1/next` (logged out, hl=en, gl=US): first page 20 items + 2 continuation pages of 20 | yes. Every list said more pages were available; we stopped at 3 pages (60 items) per video |
| Hop 2 | Up-next list of the 10 most-recommended HVAC videos from other channels in hop 1 (rule below) | 10 x 60 = 600 items (599 videos, 1 playlist) | same | yes |
| Repeat check | The same 3 seeds pulled again 10 minutes later (`_b6p0fkWhCY`, `5GbXgEYw5TE`, `BP1iDvKpNZA`) | 3 x 60 | same | 45, 46 and 46 of the 60 videos were the same; only 6, 12 and 11 of the first 20 were the same (order shuffles). Channels: 32 of 43, 35 of 46, 38 of 49 the same. **So a single logged-out pull is a sample, not a fixed list.** |
| NexLev similar videos | `get_similar_videos` for each of the 22 seeds (not the 5 borderline) | 890 results (27 to 53 per seed) | NexLev | yes. This is a semantic title match over NexLev's index, **not** YouTube's recommendations. 3 results (`o8KQu_MlpoY`, `nsRHhU6q5RY`, `kEWzIfnIhUw`) came back short and inline, so their key fields were copied into the raw file by hand (marked in `source`); the other 19 were parsed by script |
| NexLev similar channels | `get_similar_channels` for Silver Cymbal, level 3 | 159 channels | NexLev | yes, but they are general home-DIY peers (LRN2DIY 78, Is It Worth It 71, The Funny Carpenter 62, The DIY Guy 61, Proper DIY 60...), not HVAC channels. Kept in the raw file; subs from it are used below where nothing else was found |
| NexLev suggested videos | `search_youtube_suggested_videos` | 6 keyword queries x 100 | NexLev | **not usable for this task.** It has no video-ID input, so it cannot say what is suggested next to a seed. Its title match is loose: "boiler" returns Limp Bizkit and Boiler Room DJ sets, "mini split" returns a kids' video at 931M, "heat pump" returns "CHOTU DADA KA PETROL PUMP 2". Kept raw, not used in the tables |
| Subscriber figures | YouTube About panel for 43 channels missing a figure | 43 | `yt_water1.py about` (logged out), 2026-10-23 03:48 UTC | yes for 42; DEBOSS GARAGE returned nothing |
| `/watch` page, `/player` | | | | blocked from the cloud, as the seed helper found; not used |

**Hop 2 rule:** the 10 HVAC videos (title reading) from channels other than Silver Cymbal that appear in the most hop-1 lists. Picked: `_ZgVjFpBnQA` (in 10 of 27 lists), `k7PSzi7NSyc` (6), `D_2T5H7CFmA` (6), `BSTkKiJPeaQ` (5), `AQ4EYHNCDzg` (5), `5dCCntGj1wM` (5), `dOZ-8__G4uU` (5), `GfMNLWzaUHU` (5), `k1HGyewDZ_k` (5), and `2mKwCmaR5Qg` (4; the tie at 4 was broken by the best average position, 9.75). Wood stoves and diesel heaters were counted as heating-adjacent, not core HVAC, for this pick, so `s6gYsaYvdjg` (9), `U6QPw6H_yMc` (8) and `-i28W_xx2mw` (8) were skipped. Six of the ten picks are mini-split videos, so hop 2 leans to mini-splits (a bias of the pick, noted).

**How to read the counts:** "Hop 1" = in how many of the 27 hop-1 lists the channel appears at least once (in brackets: of the 22 true seeds). "Hop 2" = of the 10 hop-2 lists. "NexLev similar" = in how many of the 22 seeds' NexLev similar-video lists. Views in up-next are YouTube's rounded short text ("763K"); length is the thumbnail badge. "HVAC-related?" is my reading: a keyword test on the titles we saw from that channel (in brackets: how many of its titles matched), corrected by hand for the channels where the keyword test is misleading (marked with a short description). Water heaters are counted as plumbing, not HVAC. Wood stoves, diesel heaters and "free heat" videos are marked heating-adjacent.

**What the logged-out up-next mixes in:** a logged-out viewer has no history, so YouTube fills part of every list with generally popular videos: news, politics, trucks, science (see the topic table). These are not signals about the seeds.

## Channels in the up-next and similar results (HVAC or partly HVAC)

Sorted by hop 1, then hop 2, then NexLev similar. Silver Cymbal himself is left out (in 21 of the 27 hop-1 lists, 17 of 22 seeds; his own HVAC videos fill 22 of the 899 HVAC items). Included: every channel with HVAC titles that shows up in at least 3 up-next lists (hop 1 + hop 2) or in at least 3 NexLev similar lists; 129 channels.

| # | Channel | ID / handle | Up-next hop 1 (of 27 sources; of 22 seeds) | Up-next hop 2 (of 10) | NexLev similar videos (of 22 seeds) | HVAC-related? | Example recommended video | Subs seen (source) |
|---|---|---|---|---|---|---|---|---|
| 1 | The DIY HVAC Guy | `UC2w60mhlxFmAhoi2oSDcEng` @diyhvacguy | 15 (12) | 7 | 13 | yes: HVAC contractor DIY (Utah) (reading) | "The Mini Split - REINVENTED." (`-VPZuCK0Ag0`, 1M views, 31:23) | 527K (About, about.json) |
| 2 | How To Home | `UCpb-xu6Oun_d41RjztUgFWA` @HowToHomeDIY | 14 (11) | 6 | 4 | yes: AC cleaning/fixes, capacitor, filters (reading) | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (`k7PSzi7NSyc`, 5.6M views, 11:01) | 854K (About, about.json) |
| 3 | Ray Dutton's Garage | `UCvcKEgZcY9ZgEULZouaNAOA` @RayDuttonsGarage | 13 (13) | 7 | 0 | yes: faceless 'retired HVAC pro' (Roger's model) (reading) | "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" (`_ZgVjFpBnQA`, 763K views, 15:10) | 31.5K (About, about.json) |
| 4 | DIY JIM | `UCj-e0GX6QhDChCPUBeX-FbA` @DIYJIM | 12 (10) | 1 | 2 | yes, mixed: diesel heaters + mini-split cleaning + oil burners (reading) | "Heating My 2000 Sq Ft House With a Chinese Diesel Heater (Round 2 – Even Colder!)" (`bPj-y5o0Y7s`, 186K views, 42:01) | 112K (About, about.json) |
| 5 | Snowstead | `UCT-HKsjRFI3S3BQVqeYdsYw` @Snowstead | 12 (11) | 1 | 0 | heating-adjacent: off-grid / diesel-heater home heating (reading) | "Can a DIRT CHEAP Diesel Heater Actually Keep My Homestead Warm?" (`s6gYsaYvdjg`, 1.3M views, 17:32) | 123K (About, this pull) |
| 6 | Everyday Home Repairs | `UCw1V3VC3xAzL66X4VwqaKlg` @EverydayHomeRepairs | 10 (8) | 4 | 4 | yes (17 of 21 titles; reading) | "Complete DIY Mini Split Installation / New Mr Cool 4th Gen Unit" (`qwDq0JCo2eM`, 1.1M views, 18:43) | 1.31M (About, about.json) |
| 7 | This Old House | `UCUtWNBWbFL9We-cdXkiAuJA` @thisoldhouse | 10 (9) | 3 | 7 | yes (11 of 15 titles; reading) | "How to Install a Ductless Mini-Split Air Conditioner / This Old House" (`ozaw9QhxkQU`, 5.2M views, 7:09) | 2.34M (About, about.json) |
| 8 | Greenhill Forge | `UCkmEk3ldK7uJ1OvdLKwGrxg` @GreenhillForge | 10 (8) | 2 | 0 | heating-adjacent: wood stoves, DIY heaters (reading) | "Wood Stove Water Heater Experiment - Surprising Results! Part 1" (`-i28W_xx2mw`, 1.6M views, 19:53) | 148K (About, this pull) |
| 9 | Taddy Digest | `UCuMyjTVlkM4xZ5z_eSyoB1w` @taddydigest | 9 (9) | 6 | 2 | yes (31 of 31 titles; reading) | "Top 5 Mini Split Installation Mistakes - Don't Do This!" (`D_2T5H7CFmA`, 132K views, 17:12) | 273K (About, about.json) |
| 10 | AC Service Tech LLC | `UCOZR-1IqsAer9wzlvFgb4mA` @acservicetechchannel | 9 (9) | 4 | 11 | yes (31 of 31 titles; reading) | "Full Installation of Mini Split Ductless Unit, Step by Step!" (`JQkth-AM5CE`, 2.5M views, 1:28:33) | 689K (About, about.json) |
| 11 | LRN2DIY | `UCPKAKrjoMz7POptCloy7AIQ` @LRN2DIY | 8 (6) | 4 | 6 | yes (30 of 32 titles; reading) | "DIY Mini Split Install - All the Things Nobody Shows You" (`2mKwCmaR5Qg`, 3.2M views, 33:23) | 1.28M (About, about.json) |
| 12 | Benjamin Sahlstrom | `UC-Z9UcrgFzJIg49LtJFc_kg` @BenjaminSahlstrom | 8 (7) | 4 | 1 | yes (15 of 16 titles; reading) | "Are Mini Split Air Conditioners Worth It? - Top 5 Pros & Cons" (`3DHyShrGUXw`, 2M views, 15:33) | 486K (About, this pull) |
| 13 | The Handyman | `UCtXVIqkc3iBk0bV5gvcNWgw` @TheHandyman1 | 8 (7) | 4 | 0 | partly: handyman business, mini-split installs (reading) | "The New Way to Install Mini Splits in 2026 (Step-by-Step)" (`jCEc4gtd56w`, 105K views, 20:07) | 533K (About, this pull) |
| 14 | Bezdymne Piece | `UC_eTsy7fL7l2ZXUUTiT3ShQ` @bezdymnepiece | 8 (7) | 3 | 0 | heating-adjacent: wood stoves (About title now 'Smokeless Stoves') (reading) | "A stove that saves 50% of firewood and heats the house for 50 hours without a fire" (`U6QPw6H_yMc`, 3.4M views, 1:08:31) | 45.3K (About, this pull) |
| 15 | Fix This House | `UCjhwaa5Ufj-l_5JGFwfp98Q` @FixThisHouse | 8 (6) | 2 | 2 | yes (12 of 16 titles; reading) | "HVAC Contractors Charge Hundreds For This SECRET 5-Minute AC Fix!" (`9QJL_dhfudc`, 537K views, 9:51) | 731K (About, about.json) |
| 16 | Project Farm | `UC2rzsm1Qi6N1X-wuOg_p0Ng` @ProjectFarm | 8 (8) | 2 | 0 | partly: product tests, some AC and diesel heaters (reading) | "Coldest and Quietest Air Conditioner Ever Tested!" (`BSTkKiJPeaQ`, 1M views, 20:18) | 3.94M (About, about.json) |
| 17 | Word of Advice TV | `UCekKmUEJxBRx5tI1tUyHOqA` @WordofAdviceTV | 7 (7) | 1 | 7 | yes (15 of 16 titles; reading) | "Window Air Conditioner Not Cooling And The Most Common Fix" (`an1yClPV4i4`, 2.3M views, 14:55) | 661K (About, about.json) |
| 18 | Zen Garden Oasis | `UCq0fxytZwEYul4AmfEiXL_w` @ZenGardenOasis. | 6 (4) | 4 | 0 | heating-adjacent: 'unlimited heat, no electric' rocket/candle heaters (reading) | "UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" (`7LV5wY-iM34`, 12,933,357 views (checker, 2026-10-23; up-next showed "12M"), 26:04) | 789K (About, about.json) |
| 19 | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | `UCG_Pwm8tfMnJg1Rp2Fsd-qA` @PipeDoctor | 6 (6) | 2 | 5 | yes (19 of 19 titles; reading) | "Homeowner Tries To Fix Gas Boiler and Fails Miserably How to Bled or Purge Zones" (`cygl4HHnzdk`, 247K views, 31:54) | 207K (About, about.json) |
| 20 | DEBOSS GARAGE | `UCLXV9vzJwgYOyGaZlD89VfA` @DEBOSSGARAGE | 6 (5) | 1 | 0 | heating-adjacent: diesel heaters (reading) | "Make a $100 Amazon Diesel Heater Even Better With This Simple Trick" (`XfzCeXlDq0A`, 1.8M views, 26:11) | not found |
| 21 | Japan with Nao | `UCBK3AwEX1vL8qky015Z93vA` @JapanwithNao | 6 (6) | 1 | 0 | partly: Japanese homes without central heating (reading) | "No Central Heating? Here's What Japanese Homes Do Instead" (`FsmLvHuA96M`, 1.8M views, 14:32) | 91.1K (About, this pull) |
| 22 | HOBOTECH | `UCVsNMiYQkqwIq_gd0rTJF9g` @HOBOTECH | 6 (6) | 0 | 5 | yes (portable / battery ACs for van and camping) (reading) | "BEST PORTABLE 12v-48v A/C! "EcoFlow Wave 3" 6100 BTU Battery Air Conditioner Heater" (`-rQD-9onhFQ`, 748K views, 39:11) | 309K (About, this pull) |
| 23 | The Funny Carpenter | `UCgx_ERh6IE-Td3FLJstu1iQ` @TheFunnyCarpenter | 6 (4) | 0 | 1 | mostly no (1 of 8 titles; reading) | "5 Furnace Filter Mistakes That Will Cost You Money!" (`_g8gQ1gg1FM`, 2.8M views, 5:34) | 783K (About, about.json) |
| 24 | Jersey Mike HVAC | `UCxzAJacWR8mwOcUbplo9U-A` @JerseyMikeHVAC | 6 (6) | 0 | 1 | yes (6 of 6 titles; reading) | "Purging Air From A Boiler System (Residential)" (`F4OdgpqKkzw`, 188K views, 14:34) | 55.5K (About, this pull) |
| 25 | Joshua De Lisle | `UC-5at4izid5vmBmbMd0RylQ` @joshuadelisle | 6 (5) | 0 | 0 | heating-adjacent: diesel heaters (reading) | "Free heating fuel but it's illegal - £120 8kw Diesel parking heater review from VEVOR" (`KyiUpFjwtlU`, 4.9M views, 24:38) | 333K (About, this pull) |
| 26 | Craftsman Chris | `UCaKBU_jFbCCRbw8LEe5LIrw` @craftzmanchris9859 | 5 (5) | 5 | 0 | yes (12 of 12 titles; reading) | "Turning a Dumpster AC Into a Super-Efficient Geothermal Heat Pump" (`GfMNLWzaUHU`, 765K views, 31:16) | 50.7K (About, this pull) |
| 27 | Ramón Delgado | `UC6nh_16KkkMHjccUXBNPEfQ` @FixTheMexicanWay | 5 (5) | 4 | 0 | yes: cooling/heating 'The Mexican Way' (reading) | "This Is How We Cool Our House Without AC (The Mexican Way)" (`k1HGyewDZ_k`, 958K views, 23:12) | 33.4K (About, this pull) |
| 28 | Fer's Reviews | `UCj4ILMwnfh-fmMk6Fg1BynA` @FersReviews | 5 (5) | 3 | 4 | yes (8 of 8 titles; reading) | "How To Install A Mini Split Air Conditioner – Complete Step-By-Step Guide" (`AQ4EYHNCDzg`, 663K views, 24:22) | 11.3K (About, this pull) |
| 29 | Linus Tech Tips | `UCXuqSBlHAE6Xw-yeJA0Tunw` @LinusTechTips | 5 (4) | 2 | 1 | no: tech (one AC video) (reading) | "I Have Strong Feelings About Air Conditioning in the Tech House" (`1H20xp8Brnc`, 1.9M views, 21:04) | 16,900,000 (NexLev sim-ch, 2026-10-22) |
| 30 | John The HVAC Guy | `UCOyYTw-deou3ax6gvCmX2dg` @JohnTheHVACGuy | 5 (5) | 2 | 0 | yes (7 of 7 titles; reading) | "9 Furnaces That NEVER Break Down (Buy Once, Heat Forever)" (`FgO_twJeHJ0`, 14K views, 30:06) | 7.13K (About, about.json) |
| 31 | Technology Connections | `UCy0tKL1T7wFoYcxCe0xjN6Q` @TechnologyConnections | 5 (5) | 1 | 6 | partly: tech explainers incl. portable AC, heat pumps (reading) | "Portable Air Conditioners - Why you shouldn't like them" (`_-mBeYC2KGc`, 10M views, 16:39) | 3.22M (About, about.json) |
| 32 | Adventure Gear TV | `UCm3B_8DYaxvCoK_337_ACGw` @AdventureGearTV | 5 (5) | 1 | 5 | partly: portable ACs for camping (reading) | "What Nobody Says About Portable AC Units: Zero Breeze Mark 3" (`knBKw9FrxgE`, 193K views, 22:25) | 128K (About, this pull) |
| 33 | Skill Builder | `UC9GdB6vG6m6cDAwrTAWXgyg` @SkillBuilder | 5 (5) | 0 | 2 | yes (8 of 8 titles; reading) | "Expert Reveals Secrets to REPLACING A HEATING PUMP" (`8su-UOh8_wE`, 334K views, 8:25) | 749K (About, about.json) |
| 34 | Stud Pack | `UCjG94SagJZoyPggcBhUdFCA` @StudPack | 4 (3) | 4 | 1 | yes (6 of 8 titles; reading) | "How To Clean Your AC Condenser! - The ULTIMATE Step-by-Step Guide!" (`tWeRkOpRpB0`, 181K views, 24:36) | 813K (About, this pull) |
| 35 | The Thought Provocateur | `UCVyfrw6CcrxavbVBxviKiSQ` @thethoughtprovocateur | 4 (4) | 3 | 4 | yes (7 of 7 titles; reading) | "5 most common Boiler Problems 🔥🛠️" (`VrGeQ0wdfQ8`, 86K views, 9:44) | 110K (About, this pull) |
| 36 | Yarbrough & Sons Heating, Cooling & Plumbing | `UCOtjEgHlsAxG0YNzaSVIOgw` @yarbrough_and_sons | 4 (4) | 3 | 0 | yes (9 of 9 titles; reading) | "Ranking the Best and Worst Mini Split Brands" (`yIOmar-8Rl0`, 258K views, 12:49) | 5.68K (About, about.json) |
| 37 | CaptiveAire | `UCt0ArHe_-CKAr1So3IEwmsA` @CAPTIVEAIRE | 4 (4) | 1 | 1 | partly (1 of 5 titles; reading) | "HVAC Maintenance / A Step-by-Step Guide" (`TDMlGDtu20s`, 35K views, 39:15) | not found |
| 38 | steven lavimoniere / PLUMBING HEATING & AC VIDEO'S | `UC4mZGMmJ1kOaOG1oRACZDbQ` @stevenlavimoniere | 4 (4) | 0 | 2 | yes (12 of 12 titles; reading) | "OIL FIRED BECKETT FURNACE WILL NOT FIRE UP -JUST SERVICED" (`ztCb3QKO6zI`, 87K views, 15:48) | 213K (About, about.json) |
| 39 | CNET and 4 more | `UCOmcA3f_RrH6b9NmcNa4tdg` @CNET | 4 (4) | 0 | 2 | partly (1 of 4 titles; reading) | "AC Powered by the Sun? Testing the EcoFlow Wave 3 / Prove It" (`8ts0wjBaDKw`, 58K views, 7:24) | not found |
| 40 | Jay Of All Trades | `UCSsBkNmIaBWj-B7c0dNbzoA` @JayOfAllTrades1 | 4 (4) | 0 | 1 | yes (4 of 4 titles; reading) | "How to Replace an Oil Burner Nozzle / One Year Later" (`nUhDDJ8fHx0`, 1.3K views, 18:53) | 5.85K (About, this pull) |
| 41 | RealHouseDIY | `UC6RIV9eUSn1mW8jjbPFwK6A` @realhouseDIY | 4 (4) | 0 | 0 | yes (7 of 7 titles; reading) | "Gas Boiler Overview - Crane 100 Series with Honeywell Controls - Hot Water Baseboard Radiator" (`OIqQ9t5vsv4`, 34K views, 10:31) | 14.6K (About, this pull) |
| 42 | HAXMAN | `UCgFkhHePN1RqdTRsBFSvAVQ` @HAXMAN | 4 (1) | 0 | 0 | partly (1 of 5 titles; reading) | "Is DIY Spray Foam A Scam? I Tested It On A Shed" (`sJLJozISnAU`, 670K views, 20:00) | not found |
| 43 | Fix It With Zim | `UCvYKGi_PXOpd4-YCS0UOPYA` @fixitwithzim | 4 (4) | 0 | 0 | yes (4 of 4 titles; reading) | "Remove Air from your Boiler and Heating System / How To" (`voS7Url50M4`, 1.1M views, 16:25) | 41.4K (About, this pull) |
| 44 | Chuck Kososky | `UC3sPVoO93NhSdJ_vi4FpGfA` @AllThingsCool | 4 (4) | 0 | 0 | heating-adjacent: diesel heaters (reading) | "Why you Should Buy the New Upgraded Vevor Diesel Heater" (`b900VSyTb-I`, 419K views, 10:36) | 49.2K (About, this pull) |
| 45 | There's A Trick For That | `UCcPAcUV5haCy4Y46t-VsRWA` @theresatrickforthat | 3 (3) | 4 | 5 | yes (10 of 10 titles; reading) | "How to Install a $360 Mini Split Heat Pump — Complete DIY Guide" (`uv75G4ed2dw`, 555K views, 18:12) | 90.9K (About, about.json) |
| 46 | Red Beard Engineered | `UCUiHxNYiHc1qeZ6CYaXzitQ` @redbeardengineered | 3 (3) | 4 | 3 | yes (9 of 9 titles; reading) | "This MINI-Split AC System Changed My Life / Learn How To Install One Yourself" (`FditJqUenAk`, 1M views, 14:46) | 9.37K (About, this pull) |
| 47 | RR Buildings | `UCWXEQsK3UiHszjwgGN5HUeQ` @RRBuildings | 3 (3) | 4 | 3 | yes (7 of 7 titles; reading) | "Pro Level Mr Cool DIY Install in less than 1 day!" (`VxWH4J1jM8I`, 779K views, 52:09) | 1.86M (About, this pull) |
| 48 | Minute Man Solar | `UCWm9NBXq1HWoIxfYLdIPS_Q` @minutemansolar | 3 (2) | 3 | 3 | partly (3 of 6 titles; reading) | "The Truth About Cheap Mini Splits [Don't Be Fooled]" (`bELnEH7jJGc`, 114K views, 12:44) | 146,000 (NexLev sim-ch, 2026-10-22) |
| 49 | Modern Builds | `UCIxAaCJ84uefATKmazDyIjw` @ModernBuilds | 3 (3) | 2 | 3 | yes (5 of 5 titles; reading) | "DIY Multi-Zone Ductless Mini Split AC & Heating System / MR Cool Install 2021" (`7lrgnM90pQY`, 1M views, 14:37) | 1.85M (About, this pull) |
| 50 | CarlTheLandscapeGuy | `UC9PvGNz3BZVN7EU2SL0SyZg` @CarlTheLandscapeGuy | 3 (3) | 2 | 1 | yes (5 of 5 titles; reading) | "AIR CONDITIONER DETAIL INSTALL /SPLIT DUCTLESS AC HEATING INVERTER,MINI PUMP SYSTEM SETUP,DIY HOW TO" (`2RDfAkmDId0`, 7.8M views, 27:53) | 104K (About, this pull) |
| 51 | The Excellent Laborer | `UCUJXaEduMHGB3Iap3DusmAA` @TheExcellentLaborer | 3 (3) | 2 | 0 | yes (4 of 5 titles; reading) | "How To Install An AC disconnect - ALL WIRING!" (`0gS0Pw_YCuE`, 490K views, 14:53) | not found |
| 52 | Precision Metal | `UC31d5ED-_bJ7BR4hKEZSmCg` @precisionmetalin | 3 (2) | 2 | 0 | heating-adjacent: DIY wood heater for a shop (reading) | "How I’m Heating My 2,100 Sq Ft Shop with a $257 DIY Wood Heater" (`giBj9uY5SdI`, 1.1M views, 27:19) | 35.9K (About, this pull) |
| 53 | The Kelley's Country Life | `UCq6YaxJHA-t4bYBHHvaoZ8w` @TKCL | 3 (2) | 2 | 0 | yes (5 of 5 titles; reading) | "Step By Step Della Mini Split Install! DIY" (`lrtojOjTF5c`, 195K views, 35:52) | 226K (About, this pull) |
| 54 | World of HVAC | `UC0KNvNxxtc_NKRzM_JDzJSg` @WorldofHVAC | 3 (3) | 1 | 3 | yes (4 of 4 titles; reading) | "Testing 5 Coil Cleaners To See Which Brand Is The Best!" (`asytum1GWNE`, 55K views, 14:51) | 13.7K (About, this pull) |
| 55 | ChrisFix | `UCes1EvRjcKU4sY_UEavndBw` @chrisfix | 3 (3) | 1 | 2 | no: cars (its 'cooling system' video is a car radiator) (reading) | "How to SUPER FLUSH your Cars Cooling System" (`s--5ft5YiHg`, 19M views, 22:07) | 11,300,000 (NexLev sim-ch, 2026-10-22) |
| 56 | Fix This Build That | `UCHYSw4XKO_q1GaChw5pxa-w` @Fixthisbuildthat | 3 (1) | 1 | 0 | partly (2 of 4 titles; reading) | "Why Don’t People Do This Before Calling an HVAC Tech?" (`ActRTlyS82g`, 93K views, 30:31) | 2.2M (About, about.json) |
| 57 | Clean That Up | `UC1GLDECMH83KqDn6hypodYw` @CleanThatUp | 3 (3) | 1 | 0 | yes (4 of 4 titles; reading) | "The Best Way to Clean Your AC Unit and Coils!" (`l_4kBGL3mPg`, 2.3M views, 8:50) | 1.38M (About, this pull) |
| 58 | grayfurnaceman | `UCchpiPYTBEg4DpK6mKfYi2A` @grayfurnaceman | 3 (3) | 0 | 3 | yes (4 of 4 titles; reading) | "Oil furnace troubleshoot part 2 No flame" (`TfPnLUz1Vh4`, 1M views, 11:47) | 167K (About, about.json) |
| 59 | Freakin' Reviews | `UCTCpOFIu6dHgOjNJ0rTymkQ` @Freakinreviews | 3 (3) | 0 | 3 | yes (3 of 3 titles; reading) | "Arctic Air Ice Jet vs Pure Chill: Ultimate Cooling Showdown!" (`T6eo4GuwlNs`, 388K views, 10:24) | 875K (About, this pull) |
| 60 | Salty Trips | `UCHlIZmdc0b_hNQJTN4N5Enw` @saltytrips | 3 (3) | 0 | 2 | yes (3 of 3 titles; reading) | "Portable Air Conditioner for RV by EnjoyCool #rvliving #rvlife" (`OHjz1H8hcS4`, 58K views, 11:37) | not found |
| 61 | Andrew W | `UCAn_HKnYFSombNl-Y-LjwyA` @AndrewWorkshop | 3 (3) | 0 | 1 | yes (3 of 4 titles; reading) | "How to Change a Circulator Pump - Hot Water Heating Hydronic" (`9hcaV5v0RA8`, 74K views, 12:08) | 146K (About, this pull) |
| 62 | HouseImprovements | `UCpJ1vJPFqImom-NN2fkBS0A` @HouseImprovements | 3 (2) | 0 | 1 | yes (2 of 3 titles; reading) | "How To Clean Your Air Conditioner Condenser" (`HAIXiCDuEWI`, 2.6M views, 13:09) | 993,000 (NexLev sim-ch, 2026-10-22) |
| 63 | PatriotDIY | `UC1usuCeFHj1tQikOJ00SWyA` @PatriotDIY | 3 (2) | 0 | 1 | yes (2 of 3 titles; reading) | "How To Clean A Ductless Mini Split Air Conditioner / Mr Cool" (`x8c_-5zHi_o`, 305K views, 15:44) | not found |
| 64 | OldSoulMillennial | `UCooulUwMsi9jJpOz7wfYR5Q` @OldSoulMillennial | 3 (3) | 0 | 1 | yes (3 of 3 titles; reading) | "How to Bleed AIR from Baseboard heating system" (`uqzDEjFqfpk`, 232K views, 7:34) | not found |
| 65 | HVAC Exposed | `UCZ1IwSV46bb09fMvqHn6_2A` @HVACExposed | 3 (3) | 0 | 0 | yes (3 of 3 titles; reading) | "How Smart Homeowners Are Beating the HVAC Industry (The 15-Year Loophole)" (`wz-06sf2Dy0`, 382K views, 13:03) | 9.59K (About, about.json) |
| 66 | TheWXTV | `UCe8AWQ-hpWaO6JXw1jDJ_2Q` @TheWXTV | 3 (3) | 0 | 0 | yes (3 of 3 titles; reading) | "Boiler Basics: Part III - External Components" (`3NVZFAcqDOk`, 939K views, 11:09) | 15.5K (About, this pull) |
| 67 | HVAC Service Mentor | `UC_wC1rbMeYAv0qQUj6YmFcw` @hvacservicementor | 3 (3) | 0 | 0 | yes (3 of 3 titles; reading) | "How to set hot water boiler pressure" (`D9jtvsXJoGg`, 96K views, 18:48) | 13.2K (About, this pull) |
| 68 | Mick's Air Con | `UCwrRvd_li-w3r0SVii1YpPw` @MicksAirCon | 2 (2) | 5 | 0 | yes: split-system AC (Australian wording), 42 subs (reading) | "Split System vs Ducted Air Conditioning — What a Technician Would Install" (`tBuc6KDjcGM`, 3.5K views, 15:10) | 42 (About, this pull) |
| 69 | M.T. HOMES | `UCDPFMkd53-DJQpI4HJqyllA` @MT_Homes | 2 (2) | 4 | 0 | yes (6 of 6 titles; reading) | "HOW TO INSTALL A DIY MINI SPLIT (no HVAC tools required)" (`8olWmuMMt8k`, 136K views, 31:26) | 32.5K (About, this pull) |
| 70 | alpinehomeair | `UCMvzPcAmmdFJr6Yk-2v0k-w` @alpinehomeair | 2 (2) | 3 | 3 | yes (5 of 5 titles; reading) | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" (`DzVJiSQNbew`, 13M views, 9:16) | 39.6K (About, this pull) |
| 71 | I Like To Build Stuff | `UCsS2CuRMlB83sdafJOCvY1A` @ILikeToBuildStuff | 2 (2) | 3 | 1 | yes (6 of 6 titles; reading) | "DIY Dual Zone Mini Split Install - This SAVES You Thousands!" (`z9elRDw3faM`, 702K views, 37:40) | 16.4K (About, this pull) |
| 72 | Miillers Construction | `UCK9DXL31fZSNi3h7DTqTyzg` @miillersconstruction | 2 (2) | 3 | 1 | yes (5 of 5 titles; reading) | "We Filmed the Most Detailed Mini Split Install on the Internet / TOSOT Aoraki" (`vEdHIRHoJ60`, 36K views, 54:34) | not found |
| 73 | HomePro Hero | `UCmPc7lvTIm-J9GmvQku5wAw` @HomeProHero | 2 (2) | 3 | 1 | yes (5 of 5 titles; reading) | "DIY Mini‑Split Install: TOSOT vs Mr Cool vs Della" (`Bbkg2y6gaQY`, 326K views, 19:19) | 73.5K (About, this pull) |
| 74 | Exposi | `UCQCRIhHQ__ncUxtOHiIXI4A` @Exposerosi34 | 2 (2) | 3 | 0 | yes (7 of 7 titles; reading) | "Doing This Will Make Your AC Run Like NEW Again!" (`ExzlvE5GfX8`, 329K views, 14:07) | 2.52K (About, about.json) |
| 75 | TheCheapFix and John Brown | `UC7xrSTuKm8YPd2l6WPgMt-g` @TheCheapFix | 2 (2) | 3 | 0 | yes (4 of 5 titles; reading) | "11 Things HVAC Technicians Don't Want You to Know About Hydrogen Peroxide! (#8 Saves $900)" (`yIh1HAlbhc0`, 1M views, 14:58) | 66.1K (About, about.json) |
| 76 | craftsman tv | `UCTn8OBw8WEVtZtI_BVrbHXw` @craftsmantv7205 | 2 (2) | 3 | 0 | yes (5 of 5 titles; reading) | "Multi-zone split type Air Conditioner installation" (`v586WsJn-dk`, 1.3M views, 16:49) | 61.6K (About, this pull) |
| 77 | The Fixer | `UCZ32JAyPXVY2f3g2VxekBjA` @TheFixerHomeRepair | 2 (2) | 2 | 1 | partly: window-AC cleaning + dryer vents (reading) | "How to SUPER CLEAN Your Dryer and Dryer Vents!" (`lJv1Eu77cHM`, 2.1M views, 26:59) | 671K (About, about.json) |
| 78 | Grain & Gravity | `UCqrSZXBGR6kD4ZMx9WLSqig` @GrainandGravity | 2 (0) | 2 | 0 | mostly no (1 of 7 titles; reading) | "This $3 HOME DEPOT OUTLET Heats Your Whole House WITHOUT A Generator. Why Aren't We Using Them?!" (`D_EnUK1O9bY`, 16K views, 30:42) | not found |
| 79 | Richard Nakamura Secrets | `UClcy6Bt3jTQZDPtxXa-lxSw` @richnakasecret | 2 (2) | 2 | 0 | yes (3 of 4 titles; reading) | "I Fixed The Worst Problem With Portable AC Units! (Easy Fix)" (`kuEuMUyHz3s`, 115K views, 17:21) | not found |
| 80 | The French Glow | `UCEP78fa8psaWGvQMP4APtMA` @TheFrenchGlow | 2 (2) | 1 | 4 | yes (3 of 3 titles; reading) | "Don’t Buy a Cheap Portable AC. They’re a Trap." (`9G7TcoT7Nyc`, 44K views, 12:16) | 39,400 (NexLev sim-ch, 2026-10-22) |
| 81 | HVAC Guide for Homeowners | `UCp_5AZlvvW9jn6L4EZuCbNQ` @NewHVACGuide | 2 (2) | 1 | 3 | yes (4 of 4 titles; reading) | "Mini-Split Location Matters! EXPERT TIPS!" (`2WReKNtj87Y`, 253K views, 11:44) | 169K (About, about.json) |
| 82 | Undecided with Matt Ferrell | `UCjtUS7-SZTi6pXjUbzGHQCg` @UndecidedTechnology | 2 (2) | 1 | 1 | yes (5 of 8 titles; reading) | "Why This Window Heat Pump Is Genius" (`KNlDu_ZHIo8`, 1.5M views, 13:24) | 1.81M (About, about.json) |
| 83 | Anti DIY HVAC | `UCFxf3hjNRSQ706L3jgDYnBw` @TedCookHVAC | 2 (2) | 1 | 1 | yes (5 of 5 titles; reading) | "AC Drain Clogged P Trap last place I looked" (`bLshRVFnnh4`, 83K views, 15:09) | 78.4K (About, about.json) |
| 84 | AmplifyDIY | `UC1sPYHJYgJppmlkhi1AekuQ` @AmplifyDIY | 2 (2) | 1 | 1 | yes (3 of 3 titles; reading) | "How To Clean Your Air Conditioner Condenser Coil (Step By Step)" (`_M-JLzIQHtk`, 1.9M views, 8:20) | not found |
| 85 | Consumer Analysis | `UCNhyZZ8OotnN9E1rQYriuiA` @consumer-analysis | 2 (2) | 1 | 1 | yes (3 of 3 titles; reading) | "Single vs Dual Hose Portable Air Conditioners" (`WMIKrW5131s`, 365K views, 8:25) | not found |
| 86 | Footprint Hero with Alex Beale | `UCLnGgnj-hneDI3CFzBmdGLg` @footprinthero | 2 (1) | 1 | 0 | partly (2 of 5 titles; reading) | "I Bought Amazon's #1 Device for Lowering Your Electric Bill" (`Pp87kTvyiqk`, 910K views, 17:20) | 215K (About, about.json) |
| 87 | Roger the Pipe Guy | `UCR2C--KENITllxSo1aAbWWA` @RogerthePipeGuy | 2 (1) | 1 | 0 | operator's own plumbing channel (AC drain-line video) (reading) | "Pour One Cup of Vinegar Down Your AC's Drain Line Today (Before It Floods Your Ceiling)" (`cFYptbCvNjI`, 36K views, 23:30) | 76.5K (About, this pull) |
| 88 | Home RenoVision DIY | `UCnorhjQR4zJkT7AVNhu395Q` @HomeRenoVisionDIY | 2 (1) | 1 | 0 | partly (1 of 4 titles; reading) | "THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique!" (`J95l9Ue4224`, 5.8M views, 18:21) | 4.31M (About, about.json) |
| 89 | JAMIE AND SARAH | `UCvRnm6z-xSXgFs01W7l2JAA` @JAMIEANDSARAH | 2 (2) | 1 | 0 | yes (3 of 3 titles; reading) | "DIY Mini Split - MRCOOL Multi-Zone Install Start to Finish" (`5whzTEKo33k`, 64K views, 21:11) | not found |
| 90 | HobbyJohnDo | `UCCrtUWbEpfj3puNv19sVXHQ` @HobbyJohnDo | 2 (2) | 1 | 0 | yes (3 of 3 titles; reading) | "Before You Pay $300 to Clean Your AC, Watch This!" (`QtTW7BwdaUw`, 10K views, 5:06) | not found |
| 91 | Jumper man Tech | `UCUisLZYxDNx-rKrgCcDDO5A` @JumpermanTech | 2 (2) | 1 | 0 | yes (3 of 3 titles; reading) | "HVAC: How To Clean A Commercial Air Conditioner (Condenser/Evaporator Coil Cleaning) Acid Wash RTU" (`toW2c3h9dKU`, 356K views, 16:19) | not found |
| 92 | A2Z Construction | `UCtdNnHQQeUXT0H1tsRuJqtQ` @A2ZConstruction | 2 (2) | 1 | 0 | yes (3 of 3 titles; reading) | "Split Air Conditioner Installation Step By Step / Actual Installation Cost" (`9nbK1FFBC7U`, 4.1M views, 15:58) | not found |
| 93 | seejanedrill | `UCraGaDLfWec67xl9FEPndtw` @seejanedrill | 2 (2) | 1 | 0 | yes (3 of 3 titles; reading) | "I saved $4,200 installing a mini split AC myself" (`gosqASYxwgY`, 1M views, 16:32) | not found |
| 94 | HVACR Survival | `UC7EJjONRyeihmQELDIFF8qQ` @HVACRSurvival | 2 (2) | 1 | 0 | yes (3 of 3 titles; reading) | "I HATE Mitsubishi MiniSplits" (`XFFkHYWdqjs`, 171K views, 15:41) | not found |
| 95 | Air Conditioner Lab | `UC7_ZnG9TKRWsxPRa0-WnTOw` @AirConditionerLab | 2 (2) | 0 | 5 | yes (5 of 5 titles; reading) | "6 Best Portable Car Air Conditioners - Cooling Relief In Your Vehicle" (`XmKamPp-QtQ`, 151K views, 6:27) | not found |
| 96 | Computer Clan | `UCQ6fPy9wr7qnMxAbFOGBaLw` @ComputerClan | 2 (2) | 0 | 4 | yes (2 of 2 titles; reading) | "Is Chillwell Portable AC a Scam? (Yes, Here’s Why) - Krazy Ken’s Tech Talk" (`URxSoHpwIz8`, 1.7M views, 21:25) | not found |
| 97 | DIY Creators | `UChKlSK39lLg8eZHIX0iVzLA` @DIYCreators | 2 (2) | 0 | 3 | yes (2 of 2 titles; reading) | "How to install a Central AC & Heating System step by step // Senville HVAC DIY" (`wBn84EtALbI`, 380K views, 34:52) | not found |
| 98 | Charbax | `UC_VskFf9nosePUtxucxirRQ` @charbax | 2 (2) | 0 | 3 | yes (2 of 2 titles; reading) | "$210 Mini portable air conditioner for camping by Foshan Zhenyun Refrigeration Technology Co., Ltd." (`r0xbDV9NNSg`, 64K views, 7:17) | not found |
| 99 | Consumer Betterment | `UCrtvRaGLiPPWm0QNbRg0T6A` @ConsumerBetterment | 2 (1) | 0 | 3 | yes (2 of 2 titles; reading) | "8 Best Portable Air Conditioners for Staying Cool in 2026" (`-Ssdpil9dsY`, 5.8K views, 11:27) | 57,600 (NexLev sim-ch, 2026-10-21) |
| 100 | Quality HVACR | `UC2AsqyR6xLMkte3mQHf-umw` @QualityHVACR | 1 (1) | 5 | 1 | yes (8 of 8 titles; reading) | "#1 Reason Why DUCTLESS Units Fail / How I Fix It..." (`QjTXu1pMlGA`, 1M views, 13:59) | 132K (About, about.json) |
| 101 | Hank Cole | `UC5NJ3yYhsZFkfWLJJJVoxMA` @HankColeUS | 1 (1) | 3 | 0 | yes (5 of 5 titles; reading) | "The $5 Fix That Makes Your AC Blow 9° Colder — 40 Years In, Nobody Tells You This" (`HPYZfXWGzjQ`, 156K views, 12:49) | 1.37K (About, about.json) |
| 102 | Electrum Electrical | `UC2veDhI08nz8VvM0Pj8Xvcw` @electrumelectrical | 1 (1) | 3 | 0 | yes (4 of 4 titles; reading) | "7 things you need to know before getting air con installed" (`6lTEQI2tLVc`, 127K views, 7:31) | not found |
| 103 | Wild Line | `UC1AtJIwlt9tI-Z-QKQJJ_Vw` @wildline_YT | 1 (0) | 2 | 2 | yes (4 of 4 titles; reading) | "Why Did We Stop Using This Natural Cooling System?" (`SVuQqEXaWdw`, 2.1M views, 12:07) | 80.1K (About, about.json) |
| 104 | Crafted Workshop | `UC-hTi9atsD6wAl2s46LpAVw` @craftedworkshop | 1 (1) | 2 | 2 | yes (3 of 3 titles; reading) | "DIY MULTI-ZONE Ductless MINI SPLIT Installation in New Construction!" (`KD2GM0fg8eU`, 776K views, 17:14) | not found |
| 105 | HVAC Mechanic | `UC5j2jKeDj5pkr-ie1TyMHQw` @HVAC_Mechanic | 1 (1) | 2 | 1 | yes (5 of 5 titles; reading) | "Step by Step How to Vacuum Down Mini Split Using Analog Gauges Release Refrigerant Check for Leaks" (`DgaPPyAZSTs`, 198K views, 10:56) | not found |
| 106 | DIY Solar Power with Will Prowse | `UCoj6RxIAQq8kmJme-5dnN0Q` @WillProwse | 1 (0) | 2 | 1 | partly (2 of 4 titles; reading) | "Budget Mini Split Installation for Beginners! w/ Vacuum Pump and Gauges" (`5trJX6Ef1iI`, 840K views, 19:47) | not found |
| 107 | Blue Bulldog Plumbing | `UC1am9-qDtiXGT9tAe6La6pQ` @bluebulldog_uk | 1 (1) | 2 | 0 | yes (6 of 6 titles; reading) | "Worcester Bosch CL3200i Air Conditioning Installation / Full Installation " (`CwvTXWMZPvk`, 121K views, 52:05) | not found |
| 108 | Frugal Folks Garage | `UCM1qfMnYkAqeRNA04S_tLlw` @FrugalFolksGarage | 1 (1) | 2 | 0 | yes (3 of 3 titles; reading) | "DIY HVAC Maintenance: Save Hundreds Without Calling a Technician (Air Handler & Condenser Cleaning)" (`JDlPVhleV8A`, 249K views, 13:59) | not found |
| 109 | Tech Ingredients | `UCVSHXNNBitaPd5lYz48--yg` @TechIngredients | 1 (1) | 2 | 0 | yes (3 of 3 titles; reading) | "Turning a $150 AC Into a Super-Efficient Geothermal Unit!" (`s-41UF02vrU`, 2.7M views, 57:43) | not found |
| 110 | Backyard Low Tech | `UCSedPjb56LMeiq_VV8164OA` @BackyardLowTech | 1 (1) | 2 | 0 | yes (3 of 3 titles; reading) | "This Window Heat Pump Plugs Into 115V — But Stops Being the Answer at 40°F" (`FxtDaRsY-cQ`, 8K views, 18:36) | 12.2K (About, about.json) |
| 111 | The Passive House Files | `UCx0OIvHyA-rLE1_jHfrJTbQ` @griffithselijah7018 | 1 (1) | 2 | 0 | yes (2 of 3 titles; reading) | "This $12 Device Makes Your AC Bill 90% Cheaper. Why Is Nobody Talking About It?" (`CxNTiX1Waak`, 64K views, 28:27) | 73.5K (About, about.json) |
| 112 | Broken Branch DIY | `UCE_98I9-o_axbL0-tBHLAiQ` @BrokenBranchDIY | 1 (1) | 2 | 0 | yes (3 of 3 titles; reading) | "Top 3 Reasons Your AC Isn’t Blowing Cold Air🔥❄️" (`4I_jIp1bpq8`, 6.4K views, 20:18) | not found |
| 113 | Foremost Picks | `UC5lBPQsMMJEE5PTJMzf_sug` @TheForemostPicksof2027 | 1 (1) | 1 | 4 | yes (2 of 2 titles; reading) | "✅ Best Portable Air Conditioner 2026 [Find Which One is Right for YOU?]" (`zGCme5_xapw`, 33K views, 8:48) | 35,700 (NexLev sim-ch, ) |
| 114 | MRCOOL | `UCa3r1wr9L-2HVXKLlf2FeuQ` @MrcoolComfort | 1 (1) | 0 | 4 | yes (3 of 3 titles; reading) | "How to Use the Remote for the MR COOL DIY Ductless Mini Split" (`cDnK1C5l1CU`, 581K views, 3:18) | not found |
| 115 | Scamadviser | `UCERAPMuOxhqOg6WqIDR1G2w` @ScamadviserYoutube | 1 (1) | 0 | 4 | yes (1 of 1 titles; reading) | "Epicooler Portable AC Genuine Review - Let’s See If It’s a Legit Air Conditioner Or Scam!" (`PgzIy5kkP1E`, 314K views, 2:40) | not found |
| 116 | Home Caprice | `UCgm8JAXkb9MpHQwKaksj4PA` @homecapricehc | 1 (1) | 0 | 3 | yes (1 of 1 titles; reading) | "Dry Mode in Air Conditioners Explained [Quick Overview]" (`ANcISCxrvTQ`, 791K views, 5:34) | not found |
| 117 | FarmCraft101 | `UCO4AaIooUgGTlBH64KWO76w` @FarmCraft101 | 0 (0) | 4 | 1 | yes (3 of 4 titles; reading) | "DIY Mini Split Install: Mr. Cool, Multi Zone System." (`enDmWk5QKF8`, 355K views, 53:28) | not found |
| 118 | rowe robles and The Firearms Bench | `UCCioen-NhBnRx23njAOGO4w` @rowerobles6322 | 0 (0) | 3 | 0 | yes (2 of 3 titles; reading) | "Only 1% of HVAC Technicians Know This AC Trick (USE IT NOW)" (`bk1Bvq4Kx7o`, 1.2K views, 25:04) | not found |
| 119 | Ask Big Jim. | `UCMDHm9pBWFY8r1NUkyWxPBw` @ask.big.jim01 | 0 (0) | 3 | 0 | yes (3 of 3 titles; reading) | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" (`f4lEHVgqU3I`, 10K views, 13:37) | 437 (About, about.json) |
| 120 | The Cooler | `UCZ9yiigZbPeeDZs1ze0QaCQ` @TheCoolerYT | 0 (0) | 3 | 0 | yes (3 of 3 titles; reading) | "The Only 3 Mini Splits Worth Buying in 2026 (Everyone Else Is Wasting Your Money)" (`18o412r4IXA`, 6K views, 25:57) | not found |
| 121 | HeatAndCool.com | `UCTppb1CuxtXej-1JE4BxoZg` @HeatAndCool | 0 (0) | 3 | 0 | yes (3 of 3 titles; reading) | "Klimaire Mini Split Installation" (`0whZxKT4BF0`, 1.5K views, 18:22) | not found |
| 122 | Robert Longechal | `UCc_pRip5WE5RRxadu6mL1hw` @robertlongechal | 0 (0) | 3 | 0 | yes (3 of 3 titles; reading) | "How to easily install a dual split reversible air conditioner - DIY tutorial with Robert" (`3DV8zQtDMeA`, 2.2M views, 17:18) | not found |
| 123 | Lowe's Home Improvement | `UCqd2hbtE2N9fb0D2nTrLT1w`  | 0 (0) | 0 | 5 | not read (NexLev similar only) | "How To Clean an Air Conditioner" (`pzDNFuiAESE`, 2,536,381 views [NexLev], 1:38) [NexLev similar] | 1,350,000 (NexLev sim-ch, 2026-10-22) |
| 124 | TECH GARAGE | `UC9p3gKPCS8PF9ZeNbnrtaGg`  | 0 (0) | 0 | 4 | not read (NexLev similar only) | "Should You Buy a PORTABLE AC in 2024? / All Pros & Cons" (`llG5z3yKsyU`, 117,157 views [NexLev], 5:58) [NexLev similar] | not found |
| 125 | The Air Of Authority | `UCXuC2KTVSVH7sS7bNkirRZQ`  | 0 (0) | 0 | 3 | not read (NexLev similar only) | "Air Conditioner Not Cooling Enough [2 Simple Checks to Do Yourself]" (`4zpLPkeZZxg`, 1,078,140 views [NexLev], 4:10) [NexLev similar] | 32.4K (About, about.json) |
| 126 | RepairClinic.com | `UCGIWoFCiw_H5SW4sHWFzQSw`  | 0 (0) | 0 | 3 | not read (NexLev similar only) | "Central Air Conditioner Not Cooling — Central Air Conditioner Troubleshooting" (`REdKaGJDktI`, 39,538 views [NexLev], 3:12) [NexLev similar] | not found |
| 127 | Monkey Wrench Plumbing, Heating, Air & Electric | `UCAiLfdXEsKVOAarqANjSweQ`  | 0 (0) | 0 | 3 | not read (NexLev similar only) | "12 types of heating systems for your home" (`pPziS7RHoBM`, 90,843 views [NexLev], 7:30) [NexLev similar] | 10.2K (About, about.json) |
| 128 | ZERO BREEZE | `UCu67ms6tiDFP4GZ0GoCJ2og`  | 0 (0) | 0 | 3 | not read (NexLev similar only) | "How to Set up the ZERO BREEZE Mark 2 Portable A/C in Your Van" (`ss_rZINSBGQ`, 46,878 views [NexLev], 1:32) [NexLev similar] | not found |
| 129 | Smiles Per Hour | `UCcOrqZYw3DK0oStenY1oaVg`  | 0 (0) | 0 | 3 | not read (NexLev similar only) | "Do Portable Air Conditioners REALLY work? (Rintuf 12K BTU Review)" (`oGar5fF0UAY`, 282,017 views [NexLev], 6:40) [NexLev similar] | not found |


**Known channels from the brief, where they landed:** The DIY HVAC Guy #1 (15 lists), Ray Dutton's Garage #3 (13, all 13 of them true seeds; 0 in NexLev similar, so NexLev's video index does not seem to hold his videos yet), John The HVAC Guy (5), HVAC Exposed (3), Exposi (2 + 3 in hop 2), Hank Cole (1 + 3 in hop 2). **Vent Exposed and Gus Whitaker did not appear** anywhere in these pulls (not found). Roger the Pipe Guy (the operator's plumbing channel) appeared in 2 hop-1 lists and 1 hop-2 list with "Pour One Cup of Vinegar Down Your AC's Drain Line Today (Before It Floods Your Ceiling)" (`cFYptbCvNjI`, 36K views, 23:30).

**Readings worth a look (not measured):**
- Faceless "retired pro" style titles do get paired with these seeds: Ray Dutton's Garage (13 lists), Hank Cole ("The $5 Fix That Makes Your AC Blow 9° Colder — 40 Years In, Nobody Tells You This", `HPYZfXWGzjQ`, 156K), and a home-security collab "Seniors, Put Foil on Your Door Knob Tonight — A Retired Locksmith Explains Why" (`M2E-MjKZKHk`, 242K, 5 lists).
- Ramón Delgado (@FixTheMexicanWay, 33.4K subs, 26 videos) shows up in 5 hop-1 and 4 hop-2 lists with "This Is How We Cool Our House Without AC (The Mexican Way)" (`k1HGyewDZ_k`, 958K, 1 month old). A "(The X Way)" title format getting pushed next to HVAC how-tos.
- Heating "without the bill" is a big neighbour: diesel heaters (DIY JIM, Snowstead, DEBOSS GARAGE, Joshua De Lisle, Chuck Kososky), wood stoves (Bezdymne Piece / Smokeless Stoves, Greenhill Forge, Precision Metal) and "UNLIMITED Heat For Your Home | NO ELECTRIC NEEDED" (Zen Garden Oasis, `7LV5wY-iM34`, 12,933,357 on the checker's pull). 115 of the 899 hop-1 HVAC items are this kind.

## Non-HVAC channels YouTube pairs with these seeds most (in at least 5 hop-1 lists)

| Channel | ID / handle | Up-next hop 1 (of 27; of 22 seeds) | Hop 2 (of 10) | What it is (reading) | Example recommended video |
|---|---|---|---|---|---|
| Weirdward Bound | `UCuJxFxVuj4s_MmupOMmDqCQ` @WeirdwardBound | 26 (22) | 10 | no: electrical explainers (neutral wire, 60 Hz, solid vs stranded) | "What Does The Neutral Wire Actually Do?" (`Px_SYXzatR8`, 214K views, 25:12) |
| Home Central and 2 more | `UCCVFpW5fDEXY47ysgDVV-AQ`  | 18 (16) | 6 | no: home-design list video (collab of 3 channels) | "12 Japanese Home Features That Are Simply GENIUS" (`cED5CV5v5_k`, 276K views, 32:04) |
| Girl Truck Routine | `UCMTFcOaJlwRjVNoSoS9D2Vg` @GirlTruckRoutine | 15 (12) | 6 |  | "Back to Living in My Truck After a Long Break" (`FoWlWP3tmlw`, 177K views, 19:11) |
| DIY Hacks | `UCe_5cyghC66jIC64KnUs77w` @DIYHacks-t7n | 14 (10) | 3 | no: DIY repair hacks | "🔋Never Buy Drill Batteries Again! Use a Ballpoint Pen and Watch What Happens!😱 / DIY Hacks" (`UEwFDO9hQMM`, 712K views, 20:38) |
| Jake Broe | `UCYHosdETLPp6dpJEsgIUTmw` @JakeBroe | 12 (12) | 3 |  | "Two Russian Su-30 Jets CRASH in Kaliningrad" (`dtdGo50Ng00`, 46K views, 32:07) |
| ohdt nldyis | `UC5BvqGQpcqNUYGuCeCXf-9A` @ohdtnldyis | 11 (9) | 2 |  | "Trump’s Team Warns Canada — Carney’s Bold Response Shocks Washington!" (`uSG2k3cKLLg`, 3.2K views, 22:38) |
| Quantum Makers | `UC4Tklxku1yPcRIH0VVCKoeA` @QuantumMakers | 10 (10) | 1 |  | "Man Turns WWII-Era Stone Ruin Into Dream Home In Just One Year / Start To Finish @Luxon Bushcraft" (`YZTJN6CZfG0`, 56M views, 43:59) |
| Trending Machine | `UCCfpI5ggGDPkD0F0Qfsbdpw` @trending.machine | 8 (7) | 2 |  | "Craziest Homemade Vehicles That Broke the Internet !" (`L5OrcxFZWck`, 296K views, 25:13) |
| Prop Department | `UCU0wOR4RQA9L7ZBOeyQI20A` @propdepartment | 8 (7) | 1 |  | "I Built the WIDEST Street Legal Car" (`PvTyTUkuem8`, 22M views, 35:10) |
| Professor Gerdes Explains 🇺🇦 | `UCjf_Tw9PA9QIZ6R6aLukBaA` @Professor-Gerdes | 8 (8) | 0 |  | "Zelenskyy Calls Out Trump: “He Couldn't Make a Deal WITH PUTIN”" (`7dR-2ejTpMQ`, 83K views, 16:19) |
| Veritasium | `UCHnyfMqiRRG1u-2MsSQLbXA` @veritasium | 7 (7) | 2 |  | "The Closest Thing We Have to Alien Technology" (`MiUHjLxm3V0`, 64M views, 55:00) |
| The Daily Show | `UCwWhs_6x42TyRM4Wstoq8HA` @TheDailyShow | 7 (7) | 1 |  | "Trump Is Hot for Tim Scott & Susan Collins Side-Eyes Troy Jackson's Second Cousin / The Daily Show" (`LTc4kp_liiI`, 141K views, 12:15) |
| Oneindia News | `UCqTa3sNT6SfiQ2DQK_kuWlA` @oneindia | 7 (7) | 1 |  | "‘WHO DO WE WANT TO WIN?’: Kennedy’s Que Goes Viral Amid Trump’s Changing Russia Stance" (`i148xZKMqgk`, 666K views, 6:26) |
| The Young Turks | `UC1yBKRuGpC1tSM73A0ZjYjQ` @TheYoungTurks | 7 (7) | 0 |  | "BREAKING: Kushner RAGES At SHOCKING New Allegations Of Corruption" (`BVqlijcyfm4`, 29K views, 16:30) |
| Survival Gear | `UCm4NMZNhZwi8tc3886te4pA` @survivalgearofficial | 6 (5) | 2 |  | "World's Most Insane Camping Inventions That Will Save You TONS of Money!" (`1vJfy-SkxU0`, 6K views, 14:14) |
| TechFreeze | `UCUi4aspUAMcEG5ZEdnOrBQg` @TechFreezeOfficial | 6 (5) | 1 |  | "Man Uses FREE ABANDONED PALLETS to Build a House in the Forest / Full Build by @lesnoy" (`vvGEQnkdLTE`, 2.2M views, 39:31) |
| David Pakman | `UCvixJtaXuNdMPUGdOPcY8Ag` @thedavidpakmanshow | 6 (5) | 0 |  | "Trump SMASHES random woman for no reason" (`VIeq4OOHStI`, 351K views, 8:35) |
| REC Anything | `UCZpk9Hr33dOAw3HIbqPyWPQ` @recanything | 5 (5) | 2 |  | "All New 2028 Tesla Roadster can Fly - World Premiere and First Look" (`d2jH2x1HWxE`, 3.9M views, 22:12) |
| Techfusion | `UCtFYYDi8gkaRSf2UVVveIDA` @Techfusion98 | 5 (4) | 0 |  | "45 Coolest New Amazon Gadgets Almost Nobody Has Seen Yet (#13 Most Hyped)" (`ZYXPZs9j__o`, 14K views, 19:49) |
| The Economist | `UC0p5jTq6Xx_DosDFxVXnWaQ` @TheEconomist | 5 (4) | 0 |  | "AfD co-leader Alice Weidel on Ukraine, migration and Germany’s future / The Economist" (`_cGGDu8sgXY`, 637K views, 59:33) |


Weirdward Bound (62.5K subs, 160 videos; About panel, this pull) is the single most-paired channel of all: in 26 of the 27 hop-1 lists and all 10 hop-2 lists, with long electrical explainers ("What Does The Neutral Wire Actually Do?", `Px_SYXzatR8`, 214K, 25:12, 8 days old). Reading: a strong lead for the electrical study, and a sign that HVAC viewers are shown "how your house works" explainers.

## Most-recommended videos (HVAC / energy / insulation, other channels, 5 minutes or longer where the length is shown)

Sorted by hop 1 + hop 2 lists, then NexLev similar. 691 videos qualify; top 40 shown. Heating-adjacent videos (stoves, diesel heaters) are included because they are home heating.

| # | Video ID | Title | Channel | Views (up-next text) | Length | Up-next hop 1 (of 27) / hop 2 (of 10) | NexLev similar (of 22) |
|---|---|---|---|---|---|---|---|
| 1 | `_ZgVjFpBnQA` | "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" | Ray Dutton's Garage | 763K | 15:10 | 10 / 6 | 0 |
| 2 | `U6QPw6H_yMc` | "A stove that saves 50% of firewood and heats the house for 50 hours without a fire" | Bezdymne Piece | 3.4M | 1:08:31 | 8 / 3 | 0 |
| 3 | `s6gYsaYvdjg` | "Can a DIRT CHEAP Diesel Heater Actually Keep My Homestead Warm?" | Snowstead | 1.3M | 17:32 | 9 / 1 | 0 |
| 4 | `-i28W_xx2mw` | "Wood Stove Water Heater Experiment - Surprising Results! Part 1" | Greenhill Forge | 1.6M | 19:53 | 8 / 2 | 0 |
| 5 | `D_2T5H7CFmA` | "Top 5 Mini Split Installation Mistakes - Don't Do This!" | Taddy Digest | 132K | 17:12 | 6 / 3 | 0 |
| 6 | `AQ4EYHNCDzg` | "How To Install A Mini Split Air Conditioner – Complete Step-By-Step Guide" | Fer's Reviews | 663K | 24:22 | 5 / 3 | 3 |
| 7 | `k1HGyewDZ_k` | "This Is How We Cool Our House Without AC (The Mexican Way)" | Ramón Delgado | 958K | 23:12 | 5 / 3 | 0 |
| 8 | `-VPZuCK0Ag0` | "The Mini Split - REINVENTED." | The DIY HVAC Guy | 1M | 31:23 | 4 / 4 | 0 |
| 9 | `GfMNLWzaUHU` | "Turning a Dumpster AC Into a Super-Efficient Geothermal Heat Pump" | Craftsman Chris | 765K | 31:16 | 5 / 3 | 0 |
| 10 | `5dCCntGj1wM` | "DIY Mini Split Install: 3 Regrets After 1 Year of Use" | LRN2DIY | 2.3M | 8:11 | 5 / 2 | 4 |
| 11 | `2mKwCmaR5Qg` | "DIY Mini Split Install - All the Things Nobody Shows You" | LRN2DIY | 3.2M | 33:23 | 4 / 3 | 3 |
| 12 | `FditJqUenAk` | "This MINI-Split AC System Changed My Life / Learn How To Install One Yourself" | Red Beard Engineered | 1M | 14:46 | 3 / 4 | 3 |
| 13 | `VxWH4J1jM8I` | "Pro Level Mr Cool DIY Install in less than 1 day!" | RR Buildings | 779K | 52:09 | 3 / 4 | 3 |
| 14 | `dOZ-8__G4uU` | "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" | Ray Dutton's Garage | 1.2M | 11:49 | 5 / 2 | 0 |
| 15 | `yIOmar-8Rl0` | "Ranking the Best and Worst Mini Split Brands" | Yarbrough & Sons Heating, Cooling & Plumbing | 258K | 12:49 | 4 / 3 | 0 |
| 16 | `XfzCeXlDq0A` | "Make a $100 Amazon Diesel Heater Even Better With This Simple Trick" | DEBOSS GARAGE | 1.8M | 26:11 | 6 / 1 | 0 |
| 17 | `FsmLvHuA96M` | "No Central Heating? Here's What Japanese Homes Do Instead" | Japan with Nao | 1.8M | 14:32 | 6 / 1 | 0 |
| 18 | `bPj-y5o0Y7s` | "Heating My 2000 Sq Ft House With a Chinese Diesel Heater (Round 2 – Even Colder!)" | DIY JIM | 186K | 42:01 | 6 / 1 | 0 |
| 19 | `7LV5wY-iM34` | "UNLIMITED Heat For Your Home \| NO ELECTRIC NEEDED" | Zen Garden Oasis | 12,933,357 (checker; up-next showed "12M") | 26:04 | 5 / 2 | 0 |
| 20 | `k7PSzi7NSyc` | "How To Clean Your AC and Coils Like the Pros Do \| WILL Make Air Blow Colder" | How To Home | 5.6M | 11:01 | 6 / 0 | 4 |
| 21 | `ozaw9QhxkQU` | "How to Install a Ductless Mini-Split Air Conditioner / This Old House" | This Old House | 5.2M | 7:09 | 3 / 3 | 3 |
| 22 | `qwDq0JCo2eM` | "Complete DIY Mini Split Installation / New Mr Cool 4th Gen Unit" | Everyday Home Repairs | 1.1M | 18:43 | 3 / 3 | 2 |
| 23 | `3DHyShrGUXw` | "Are Mini Split Air Conditioners Worth It? - Top 5 Pros & Cons" | Benjamin Sahlstrom | 2M | 15:33 | 4 / 2 | 1 |
| 24 | `uv75G4ed2dw` | "How to Install a $360 Mini Split Heat Pump — Complete DIY Guide" | There's A Trick For That | 555K | 18:12 | 2 / 4 | 1 |
| 25 | `8olWmuMMt8k` | "HOW TO INSTALL A DIY MINI SPLIT (no HVAC tools required)" | M.T. HOMES | 136K | 31:26 | 2 / 4 | 0 |
| 26 | `0qObernb9_Q` | "Every Mini Split Part Explained — And How to Test Each One" | Taddy Digest | 45K | 26:41 | 4 / 2 | 0 |
| 27 | `hCVDgGLItwg` | "I Tried Heating My Entire House With a Chinese Diesel Heater… Shocked at the Results" | DIY JIM | 327K | 21:49 | 6 / 0 | 0 |
| 28 | `jCEc4gtd56w` | "The New Way to Install Mini Splits in 2026 (Step-by-Step)" | The Handyman | 105K | 20:07 | 4 / 2 | 0 |
| 29 | `KyiUpFjwtlU` | "Free heating fuel but it's illegal - £120 8kw Diesel parking heater review from VEVOR" | Joshua De Lisle  | 4.9M | 24:38 | 6 / 0 | 0 |
| 30 | `_-mBeYC2KGc` | "Portable Air Conditioners - Why you shouldn't like them" | Technology Connections | 10M | 16:39 | 4 / 1 | 4 |
| 31 | `nsFLpln9ezQ` | "This Is Officially The EASIEST Mini Split To Install." | The DIY HVAC Guy | 317K | 19:49 | 3 / 2 | 3 |
| 32 | `7lrgnM90pQY` | "DIY Multi-Zone Ductless Mini Split AC & Heating System / MR Cool Install 2021" | Modern Builds | 1M | 14:37 | 3 / 2 | 3 |
| 33 | `DzVJiSQNbew` | "How to Install a Ductless Mini-Split Air Conditioner - Blueridge" | alpinehomeair | 13M | 9:16 | 2 / 3 | 3 |
| 34 | `JQkth-AM5CE` | "Full Installation of Mini Split Ductless Unit, Step by Step!" | AC Service Tech LLC | 2.5M | 1:28:33 | 2 / 3 | 2 |
| 35 | `AMa6YRUwL2I` | "Watch This Before You Buy a Mr Cool Mini Split" | LRN2DIY | 623K | 35:24 | 3 / 2 | 1 |
| 36 | `2RDfAkmDId0` | "AIR CONDITIONER DETAIL INSTALL /SPLIT DUCTLESS AC HEATING INVERTER,MINI PUMP SYSTEM SETUP,DIY HOW TO" | CarlTheLandscapeGuy | 7.8M | 27:53 | 3 / 2 | 1 |
| 37 | `Bbkg2y6gaQY` | "DIY Mini‑Split Install: TOSOT vs Mr Cool vs Della" | HomePro Hero | 326K | 19:19 | 2 / 3 | 1 |
| 38 | `9U_a_6pBnkA` | "ULTIMATE Mini Split Install Guide to Save You THOUSANDS" | LRN2DIY | 79K | 50:19 | 1 / 4 | 1 |
| 39 | `BSTkKiJPeaQ` | "Coldest and Quietest Air Conditioner Ever Tested!" | Project Farm | 1M | 20:18 | 5 / 0 | 0 |
| 40 | `v586WsJn-dk` | "Multi-zone split type Air Conditioner installation" | craftsman tv | 1.3M | 16:49 | 2 / 3 | 0 |


Silver Cymbal's own HVAC videos in the lists (hop 1 / hop 2): "The BEST Portable Air Conditioner Just Got BETTER for 2026" (`OGVXmIZtEG8`) 3/1; "#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" (`_b6p0fkWhCY`) 3/0; "Oil Heat 🔥 Boilers - How it works - Understand the Basics" (`5GbXgEYw5TE`) 2/0; "Central Air Conditioner Condenser Cleaning" (`nsRHhU6q5RY`) 2/0; "Why Heating Oil is BETTER than GAS" (`GdTOl1WcHV0`) 2/0; "How to Clean Your Mini Split AC Condenser" (`DSNUyxZtrmo`) 1/1; six more at 1/0.

## What else YouTube pairs with the seeds

Every up-next item, tagged by a keyword reading of its title (first match wins; HVAC first). Counts are items (one video can be counted in several lists) and different videos.

| Topic (reading) | Hop 1 items (of 1,618) | Hop 1 different videos | Hop 1 share | Hop 2 items (of 599) | Hop 2 share | Top examples (title, channel, views, ID, lists) |
|---|---|---|---|---|---|---|
| HVAC / energy / insulation | 899 | 615 | 55.6% | 396 | 66.1% | "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" (Ray Dutton's Garage, 763K, `_ZgVjFpBnQA`, 16 lists) |
| of which stoves / diesel heaters / "free heat" | 115 | | 7.1% | 16 | 2.7% | "A stove that saves 50% of firewood and heats the house for 50 hours without a fire" (Bezdymne Piece, 3.4M, `U6QPw6H_yMc`, 11) |
| other / unclassified | 146 | 120 | 9.0% | 64 | 10.7% | "Schools In China Are Crazy" (Daily Dose Of Internet, 388K, `bWkE5joFMzY`, 5); "Seniors, Put Foil on Your Door Knob Tonight — A Retired Locksmith Explains Why" (`M2E-MjKZKHk`, 242K, 5) |
| news / politics | 103 | 39 | 6.4% | 13 | 2.2% | "Two Russian Su-30 Jets CRASH in Kaliningrad" (Jake Broe, 46K, `dtdGo50Ng00`, 15) |
| generators / power stations / solar | 98 | 83 | 6.1% | 16 | 2.7% | "Most Powerful DIY Mobile Power Station 6.2Kw" (Keeping It Simply Solar, 8.2K, `Oh9LHWIShJs`, 5); "BRUTALLY Honest Comparison: EcoFlow Wave 3 vs. Zero Breeze Mark 3..." (Adventure Gear TV, 243K, `FohXlzXCO8Y`, 4; a portable-AC comparison the keyword test put here) |
| cars / trucks / vehicles | 83 | 36 | 5.1% | 33 | 5.5% | "Back to Living in My Truck After a Long Break" (Girl Truck Routine, 177K, `FoWlWP3tmlw`, 21); "I Built the WIDEST Street Legal Car" (Prop Department, 22M, `PvTyTUkuem8`, 9) |
| electrical | 74 | 18 | 4.6% | 24 | 4.0% | "What Does The Neutral Wire Actually Do?" and "Why Does America Use 60 Hz While Europe Uses 50 Hz?" (Weirdward Bound, 31 lists each) |
| tools / DIY hacks / repair tricks | 67 | 36 | 4.1% | 17 | 2.8% | "🔋Never Buy Drill Batteries Again! Use a Ballpoint Pen..." (DIY Hacks, 712K, `UEwFDO9hQMM`, 13) |
| tech / gadgets / science | 37 | 15 | 2.3% | 13 | 2.2% | "The Closest Thing We Have to Alien Technology" (Veritasium, 64M, `MiUHjLxm3V0`, 9) |
| plumbing / water heater | 37 | 32 | 2.3% | 9 | 1.5% | "Why Don't Homeowners Use This $40 Copper Coil That Gives Endless Hot Water Without Electricity?" (Jhon Construction, 160K, `ZjXg6oi7bEo`, 3); "Don't Flush Your Water Heater Until You Watch This" (Roman Monzon, 273K, `DghkuWT-SCc`, 3) |
| house building / renovation / cabins | 31 | 4 | 1.9% | 6 | 1.0% | "12 Japanese Home Features That Are Simply GENIUS" (Home Central + 2, 276K, `cED5CV5v5_k`, 24) |
| lawn / garden / outdoor | 14 | 5 | 0.9% | 2 | 0.3% | "Mosquito Spraying is Expensive. Do This Instead!" (Silver Cymbal, 1M, `KLtlE41cTOI`, 5) |
| money / deals / scams | 13 | 6 | 0.8% | 5 | 0.8% | "10 NEW Costco Deals You NEED To Buy RIGHT NOW! (October 2026)" (The Deal Guy, 898K, `wvZ8ww5u8f0`, 3) |
| non-English | 12 | 12 | 0.7% | 0 | 0% | French, Farsi, Hungarian, Russian, Serbian news and talk |
| military / history | 4 | 2 | 0.2% | 1 | 0.2% | "What It Was Like to Fight Inside a B-17 Tail Gunner Position at 25,000 Feet" (Inside the Steel, 1.1M, `4cwBrK2zq50`, 3) |

**Per seed (hop 1), HVAC items out of 60:** the HVAC seeds get 28 to 57 HVAC items (most: "How to Install a Mr Cool 18,000 BTU AC in Just 1 Day!" 57; "Oil Heat Boilers" 50; "Top 10 Heating Problems" 49). Exception: "First Look at the NEW ECOFLOW Glacier Classic & Wave 3 Portable AC" (`S8XO4wFhrPU`) gets only 10, so YouTube files it with power stations, not HVAC. The borderline videos get few: spray foam 13, pellet stoves 36, generator hookup 3, whole-house battery 6, garage-door seal 5. Reading: YouTube treats the pellet-stove video as heating, and the generator, battery and garage-door videos as something else.

## Problems and limits

1. **Logged-out lists move.** A repeat pull 10 minutes later kept about 75% of the videos (45 to 46 of 60) but reshuffled the order; one pull per video is a sample. A trained, logged-in feed (the operator's browser) would differ again.
2. **Part of each list is generic popular content** that a logged-out viewer gets whatever they watch. News/politics, cars, tech/science and unclassified together are 369 of the 1,618 hop-1 items (22.8%); my reading is that most of these are generic. They are counted in the topic table but should not be read as audience overlap.
3. **The topic and HVAC tags are keyword readings** of titles. Known misses: EcoFlow Wave portable-AC titles without "AC" in them fall under power stations; "Japanese Home Features" falls under house building. Channel readings were corrected by hand where obviously wrong (marked).
4. **Up-next views are rounded** ("763K"); exact counts would need `/next` per video (`vid_next_batch.py`). Subscriber figures come from three sources of different dates (About panel this pull, the other helper's `about.json`, NexLev similar-channels `updatedAt`); "not found" where none had it.
5. **NexLev `get_similar_videos` is a title-similarity search**, not YouTube's recommendations; it surfaces many tiny, foreign and Shorts-length videos. Ray Dutton's Garage, Snowstead, Greenhill Forge and the diesel-heater channels never appear in it.
6. **NexLev `search_youtube_suggested_videos` could not be used** (no video input; loose keyword match).
7. **Hop 2 leans to mini-splits** (6 of the 10 hop-2 inputs), which lifts mini-split install channels' hop-2 counts.
8. Not yet re-checked by a second helper.

## Files

- `data/raw/upnext-2026-10-23.json`: `hop1` and `hop2` (every up-next item: position, page, ID, title, channel, channel ID, handle, views text, age text, length), `recheck_same_seed_repull`, `nexlev_similar_videos` (22 seeds, compact), `nexlev_similar_channels` (159), `nexlev_suggested_videos_keyword` (6 queries, raw only), `channel_about_this_pull` (43 About panels), and the method notes.
- `data/tools/upnext.py`: up-next pull (first page + continuations), paced at 1.5 s per request.
- `data/tools/upnext_build.py`: merges the pulls and prints these tables (`md` mode) and the topic counts (`top` mode).
