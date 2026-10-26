# HVAC sub-niche map (deliverable 3)

Built 2026-10-26 by `data/tools/subniche_map.py` (round 3 sub-niche helper) from the census pull of 2026-10-26 (`data/raw/census-videos-2026-10-26.csv`, `census-channels-2026-10-26.csv`). Nothing committed or pushed. **Not yet re-checked by a second helper (working rule 3).** Per-video table: `data/raw/subniches-2026-10-26.csv`.

## Read this first

- **Measured:** views (the Videos tab's **rounded** text, e.g. "24K", pulled logged out on 2026-10-26), the multiple (views / the channel's baseline, from `census_build.py`), counts.
- **Approximate:** upload dates come from the tab's age text ("3mo ago"), so "last 12 months" means age text up to "11mo ago" (about 2025-10-26 to 2026-10-26, edges fuzzy). Multiples inherit the rounding.
- **Readings, not measurements:** the HVAC mark (`is_hvac`, census rule), the tiers, the channel types and **every sub-niche tag** (a keyword rule on the title only; no thumbnails, descriptions or transcripts). Hand-check accuracy is below.
- **The multiple** (labels.md section 6): views / median views of the channel's long-form videos from the last 12 months (`12M`); if it had fewer than 10, the median of its last 30 long-form (`last30`). In the map set: 13,333 videos on the 12M rule, 4,771 on last30, 11 with no multiple. **Caution:** an old video against a recent baseline gets a high multiple partly from age and partly from the channel's recent decline, so the all-time multiples lean high for old-video sub-niches; the 12-month table is the fairer comparison.
- **Medians, not means,** and every row shows n. Sub-niches with n under 15 are listed separately, not ranked. "Biggest channel's share" warns when one channel makes most of a row.

## Summary (tiers A-C; sub-niches are rule-based readings, views tab-rounded, dates approximate)

**Top 15 homeowner sub-niches by median multiple, all time** (n >= 15; general catch-alls, trade and adjacent left out):

| # | Sub-niche | n | channels | median views | median multiple | share at 2x+ | biggest channel's share |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | AC: window | 80 | 39 | 30K | 7.29 | 70% | 11% |
| 2 | off-grid heat: DIY stove builds (cement, barrel, brick craft) | 409 | 37 | 88K | 5.72 | 67% | 22% |
| 3 | AC: portable | 96 | 39 | 20K | 4.29 | 64% | 10% |
| 4 | off-grid heat: diesel, propane and kerosene heaters | 112 | 33 | 18K | 3.67 | 60% | 48% |
| 5 | evaporative coolers | 132 | 27 | 11K | 3.56 | 67% | 17% |
| 6 | oil heat | 153 | 41 | 8.3K | 2.73 | 57% | 14% |
| 7 | thermostats | 431 | 170 | 7.5K | 2.64 | 54% | 8% |
| 8 | mini-split | 506 | 110 | 12K | 2.64 | 57% | 7% |
| 9 | brand verdicts | 983 | 175 | 1.6K | 2.62 | 55% | 18% |
| 10 | smart thermostats | 180 | 61 | 4.7K | 2.51 | 56% | 23% |
| 11 | condensate drain and water leaks | 128 | 61 | 11K | 2.40 | 54% | 14% |
| 12 | boilers, radiators and steam | 689 | 119 | 6.9K | 2.30 | 53% | 13% |
| 13 | indoor air and purifiers | 383 | 121 | 14K | 2.13 | 52% | 18% |
| 14 | furnaces | 615 | 142 | 3.1K | 2.08 | 51% | 10% |
| 15 | fans for cooling (ceiling, whole-house, box) | 161 | 91 | 7K | 2.02 | 50% | 4% |

**Top 15 homeowner sub-niches by median multiple, last 12 months** (n >= 15; general catch-alls, trade and adjacent left out):

| # | Sub-niche | n | channels | median views | median multiple | share at 2x+ | biggest channel's share |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | AC: window | 16 | 14 | 8K | 2.71 | 56% | 12% |
| 2 | evaporative coolers | 38 | 14 | 1.6K | 2.19 | 55% | 24% |
| 3 | off-grid heat: diesel, propane and kerosene heaters | 32 | 17 | 4.5K | 1.67 | 47% | 31% |
| 4 | off-grid heat: DIY stove builds (cement, barrel, brick craft) | 81 | 24 | 10K | 1.60 | 44% | 20% |
| 5 | fans for cooling (ceiling, whole-house, box) | 78 | 50 | 1.9K | 1.46 | 37% | 9% |
| 6 | brand verdicts | 477 | 112 | 691 | 1.44 | 41% | 14% |
| 7 | off-grid heat: wood and pellet stoves, fireplaces | 307 | 85 | 4.4K | 1.37 | 38% | 11% |
| 8 | drafts, insulation and windows | 240 | 124 | 1.6K | 1.34 | 39% | 4% |
| 9 | cooling without AC (tricks, DIY coolers) | 262 | 94 | 2.9K | 1.33 | 40% | 6% |
| 10 | smart thermostats | 74 | 22 | 1K | 1.29 | 35% | 53% |
| 11 | heat and power in an outage | 394 | 131 | 2.1K | 1.25 | 39% | 13% |
| 12 | thermostats | 166 | 98 | 1.4K | 1.23 | 34% | 8% |
| 13 | scams and upsells | 181 | 78 | 1K | 1.19 | 35% | 9% |
| 14 | furnaces | 169 | 77 | 702 | 1.16 | 32% | 19% |
| 15 | off-grid heat: free-heat tricks and DIY heaters | 949 | 123 | 5.1K | 1.15 | 37% | 16% |

**Biggest tier gaps, last 12 months** (A vs B/C, median multiple; both n >= 15, no cell where one channel made 50%+): mini-split 1.09 (n 49) vs 2.15 (n 47); buy or replace (sizing, repair vs replace, new system) 0.97 (n 60) vs 1.58 (n 16); heat and power in an outage 0.91 (n 96) vs 1.43 (n 298); indoor air and purifiers 0.87 (n 45) vs 1.33 (n 30); brand verdicts 1.69 (n 221) vs 1.23 (n 256); fans for cooling (ceiling, whole-house, box) 1.22 (n 37) vs 1.58 (n 41).

**Biggest tier gaps, all time** (A vs B/C, median multiple; both n >= 15, no cell where one channel made 50%+): AC: window 3.15 (n 40) vs 11.09 (n 40); condensate drain and water leaks 1.62 (n 93) vs 8.93 (n 35); furnaces 1.74 (n 471) vs 5.02 (n 144); AC: portable 2.36 (n 49) vs 5.41 (n 47); oil heat 1.66 (n 53) vs 4.59 (n 100); buy or replace (sizing, repair vs replace, new system) 1.27 (n 212) vs 4.12 (n 48).

**Biggest type gaps, last 12 months** (faceless (incl. persona) vs on camera, median multiple; both n >= 15, no cell where one channel made 50%+): coils and condenser cleaning 1.50 (n 28) vs 0.81 (n 19); thermostats 1.15 (n 130) vs 1.69 (n 32); off-grid heat: wood and pellet stoves, fireplaces 1.57 (n 201) vs 1.09 (n 103); ducts and vents 1.41 (n 84) vs 1.00 (n 28); off-grid heat: free-heat tricks and DIY heaters 1.15 (n 934) vs 1.54 (n 15); heat pumps 0.92 (n 71) vs 1.30 (n 121).

**Biggest type gaps, all time** (faceless (incl. persona) vs on camera, median multiple; both n >= 15, no cell where one channel made 50%+): thermostats 1.35 (n 230) vs 7.50 (n 173); off-grid heat: free-heat tricks and DIY heaters 1.58 (n 1156) vs 5.54 (n 123); off-grid heat: DIY stove builds (cement, barrel, brick craft) 6.03 (n 388) vs 2.52 (n 21); AC: window 9.03 (n 35) vs 6.45 (n 42); AC: portable 2.87 (n 45) vs 5.11 (n 50); oil heat 3.52 (n 92) vs 1.97 (n 37).

## Method

- **The map set:** every long-form (5:00+) video marked HVAC (`is_hvac = yes`) of the **tier A, B and C** channels: **18,104 videos from 568 channels** (10,302 A, 4,692 B, 3,110 C). Tier D (trade and company channels, 10,888 HVAC videos) is shown in its own table, as a contrast; tier X (under 10% HVAC) is in the CSV but not in any table.
- **Last 12 months:** 7,147 of those videos.
- **Sub-niche rules:** `SUBNICHE_RULES` in `subniche_map.py` (my own file; `census_build.py` was not edited). Each fine sub-niche rolls up to its `labels.md` section 4 parent; the ones marked "NEW (not in labels.md)" (smells and noises, evaporative coolers, cooling without AC, fans for cooling, RV / van / camping, garage and shop, error codes, and the general catch-alls) are **proposals** and need the operator's yes before `labels.md` takes them. Fine splits inside a parent (refrigerant, coils, condensate drain inside AC: central; smart thermostats inside thermostats; oil heat inside boilers and old-house heat; the six off-grid splits (DIY stove builds, free-heat tricks, wood and pellet stoves, diesel / propane / kerosene heaters, electric space heaters, staying warm); scams, quotes, contractor choice and buy-or-replace inside buying and replacing) are also my proposals.
- **One primary sub-niche per video. Ties break by rule order: the first rule that matches wins.** The order (top of `subniche_map.py`): out-of-scope, adjacent and trade-facing first; then the homeowner *question* the title sells (outage, scams, the bill, cost and quotes, brands, contractor, buy or replace, smells and noises), which wins over the equipment named; then distinct appliance families (coolers, fans, portable, window, RV, garage, mini-split, heat pumps); then the component (thermostat, filter, part, refrigerant, coil, drain, ducts, humidity, indoor air, CO, insulation), which wins over the system it sits in; then heat-system families; then broad topics; then catch-alls. Every rule a title matched is in the CSV's `all_tags` column.
- **Scope:** `home` sub-niches are ranked. `trade` (careers and tech life, technical training, commercial), `adjacent` (water heaters, frozen pipes, fridges, solar and batteries; labels.md: "seen but not counted") and `out` (vehicle AC) are shown in their own table, not ranked. `general` catch-alls (heating or cooling with no equipment or topic named, HVAC basics) are mapped but flagged.
- **Coverage:** the census builder left 2,974 of 18,104 A-C HVAC titles unmapped (16.4%; 23.0% of A-D). This map leaves **96 unmapped (0.5%)** of A-C (158, 0.5% of A-D). A further 908 (5.0%) fall to a `general` catch-all, so 5.5% have no specific topic. Many of the unmapped are not HVAC at all (errors of the `is_hvac` title mark, e.g. juicers, lawn care), which this map does not re-decide.
- **Channel types:** the round 3 type helpers' files (census-types-A-2026-10-26.csv, census-types-B-2026-10-26.csv, census-types-C-2026-10-26.csv) typed 568 of the 568 A-C channels in the map. Types there are the helpers' readings from thumbnail sheets and About text, not measurements; not yet re-checked by a second helper here.
  Typed A-C channels in the map: on camera 163, faceless 235, faceless persona 120, other (brand, AI avatar) 50, untyped 0 (videos: on camera 6,291, faceless 8,298, faceless persona 1,681, other 1,834, untyped 0). The type split covers typed channels only.

## The map, all time (tiers A-C, sorted by median multiple)

All 18,104 A-C HVAC videos (all time): median views 5.2K, median multiple 1.77, share at 2x+ 47%. Homeowner and general sub-niches with n >= 15:

| # | Sub-niche (reading) | labels.md parent | n videos | channels | median views | median multiple (n with multiple) | share at 2x+ | biggest channel's share of n | faceless-persona videos |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | AC: window | AC: window | 80 | 39 | 30K | 7.29 (80) | 70% | 11% | 2 |
| 2 | off-grid heat: DIY stove builds (cement, barrel, brick craft) | alternative and supplemental heat (off-grid heat) | 409 | 37 | 88K | 5.72 (409) | 67% | 22% | 3 |
| 3 | AC: portable | AC: portable | 96 | 39 | 20K | 4.29 (96) | 64% | 10% | 6 |
| 4 | off-grid heat: diesel, propane and kerosene heaters | alternative and supplemental heat (off-grid heat) | 112 | 33 | 18K | 3.67 (112) | 60% | 48% | 7 |
| 5 | evaporative coolers | NEW (not in labels.md) | 132 | 27 | 11K | 3.56 (132) | 67% | 17% | 0 |
| 6 | oil heat | boilers and old-house heat | 153 | 41 | 8.3K | 2.73 (153) | 57% | 14% | 2 |
| 7 | mini-split | mini-split | 506 | 110 | 12K | 2.64 (506) | 57% | 7% | 2 |
| 8 | thermostats | thermostats | 431 | 170 | 7.5K | 2.64 (431) | 54% | 8% | 65 |
| 9 | brand verdicts | brand verdicts | 983 | 175 | 1.6K | 2.62 (983) | 55% | 18% | 82 |
| 10 | smart thermostats | thermostats | 180 | 61 | 4.7K | 2.51 (180) | 56% | 23% | 4 |
| 11 | condensate drain and water leaks | AC: central | 128 | 61 | 11K | 2.40 (128) | 54% | 14% | 5 |
| 12 | boilers, radiators and steam | boilers and old-house heat | 689 | 119 | 6.9K | 2.30 (689) | 53% | 13% | 10 |
| 13 | indoor air and purifiers | humidity, ventilation and indoor air | 383 | 121 | 14K | 2.13 (383) | 52% | 18% | 5 |
| 14 | furnaces | furnaces | 615 | 142 | 3.1K | 2.08 (614) | 51% | 10% | 61 |
| 15 | fans for cooling (ceiling, whole-house, box) | NEW (not in labels.md) | 161 | 91 | 7K | 2.02 (161) | 50% | 4% | 17 |
| 16 | coils and condenser cleaning | AC: central | 267 | 98 | 4.5K | 2.00 (267) | 50% | 7% | 9 |
| 17 | off-grid heat: wood and pellet stoves, fireplaces | alternative and supplemental heat (off-grid heat) | 723 | 143 | 17K | 1.98 (723) | 50% | 15% | 84 |
| 18 | parts homeowners touch | parts homeowners touch | 798 | 138 | 7K | 1.97 (793) | 50% | 6% | 9 |
| 19 | error codes and troubleshooting | NEW (not in labels.md) | 168 | 57 | 6K | 1.85 (168) | 48% | 22% | 4 |
| 20 | ducts and vents | ducts and vents | 512 | 154 | 4K | 1.83 (512) | 49% | 7% | 20 |
| 21 | smells and noises | NEW (not in labels.md) | 146 | 79 | 3.9K | 1.82 (146) | 49% | 5% | 3 |
| 22 | off-grid heat: free-heat tricks and DIY heaters | alternative and supplemental heat (off-grid heat) | 1,283 | 156 | 8.6K | 1.79 (1283) | 48% | 12% | 173 |
| 23 | scams and upsells | buying and replacing a system | 264 | 109 | 2.4K | 1.71 (264) | 45% | 8% | 97 |
| 24 | garage, shop and outbuildings | NEW (not in labels.md) | 24 | 19 | 16K | 1.67 (24) | 46% | 8% | 5 |
| 25 | heat pumps | heat pumps | 953 | 137 | 4.9K | 1.66 (953) | 45% | 10% | 19 |
| 26 | AC: central | AC: central | 1,300 | 219 | 2.9K | 1.65 (1298) | 45% | 8% | 91 |
| 27 | humidity and dehumidifiers | humidity, ventilation and indoor air | 368 | 131 | 7.2K | 1.65 (368) | 45% | 17% | 22 |
| 28 | refrigerant | AC: central | 357 | 103 | 4.3K | 1.62 (357) | 45% | 5% | 13 |
| 29 | drafts, insulation and windows | drafts, insulation and air sealing | 507 | 207 | 5.4K | 1.60 (507) | 45% | 6% | 77 |
| 30 | heating fuel and fuel choice | heating fuel and fuel choice | 41 | 28 | 7.2K | 1.60 (41) | 41% | 12% | 3 |
| 31 | heat and power in an outage | heat and power in an outage | 499 | 177 | 3.5K | 1.54 (499) | 44% | 10% | 176 |
| 32 | filters | filters | 188 | 122 | 5.2K | 1.54 (188) | 45% | 4% | 33 |
| 33 | cooling without AC (tricks, DIY coolers) | NEW (not in labels.md) | 300 | 109 | 3.6K | 1.46 (300) | 44% | 5% | 68 |
| 34 | buy or replace (sizing, repair vs replace, new system) | buying and replacing a system | 260 | 118 | 7.4K | 1.46 (260) | 41% | 7% | 13 |
| 35 | space heaters (electric) | alternative and supplemental heat (off-grid heat) | 180 | 109 | 5.4K | 1.35 (180) | 42% | 9% | 25 |
| 36 | general: HVAC, topic not named (general) | NEW (not in labels.md) | 623 | 105 | 3.3K | 1.32 (623) | 38% | 8% | 29 |
| 37 | general: no heat (equipment not named) (general) | NEW (not in labels.md) | 46 | 22 | 3K | 1.32 (46) | 35% | 9% | 1 |
| 38 | carbon monoxide and gas safety | humidity, ventilation and indoor air | 64 | 41 | 1.7K | 1.19 (64) | 39% | 14% | 4 |
| 39 | general: heating (equipment not named) (general) | NEW (not in labels.md) | 204 | 110 | 5K | 1.17 (204) | 38% | 8% | 24 |
| 40 | energy bills | energy bills | 717 | 230 | 2.3K | 1.17 (716) | 35% | 4% | 195 |
| 41 | choosing a contractor | buying and replacing a system | 112 | 53 | 2.9K | 1.11 (112) | 37% | 11% | 12 |
| 42 | seasonal maintenance | seasonal maintenance | 278 | 148 | 1.1K | 1.08 (277) | 35% | 6% | 81 |
| 43 | general: cooling (equipment not named) (general) | NEW (not in labels.md) | 21 | 16 | 4.3K | 1.04 (21) | 29% | 19% | 1 |
| 44 | replacement cost and quotes | buying and replacing a system | 201 | 98 | 1.2K | 1.03 (201) | 37% | 7% | 26 |
| 45 | staying warm without heating (body, bed, clothes) | alternative and supplemental heat (off-grid heat) | 101 | 77 | 1.1K | 0.94 (101) | 27% | 4% | 50 |
| 46 | RV, van, tent and camping heat or cool | NEW (not in labels.md) | 33 | 25 | 4.9K | 0.93 (33) | 30% | 12% | 1 |

**n under 15 (all time), not ranked:** general: HVAC basics and how it works (n 14, median views 2.7K, median multiple 1.50).

**Trade-facing, adjacent, out of scope and unmapped (all time), not ranked:**

| # | Sub-niche (reading) | labels.md parent | n videos | channels | median views | median multiple (n with multiple) | share at 2x+ | biggest channel's share of n | faceless-persona videos |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| - | trade: technical training | trade-facing | 488 | 93 | 11K | 3.77 (487) | 59% | 34% | 5 |
| - | adjacent: water heaters | adjacent: water heaters | 6 | 6 | 2.7K | 1.58 (6) | 50% | 17% | 1 |
| - | trade: commercial and refrigeration | trade-facing | 289 | 69 | 2.8K | 1.44 (289) | 40% | 9% | 10 |
| - | trade: careers, business and tech life | trade-facing | 546 | 81 | 4.2K | 1.19 (546) | 30% | 23% | 2 |
| - | HVAC, not mapped | not mapped | 96 | 48 | 4.8K | 1.13 (96) | 38% | 12% | 15 |
| - | adjacent: solar, batteries and home energy systems | adjacent: solar and home energy | 65 | 37 | 4.6K | 0.90 (65) | 26% | 12% | 8 |
| - | out of scope: vehicle AC and heat | out of scope | 3 | 2 | 449 | 0.60 (3) | 33% | 67% | 0 |
| - | adjacent: frozen pipes | adjacent: frozen pipes | 1 | 1 | 32 | 0.15 (1) | 0% | 100% | 1 |

**Rolled up to the labels.md parents (all time):**

| labels.md parent | n | channels | median views | median multiple | share at 2x+ |
|---|---:|---:|---:|---:|---:|
| AC: window | 80 | 39 | 30K | 7.29 | 70% |
| AC: portable | 96 | 39 | 20K | 4.29 | 64% |
| mini-split | 506 | 110 | 12K | 2.64 | 57% |
| brand verdicts | 983 | 175 | 1.6K | 2.62 | 55% |
| thermostats | 611 | 186 | 6.4K | 2.62 | 55% |
| boilers and old-house heat | 842 | 137 | 7.2K | 2.35 | 54% |
| furnaces | 615 | 142 | 3.1K | 2.08 | 51% |
| alternative and supplemental heat (off-grid heat) | 2,808 | 324 | 13K | 2.04 | 50% |
| parts homeowners touch | 798 | 138 | 7K | 1.97 | 50% |
| ducts and vents | 512 | 154 | 4K | 1.83 | 49% |
| humidity, ventilation and indoor air | 815 | 214 | 9.3K | 1.78 | 48% |
| AC: central | 2,052 | 263 | 3.6K | 1.70 | 46% |
| heat pumps | 953 | 137 | 4.9K | 1.66 | 45% |
| drafts, insulation and air sealing | 507 | 207 | 5.4K | 1.60 | 45% |
| heating fuel and fuel choice | 41 | 28 | 7.2K | 1.60 | 41% |
| NEW (not in labels.md) | 1,872 | 345 | 4.3K | 1.56 | 44% |
| heat and power in an outage | 499 | 177 | 3.5K | 1.54 | 44% |
| filters | 188 | 122 | 5.2K | 1.54 | 45% |
| buying and replacing a system | 837 | 224 | 3K | 1.42 | 41% |
| energy bills | 717 | 230 | 2.3K | 1.17 | 35% |
| seasonal maintenance | 278 | 148 | 1.1K | 1.08 | 35% |

