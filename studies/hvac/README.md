# HVAC study: Roger the HVAC Guy

The research for the new channel Roger the HVAC Guy, following `RESEARCH-BRIEF.md`. Owned by the HVAC research chat.

**Status (2026-10-23):** round 1 (seeds) done and checked; round 2 (spread) done and checked 2026-10-24; reported to the operator; round 3 waiting for the go.

## Scope decisions (operator, 2026-10-23)

- Generator videos count only when they are about keeping the house warm in an outage; generator and power-station product reviews are out.
- Drafts, weatherstripping, spray foam, windows and attic insulation count when the title is about heating, cooling or the bill.
- Round 1 also starts finding channels ("go and find more channels too").

## Operator decisions, 2026-10-24 (on the round 1 report)

- New emotions E19 comfort and E20 new-gadget wonder: yes. New formats (symptom-fix, install/DIY project, review, explainer, news-warning): yes. See `labels.md`.
- **NexLev RPM is not used:** "ignore nexlev rpm its wrong". RPM and NexLev's RPM-based figures are not used for any finding or comparison in this study. (NexLev monthly earnings are RPM-based too, so they are kept in the raw data but marked as NexLev estimates and not relied on.)
- Off-grid heat (wood and pellet stoves, diesel heaters, "free heat" tricks) is mapped as its own sub-niche (my reading of the answer to question 4).
- Silver Cymbal borderline videos: the pellet stove video (`9d9TL02idO4`) counts as a seed; spray foam, garage-door seal, crawlspace and snowstorm videos stay out.
- Search sorts: "this month" and "this year" filters replace the broken "upload date" sort; old videos come from each channel's Oldest tab, as YouTube search has no "oldest" sort.

## Files

| Path | What it is |
|---|---|
| `README.md` | This file: what's here, the status, the dates pulled. |
| `log.md` | Every round: what ran, how many helpers, what changed. |
| `labels.md` | Label definitions (emotions, villains, formats, sub-niches, types, the multiple), including proposed new ones marked NEW. |
| `seeds/` | Round 1: `silver-cymbal.md` (22 HVAC seed videos, labelled; borderline and adjacent tables), `known-channels-recheck.md` (the 8 known channels re-checked), `leads-channels.md` (up-next and similar-video leads), `channel-finds-round1.md` (174 channels found), `keywords-round2.md` (round 2 keyword list), `check-round1.md` (the round 1 check), `round1-report.md` (what was reported to the operator). |
| `data/raw/` | Raw pulls (JSON, CSV), one file per pull, named with the date. |
| `data/tools/` | The small scripts used. Copied from `recovered/2026-10-22-roger-sub-brands/tools/` on 2026-10-23, then adapted where noted. |
| `round2/` | Round 2 working files: `keyword-sweep.md`, `formats.md`, `nexlev-channels.md`, `old-house-heat.md`, `channels-master.md` (the master channel list), the checks `check-round2.md` and `check-master.md`, and `round2-report.md` (what was reported to the operator). |
| `thumbnails/` | Deliverable 5 (later rounds). |
