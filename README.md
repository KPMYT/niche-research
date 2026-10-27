# Niche research

Research on which niches and channels to make: competitors, audience size, views, framing and emotional triggers. Scripting (the packs, personas, tests and skills) lives in the separate `script-system` repository, which reads from here.

## Rules

- **Collect and describe.** Never edit research data to fit a conclusion. Mark what was checked, by what, and what wasn't.
- **Never delete history.** New research goes in new dated folders.
- **Log every change** in `CHANGELOG.md`: date | files | what changed | why.

## File map

| Path | What it is |
|---|---|
| `CLAUDE.md` | Read first: what this repository is, the layout, the working rules (including the handover and `main`) and how to work with the operator. |
| `SESSION-HANDOVER.md` | Where things stand and what each chat does next; one section per research chat. |
| `RESEARCH-BRIEF.md` | Exactly what the HVAC and electrical niche studies deliver (the channel census, new channels, the sub-niche map, emotions, thumbnail styles, recent winners, the top 100, the keyword sweep, conclusions), the shared labels, sources, rounds and the folder layout. |
| `studies/` | One folder per niche study (`hvac/`, `electrical/`), filled by the research chats. |
| `studies/hvac/` | The HVAC study for Roger the HVAC Guy (HVAC research chat). See its `README.md`. |
| `studies/electrical/` | The electrical study for Frederick Barnes's new brand (or Jack Redfield; channel pinned): the census, new channels, sub-niche map, emotions, thumbnail styles, recent winners, top 100, keyword sweep, formats, the report, `CONCLUSIONS.md`, and `ideation/` (topic heat and proof, recent formats, the 17 confirmed initial ideas). See its `README.md` (research done 2026-10-26; ideation 2026-10-26/27). |
| `ideation/electrical-ideation/` | The electrical ideation skill (thin overlay on `ideation-core`, modelled on `plumbing-ideation`): `SKILL.md` and `references/` (steering with the base ideation plan, audience, demand map, formats with examples, reference titles, word bank, thumbnail niche pack, produced log, dead list). Built 2026-10-27 from `studies/electrical/`. |
| `ideation/dist/electrical-ideation.skill` | The ideation skill packaged for upload (claude.ai, Settings, Capabilities, Skills). |
| `ideation/electrical-ideation-build/` | How the skill was built: the build spec, the checker's report (about 800 figures checked, 17 fixed) and the proposal to register it in `ideation-core` (not applied). |
| `ideation/hvac-ideation/` | The HVAC ideation skill for Roger the HVAC Guy (built 2026-10-27 from the HVAC study; a thin overlay on `ideation-core`, modelled on `script-system/ideation/plumbing-ideation`): `SKILL.md`, `references/` (steering, demand map with the season calendar, reference titles, examples by format, word bank, audience, dead list, produced log, thumbnail niche pack) and `core-proposals.md` (the core and sibling-skill changes it needs, pending the operator's yes). |
| `ideation/thumbnails-upload/` | Draft files for the `thumbnails` skill (HVAC niche file, Roger the HVAC Guy channel file, the index line), to install only after the operator's yes. |
| `findings/2026-10-22-hvac-and-electrical.md` | What the 2026-10-22 research found for Roger the HVAC Guy and Frederick Barnes's electrical brand, quoted from the recovered chats. Not re-checked. |
| `recovered/2026-10-22-roger-sub-brands/` | The full history of the chat "Roger the Pipe Guy sub-brand opportunities" (2026-10-22), recovered from its transcript because its files were never pushed. See its `README.md`. |
| `recovered/2026-10-22-frederick-script-analysis/` | The history of the chat "Frederick Barnes script analysis" (2026-10-22), including the HVAC villain answer that was never saved. See its `README.md`. |