## The map, last 12 months (tiers A-C, sorted by median multiple)

All 7,147 A-C HVAC videos (last 12 months): median views 1.8K, median multiple 1.10, share at 2x+ 33%. Homeowner and general sub-niches with n >= 15:

| # | Sub-niche (reading) | labels.md parent | n videos | channels | median views | median multiple (n with multiple) | share at 2x+ | biggest channel's share of n | faceless-persona videos |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | AC: window | AC: window | 16 | 14 | 8K | 2.71 (16) | 56% | 12% | 2 |
| 2 | evaporative coolers | NEW (not in labels.md) | 38 | 14 | 1.6K | 2.19 (38) | 55% | 24% | 0 |
| 3 | off-grid heat: diesel, propane and kerosene heaters | alternative and supplemental heat (off-grid heat) | 32 | 17 | 4.5K | 1.67 (32) | 47% | 31% | 7 |
| 4 | off-grid heat: DIY stove builds (cement, barrel, brick craft) | alternative and supplemental heat (off-grid heat) | 81 | 24 | 10K | 1.60 (81) | 44% | 20% | 3 |
| 5 | fans for cooling (ceiling, whole-house, box) | NEW (not in labels.md) | 78 | 50 | 1.9K | 1.46 (78) | 37% | 9% | 17 |
| 6 | brand verdicts | brand verdicts | 477 | 112 | 691 | 1.44 (477) | 41% | 14% | 82 |
| 7 | off-grid heat: wood and pellet stoves, fireplaces | alternative and supplemental heat (off-grid heat) | 307 | 85 | 4.4K | 1.37 (307) | 38% | 11% | 84 |
| 8 | drafts, insulation and windows | drafts, insulation and air sealing | 240 | 124 | 1.6K | 1.34 (240) | 39% | 4% | 77 |
| 9 | cooling without AC (tricks, DIY coolers) | NEW (not in labels.md) | 262 | 94 | 2.9K | 1.33 (262) | 40% | 6% | 68 |
| 10 | smart thermostats | thermostats | 74 | 22 | 1K | 1.29 (74) | 35% | 53% | 4 |
| 11 | heat and power in an outage | heat and power in an outage | 394 | 131 | 2.1K | 1.25 (394) | 39% | 13% | 176 |
| 12 | thermostats | thermostats | 166 | 98 | 1.4K | 1.23 (166) | 34% | 8% | 65 |
| 13 | scams and upsells | buying and replacing a system | 181 | 78 | 1K | 1.19 (181) | 35% | 9% | 97 |
| 14 | furnaces | furnaces | 169 | 77 | 702 | 1.16 (169) | 32% | 19% | 60 |
| 15 | off-grid heat: free-heat tricks and DIY heaters | alternative and supplemental heat (off-grid heat) | 949 | 123 | 5.1K | 1.15 (949) | 37% | 16% | 173 |
| 16 | heat pumps | heat pumps | 287 | 81 | 2.3K | 1.15 (287) | 33% | 18% | 19 |
| 17 | mini-split | mini-split | 96 | 44 | 5.2K | 1.15 (96) | 44% | 10% | 2 |
| 18 | coils and condenser cleaning | AC: central | 50 | 39 | 2.9K | 1.14 (50) | 28% | 10% | 9 |
| 19 | general: no heat (equipment not named) (general) | NEW (not in labels.md) | 15 | 10 | 3K | 1.14 (15) | 13% | 27% | 1 |
| 20 | condensate drain and water leaks | AC: central | 24 | 19 | 1.9K | 1.09 (24) | 33% | 12% | 5 |
| 21 | ducts and vents | ducts and vents | 162 | 68 | 660 | 1.08 (162) | 30% | 23% | 20 |
| 22 | filters | filters | 74 | 60 | 914 | 1.06 (74) | 30% | 4% | 33 |
| 23 | smells and noises | NEW (not in labels.md) | 32 | 26 | 534 | 1.06 (32) | 22% | 9% | 3 |
| 24 | AC: portable | AC: portable | 28 | 18 | 1.1K | 1.03 (28) | 29% | 14% | 6 |
| 25 | refrigerant | AC: central | 91 | 45 | 1.9K | 1.02 (91) | 24% | 11% | 13 |
| 26 | AC: central | AC: central | 465 | 140 | 1.7K | 1.01 (465) | 31% | 7% | 89 |
| 27 | heating fuel and fuel choice | heating fuel and fuel choice | 18 | 12 | 4.8K | 1.00 (18) | 39% | 28% | 3 |
| 28 | energy bills | energy bills | 532 | 174 | 1.1K | 1.00 (532) | 31% | 6% | 194 |
| 29 | boilers, radiators and steam | boilers and old-house heat | 164 | 56 | 1K | 1.00 (164) | 22% | 11% | 10 |
| 30 | humidity and dehumidifiers | humidity, ventilation and indoor air | 147 | 85 | 1.5K | 1.00 (147) | 29% | 6% | 22 |
| 31 | general: HVAC, topic not named (general) | NEW (not in labels.md) | 135 | 54 | 1K | 1.00 (135) | 29% | 13% | 29 |
| 32 | oil heat | boilers and old-house heat | 47 | 19 | 1.8K | 1.00 (47) | 28% | 19% | 2 |
| 33 | choosing a contractor | buying and replacing a system | 42 | 31 | 1.7K | 1.00 (42) | 33% | 10% | 12 |
| 34 | buy or replace (sizing, repair vs replace, new system) | buying and replacing a system | 76 | 51 | 1.7K | 0.99 (76) | 18% | 8% | 13 |
| 35 | space heaters (electric) | alternative and supplemental heat (off-grid heat) | 85 | 61 | 1.7K | 0.99 (85) | 27% | 6% | 25 |
| 36 | seasonal maintenance | seasonal maintenance | 169 | 98 | 652 | 0.95 (169) | 28% | 5% | 80 |
| 37 | parts homeowners touch | parts homeowners touch | 122 | 58 | 2.4K | 0.92 (122) | 20% | 8% | 4 |
| 38 | replacement cost and quotes | buying and replacing a system | 103 | 55 | 363 | 0.91 (103) | 27% | 8% | 26 |
| 39 | indoor air and purifiers | humidity, ventilation and indoor air | 75 | 43 | 1.6K | 0.91 (75) | 32% | 11% | 5 |
| 40 | staying warm without heating (body, bed, clothes) | alternative and supplemental heat (off-grid heat) | 92 | 69 | 773 | 0.90 (92) | 23% | 4% | 50 |
| 41 | error codes and troubleshooting | NEW (not in labels.md) | 41 | 27 | 3.7K | 0.85 (41) | 27% | 24% | 4 |
| 42 | general: heating (equipment not named) (general) | NEW (not in labels.md) | 109 | 73 | 1K | 0.79 (109) | 25% | 6% | 24 |

**n under 15 (last 12 months), not ranked:** RV, van, tent and camping heat or cool (n 14, median views 3.4K, median multiple 0.93); carbon monoxide and gas safety (n 13, median views 109, median multiple 0.68); garage, shop and outbuildings (n 13, median views 2K, median multiple 1.34); general: cooling (equipment not named) (n 13, median views 8.6K, median multiple 1.48); general: HVAC basics and how it works (n 3, median views 433, median multiple 0.61).

**Trade-facing, adjacent, out of scope and unmapped (last 12 months), not ranked:**

| # | Sub-niche (reading) | labels.md parent | n videos | channels | median views | median multiple (n with multiple) | share at 2x+ | biggest channel's share of n | faceless-persona videos |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| - | adjacent: water heaters | adjacent: water heaters | 2 | 2 | 2.7K | 1.41 (2) | 50% | 50% | 1 |
| - | trade: technical training | trade-facing | 44 | 29 | 1.9K | 1.25 (44) | 30% | 11% | 4 |
| - | trade: careers, business and tech life | trade-facing | 137 | 31 | 4.3K | 1.04 (137) | 17% | 61% | 2 |
| - | trade: commercial and refrigeration | trade-facing | 67 | 35 | 1.3K | 0.97 (67) | 21% | 15% | 10 |
| - | adjacent: solar, batteries and home energy systems | adjacent: solar and home energy | 42 | 26 | 4.9K | 0.96 (42) | 21% | 17% | 8 |
| - | HVAC, not mapped | not mapped | 52 | 33 | 1.2K | 0.90 (52) | 35% | 15% | 15 |
| - | out of scope: vehicle AC and heat | out of scope | 1 | 1 | 449 | 0.60 (1) | 0% | 100% | 0 |
| - | adjacent: frozen pipes | adjacent: frozen pipes | 1 | 1 | 32 | 0.15 (1) | 0% | 100% | 1 |

**Rolled up to the labels.md parents (last 12 months):**

| labels.md parent | n | channels | median views | median multiple | share at 2x+ |
|---|---:|---:|---:|---:|---:|
| AC: window | 16 | 14 | 8K | 2.71 | 56% |
| brand verdicts | 477 | 112 | 691 | 1.44 | 41% |
| drafts, insulation and air sealing | 240 | 124 | 1.6K | 1.34 | 39% |
| heat and power in an outage | 394 | 131 | 2.1K | 1.25 | 39% |
| thermostats | 240 | 108 | 1.2K | 1.23 | 34% |
| alternative and supplemental heat (off-grid heat) | 1,546 | 223 | 4.4K | 1.17 | 36% |
| furnaces | 169 | 77 | 702 | 1.16 | 32% |
| heat pumps | 287 | 81 | 2.3K | 1.15 | 33% |
| mini-split | 96 | 44 | 5.2K | 1.15 | 44% |
| NEW (not in labels.md) | 753 | 236 | 1.9K | 1.12 | 34% |
| ducts and vents | 162 | 68 | 660 | 1.08 | 30% |
| filters | 74 | 60 | 914 | 1.06 | 30% |
| AC: portable | 28 | 18 | 1.1K | 1.03 | 29% |
| AC: central | 630 | 166 | 1.8K | 1.03 | 30% |
| heating fuel and fuel choice | 18 | 12 | 4.8K | 1.00 | 39% |
| energy bills | 532 | 174 | 1.1K | 1.00 | 31% |
| boilers and old-house heat | 211 | 69 | 1.2K | 1.00 | 23% |
| buying and replacing a system | 402 | 139 | 946 | 1.00 | 30% |
| seasonal maintenance | 169 | 98 | 652 | 0.95 | 28% |
| humidity, ventilation and indoor air | 235 | 117 | 1.4K | 0.94 | 29% |
| parts homeowners touch | 122 | 58 | 2.4K | 0.92 | 20% |

## Split by tier: A vs B/C

Tier A = 50%+ of the latest 30 long-form titles HVAC; B/C = 10-49% (C = adjacent-lane channels: off-grid, old ways, frugal, energy). Rows sorted by the size of the gap (where both sides have n >= 15), then by n; rows with fewer than 15 videos in total are left out. `*` after an n = one channel made 50%+ of that cell (read it as that channel, not the sub-niche). All-time gaps mix in video age (old videos on a recent baseline); the 12-month gaps are the fairer ones.

### all time

| Sub-niche | A n | A median views | A median multiple | A 2x+ | B/C n | B/C median views | B/C median multiple | B/C 2x+ | gap in median multiple (A minus B/C; both n >= 15) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| smart thermostats | 108 | 1.8K | 1.52 | 44% | 72* | 51K | 10.68 | 74% | -9.17 |
| AC: window | 40 | 16K | 3.15 | 62% | 40 | 72K | 11.09 | 78% | -7.94 |
| condensate drain and water leaks | 93 | 8.2K | 1.62 | 47% | 35 | 52K | 8.93 | 71% | -7.31 |
| evaporative coolers | 31* | 10K | 1.33 | 35% | 101 | 12K | 5.73 | 77% | -4.40 |
| off-grid heat: DIY stove builds (cement, barrel, brick craft) | 26* | 5K | 2.04 | 50% | 383 | 103K | 6.00 | 68% | -3.96 |
| furnaces | 471 | 2.4K | 1.74 | 46% | 144 | 7.8K | 5.02 | 66% | -3.28 |
| AC: portable | 49 | 20K | 2.36 | 53% | 47 | 16K | 5.41 | 74% | -3.05 |
| oil heat | 53 | 3K | 1.66 | 45% | 100 | 15K | 4.59 | 63% | -2.93 |
| buy or replace (sizing, repair vs replace, new system) | 212 | 5K | 1.27 | 36% | 48 | 19K | 4.12 | 62% | -2.85 |
| fans for cooling (ceiling, whole-house, box) | 80 | 2.2K | 1.55 | 45% | 81 | 23K | 4.38 | 56% | -2.83 |
| ducts and vents | 373 | 3.2K | 1.64 | 46% | 139 | 9.9K | 3.39 | 56% | -1.75 |
| mini-split | 343 | 10K | 2.21 | 52% | 163 | 17K | 3.83 | 66% | -1.62 |
| indoor air and purifiers | 151 | 7.8K | 1.27 | 40% | 232 | 19K | 2.88 | 59% | -1.60 |
| parts homeowners touch | 553 | 6.2K | 1.71 | 45% | 245 | 8.2K | 3.24 | 59% | -1.53 |
| boilers, radiators and steam | 423 | 3.8K | 1.96 | 50% | 266 | 25K | 3.35 | 59% | -1.39 |
| smells and noises | 109 | 2.5K | 1.65 | 45% | 37 | 18K | 2.90 | 59% | -1.25 |
| refrigerant | 295 | 4.2K | 1.50 | 41% | 62 | 4.8K | 2.55 | 61% | -1.05 |
| thermostats | 299 | 9.7K | 3.10 | 56% | 132 | 5.2K | 2.17 | 51% | +0.93 |
| heating fuel and fuel choice | 22 | 6.5K | 1.19 | 32% | 19 | 10K | 2.03 | 53% | -0.84 |
| drafts, insulation and windows | 201 | 1.9K | 1.29 | 35% | 306 | 10K | 2.06 | 51% | -0.77 |
| off-grid heat: wood and pellet stoves, fireplaces | 187 | 5.7K | 1.53 | 42% | 536 | 24K | 2.27 | 53% | -0.74 |
| heat and power in an outage | 145 | 1.1K | 1.00 | 36% | 354 | 4.6K | 1.71 | 47% | -0.71 |
| scams and upsells | 216 | 2.3K | 1.65 | 44% | 48 | 2.8K | 2.31 | 52% | -0.67 |
| coils and condenser cleaning | 176 | 4.7K | 1.82 | 48% | 91 | 4.4K | 2.38 | 54% | -0.56 |
| space heaters (electric) | 70 | 3.6K | 1.04 | 34% | 110 | 7.5K | 1.59 | 46% | -0.55 |
| heat pumps | 742 | 4K | 1.58 | 43% | 211 | 7.6K | 2.03 | 51% | -0.45 |
| off-grid heat: free-heat tricks and DIY heaters | 212 | 2.8K | 1.44 | 42% | 1,071 | 10K | 1.89 | 49% | -0.45 |
| seasonal maintenance | 179 | 765 | 0.96 | 33% | 99 | 1.8K | 1.36 | 38% | -0.40 |
| carbon monoxide and gas safety | 45 | 1.7K | 1.17 | 38% | 19 | 1.3K | 1.57 | 42% | -0.40 |
| filters | 105 | 3.8K | 1.46 | 43% | 83 | 10K | 1.81 | 47% | -0.35 |
| brand verdicts | 498 | 5.2K | 2.48 | 54% | 485 | 367 | 2.75 | 57% | -0.27 |
| replacement cost and quotes | 153 | 1.1K | 1.27 | 40% | 48 | 2.1K | 1.00 | 29% | +0.27 |
| energy bills | 255 | 1K | 1.00 | 31% | 462 | 4K | 1.24 | 37% | -0.24 |
| general: HVAC, topic not named | 550 | 3.5K | 1.38 | 39% | 73 | 1.7K | 1.18 | 34% | +0.20 |
| cooling without AC (tricks, DIY coolers) | 89 | 1.1K | 1.32 | 42% | 211 | 6.2K | 1.51 | 45% | -0.19 |
| staying warm without heating (body, bed, clothes) | 31 | 690 | 1.02 | 26% | 70 | 1.4K | 0.90 | 27% | +0.12 |
| humidity and dehumidifiers | 182 | 6.2K | 1.71 | 46% | 186 | 9.7K | 1.61 | 44% | +0.09 |
| error codes and troubleshooting | 141 | 6K | 1.85 | 48% | 27 | 3.5K | 1.93 | 48% | -0.08 |
| AC: central | 1,011 | 2.8K | 1.65 | 45% | 289 | 4.3K | 1.69 | 47% | -0.04 |
| general: heating (equipment not named) | 53 | 2.1K | 1.17 | 30% | 151 | 5.7K | 1.18 | 41% | -0.01 |
| off-grid heat: diesel, propane and kerosene heaters | 13 | 6.4K | 1.17 | 31% | 99* | 19K | 3.93 | 64% | - |
| choosing a contractor | 102 | 2.9K | 1.02 | 38% | 10 | 3K | 1.29 | 20% | - |
| general: no heat (equipment not named) | 35 | 4.6K | 1.35 | 43% | 11 | 2.3K | 1.27 | 9% | - |
| RV, van, tent and camping heat or cool | 9 | 2.6K | 0.87 | 22% | 24 | 6K | 0.94 | 33% | - |
| garage, shop and outbuildings | 12 | 1.6K | 1.33 | 33% | 12 | 126K | 2.66 | 58% | - |
| general: cooling (equipment not named) | 4 | 5.2K | 1.16 | 25% | 17 | 4.3K | 0.90 | 29% | - |

### last 12 months

| Sub-niche | A n | A median views | A median multiple | A 2x+ | B/C n | B/C median views | B/C median multiple | B/C 2x+ | gap in median multiple (A minus B/C; both n >= 15) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| off-grid heat: DIY stove builds (cement, barrel, brick craft) | 20* | 7K | 2.72 | 55% | 61 | 13K | 1.33 | 41% | +1.39 |
| mini-split | 49 | 5.1K | 1.09 | 37% | 47 | 5.2K | 2.15 | 51% | -1.06 |
| buy or replace (sizing, repair vs replace, new system) | 60 | 1.1K | 0.97 | 12% | 16 | 6.8K | 1.58 | 44% | -0.60 |
| heat and power in an outage | 96 | 579 | 0.91 | 26% | 298 | 3.5K | 1.43 | 43% | -0.52 |
| indoor air and purifiers | 45 | 1K | 0.87 | 27% | 30 | 1.6K | 1.33 | 40% | -0.46 |
| brand verdicts | 221 | 2.9K | 1.69 | 46% | 256 | 140 | 1.23 | 37% | +0.46 |
| fans for cooling (ceiling, whole-house, box) | 37 | 903 | 1.22 | 38% | 41 | 5.9K | 1.58 | 37% | -0.36 |
| oil heat | 15* | 371 | 0.66 | 20% | 32 | 2.5K | 1.00 | 31% | -0.34 |
| scams and upsells | 146 | 904 | 1.08 | 34% | 35 | 1K | 1.41 | 40% | -0.33 |
| staying warm without heating (body, bed, clothes) | 31 | 690 | 1.02 | 26% | 61 | 1K | 0.71 | 21% | +0.31 |
| general: HVAC, topic not named | 118 | 1K | 1.02 | 30% | 17 | 2.3K | 0.74 | 24% | +0.28 |
| smart thermostats | 58* | 1.1K | 1.17 | 34% | 16 | 185 | 1.44 | 38% | -0.27 |
| coils and condenser cleaning | 29 | 1.6K | 1.33 | 28% | 21 | 4.5K | 1.06 | 29% | +0.27 |
| cooling without AC (tricks, DIY coolers) | 75 | 1.1K | 1.19 | 37% | 187 | 5.1K | 1.43 | 42% | -0.24 |
| drafts, insulation and windows | 105 | 946 | 1.48 | 44% | 135 | 2.2K | 1.24 | 36% | +0.24 |
| parts homeowners touch | 70 | 2.5K | 0.88 | 13% | 52 | 2.1K | 1.10 | 31% | -0.22 |
| off-grid heat: wood and pellet stoves, fireplaces | 153 | 3.8K | 1.47 | 39% | 154 | 4.8K | 1.31 | 38% | +0.16 |
| general: heating (equipment not named) | 22 | 307 | 0.67 | 23% | 87 | 1.1K | 0.82 | 25% | -0.15 |
| heat pumps | 222 | 1.8K | 1.13 | 32% | 65 | 6.2K | 1.23 | 37% | -0.10 |
| thermostats | 107 | 939 | 1.21 | 38% | 59 | 1.9K | 1.31 | 25% | -0.10 |
| seasonal maintenance | 103 | 339 | 0.94 | 26% | 66 | 1.4K | 1.03 | 32% | -0.09 |
| AC: central | 332 | 1.5K | 1.00 | 30% | 133 | 2.3K | 1.06 | 32% | -0.06 |
| humidity and dehumidifiers | 56 | 2.8K | 0.95 | 32% | 91 | 1.2K | 1.01 | 27% | -0.06 |
| furnaces | 131 | 552 | 1.16 | 30% | 38 | 1.6K | 1.21 | 39% | -0.05 |
| boilers, radiators and steam | 87 | 626 | 1.02 | 17% | 77 | 2.6K | 0.97 | 27% | +0.05 |
| energy bills | 198 | 505 | 0.99 | 28% | 334 | 1.8K | 1.04 | 33% | -0.05 |
| space heaters (electric) | 30 | 1.9K | 0.95 | 27% | 55 | 1.5K | 1.00 | 27% | -0.05 |
| off-grid heat: free-heat tricks and DIY heaters | 162 | 1.7K | 1.13 | 33% | 787 | 6.3K | 1.17 | 37% | -0.04 |
| filters | 40 | 1.8K | 1.04 | 32% | 34 | 572 | 1.06 | 26% | -0.03 |
| replacement cost and quotes | 75 | 213 | 0.91 | 29% | 28 | 1.4K | 0.93 | 21% | -0.02 |
| ducts and vents | 129 | 532 | 1.09 | 32% | 33 | 2.8K | 1.08 | 24% | +0.01 |
| refrigerant | 77 | 1.9K | 0.96 | 19% | 14 | 1.9K | 1.68 | 50% | - |
| choosing a contractor | 38 | 1.5K | 0.97 | 37% | 4 | 28K | 1.03 | 0% | - |
| error codes and troubleshooting | 33 | 3.9K | 0.87 | 27% | 8 | 1.3K | 0.58 | 25% | - |
| evaporative coolers | 5 | 2.2K | 1.33 | 40% | 33 | 1.4K | 2.21 | 58% | - |
| smells and noises | 27 | 479 | 1.08 | 26% | 5 | 599 | 0.42 | 0% | - |
| off-grid heat: diesel, propane and kerosene heaters | 3 | 1.7K | 1.17 | 0% | 29 | 4.6K | 2.14 | 52% | - |
| AC: portable | 15 | 1.1K | 0.82 | 13% | 13 | 1.1K | 1.68 | 46% | - |
| condensate drain and water leaks | 20 | 1.9K | 1.03 | 30% | 4 | 7.6K | 2.17 | 50% | - |
| heating fuel and fuel choice | 4 | 5.2K | 0.80 | 0% | 14 | 4.2K | 1.60 | 50% | - |
| AC: window | 8 | 3.5K | 2.12 | 50% | 8 | 14K | 3.71 | 62% | - |
| general: no heat (equipment not named) | 9 | 3.5K | 1.10 | 11% | 6 | 2.7K | 1.49 | 17% | - |

