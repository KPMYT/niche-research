# Brief spec: electrical channel, 17 initial ideas (2026-10-27)

You are drafting video briefs for a long-form (8-17 min) YouTube channel on home electrical DIY and safety, aimed at US homeowners (many 50+). The presenter is an AI persona whose background stays mostly unspoken (a retired electrician when it has to be said). The briefs go into a spreadsheet and a scriptwriter writes the script from them.

## What a brief is (house rules, followed for every niche)
- **Facts only: talking points and content context.** The items, mechanisms, steps, materials, specs, code rules, cautions and "why" a scriptwriter needs. **No structural direction, no editing direction, no format direction, no tone/language/script direction.** Never write "open with", "the hook is", "show", "cut to", "B-roll", "in the script", "the video should", "end with", "tease", "the viewer will feel". Just the facts and points.
- **One flowing paragraph, 200-300 words.** No line breaks, no bullets. Numbered items inline like "1) ... 2) ..." are fine for listicles.
- **The honest mechanism lives in the brief.** Every big claim in the title must be backed by defensible facts in the brief (e.g. "can kill the lineman": explain how backfeed reaches a transformer and is stepped up).
- **Listicle titles:** the brief must give exactly the number of items the title promises (7, 10, 9, 3...).
- **Safety boundaries** where relevant: power off at the breaker and verified dead with a tester before touching wires; when it's a job for a licensed electrician or needs a permit; local code may differ from the NEC and the local inspector has the final say. Keep them factual, one or two clauses.
- **Code citations:** cite the NEC (2023 edition) article where a rule comes from (e.g. NEC 300.14) only when you have verified it in a source. If unsure of an article number, describe the rule without the number.

## Operator rules for this channel
- **No money framing.** Do not give dollar prices, costs or savings. ("we dont really need to use money in electrical.")
- **Fire is the stakes, never the topic.** Overheating, arcing and fire risk can be named as consequences; no fire-prevention topics.
- **No demonstrations claimed.** Nothing that says the channel tested, burned, measured or filmed something. Explain, don't demonstrate. Referencing well-known facts or manufacturer data is fine.
- **No persona claims** (no "in my 40 years"). Facts only.
- US terms and US code (120/240 V, NEC, NEMA). No UK wording.

## How to work
1. For each of your ideas, pull the reference video's transcript with the NexLev tool `get_video_transcript` (load it via ToolSearch "select:mcp__NexLev__get_video_transcript"; if it fails, try `get_video_subtitle`, or `watch_youtube_video_and_ask` with a question asking for every talking point in order). Note every talking point the reference covers: our video "takes and improves on" the top video, so the brief should cover what the reference covers, corrected where it's wrong, plus what it misses.
2. Check facts with web search (cap: about 25 searches for you in total). Prefer primary sources: NFPA/NEC text or summaries from code-focused sites (e.g. Mike Holt, IAEI, ecmweb), CPSC, OSHA, manufacturer instructions (Leviton, Ideal, Wago, Generac, Reliance, Square D, Eaton), utilities.
3. Write each brief per the spec.

## Output
Write ONE file: `<your folder>/briefs.json`, a list of objects:
`{"key": "A1", "title": "...", "reference_points": "short summary of what the reference video covers, in order", "brief": "the 200-300 word paragraph", "sources": ["url — what it supports", ...], "doubts": "anything you could not verify or think the operator should know (e.g. title claim that's hard to back)"}`
Work only inside your own folder. Do not touch the git repository. Your final message: a short summary (one line per idea: key, word count, any doubt).
