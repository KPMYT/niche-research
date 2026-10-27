# Proposal: register `electrical-ideation` in `ideation-core` (not applied)

`ideation-core` lives in `KPMYT/script-system/ideation/ideation-core/` and is installed as its own skill. Registering a niche (core `launch-playbook.md` §2 step 6) adds three things there. Nothing is applied until the operator says yes; then the core skill is rebuilt and re-uploaded.

## 1. `references/registry.md`: a new section

```
## electrical-ideation
- **Path:** `/mnt/skills/plugins/electrical-ideation`
- **Profile:** A (50+ American DIY homeowner), a hypothesis: no audience tab read yet.
- **Channels:**
  - **Frederick Barnes** — AI persona presenter (talking head) / mixed search and browse / quiet-insider tradesman; a retired electrician, 35 years, background mostly unspoken. Footage: AI presenter + compiled b-roll and diagrams — knowledge only. Chosen for the electrical lane 2026-10-27; channel since 2026-09-21 (1,350 subs).
  - **Jack Redfield** — pinned as a possible second lane (stopped generator and solar channel, 4,230 subs); generator-safety ideas suit him.
- **Generation default when no channel is named:** Frederick Barnes (the only active electrical channel).
- **Batches:** 2026-10-26 initial ideas: 17 greenlit (titles, thumbnail instructions, briefs in niche-research `studies/electrical/ideation/`).
- **Niche rules:** proof rule (300K+ faceless / 1M+ real); fire is the stakes, never the topic; no money framing; explain, never demonstrate; villains never electricians, inspectors or firefighters; long-form only.
- **Dead (operator 2026-10-26):** fire-first topics, NEVER lists, real inspections, real stories, the fire investigator.
```

## 2. `references/scoreboard.md`: an Electrical column

Every F-row gets an Electrical cell copied from `electrical-ideation/references/examples-by-format.md` §1 (proven / candidate / excluded, with the evidence title and views). The electrical-only P-codes stay out of the master until the operator assigns F-numbers.

## 3. `references/kinship-map.md`: one line

```
- **Quiet-insider tradesman (face — added 2026-10-27, electrical launch):** **Frederick Barnes** (electrical, retired electrician, 35 years, AI presenter) = the veteran-tradesman honest insider (Roger, Norbert Daniels) without the trade-as-adversary edge or money anchors: electricians, inspectors and firefighters are trusted insiders, never villains; pride in doing it right leads and fire and shock are the stakes. Face doctrine from Werner and Hank (synthetic presenter, disclosure, persona verdicts, no on-camera demonstration). Nearest sibling for any future safety-trade persona (HVAC tech, gas fitter).
```

Note: `steering.md` and `SKILL.md` in the overlay still say the channel is pinned; once the operator confirms Frederick as the channel (2026-10-27, for the scripts), those lines are updated in the same change.