## Split by channel type: faceless (incl. faceless persona) vs on camera

Types are readings (see Method for how many channels were typed and from where). Brand and AI-avatar channels and untyped channels are left out of this split. Faceless-persona videos are also counted in every map row and shown separately below. `*` after an n = one channel made 50%+ of that cell.

### all time

| Sub-niche | faceless n | faceless median views | faceless median multiple | faceless 2x+ | on camera n | on camera median views | on camera median multiple | on camera 2x+ | gap in median multiple (faceless minus on camera; both n >= 15) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| thermostats | 230 | 2K | 1.35 | 42% | 173 | 31K | 7.50 | 72% | -6.15 |
| smart thermostats | 98 | 17K | 5.97 | 70% | 71* | 2.1K | 1.42 | 39% | +4.55 |
| off-grid heat: free-heat tricks and DIY heaters | 1,156 | 7.3K | 1.58 | 45% | 123 | 44K | 5.54 | 72% | -3.96 |
| off-grid heat: DIY stove builds (cement, barrel, brick craft) | 388 | 90K | 6.03 | 67% | 21 | 37K | 2.52 | 57% | +3.51 |
| off-grid heat: diesel, propane and kerosene heaters | 70* | 25K | 5.27 | 63% | 41 | 10K | 2.38 | 54% | +2.89 |
| AC: window | 35 | 26K | 9.03 | 71% | 42 | 68K | 6.45 | 74% | +2.58 |
| AC: portable | 45 | 1.8K | 2.87 | 56% | 50 | 36K | 5.11 | 70% | -2.24 |
| oil heat | 92 | 10K | 3.52 | 60% | 37 | 6.1K | 1.97 | 49% | +1.55 |
| filters | 111 | 2.7K | 1.31 | 37% | 57 | 12K | 2.79 | 56% | -1.48 |
| choosing a contractor | 36 | 3.1K | 2.18 | 56% | 56 | 2.5K | 0.75 | 25% | +1.43 |
| carbon monoxide and gas safety | 22 | 826 | 0.70 | 27% | 27 | 3.2K | 1.89 | 44% | -1.19 |
| heat and power in an outage | 415 | 2.5K | 1.36 | 41% | 74 | 22K | 2.50 | 54% | -1.14 |
| furnaces | 313 | 2.4K | 1.93 | 49% | 233 | 3.4K | 2.91 | 56% | -0.98 |
| replacement cost and quotes | 60 | 318 | 0.80 | 20% | 73 | 4.6K | 1.66 | 44% | -0.86 |
| fans for cooling (ceiling, whole-house, box) | 112 | 5K | 1.84 | 46% | 39 | 12K | 2.69 | 59% | -0.85 |
| scams and upsells | 180 | 1.1K | 1.42 | 42% | 64 | 26K | 2.27 | 52% | -0.85 |
| mini-split | 174 | 9.6K | 3.41 | 61% | 226 | 16K | 2.68 | 59% | +0.73 |
| error codes and troubleshooting | 70 | 3K | 1.56 | 41% | 73* | 8.5K | 2.17 | 52% | -0.61 |
| AC: central | 738 | 2.9K | 2.00 | 50% | 425 | 3.3K | 1.48 | 39% | +0.52 |
| coils and condenser cleaning | 142 | 4.8K | 2.31 | 53% | 107 | 3.9K | 1.82 | 49% | +0.49 |
| general: HVAC, topic not named | 241 | 4.7K | 1.77 | 47% | 279 | 2.5K | 1.30 | 34% | +0.47 |
| brand verdicts | 655 | 518 | 2.35 | 53% | 279 | 16K | 2.73 | 58% | -0.38 |
| condensate drain and water leaks | 65 | 14K | 2.55 | 55% | 49 | 5.2K | 2.19 | 53% | +0.36 |
| energy bills | 488 | 881 | 1.07 | 34% | 183 | 11K | 1.42 | 36% | -0.35 |
| boilers, radiators and steam | 236 | 3.2K | 2.39 | 53% | 353 | 17K | 2.73 | 57% | -0.34 |
| heat pumps | 237 | 3.6K | 1.33 | 43% | 488 | 5.8K | 1.67 | 43% | -0.34 |
| refrigerant | 175 | 3.7K | 1.45 | 41% | 145 | 4.7K | 1.72 | 47% | -0.27 |
| indoor air and purifiers | 193 | 14K | 2.10 | 51% | 154 | 16K | 2.30 | 54% | -0.20 |
| off-grid heat: wood and pellet stoves, fireplaces | 280 | 5K | 1.86 | 48% | 437 | 28K | 2.04 | 51% | -0.18 |
| seasonal maintenance | 166 | 1.1K | 1.06 | 35% | 81 | 1.7K | 1.23 | 40% | -0.17 |
| general: heating (equipment not named) | 114 | 1.4K | 1.08 | 36% | 74 | 26K | 1.25 | 43% | -0.17 |
| ducts and vents | 231 | 3.4K | 2.14 | 51% | 182 | 8.2K | 2.02 | 51% | +0.12 |
| evaporative coolers | 115 | 13K | 3.50 | 70% | 17* | 3K | 3.62 | 53% | -0.12 |
| smells and noises | 65 | 3.7K | 1.76 | 48% | 59 | 3.9K | 1.88 | 49% | -0.12 |
| parts homeowners touch | 426 | 7.2K | 1.89 | 48% | 314 | 5.9K | 2.00 | 50% | -0.11 |
| general: no heat (equipment not named) | 22 | 4.6K | 1.42 | 41% | 24 | 2.6K | 1.32 | 29% | +0.10 |
| humidity and dehumidifiers | 159 | 3.6K | 1.59 | 45% | 129 | 9.1K | 1.49 | 40% | +0.10 |
| drafts, insulation and windows | 272 | 2.1K | 1.60 | 44% | 179 | 14K | 1.69 | 46% | -0.08 |
| space heaters (electric) | 101 | 2.7K | 1.37 | 41% | 75 | 11K | 1.31 | 44% | +0.06 |
| cooling without AC (tricks, DIY coolers) | 261 | 3.2K | 1.43 | 43% | 26 | 32K | 1.46 | 46% | -0.03 |
| buy or replace (sizing, repair vs replace, new system) | 81 | 1.3K | 1.46 | 38% | 126 | 13K | 1.48 | 43% | -0.02 |
| staying warm without heating (body, bed, clothes) | 93 | 967 | 0.93 | 27% | 8 | 14K | 1.04 | 25% | - |
| heating fuel and fuel choice | 28 | 5K | 1.36 | 36% | 10 | 8.4K | 1.54 | 40% | - |
| RV, van, tent and camping heat or cool | 21 | 4.3K | 0.90 | 38% | 8 | 6K | 0.94 | 25% | - |
| garage, shop and outbuildings | 14 | 550 | 1.11 | 29% | 8 | 408K | 4.12 | 75% | - |
| general: cooling (equipment not named) | 16 | 3.5K | 1.26 | 38% | 4 | 5.2K | 0.84 | 0% | - |

### last 12 months

| Sub-niche | faceless n | faceless median views | faceless median multiple | faceless 2x+ | on camera n | on camera median views | on camera median multiple | on camera 2x+ | gap in median multiple (faceless minus on camera; both n >= 15) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| off-grid heat: diesel, propane and kerosene heaters | 15 | 3.6K | 1.20 | 33% | 16* | 6.1K | 2.53 | 56% | -1.33 |
| furnaces | 109 | 827 | 1.00 | 28% | 49* | 702 | 1.69 | 41% | -0.69 |
| coils and condenser cleaning | 28 | 2.9K | 1.50 | 32% | 19 | 4.7K | 0.81 | 21% | +0.69 |
| error codes and troubleshooting | 16 | 1.1K | 0.65 | 19% | 20* | 4.2K | 1.24 | 35% | -0.59 |
| thermostats | 130 | 1.3K | 1.15 | 31% | 32 | 1.9K | 1.69 | 44% | -0.54 |
| oil heat | 30 | 3.2K | 1.08 | 30% | 15* | 514 | 0.55 | 27% | +0.53 |
| off-grid heat: wood and pellet stoves, fireplaces | 201 | 2K | 1.57 | 43% | 103 | 11K | 1.09 | 29% | +0.48 |
| smart thermostats | 28 | 672 | 1.52 | 43% | 46* | 1.4K | 1.08 | 30% | +0.44 |
| ducts and vents | 84 | 1.1K | 1.41 | 38% | 28 | 3.9K | 1.00 | 14% | +0.41 |
| off-grid heat: free-heat tricks and DIY heaters | 934 | 5K | 1.15 | 37% | 15 | 28K | 1.54 | 47% | -0.40 |
| heat pumps | 71 | 1.8K | 0.92 | 24% | 121 | 5.1K | 1.30 | 31% | -0.38 |
| drafts, insulation and windows | 202 | 1.2K | 1.39 | 39% | 30 | 7.3K | 1.06 | 33% | +0.33 |
| scams and upsells | 150 | 825 | 1.14 | 34% | 24 | 5.3K | 1.46 | 38% | -0.31 |
| boilers, radiators and steam | 56 | 258 | 0.83 | 25% | 89 | 4.9K | 1.11 | 21% | -0.28 |
| seasonal maintenance | 129 | 927 | 1.00 | 33% | 29 | 254 | 0.75 | 21% | +0.25 |
| replacement cost and quotes | 50 | 132 | 0.79 | 16% | 29 | 565 | 1.03 | 31% | -0.24 |
| refrigerant | 44 | 1.9K | 1.10 | 30% | 41 | 2.2K | 0.87 | 12% | +0.23 |
| mini-split | 26 | 2K | 1.34 | 46% | 58 | 8.6K | 1.12 | 40% | +0.22 |
| general: heating (equipment not named) | 88 | 888 | 0.80 | 26% | 19 | 23K | 0.62 | 21% | +0.18 |
| AC: central | 294 | 1.8K | 1.06 | 31% | 133 | 1.7K | 0.95 | 26% | +0.11 |
| brand verdicts | 380 | 369 | 1.38 | 41% | 84 | 5.8K | 1.48 | 39% | -0.10 |
| parts homeowners touch | 62 | 3.9K | 0.87 | 16% | 56 | 1.8K | 0.96 | 25% | -0.09 |
| humidity and dehumidifiers | 87 | 725 | 1.01 | 33% | 47 | 3.1K | 0.92 | 21% | +0.09 |
| general: HVAC, topic not named | 48 | 1000 | 1.07 | 38% | 67 | 1.7K | 1.00 | 22% | +0.07 |
| buy or replace (sizing, repair vs replace, new system) | 37 | 391 | 1.02 | 22% | 31 | 4.8K | 0.96 | 10% | +0.06 |
| space heaters (electric) | 64 | 1.3K | 0.96 | 28% | 19 | 6.8K | 1.00 | 26% | -0.04 |
| indoor air and purifiers | 41 | 572 | 0.86 | 29% | 26 | 6.5K | 0.83 | 27% | +0.03 |
| energy bills | 440 | 771 | 1.00 | 32% | 73 | 10K | 1.00 | 26% | +0.00 |
| heat and power in an outage | 377 | 2.1K | 1.28 | 39% | 13 | 4.7K | 0.75 | 15% | - |
| cooling without AC (tricks, DIY coolers) | 243 | 2.7K | 1.32 | 40% | 13 | 22K | 1.51 | 46% | - |
| staying warm without heating (body, bed, clothes) | 89 | 776 | 0.91 | 24% | 3 | 690 | 0.80 | 0% | - |
| off-grid heat: DIY stove builds (cement, barrel, brick craft) | 76 | 9.9K | 1.62 | 46% | 5 | 82K | 0.31 | 20% | - |
| fans for cooling (ceiling, whole-house, box) | 67 | 1.5K | 1.28 | 36% | 11 | 3.9K | 1.70 | 45% | - |
| filters | 60 | 598 | 1.08 | 32% | 12 | 3.2K | 1.12 | 25% | - |
| choosing a contractor | 25 | 1.1K | 1.25 | 48% | 14 | 2.1K | 0.73 | 14% | - |
| evaporative coolers | 33 | 1.8K | 2.42 | 64% | 5 | 292 | 0.78 | 0% | - |
| AC: portable | 22 | 779 | 1.04 | 27% | 6 | 8.2K | 0.98 | 33% | - |
| smells and noises | 17 | 517 | 1.10 | 18% | 10 | 2.2K | 0.83 | 10% | - |
| condensate drain and water leaks | 12 | 1.9K | 1.03 | 25% | 11 | 4.5K | 1.15 | 36% | - |
| heating fuel and fuel choice | 17 | 4.6K | 1.18 | 41% | 1 | 4.9K | 0.83 | 0% | - |
| AC: window | 13 | 2K | 2.43 | 54% | 3 | 33K | 12.82 | 67% | - |
| general: no heat (equipment not named) | 7 | 3K | 1.14 | 14% | 8 | 3.2K | 1.19 | 12% | - |

### Faceless persona only (all time and last 12 months)

| Sub-niche | persona n (all time) | channels | median views | median multiple | 2x+ | persona n (12 m) | median multiple (12 m) | 2x+ (12 m) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| energy bills | 195 | 77 | 537 | 0.98 | 28% | 194 | 0.98 | 28% |
| heat and power in an outage | 176 | 70 | 706 | 1.00 | 34% | 176 | 1.00 | 34% |
| off-grid heat: free-heat tricks and DIY heaters | 173 | 48 | 1.3K | 1.31 | 38% | 173 | 1.31 | 38% |
| scams and upsells | 97 | 32 | 1.1K | 1.19 | 35% | 97 | 1.19 | 35% |
| AC: central | 91 | 33 | 1.2K | 1.35 | 42% | 89 | 1.35 | 42% |
| off-grid heat: wood and pellet stoves, fireplaces | 84 | 24 | 2.8K | 1.79 | 45% | 84 | 1.79 | 45% |
| brand verdicts | 82 | 22 | 2K | 2.85 | 54% | 82 | 2.85 | 54% |
| seasonal maintenance | 81 | 48 | 768 | 0.99 | 30% | 80 | 0.99 | 30% |
| drafts, insulation and windows | 77 | 52 | 849 | 1.52 | 42% | 77 | 1.52 | 42% |
| cooling without AC (tricks, DIY coolers) | 68 | 27 | 1.9K | 1.60 | 43% | 68 | 1.60 | 43% |
| thermostats | 65 | 41 | 939 | 1.31 | 35% | 65 | 1.31 | 35% |
| furnaces | 61 | 32 | 702 | 1.02 | 32% | 60 | 1.02 | 32% |
| staying warm without heating (body, bed, clothes) | 50 | 37 | 700 | 0.91 | 28% | 50 | 0.91 | 28% |
| filters | 33 | 25 | 465 | 1.07 | 36% | 33 | 1.07 | 36% |
| general: HVAC, topic not named | 29 | 12 | 600 | 1.00 | 31% | 29 | 1.00 | 31% |
| replacement cost and quotes | 26 | 19 | 168 | 0.60 | 15% | 26 | 0.60 | 15% |
| space heaters (electric) | 25 | 20 | 1K | 1.29 | 40% | 25 | 1.29 | 40% |
| general: heating (equipment not named) | 24 | 21 | 802 | 0.76 | 21% | 24 | 0.76 | 21% |
| humidity and dehumidifiers | 22 | 18 | 610 | 1.00 | 27% | 22 | 1.00 | 27% |
| ducts and vents | 20 | 16 | 1.2K | 1.33 | 40% | 20 | 1.33 | 40% |
| heat pumps | 19 | 13 | 274 | 0.90 | 26% | 19 | 0.90 | 26% |
| fans for cooling (ceiling, whole-house, box) | 17 | 14 | 520 | 0.94 | 29% | 17 | 0.94 | 29% |
| refrigerant | 13 | 10 | 609 | 1.02 | 31% | 13 | 1.02 | 31% |
| buy or replace (sizing, repair vs replace, new system) | 13 | 11 | 221 | 1.27 | 8% | 13 | 1.27 | 8% |
| choosing a contractor | 12 | 9 | 3.1K | 1.97 | 50% | 12 | 1.97 | 50% |
| boilers, radiators and steam | 10 | 9 | 311 | 0.82 | 30% | 10 | 0.82 | 30% |
| coils and condenser cleaning | 9 | 8 | 1K | 2.33 | 56% | 9 | 2.33 | 56% |
| parts homeowners touch | 9 | 5 | 81K | 0.85 | 25% | 4 | 0.85 | 25% |
| off-grid heat: diesel, propane and kerosene heaters | 7 | 7 | 1.7K | 1.20 | 29% | 7 | 1.20 | 29% |
| AC: portable | 6 | 3 | 102 | 0.53 | 17% | 6 | 0.53 | 17% |
| condensate drain and water leaks | 5 | 5 | 421 | 1.58 | 20% | 5 | 1.58 | 20% |
| garage, shop and outbuildings | 5 | 4 | 413 | 1.34 | 20% | 5 | 1.34 | 20% |
| indoor air and purifiers | 5 | 4 | 2.5K | 1.56 | 20% | 5 | 1.56 | 20% |
| smart thermostats | 4 | 4 | 1.6K | 5.09 | 75% | 4 | 5.09 | 75% |
| carbon monoxide and gas safety | 4 | 4 | 416 | 0.84 | 0% | 4 | 0.84 | 0% |
| error codes and troubleshooting | 4 | 4 | 2.5K | 1.42 | 50% | 4 | 1.42 | 50% |
| smells and noises | 3 | 3 | 642 | 1.27 | 0% | 3 | 1.27 | 0% |
| off-grid heat: DIY stove builds (cement, barrel, brick craft) | 3 | 3 | 1K | 2.24 | 67% | 3 | 2.24 | 67% |
| heating fuel and fuel choice | 3 | 3 | 1.9K | 2.03 | 67% | 3 | 2.03 | 67% |
| AC: window | 2 | 2 | 10K | 20.47 | 50% | 2 | 20.47 | 50% |
| mini-split | 2 | 2 | 2K | 10.46 | 50% | 2 | 10.46 | 50% |
| oil heat | 2 | 2 | 964 | 1.91 | 50% | 2 | 1.91 | 50% |
| RV, van, tent and camping heat or cool | 1 | 1 | 1.2K | 0.75 | 0% | 1 | 0.75 | 0% |
| general: cooling (equipment not named) | 1 | 1 | 136 | 1.48 | 0% | 1 | 1.48 | 0% |
| general: no heat (equipment not named) | 1 | 1 | 8.5K | 0.57 | 0% | 1 | 0.57 | 0% |

## Tier D contrast (trade and company channels, all time)

Not part of the map; shown so the reader can see what the trade side makes. Rows with n >= 15.

