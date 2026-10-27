# Topic demand map — electrical

Topics never cross niches (core `filing-rule.md`). Evidence is the electrical study (`niche-research/studies/electrical/`). **Proof rule (operator, 2026-10-26):** a topic counts only with an on-topic long-form video of 300K+ views on a faceless channel (AI personas count as faceless) or 1M+ on a real channel. Unclear and brand channels get the 1M bar. Any upload date counts. **Heat** (`data/tools/clean_heat.py`; on-topic uploads in the last 12 months, pulled 2026-10-26): **Hot** = a 100K+ upload and a typical of 1,000+; **Warm** = one of the two; **Cold** = more than 5 uploads, none over 100K, typical under 1,000; **Hot, few uploads** = 5 or fewer, typically 10,000+; **Quiet** = 5 or fewer, typically under 10,000 (thin supply, untested). Proof says demand exists; heat says how much fresh supply competes for it.

## 1. Proven topics

`ideation/topic-proof.csv` joined with `ideation/topic-heat.csv` (views as recorded 2026-10-26; upload dates are in the CSV). "Proofs (faceless)": on-topic videos clearing the bar (of them, faceless). `*` = partial count (some page loads failed; counts are a floor). Typical = median. The 5 unproven topics are in §5.

| # | Topic | Proofs (faceless) | Biggest proof | Heat | 12 mo: uploads / typical |
|---|---|---|---|---|---|
| 1 | Adding an outlet to a finished wall * | 10 (1) | "How To Add An Outlet To A Finished Wall" (Everyday Home Repairs, real, 13.3M) | Warm | 12 / 3,123 |
| 2 | Wires too short in the box | 2 (0) | "How To Fix Short Wires In An Electrical Box" (Everyday Home Repairs, real, 5.4M) | Hot, few uploads | 3 / 102,113 |
| 3 | Ceiling light where there's no wiring | 3 (0) | "Recessed Lighting Install with No Attic or…" (Fix This Build That, real, 5.1M) | Hot, few uploads | 1 / 19,185 |
| 4 | Replacing a light with a ceiling fan | 14 (7) | "Havells Ceiling Fan – Customer Installatio…" (Havells India, real, 3.1M) | Hot | 60 / 1,582 |
| 5 | Replacing 2-prong outlets | 5 (1) | "How To Replace An Old 2 Prong Outlet Using…" (Everyday Home Repairs, real, 1.6M) | Cold | 13 / 363 |
| 6 | Using a multimeter at home * | 26 (14) | "How to Use a Multimeter for Beginners - Ho…" (Ratchets And Wrenches, faceless, 8.7M) | Cold | 71 / 470 |
| 7 | Connecting a generator to the house | 15 (3) | "Choosing a Backup Generator Plus 3 LEGAL H…" (Bailey Line Road, real, 3.9M) | Hot | 36 / 1,430 |
| 8 | 240V outlet for an EV charger | 6 (3) | "How To Install a 240 Volt Outlet – Electri…" (Everyday Home Repairs, real, 3.0M) | Hot | 48 / 1,362 |
| 9 | Replacing a circuit breaker * | 3 (1) | "How To Replace or Change a Circuit Breaker…" (Silver Cymbal, real, 4.0M) | Cold | 21 / 884 |
| 11 | Outlets dead, breaker not tripped * | 5 (4) | "Is your outlet not working? See how to res…" (Skobel Homes, real, 1.9M) | Warm | 14 / 3,220 |
| 12 | Plug won't stay in the outlet | 2 (1) | "Plug Won't Stay In Outlet" (Everyday Home Repairs, real, 2.5M) | Quiet | 3 / 451 |
| 13 | Breaker keeps tripping | 3 (2) | "How To Replace or Change a Circuit Breaker…" (Silver Cymbal, real, 4.0M) | Cold | 34 / 92 |
| 14 | LED bulbs glowing when switched off * | 5 (3) | "The bulb's switch is off, yet the bulb con…" (Royal Electric Gyan, real, 6.0M) | Hot | 9 / 5,920 |
| 15 | Ceiling fan slow, humming or wobbling | 10 (4) | "How to Fix Ceiling Fan Noise Without Repla…" (SE SOLUTION, real, 8.0M) | Warm | 33 / 291 |
| 16 | Light switch not working | 2 (2) | "Light Switch Light Fixture NOT Working? He…" (Sam, faceless, 672K) | Warm | 8 / 2,134 |
| 18 | Wire nut vs Wago vs push-in | 2 (0) | "What Wire Connector is the Best? Settling…" (GreatScott!, real, 2.2M) | Quiet | 4 / 6,224 |
| 19 | Volts vs amps | 9 (3) | "Is it the volts or amps that kill?" (styropyro, real, 7.3M) | Warm | 13 / 468 |
| 20 | Where ground electricity goes | 6 (3) | "Where Does Grounded Electricity Actually Go?" (Practical Engineering, real, 7.9M) | Warm | 13 / 197 |
| 21 | What the neutral wire does | 9 (7) | "Ground Neutral and Hot wires explained - e…" (The Engineering Mindset, faceless, 5.0M) | Warm | 35 / 403 |
| 22 | Breakers don't protect people from shock * | 1 (1) | "Why Circuit Breakers DON'T Protect People…" (The Engineering Mindset, faceless, 3.0M) | Cold | 8 / 283 |
| 23 | AFCI vs GFCI | 1 (0) | "AFCI vs GFCI: What's The Difference and Wh…" (Top Homeowner, real, 1.6M) | Cold | 11 / 92 |
| 24 | Why 2-prong outlets aren't allowed * | 1 (0) | "How to Ground a Two-Prong Electrical Outle…" (This Old House, real, 1.4M) | Quiet | 3 / 876 |
| 25 | Holes in plug prongs | 4 (2) | "Holey Plugs, Batman! But... what are they…" (Technology Connections, real, 6.7M) | Warm | 47 / 302 |
| 26 | Wires overheating inside the wall * | 2 (1) | "Testing The Burn Ability Of Insulation In…" (post 10, real, 3.2M) | Cold | 11 / 81 |
| 27 | Fake vs real Wago | 2 (2) | "Original Wago or Copy? Current Test Wago 222" (ElectroTest, faceless, 1.0M) | Quiet | 0 / 0 |
| 28 | How a circuit breaker works | 3 (0) | "MCBs, how do they work?" (Sabin Civil Engineering, real, 4.3M) | Cold | 16 / 107 |
| 29 | Outlet wiring mistakes | 5 (0) | "The BIGGEST Mistakes DIYers Don't Know The…" (How To Home, real, 12.9M) | Warm | 18 / 1,045 |
| 30 | Breaker panel mistakes * | 4 (1) | "10 Common Mistakes DIYers Make In Circuit…" (LRN2DIY, real, 3.8M) | Warm | 13 / 511 |
| 31 | Generator backfeed and mistakes | 4 (3) | "7 Backup Generator Mistakes. (Have You Mad…" (Backyard Maine, faceless, 2.6M) | Warm | 38 / 616 |
| 32 | Push-in (backstab) outlet wiring * | 2 (0) | "BEWARE Of These 3 Common Wiring Mistakes O…" (Silver Cymbal, real, 4.5M) | Cold | 10 / 563 |
| 33 | Electrical basics every homeowner should know | 4 (1) | "5 CLEVER Electrical Tricks Everyone Should…" (LRN2DIY, real, 3.6M) | Warm | 16 / 92 |
| 101 | Electricity history (before X existed) * | 4 (1) | "How New Electricals Made The Edwardian Hom…" (Absolute History, real, 3.4M) | Warm | 64 / 132 |
| 102 | Light bulbs to get rid of | 2 (0) | "7 BEST and 2 WORST Smart Light Bulbs on Am…" (Smart Home Solver, real, 1.3M) | Warm | 6 / 1,283 |
| 103 | Identify and label circuits in the panel | 1 (0) | "Identify Circuit Breakers when Panel is No…" (Apartment Maintenance Pro, real, 1.1M) | Cold | 13 / 341 |
| 104 | Sunken / loose outlet in the wall * | 3 (1) | "How To Fix Sunken Outlet – 2 Easy Options" (Everyday Home Repairs, real, 2.3M) | Cold | 6 / 765 |
| 105 | LED flicker and dimmer strobing * | 1 (1) | "Dimming LED lamps with ordinary dimmers." (bigclivedotcom, faceless, 306K) | Cold | 13 / 534 |
| 106 | Junction box mistakes | 4 (0) | "The BIGGEST Mistakes DIYers Don't Know They Are Making When Installing Metal Electrical Bo…" (How To Home, real, 2.4M) | Quiet | 3 / 394 |
| 108 | 3-way switches | 12 (7) | "The Best 3 Way Switch Explanation Ever!" (Terry Peterman, real, 4.4M) | Cold | 72 / 830 |
| 110 | Running power to a shed or garage | 8 (2) | "How to Run Underground Power to a Shed – A…" (This Old House, real, 3.3M) | Warm | 58 / 626 |
| 111 | Generator bonded vs floating neutral | 2 (2) | "The Generator Mistake Everyone Makes!" (Backyard Maine, faceless, 1.1M) | Warm | 24 / 1,110 |
| 112 | How electricity gets to and through your home | 8 (6) | "120V 240V Electricity explained - Split ph…" (The Engineering Mindset, faceless, 5.6M) | Warm | 66 / 124 |
| 113 | Loose neutral connection | 2 (1) | "Open Neutral" (Dave Gordon, real, 1.0M) | Cold | 20 / 50 |

