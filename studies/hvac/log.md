# HVAC study log

## Round 1: seeds (started 2026-10-23)

- **Plan approved** by the operator 2026-10-23 ("go and find more channels too"), with the two scope decisions in `README.md`.
- **Helpers:** puller (Silver Cymbal), re-check of the 8 known channels, keyword builder, channel finder; then labeller and up-next harvester once the seed list lands; then a checker.
- **Puller done (2026-10-23):** Silver Cymbal has 538 videos on the Videos tab (321 at 5 minutes or more). 22 long-form seed videos; baseline = median of his 18 long-form uploads in the last 12 months, 79,807 views. Popular and Oldest sorts verified complete; Latest needed the sort chip. The watch page and player endpoint are blocked from the cloud, so lengths come from NexLev; NexLev's channel video list has guessed dates and a wrong video count, so it isn't used for dates. 19 borderline videos left for the operator. Output `seeds/silver-cymbal.md`.
- **Started:** labeller (seeds and `labels.md`), up-next harvester (via the innertube /next endpoint, which works).