| # | Sub-niche (reading) | labels.md parent | n videos | channels | median views | median multiple (n with multiple) | share at 2x+ | biggest channel's share of n | faceless-persona videos |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| - | thermostats | thermostats | 179 | 64 | 14K | 4.67 (177) | 65% | 6% | 0 |
| - | drafts, insulation and windows | drafts, insulation and air sealing | 284 | 51 | 7K | 3.95 (284) | 66% | 55% | 0 |
| - | trade: technical training | trade-facing | 939 | 109 | 8.8K | 3.12 (939) | 59% | 12% | 0 |
| - | furnaces | furnaces | 193 | 60 | 8K | 2.90 (193) | 56% | 7% | 0 |
| - | off-grid heat: wood and pellet stoves, fireplaces | alternative and supplemental heat (off-grid heat) | 190 | 16 | 15K | 2.76 (190) | 59% | 26% | 0 |
| - | brand verdicts | brand verdicts | 140 | 66 | 9.5K | 2.65 (140) | 55% | 7% | 0 |
| - | mini-split | mini-split | 317 | 66 | 7.3K | 2.64 (317) | 56% | 10% | 0 |
| - | oil heat | boilers and old-house heat | 74 | 20 | 14K | 2.55 (74) | 59% | 24% | 0 |
| - | boilers, radiators and steam | boilers and old-house heat | 908 | 75 | 7.8K | 2.44 (908) | 54% | 8% | 0 |
| - | general: HVAC basics and how it works (general) | NEW (not in labels.md) | 68 | 29 | 5.6K | 2.34 (68) | 54% | 15% | 0 |
| - | heat and power in an outage | heat and power in an outage | 30 | 19 | 14K | 2.32 (30) | 53% | 10% | 0 |
| - | condensate drain and water leaks | AC: central | 76 | 37 | 8.8K | 2.27 (76) | 54% | 8% | 0 |
| - | smart thermostats | thermostats | 76 | 27 | 20K | 2.17 (76) | 55% | 17% | 0 |
| - | ducts and vents | ducts and vents | 299 | 95 | 5.1K | 2.04 (298) | 50% | 6% | 0 |
| - | humidity and dehumidifiers | humidity, ventilation and indoor air | 141 | 41 | 4.5K | 2.04 (141) | 51% | 10% | 0 |
| - | parts homeowners touch | parts homeowners touch | 648 | 93 | 4.8K | 2.01 (648) | 50% | 9% | 0 |
| - | scams and upsells | buying and replacing a system | 45 | 26 | 3.2K | 2.00 (44) | 52% | 9% | 0 |
| - | space heaters (electric) | alternative and supplemental heat (off-grid heat) | 50 | 20 | 17K | 1.97 (50) | 50% | 36% | 0 |
| - | AC: central | AC: central | 692 | 90 | 5.1K | 1.92 (692) | 50% | 10% | 0 |
| - | heat pumps | heat pumps | 465 | 85 | 5.5K | 1.87 (465) | 48% | 7% | 0 |
| - | replacement cost and quotes | buying and replacing a system | 117 | 40 | 1.2K | 1.83 (117) | 49% | 11% | 0 |
| - | seasonal maintenance | seasonal maintenance | 68 | 41 | 2.4K | 1.77 (68) | 44% | 7% | 0 |
| - | coils and condenser cleaning | AC: central | 150 | 58 | 5.5K | 1.69 (150) | 43% | 8% | 0 |
| - | buy or replace (sizing, repair vs replace, new system) | buying and replacing a system | 100 | 60 | 5.1K | 1.67 (100) | 46% | 5% | 0 |
| - | smells and noises | NEW (not in labels.md) | 60 | 33 | 7.6K | 1.65 (60) | 43% | 10% | 0 |
| - | fans for cooling (ceiling, whole-house, box) | NEW (not in labels.md) | 90 | 40 | 3.2K | 1.62 (90) | 43% | 23% | 0 |
| - | AC: window | AC: window | 23 | 8 | 4K | 1.57 (23) | 35% | 39% | 0 |
| - | refrigerant | AC: central | 341 | 76 | 4.2K | 1.56 (341) | 43% | 9% | 0 |
| - | filters | filters | 61 | 39 | 2.9K | 1.55 (61) | 39% | 8% | 0 |
| - | trade: commercial and refrigeration | trade-facing | 914 | 82 | 3.9K | 1.46 (914) | 41% | 15% | 0 |
| - | error codes and troubleshooting | NEW (not in labels.md) | 128 | 50 | 3K | 1.46 (128) | 43% | 7% | 0 |
| - | energy bills | energy bills | 73 | 44 | 9K | 1.44 (73) | 44% | 12% | 0 |
| - | indoor air and purifiers | humidity, ventilation and indoor air | 118 | 47 | 3.7K | 1.38 (118) | 42% | 9% | 0 |
| - | HVAC, not mapped | not mapped | 62 | 36 | 1.2K | 1.38 (62) | 40% | 18% | 0 |
| - | general: no heat (equipment not named) (general) | NEW (not in labels.md) | 23 | 11 | 4.8K | 1.37 (23) | 39% | 17% | 0 |
| - | trade: careers, business and tech life | trade-facing | 1,504 | 108 | 1.1K | 1.36 (1504) | 39% | 11% | 0 |
| - | carbon monoxide and gas safety | humidity, ventilation and indoor air | 39 | 28 | 1.7K | 1.36 (39) | 38% | 8% | 0 |
| - | choosing a contractor | buying and replacing a system | 117 | 38 | 739 | 1.35 (117) | 44% | 14% | 0 |
| - | general: HVAC, topic not named (general) | NEW (not in labels.md) | 853 | 113 | 1.5K | 1.31 (853) | 39% | 6% | 0 |
| - | general: heating (equipment not named) (general) | NEW (not in labels.md) | 116 | 38 | 6K | 1.17 (116) | 34% | 17% | 0 |
| - | heating fuel and fuel choice | heating fuel and fuel choice | 32 | 20 | 4K | 1.03 (32) | 38% | 12% | 0 |
| - | AC: portable | AC: portable | 17 | 10 | 4.5K | 0.89 (17) | 24% | 24% | 0 |

## Per sub-niche: top channels, biggest videos, faceless-persona count (tiers A-C, all time)

Biggest = by tab views (rounded). Multiple = views / that channel's baseline. Sorted by n.

### AC: central (AC: central; scope home)

n 1,300 videos, 219 channels; last 12 months n 465. Faceless-persona videos: 91. Top 3 channels by videos: Air Conditioners Exposed (@airconditionersexposed, tier A) 105; Drewdriskle (@Drewdriskle, tier A) 55; Mitch Attwood (@maracservices, tier A) 49.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Thermoelectric cooling: it's not great." | Technology Connections | 6.3M | 3.41 | 2y ago | `CnMRePtHMZY` |
| 2 | "#1 Problem & Quick Fix with Central Air Conditioning Not Cooling" | Silver Cymbal | 4.3M | 53.42 | 8y ago | `_b6p0fkWhCY` |
| 3 | "AC Not Turning on or Working? Try THESE Fixes (Works on Most Units)" | Word of Advice TV | 3.6M | 276.92 | 8y ago | `wzAA4dlp_70` |
| 4 | "Personal "air conditioners" aren't what they seem" | Technology Connections | 3.2M | 1.73 | 6y ago | `2horH-IeurA` |
| 5 | "Air Conditioner Wont Turn On - Here is The MOST Common Fix" | Word of Advice TV | 2.8M | 215.38 | 9y ago | `C82HvbvP08E` |

### off-grid heat: free-heat tricks and DIY heaters (alternative and supplemental heat (off-grid heat); scope home)

n 1,283 videos, 156 channels; last 12 months n 949. Faceless-persona videos: 173. Top 3 channels by videos: Creative DIY365 (@CreativeDIY365USA, tier C) 148; Creative inventions LMTN (@lmtn, tier C) 113; Tips Clever (@TipsCleverUSA, tier C) 104.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Millions of people do not know this knowledge! 3 in 1 waste oil heater! Warm for winter 2024" | Creative inventions LMTN | 14M | 2641.51 | 1y ago | `UawMGmg87ho` |
| 2 | "UNLIMITED Heat For Your Home / NO ELECTRIC NEEDED" | Zen Garden Oasis | 12M | 260.87 | 1y ago | `7LV5wY-iM34` |
| 3 | "Homemade TIN CAN Rocket Stove - DIY Rocket Stove - Awesome Stove! - EASY instructions!" | desertsun02 | 10M | 1398.60 | 13y ago | `gQyU4lokVe4` |
| 4 | "waste oil heating stove mini 3 in 1 ! Millions of people do not know this knowledge" | Creative inventions LMTN | 7.6M | 1433.96 | 1y ago | `B6jvvZkD3P0` |
| 5 | "Millions Don’t Know That Waste Oil Is a Gold Mine! DIY 3-in-1 Heating Stove" | Creative inventions LMTN | 7.6M | 1433.96 | 1y ago | `ZVlv3r1KQyo` |

### brand verdicts (brand verdicts; scope home)

n 983 videos, 175 channels; last 12 months n 477. Faceless-persona videos: 82. Top 3 channels by videos: TempTrends (@temptrends60, tier C) 175; Air Conditioner Lab (@AirConditionerLab, tier A) 83; Homey Vibe (@homeyvibe1, tier A) 51.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Top 9 outstanding videos about wood stoves made from red bricks and cement" | Creative Cement | 6.5M | 361.11 | 4y ago | `GifU1UT34Yw` |
| 2 | "NO WELDING ! The best USED OIL STOVE 2022 / Made from Cement, Blue Flame and Easily at home" | Creative inventions LMTN | 5.9M | 1113.21 | 4y ago | `bPZ2yhHm0ac` |
| 3 | "NO WELDING ! The best USED OIL STOVE 2023 / Made from Cement, Blue Flame and Easily at home" | Creative inventions LMTN | 2.8M | 528.30 | 3y ago | `NRIxYmK5UxI` |
| 4 | "Furnace Troubleshooting - Top 10 Furnace Problems" | Word of Advice TV | 2.2M | 169.23 | 7y ago | `dPXM8TFMQGw` |
| 5 | "Top 5 Furnace Problems and How to Fix Them" | Word of Advice TV | 2.1M | 161.54 | 6y ago | `T4IWtKy--Vk` |

### heat pumps (heat pumps; scope home)

n 953 videos, 137 channels; last 12 months n 287. Faceless-persona videos: 19. Top 3 channels by videos: Renewable Heating Hub (@RenewableHeatingHub, tier A) 96; The Thought Provocateur (@thethoughtprovocateur, tier A) 64; Hartzell's Heat & Air (@hartzellsheatair6003, tier A) 57.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Heat Pumps: the Future of Home Heating" | Technology Connections | 4.8M | 2.59 | 5y ago | `7J52mDjZzto` |
| 2 | "This is Why Heat Pumps May NOT Be The Future" | Skill Builder | 2.5M | 51.02 | 5y ago | `GhAKMAcmJFg` |
| 3 | "Why Heat Pumps are Immensely Important Right Now" | Technology Connections | 1.3M | 0.70 | 4y ago | `MFEHFsO-XSI` |
| 4 | "Heat Pumps are Not Hard: Here's what it will take to start pumping" | Technology Connections | 1.1M | 0.59 | 4y ago | `43XKfuptnik` |
| 5 | "Ground Source / Geothermal Heat Pumps and Other Info" | Technology Connections | 1.1M | 0.59 | 5y ago | `7zrx-b2sLUs` |

### parts homeowners touch (parts homeowners touch; scope home)

n 798 videos, 138 channels; last 12 months n 122. Faceless-persona videos: 9. Top 3 channels by videos: Anti DIY HVAC (@TedCookHVAC, tier A) 46; The HVAC Hacker (@thehvachacker, tier A) 39; OnemanHVAC (@Onemanhvac, tier A) 35.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Foam Board vs Spray Foam… Insulating our steel building/garage / Tips and Tricks" | Great American Northern Garage | 3M | 103.45 | 3y ago | `7C_ED3NDJLQ` |
| 2 | "How To Check & Replace An Air Conditioner Capacitor" | The DIY HVAC Guy | 2.3M | 55.42 | 3y ago | `FQisFmMtAis` |
| 3 | "Was Quoted $400. I Fixed It For $11.72! AC Capacitor Testing and Replacement" | How To Home | 2.1M | 10.50 | 3y ago | `i8nDBZo6XyE` |
| 4 | "Contactors: how we power the big stuff" | Technology Connections | 1.6M | 0.86 | 3y ago | `VsNHrAzx5_w` |
| 5 | "Furnace Not Igniting - How to Check and Replace Ignitor" | Word of Advice TV | 1.3M | 100.00 | 7y ago | `1bRsFAMgZRQ` |

### off-grid heat: wood and pellet stoves, fireplaces (alternative and supplemental heat (off-grid heat); scope home)

n 723 videos, 143 channels; last 12 months n 307. Faceless-persona videos: 84. Top 3 channels by videos: Back 40 Firewood (@Back40Firewood, tier B) 112; Hometown Acres (@HometownAcres, tier B) 68; Ryan’s Fireplace Diaries (@RyansFireplaceDiaries, tier A) 51.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Secretly, use water H2O to burn, wood stove" | Creative Cement Ideas | 4.1M | 68.33 | 4y ago | `Mk-IgKJMCFk` |
| 2 | "Burning Pine Cones in a Fireplace… The Results Are INSANE!" | Ryan’s Fireplace Diaries | 3.6M | 133.33 | 1y ago | `fRP0tssWeFc` |
| 3 | "3 ways I improved wood stove heating." | Double M Innovations | 3.3M | 1404.26 | 5y ago | `iGZWx0gwRCo` |
| 4 | "Amazing 4 in 1 wood stove. Would you believe it" | Creative Project | 2.9M | 483.33 | 3y ago | `ZyM53Hk5I-s` |
| 5 | "Stove that can melt aluminum at 1000 degrees C / Wood mulch stove" | Creative Project | 2.4M | 400.00 | 5y ago | `AInBNiPPi54` |

### energy bills (energy bills; scope home)

n 717 videos, 230 channels; last 12 months n 532. Faceless-persona videos: 195. Top 3 channels by videos: Secret Sparks (@SecretSparks-v8d, tier B) 31; Jonathan Tracey (@JonathanTracey, tier C) 31; Nicolas Raimo (@NicolasRaimo, tier C) 20.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Can This Device Actually Lower Your Electric Bill By 30%??" | The DIY HVAC Guy | 2.6M | 62.65 | 3y ago | `SWc0StyZiJs` |
| 2 | "The DIY Heating System That Destroyed Our Heating Bills" | Stefano Creatini | 2.5M | 641.03 | 1y ago | `0YZCQ9SuQVA` |
| 3 | "£0.03 per kWh heater modification - Top facts & lies on diesel heaters - waste veg oil burn success" | Joshua De Lisle | 2M | 10.96 | 3y ago | `4tiSEGO6pYI` |
| 4 | "Genius AC Upgrade That Makes Air Colder And Bills Lower!" | How To Home | 1.7M | 8.50 | 5mo ago | `gQjotD-B0OU` |
| 5 | "Just one copper pipe and you won’t have to pay electricity bills anymore! Free energy at home 😱" | Creative inventions LMTN | 1.3M | 245.28 | 11d ago | `SWXheAemnXI` |

### boilers, radiators and steam (boilers and old-house heat; scope home)

n 689 videos, 119 channels; last 12 months n 164. Faceless-persona videos: 10. Top 3 channels by videos: Silent Steam Team (@gordonschweizer5154, tier A) 87; Birmingham Boiler Fix (@Birminghamboilerfix, tier A) 54; Mark Ballard LTD, Professional Heating Engineer (@MarkBallardLTDHeatingEngineer, tier A) 44.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "How to Fix One Radiator Not Working - Plumbing Tips" | plumberparts | 2.4M | 80.00 | 15y ago | `wqku_Rc_YuI` |
| 2 | "BOILER KEEPS LOSING PRESSURE - WHY AND HOW TO FIX - Plumbing tips" | plumberparts | 2.2M | 73.33 | 10y ago | `4meZgMAUecw` |
| 3 | "Radiator NOT Heating Up? Expert DIY Fixes" | Skill Builder | 1.2M | 24.49 | 8y ago | `UmfKzbsQxKE` |
| 4 | "Get More Heat From Your Radiators ~ System Balance" | Skill Builder | 1.1M | 22.45 | 6y ago | `pol8IlkfAZA` |
| 5 | "Replace a Leaking Radiator Valve with Out Draining the System. Professional Step by Step Guide" | Mark Ballard LTD, Professional Heating Engineer | 1.1M | 275.00 | 5y ago | `mjsPZirB9Cg` |

### general: HVAC, topic not named (NEW (not in labels.md); scope general)

n 623 videos, 105 channels; last 12 months n 135. Faceless-persona videos: 29. Top 3 channels by videos: John Israel HVAC (@johnisraelhvac2019, tier A) 49; HVAC Guide for Homeowners (@NewHVACGuide, tier A) 46; RHODES - Cosmic Cooling (@CosmicCooling, tier A) 33.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "HVAC Startup Compilation - Every Startup I Caught in 2022" | Andrew Bdish | 1.2M | 307.69 | 3y ago | `iE9ISgh0sj8` |
| 2 | "How to perform an HVAC service call from start to finish" | T&N Services LLC. | 1M | 210.53 | 12y ago | `aTcNK-VQJP4` |
| 3 | "How to Find a Short (HVAC)" | Word of Advice TV | 900K | 69.23 | 7y ago | `4e4wsruGS0s` |
| 4 | "It's Hard to Stop  A Trane but not for snakes 2" | Anti DIY HVAC | 349K | 26.85 | 6y ago | `1ikZlbYVnfM` |
| 5 | "I Should’ve Known BETTER…/ HVAC Install" | Quality HVACR | 343K | 28.58 | 4y ago | `ypgiHAg_TWY` |

### furnaces (furnaces; scope home)

n 615 videos, 142 channels; last 12 months n 169. Faceless-persona videos: 61. Top 3 channels by videos: Drewdriskle (@Drewdriskle, tier A) 61; Advantage Heating & Cooling (@AdvantageHVAC, tier A) 57; Michigan Heating Guy (@MiHeatingGuy, tier B) 28.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "The Most Common Reason Why A Gas Furnace Won't Turn On" | Everyday Home Repairs | 2.7M | 7.54 | 4y ago | `sRvH-io-ZtA` |
| 2 | "Furnace Not Working - The Most Common Fix" | Word of Advice TV | 2.5M | 192.31 | 8y ago | `3Jonl_TLkpE` |
| 3 | "Yearly Furnace Cleaning And Maintenance Pro Tips" | Everyday Home Repairs | 2.1M | 5.87 | 3y ago | `--A2I2s7aNw` |
| 4 | "Furnace Not Blowing Hot Air - Easy Fix" | Word of Advice TV | 1.8M | 138.46 | 7y ago | `pJzP1jzYPqg` |
| 5 | "Forced-air Furnaces: The What, Why, and How" | Technology Connections | 1.7M | 0.92 | 6y ago | `lBVvnDfW2Xo` |

### trade: careers, business and tech life (trade-facing; scope trade)

n 546 videos, 81 channels; last 12 months n 137. Faceless-persona videos: 2. Top 3 channels by videos: OnemanHVAC (@Onemanhvac, tier A) 125; HVAC Life with Alex (@hvaclifewithalex4051, tier A) 73; Shorty HVAC (@ShortyHVAC, tier A) 46.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "So you want to be a HVAC technician? / 10 things you should know before you decide 🔥❄️" | Yung HVAC | 723K | 119.50 | 6y ago | `xxwGbRFD90U` |
| 2 | "HVAC Owner Reveals the Best AC System for your House - 2021" | Fox Family Heating and Air Conditioning | 318K | 13.83 | 5y ago | `Y2AIZduylTU` |
| 3 | "Which HVAC Brand Do I Prefer?? / HVAC Business Owner" | Quality HVACR | 273K | 22.75 | 5y ago | `y7QT8P3iY4k` |
| 4 | "Should YOU Choose HVAC As A Career?? My Honest Opinion…" | Quality HVACR | 253K | 21.08 | 4y ago | `J70rN-Q5a0I` |
| 5 | "What is the Starting Salary for an HVAC Technician" | Fox Family Heating and Air Conditioning | 224K | 9.74 | 7y ago | `74l6gCMpkxs` |

### ducts and vents (ducts and vents; scope home)

n 512 videos, 154 channels; last 12 months n 162. Faceless-persona videos: 20. Top 3 channels by videos: Bright Air Duct Cleaning - Florida (@BrightAirDuctCleaningFL, tier A) 37; Home Performance (@HomePerformance, tier A) 24; Talyn875 (@TALYN875, tier A) 17.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "3 PROVEN Methods To Getting Colder Air From HVAC Vents." | The DIY HVAC Guy | 1.9M | 45.78 | 2y ago | `hl3u2Zd7U4E` |
| 2 | "RADIATORS EXPLAINED How to fix balance bleed panel radiator How radiators work flow & return valves" | How2D2 | 1.6M | 16.00 | 6y ago | `PAo6yG89vyM` |
| 3 | "DIY - Clean Your Air Heat Vents" | Dave Wirth | 1.5M | 103.45 | 12y ago | `QdKvKpwGOkk` |
| 4 | "Installing Jumper Ducts to Make Bedrooms More Comfortable" | Dr. Energy Saver | 1.4M | 11.48 | 14y ago | `I0LxBLJGO24` |
| 5 | "Furnace Blower Not Working - How to Check It" | Word of Advice TV | 1.2M | 92.31 | 8y ago | `JSgLGTAbDF8` |

### drafts, insulation and windows (drafts, insulation and air sealing; scope home)

n 507 videos, 207 channels; last 12 months n 240. Faceless-persona videos: 77. Top 3 channels by videos: Home Comfort Guy (@homeairleakagetest, tier A) 30; AEPowerHouseTV (@AEPowerHouseTV, tier B) 17; Dr. Energy Saver (@DrEnergySaver, tier A) 14.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "DIY wood stove - Ideas to make a wood stove from cement roof sheets" | Garden Design | 14M | 1866.67 | 5y ago | `7QOIJhdaxiw` |
| 2 | "How To Fix A Sunken Sidewalk With Spray Foam" | Everyday Home Repairs | 5.1M | 14.25 | 4y ago | `AL1Xrd8IScY` |
| 3 | "STOP Throwing Away Half-Used Dried-Up Caulk Tubes! How To Fix It To Last Forever!" | Fix This House | 5M | 384.62 | 3y ago | `l_B2UfN8-G8` |
| 4 | "The Spray Foam Insulation Problem Nobody's Talking About" | Skill Builder | 3M | 61.22 | 4y ago | `jYNufQVIFfA` |
| 5 | "Attic Insulation Done Wrong… and How to Do It Right!" | Dr. Energy Saver | 2.1M | 17.21 | 11y ago | `fB6CbJsb1FM` |

### mini-split (mini-split; scope home)