**Notes on the proofs (readings):**
- 13 shares its top proof with 9; its own faceless proof is "Microwave Keeps Tripping Breaker? Here's WHY!" (Sam, 742K).
- 4 and 15 lean on Indian channels with English titles (`log.md`); for 15, the slow-fan capacitor fix. 14's top proofs (Royal Electric Gyan, Electric Guruji) look the same (reading). US fit is a reading.
- 26's top proof is a fire burn test: fire as the stakes, explained, never tested.
- 101: a closer fit than the top proof is "Physics and History of Why USA uses 120 volts and not 220 volts" (Kathy Loves Physics, real, 2.5M).
- 102: the top proof is a product ranking; the topic's source, "The Light Bulbs You Need to Get Rid of Immediately (New Research)" (Neal K. Shah, real, 1.09M, 2026-09-13), also clears the bar.
- B7 and B10 (in production) have no topic row; their Silver Cymbal references clear the bar themselves (4.47M and 2.72M, real).

## 2. Tiers (CONCLUSIONS §2)

From the topic map (`subniches.md`: 4,758 in-scope long-form videos, views of 2026-10-24) and the rising and falling table (`recent-winners.md`).

**Tier A: big topics that fewer new channels are making** (the core: their share of new uploads has fallen while older videos keep pulling views).

