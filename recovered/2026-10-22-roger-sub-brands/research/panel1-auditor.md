# Panel 1: Monotropic Evidence Auditor

**Lens question, applied to every candidate:** how strong and how CURRENT is the evidence that this exact audience (US 55-75 older-home owners, many of them women 70+) watches this, and that a NEW faceless persona channel can win it in 2026?

**How I scored (1-10)**
- **Points for:** several independent faceless or persona channels launched in 2025-26, growing fast, with several hits per channel rather than one, on this exact topic, and with this exact audience named or shown.
- **Points off for:**
  - face channels or evidence older than about 12 months
  - one-hit channels, where a high "x" just means the channel's baseline is low
  - an exact angle that nobody measured
  - numbers that contradict each other across lanes
  - analog spin-offs that failed

I checked the lane files wherever CANDIDATES.md cites a number. Contradictions are listed in section 0. Read them first, because several scores depend on them.

---

## 0. Data-integrity problems found (verified in the lane files)

1. **Two RPM scales are mixed together.** Lane 8 used `get_batch_channel_metrics_v2`. Lanes 1, 5 and 6 used niche-finder RPM. The same channels read 1.5-2x higher on lane 8's scale:

   | Channel | Lane 8 | Other lanes |
   |---|---|---|
   | Bertha's House Hacks | **7.67** | 4.36 (L6), ~4.4 (L5) |
   | Japanese Home Hacks | **10.09** | 5.28 (L6), ~5.3 (L5) |
   | Eli Yoder Secrets | **9.62** | 6.53 (L1, L6), ~6.5 (L5); niche base 3.0 (L1) |
   | Stop Wasting Stuff | **7.06** | 3.58 (L6) |
   | Sgt Dale Whitfield | **9.14** | ~4.8 (L5) |

   **Consequence:** the RPMs quoted for AA (7.67), AB (8.75), AC (7.23) and AD (9.14), and Britain As It Was (10.91), are all on the inflated scale. To compare them with the other candidates, divide by about 1.8: AC comes to about 4.0, AD about 4.8, AB about 4.9. Roger's own 8.13 is on that same inflated scale.
2. **"Base" and "total" RPM are mixed.**
   - Ray Dutton's Garage is shown at "RPM 6.8", but that is the niche base. His blended RPM is **3.04** (Lane 1), and $7,189/mo ÷ 2.37M views/mo ≈ $3.03.
   - B's claim of "RPM 6.8-7.2, best core trade" therefore overstates real earnings by more than 2x.
3. **Readings that flatly contradict each other for one channel:**

   | Channel | Reading 1 | Reading 2 | Affects |
   |---|---|---|---|
   | Harper & Knowles | RPM 9.3 (L2) | RPM 2.38 (L6) | P quotes the 9.3 |
   | Gary Whitaker | 9.3 (L2) | 2.61 (L4) | E |
   | Wes Tucker Prepping | 9 (L2) | 5.96 (L4) | E |
   | Blackout Basics | 9 (L2) | 6.70 (L4) | E |
   | The Scam Report | 9.0 (L3) | 4.79 (L6) | Q |
   | Forgotten American Skills | RPM 7.0, 46.4K subs (L3) | 5.78, 45.7K (L4) | K |

   - E's "RPM 5.5-9.4 (highest of trades)" mixes base and total readings. On the total scale E sits at 2.6-6.7.
   - Q's "2.2-9.0" is the same problem.
4. **Forgotten Home Engineering's RPM** reads 3.0 at about $995/mo (L2, L3), and Lane 7 says NexLev has no RPM for it. A's "RPM 2-7" takes its 7 from other channels.
   - The US template channel for A earns about **$1K/mo**.
   - The US channels in that cluster sit at 1.85-3.0 (Vanished Rooms 1.85).
   - The only high earner is the German clone (RPM 5.0, a different ad market).
5. **Ages that disagree:**
   - **Sgt Dale:** joined 2026-05-19 (L8) vs first upload ~Aug 2026 (L5).
   - **Japanese Home Hacks:** created 2026-07-23 (L6) vs first upload ~Aug (L5) vs "first real upload 2026-09-24" (L8). The "~40K subs/mo" figure only holds on the last date.
   - **Bertha network:** "~680K subs in 3-4 months", but Lane 8 has Bertha's Clean Home joining **2026-03-24**, which is about 7 months.