n 506 videos, 110 channels; last 12 months n 96. Faceless-persona videos: 2. Top 3 channels by videos: Forever Tech English (@forevertechenglish, tier B) 33; Ductless Plus HVAC (@ductlessplushvac, tier A) 32; Taddy Digest (@taddydigest, tier A) 32.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "AIR CONDITIONER DETAIL INSTALL /SPLIT DUCTLESS AC HEATING INVERTER,MINI PUMP SYSTEM SETUP,DIY HOW TO" | CarlTheLandscapeGuy | 7.8M | 200.00 | 7y ago | `2RDfAkmDId0` |
| 2 | "DIY Mini Split Install - All the Things Nobody Shows You" | LRN2DIY | 3.2M | 91.43 | 4y ago | `2mKwCmaR5Qg` |
| 3 | "Install your own AIR CONDITIONING in 4 HOURS!  DIY Mini Split MR COOL" | Silver Cymbal | 3M | 37.27 | 5y ago | `Wejop_Rjpv0` |
| 4 | "DIY Mini Split Install: 3 Regrets After 1 Year of Use" | LRN2DIY | 2.3M | 65.71 | 3y ago | `5dCCntGj1wM` |
| 5 | "How to Clean Your Mini Split AC Condenser - Make it Cold Again" | Silver Cymbal | 1.8M | 22.36 | 3y ago | `DSNUyxZtrmo` |

### heat and power in an outage (heat and power in an outage; scope home)

n 499 videos, 177 channels; last 12 months n 394. Faceless-persona videos: 176. Top 3 channels by videos: Unknowns Lab 101 (@UnknownsLab101, tier B) 50; The DIY HVAC Guy (@diyhvacguy, tier A) 17; Del Rasmussen (@TheDelRasmussen, tier C) 12.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Keep Your Family Warm During A Power Outage By Installing This $5 Part" | The DIY HVAC Guy | 4.2M | 101.20 | 3y ago | `y07w1hiKIrI` |
| 2 | "This Could Keep Your Family Warm During An Emergency Power Outage." | The DIY HVAC Guy | 2.7M | 65.06 | 3y ago | `1JNuovFpCpQ` |
| 3 | "No Power, No Gas! DIY 3-in-1 Waste Oil Heater from Oil Filter – Hidden Free Energy for Winter 2025🔥" | Unknowns Lab 101 | 1.4M | 184.21 | 11mo ago | `zGsy6s2qkr8` |
| 4 | "6 Lifesaving Tips to Keep Warm During a Winter Power Outage" | The Provident Prepper | 1.2M | 109.09 | 6y ago | `erq-QuCN0G0` |
| 5 | "No Power in Winter — Your Heater Won't Save You, This Will" | Sketchsurvive | 1M | 6191.95 | 8mo ago | `_hCqYLr74a4` |

### trade: technical training (trade-facing; scope trade)

n 488 videos, 93 channels; last 12 months n 44. Faceless-persona videos: 5. Top 3 channels by videos: HVAC Training 101 (@HVACTraining101, tier A) 165; Talyn875 (@TALYN875, tier A) 28; Home Performance (@HomePerformance, tier A) 16.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Brazing Is For Cavemen. THIS Is The Future Of HVAC Copper Connections. -RLS Crimping Tool-" | The DIY HVAC Guy | 1.3M | 31.33 | 3y ago | `zTVWVE1H0iE` |
| 2 | "Furnace Troubleshooting Step by Step with Multi Meter." | Sam | 1M | 57.14 | 7y ago | `dJzNrw6L_YU` |
| 3 | "Budget Mini Split Installation for Beginners! w/ Vacuum Pump and Gauges" | DIY Solar Power with Will Prowse | 841K | 5.04 | 3y ago | `5trJX6Ef1iI` |
| 4 | "Soldering An HVAC Line Set Using Staybrite 8.  STRONGER THAN BRAZING!" | The DIY HVAC Guy | 762K | 18.36 | 3y ago | `3dbBmMgm7lk` |
| 5 | "How to Test For BAD Compressor. Ohms Test With MultiMeter" | Sam | 663K | 37.89 | 8y ago | `bKnxKsXIMRk` |

### thermostats (thermostats; scope home)

n 431 videos, 170 channels; last 12 months n 166. Faceless-persona videos: 65. Top 3 channels by videos: Hotrods & Homestead (@ModernHotrodsNH, tier A) 35; Mark Ballard LTD, Professional Heating Engineer (@MarkBallardLTDHeatingEngineer, tier A) 19; HVAC OTJ (@hvacotj, tier A) 15.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Honeywell Thermostat Not Working? Try This" | The Amateur's Amateur-If I Can Do It You Can Do it | 3.4M | 629.63 | 7y ago | `X5oRPvYBpvs` |
| 2 | "Thermostat Wiring Made Simple" | David Jones | 2.4M | 35.04 | 13y ago | `iXquA-LiI5w` |
| 3 | "This $300 Tunnel Keeps Your Home 55°F Forever. Why Is It Banned in the U.S." | Construction Odyssey with Eddie | 2.2M | 785.71 | 6mo ago | `XJzM-fcrFck` |
| 4 | "Thermostat Wiring" | David Jones | 2.2M | 32.12 | 9y ago | `FmaDeTcgkUg` |
| 5 | "How to Use Your Honeywell T4 Pro Thermostat" | Sierra LLC Air Conditioning & Plumbing | 1.6M | 25.81 | 5y ago | `ACoidkKTI4k` |

### off-grid heat: DIY stove builds (cement, barrel, brick craft) (alternative and supplemental heat (off-grid heat); scope home)

n 409 videos, 37 channels; last 12 months n 81. Faceless-persona videos: 3. Top 3 channels by videos: Garden Design (@GardenDesign89, tier B) 88; Creative Cement (@CreativeCement, tier B) 62; Creative Project (@Creativeproject2020, tier C) 45.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Creative Firewood Stove From Plastic Chairs - Self-Made Ideas From Cement" | Creative Craft | 84M | 593.64 | 5y ago | `QzU2i-XdGXg` |
| 2 | "The idea of making wood stove from a sink and cement" | Creative Cement | 64M | 3555.56 | 5y ago | `vs2mb72A6lc` |
| 3 | "How to make a 2 in 1 wood stove from beautiful red bricks" | Creative Cement | 53M | 2944.44 | 5y ago | `DuBJ_X9C0l4` |
| 4 | "Outdoor multifunctional wood stove _ Creative ideas from cement and non iron barrels" | Creative Project | 35M | 5833.33 | 5y ago | `l8Dly23Ey3I` |
| 5 | "DIY wood stove - Ideas to make a wood stove from old plastic bottles" | Garden Design | 33M | 4400.00 | 5y ago | `tJmzTLlQpLw` |

### indoor air and purifiers (humidity, ventilation and indoor air; scope home)

n 383 videos, 121 channels; last 12 months n 75. Faceless-persona videos: 5. Top 3 channels by videos: Air Purifier First (@AirPurifierFirst, tier B) 70; HouseFresh (@HouseFresh, tier A) 37; Consumer Analysis (@consumer-analysis, tier B) 22.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Great, the idea of making smoke free wood stoves from cement and plastic baskets" | Creative Cement | 15M | 833.33 | 5y ago | `zsdYDf4Iib4` |
| 2 | "How to make smoke free wood stove   beautiful saving firewood" | Creative Cement | 5.8M | 322.22 | 5y ago | `YQ1AVYdBpic` |
| 3 | "Building firewood stoves no smoke 3 in 1simple \ Idea wood stove clever" | Garden Design | 4.2M | 560.00 | 5y ago | `0OLbZs0rLmw` |
| 4 | "DIY firewood stove _ Save firewood without smoke" | Creative Project | 3.9M | 650.00 | 6y ago | `i2jCL0Toev0` |
| 5 | "How To Replace And Install A Bathroom Exhaust Fan To A Quiet Motion Sensor Exhaust Fan! DIY Tutorial" | Fix This House | 3.2M | 246.15 | 5y ago | `NzjmnIv89Ls` |

### humidity and dehumidifiers (humidity, ventilation and indoor air; scope home)

n 368 videos, 131 channels; last 12 months n 147. Faceless-persona videos: 22. Top 3 channels by videos: Crawl Space Ninja (@CrawlSpaceNinja, tier A) 61; Air Conditioner Lab (@AirConditionerLab, tier A) 12; Home Performance (@HomePerformance, tier A) 12.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "DIY - Making Firewood Stoves From Trash Can Mold" | Creative Craft | 7.6M | 53.71 | 5y ago | `RB02-QBhd4Q` |
| 2 | "The idea of making firewood stoves from cement and clay with plastic bucket molds" | Creative Cement | 5.1M | 283.33 | 5y ago | `n6OZgAKUveI` |
| 3 | "Humidifiers: Simpler is better?" | Technology Connections | 3.4M | 1.84 | 5y ago | `oHeehYYgl28` |
| 4 | "Dehumidifiers are confusing. Here's why." | Technology Connections | 3.3M | 1.78 | 1y ago | `j_QfX0SYCE8` |
| 5 | "How To Make A 2-in-1 Firewood Stove From A Plastic Mold - Beautiful and Easy" | Creative Craft | 3.2M | 22.61 | 5y ago | `H3sIVa5VWk8` |

### refrigerant (AC: central; scope home)

n 357 videos, 103 channels; last 12 months n 91. Faceless-persona videos: 13. Top 3 channels by videos: The HVAC Hacker (@thehvachacker, tier A) 17; Jeff’s HVAC Adventures (@JeffsHVACAdventures, tier A) 17; Mitch Attwood (@maracservices, tier A) 15.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "How to Check AC Freon Level" | Word of Advice TV | 2.4M | 184.62 | 8y ago | `dExFtP-nXTw` |
| 2 | "How To Add Refrigerant To Air Conditioner" | Word of Advice TV | 2.2M | 169.23 | 6y ago | `T2s38Dg8s4g` |
| 3 | "How To Add Refrigerant To Your Air Conditioner R410A & R22" | The DIY HVAC Guy | 1.2M | 28.92 | 3y ago | `MHZVnjqdYEY` |
| 4 | "How To PROPERLY Recharge Your Air Conditioner" | The DIY HVAC Guy | 1M | 24.10 | 3y ago | `J1s4wxDBe24` |
| 5 | "How to Stop Cold Air Leaks in Your House for the Winter / Make Your Home More Energy Efficient" | The Fixer | 857K | 17.67 | 2y ago | `yV2Jv3fPq9k` |

### cooling without AC (tricks, DIY coolers) (NEW (not in labels.md); scope home)

n 300 videos, 109 channels; last 12 months n 262. Faceless-persona videos: 68. Top 3 channels by videos: Builds With Eli Yoder (@BuildsWithEliYoder, tier C) 16; Passive Survival (@PassiveSurvival, tier A) 13; Sketchy Survival (@SketchySurvival101, tier C) 10.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Turn Any Fan Into an Air Conditioner with 2 Ice Bottles ($0 DIY AC)" | Why Am I Green | 3.7M | 606.56 | 4mo ago | `H514-w6ttNo` |
| 2 | "2 in 1 DIY Mini Air Conditioner with a Fan – Cools Instantly Like a Real AC" | Holic Creation | 1.9M | 135.71 | 5mo ago | `XXBuzbGRDqk` |
| 3 | "Transform Any Fan Into A Free AC System / DIY AC That Really Works!!!" | Zen Garden Oasis | 1.7M | 36.96 | 3mo ago | `mUoj_DGsOZY` |
| 4 | "This $300 Tunnel Cools Any Home 55°F FOREVER...(Science Explained)" | Sketchy Survival | 1.5M | 1250.00 | 6mo ago | `zn5IiwhAxgU` |
| 5 | "DIY  Mini Air Conditioner with Fan – Cools Instantly Like a Real AC" | Holic Creation | 1.5M | 107.14 | 1y ago | `LpCmVZvikSk` |

### trade: commercial and refrigeration (trade-facing; scope trade)

n 289 videos, 69 channels; last 12 months n 67. Faceless-persona videos: 10. Top 3 channels by videos: Jeff’s HVAC Adventures (@JeffsHVACAdventures, tier A) 27; D2D NY Real World HVAC Simplified (@D2DNYAC, tier A) 25; Ryan Hughes HVAC (@RyanHughesHVAC, tier A) 20.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "5 Woodpile Dangers That Can Put You in the Hospital. Number 3 Grows on Half of America's Firewood" | Harlan Sawyer | 438K | 128.82 | 1mo ago | `BlHC-momweM` |
| 2 | "Commercial or Residential HVAC / Which Do I Prefer??" | Quality HVACR | 227K | 18.92 | 6y ago | `j6vQoVZ9HpQ` |
| 3 | "HVAC Commercial rooftop package unit Beginners Guide" | Taddy Digest | 206K | 18.73 | 6y ago | `ZW579yzqnrY` |
| 4 | "Commercial Log Splitter vs. Firewood Processor" | Hometown Acres | 171K | 3.23 | 6y ago | `EeQzedpINEo` |
| 5 | "#1 Failure with Commercial HVAC" | Quality HVACR | 158K | 13.17 | 3y ago | `2A3P1edJacM` |

### seasonal maintenance (seasonal maintenance; scope home)

n 278 videos, 148 channels; last 12 months n 169. Faceless-persona videos: 81. Top 3 channels by videos: Drewdriskle (@Drewdriskle, tier A) 16; OnemanHVAC (@Onemanhvac, tier A) 11; Yarbrough & Sons Heating, Cooling & Plumbing (@yarbrough_and_sons, tier A) 9.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Effective heating for winter 2024! I welded a barrel of pipes and it all worked out!" | Creative inventions LMTN | 2.6M | 490.57 | 2y ago | `pO99zPvez_M` |
| 2 | "The $4 Amish Fix for a Deadly Hot House (Save $3000 This Summer)" | Elias Yoder | 1.9M | 208.79 | 5mo ago | `H8-QNBd7MIo` |
| 3 | "15 Air Conditioner Maintenance Tips" | Word of Advice TV | 1.9M | 146.15 | 7y ago | `pBBnXHse-T0` |
| 4 | "Why Every Homeowner Should Consider Installing an AC Soft Starter / Micro Air Easy Start Install" | How To Home | 1.3M | 6.50 | 3y ago | `MDp1g8r8IVs` |
| 5 | "Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter)" | The DIY HVAC Guy | 1.2M | 28.92 | 4w ago | `mP0IjyvQtxw` |

### coils and condenser cleaning (AC: central; scope home)

n 267 videos, 98 channels; last 12 months n 50. Faceless-persona videos: 9. Top 3 channels by videos: John Israel HVAC (@johnisraelhvac2019, tier A) 18; RHODES - Cosmic Cooling (@CosmicCooling, tier A) 13; Powlas HVAC (@Powlashvac, tier B) 13.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "How To Clean Your AC and Coils Like the Pros Do / WILL Make Air Blow Colder" | How To Home | 5.6M | 28.00 | 3y ago | `k7PSzi7NSyc` |
| 2 | "How To Properly Clean An AC Evaporator Coil & Save HUNDREDS!" | The DIY HVAC Guy | 2.2M | 53.01 | 3y ago | `kJNwqa7YXF0` |
| 3 | "8 Reasons Why Your AC is Freezing Up" | Word of Advice TV | 2M | 153.85 | 8y ago | `stZs8Co80vk` |
| 4 | "How To Clean Your AC Condenser Unit / Spring Cleaning Pro Tips" | Everyday Home Repairs | 1.8M | 5.03 | 3y ago | `IHtlj50PPYg` |
| 5 | "Central Air Conditioner Condenser Cleaning - How To - Make it COLD again!" | Silver Cymbal | 1.4M | 17.39 | 7y ago | `nsRHhU6q5RY` |

### scams and upsells (buying and replacing a system; scope home)

n 264 videos, 109 channels; last 12 months n 181. Faceless-persona videos: 97. Top 3 channels by videos: Anti DIY HVAC (@TedCookHVAC, tier A) 22; John The HVAC Guy (@JohnTheHVACGuy, tier A) 16; The DIY HVAC Guy (@diyhvacguy, tier A) 13.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Top 5 Things AC Companies Don't Want You To Know How To Do!" | How To Home | 2.9M | 14.50 | 3y ago | `AQQH9QwC46A` |
| 2 | "3 Things HVAC Contractors Don't Want You To Know About." | The DIY HVAC Guy | 2.7M | 65.06 | 4y ago | `SkLMRM9NnBY` |
| 3 | "HVAC Contractors Hate Me For Sharing This Secret" | The DIY HVAC Guy | 1.6M | 38.55 | 2y ago | `FMr4xOkUbO8` |
| 4 | "New Construction HVAC Hack Job Butcher Sabotage pathetic installers" | Anti DIY HVAC | 1.1M | 84.62 | 4y ago | `4r9tPgRlcxo` |
| 5 | "Most HEPA Air Purifiers Are A SCAM (There's A Better Option)" | Healthy Home Guide | 1.1M | 70.97 | 2y ago | `gaQTYrisieA` |

### buy or replace (sizing, repair vs replace, new system) (buying and replacing a system; scope home)

n 260 videos, 118 channels; last 12 months n 76. Faceless-persona videos: 13. Top 3 channels by videos: The DIY HVAC Guy (@diyhvacguy, tier A) 18; The Thought Provocateur (@thethoughtprovocateur, tier A) 12; Advantage Heating & Cooling (@AdvantageHVAC, tier A) 11.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Mini Split - 3 Things I Wish I Knew Before Installing" | LRN2DIY | 1.5M | 42.86 | 4y ago | `b67w0gEqHe8` |
| 2 | "Did You Know You Can Replace Your Own Air Conditioner?   -SAVE THOUSANDS-" | The DIY HVAC Guy | 954K | 22.99 | 3y ago | `FSrxRnYEt8E` |
| 3 | "Watch This Before You Buy a Mr Cool Mini Split" | LRN2DIY | 623K | 17.80 | 2y ago | `AMa6YRUwL2I` |
| 4 | "Save THOUSANDS Replacing Your Gas Furnace Yourself." | The DIY HVAC Guy | 545K | 13.13 | 3y ago | `jo98d4lx0FQ` |
| 5 | "Troubleshooting the limit switch on the 80% AFUE gas furnace" | grayfurnaceman | 540K | 469.57 | 13y ago | `rBCW3qYjtr0` |

### general: heating (equipment not named) (NEW (not in labels.md); scope general)

n 204 videos, 110 channels; last 12 months n 109. Faceless-persona videos: 24. Top 3 channels by videos: plumberparts (@plumberparts, tier B) 17; Skill Builder (@SkillBuilder, tier B) 9; Elderly Thoughts (@ElderlyThoughts1, tier C) 8.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Endless Heat Without Electric / Safe Reliable And Low Cost" | Zen Garden Oasis | 2M | 43.48 | 1y ago | `UfcgT1Ysegc` |
| 2 | "This Home Survives EF5 Tornadoes, Wildfires, and Costs $0 to Heat. Why Aren't We Using It?" | Wild Line | 963K | 22.93 | 7mo ago | `B-WJqqw5GcE` |
| 3 | "How to restore your central heating if you have a defective motorised valve." | dereton33 Plumbing and heating, DIY and blogging. | 649K | 332.82 | 13y ago | `T7UTDtrmcvM` |
| 4 | "SHOCKED This Heating System NEVER WORKED! Matt's Problem" | plumberparts | 606K | 20.20 | 2y ago | `byufrOQHIvA` |
| 5 | "Why is Your House Cold?" | Skill Builder | 562K | 11.47 | 5y ago | `pd-sIX01S5A` |

### replacement cost and quotes (buying and replacing a system; scope home)

n 201 videos, 98 channels; last 12 months n 103. Faceless-persona videos: 26. Top 3 channels by videos: Yarbrough & Sons Heating, Cooling & Plumbing (@yarbrough_and_sons, tier A) 14; Hartzell's Heat & Air (@hartzellsheatair6003, tier A) 10; Fire & Ice Home Services (@fireiceheatingandaircondit4363, tier A) 10.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "This Forgotten NASA Insulation Trick Cuts AC Costs 70%. They Stopped Teaching It in 1991." | Lost Tech Vault | 696K | 750.81 | 7mo ago | `qqevEiBIDUQ` |
| 2 | "Does Turning OFF your AC Cost You Big???" | Atlas AC | 445K | 23.42 | 1y ago | `DxOMhHEeUUs` |
| 3 | "Installing a low cost under floor radiant heat system in my house" | Jesse Muller | 300K | 3.08 | 4y ago | `ZvgqlQN1xEc` |
| 4 | "AC Unit Cost OVER THE TOP? Find out how to get a good deal!" | Atlas AC | 205K | 10.79 | 3y ago | `TRKuRbxhDrs` |
| 5 | "Infrared heater efficiency -- how much is radiated infrared?" | Matthias random stuff | 203K | 3.94 | 4y ago | `SDUlQagvT2k` |

### filters (filters; scope home)

n 188 videos, 122 channels; last 12 months n 74. Faceless-persona videos: 33. Top 3 channels by videos: The 3D Handyman (@The3DHandyman, tier B) 8; HowTo (@How2, tier B) 5; The Air Of Authority (@TheAirOfAuthority, tier A) 5.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Why You Need To Stop Using These Filters To Purify Your Air!  What To Use Instead" | How To Home | 1.9M | 9.50 | 2y ago | `6PcBk2umEWA` |
| 2 | "Connecting Two Metals Purifies ANY Water — The "Earth Filter" Secret They Buried" | Historia Prime | 1.6M | 145.45 | 7mo ago | `tSFizbjaCBo` |
| 3 | "Furnace Air Filter - How to Change It Properly" | LRN2DIY | 1.3M | 37.14 | 5y ago | `sOcfx5o9-B4` |
| 4 | "The Most Common Furnace Filter Issue And How To Fix It" | Everyday Home Repairs | 1.3M | 3.63 | 4y ago | `MFGRsWoSf4w` |
| 5 | "How to Change your Home Furnace Air Filter" | HowToWith GEO | 1M | 833.33 | 14y ago | `-lO4xAsTyqM` |

### smart thermostats (thermostats; scope home)

