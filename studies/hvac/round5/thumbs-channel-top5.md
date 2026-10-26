# Round 5: each main channel's top 5 thumbnails (deliverable 5, part)

Built 2026-10-26 by a round 5 thumbnail helper. Nothing committed or pushed. **Not yet re-checked by a second helper (working rule 3).** Web searches used: 0.

Full labels: `../thumbnails/labels-channel-top5.csv` (285 rows, one per video). Images: `../thumbnails/img/<video_id>.jpg`.

---

## Method

**Main channels (the rule).** From `channels.csv` (census, tiers A-D, built 2026-10-26), deduplicated by channel ID:

1. the 30 biggest **tier A** channels by subscribers (census Videos-tab header, rounded), **excluding brand and company channels**: `type` starting "brand" and every channel flagged `contractor` (local heating-and-air companies are companies, so they are out; my reading of "company");
2. every **tier A, B or C** channel whose `type` is "faceless persona" and that has **5,000+ subscribers** (23 channels; 4 of them already in list 1);
3. **Ray Dutton's Garage** and **Silver Cymbal** (by name; Silver Cymbal is tier B, on camera, 1,090,000 subs);
4. the **top 10 of `new-channels.md`** by its score (`data/raw/new-channels-2026-10-26.csv`, `rank` 1-10). Eli Yoder Secrets (#4), Ray Dutton's Garage (#5), Elias Yoder (#2) and Ramón Delgado (#7) were already in; JustintimeHVAC (#9) comes in here although it is flagged `contractor`.

Result: **57 channels** (30 + 19 new from rule 2 + Silver Cymbal + 7 new from rule 4). The 30th tier A channel by subscribers is Passive Survival (9,620).

**The 5 videos.** For each channel, the first 5 videos of **5:00 or longer** on its Videos tab **Popular** sort, from the census pull `data/raw/census-2026-10-26/<channelId>.json` (logged out, pulled 2026-10-26; all 57 were there, so no new pulls). Views are the tab's **rounded** text ("1.2M"), not exact counts. Shorts are not on the Videos tab. The Popular sort is all-time, so for channels that changed topic (Silver Cymbal, Homey Vibe, Craftsman Chris, Let Sal Explain, DIY mr.T) some of the top 5 are not HVAC; they are listed as they are.

**Multiple** = tab views / the channel's baseline in `data/raw/census-channels-2026-10-26.csv` (median tab views of its long-form uploads of the last 12 months, or of its last 30 long-form when it has fewer than 10; `baseline_rule` there). hvacrepairguy has no baseline (no long-form in its Latest list): "not found".

**Skipped videos.** 28 of the 285 were already in `thumbnails/img/` or in the top-100 / recent-winners set that the other helper labels (`labels-top-winners.csv`). I did not label them; they are still listed in the CSV, with that helper's fields copied in and marked as theirs. One (Historia Prime #1, `tSFizbjaCBo`) was not yet in their file or in `img/` when I built mine: `style_group` "not labelled yet".

**Downloads.** 257 images, `maxresdefault.jpg` where it exists (234), else `hqdefault.jpg` (23), saved as `thumbnails/img/<id>.jpg` (scripts in my scratch folder, not in the repo).

**Labelling.** I looked at every image (contact sheets of 6 at 720×405 per tile) and read the text word for word. Every label is **my reading**, not a measurement: the age ranges, "AI image" vs "realistic photo" (I mark "(reading)" where it is a close call), and the style group. Bengali text on Homey Vibe is marked, not transcribed. I re-viewed 2 of the 43 sheets (12 thumbnails) after labelling: all 12 labels held. That is not the second-helper check.

**Style groups.** `style_group` uses the other helper's group names (from `labels-top-winners.csv`, as it stood at 08:43 UTC) so the two files can be counted together. `style_detail` keeps my finer name (e.g. "AI old man + white/red text", "product + red arrow", "vs split"). The mapping is in the table at the end.

---

## Each channel's house style (one line each; readings)

Views = median tab views of its top 5; multiple = median multiple. "(2 from other helper)" = that many of its top 5 carry the other helper's labels.

| # | Channel | Tier, type, subs | Why in | Top-5 median views (multiple) | House style |
|---:|---|---|---|---:|---|
| 1 | Word of Advice TV | A, on camera, 661,000 | A top 30 | 2,500,000 (192x) | black text panel on the left (white caps, one word in red, cyan or green, green tick or "#1"), real part photo on the right, red arrow; its top 2 are real face + text (2 from other helper) |
| 2 | The DIY HVAC Guy | A, on camera, 527,000 | A top 30 | 2,700,000 (65x) | real young bearded presenter in a cap, doubtful or surprised face, pointing at the unit; short white-on-black or green caps question ("DOES THIS ACTUALLY WORK?", "OFF-GRID") (2 from other helper) |
| 3 | Taddy Digest | A, on camera, 273,000 | A top 30 | 540,000 (49x) | real bearded tech talking beside the equipment, small white or yellow title-case text ("Limit Switch"); one AI-looking solar thumbnail |
| 4 | Eli Yoder Secrets | A, faceless persona, 249,000 | A top 30, persona, new #4 | 1,200,000 (264x) | busy AI scenes: an AI white-bearded Amish old man or a glowing product, dark grasping hands, yellow caps claim + red "BURIED"/"BANNED" stamps and badges ("ROCKEFELLER BURIED THIS") (1 from other helper) |
| 5 | HVAC Guide for Homeowners | A, on camera, 169,000 | A top 30 | 685,000 (298x) | real bearded contractor in a company cap, fingers up or shocked, yellow or white title text ("3 HVAC Secrets / Contractors don't want you to know!") |
| 6 | The Thought Provocateur | A, on camera, 110,000 | A top 30 | 229,000 (42x) | real bearded host cut out, shocked open mouth, pointing at a heat pump, just a year ("2026") or a short question on a blue gradient |
| 7 | Home Performance | A, on camera, 103,000 | A top 30 | 504,000 (107x) | real person working, channel logo, a long descriptive title in distressed or coloured caps |
| 8 | HVAC Talkshow and Review For Homeowners & DIY | A, on camera, 99,300 | A top 30 | 180,000 (3.4x) | two real presenters pointing at units in a grey studio, "VS" or price boxes ("$21000 / $7000 / SCAM OR REAL?") |
| 9 | DIY mr.T | A, faceless, 96,500 | A top 30 | 1,800,000 (655x) | no text at all: AI-looking close-ups of tuna-can and sand stoves with blue flames (1 from other helper) |
| 10 | Anti DIY HVAC | A, faceless, 78,400 | A top 30 | 758,000 (58x) | plain real photos of dirty condensers and coils, no text |
| 11 | David Jones | A, on camera, 74,800 | A top 30 | 897,000 (13x) | plain old low-resolution real photos of thermostat wiring and parts, no text |
| 12 | John Israel HVAC | A, faceless, 42,000 | A top 30 | 253,000 (54x) | plain real photos of coils and parts, at most a watermark |
| 13 | Talyn875 | A, on camera, 41,100 | A top 30 | 264,000 (132x) | real part photo with a yellow, red or blue outlined title ("Dual Run Capacitor Wiring") and arrow or tick icons |
| 14 | Ray Dutton's Garage | A, faceless persona, 31,900 | A top 30, persona, named, new #5 | 943,000 (63x) | **the AI "Ray": grey-haired man about 50-65 in a navy work shirt with a "RAY" name patch, pointing at the part; 2-4 word white caps warning on a red brush band ("BIG FALL MISTAKE!", "STOP DOING THIS!"); red curved arrow, sometimes a red circle** (4 from other helper) |
| 15 | HouseFresh | A, on camera, 26,900 | A top 30 | 276,000 (18x) | real reviewer's face (shocked, smug or doubtful) with the products, "BEST ..." text on blue or orange bands |
| 16 | D2D NY Real World HVAC Simplified | A, faceless, 26,100 | A top 30 | 171,000 (171x) | plain real close-ups of thermostats and controls, no text |
| 17 | Hotrods & Homestead | A, on camera, 24,900 | A top 30 | 419,000 (451x) | the Honeywell thermostat itself, white and yellow mixed-case text ("HONEYWELL ThermoSTAT Part ONE") |
| 18 | Ryan's Fireplace Diaries | A, on camera, 24,100 | A top 30 | 302,000 (11x) | real host with a big surprised grin holding the fuel, "WHAT HAPPENS WHEN YOU BURN ..." in white / yellow / red, drawn flames (1 from other helper) |
| 19 | Homey Vibe | A, faceless, 23,200 | A top 30 | 133,000 (111x) | product bottles on a sill with Bengali text in a rounded box; skin-care, not HVAC (its census tier A looks wrong: a reading) |
| 20 | The Apprentice Survival Guide | A, on camera, 22,400 | A top 30 | 61,000 (13x) | real equipment photos with 2-5 word white or black text, a few arrows |
| 21 | Construction Odyssey with Eddie | A, faceless, 22,300 | A top 30 | 272,000 (97x) | AI cut-away of soil and house with an underground pipe, 2 words "FREE AC" / "FREE COLD" with an arrow (1 from other helper) |
| 22 | HVAC Training 101 | A, faceless, 17,100 | A top 30 | 162,000 (46x) | template: orange diamond graphic, real product photo, stacked white / black / red / blue caps boxes, cartoon technician logo |
| 23 | Candlelight Archives | A, faceless persona, 16,400 | A top 30, persona | 250,000 (98x) | the same cartoon handyman (red beard, cap, suspenders), shocked and pointing, holding a price tag ("$3", "$0", "$15"), yellow price-claim text ("$14 = 40°F COOLER") |
| 24 | Jeff's HVAC Adventures | A, faceless, 16,000 | A top 30 | 115,000 (64x) | real part photo with a tilted yellow / white title with red 3D shadow ("Nozzle And Filter Change!") |
| 25 | Yung HVAC | A, on camera, 15,000 | A top 30 | 63,000 (10x) | real young tech cut out (facepalm, finger up), white caps with emojis on motion-blur colour |
| 26 | Ryan Hughes HVAC | A, on camera, 13,700 | A top 30 | 41,000 (8.5x) | real job photos with big black / red / orange outlined title text |
| 27 | Air Conditioner Lab | A, on camera, 11,000 | A top 30 | 169,000 (32x) | smiling presenter pointing at cut-out products, "BEST ..." on black and white bands, logo |
| 28 | SmitHVAC | A, on camera, 10,700 | A top 30 | 95,000 (12x) | real photo of the unit with a big white / red outlined phrase ("THIS IS BAD!", "1 YEAR REVIEW!") |
| 29 | DC HVAC | A, on camera, 10,400 | A top 30 | 35,000 (15x) | real job photos, brand and own logos, neon or block titles; one collage with the young tech's face |
| 30 | Passive Survival | A, faceless, 9,620 | A top 30 | 99,000 (450x) | vintage-paper AI illustrations with a cream-on-red banner ("NO POWER. ALL ICE."), some labelled BEFORE / AFTER (1 from other helper) |
| 31 | Elias Homestead | B, faceless persona, 26,600 | persona | 140,000 (93x) | AI Amish-look man about 40-50 (dark beard, straw hat, suspenders) holding out a cup of powder, "1 CUP" in yellow, red arrow, red badge ("WEEDS GONE") |
| 32 | Frugal Frannie | C, faceless persona, 27,500 | persona | 235,000 (38x) | AI grandmother about 75-85 (white hair, glasses, cardigan), shh gesture or smiling with the item, yellow or white caps ("WATER CO. HATE THIS") |
| 33 | Walter's Tool Talk | B, faceless persona, 8,370 | persona | 126,000 (74x) | one collectible on a cutting mat, "NEVER SELL!!!" yellow / white, yellow arrow; once the AI old man |
| 34 | Harlan Sawyer | A, faceless persona, 5,950 | persona | 113,000 (33x) | AI old logger about 65-75 (grey stubble, cap, red plaid flannel), serious, holding the wood; yellow + white caps, red band or red arrow and circle |
| 35 | Christopher Johnson | C, faceless persona, 7,100 | persona | 233,000 (16x) | AI grey-haired man about 55-65 in a quilted vest, serious, pointing; white-on-black and white-on-red boxes or yellow caps, red arrows and circles |
| 36 | Ramón Delgado | B, faceless persona, 33,600 | persona, new #7 | 147,000 (34x) | AI Hispanic man about 50-60 (grey hair, goatee) in a **navy work shirt**, "THE MEXICAN WAY" in white caps, red curved arrow at the job (1 from other helper) |
| 37 | Let Sal Explain | B, faceless persona, 17,900 | persona | 382,000 (50x) | the same cartoon bearded man in a suit and glasses, panicking or pointing between two products ("FRONT LOAD OR TOP LOAD?") |
| 38 | Sylvie Mercer | B, faceless persona, 9,950 | persona | 91,000 (34x) | AI woman about 50-60 in a headscarf and pioneer apron, talking, with the item; yellow + white caps ("I ACTUALLY TRIED IT") |
| 39 | Jhon Construction | C, faceless persona, 23,300 | persona | 325,000 (33x) | AI bald old man about 70-80 (white beard, glasses) with the item; white + yellow / green caps, yellow arrows, a red band |
| 40 | hvacrepairguy | A, faceless persona, 6,360 | persona | 431,000 (not found) | old low-resolution real video stills of a real grey-haired tech at a furnace, no text (the "faceless persona" type looks wrong here: a reading) |
| 41 | John The HVAC Guy | A, faceless persona, 7,230 | persona | 103,000 (52x) | **no person**: photo-real AI basement or equipment scene, white caps with yellow key words ("THEIR $900 SCAM / A $3 BOTTLE DOES IT"), yellow arrow (1 from other helper) |
| 42 | Earl Knows How | C, faceless persona, 43,900 | persona | 473,000 (296x) | AI old man about 60-70 (moustache, cap or a blue work shirt with an "EARL" patch) beside the fix, one word "GENIUS" or a white band, red arrow (3 from other helper) |
| 43 | Caleb Greer — Off-Grid Water & Power | C, faceless persona, 20,500 | persona | 183,000 (23x) | AI man about 35-45 (beard, red "GREER OFF-GRID" cap), pointing at the build, yellow / red / green caps |
| 44 | Backyard Low Tech | C, faceless persona, 12,300 | persona | 102,000 (32x) | AI white-haired man about 60-70 in a **navy polo**, holding or presenting the build; yellow number + white caps ("$50 NOT $450?"), yellow arrows |
| 45 | Ray Sutter | C, faceless persona, 32,000 | persona | 641,000 (46x) | AI grey man about 55-65 in plaid, serious, pointing or shh; black-on-white and white-on-red boxes ("BUY QUIETLY / BEFORE PANIC"), red arrows (1 from other helper) |
| 46 | HVAC Exposed | A, faceless persona, 9,590 | persona | 351,000 (195x) | **no person**: desaturated AI warehouse / factory / product shots, yellow + white condensed caps ("PURE GARBAGE / DON'T BUY THESE"), red X vs green tick, red arrow (1 from other helper) |
| 47 | Silas Mercer | C, faceless persona, 149,000 | persona | 733,000 (94x) | AI frontiersman about 60-70 (long grey beard, brown hat, sheepskin) pointing; "... CAN KILL YOU" white-on-red, red arrow, snowy cabin |
| 48 | Elias Yoder | B, faceless persona, 369,000 | persona, new #2 | 1,100,000 (121x) | AI Amish-look man about 40-50 (same look as Elias Homestead: reading), pointing, holding a yellow price sign ("$7"), yellow / white caps, red arrows (1 from other helper) |
| 49 | DTD History Radio | B, faceless persona, 28,700 | persona | 172,000 (486x) | AI old man about 75-85 (flat cap, wool sweater) holding the food; "STILL WORKS" yellow on black, or a long yellow / white sentence |
| 50 | WiseMoney | C, faceless persona, 22,000 | persona | 332,000 (485x) | AI young East Asian man with glasses holding two products; white headline with one green word underlined in red, red bottom line, yellow stamp ("BUY NOW!") (1 from other helper) |
| 51 | Silver Cymbal | B, on camera, 1,090,000 | named | 10,000,000 (124x) | no person: clean product close-ups (often AI or 3D-looking) with big red ticks and crosses, old vs new or before / after splits, white caps ("NEVER SOLDER AGAIN"); none of its top 5 is HVAC |
| 52 | Unknowns Lab 101 | B, faceless, 140,000 | new #1 | 2,100,000 (276x) | no text: AI-looking objects (tyre on caster wheels, wheel-rim stove, salt on charcoal), red arrow at most (2 from other helper) |
| 53 | Why Am I Green | B, faceless, 85,400 | new #3 | 801,000 (131x) | AI object close-ups (Crisco candle, pipe heater) with 2-4 word yellow / white caps ("BURNS FOR 4 MONTHS") (2 from other helper) |
| 54 | OffGrid Secrets | B, faceless, 41,600 | new #6 | 411,000 (69x) | AI aerial house shots with one black-on-yellow question ("ILLEGAL IN USA?", "BANNED?") |
| 55 | Craftsman Chris | B, on camera, 50,800 | new #8 | 513,000 (30x) | real bearded maker in a cap, shrugging, glow-outlined, white caps + one green word ("WILL IT WORK?") (1 from other helper) |
| 56 | JustintimeHVAC | A, on camera, 17,200 | new #9 | 261,000 (26x) | real tech's selfie or shocked face, customer-story caps ("84 YEAR OLD NEIGHBOR'S AC OUT!"), "$0 CHARGE" red badge, heart, own logo |
| 57 | Historia Prime | B, faceless, 103,000 | new #10 | 982,000 (89x) | dark AI scenes (rust, metals, medieval) with red / yellow / white caps claims ("RUST GONE FOREVER / $3 LIQUID"), red arrows (1 not labelled yet) |

---

## The persona channels' styles compared (23 channels; readings)

The 23 "faceless persona" channels in the main list fall into 5 looks:

| Look | Channels | What it is | Top-5 median views per channel |
|---|---|---|---|
| **The navy-shirt pro** (Ray Dutton's look) | Ray Dutton's Garage; Ramón Delgado; Earl Knows How; Backyard Low Tech (partly) | photo-real AI tradesman 50-70 in a navy or blue work shirt or polo, sometimes a name patch, pointing at the part, 1-4 word caps warning, red curved arrow | Ray 943,000; Earl 473,000; Ramón 147,000; Backyard Low Tech 102,000 |
| **The plaid old-timer with a warning** | Harlan Sawyer; Christopher Johnson; Ray Sutter; Jhon Construction | AI grey or white-haired man 55-80 in plaid or a quilted vest, serious stare, pointing; white-on-black and white-on-red boxes or yellow caps; red arrows and circles | Ray Sutter 641,000; Jhon 325,000; Christopher Johnson 233,000; Harlan 113,000 |
| **The old-ways elder** (Amish, frontier, grandmother) | Eli Yoder Secrets; Elias Yoder; Elias Homestead; Silas Mercer; Sylvie Mercer; DTD History Radio; Frugal Frannie | AI Amish man with straw hat and beard, long-bearded frontiersman, headscarf pioneer woman, flat-cap grandad or cardigan grandmother holding the cheap fix; yellow price or claim ("1 CUP", "$7"), red arrows | Eli Yoder Secrets 1,200,000; Elias Yoder 1,100,000; Silas 733,000; Frannie 235,000; DTD 172,000; Elias Homestead 140,000; Sylvie 91,000 |
| **Other AI presenters** | Caleb Greer; WiseMoney | a younger AI man (35-45 bearded builder in a branded cap; 25-35 East Asian man with glasses) holding the products, busy multi-colour caps | WiseMoney 332,000; Caleb 183,000 |
| **No person, or a cartoon** | John The HVAC Guy; HVAC Exposed; Walter's Tool Talk; Candlelight Archives; Let Sal Explain; hvacrepairguy | photo-real AI equipment scenes with yellow + white caps (John, HVAC Exposed), an object on a mat (Walter), a recurring cartoon man (Candlelight, Let Sal), or old real video stills (hvacrepairguy) | Let Sal 382,000; HVAC Exposed 351,000; Candlelight 250,000; Walter 126,000; John 103,000 |

What they share (counts from the CSV, all 115 persona-channel rows): 77 of 115 are "AI persona + bold text (+ red arrow)", 16 "AI object/build + bold text", 9 cartoon, 6 splits. Across the 81 "AI persona" thumbnails in the whole file, 44 have an arrow or circle (31 of them red) and 45 use yellow text. Median text length is 4 words in every big group.

Lookalikes I noticed, not checked (readings): Elias Yoder and Elias Homestead show what looks like the same AI Amish man; Silas Mercer and Sylvie Mercer share a surname and the About line "Drawing from my own everyday experience living entirely off the grid" (`channels.csv`); Christopher Johnson's "NO ELECTRICITY NEEDED" thumbnail and title ("20 Heating Sources That Don't Need Electricity in uk (Stockpile NOW)", `yCgv4IA6W0s`) match Ray Sutter's "20 Heating Sources That Don't Need Electricity (Stockpile NOW)" (`4QAyLUhJYng`, uploaded 2026-09-11; Christopher Johnson's first long-form is 2026-09-24, per `new-channels.md`), and its "11 POUNDLAND HEATING ITEMS THAT'LL BE WORTH GOLD IN WINTER BLACKOUT" is the "11 DOLLAR TREE HEATING ITEMS THAT'LL BE WORTH GOLD" thumbnail the other helper found on 2 prepper channels, made British.

### Ray Dutton's look, and who copies it

**Ray Dutton's top 5** (all "AI persona + bold text (+ red arrow)"; 4 labelled by the other helper, 1 by me, and I looked at all 5):

| Rank | Video | Tab views (multiple) | Text | What's shown |
|---:|---|---:|---|---|
| 1 | `dOZ-8__G4uU` "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)" | 1,200,000 (80x) | "BIG FALL MISTAKE!" | covered condenser, red arrow |
| 2 | `K2jCz3D5z_0` "The 5 Thermostat Habits That Wear Out Your AC Years Early" | 1,100,000 (73x) | "AVOID THIS!" | thermostat, red arrow and red circle |
| 3 | `fHAlfm21vYw` "Before You Turn On Your Heat This Fall, Do This (Or Pay for It All Winter)" | 943,000 (63x) | "THEY HOPE YOU MISS THIS" | open furnace burners, red arrow |
| 4 | `_ZgVjFpBnQA` "The $30 AC Filter Is Destroying Your HVAC System (Here's Why)" | 773,000 (52x) | "STOP USING THESE!" | boxed MERV 13 filter, red arrow |
| 5 | `qbWN3OViWxQ` "5 AC Mistakes HVAC Companies Hope You Keep Making" | 589,000 (39x) | "STOP DOING THIS!" | thermostat at 60° circled in red, red arrow |

The formula (my reading of these 5, matching `new-channels.md`'s reading of his 12 best): the **same photo-real AI man**, grey hair, about 50-65, **navy work shirt with a "RAY" name patch**, in a garage, at a house wall or beside the furnace, looking at the viewer and **pointing** at the part. One short **white caps warning** (2-5 words, imperative or conspiratorial: "AVOID THIS!", "THEY HOPE YOU MISS THIS"), usually on a **red brush band**. A **red curved arrow** from the text to the problem, sometimes a red circle. No numbers, no prices, no before / after.

**Who copies it, among the main channels:**

- **Ramón Delgado** (joined 2026-08-15, six weeks after Ray): the navy work shirt, the grey older man, white caps and the red curved arrow; no name patch and no red band; the words are the brand ("THE MEXICAN WAY"). `new-channels.md` also found it reusing Ray's power-meter "LOWER YOUR POWER BILL" thumbnail. Its top 5 median: 147,000 (best `k1HGyewDZ_k`, 974,000).
- **Earl Knows How** (joined 2026-06-12, before Ray): an AI old man; its #4 (`f5zNFxYRIuI`) puts him in a blue work shirt with an **"EARL" name patch**, the same device as Ray's patch (upload date of that video not checked, so who came first is not known). `new-channels.md` lists it among Ray's copiers (5 copied titles from 2026-08-13), with a furnace + red arrow + "THEY HOPE YOU MISS THIS" thumbnail. Top 5 median 473,000; its winners are the "GENIUS!" window and fan ones, not the copies.
- **Backyard Low Tech** (partly): an AI older man in a navy polo, pointing at the build, but yellow numbers and yellow arrows ("$50 NOT $450?"), so closer to the old-timer look.
- **John The HVAC Guy** copies Ray's titles (10 copies in `new-channels.md`) but not his look: no person, a photo-real AI basement scene with white + yellow caps and a yellow arrow.
- **HVAC Exposed**: Ray borrowed 2 title templates from it; its thumbnails have no person (AI warehouse, X vs tick).
- Outside this list, `new-channels.md` names at least 9 channels with the navy shirt and a name patch, several reading "RAY". Most have under 1,000 subs; their median copy has 450 views.

**Reading:** among the main channels, the navy-shirt look works for Ray himself (all 5 of his top 5) and for Earl Knows How's original ideas. Ramón Delgado's biggest hit is its own "Mexican way" topic. The older plaid or Amish personas get as many or more views with the same build (AI man + pointing + 2-5 caps words + red arrow), so **the formula is shared across the niche; what is Ray's own is the navy shirt, the name patch and the white-on-red warning.** A Roger channel using the same AI tradesman + pointing + red arrow will look like a Ray copy unless the character and colours differ.

---

## Counts per style group, with median views

**My 257 labels** (tab views, rounded; multiple = views / channel baseline):

| Style group | Thumbnails | Median views | Median multiple | Biggest |
|---|---:|---:|---:|---:|
| AI persona + bold text (+ red arrow) | 73 | 235,000 | 52.5x | 2,200,000 |
| real face + text | 47 | 293,000 | 32.2x | 2,600,000 |
| real build/product photo + text | 41 | 191,000 | 56.7x | 15,000,000 |
| AI object/build + bold text | 27 | 364,000 | 86.9x | 21,000,000 |
| real build/product photo, no text | 26 | 365,500 | 64.6x | 2,400,000 |
| cartoon / sketch / 3D animation | 11 | 250,000 | 77.7x | 616,000 |
| before/after or hot-vs-cold split | 9 | 196,000 | 110.6x | 10,000,000 |
| bold text panel + product cut-out | 8 | 312,500 | 89.3x | 2,500,000 |
| AI object/build, no headline | 6 | 2,050,000 | 484.8x | 3,500,000 |
| real person on the job, no text | 5 | 431,000 | 9.2x | 693,000 |
| AI cut-away house / buried pipe + claim text | 4 | 191,000 | 68.2x | 604,000 |
| **All** | **257** | | | |

**All 284 labelled rows** (mine plus the 27 copied from `labels-top-winners.csv`; 1 not labelled yet):

| Style group | Thumbnails | Median views | Median multiple |
|---|---:|---:|---:|
| AI persona + bold text (+ red arrow) | 81 | 315,000 | 54.8x |
| real face + text | 52 | 330,000 | 36.8x |
| real build/product photo + text | 43 | 194,000 | 61.1x |
| AI object/build + bold text | 30 | 373,000 | 88.9x |
| real build/product photo, no text | 26 | 365,500 | 64.6x |
| before/after or hot-vs-cold split | 13 | 332,000 | 195.0x |
| cartoon / sketch / 3D animation | 12 | 316,000 | 87.8x |
| bold text panel + product cut-out | 8 | 312,500 | 89.3x |
| AI cut-away house / buried pipe + claim text | 7 | 604,000 | 208.8x |
| AI object/build, no headline | 7 | 2,100,000 | 509.1x |
| real person on the job, no text | 5 | 431,000 | 9.2x |

**By channel type (all 285 rows):** on camera 105 thumbnails, median 358,000 (38.4x); faceless persona 115, median 283,000 (64.7x); faceless 65, median 411,000 (128.3x).

**My finer groups (`style_detail`, 257 rows):** product + text 42 (median 176,500); face reaction + text 40 (280,500); AI old man + yellow text 25 (163,000); plain photo no text 24 (396,500); AI old man + white/red text 17 (550,000); AI middle-aged man + text 15 (284,000); AI scene + yellow text 12 (724,500); AI scene + text 12 (114,500); AI old woman + text 10 (167,000); real person at work + text 8 (499,500); product + red arrow 7 (307,000); AI image no text 6 (2,050,000); real person at work, no text 5; cartoon man + yellow text 5; before/after split 5 (147,000); cartoon man + text 5; vs split 4; AI cutaway + text 4; AI person (other) + text 4; AI person (not old man) + text 2; product + red check/X 2 (Silver Cymbal, 18,000,000); product + arrow (not red) 1; product + icon, no text 1; AI illustration + banner text 1.

**What the counts do and don't say (reading):**

- These are each channel's 5 best, so every row is a winner for its channel; the groups compare kinds of winners, not winners with losers. Raw views mostly follow channel size: the 5 biggest rows are all Silver Cymbal (8.1-21 million, none HVAC), and "AI object/build, no headline" is 2 channels (DIY mr.T, Unknowns Lab 101) whose stove and gadget videos get millions. The multiple is the fairer column.
- On the multiple, the no-person AI groups do best (no-headline AI objects 509x, AI cut-aways 209x, splits 195x). "AI persona" (55x) is the most common style among winners but sits mid-table, and real faces are the lowest of the big groups (37x; only the 5 no-text job photos are lower, 9x).
- Inside the persona group, "AI old man + white/red text" (Ray's colours; 17 rows, median 550,000) beats "AI old man + yellow text" (25 rows, 163,000), but the white/red rows are mostly from bigger channels (Silas Mercer, Ray Sutter, Ray Dutton, Eli Yoder Secrets); small numbers, not a finding.
- The established HVAC-repair channels (Anti DIY HVAC, John Israel, D2D NY, David Jones, hvacrepairguy) reach 0.2-2.4 million with plain no-text photos uploaded years ago; the new persona channels all use AI images with text.

### How my groups map to the shared names

| My `style_detail` | `style_group` used |
|---|---|
| AI old man + yellow text; AI old man + white/red text; AI middle-aged man + text; AI old woman + text; AI person (other) + text; AI person (not old man) + text | AI persona + bold text (+ red arrow) (the last two are AI people who are not a channel persona: Taddy Digest's hard-hat man, HVAC Talkshow's sledgehammer image) |
| face reaction + text; real person at work + text with a face | real face + text |
| product + text; product + red arrow; product + arrow (not red); product + red check/X (real photo); real person at work + text with no face | real build/product photo + text |
| plain photo no text; product + icon, no text; CCTV still with only a red circle (`fKadN2AnPfM`) | real build/product photo, no text |
| AI scene + text; AI scene + yellow text; AI or 3D product + red arrow or check/X | AI object/build + bold text |
| AI image no text | AI object/build, no headline |
| AI cutaway + text | AI cut-away house / buried pipe + claim text |
| before/after split; vs split (new vs old, X vs tick, inverter vs normal) | before/after or hot-vs-cold split |
| cartoon man + text; cartoon man + yellow text; AI illustration + banner text | cartoon / sketch / 3D animation |
| Word of Advice TV text panel + photo; HVAC Training 101 graphic boxes + product | bold text panel + product cut-out |
| real person at work, no text | real person on the job, no text |

---

## Limits and open points

- Views are the tab's rounded figures, pulled 2026-10-26; the multiple uses the census baseline, also from tab views.
- All labels are readings by one helper; the second-helper check (working rule 3) has not been done.
- Rows copied from `labels-top-winners.csv` are that helper's readings as of 08:43 UTC 2026-10-26; that file was still being written. Historia Prime #1 (`tSFizbjaCBo`) still needs a label.
- Census types that look wrong from the thumbnails (readings, not changed): Homey Vibe (tier A, but Bengali skin-care videos), hvacrepairguy (typed "faceless persona", but its top 5 show a real technician in old video stills).
- Not checked: whether the lookalike channels (Elias Yoder / Elias Homestead, Silas / Sylvie Mercer, Christopher Johnson / Ray Sutter) share an owner.