6. **View snapshots differ across lanes** for the same video:
   - MechaniCar peroxide: 125K on 797 subs (L4) vs 274K on 1.69K subs (L6).
   - Mechanic's Code WD-40: 272K, 316K, 336K and 338K.
   - Mechanic's Code baby oil: 287K (L4) vs 475K (L6).

   Outlier ratios quoted from different snapshots can't be compared.
7. **Statistical artifacts:**
   - Outlier scores of 65.6 and 114 on **2-video** channels (American Frontier Living, Old Frontier Wisdom) mean nothing.
   - Hillbilly Way's RPM 8.75 is a projection for an unmonetized channel, so it isn't evidence.
   - Several "x" ratios mainly show a low baseline. For example, Hidden History Project's 475K at 96.5x means its average is about 4.9K views.
8. **The Otis precedent is weaker than the summary says.**
   - Of 5 Otis channels, Kitchen has 45.5K subs and Otis Granger (tools) 31.6K. Barn has 9.12K and 261K views, FarmHouse 5.32K, and **Otis Grangers Clean Home 1.89K**.
   - The tools channel's first video was 2026-08-20, so it did not launch the same day.
   - The cleaning sibling, the one closest to C and AA, is the weakest of the five.
9. **Spouse and brand spin-offs have already failed in this graph.**
   - **Martha Yoder Secrets**, the female sibling of a working male elder brand, has **104 subs**.
   - Eli Yoder The Plumber gains about 590 subs/mo.
   - The "Roger's wife" structure (S and AA) is 0 for 1 on direct analogs.
10. **Name collisions nobody flagged:**

    | Proposed | Existing channel |
    |---|---|
    | AA "June" | **June's Kitchen Table** already exists (L2: 1.37K subs, $2,006/mo, a winter-warmth channel) |
    | S "Margaret" | **Nan Margaret** is on Roger's own audience tab |
    | P "Walt" | **Walt Brandt** is a faceless appliance-clone persona. Walt/Walter is also the most overused AI persona name in this graph: Walter Tries It, Walter Bennet, Walter's Garage Finds, Walt Brennan, Walt Senior Money Watch, Walter Tillman, Walt Harmon, Walter Hayes. The operator also runs Walt Wren. |
    | AC (any "Roger RV" name) | Roger RVs and Motorhomes |

11. **No lane has a single demographic number.** "Many of them women 70+" rests on the top comments of two Roger videos. No age or gender split was pulled. Every score below that relies on "women 70+" uses inferred fit, not measured fit.

---

## 1. Scoring table