| Topic | Videos | Typical | Over 1M | New vs older share |
|---|---|---|---|---|
| Outlets and switches | 409 | 69K | 71 | 6.0% vs 11.6% |
| Ceiling fans | 78 | 96K | 11 | 1.2% vs 2.2% |
| Lighting and LED | 153 | 47K | 15 | 2.5% vs 4.0% |
| Wire connectors | 140 | 44K | 8 | 1.9% vs 4.1% |
| GFCI / AFCI | 195 | 9.5K | 8 | 3.3% vs 5.0% |
| Old wiring (aluminum, 2-prong, knob and tube) | 147 | 7.8K | 2 | 2.1% vs 4.2% |

**Tier B: solid topics, steady supply** (videos / typical / over 1M): testers and multimeters 151 / 29K / 21; EV chargers and 240V outlets 143 / 27K / 4; breakers and panels 394 / 10K / 24; generator safety (backfeed, transfer switches, cords) 226 / 12K / 17; wiring mistakes 219 / 7.8K / 13. Generator safety is the bridge to Jack Redfield's old audience (his "Transfer Switch vs. Interlock Kit": 5.1K, `data/jack-redfield/`).

**Tier C: high ceiling, hit or miss.** Electrical explainers: 521 / 1.5K / 33. Persona and faceless channels have won here lately: "Volts, Amps & Watts Explained — and Which One Kills You" (The Apprentice's Guide, 841K); "What Does the Neutral Wire Actually Do" (Modern-Day Edison, 520K, 925 times its channel's typical); "Solid vs. Stranded Wire" (History of Simple Things, 459K). The test topics go here, explained, never demonstrated. Explainers have the biggest rise in share of new uploads, 14.2% vs 7.7% (`recent-winners.md`), so supply is growing.

