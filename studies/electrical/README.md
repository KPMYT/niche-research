# Electrical and fire prevention study

For Frederick Barnes's new brand (electrical DIY, electrical safety, avoiding electrical mistakes, fire prevention). Follows `../../RESEARCH-BRIEF.md`. Owned by the "Electrical and fire prevention research chat".

**Status (2026-10-26):** rounds 1-6 done and checked. **Start with `REPORT-2026-10-26.md`** (the findings in plain words and the questions for the operator); next the back and forth, then `CONCLUSIONS.md`.

**Scope (operator, 2026-10-24):** narrow: core electrical and fire prevention. Out: winter blackouts, heat without power, generator and power-station buying (a possible later channel, Jack Redfield), seniors' home security, prepping, free energy. Long-form only (5:00+), English; under-5:00 hits are listed in `short-reference.md` but never counted.

## Deliverables (`RESEARCH-BRIEF.md` section 2)

| File | Deliverable |
|---|---|
| `channels.md`, `channels.csv` | 1. The channel census (298 channels: core, partial, out), plus the presenter-background table. |
| `new-channels.md` | 2. New channels taking off. |
| `subniches.md` | 3. The sub-niche map. |
| `emotions.md` | 4. Emotions in each sub-niche (with how far to trust each emotion). |
| `ideation/` | Ideation built on the conclusions: round 1 (34 ideas, CSV and page). Its own `README.md` maps the files. |
| `CONCLUSIONS.md` | 9. The conclusions and strategy, after the operator's walkthrough (2026-10-26): topics in three tiers, formats, emotions and villains, titles and thumbnails, gaps, how to stand apart, what the scripting pack should take. Channel-neutral (channel pinned). |
| `thumbnails/thumbnail-text.html` | The words on the 82 recent winners' thumbnails by text type, plus the operator's two looks (character + explainer board; a person reacting or pointing) and close-ups with no character (2026-10-26; published privately: https://claude.ai/artifact/DU5qu4MruAiEVR5B2eY4Rg). Built by `data/tools/build_text_page.py` from `data/thumb-text/recent-thumb-text.csv` (text types and lane are readings; `blind-check.csv` is the second helper's blind sort, 65 of 73 agree). |
| `thumbnails/thumbnail-styles.html` | 5. Thumbnail styles, shown visually (published privately: https://claude.ai/artifact/4ZPp2yNMNRvQccsNo3yyet). Labels: `thumbnails/labels-*.csv`; images: `thumbnails/images/`. |
| `recent-winners.md` | 6. What has worked recently (last 90 days, last 12 months, rising and falling). |
| `top-100.md`, `top-100.csv` | 7. The top 100 of all time. |
| `keyword-sweep.md`, `formats.md` | 8. The keyword sweep and the formats. |
| `CONCLUSIONS.md` | 9. After the back and forth with the operator (not written yet). |

## Other files

| Path | What it is |
|---|---|
| `README.md` | This file. |
| `REPORT-2026-10-26.md` | The research report for the operator: what was done, the findings, the 4 questions, where everything is. |
| `log.md` | Every round: what ran, the helpers, the checkers, every fix and the operator's decisions. |
| `labels.md` | Label definitions (emotions incl. new N1-N4, villains, formats incl. new ones, channel types, presenter background, the multiple, the length rule) and the rules clarified after the checkers. |
| `seeds.md` | Round 1: Silver Cymbal's electrical and fire videos. |
| `short-reference.md` | Under-5:00 hits, listed but never counted. |
| `thumbnails/report-*.md` | The two thumbnail labellers' reports; `thumbnails/labels-extra.csv` holds 4 thumbnails labelled by the main session after checker G. |
| `.gitignore` | Keeps Python caches and editor temp files out of git. |
| `data/jack-redfield/` | The stopped Jack Redfield generator channel, pulled 2026-10-26 for the operator's question (fit for the electrical lane versus Frederick's channel). |
| `data/tools/` | The scripts: `yt.py` (logged-out YouTube loader; notes on which sorts work), `merge_sweeps.py`, `channel_medians.py`, `subniche_map.py`, `top100_final.py`, `build_docs.py`, `build_channels.py`, `build_thumb_page.py`, `build_text_page.py`. The deliverables above are built by the last three; re-run them after any data fix. |
| `data/silver-cymbal/` | Round 1: Silver Cymbal's full video list and the seed CSV. |
| `data/known-channels/` | Round 1: the six known channels re-checked against the 2026-10-22 figures. |
| `data/just-stop-fire/` | Round 1: Frederick Barnes's own channel (named "Frederick Barnes" on YouTube). |
| `data/seed-spread/` | Round 1: the spread from Silver Cymbal's seeds (385 candidates). |
| `data/new-channels-nexlev/`, `data/new-channels-search/` | Round 1: the two new-channel hunts (incl. adjacent lanes later ruled out). |
| `data/channel-list/` | Round 2: the master list (957 channels, re-scoped). |
| `data/sweep/<group>/` | Round 2: the keyword sweep, six topic groups (wiring, panels, cords, devices, fire, explainers incl. `presenters.csv`); `wiring/tools/` keeps that helper's scripts as .txt. |
| `data/merged/` | Round 2-3: all sweep videos deduped (`videos-all.csv`), the checkers' `corrections.csv`, `videos-with-multiples.csv`, `subniche-map.csv`, `format-map.csv`. |
| `data/medians/` | Round 3: each channel's median long-form views (for the multiple). |
| `data/census/` | Round 3: the census chunks, `census-all.csv`, `nexlev-daily.csv` (30-day views), raw pulls. |
| `data/top100/` | Round 3: `top250-checked.csv` and `search-candidates-checked.csv` (the inputs), `top100-final.csv`, `top100-narrated.csv` (without unnarrated hack channels), recent lists; `top100.csv` is the helper's first version, kept for history. |
| `data/investigator/` | Round 3: the fire investigator / inspector deep look. |
| `data/labels/` | Round 4: the labelling sets, labelled files and summaries, `labelled-extra.csv` (4 top-100 videos labelled by the main session after checker G), `blind-sample.csv` (checker F's sample); `thumb-channels.csv` (round 5's channel list). |
| `data/checks/` | Every checker's results (A-H), `presenters-summary-corrected.csv`, `findings-recheck.csv`. |

Helper folders keep their helper's report (`report.md`, or `report-*.md` in `census/`, `labels/` and `thumbnails/`; saved by the main session, since helpers can't write report files) and, where they pulled pages, `raw/`. `medians/` and `merged/` are built by the main session's scripts and have no report.

## Dates pulled

Round 1: 2026-10-23. Round 2: 2026-10-24. Rounds 3-6: 2026-10-26. Each table says its source and date.
