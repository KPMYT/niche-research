# HVAC study log

## Round 1: seeds (started 2026-10-23)

- **Plan approved** by the operator 2026-10-23 ("go and find more channels too"), with the two scope decisions in `README.md`.
- **Helpers:** puller (Silver Cymbal), re-check of the 8 known channels, keyword builder, channel finder; then labeller and up-next harvester once the seed list lands; then a checker.
- **Puller done (2026-10-23):** Silver Cymbal has 538 videos on the Videos tab (321 at 5 minutes or more). 22 long-form seed videos; baseline = median of his 18 long-form uploads in the last 12 months, 79,807 views. Popular and Oldest sorts verified complete; Latest needed the sort chip. The watch page and player endpoint are blocked from the cloud, so lengths come from NexLev; NexLev's channel video list has guessed dates and a wrong video count, so it isn't used for dates. 19 borderline videos left for the operator. Output `seeds/silver-cymbal.md`.
- **Started:** labeller (seeds and `labels.md`), up-next harvester (via the innertube /next endpoint, which works).
- **Known-channel re-check done (2026-10-23):** all 8 exist and the old chat's quoted hits are on the right channels. Corrections: the old 6.8-7.2 "RPM" is NexLev's niche base, not the channels' (NexLev blended RPM 2.07-3.04 for all 8; batch tool 3.72-5.99); The DIY HVAC Guy is on camera, so not "8 faceless"; Vent Exposed is dormant since 2026-05-30 and not monetized; HVAC Exposed's hits are from Feb-Mar 2026 and recent uploads are small; Hank Cole has switched mostly to cars; the right Gus Whitaker is @GusWhitakerr. NexLev money figures are a stored snapshot (updated Oct 7-20). 23 more channels in its Leads. Output `seeds/known-channels-recheck.md`.
