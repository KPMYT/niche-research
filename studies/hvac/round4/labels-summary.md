# Round 4 labels: summary

Built 2026-10-26 by `data/tools/round4_build.py` from the round 4 hand labels (batches done: 1, 2, 3, 4, 5, 6, 7, 8 of 8). 16,892 titles labelled; scope y 14,156, n 1,671, ? 1,065. Only the 14,156 in-scope (y) videos are counted; 6,129 of them are from the last 12 months. Views are Videos-tab figures (rounded), dates approximate; the multiple is views / the channel's baseline (`channels.md`). **Every label is a reading from the title only.** Agreement between the 8 labellers on 40 shared titles: scope 97%, sub-niche 93%, format 93%, villain 96%, first emotion 89%, the most-voted emotion present 92% (average share of labellers agreeing with the majority).

**Round 6 changes (2026-10-26, after `round6/check-labels.md`):** ranking needs 50+ videos; 'adjacent' is listed but not ranked; median multiples and 2x shares use only channels whose baseline is 100+ views; a top-3-channels share column shows concentration; two labeller habits harmonized by rule: 191 craft stove builds with no heat word set to '?', 90 'Top N / N best' lists moved to brand-verdict. The blind re-label of 200 titles agreed 88% on scope, 90% sub-niche, 88% format, 95% villain, 68% first emotion (77% where both gave one).

## Calibration (40 titles, every labeller)

| Field | Average share agreeing with the majority |
|---|---:|
| scope_ok | 97% |
| subniche | 93% |
| format | 93% |
| villain | 96% |
| e1 | 89% |
| top_emotion_present | 92% |

## Counts (in scope)

| Field | Top values |
|---|---|
| subniche | offgrid-heat 2,103; ac-central 1,793; furnace 971; heat-pump 943; boiler-oldheat 895; brand-verdict 859; humidity-air 787; cooling-no-ac 690; hvac-general 612; mini-split 597; drafts-insulation 561; thermostat 518 |
| format | how-to 2,178; symptom-fix 2,037; secret 1,418; install-diy 1,329; explainer 1,301; cheap-hack 1,278; only-x 944; story 773; review 552; plain 459; test 446; mistakes 343 |
| villain | none 12,354; hvac-company 589; maker-shelf 381; own-habit 355; utility 166; insider 104; upsell 98; service-call 63; last-owner 46 |
| emotions | E1 2,966; E10 1,754; E19 1,187; E13 1,109; E5 915; E20 830; E15 784; E3 629; E4 598; E2 467; E6 402; E12 356; E17 352; E18 311; E14 241; E16 238; E8 215; E11 192; E7 161; E9 46 |
