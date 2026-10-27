# Electrical ideation

Ideation built on this study (`../CONCLUSIONS.md`). Channel-neutral while the channel is pinned.

| File | What |
|---|---|
| `round-1-ideas.csv` | Round 1 (2026-10-26): 34 ideas. Each has our title, format (F-numbers from `script-system/ideation/ideation-core/references/format-bank-master.md`), topic, thumbnail look (Board = character + blue explainer board; Point = character pointing at the problem), thumbnail words, emotion, villain, and the niche video it improves on. |
| `round-1-ideas.html` | The same as a page, each idea beside its source thumbnail, with the source's posting date and the topic's heat (published privately: https://claude.ai/artifact/RA9dH5LGVFZk92WzE9yG6e). Built by `../data/tools/build_ideas_page.py`. |
| `source-check.csv` | A second helper's live check of 12 of the 34 sources (NexLev, 2026-10-26): all 12 match. |
| `extra-topics.csv` | 13 deeper topics dug out of the recent winners (numbered 101-113). |
| `heat-raw/` | `topic_heat.py`'s raw pulls per topic: every matched title with views, age and where it was found. |
| `round-1-heat.csv`, `extra-topics-heat.csv` | `topic_heat.py`'s first counts, before the on-topic check. Superseded by `topic-heat.csv`. |
| `heat-judged.csv` | Three helpers' on-topic judgements for all 2,582 matched English titles. |
| `topic-heat.csv` | The cleaned topic heat for all 47 topics: source date, uploads since (same channel / others), last 12 months and 90 days, best recent upload, heat label, partial flag. Built by `../data/tools/clean_heat.py`. |
| `recent-formats.csv` | 33 recent winning title formats in this niche (R1-R33), each with its proof video. |
| `titles-50.csv` | 50 titles: a measured topic in a recent winning format, with heat and format source. |
| `titles-50.html` | The same as a page, hottest topics first (published privately: https://claude.ai/artifact/3QAKWSMampn4ai4pycKAh9). Built by `../data/tools/build_titles_page.py`. |
| `heat-judged-300k.csv` | A helper's on-topic judgements for the 376 videos of 300K+ not yet judged. |
| `channel-types.csv` | 150 channels typed real / faceless / AI persona / unclear by two helpers (NexLev check_faceless_channel). |
| `proof-candidates.json` | Every on-topic 300K+ video per topic, plus the sources: the input to the proof check. |
| `topic-proof.csv` | The operator's rule (300K+ faceless or 1M+ real) per topic: proven or not, the biggest proof and the count. Built by `../data/tools/topic_proof.py`. |
| `proven-formats.csv` | Formats whose proof clears the same bar, recent winners (P codes) plus bank formats. |
| `silver-cymbal-copies.csv` | Silver Cymbal's 1M+ electrical videos with lightly altered titles (operator, 2026-10-26). |
| `titles-50-v2.csv` | The 50 titles rebuilt on proven topics and proven formats (version 1 kept as `titles-50.csv`). |
| `round-2.html` | Round 2: the kept round-1 ideas (1, 2, 7, 12, 14, 29, 30, 31, 33), the Silver Cymbal copies and the 50 v2 titles, each with topic proof and heat (published privately: https://claude.ai/artifact/Mxf5cotJEuSLjDFnWAtdL9). Built by `../data/tools/build_round2_page.py`. |
| `initial-ideas.csv`, `initial-ideas.html` | The operator's 17 initial ideas (round 2 picks: A all 9, B 3 6 7 10 11, C 2 12 15) with reference, heat and thumbnail advice (published privately: https://claude.ai/artifact/QnG8dP83G7LZ84rpat3Qek). Built by `../data/tools/build_initial_page.py`. |
| `thumb-instructions.csv`, `thumb-instructions.xlsx` | Short thumbnail instructions for the 17 (operator-approved advice; A1 per the operator: the reference with its 2 arrows, only the text and character changed, logo removed), with links to each reference video and thumbnail, and a style reference for A30, C2 and C12. Built by `../data/tools/build_thumb_instructions.py`. |

Not yet: the operator's picks, the ideation skill, the base ideation plan and the thumbnail plan (on the operator's call).