| id | name | score | reason |
|---|---|---|---|
| A | Roger's Old House | 6 | Several independent 2026 faceless channels with several hits each: Forgotten Home Engineering (FHE) 3.9-8.6x across 6 videos, House Secrets, Vanished Rooms, Forgotten American Farm. But no persona has been tested, US RPM is 1.85-3.0, the template earns about $1K/mo, and FHE grows only about 3.7K subs/mo. |
| B | Roger's Boiler Room / Furnace Room | 7 | The only trade with **direct audience-tab proof** (Ray's channel). Ray Dutton is a 2026 faceless persona with 6 videos of 397K or more, about 9K subs/mo, and 5+ other 2026 faceless HVAC entrants at 230-670K. But blended RPM is about 3.0, not 6.8. The boiler/radiator/steam angle was **never measured**. |
| C | Roger's Cupboard / Clean Guy | 5 | The topic proof is the strongest in the file. But the exact analogs, male-elder sibling channels doing cheap substances, are weak: Otis Clean Home 1.89K, Eli Yoder The Plumber about 590/mo. Copycats get 9-11 views and Earl Knows How already holds "plumbers + peroxide". The winners all have a culture hook. |
| D | Roger the Water Guy | 5 | The big numbers are face channels, mostly 1-8 years old (Project Farm, Johnny Harris, Veritasium, a softener video from 8 years ago). Only one 2026 faceless channel is on topic (Caleb Greer, 16.1K, ~$4K/mo). Hidden Homestead (971K) is on the audience tab but is pseudoscience. |
| E | Roger's Dry Taps / Storm Shelf | 6 | Many independent 2026 faceless channels (Blackout Basics, Wes Tucker Prepping, Survival Blueprint, Caleb Greer, Gary Whitaker, Harlan Pike), with hits days to weeks old and seniors named in titles. But sub growth is slow (3-10K total), the RPMs contradict each other, faceless generator titles fail (best 21.9K), Collapse Crate fails, and the plumbing-in-an-outage angle was never measured. |
| F | Buck the Bug Man / Roger the Bug Guy | 6 | Pest control is on the audience tab. Clem Reveals (Apr 2026) has 4 hits from 606K to 1.6M, plus Titus Freeman (Aug 2026), Dr Lucas Richards and "never had a bug" grannies in 3 cultures. But the two veteran-exterminator personas failed (3.3K views; 6 views), RPM is 1.8-3.7, and the winners have no persona or are grannies. |
| G | Roger's Japanese Obsession | 4 | The current, multi-channel evidence proves the **insider** seat. The proof for the outsider-plumber seat is 3-7 years old and from face channels (Wakefield 5 years, fern 3 years, Insider Tech 7 years). The one direct 2026 attempt (Humbled Craftsman) gets about 200 views. |
| H | Roger Goes Amish | 4 | The insider lens is huge and current. The outsider proof is all face vloggers or real physical tests (Red Poppy Ranch 1.2M), and a faceless channel can't fake those. The one Amish + plumbing channel that exists (Eli Yoder The Plumber) gains about 590 subs/mo. |
| I | Roger Around the World | 3 | The evidence is 5-7 years old and from face channels. Erik Johansson is a single 1.2M hit with the rest at 86-95K. Mixed-lens titles fail: Uncle Kenji 8.9K, and Steven Joshua's Scandinavian version 3.7K vs 190K for the Japanese one. |
| J | Roger's Toilet Through Time | 4 | Carried by outliers. Hidden History's 96.5x means an average of about 4.9K, and the incumbents are 6-9 years old. Direct-topic searches return tiny results: garderobes 8-3.7K, "plumbing for sleep" 2-3.8K, gong farmer 1-900. Sleep channels with high RPM earn only $0.9-1.6K/mo. |
| K | Roger's Old Ways | 6 | Forgotten American Skills (Apr 2026) has 6 hits at 3-8x and about $11.5K/mo, and Sidney gains about 26K/mo. But the clones are crowded, the closest analog (Otis's Barn) is weak at 261K views in 9 weeks, and the topics are mostly camping and farm, a poor fit for women 70+. |
| L | Roger's Old Advice | 3 | The large numbers are 2-11 years old and from face channels (17.66M, 6.82M). The AI elders spike and fade (Peter Whitmore down to about 13.6K views/mo). The proposed target is young men, which is the wrong audience. Policy risk is the highest of any candidate. |
| M | Roger the Tool Guy / Toolbox | 4 | Every 2026 hit is outlier-carried: Built to Fail's 54.8x is on an average of about 9.7K. The large numbers are 2-11 years old and from face channels. RPM is 1.6-3.6, and the fit for women 70+ is close to zero. |
| N | Roger's Yard / Mower Guy | 5 | Several 2026 faceless channels have several hits each (HardYardCo with 5 videos from 167K to 501K, Lenny Harper, Yard Secrets, Backyard Verdict), and lawn is on the audience tab. But every one is under 16K subs and earns under $1K/mo, it's off-season from now, and the fit for women 70+ is weak. |
| O | Roger's Garage | 4 | There is real 2026 demand (Japanese Car Hacks 558K, Car Secrets, Everything Trucks). But at least 6 new mechanic personas get 9-293 views, the snapshots contradict each other, and a plumber has no credibility on cars. |
| P | Walt the Appliance Man | 4 | The hits come from a face channel (Harper & Knowles), and its RPM contradicts itself (9.3 vs 2.38). The faceless hits are single outliers (Engine Hacks 65.3x). Clones get 50-1,500 views, and "Walt" is already a clone's name. |
| Q | Roger's Bill & Scam Watch | 5 | Senior scam/bill demand is current, spread over several channels, and fits women 70+ (Joseph Retires, Senior Benefit Guide, Fraud Watch HQ, Safety Senior). But Safety Senior is one title plus its re-upload. Roger's angle (contractor scams) was searched and **not found to work** (204K, news). The RPMs contradict each other. |
| R | Roger's Penny | 4 | The 2026 evidence is almost all **female** AI grannies, which supports a female voice, not Roger. The only male channel is Walt Senior Money Watch (coupons). "The male voice is open" is just as likely to mean there is no demand for it. |
| S | Margaret's Kitchen / Roger's Pantry | 7 | The best evidence of its kind in the file: **five independent 2025-26 faceless or persona channels**, several under 3 months old and earning money: Otis's Kitchen, Grandma Edith Cooks, Cooking for Seniors with Ray (3 weeks old, $3K/mo), Survival Kitchen 1930 and Cooking With Larry. Seniors are named in titles. Points off because the one direct spouse-spin-off analog failed (Martha Yoder, 104 subs) and "Margaret" collides with Nan Margaret. |
| T | Roger the Grill Guy | 4 | Carried by one strong channel (James J. Conner). The other BBQ channels earn $85-254/mo despite 300-500K hits, and the fit for women 70+ is close to nil. |
| U | Roger's Job-Site Stories | 3 | All the evidence is outlier-carried (80.7x on 3.3K subs, and so on). Plumber-story demand was searched and returned 2.2-6.2K. "Nobody serves it" here fits no demand as well as a gap. |
| V | Roger's Frontier Fixes | 4 | The headline outlier scores are 2-video artifacts. Past Trek (928K, about $3.1K/mo) is real but it is one channel, and the format is story-fiction rather than this audience's home problem. |
| W | Roger's Disaster Files | 2 | The incumbents are face or old (Practical Engineering), CONSTRUCTUM isn't about water, the US water-disaster search found one 14-year-old video and the rest under 17K, and RPM is about 2. |
| X | Roger Inspects / vs the Flippers | 3 | The proof is 1-6 years old and from face channels (Wakefield 6 years, Zac Rios, Site Inspections). The only faceless proof is one week-old video on a 1.17K-sub channel, and copyright risk applies. |
| Y | Roger the Body Plumber | 3 | The senior-health audience is real, current and female. But 15+ AI "Dr" channels get 5-900 views, the plumber angle has a single 1-view Short, the YMYL and policy risk is the highest, and the brand damage would land on the main channel. |
| Z | Roger Tries It | 2 | The direct 2026 analog (Walter Tries It) gets 90% of its views from one copied Roger title, and its real tests get 130-800 views. A faceless channel can't run tests. |
| AA | The Plumber's Wife (June) | 6 | The audience fit for women 70+ is the best in the file, and female elder household channels are the fastest growers. But they all have a **culture hook**. The hook-less analogs are modest: Mrs. Doris Cleans 4.95K at $1.6K/mo, Otis Clean Home 1.89K. Martha Yoder failed, the RPM quoted is on the inflated scale (comparable figure about 4.4), and "June's Kitchen Table" already exists. |
| AB | Roger's Holler | 5 | The lane is strong and current (Eli Yoder about 29K/mo, Sidney, Britain As It Was winter titles 11 days old). The archetype rests on **one 5-week, unmonetized channel** with two hits at 36-41K, and its RPM is a projection on the inflated scale. |
| AC | Roger on the Road | 5 | Dave Jennings has 7 outliers, not one, plus Road Life Guide and The Recreational Vehicle. But only the peroxide video is plumbing, the real RPM is about 4 rather than 7.23, RV-plumbing evidence is 6-10 years old, and the name collides with Roger RVs and Motorhomes. |
| AD | Roger's Army Buddy / The Sarge | 3 | Hit-driven (2 hits, everything else 1-3K), the lanes disagree on its join date and RPM (May vs Aug; 9.14 vs ~4.8), and it collides with the operator's Navy vet. |

