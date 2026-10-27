---
name: "electrical-ideation"
description: YouTube ideation for the operator's home-electrical channel: Frederick Barnes, a quiet-insider AI persona and retired electrician (Jack Redfield pinned as a possible second lane), making everyday electrical fixes, "why does it keep doing that" videos and explainers for American homeowners, with fire and shock as the stakes, never the topic. Holds the steering, the proof rule (300K+ faceless / 1M+ real), proven topics with heat, proven formats, reference titles with views, audience levers and villains, the word bank, the thumbnail pack, the produced log and the dead list. Use it whenever the operator wants electrical, outlet, switch, GFCI, AFCI, breaker, panel, wiring, ceiling fan, light, LED, Wago, tester, EV charger, 240V, generator hookup, transfer switch, interlock or backfeed titles, ideas, reworks or briefs; names Frederick Barnes or Jack Redfield; mentions Silver Cymbal's electrical videos; or pastes screenshots of electrical DIY channels, even without the word "ideation".
---

# Electrical Ideation: niche overlay

A **thin overlay** on `ideation-core`. The method, the format definitions, the hard rules, the brief spec and the output formats live in core; this skill holds only what is electrical-specific: the channel, the operator's decisions, audience in this niche, vocabulary, demand map, evidence, thumbnails and the produced log. The evidence comes from the electrical study (niche-research repository, `studies/electrical/`, conclusions 2026-10-26).

## 1. Read core first: structural dependency

Before doing anything, read from `ideation-core`'s `references/`:

1. `framework.md`: the atom (proven topic × proven format × channel dials), intake, channel-normal judgment, phases, reformat mode, batch mix.
2. `rules-and-specs.md`: universal hard rules, dial-keyed rules, the brief spec, output formatting.
3. `format-bank-master.md`: the ONE F-namespace. Electrical-only formats in this overlay keep the study's P-codes as candidates until the operator assigns F-numbers.
4. `audience-profiles.md`: **Profile A** (50+ American DIY homeowner), as a hypothesis here.

**If core is unreachable, STOP and tell the operator.** Then read `references/steering.md` and, per task, the files in §5.

## 2. Channel (steering summary)

| Channel | Status | Notes |
|---|---|---|
| **Frederick Barnes** | the channel (operator, 2026-10-27: "we will do frederick for this") | AI persona, talking head (channel since 2026-09-21; 1,350 subs, one fire video carries it). Background mostly unspoken; a retired electrician, 35 years, when it has to be said. No book for now: the only CTA is a very short subscribe ask. |
| **Jack Redfield** | pinned: possible second lane | Stopped generator and solar channel (4,230 subs); a 30-year power-equipment man from rural Tennessee. Generator-safety ideas suit him. |

**Generation default: Frederick Barnes.** Jack Redfield only when the operator names him. Dials: AI persona presenter / mixed search and browse / quiet insider. Knowledge only: never a filmed test or a single-job transformation.

## 3. Electrical-specific hard rules (add to core's; never relax core's)

1. **The proof rule.** A topic or format counts only with a video of **300K+ views on a faceless channel** (AI personas count as faceless) **or 1M+ on a real (on-camera) channel**; unclear and brand channels get the 1M bar. Every idea shows its proof: title, views, channel, type, date.
2. **Fire is the stakes, never the topic.** No fire-prevention topics (`dead-list.md`). Fire and shock appear as consequences, plainly and briefly; the viewer leaves feeling able, not scared.
3. **No money framing** anywhere: titles, thumbnails, briefs. This overrides core's brief-spec money anchors.
4. **Explain, never demonstrate.** Take the best test topics and explain the result; never claim the channel tested, burned or measured anything ("I tested" fails here even as a persona verdict).
5. **Villains:** the last owner's or handyman's wiring, the cheap product, known problem panels (Federal Pacific, Zinsco) inside other topics. **Never electricians, inspectors or firefighters.**
6. **Briefs:** core brief spec (facts only, one paragraph, no structural, editing, format or script direction), 200-300 words for greenlit titles, plus safety boundaries in every how-to: power off at the breaker and verified dead with a tester; panel interiors, service work and aluminum-wiring repairs are a licensed electrician's job; permits and local code ("the inspector has the final say"); generators outdoors at least 20 feet from doors, windows and vents (CPSC); never a male-to-male cord. Code citations only when verified (NEC 2023). Every brief is re-checked by a second helper against sources before the operator sees it.
7. **Persona claims:** background mostly unspoken; no checkable claims (no counts of houses, no named employers, no licence numbers). Tenure: 35 years (operator, 2026-10-27), one fixed number, said only where it does a job.
8. **Long-form only** (8-17 minutes). No Shorts ideas.

## 4. Niche deltas to the core method

- **Intake sources, in value order:** the top videos in the chosen formats in this niche (take and improve: clearer why, the stakes, the villain in the walls) → Silver Cymbal's 1M+ electrical videos (re-made long-form, title lightly altered) → recent winners of the last 12 months (formats) → viral formats from other persona channels (Bertha's Clean Home, Ray Dutton's Garage and the like) where they fit.
- **Topic heat:** show posting date and uploads since (same channel / others, last 12 months, typical views) for every reference, so the operator can judge whether a topic is still hot (`demand-map.md`).
- **Stake factor:** fire and shock behind the wall; the dead outlet, the tripping breaker, the plug that falls out (nuisance). Pride in doing it right leads.
- **Batch mix and layout:** `steering.md` §3 (base ideation plan).
- **Dedup** against `references/produced-log.md`; near-twins on one topic are allowed with different thumbnail pictures.

## 5. Which reference to read for which task

| Task | Read |
|---|---|
| Any generation or rework | `steering.md`, `examples-by-format.md`, `demand-map.md`, `word-bank.md`, `produced-log.md`, `dead-list.md` |
| Audience questions, brief writing, villains, safety | `audience.md` |
| Intake, screenshot analysis, "is this proven?" | `reference-titles.md`, `demand-map.md`, core `framework.md` §3-§5 |
| Thumbnail ideas, instructions or prompts | `niche-packs.md` (the `thumbnails` skill loads this) |

## 6. Banking

End every session where titles are greenlit with the **banking ritual** (core `filing-rule.md` §2): propose the diff by destination file, the operator approves line by line, then write. Produced log always; steering, word-bank, demand-map and dead-list entries only with view data or the operator's explicit call. New formats go to the core master with the next free F-number, only on the operator's yes.