n 180 videos, 61 channels; last 12 months n 74. Faceless-persona videos: 4. Top 3 channels by videos: Hotrods & Homestead (@ModernHotrodsNH, tier A) 41; One Hour Smart Home (@OneHourSmartHome, tier B) 36; Simple Fix! (@AJ-cn6bz, tier A) 7.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "How to Replace HVAC Thermostat (How to Install Nest Thermostat)" | Word of Advice TV | 2.2M | 169.23 | 6y ago | `1mJkjrwxdP4` |
| 2 | "How To Fix A Missing C Wire / Nest Thermostat Troubleshooting" | Everyday Home Repairs | 923K | 2.58 | 4y ago | `Af6aaUyMc3E` |
| 3 | "Nest Thermostat No C Wire  Problem and Solutions" | Word of Advice TV | 801K | 61.62 | 6y ago | `nki-65gtvac` |
| 4 | "How To Use Nest Thermostat [The Missing Manual]" | One Hour Smart Home | 779K | 106.71 | 6y ago | `rdfUbAZi7k0` |
| 5 | "How To Install Ecobee SmartThermostat 2021 With 4 Wires, No C Wire" | One Hour Smart Home | 475K | 65.07 | 5y ago | `co-VS2mrKzg` |

### space heaters (electric) (alternative and supplemental heat (off-grid heat); scope home)

n 180 videos, 109 channels; last 12 months n 85. Faceless-persona videos: 25. Top 3 channels by videos: Magic Touch: Fire & Air (@magictouchair, tier A) 16; Channel Ron (, tier B) 7; DIY Top Tricks (@diytoptricks, tier B) 5.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Space Heater Nonsense" | Technology Connections | 5.3M | 2.86 | 7y ago | `V-jmSjy2ArM` |
| 2 | "Why Didn’t We Think Of This Sooner? DIY SAND HEATER" | The DIY HVAC Guy | 1.9M | 45.78 | 1y ago | `DZ1CkDlN6Xw` |
| 3 | "DIY Electric Fireplace Wall (Step By Step) / Shiplap" | House to Home DIY | 889K | 15.33 | 5y ago | `ON_xRrrpinc` |
| 4 | "More Space Heater Nonsense" | Technology Connextras | 807K | 2.57 | 7y ago | `Znt9WR5hhjE` |
| 5 | "DIY Carbon Felt Heater / Burns Forever Without Changing Out The Wick" | Zen Garden Oasis | 638K | 13.87 | 2y ago | `WTWE7yyu-5I` |

### error codes and troubleshooting (NEW (not in labels.md); scope home)

n 168 videos, 57 channels; last 12 months n 41. Faceless-persona videos: 4. Top 3 channels by videos: Mitch Attwood (@maracservices, tier A) 37; D2D NY Real World HVAC Simplified (@D2DNYAC, tier A) 20; Quality HVACR (@QualityHVACR, tier A) 13.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Old HVAC industry practices are holding us back and costing us money. But we can fix it." | Technology Connections | 2.8M | 1.51 | 2y ago | `DTsQjiPlksA` |
| 2 | "How to Repair a Motorised Central Heating Valve" | Skill Builder | 575K | 11.73 | 9y ago | `KT6mq1440zM` |
| 3 | "Diagnosing the stuck HVAC reversing valve" | grayfurnaceman | 547K | 475.65 | 13y ago | `HMY4N9ZM1cs` |
| 4 | ""It NEVER WORKED" Can We Fix Robert's Heating Problem?" | plumberparts | 479K | 15.97 | 10mo ago | `IlbIvvURRHI` |
| 5 | "Hot Ground Reverse on Outlet Tester Troubleshooting" | Apartment Maintenance Pro | 441K | 84.81 | 5y ago | `k6WpxvSgBPI` |

### fans for cooling (ceiling, whole-house, box) (NEW (not in labels.md); scope home)

n 161 videos, 91 channels; last 12 months n 78. Faceless-persona videos: 17. Top 3 channels by videos: Attic Airflow Lab (@AtticAirflowLab-YT, tier A) 7; HVAC OTJ (@hvacotj, tier A) 7; Creative DIY365 (@CreativeDIY365USA, tier C) 6.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "2 in 1 Used Oil Stove used fan 12 Voltage to replace gas / DIY Waste Oil Burner Stove" | Creative inventions LMTN | 3.4M | 641.51 | 4y ago | `tfpmlxeUwc0` |
| 2 | "How to make a highly efficient wood stove with a fan" | Creative Cement | 2.4M | 133.33 | 4y ago | `C4B5srrbqzE` |
| 3 | "AC Fan Outside Not Working - How To Check It" | Word of Advice TV | 803K | 61.77 | 8y ago | `fwjBkor-D3c` |
| 4 | "Why Did They Remove the Only Fan That Cools for Free? It’s Not Why You Think" | Earl Knows How | 484K | 302.50 | 1mo ago | `H6TQ8DLCqTQ` |
| 5 | "DIY Waste Oil Burner No Fan! Homemade Free Heat!" | Country Living Experience: A Homesteading Journey | 391K | 51.45 | 10mo ago | `pFGSAkditqk` |

### oil heat (boilers and old-house heat; scope home)

n 153 videos, 41 channels; last 12 months n 47. Faceless-persona videos: 2. Top 3 channels by videos: Barton Oil Burner Services (@BartonOilBurnerServices, tier A) 21; grayfurnaceman (@grayfurnaceman, tier B) 15; NOBOX7 (@NOBOX7, tier B) 13.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Free Heating Energy At Home ! DIY 3-in-1 Stove from an Old Oil Filter" | Holic Creation | 1.6M | 114.29 | 1y ago | `BiDkkufzctE` |
| 2 | "Millions don’t know waste oil is a gold mine! DIY 3-in-1 waste oil heater from oil filter" | Creative inventions LMTN | 1.2M | 226.42 | 4mo ago | `IRjeZP11TVg` |
| 3 | "I Made My Own Mini Heating Stove at Home! Simple / No-Electricity / Using an Oil Filter / Easy to Do" | Holic Creation | 1.2M | 85.71 | 1y ago | `sYn6EoBpcXM` |
| 4 | "Troubleshoot the oil furnace part 1. Burner won't start." | grayfurnaceman | 1M | 869.57 | 12y ago | `cog7MaShR7M` |
| 5 | "Oil furnace troubleshoot part 2 No flame" | grayfurnaceman | 1M | 869.57 | 12y ago | `TfPnLUz1Vh4` |

### smells and noises (NEW (not in labels.md); scope home)

n 146 videos, 79 channels; last 12 months n 32. Faceless-persona videos: 3. Top 3 channels by videos: The HVAC Hacker (@thehvachacker, tier A) 7; Drewdriskle (@Drewdriskle, tier A) 6; Derek Cole (@DerekMCole, tier A) 6.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Air Conditioner Noisy and Loud" | Word of Advice TV | 627K | 48.23 | 4y ago | `3sW14-QELUU` |
| 2 | "Next-Gen Window AC / Efficient Cooling Without The Annoying Noise" | Everyday Home Repairs | 627K | 1.75 | 3y ago | `flQjv5o1RzA` |
| 3 | "How To Fix a Noisy Bathroom Exhaust Fan / Easy Project" | Everyday Home Repairs | 445K | 1.24 | 6y ago | `YpOvA3Khd9w` |
| 4 | "How to stop kettling and banging noises from your central heating boiler." | dereton33 Plumbing and heating, DIY and blogging. | 301K | 154.36 | 12y ago | `KmGK0F3GMBM` |
| 5 | "Furnace Making Noise - Fix Blower Motor" | Dave Wirth | 299K | 20.62 | 8y ago | `cAE0dPJO1OQ` |

### evaporative coolers (NEW (not in labels.md); scope home)

n 132 videos, 27 channels; last 12 months n 38. Faceless-persona videos: 0. Top 3 channels by videos: desertsun02 (@desertsun02, tier C) 22; see how to do it (@boogity66, tier A) 22; Desi Ideas & Creativity (@desiideascreativity, tier C) 21.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Homemade air conditioner DIY - Awesome Air Cooler! - EASY Instructions - can be solar powered!" | desertsun02 | 15M | 2097.90 | 12y ago | `ITtlxjvLQis` |
| 2 | "Unique Ideas Fan Convert to Air Cooler.  Fan To Ac #invention" | Desi Ideas & Creativity | 3.7M | 2642.86 | 3y ago | `3y8cnTzVlfM` |
| 3 | "Making Air Cooler in just $3. Cool like Air Condition #diy" | Desi Ideas & Creativity | 2.6M | 1857.14 | 4y ago | `RVH4MiaJuyc` |
| 4 | "Homemade Evap. Air Cooler - The "5 Gallon Bucket" Swamp Cooler! DIY - can be solar powered!" | desertsun02 | 1.8M | 251.75 | 13y ago | `aHbQYajfGqM` |
| 5 | "Homemade Evaporative Air Cooler! - Simple "Box Fan" Conversion - EASY Instructions!" | desertsun02 | 1.6M | 223.78 | 13y ago | `Wf2Zhu4Fmzo` |

### condensate drain and water leaks (AC: central; scope home)

n 128 videos, 61 channels; last 12 months n 24. Faceless-persona videos: 5. Top 3 channels by videos: Anti DIY HVAC (@TedCookHVAC, tier A) 18; Kevin Jones (@kjfacilities-maint, tier B) 5; The HVAC Hacker (@thehvachacker, tier A) 5.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "How to UNCLOG your AC DRAIN Condensate line FAST - Water stains on Ceiling? or in the Pan" | Silver Cymbal | 3.7M | 45.96 | 7y ago | `qAxJb0J1HH0` |
| 2 | "HOW TO DRAIN YOUR HEATING SYSTEM - Pressurised - PLUMBING TIPS" | plumberparts | 772K | 25.73 | 12y ago | `_diB6LmlVq0` |
| 3 | "How to Clear Your Clogged AC Drain Line" | Willman Air Heating and Air Conditioning | 491K | 880.72 | 1y ago | `cFdN2XANBOQ` |
| 4 | "HOME AC CONDENSATION DRAIN LINE CLOG HOW TO MAKE IT EASIER TO UNCLOG & WHAT CAN HAPPEN IF YOU DON’T" | DIY Dan | 465K | 971.79 | 4y ago | `KsJEkqfWJqE` |
| 5 | "HOW TO DRAIN DOWN HEATING SYSTEMS - GRAVITY FED - Plumbing Tips" | plumberparts | 457K | 15.23 | 12y ago | `rZgOp6cACW4` |

### off-grid heat: diesel, propane and kerosene heaters (alternative and supplemental heat (off-grid heat); scope home)

n 112 videos, 33 channels; last 12 months n 32. Faceless-persona videos: 7. Top 3 channels by videos: David McLuckie (@DavidMcLuckie, tier C) 54; DIY JIM (@DIYJIM, tier B) 13; andyfireblade (@andyfireblade, tier C) 5.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "5 Buddy Heater Hacks You Probably Didn't Know! Don't Get Left Out" | SeidelRanch | 1.9M | 2004.22 | 3y ago | `aqfO0mdzD8Y` |
| 2 | "They banned my super cheap heating! 😡 New Diesel heater hacks tested proving efficiency and safety 🤯" | Joshua De Lisle | 1.8M | 9.86 | 2y ago | `gNKTZosL6d8` |
| 3 | "Cheapest diesel night heater on eBay test / review" | David McLuckie | 989K | 176.61 | 7y ago | `9YthaCqkMOs` |
| 4 | "A look inside the diesel heater while running" | David McLuckie | 447K | 79.82 | 7y ago | `0tTr16LY_TI` |
| 5 | "I Bet You Didn't Know About These Mr. Heater Hacks" | The DIY HVAC Guy | 427K | 10.29 | 2y ago | `0kFCjB2s6dg` |

### choosing a contractor (buying and replacing a system; scope home)

n 112 videos, 53 channels; last 12 months n 42. Faceless-persona videos: 12. Top 3 channels by videos: The Thought Provocateur (@thethoughtprovocateur, tier A) 12; HVAC Guide for Homeowners (@NewHVACGuide, tier A) 10; Anti DIY HVAC (@TedCookHVAC, tier A) 8.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "HVAC Contractors Practically Make Their Living On These" | The DIY HVAC Guy | 2.4M | 57.83 | 2y ago | `Is0pv2Qnza0` |
| 2 | "No Heat HVAC Sabotage by installers unsafe hackers" | Anti DIY HVAC | 355K | 27.31 | 7y ago | `PpE6q52-atM` |
| 3 | "We FIRED Our HVAC Contractor... Now It's Our Job" | Stud Pack | 225K | 1.32 | 2w ago | `i7n6h6em2HE` |
| 4 | "Lennox hack-job installers the butchery continues" | Anti DIY HVAC | 200K | 15.38 | 5y ago | `Z6eE5TVRSl4` |
| 5 | "How to insulate Metal Ductwork with foil insulation - for HVAC installers" | Clean Air Heating & Cooling | 156K | 256.37 | 3y ago | `pO4gVf4t0A0` |

### staying warm without heating (body, bed, clothes) (alternative and supplemental heat (off-grid heat); scope home)

n 101 videos, 77 channels; last 12 months n 92. Faceless-persona videos: 50. Top 3 channels by videos: June's Kitchen Table (@JunesKitchenTable, tier A) 4; Lost Survival Knowledge (@LostSurvivalKnowledge, tier C) 3; Sylvie Mercer (@SylvieMercer, tier B) 3.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Reusable handwarmers that get hot by freezing" | Technology Connections | 3.5M | 1.89 | 5y ago | `Oj0plwm_NMs` |
| 2 | "Staying Warm at the Cabin / Winter Day Living in Alaska" | Simple Living Alaska | 1.4M | 3.46 | 5y ago | `OwHYz0kTEk4` |
| 3 | "15 Cheap Walmart Items That Become WORTH GOLD When Your Furnace Dies" | Lost Survival Knowledge | 1.3M | 130.00 | 11d ago | `rX4eyZaHAjw` |
| 4 | "Before You Turn On Your Heat This Fall, Do This (Or Pay for It the First Cold Night)" | Ray Dutton's Garage | 943K | 62.87 | 1mo ago | `fHAlfm21vYw` |
| 5 | "Growing tropical fruit in the freezing mountains of Colorado without heating" | Stefano Creatini | 639K | 163.85 | 2y ago | `f5_fK7PNw1Q` |

### AC: portable (AC: portable; scope home)

n 96 videos, 39 channels; last 12 months n 28. Faceless-persona videos: 6. Top 3 channels by videos: SmitHVAC (@SmitHVAC., tier A) 10; Air Conditioner Lab (@AirConditionerLab, tier A) 8; Consumer Analysis (@consumer-analysis, tier B) 7.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Portable Air Conditioners - Why you shouldn't like them" | Technology Connections | 10M | 5.41 | 7y ago | `_-mBeYC2KGc` |
| 2 | "(1 YEAR REVIEW) black & decker “portable air conditioner” 12000 btu" | Live Free | 3.7M | 10755.81 | 5y ago | `RJQyCq9R6Cs` |
| 3 | "The Cheapest Way to Cool Your Home / Solar AC Setup" | Taddy Digest | 882K | 80.18 | 2y ago | `-fGgoRoi_u4` |
| 4 | "How to Install a Portable AC Unit in a Window (Step-by-Step)" | HowToWith GEO | 822K | 685.00 | 1y ago | `ovyHVr0DNW4` |
| 5 | "10 Ways to Vent a Portable Air Conditioner" | Word of Advice TV | 556K | 42.77 | 2y ago | `EjQH6H_31ME` |

### HVAC, not mapped (not mapped; scope unmapped)

n 96 videos, 48 channels; last 12 months n 52. Faceless-persona videos: 15. Top 3 channels by videos: AEPowerHouseTV (@AEPowerHouseTV, tier B) 12; Nor-Cal Refrigeration & H.V.A.C (@NorCal-refrigeration, tier B) 8; Everything Electric TECH (@EverythingElectricShow, tier C) 7.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Power is not energy: why the difference matters" | Technology Connections | 2.2M | 1.19 | 1y ago | `OOK5xkFijPc` |
| 2 | "Free Electricity! Don't Throw Away Your Old TV - Easy Ways to Generate Energy from Old Electronics" | Holic Creation | 626K | 44.71 | 1y ago | `xJAkYwxMvGc` |
| 3 | "How to Make a House Energy Efficient" | Dr. Energy Saver | 607K | 4.98 | 14y ago | `HQVTcy4SlAk` |
| 4 | "Ghost Shelter Secrets: Hide From Thermal Drones Like A Pro!" | Sketchy Survival | 457K | 380.83 | 9mo ago | `390CFzk3-Ak` |
| 5 | "This $80 Amish Device Powers Any Home Off-Grid Forever. Why Is the Energy Industry Silent?" | Builds With Eli Yoder | 415K | 244.12 | 5mo ago | `ZfowdGYNqaU` |

### AC: window (AC: window; scope home)

n 80 videos, 39 channels; last 12 months n 16. Faceless-persona videos: 2. Top 3 channels by videos: Air Conditioner Lab (@AirConditionerLab, tier A) 9; The Fixer 2 (@thefixerhomerepair2, tier B) 9; Word of Advice TV (@WordofAdviceTV, tier A) 7.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Midea 8,000 BTU U Smart Inverter Window AC Installation and Review" | The Fixer | 7M | 144.33 | 5y ago | `hux4BEKiu6k` |
| 2 | "Clean Window AC the LAZY (but still effective) way!" | Handyman Hertz | 3.1M | 873.24 | 3y ago | `nVLRm_S0zto` |
| 3 | "Window Air Conditioner Not Cooling? EASY Common Fix - How to Clean a Windows AC" | Silver Cymbal | 2.3M | 28.57 | 6y ago | `o8KQu_MlpoY` |
| 4 | "How to Install a Window A/C Unit" | HowToWith GEO | 2.3M | 1916.67 | 13y ago | `mwoEkiRFEA4` |
| 5 | "Window Air Conditioner Not Cooling And The Most Common Fix" | Word of Advice TV | 2.3M | 176.92 | 6y ago | `an1yClPV4i4` |

### adjacent: solar, batteries and home energy systems (adjacent: solar and home energy; scope adjacent)

n 65 videos, 37 channels; last 12 months n 42. Faceless-persona videos: 8. Top 3 channels by videos: DIY Solar Power with Will Prowse (@WillProwse, tier C) 8; Simple Tek (@SimpleTek, tier C) 5; Secret Sparks (@SecretSparks-v8d, tier B) 4.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Sand for Thermal Energy Storage" | Simple Tek | 256K | 15.06 | 5y ago | `UvNv_gM_ZUk` |
| 2 | "My Battleborn Battery (Dragonfly Energy) Caught on Fire. Thermal Failsafe did NOT work." | DIY Solar Power with Will Prowse | 245K | 1.47 | 3mo ago | `_MOol0_DuU4` |
| 3 | "HERSCHEL Infrared Heating - The Smart Route to Net Zero Heating" | Everything Electric TECH | 238K | 6.03 | 4y ago | `zSzYSfkwrts` |
| 4 | "6 Types of Solar Thermal Collector" | Simple Tek | 234K | 13.76 | 6y ago | `rg1x4jJmSl4` |
| 5 | "Do You Own Battleborn Batteries (Dragonfly Energy)? Watch This! Safety Issue Update" | DIY Solar Power with Will Prowse | 205K | 1.23 | 8mo ago | `DUtbnbLpvFk` |

### carbon monoxide and gas safety (humidity, ventilation and indoor air; scope home)

n 64 videos, 41 channels; last 12 months n 13. Faceless-persona videos: 4. Top 3 channels by videos: WarmZilla (@WarmZilla, tier A) 9; American Veteran Air & Heat (@americanveteranairandheat, tier A) 3; Mikey Pipes - Pipe Doctor Plumbing & Heating & Air (@PipeDoctor, tier A) 3.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "The clever feature that makes cheap heaters safe — and why they're actually dangerous" | Technology Connections | 2.9M | 1.57 | 1y ago | `HnMuNCl7tZ8` |
| 2 | "⚠️How to SAFELY Transfer Propane from 20# Tank⚠️ Refill ANY SIZE" | Hotrods & Homestead | 210K | 225.93 | 5y ago | `vYlForpG2OI` |
| 3 | "Testing UL Listed Carbon Monoxide Alarms vs. Defender Low Level Upgrade" | Home Performance | 120K | 25.53 | 5y ago | `e_R9NaTRVFE` |
| 4 | "Carbon Monoxide: I've Been Doing This Wrong My Whole Life" | LRN2DIY | 64K | 1.83 | 2y ago | `4kr5VcOV0P0` |
| 5 | "SMOKE/FIRE & CARBON MONOXIDE FIRST ALERT ALARM WHAT 1 CHIRP, 3 CHIRPS, & 5 CHIRPS MEAN & HOW TO FIX" | DIY Dan | 60K | 125.39 | 5y ago | `--bhph1xxus` |

### general: no heat (equipment not named) (NEW (not in labels.md); scope general)

n 46 videos, 22 channels; last 12 months n 15. Faceless-persona videos: 1. Top 3 channels by videos: Ryan Hughes HVAC (@RyanHughesHVAC, tier A) 4; Davevid (@Davenagams, tier B) 4; The HVAC Hacker (@thehvachacker, tier A) 4.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "No Heating late night service call" | Anti DIY HVAC | 166K | 12.77 | 4y ago | `2zMn1Yah6jY` |
| 2 | "Weil McLain No Heat Emergency Service Call by Local Plumber Pipe Doctor" | Mikey Pipes - Pipe Doctor Plumbing & Heating & Air | 156K | 26.44 | 1y ago | `K3m-OCX6LLM` |
| 3 | "No Heat Burners Keeps Cutting Out" | The HVAC Hacker | 87K | 11.30 | 7y ago | `aGA_iNpzq4M` |
| 4 | "No Heat Service Call Basement Flooded" | Anti DIY HVAC | 64K | 4.92 | 7y ago | `tK8dpH3hAkQ` |
| 5 | "No Heat - 6 FIGURE Unit Down $$$$" | Davevid | 60K | 42.86 | 8mo ago | `GVcfZm-zCjY` |