## 3. Topics already in production (the 17 initial ideas)

Titles confirmed by the operator 2026-10-26; briefs 2026-10-27 (`ideation/initial-ideas.csv`, `ideation/briefs-2026-10-27.xlsx`); no uploads recorded yet. Formats: F-numbers from core `format-bank-master.md`; P-codes from `ideation/proven-formats.csv` (P8 "The mistake everyone makes", P18 "Pull THIS out and never again") are candidates awaiting an F-number (operator call).

| Topic (#, heat) | Key: title | Format |
|---|---|---|
| Adding an outlet (1, Warm) | A1: How to Add an Outlet to a Finished Wall the Right Way (No Patching, No Mess) | F11 |
| Wires too short (2, Hot, few uploads) | A2: How To Actually Fix Short Wires In An Electrical Box (The Safe Way) · C2: The Short-Wire Mistake Everyone Makes in the Electrical Box | F17 + F6 (soft) · P8 |
| Plug won't stay in (12, Quiet) | A12: The REAL Reason Your Plug Won't Stay In The Outlet · C12: Pull THIS Out of Your Wall and Your Plugs Will Never Fall Out Again | F17 · P18 |
| Dead outlets, breaker fine (11, Warm) | C15: The Dead Outlet Mistake Everyone Makes (It's Not the Breaker) | P8 |
| Outlet wiring mistakes (29, Warm) | A29: 7 Outlet Wiring Mistakes I Find in Almost Every Older House · B6: BEWARE of These 3 Common Wiring Mistakes on Outlets & Switches | F9 · Silver Cymbal copy |
| Holes in plug prongs (25, Warm) | B3: Why Exactly Do Electric Plugs Have Holes? | Silver Cymbal copy |
| LED glow when off (14, Hot) | A14: Why Do LED Bulbs Glow After You Switch Them Off? (WARNING) | F10 + F32 |
| Panel mistakes (30, Warm) | A30: 10 Breaker Box Mistakes That Make a Panel Dangerous (Is Yours One?) | F9 |
| Generator connection (7, Hot) | A7: How to Connect a Generator to Your House the Safe, Legal Way (Interlock vs Transfer Switch) | F11 + F7b |
| Generator backfeed (31, Warm) | A31: The Generator Mistake That Can Kill the Lineman Down the Street · B11: The Worst Electrical Mistake You Can Make - Backfeeding a Generator | F9 · Silver Cymbal copy |
| Homeowner basics (33, Warm) | A33: 9 Electrical Things Every Homeowner Wishes They'd Learned Sooner | F14 |
| Connections, no topic row | B7: Never Solder Wires Again - The EASY Way to Connect Them | Silver Cymbal copy |
| Cable, no topic row | B10: The #1 DIY Electrical Mistake - Can You Run Romex in Conduit? | Silver Cymbal copy |

Overlaps: A2/C2 and A12/C12 (different thumbnails needed), A31/B11 (close).

Format lines are as recorded in `ideation/initial-ideas.csv`, set before the operator reworded five titles. A2 now reads as a how-to (F11) and A12 as "The REAL Reason" (F21's word) rather than a symptom question (reading).

## 4. Mapped, not yet produced (future batches draw here first)

Proven topics not among the 17, hottest first; within a label by 12-month typical (figures in §1). Framing notes follow the safety boundaries in `audience.md` §7 (readings).

- **Hot:** 4 replacing a light with a ceiling fan (Tier A; 14 proofs, 7 faceless) · 8 240V outlet for an EV charger (a new panel circuit: a permit and electrician topic, run as what to know).
- **Hot, few uploads:** 3 ceiling light where there's no wiring.
- **Warm:** 16 light switch not working · 102 light bulbs to get rid of · 111 generator bonded vs floating neutral · 110 power to a shed or garage (permit; NM is barred in wet conduit) · 19 volts vs amps · 21 what the neutral does · 15 ceiling fan slow, humming or wobbling (Tier A, nuisance) · 20 where ground electricity goes · 101 electricity history · 112 how electricity gets to and through the home.
- **Quiet (thin new supply, untested):** 18 wire nut vs Wago vs push-in (explain the debate) · 24 why 2-prong outlets aren't allowed (F21 territory) · 106 junction box mistakes · 27 fake vs real Wago (no on-topic upload found in 12 months; cheap-product villain; explain, never test).
- **Cold (crowded, low typical):** 9 replacing a breaker and 13 breaker keeps tripping (panel interior: explain and say when to call, never a DIY swap) · 108 3-way switches · 104 sunken outlet · 32 backstab wiring (also inside A29, B6) · 105 LED flicker · 6 multimeter (Tier B) · 5 replacing 2-prong outlets · 103 identifying circuits (no cover off) · 22 breakers don't protect people · 28 how a breaker works · 23 AFCI vs GFCI · 26 wires overheating in the wall (fire as stakes) · 113 loose neutral (service side: utility or electrician).

## 5. Not proven (and why)

| # | Topic | Why | Heat |
|---|---|---|---|
| 10 | GFCI keeps tripping | Source "Why does my GFI keep tripping?" (David Jones, typed real, 898K) is under the 1M bar; no other proof. CONCLUSIONS §3 still cites it as a "why does X keep doing Y" example. | Cold |
| 17 | Shocks from a faucet or appliance | No video clears the bar; source 218K. | Quiet |
| 34 | Yearly electrical safety checks | Only a stand-in source (LRN2DIY's "5 CLEVER Electrical Tricks…", the topic 33 proof). | Quiet |
| 107 | Upgrades for a new or remodelled home | Only "proof" was a 200-amp service upgrade, off topic. | Cold |
| 109 | Electrical tape used wrong | No video clears the bar; source 62K. | Cold |

**Out by decision, not by the proof rule** (`subniches.md`, videos / typical / over 1M):
- **Fire-first topics:** space heaters 99 / 1,040 / 4; cords and strips 343 / 1,672 / 6; fire habits 319 / 1,075 / 7; kitchen 61 / 433 / 1; extinguishers 109 / 2,215 / 2. Smoke and CO alarms (192 / 11,767 / 7), dryer vents (150 / 17,502 / 12) and lithium batteries (221 / 23,925 / 7) have real demand: out by the operator's call, not weak data.
- **Electric bill:** 140 / 671 / 4 (and money is out).
- **Home inspection walkthroughs:** 167 / 4,525 / 0. Real inspections and real stories are out as formats.
- **Holiday lights:** 33 / 4,440 / 1 ("small and seasonal").
- **Old panels as a topic:** 103 / 3,664 / 0. Federal Pacific and Zinsco are used only as villains inside other videos.
- **Scope (2026-10-24):** winter blackout survival, heat without power, power-station and generator buying reviews (Jack Redfield's old lane), seniors' home safety, "free energy" (`log.md`).

## 6. Problem selection inside a proven template

Universality (every house has outlets, switches, breakers, lights) × how annoying and how often (the plug that falls out, the dead outlet, the wobble, the glow) × the stakes (shock, fire). Not cost: money is out. Universality sets the ceiling. The template in one channel: Everyday Home Repairs, one plain how-to per problem, holds the top proof on six topics (1, 2, 8, 12, 104, 5: 13.3M down to 1.6M, `ideation/topic-proof.csv`). Silver Cymbal has 20 electrical videos over 1M, 14 under 5 minutes, so long-form versions are open (`ideation/silver-cymbal-copies.csv`).

Once a topic is proven, pick by heat:
- prefer proven topics with thin fresh supply (Hot, few uploads; Quiet), which is the Tier A logic;
- one topic can carry two formats when the thumbnails differ (A2 and C2, A12 and C12);
- start from the topic's top video and fix what it lacks: a clearer "why", the stakes, the villain in the walls (CONCLUSIONS §7).

## 7. Seasonal notes

Not measured: the study has no month-by-month data.
- **Holiday lights:** left out, small and seasonal (§5).
- **Generator and outage season:** no seasonal data. Generator connection is Hot (36 on-topic uploads in 12 months); the best recent one, "The One Install Everyone Should Consider Before It's Too Late! (Proper Generator Connection)" (How To Home, 268K), was 4 weeks old on 2026-10-26 (`ideation/topic-heat.csv`). Winter blackouts are out of scope (maybe Jack Redfield's). Generator safety as its own strand is still open (CONCLUSIONS §9).