---

## 2. Top 8 (in order)

1. **S: Margaret's Kitchen / Roger's Pantry (7), merged with AA (see merges).**
   - **Evidence:** the only candidate with five or more independent faceless or persona channels, all launched Nov 2025 to Oct 2026, most earning $1.7-9.8K/mo within weeks, and with "seniors" or "living alone" in the titles. Otis's Kitchen is the nearest model (an old-man persona whose kitchen sibling beat his other channels), and Cooking for Seniors with Ray earned about $3K/mo in its first 3 weeks.
   - **Caveat:** it is proven as cooking for seniors, **not** as a spouse spin-off (Martha Yoder: 104 subs). The handoff has to be built deliberately, and the persona needs a name that isn't Margaret.
2. **B: Roger's Boiler Room (7).**
   - **Evidence:** the only candidate with direct audience-tab proof that Roger's viewers watch it. The 2026 faceless persona model has worked here with several hits (Ray Dutton: 6 videos at 397K-1.1M), and 5+ other 2026 faceless HVAC entrants are reaching 230-670K.
   - **Caveats:** the real RPM is about 3.0, not 6.8. The old-house heat angle needs one measuring search before launch, because nobody ran it.
3. **AA: The Plumber's Wife (6), as the cleaning and frugal pillar of S rather than its own channel.**
   - **Evidence:** the fastest-growing persona type in Roger's graph (female elders passing down household methods), and the best inferred match for women 70+.
   - **Caveats:** every fast grower has a culture hook. Without one the evidence is modest (Mrs. Doris, Frugal Frannie, Grandma Edith), so it ranks below S.