### heating fuel and fuel choice (heating fuel and fuel choice; scope home)

n 41 videos, 28 channels; last 12 months n 18. Faceless-persona videos: 3. Top 3 channels by videos: The Passive House Files (@griffithselijah7018, tier C) 5; Anti DIY HVAC (@TedCookHVAC, tier A) 3; John Israel HVAC (@johnisraelhvac2019, tier A) 3.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "STOP Buying $10,000 Home Batteries. Fill This $150 PROPANE TANK With Solar Power in One Weekend!!" | The Passive House Files | 315K | 31.50 | 2mo ago | `-goA9ImZHIQ` |
| 2 | "This $90 PROPANE TANK Stores SOLAR Power For 30 YEARS — NO BATTERIES NEEDED!!" | The Passive House Files | 290K | 29.00 | 3mo ago | `KMvlD6e87Ak` |
| 3 | "Propane torch "boost Upgrade" hack" | NOBOX7 | 170K | 130.77 | 8y ago | `u5zOhEMSdWM` |
| 4 | "⚠️Propane Tank OPD Valve Disassembly⚠️ HOW it works & What CAN be REPLACED?" | Hotrods & Homestead | 74K | 79.61 | 5y ago | `YfQGu2kKHPE` |
| 5 | "The Hidden Cost Of Propane And Some ways of ripping open the cage" | Life in Farmland | 62K | 8.67 | 7y ago | `eKPLvAwyOKM` |

### RV, van, tent and camping heat or cool (NEW (not in labels.md); scope home)

n 33 videos, 25 channels; last 12 months n 14. Faceless-persona videos: 1. Top 3 channels by videos: DIY Top Tricks (@diytoptricks, tier B) 4; MR Post Frame (@MrPostFrame, tier B) 3; Forgotten Survival (@ForgottenSurvival, tier C) 2.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Free heating fuel but it's illegal - £120 8kw Diesel parking heater review from VEVOR" | Joshua De Lisle | 5M | 27.40 | 3y ago | `KyiUpFjwtlU` |
| 2 | "How to make the ultimate rocket stove from tin cans! Perfect for heating and camping" | DIY Top Tricks | 321K | 25.68 | 1y ago | `6aDczSvW6o4` |
| 3 | "10 WWII Cabin Heating Secrets — Why Did Modern Builders Forget These?" | Historia Prime | 306K | 27.82 | 9mo ago | `lPZo_xlSYmI` |
| 4 | "how to make a mini camping wood stove #160 #" | Penpen vn 1 | 215K | 0.25 | 5y ago | `YPZlPHvtcT4` |
| 5 | "Medieval Builders Knew About LOG CABIN Heating That Modern Ones Forgot" | Medieval Wisdom | 152K | 23.21 | 11mo ago | `CmEmlwUpmjQ` |

### garage, shop and outbuildings (NEW (not in labels.md); scope home)

n 24 videos, 19 channels; last 12 months n 13. Faceless-persona videos: 5. Top 3 channels by videos: Quality HVACR (@QualityHVACR, tier A) 2; Simple Living Alaska (@SimpleLivingAlaska, tier B) 2; Country Living Experience: A Homesteading Journey (@CountryLivingExperience, tier C) 2.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Warm Winter Days / Cabin Life in Alaska" | Simple Living Alaska | 839K | 2.07 | 4y ago | `pwj-0Bh8-h8` |
| 2 | "Solar Shed: Running a Cheap Air Conditioner" | DIY Solar Power with Will Prowse | 541K | 3.24 | 6y ago | `2Qh14pX3IxA` |
| 3 | "How To Heat Your Garage / Workshop for CHEAP" | Hometown Acres | 519K | 9.79 | 5y ago | `XDNLKG74XcY` |
| 4 | "When Can Chicks Go Outside In Coop Full Time Without A Heat Lamp?" | Country Living Experience: A Homesteading Journey | 464K | 61.05 | 6y ago | `B8kckzKvC04` |
| 5 | "Building a Shop Workbench & Corned Caribou / Warm Winter Weather at the Cabin" | Simple Living Alaska | 351K | 0.87 | 1y ago | `v3h9xG-IR70` |

### general: cooling (equipment not named) (NEW (not in labels.md); scope general)

n 21 videos, 16 channels; last 12 months n 13. Faceless-persona videos: 1. Top 3 channels by videos: Why Am I Green (@whyamigreen, tier B) 4; Patina (@PatinaYT1, tier C) 2; The Build Guide (@TheBuildGuides, tier C) 2.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "This House NEVER gets Hot. Why Did the Energy Industry Bury It?" | The Build Guide | 252K | 469.27 | 6mo ago | `C5DRPlNLZVU` |
| 2 | "How to remove hot air from your house naturally" | Archi notes | 222K | 23.37 | 1mo ago | `y7BODYGLZUQ` |
| 3 | "DIY Kiln Build -Super Hot & Ultra Efficient" | Greenhill Forge | 156K | 0.85 | 1y ago | `05XwPTy9cE8` |
| 4 | "25 Cheap Meals Our Grandparents Ate to Survive Hot Summers" | Wonders | 54K | 1.96 | 3mo ago | `CcnT_Ke17R0` |
| 5 | "What Did Ancient Japanese Do When It Was Too Hot to Sleep?" | Patina | 17K | 2.70 | 1mo ago | `81S4qZ1zUlg` |

### general: HVAC basics and how it works (NEW (not in labels.md); scope general)

n 14 videos, 12 channels; last 12 months n 3. Faceless-persona videos: 0. Top 3 channels by videos: AEPowerHouseTV (@AEPowerHouseTV, tier B) 2; Heat Geek (@HeatGeek, tier A) 2; Sketchy Survival (@SketchySurvival101, tier C) 1.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Variable Speed HVAC FINALLY explained by Carrier expert!!" | Atlas AC | 39K | 2.05 | 2y ago | `5a9RSnA4UaY` |
| 2 | "Heating Water treatment explained (VDI 2035) and BIG NEWS!" | Heat Geek | 21K | 1.31 | 5y ago | `NJFU-nbliXw` |
| 3 | "Unexplained glitch on HVAC system" | Anti DIY HVAC | 10K | 0.77 | 1y ago | `6t109XIw3VU` |
| 4 | "Heating Mastery - What it is, and how it works" | Heat Geek | 5.1K | 0.32 | 5y ago | `JNWmfEsyzNY` |
| 5 | "Whole-House Air Filtration Systems Explained / Healthier Air for Cold & Flu Season" | AEPowerHouseTV | 4.9K | 36.57 | 1y ago | `aSbSI4Ee9U8` |

### adjacent: water heaters (adjacent: water heaters; scope adjacent)

n 6 videos, 6 channels; last 12 months n 2. Faceless-persona videos: 1. Top 3 channels by videos: DIY DDS (@Drrich_DIY, tier B) 1; Silent Steam Team (@gordonschweizer5154, tier A) 1; iDoThings (@idothings6605, tier B) 1.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Removing tankless coil from boiler and replacing with blank cover plate" | iDoThings | 46K | 3.41 | 5y ago | `O_jaLW8fB3Q` |
| 2 | "Oil fired boiler Tankless coil gasket leak- DIY replaced cover and gasket" | DIY DDS | 17K | 29.82 | 6y ago | `vU4qZL91wm8` |
| 3 | "This Underground Water Tank Stores Summer Heat for Winter. $0 Bills Forever. Illegal in 31 States?" | Builds With Eli Yoder | 4.1K | 2.41 | 6mo ago | `T7SCu4dVkSM` |
| 4 | "A Water Tank Can Store Heat for Your Home — It Can’t Replace a Battery" | Backyard Low Tech | 1.3K | 0.41 | 1mo ago | `HMJS35Y4h5w` |
| 5 | "Adding A Sacrificial Anode To A Steam Boiler Water Feed Tank" | Silent Steam Team | 553 | 0.68 | 2y ago | `pNV2KBaTQEI` |

### out of scope: vehicle AC and heat (out of scope; scope out)

n 3 videos, 2 channels; last 12 months n 1. Faceless-persona videos: 0. Top 3 channels by videos: D2D NY Real World HVAC Simplified (@D2DNYAC, tier A) 2; Reuben Sahlstrom (@ReubenSahlstrom, tier B) 1.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "HOW TO WIRE A 9 LEADS SEMI HERMETIC COMPRESSOR STEP BY STEP" | D2D NY Real World HVAC Simplified | 12K | 12.00 | 6y ago | `S32keqBIIOk` |
| 2 | "Semi hermetic compressor tear down!" | Reuben Sahlstrom | 449 | 0.60 | 7mo ago | `7uYI4_p4x84` |
| 3 | "HVAC CONTROLS / SEMI HERMETIC COMPRESSOR" | D2D NY Real World HVAC Simplified | 399 | 0.40 | 5y ago | `oJlAcWFrdzc` |

### adjacent: frozen pipes (adjacent: frozen pipes; scope adjacent)

n 1 videos, 1 channels; last 12 months n 1. Faceless-persona videos: 1. Top 3 channels by videos: BIG TICKET TRUTH (@BIGTICKETTRUTH, tier C) 1.

| # | Title | Channel | Views (tab) | Multiple | Age | ID |
|---:|---|---|---:|---:|---|---|
| 1 | "Ice Storm Outage Plan: Generator vs Battery vs Nothing — Only 1 Keeps Your Pipes From Bursting" | BIG TICKET TRUTH | 32 | 0.15 | 6d ago | `-toBQ46Dmus` |

## Hand-check: 100 random A-C HVAC titles (seed 2611)

`random.Random(2611).sample` of the A-C HVAC video IDs, sorted. I read each title and gave my own primary sub-niche under the same tie-break (a reading). "First pass" = the rule's tag when I first read the sample; "rule now" = after the fixes the sample led to (the rules were then re-run). Agreement after fixes is not an independent test, because the fixes were written from this sample. Three titles I agreed with when read (two here, one in the fresh check) later moved, with my reading, to the DIY stove-build split added after both checks; they count as agreeing when read.

**Agreement (fine sub-niche): first pass 70 of 100; after fixes 93 of 100. At the labels.md parent level after fixes: 94 of 100.** 3 of the 100 are not HVAC in my reading (errors of the `is_hvac` title mark, not of this map; counted as disagreements).

| # | ID | Title | Rule first pass | Rule now | Mine | Agree now | Note |
|---:|---|---|---|---|---|:---:|---|
| 1 | `jzEu33PfP9E` | "I HEAT THIS HOMEMADE RADIATOR FOR FREE Using Waste Exhaust Gas from a Diesel Oil Heater Chinese" | oil heat | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | yes | homemade radiator heated free from diesel-heater exhaust: a DIY free-heat build |
| 2 | `VgwWoHq8pjE` | "Share how to make a large wood stove for your family to use, can be used indoors and outdoors # 217" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: DIY stove builds (cement, barrel, brick craft) | off-grid heat: DIY stove builds (cement, barrel, brick craft) | yes | (split added after this check) a stove-building craft video |
| 3 | `0lKIYb5R62c` | "TESTING AN IGNITION COIL PACK IS EASY ~ STEP-BY-STEP" | parts homeowners touch | parts homeowners touch | not HVAC | **no** | ignition coil pack is a car part; an is_hvac false positive |
| 4 | `dg8KqDEpOyE` | "Air Purifiers vs. Ventilation: The Truth About Indoor Air Quality" | indoor air and purifiers | indoor air and purifiers | indoor air and purifiers | yes |  |
| 5 | `-adyiizXIIE` | "Top 5 Best Air Conditioner For Room / Top-Rated Air Conditioners For Every Room" | brand verdicts | brand verdicts | brand verdicts | yes | a 'best' list = brand verdicts (labels.md: choosing across a category) |
| 6 | `z6oUS6gkicU` | "9 Ways I Keep My Bed Warm With No Heat (The Cold Comes From Underneath)" | staying warm without heating (body, bed, clothes) | staying warm without heating (body, bed, clothes) | staying warm without heating (body, bed, clothes) | yes |  |
| 7 | `us9OA6qMqNw` | "How To Clean Your Mini Split System Like A Pro" | mini-split | mini-split | mini-split | yes |  |
| 8 | `AkAtgMgbnmY` | "HVAC Service- Evaporator Coil Replacement" | coils and condenser cleaning | coils and condenser cleaning | coils and condenser cleaning | yes |  |
| 9 | `Xy0Sk8sWNA4` | "Building the PERFECT Crawlspace" | humidity and dehumidifiers | humidity and dehumidifiers | humidity and dehumidifiers | yes |  |
| 10 | `kX6fguBrYCY` | "Furnace Heater Not Running? Bad Thermostat? Blower Running? AC Running Simultaneously?" | thermostats | thermostats | furnaces | **no** | the furnace not running is the subject; the thermostat is one guessed cause |
| 11 | `HV99XjzVZDI` | "Emergency Heat / How To Power Your Gas Furnace When The Lights Go Out" | heat and power in an outage | heat and power in an outage | heat and power in an outage | yes |  |
| 12 | `rUhaUWh-Xks` | "Replacing a 30-Year-Old Heat Pump With a New Goodman R-32 System" | heat pumps | buy or replace (sizing, repair vs replace, new system) | buy or replace (sizing, repair vs replace, new system) | yes | replacing a 30-year-old heat pump with a new system |
| 13 | `7wXGWCn0oGg` | "Panasonic Whisper Remodel 80 - 110 CFM Exhaust Fan FV-0811RFL1 Install #homeimprovement #diy  #how" | trade: technical training | indoor air and purifiers | indoor air and purifiers | yes | bathroom exhaust-fan install; 'CFM' is a spec, not trade training |
| 14 | `jPcp0iLoJtM` | "How to Point a Brickwork Wall or Repoint a Chimney" | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: wood and pellet stoves, fireplaces | not HVAC | **no** | masonry repointing; the chimney is incidental |
| 15 | `aVm5OO7CDCg` | "The AC Was Cooling... So Why Was the House Still Humid?" | humidity and dehumidifiers | humidity and dehumidifiers | humidity and dehumidifiers | yes |  |
| 16 | `R5zomh0xdWg` | "Bryant HVAC Install And Return Added" | ducts and vents | ducts and vents | ducts and vents | yes | system install with a return added |
| 17 | `AInBNiPPi54` | "Stove that can melt aluminum at 1000 degrees C / Wood mulch stove" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | yes | DIY stove craft from wood mulch; wood stoves |
| 18 | `rhYuYgf-Jzg` | "Aprilaire 800 Steam Humidifier Installation And Carrier COR Thermostat" | thermostats | thermostats | humidity and dehumidifiers | **no** | humidifier install named first; the thermostat is secondary (two-topic title) |
| 19 | `lnP_WEnG2TU` | "Adding / Pairing SMART Room Sensor / Ecobee Premium Enhanced Essential Thermostat (QUICK Guide)" | smart thermostats | smart thermostats | smart thermostats | yes |  |
| 20 | `znWQFDsLBTw` | "Truth About Heat Loss Calculations – What Homeowners Need to Know Before Installing a Heat Pump" | heat pumps | buy or replace (sizing, repair vs replace, new system) | buy or replace (sizing, repair vs replace, new system) | yes | heat-loss calculation = sizing before buying |
| 21 | `26uq_qHKRjU` | "DIY Freezing AC : Crafting an Icy Air Conditioner down to -32°C!" | thermostats | cooling without AC (tricks, DIY coolers) | cooling without AC (tricks, DIY coolers) | yes | DIY 'freezing AC' craft build; the -32°C is not a thermostat setting |
| 22 | `sJiRT_tNOQk` | "How to Properly Perform Annual Service and Maintenance on a Central AC System" | seasonal maintenance | seasonal maintenance | seasonal maintenance | yes |  |
| 23 | `U0u40HBqJwg` | "Exhaust fan motor change out" | buy or replace (sizing, repair vs replace, new system) | indoor air and purifiers | indoor air and purifiers | yes | exhaust-fan motor swap; 'change out' is not a system replacement |
| 24 | `QF8tLQZD5n0` | "Window Condensation in Winter? 7 Things Homeowners Should Check" | humidity and dehumidifiers | humidity and dehumidifiers | humidity and dehumidifiers | yes |  |
| 25 | `yIFz5umIUHQ` | "Mini Split AC Control board Blowing Up - What's Wrong?" | mini-split | mini-split | mini-split | yes |  |
| 26 | `_Ov2uBZ9dT4` | "9 Furnace Mistakes That Keep Your House Cold All Winter" | furnaces | furnaces | furnaces | yes |  |
| 27 | `_BNWKZPKIhU` | "Best AC Compressor Replacement Video on Youtube" | brand verdicts | AC: central | AC: central | yes | compressor replacement how-to; not a brand or model verdict |
| 28 | `1ahpc4q_p6I` | "25 Winter Survival Tricks for Seniors Living Alone (That Cost Pennies!)" | heat and power in an outage | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | yes | cheap winter survival tricks; nothing says the power is out |
| 29 | `9eDVW1BdVzo` | "Trane Variable Speed Blow Motor Fail and Repair" | parts homeowners touch | parts homeowners touch | parts homeowners touch | yes |  |
| 30 | `_RsLb2rUXGo` | "Does a Heat Pump Really Work In A Victorian Terrace?" | heat pumps | heat pumps | heat pumps | yes |  |
| 31 | `6WiA9rtMKQk` | "Nuwave Oxypure Smart Review - The Best Air Purifier for Large Rooms?" | brand verdicts | indoor air and purifiers | indoor air and purifiers | yes | one named purifier reviewed: labels.md keeps single-product reviews in the equipment's sub-niche |
| 32 | `AhLs0FdTL40` | "Heat Pump Noise Nightmares? Here’s What You Need To Know" | scams and upsells | smells and noises | smells and noises | yes | heat-pump noise; 'nightmares' is not a scam |
| 33 | `oia-jFUva40` | "How to Clean Condenser Coils on Air Conditioner" | coils and condenser cleaning | coils and condenser cleaning | coils and condenser cleaning | yes |  |
| 34 | `4nddYnLGRcg` | "How To Install a Ductless Mini Split Pro DIY at My House" | mini-split | mini-split | mini-split | yes |  |
| 35 | `6gB-QA33NoE` | "The Reason I Prefer Softwood Firewood (Nobody Talks About This)" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | yes |  |
| 36 | `ft5mwIT8ZKg` | "Add 15 Gallon Tank to Diesel Heater" | off-grid heat: diesel, propane and kerosene heaters | off-grid heat: diesel, propane and kerosene heaters | off-grid heat: diesel, propane and kerosene heaters | yes |  |
| 37 | `AAT7xUT3qsI` | "How to Detect a Mini Split Refrigerant Leak and Review of the Sensyx SFD201 Leak Detector" | mini-split | mini-split | mini-split | yes | mini-split family wins over refrigerant (tie-break) |
| 38 | `p5_CWjAxHF0` | "How I Deal With CALLBACKS In The HVAC Trade" | general: HVAC, topic not named | trade: careers, business and tech life | trade: careers, business and tech life | yes | callbacks in the HVAC trade |
| 39 | `dcWrBA8EIDA` | "The Attic Trick That Cuts Heating Bills in Half" | energy bills | energy bills | energy bills | yes | the bill wins over the attic (tie-break) |
| 40 | `2JxwVP4LbOQ` | "🏆 This Buried Pipe Cools Your Home for FREE (Nobody Talks About It)" | off-grid heat: free-heat tricks and DIY heaters | cooling without AC (tricks, DIY coolers) | cooling without AC (tricks, DIY coolers) | yes | a buried pipe that cools the home |
| 41 | `vHVITBbPcQI` | "Upstairs Hot, Downstairs Cold? Flip This Lever First" | ducts and vents | ducts and vents | ducts and vents | yes |  |
| 42 | `PXTCa5ndKWw` | "The $77,000 Mistake You're Making With Your Fireplace" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | yes |  |
| 43 | `MD6o8FBah1Y` | "Heating wood pellet review 2020" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | yes |  |
| 44 | `3T1bown4WG8` | "5 Things HVAC Contractors Don't Want You To Know About" | scams and upsells | scams and upsells | scams and upsells | yes | contractor villain |
| 45 | `hWKtzvWf5es` | "How to initiate Forced Defrost and replace defrost thermostat?" | heat pumps | heat pumps | heat pumps | yes |  |
| 46 | `YoeGMiVNoIU` | "Convert R22 unit to R404A" | refrigerant | refrigerant | refrigerant | yes |  |
| 47 | `Do6Rt9awpbQ` | "STOP Paying $6,000 for a New Furnace. 9 Old Habits From 1977 Fix the Bill" | energy bills | energy bills | energy bills | yes | bill named; the furnace quote is secondary |
| 48 | `9tbUFAocp5A` | "I Built a 3-in-1 Heater for My Home 😱 No Electricity, No Gas! Ready for Winter!" | heat and power in an outage | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | yes | homemade 3-in-1 heater that needs no electricity; no outage named |
| 49 | `qhVHQgGZ2A8` | "Should You Repair or Replace Your Furnace" | buy or replace (sizing, repair vs replace, new system) | buy or replace (sizing, repair vs replace, new system) | buy or replace (sizing, repair vs replace, new system) | yes |  |
| 50 | `J0g5NSwSJC8` | "Best Air Purifiers For Smoke 🚬 (Buyer's Guide) / HVAC Training 101" | trade: technical training | trade: technical training | brand verdicts | **no** | best purifiers buyer's guide; 'HVAC Training 101' is the channel's tag |
| 51 | `ym9sY2deIWk` | "WHY DOES MY GAS FURNACE KEEP SHUTTING OFF?  IT STARTS AND THEN TRIES TO START AGAIN????" | furnaces | furnaces | furnaces | yes |  |
| 52 | `fdUD8FZpkc8` | "This $1,300 Plug-In Heat Pump Replaces a $12,000 HVAC System — No Ducts Needed!" | heat pumps | heat pumps | heat pumps | yes |  |
| 53 | `geISIICV8Ag` | "Carrier heater running on a cold day" | space heaters (electric) | general: HVAC, topic not named | general: heating (equipment not named) | **no** | a Carrier 'heater' with no topic; probably a furnace or heat pump, not a space heater |
| 54 | `PGJ7xsWEm-U` | "14 Walmart Items to Stock Up On Before the First Hard Freeze" | seasonal maintenance | seasonal maintenance | seasonal maintenance | yes | borderline: winter stock-up list, not HVAC maintenance |
| 55 | `92DaQEp83QY` | "7 HVAC Products That Worked Too Well (So the Industry Quietly Killed Them)" | general: HVAC, topic not named | general: HVAC, topic not named | general: HVAC, topic not named | yes | no topic named; 'industry killed them' is the villain |
| 56 | `YZdbaxR9ZCc` | "My Ultimate Shop Wood Stove Build Part 2" | garage, shop and outbuildings | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | yes | a wood-stove build; the shop is the setting |
| 57 | `9KYbiMdP79U` | "Toucan Sam Parrot bird and the old floor furnace" | furnaces | furnaces | furnaces | yes |  |
| 58 | `PyrlxJW0tHw` | "Veto bag loadout HVAC" | trade: careers, business and tech life | trade: careers, business and tech life | trade: careers, business and tech life | yes |  |
| 59 | `SRCiGn7B0q4` | "HVAC Install- Return Duct Upgrade" | ducts and vents | ducts and vents | ducts and vents | yes |  |
| 60 | `9G3pkS6BkX4` | "Everything You Need To Know Before Buying A Trane AC" | buy or replace (sizing, repair vs replace, new system) | buy or replace (sizing, repair vs replace, new system) | buy or replace (sizing, repair vs replace, new system) | yes |  |
| 61 | `gkqG83hDjZY` | "No AC, no electricity needed! Powerful Homemade Air Conditioner That Freezes an Entire Room! 🥶" | heat and power in an outage | cooling without AC (tricks, DIY coolers) | cooling without AC (tricks, DIY coolers) | yes | homemade AC; 'no electricity needed' is the device, not an outage |
| 62 | `_P3pVtShkcc` | "HVAC Companies Practically Make a Living Off of this Cheap DIY Fix!" | error codes and troubleshooting | scams and upsells | scams and upsells | yes | 'HVAC companies make a living off this' = the company villain; the fix itself is not named |
| 63 | `dyusib94N20` | "Servicing the oil furnace part 1, the oil filter replacement" | filters | oil heat | oil heat | yes | oil furnace service (oil filter) |
| 64 | `etr11lF-Fu0` | "8 Medieval Heating Inventions So Advanced We Still Can't Beat Them" | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | yes |  |
| 65 | `BoiUDGU_VUw` | "How to make a wood stove from an old iron barrel" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: DIY stove builds (cement, barrel, brick craft) | off-grid heat: DIY stove builds (cement, barrel, brick craft) | yes | (split added after this check) a stove-building craft video |
| 66 | `rFAQTAnM0H4` | "HVAC Vlog: “Furnace & Air”" | trade: careers, business and tech life | trade: careers, business and tech life | trade: careers, business and tech life | yes |  |
| 67 | `h-s5G15iqDc` | "Installing a Blower Motor after a little Troubleshooting" | parts homeowners touch | parts homeowners touch | parts homeowners touch | yes |  |
| 68 | `0lfMtdU4C3c` | "Air Direction (Louver) Control in Air Conditioners Explained [Quick Overview]" | AC: central | AC: central | AC: central | yes | louvers on an AC; type of AC not named |
| 69 | `WnSQDl0rWuI` | "Wood Stove Deep Clean Every 3-4 Weeks for Maximum Performance" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | yes |  |
| 70 | `UY2Ee7hcX0I` | "The 7 Greatest Attic Fans Ever Built (And Why Most Disappoint) / No One Tell This Secret" | fans for cooling (ceiling, whole-house, box) | fans for cooling (ceiling, whole-house, box) | fans for cooling (ceiling, whole-house, box) | yes |  |
| 71 | `nuVRiIj1aU0` | "The $1 Homeless Meal That Lasts 7 Days Without Refrigeration" | HVAC, not mapped | HVAC, not mapped | not HVAC | **no** | a food video; is_hvac false positive ('refrigeration') |
| 72 | `OsnwssiwPIw` | "We Added Air Conditioning To This Home In ONE DAY.     /      Full Installation From Start To Finish" | AC: central | AC: central | AC: central | yes |  |
| 73 | `jR2MtQZInP8` | "Trane Capacitor replaced" | parts homeowners touch | parts homeowners touch | parts homeowners touch | yes |  |
| 74 | `I5nNfA1NFUw` | "Diesel Heater - Start on Diesel then switch to Veg oil?" | off-grid heat: diesel, propane and kerosene heaters | off-grid heat: diesel, propane and kerosene heaters | off-grid heat: diesel, propane and kerosene heaters | yes |  |
| 75 | `IW9pt75WAto` | "Do These 3 Things in September and Your Furnace Will Last 25 Years" | furnaces | furnaces | furnaces | yes | furnace-specific maintenance stays furnaces (labels.md: seasonal = across the whole system) |
| 76 | `LMZNx2XF6RQ` | "How Loud Is An Air Conditioner? Will My Neighbours Hate My AC?" | smells and noises | smells and noises | smells and noises | yes |  |
| 77 | `D8-2aks4ulo` | "How to make a 2 in 1 wood stove from beautiful red bricks" | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: DIY stove builds (cement, barrel, brick craft) | off-grid heat: DIY stove builds (cement, barrel, brick craft) | yes | a wood stove built from bricks (DIY stove-build split added after this check) |
| 78 | `Bk1H8BrI6-g` | "HOT Bonus Room? You MISSED This One Thing!" | general: cooling (equipment not named) | ducts and vents | ducts and vents | yes | a hot bonus room = airflow / uneven rooms |
| 79 | `jk4AWVn_Z1s` | "Steam Boiler Install: Dramatis Personae on Stage - Now They Await Their Lines" | boilers, radiators and steam | boilers, radiators and steam | boilers, radiators and steam | yes |  |
| 80 | `KdmFeXbdlGs` | "How to Make Your AC Blow Colder for Under $20 in 1 Hour!" | AC: central | AC: central | AC: central | yes |  |
| 81 | `CamdecXrezE` | "These 4 Things Will Kill Your AC Unit And Raise Your Bill!" | energy bills | energy bills | energy bills | yes | bill named; AC damage is the other half (tie-break) |
| 82 | `c5qtf0LnMa4` | "Inside the UK's Heating Revolution: New Heat Pumps, Industry Shake-Ups & Celeb Interview" | trade: careers, business and tech life | heat pumps | heat pumps | yes | heat-pump news; 'interview' is not trade-facing here |
| 83 | `je8M-2APogM` | "water source heat pump maintenance how does water source heat pump works" | heat pumps | heat pumps | heat pumps | yes |  |
| 84 | `BYpa5aptQh4` | "ACTRON AIR CONDITIONER NOT COOLING!!" | AC: central | AC: central | AC: central | yes |  |
| 85 | `OW2KUDVotYk` | "This 50 Year Old Boiler Shouldn’t Be Running" | boilers, radiators and steam | boilers, radiators and steam | boilers, radiators and steam | yes |  |
| 86 | `AiKcx7ghtHk` | "Build a New and improved fantastic output Waste Oil Burner." | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | yes |  |
| 87 | `bckTbpJbie4` | "Top 5 Best Small Window Air Conditioner!🔥🔥" | brand verdicts | brand verdicts | brand verdicts | yes | a 'best' list = brand verdicts |
| 88 | `Y6jWEzWZiwI` | "1961 Emerson Radio Quiet Kool 8000 BTU Air Conditioner" | AC: central | AC: central | AC: central | yes | vintage room AC; type not named in the title |
| 89 | `BQsSICx5H6g` | "Quick Oil Boiler Service! Nozzle and Filter Change!" | filters | oil heat | oil heat | yes | oil boiler service (nozzle and filter) |
| 90 | `Cym3gvCoZ9E` | "HVAC: Dealing With “Helicopter” Customers…" | general: HVAC, topic not named | trade: careers, business and tech life | trade: careers, business and tech life | yes | dealing with customers: trade-facing |
| 91 | `5K9pu-tkNYM` | "HVAC Tip on UV Lights! (Location Matters!)" | indoor air and purifiers | indoor air and purifiers | indoor air and purifiers | yes |  |
| 92 | `rEb7oryCQHI` | "Coleman Furnace Not Working / Furnaces" | furnaces | furnaces | furnaces | yes |  |
| 93 | `19FVhOr-SnQ` | "Solar & A2A update - Nov 2024 - super cheap heating" | adjacent: solar, batteries and home energy systems | heat pumps | heat pumps | yes | A2A = air-to-air heat pump |
| 94 | `VHStuvd5Zeg` | "Secrets mini HEATERS that few people know ! You should have when New York is buried in sea of ​​Snow" | space heaters (electric) | space heaters (electric) | space heaters (electric) | yes |  |
| 95 | `Lexucc10ODU` | "Why Does Every New Heat Pump Come with an Unreadable & Useless Controller?" | heat pumps | heat pumps | heat pumps | yes |  |
| 96 | `-jsHaxE9vrs` | "Why Your AC Keeps Running But Not Cooling DOWN?" | AC: central | AC: central | AC: central | yes |  |
| 97 | `e4b7t2n_y70` | "CARRIER INFINITY 25VNA KEEPS BLOWING FUSE??" | parts homeowners touch | parts homeowners touch | parts homeowners touch | yes |  |
| 98 | `EKz9EYcUlRc` | "2022 Carrier Heat Pump not Heating." | heat pumps | heat pumps | heat pumps | yes |  |
| 99 | `GIE1-hIhbvM` | "Battleborn Battery (Dragonfly Energy) Investigation" | adjacent: solar, batteries and home energy systems | adjacent: solar, batteries and home energy systems | adjacent: solar, batteries and home energy systems | yes | a battery company: adjacent |
| 100 | `f-fnwJ_L3GM` | "How to Clean Window AC (No Coil Cleaners)" | AC: window | AC: window | AC: window | yes |  |

