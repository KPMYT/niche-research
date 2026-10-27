---
name: "hvac-ideation"
description: YouTube ideation system for the operator's HVAC channel, Roger the HVAC Guy (a faceless 45-year tradesman, the same persona style as Roger the Pipe Guy) — heating, cooling, furnaces, AC, heat pumps, filters, thermostats, drafts and the heating bill for older US homeowners. Holds the channel steering, the HVAC evidence (Ray Dutton's Garage and how he built his hits, the source channels' outliers, the real-person 2M+ videos, the operator's own HVAC data points), the demand map with the season calendar, word bank, audience, dead list, the greenlit log, HVAC safety rules and the thumbnail niche pack. Use whenever the operator wants HVAC, furnace, AC, air conditioner, heat pump, mini-split, filter, thermostat, space heater, fireplace, insulation-for-heat, heating-bill or "Roger the HVAC Guy" titles, ideas, reworks, briefs or thumbnail seeds; names Ray Dutton, HVAC Exposed, John The HVAC Guy or The DIY HVAC Guy as a source; or pastes screenshots of HVAC channels — even without the word "ideation".
---

# HVAC Ideation — niche overlay

A **thin overlay** on `ideation-core`, built the same way as `plumbing-ideation`. The method, the format definitions (F-numbers), the hard rules, the brief spec and the output layout live in core; this skill holds only what is HVAC-specific. **Built 2026-10-27 from the HVAC study** (`niche-research/studies/hvac/`), before the channel has any uploads: everything here is ecosystem evidence plus the operator's plumbing data, and it will be adapted as Roger the HVAC Guy's own numbers come in (operator: "we will very much adapt as time goes on").

## 1. Read core first — structural dependency

Before doing anything, read from `ideation-core/references/`: `framework.md`, `rules-and-specs.md`, `format-bank-master.md`, and Profile A in `audience-profiles.md`. **If core is unreachable, STOP and tell the operator** — titles can't be tagged without the master bank.

Then read this skill's `references/steering.md` and, per task, the files in §5.

## 2. Channel (steering summary)

| Channel | Dials | Notes |
|---|---|---|
| **Roger the HVAC Guy** | faceless / browse / veteran-tradesman · Profile A | New channel (operator, 2026-10-23); Roger the Pipe Guy carries on. Persona: **45 years, "same as rogers pipe guy in most aspects"** (operator, 2026-10-27) — the honest insider breaking ranks, now on heating and cooling. Compiled b-roll: knowledge titles only. No own view data yet; batch 1 (16 titles) greenlit 2026-10-26 for November uploads. Full block in `references/steering.md`. |

Only one HVAC channel exists, so it is the generation default for this skill; still name it in the output.

## 3. HVAC hard rules (add to core's; never relax core's)

1. **Honest persona versions only.** Roger is the 45-year insider, so suppression, banned and lost-wisdom formats (F19, F21, F22, F29) run on real stories: the R-22 phase-out and the R-410A phase-down, builder-grade sizing by rule of thumb, sister brands built in one factory, the condensate trap nobody shows you. No invented bans, documents or dates.
2. **Distrust and self-reliance lead; damage and fear stay inside the video.** In this niche fear of damage and safety fear are weak hooks (`audience.md`); money and the cold night are the stakes, the HVAC company and the store shelf are the villains.
3. **Safety boundaries in every brief where relevant (the channel's moat):** smell gas → leave and call the gas company from outside; CO alarms on every level; never run a red-tagged furnace; refrigerant work is for licensed techs (no DIY charging); power off at the switch or disconnect, gas valve off for burner work; never bypass a limit or pressure switch; refill the condensate trap after cleaning, never pour into the pressure-switch hoses; air sealing near natural-draft appliances needs a combustion safety test; fireplace damper closed only when cold, never on gas logs; space heaters straight into the wall; a car or generator outside, 20 feet from doors, windows and vents, never in a garage, never backfeeding a panel; never mix bleach and vinegar.
4. **Briefs the script can write from** (as plumbing rule 7): for every item the title promises — what it costs if ignored, the fix, the cheap price against the tech's price as rounded ranges; a price that can't be found is left out, never guessed. Batch 1's fact-checked figures are the starting price list (`steering.md` §4).
5. **"I tested" is a persona verdict** ("A 45-Year HVAC Man Ranks All 4"), never a filmed test.
6. **Don't copy Ray Dutton's look or his exact templates.** 115 titles on 51 channels copy his templates (median 450 views); 9 channels copy his navy-shirt look and none is well above its tier. Take his method (`reference-titles.md` §2), not his words.
7. **Season first.** Heating topics October to February, cooling March to August, the shoulder titles (shut-down, start-up) at the turn.

## 4. Niche deltas to the core method

- **Intake sources, in value order:** Roger the HVAC Guy's own uploads (none yet) → the operator's plumbing channels' current winners on HVAC fixtures (the substance engine) → Ray Dutton's Garage and the faceless HVAC exposé channels (HVAC Exposed, Vent Exposed, John The HVAC Guy, HVAC Mike, Deals with Lucy, Coil Exposed) → the real-person 2M+ videos (topic pools) → audience-overlap channels (plumbing, energy, cleaning, outage prep).
- **Stake factor:** the cold house on the coldest night · the service call and the after-hours rate · the replacement quote · the heating bill. Carbon monoxide is a safety line, not a hook.
- **Problem selection:** how universal (every furnace has a filter; only condensing furnaces have a trap) × how annoying or costly × how seasonal × how big the tech's price is against the cheap fix.
- **Batch mix:** core initial-batch rule (80–85% on ecosystem winners, 15–20% new) until Roger the HVAC Guy has his own data. Batch 1 ran 4 Ray remakes, 6 plumbing formats on HVAC fixtures, 6 real-person topics, on purpose, to see which engine HVAC follows.
- **Ray's method as a standing move:** a proven outlier → a bigger list or its inverse → the season → a fast rerun of the winner (3–7 days).
- **Dedup** against `references/produced-log.md`; adjacent angles are fine.

## 5. Which reference to read for which task

| Task | Read |
|---|---|
| Any generation or rework | `steering.md`, `examples-by-format.md`, `word-bank.md`, `demand-map.md`, `produced-log.md`, `dead-list.md` |
| Audience, brief writing, persona register | `audience.md` |
| Intake / screenshot analysis, "is this new?" | `reference-titles.md` and core `framework.md` §3–§5 |
| Thumbnail seeds or prompts | `niche-packs.md` (the `thumbnails` skill loads this) |

The study behind every figure: `niche-research/studies/hvac/` (`CONCLUSIONS.md`, `ray-dutton-sources.md`, `ideation/2026-10-26-batch-1.md`, `emotions.md`, `subniches.md`, `formats.md`).

## 6. Banking

End every session where titles are greenlit with the banking ritual (core `filing-rule.md` §2): propose the diff by destination file, the operator approves line by line, then write. Produced log always; steering, word-bank, demand-map and dead-list entries only with view data or the operator's explicit `endorsed`. New formats go to the core master with the next free F-number — never to this overlay. **Pending core changes for this skill** (registry line, scoreboard column, kinship line) are proposed in `core-proposals.md` and wait for the operator's yes.