4. **F: Buck the Bug Man (6).**
   - **Evidence:** pest control is on the audience tab. Clem Reveals (Apr 2026) has 4 hits from 606K to 1.6M, not one, and "never had a bug in 40 years" grannies hit in three cultures.
   - **Caveats:** the two veteran-exterminator personas failed, so the persona needs a household framing ("what my brother does in his own house"), not a trade-credential pitch. RPM is low.
5. **A: Roger's Old House (6).**
   - **Evidence:** several independent 2026 faceless channels with steady multi-hit performance: Forgotten Home Engineering has 6 videos at 3.9-8.6x, which is not one outlier. It is closest to Roger's book and audience (older-home owners).
   - **Caveats:** US monetization is thin (template about $1K/mo, RPM 1.85-3.0). No persona has been tested on it, so the persona edge is an assumption.
6. **E: Roger's Dry Taps (6), better delivered as B's winter arm.**
   - **Evidence:** the most independent 2026 faceless channels of any lane, with hits days to weeks old and "seniors" in the titles. It is in season now.
   - **Caveats:** sub growth is slow, the RPMs contradict each other, "generator mistakes" titles fail, and the plumbing-in-an-outage angle was never measured.
7. **K: Roger's Old Ways (6).**
   - **Evidence:** Forgotten American Skills is a genuine multi-hit 2026 faceless earner (about $11.5K/mo), and Sidney grows about 26K/mo.
   - **Caveats:** the closest analog (Otis's Barn) is weak, clones are everywhere, and camping and farm topics miss women 70+. Its household half should go into A.
8. **AC: Roger on the Road (5).**
   - **Evidence:** Dave Jennings is a 2026 retiree persona with 7 outliers rather than 1, and the peroxide lever already worked in RVs (254K).
   - **Caveats:** on comparable scales the RPM is about 4. RV-plumbing evidence specifically is 6-10 years old, and the name collides with an existing channel. Make it a test, not a launch.

---

## 3. Kill list (not to be built as separate channels)

| id | Reason |
|---|---|
| Z | The direct 2026 analog failed (130-800 views on real videos). Faceless tests can't be shown. Keep "Roger's Verdict" as a series on the main channel. |
| Y | YMYL and policy risk; 15+ AI "Dr" clones at 5-900 views; the plumber angle has one 1-view Short. It would damage the main brand. |
| L | The evidence is old and from face channels, the AI elders spike and fade, it targets young men (the wrong audience), and the policy risk is the highest. |
| I | The evidence is 5-7 years old and from face channels, and mixed-lens titles were measured to fail. |
| W | Old or face incumbents, no water-disaster demand found (best under 17K, apart from one 14-year-old video), RPM about 2. |
| X | The proof is from face channels and 1-6 years old, there is one faceless datapoint a week old, and copyright risk applies. |
| AD | Two hits, contradictory data, and a collision with the Navy vet. |
| O | At least 6 new mechanic personas sit at 9-293 views, and a plumber has no credibility on cars. |
| T | One competitor carries all the evidence, the other BBQ channels earn $85-254/mo, and the fit for women 70+ is nil. |
| P | Face-led evidence, an RPM that contradicts itself, a clone flood at 50-1,500 views, and the name is taken. |
| G | The outsider seat's proof is old and from face channels, and the one live attempt gets about 200 views. Use it for one-off titles on the main channel. |
| H | The outsider proof needs real tests, and the Amish + plumbing channel that exists stalls (about 590/mo). Use one-offs on the main channel. |
| J | Outlier-carried, and direct-topic searches are tiny. At most a series on the main channel. |
| U | No demand found for plumber stories (2.2-6.2K), and the drama evidence is outlier-only. |
| V | The headline stats are 2-video artifacts, and the format is fiction. |
| M | Every hit is outlier-carried, RPM is low, and it misses the women 70+. Run it as a series on the main channel. |
| C | The exact analogs (Otis Clean Home, Eli Yoder The Plumber) are weak, and Roger already owns this on his main channel. Move it into the main channel plus the S/AA cleaning pillar. |
| R | The evidence supports a *female* frugal voice only. Move it into S/AA. |

**On hold, not killed:** D and Q. Roger's specific angle in each one needs measuring first. Run each as a 6-8 video series on the main channel and promote it only if the series beats Roger's average of about 42.8K views per video.

---

## 4. Merges

1. **S + AA + R:** one spouse channel. Cooking for two and seniors leads, because that is where the hook-less evidence is strongest. Cheap-substance cleaning and fixed-income frugality are the second and third pillars.
   - It needs a non-colliding name (not June, not Margaret).
   - It must be handed off deliberately: a collab byline, the wife appearing on Roger's channel first, and end screens. Martha Yoder and Eli Yoder The Plumber show that the name alone moves nobody.
2. **E into B:** "Roger's Boiler Room" gets a winter-outage arm (pipes, well pump and water heater when the power's out). This follows Lane 1's own recommendation and avoids a stand-alone channel against the operator's Fireman channel.
3. **K's household half into A:** old-house "what the old builders and old-timers knew". Drop K's camping and farm half, which is off-audience.
4. **C, Z, M, J and the G/H one-offs:** recurring series on Roger's main channel, not channels.
5. **D's emergency-water storage into B/E;** the rest of D stays as a series on the main channel until it is measured.

---

## 5. One idea nobody listed (grounded in the lane data)

**A winter-warmth channel for seniors living alone in an older house.** Working name: "Roger's Warm House"; it cannot be "June's…", which is taken.

No candidate is defined this way. E is grid-down, AB is Appalachian and B is HVAC. But my lens finds the densest cluster of **current, independent, faceless 2026 hits that name the audience outright**:

| Channel | Video | Views | Age / note |
|---|---|---|---|
| June's Kitchen Table | "9 Ways I Keep One Room Warm With No Power" | 151K | 88.9x |
| June's Kitchen Table | "9 Ways I Keep My Bed Warm With No Heat" | 318K | 1.37K subs, ~$2.0K/mo |
| Britain As It Was | "20 Winter Clothing Tricks…" | 158K | 11 days |
| Britain As It Was | "Sleep Warm in a Freezing Bedroom" | 80K | 9 days |
| Jhon Construction | "Why Don't **Seniors** Try This $10 Bucket of Salt…" | 570K | |
| Harlan Pike Prepping | "12 Walmart Items **Seniors** Should Buy Before the First Winter Blackout" | 100K | on 1.19K subs |
| Blackout Basics | "12 Dollar Tree Items That Keep You WARM…" | 241K | |
| Lost Survival Knowledge | "…When Your Furnace Stops Working" | 363K | 47.2x |
| Wes Tucker Prepping | DIY stove | 297K | |
| Eli Yoder | $50 heater | 813K | |
| Hillbilly Way | | 41K | 10.6x |

**Why it fits:**
- That is 10 independent channels, most launched in 2026, with hits from days to weeks old.
- The titles skew to a first-person woman living alone ("my bed", "one room"). That matches the women-70+ commenters better than any male-trade candidate does.
- The plumbing tie is native: frozen pipes, water-heater heat, the heat bill, drafts in an old house.

**Risks:**
- It is seasonal (Oct-Mar).
- It overlaps the operator's Fireman channel (outages) and the "living alone" framing in home-security.

**The cleanest option:** run it as the **launch season of the S/AA spouse channel** (Oct-Mar), not as an eighth channel.

**A measurement step that should come before any launch:** pull Roger's real age and gender split (NexLev `get_my_audience_demographics` on the connected channel). Every "women 70+" claim in this whole exercise rests on the top comments of two videos. If the real split is mostly men 55-65, then S/AA and the winter-warmth idea fall and B, A and F rise.
