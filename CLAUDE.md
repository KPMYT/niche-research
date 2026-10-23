# Niche research: read this first

This repository holds the research behind the operator's YouTube channels: which niches and channels to make, the competitors, audience size, topics, emotions, thumbnails and titles. It also holds the ideation work built from that research (ideation skills, base ideation plans and thumbnail plans). The scripting library (niche packs, personas, the script tests and the script skills) lives in the separate `KPMYT/script-system` repository. Keep the two apart: "keep niche reserach and scripting in seperate repos."

Read `SESSION-HANDOVER.md` (where things stand and which chat does what) first, then `RESEARCH-BRIEF.md` (exactly what each niche study delivers and how), `README.md` (what each file is) and `CHANGELOG.md`.

## Layout

- `studies/<niche>/`: one folder per niche study (for example `studies/hvac/`, `studies/electrical/`), laid out as `RESEARCH-BRIEF.md` says.
- `findings/`: short dated notes that pull conclusions together across studies.
- `recovered/`: chat histories recovered from transcripts. Read-only.
- `ideation/` (when built): ideation skills and plans, modelled on `script-system/ideation/`.

## Working rules

1. **Never change a rule, a file another chat owns, or a skill without the operator's explicit yes to that specific change.** Show the exact change first. "never change skills without me knowing. or approving. you always default to me."
2. **Collect and describe.** Never edit research data to fit a conclusion. Every figure says where it came from (NexLev, a YouTube page, a script's count) and when it was pulled. Mark what is measured and what is your reading. Never fill a gap with a guessed number: write "not found".
3. **Check helpers' work.** Have a second helper re-check a sample of every list against the source before it's reported to the operator. Helpers' reports can be wrong.
4. **Log every change** in `CHANGELOG.md`: date | files | what changed | why.
5. **Never delete history.** New rounds go in new files or dated folders; old ones are kept.
6. **Keep `README.md`'s file map current** whenever files are added or renamed.
7. **Parallel chats stay in their own folder.** A niche chat writes only inside `studies/<its niche>/` (and, later, its own `ideation/` folder), plus one row per change in `CHANGELOG.md`, its own lines in `README.md` and its own section of `SESSION-HANDOVER.md`. When merging, keep both sides of every shared file.
8. **Handover and `main`.** `main` is the shared branch every new chat starts from. Work on the chat's own branch. At every handover (the operator says when), rewrite your section of `SESSION-HANDOVER.md`, log it, commit, then merge the chat's branch into `main` and push `main`. The operator has given standing permission for this push. Never force-push `main` and never delete branches.
9. **Commit and push as work lands,** so nothing lives only in a chat. (The 2026-10-22 research chat never pushed, and its files had to be recovered from its transcript.)

## How to work with the operator

- The operator is not technical. Explain plainly, do the Claude Code and git steps for them, and keep messages short, with numbered items they can answer "1 yes, 2 no". Tables help.
- They want depth, real data and examples: quoted titles, view counts, counts, before and after.
- When an answer is genuinely ambiguous, state your reading and ask once.
- Use many helpers in parallel for wide research, split into rounds. Web search is capped at about 200 searches a round, shared by all helpers; NexLev and direct YouTube page loads don't count against it.
- Use waiting time, and commit helpers' work as it lands.