### Fresh check: 50 more titles read after the seed-2611 fixes (seed 2612)

Because the after-fix figure above is not independent, I drew 50 more A-C HVAC titles (`random.Random(2612).sample` of the sorted IDs not in the first sample) and read them against the rules as they then stood. **Agreement when read: 34 of 50 (68%) at the fine sub-niche, 36 of 50 at the labels.md parent.** This is the fairest estimate of the map's accuracy. I then fixed the clear rule errors it showed; agreement with the rules now: 41 of 50 (again not independent).

| # | ID | Title | Rule when read | Rule now | Mine | Note |
|---:|---|---|---|---|---|---|
| 1 | `Isjsvft-3kw` | "HVAC Service Call Clips. Massive Commercial R22 Leak, Bad Maintenance Done By Well Known Company!" | trade: commercial and refrigeration | trade: commercial and refrigeration | trade: commercial and refrigeration |  |
| 2 | `lk3tuUg2jKU` | "CUSTOMER DOESNT THINK HER TRANE SYSTEM IS WORKING.  SHE FELT WARM AIR FROM VENTS." | ducts and vents | ducts and vents | AC: central | warm air from the vents of a Trane system = not cooling; vents are where she felt it |
| 3 | `-ctojtnu_vQ` | "Maintenance on a roof top package unit #heatingandcooling #hvaclife #hvac #hvactraining #" | trade: careers, business and tech life | trade: careers, business and tech life | trade: commercial and refrigeration | rooftop package unit maintenance (commercial); trade either way |
| 4 | `ObvRH5JDOZM` | "The Hidden Reason Your Electric Bill Keeps Rising / The Energy Secret Most Homeowners Never Hear" | energy bills | energy bills | energy bills |  |
| 5 | `DnqOOzIz7ic` | "Hamilton Beach TrueAir Air Purifier - In-depth Review (+ Smoke Test)" | indoor air and purifiers | indoor air and purifiers | indoor air and purifiers |  |
| 6 | `CvH8xDoDvd4` | "Emerson SENSI ST55 / 7-Day Programming Schedule / Digtal WiFi Thermostat" | smart thermostats | smart thermostats | smart thermostats |  |
| 7 | `sz5tjkwGvXg` | "Going Ductless Might NOT Be In Your Best Interest" | mini-split | mini-split | mini-split |  |
| 8 | `heez6VLi4hg` | "Trane     Compressor Change Out" | AC: central | AC: central | AC: central |  |
| 9 | `bHL_oMwztNs` | "7 Things You MUST Do The Moment Your Heat Goes Out (Do #7 FIRST!)" | general: heating (equipment not named) | general: heating (equipment not named) | general: no heat (equipment not named) | 'the moment your heat goes out' |
| 10 | `R9vtoIes4x0` | "HVAC Residential Install Part 2: 80% Furnace" | furnaces | furnaces | furnaces |  |
| 11 | `IoS5BMs5yY8` | "An Air Purifier Without Filters? ▸▸▸ Clarifion Air Ionizer" | filters | indoor air and purifiers | indoor air and purifiers | an ionizer purifier; 'without filters' is the pitch |
| 12 | `cPwYBdTsww0` | "I Got PROMOTED! HVAC Talk + Attic Central AC Install" | drafts, insulation and windows | drafts, insulation and windows | AC: central | a central AC install in the attic; the attic is the location |
| 13 | `X6UvlAmGliM` | "Free Heat from Waste Exhaust Gases Heating Radiator Home Oil Diesel Heater Chinese Recovery Exchange" | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters |  |
| 14 | `f2j7WdlY5bw` | "swamp cooler Repair & Rebuild" | evaporative coolers | evaporative coolers | evaporative coolers |  |
| 15 | `vZKjLiRbtis` | "Wisetack Financing Guide for Hartzell’s Heat and Air" | replacement cost and quotes | replacement cost and quotes | replacement cost and quotes |  |
| 16 | `6sx1qrmGZ0g` | "The WORST AC Units Ever Made (AVOID AT ALL COST!)" | brand verdicts | brand verdicts | brand verdicts |  |
| 17 | `OBiasIlDjRQ` | "Vintage Cast Iron Radiators" | boilers, radiators and steam | boilers, radiators and steam | boilers, radiators and steam |  |
| 18 | `NNYYmyGUWY0` | "The 5 Thermostat Habits That Are Draining Your Wallet Every Month" | thermostats | thermostats | thermostats |  |
| 19 | `E8QuIurpmt4` | "30 Days Without Power in Winter: What Fails Week by Week (A Realistic Timeline)" | heat and power in an outage | heat and power in an outage | heat and power in an outage |  |
| 20 | `hWDFD_I9s2U` | "Mix banana peel with salt and you won’t need to buy gas cylinders anymore! Free energy at home 😱" | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters |  |
| 21 | `feAUrVDhuBo` | "20 Cheap Walmart Items That Become WORTH GOLD When Your Furnace Dies." | furnaces | staying warm without heating (body, bed, clothes) | staying warm without heating (body, bed, clothes) | items for when the furnace dies, not furnace repair |
| 22 | `ezKweiF6YNM` | "Should you use HVAC duct work for an ERV? Responding to a comment. Energy Recovery Ventilator" | ducts and vents | indoor air and purifiers | indoor air and purifiers | the ERV is the subject; the ductwork is the question about it |
| 23 | `GpKeKdETd1I` | "Stop Burning Firewood Like This — You're Wasting Almost Half of It" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces |  |
| 24 | `Hv2y9oAdEKQ` | "Grant Oil Boiler Repair" | oil heat | oil heat | oil heat |  |
| 25 | `y5XV2kp0PiY` | "How to make a very simple wood stove from an old gas cylinder for those who do not know" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: DIY stove builds (cement, barrel, brick craft) | off-grid heat: DIY stove builds (cement, barrel, brick craft) | a stove built from a gas cylinder (DIY stove-build split added after this check; counted as agreeing when read) |
| 26 | `UBDJXU6_1zg` | "Why Does Your Wood Stove Need This Tiny Layer of Ash The Hidden Science of Better Fires." | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces |  |
| 27 | `eic0r6AhCXE` | "Manual D Duct Design by Hand: ACCA HVAC Design Calcs with TEL, Static Pressure, & Friction Rate" | trade: technical training | trade: technical training | trade: technical training |  |
| 28 | `7pA23BGW6QU` | "GOOD and BAD of High SEER Inverter HVAC!" | adjacent: solar, batteries and home energy systems | general: HVAC, topic not named | buy or replace (sizing, repair vs replace, new system) | high-SEER inverter systems: an equipment choice, not solar |
| 29 | `4tRfzOjTV8s` | "How to Keep One Room Cold During a Long Summer Blackout No Power" | heat and power in an outage | heat and power in an outage | heat and power in an outage |  |
| 30 | `5X4q5iL8K4Q` | "20 Heating Sources That Don't Need Electricity Stockpile These Before Winter Hits" | seasonal maintenance | off-grid heat: free-heat tricks and DIY heaters | off-grid heat: free-heat tricks and DIY heaters | heating sources that need no electricity |
| 31 | `TjltfDyVluo` | "Light Your Fireplace Before Checking This and It Could Cost You $3,000 — An Old Bricklayer Warns" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces |  |
| 32 | `Mh2FgUXgp68` | "This $3 Japanese Clay Trick Cools Any Room to 65° — No Electricity, BANNED in 4 States" | thermostats | cooling without AC (tricks, DIY coolers) | cooling without AC (tricks, DIY coolers) | a clay trick that cools a room; 65° is not a thermostat setting |
| 33 | `ovNGqHTRRIk` | "Building a zero carbon energy system with James Murray from Business Green" | adjacent: solar, batteries and home energy systems | adjacent: solar, batteries and home energy systems | adjacent: solar, batteries and home energy systems |  |
| 34 | `kSgLM4HSl_U` | "What A Rookie MISTAKE!! / HVAC Life" | trade: careers, business and tech life | trade: careers, business and tech life | trade: careers, business and tech life |  |
| 35 | `IISH9nTOwN8` | "Important Furnace Maintenance Tip Most Homeowners Don't Know" | furnaces | furnaces | furnaces |  |
| 36 | `cKTFJm7J09w` | "HVAC Vlog: Kitchen Remodel Rough-In" | trade: careers, business and tech life | trade: careers, business and tech life | trade: careers, business and tech life |  |
| 37 | `adrXIOHiKgU` | "DUCTABLE AC REPAIRING HP LP CF PROBLEM STEP BY STEP CHECK // MRACTECH" | AC: central | AC: central | AC: central |  |
| 38 | `48k3AlQLYao` | "Discover the DREO Convection Heater 711s" | AC: portable | space heaters (electric) | space heaters (electric) | a Dreo convection heater, not a portable AC |
| 39 | `MnoXmoU5YR8` | "Best 12000 BTU Air Conditioners ❄: The Complete Round-Up / HVAC Training 101" | trade: technical training | trade: technical training | brand verdicts | a 'best 12000 BTU ACs' round-up; 'HVAC Training 101' is the channel's tag |
| 40 | `N9FZ2l3cOgY` | "Why We Don't Talk About ICFs?? Window Flashings, Air Sealing, & More! / Q&A #6" | drafts, insulation and windows | drafts, insulation and windows | drafts, insulation and windows |  |
| 41 | `3cVbRkEeLWY` | "Genius Man Creates Rocket Stove From Tin Cans! Free Energy For Camping" | RV, van, tent and camping heat or cool | RV, van, tent and camping heat or cool | off-grid heat: free-heat tricks and DIY heaters | a tin-can rocket stove build; camping is the use |
| 42 | `3NVZFAcqDOk` | "Boiler Basics: Part III - External Components" | boilers, radiators and steam | boilers, radiators and steam | boilers, radiators and steam |  |
| 43 | `exM3TGNGnSU` | "HVAC Service- Blower Motor Bracket Repair" | parts homeowners touch | parts homeowners touch | parts homeowners touch |  |
| 44 | `pv_bhBd9wUc` | "HVAC- My Scrap Pile" | general: HVAC, topic not named | general: HVAC, topic not named | trade: careers, business and tech life | a tech's scrap-pile vlog |
| 45 | `matJ5R4VA6I` | "40 Cheap Winter Hacks That Keep Your Home Warm" | staying warm without heating (body, bed, clothes) | staying warm without heating (body, bed, clothes) | staying warm without heating (body, bed, clothes) |  |
| 46 | `BN-uV3R7inc` | "AC + Furnace Replacement Cost in 2026 (Real Numbers)" | replacement cost and quotes | replacement cost and quotes | replacement cost and quotes |  |
| 47 | `6ffHk08yqaQ` | "Heat Pumps vs Gas Boiler Running Costs... The TRUTH" | energy bills | energy bills | energy bills |  |
| 48 | `CxnZrYrdEQc` | "Furnace doesn't blow air - how to fix furnace heater like PRO - step-by-step diagnostic" | space heaters (electric) | furnaces | furnaces | furnace not blowing air; 'furnace heater' is not a space heater |
| 49 | `X0DcioS0FM8` | "DIY Firewood Cover 10-8-2010" | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces | off-grid heat: wood and pellet stoves, fireplaces |  |
| 50 | `HfMwakAYUbM` | "Box Vents vs Ridge Vents: Which Removes More Heat? / Attic Ventilation" | ducts and vents | ducts and vents | drafts, insulation and windows | attic roof vents (box vs ridge), not HVAC ducts or registers |

