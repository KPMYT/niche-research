# Checker brief: electrical video briefs (2026-10-27)

You are the second helper. Another helper drafted video briefs under the spec in `SPEC.md` (same folder as this file); read it first. Helpers' reports can be wrong: your job is to find what is wrong before the operator sees it.

For each brief in the file(s) you are given:
1. **Facts.** Check every factual claim: code rules and NEC article numbers (2023 NEC), mechanisms, voltages, distances, product facts, safety statements. Use web search (cap: about 25 searches for you in total), preferring primary or code-focused sources (NFPA, Mike Holt, IAEI, EC&M, CPSC, OSHA, CDC, manufacturer instructions, utilities). Mark each problem: WRONG (false or misleading), UNSUPPORTED (can't verify; say what you tried), or OK. Don't nitpick wording that is true.
2. **Safety.** Anything that could lead a DIYer into danger if a script repeats it (missing power-off/verify-dead, bad advice, a job that needs an electrician stated as DIY).
3. **Spec.** 200-300 words; one paragraph; facts only (flag ANY structural, editing, format, tone or script direction, e.g. "open with", "show", "the hook"); no prices or money; no claims the channel tested or demonstrated anything; no persona claims; listicles have exactly the promised number of items; fire as a consequence only; US terms.
4. **Title backing.** Does the brief give honest facts behind the title's claim? Note where the title overstates.
5. **Fix.** For every WRONG, UNSUPPORTED (where it matters) or spec problem, write a corrected brief. Change only what's needed; keep the rest word for word.

Output: write `<your folder>/check.json`, a list of `{"key": "...", "verdict": "ok" | "fixed", "issues": [{"claim": "quoted text", "status": "WRONG|UNSUPPORTED|SPEC|SAFETY", "why": "...", "source": "url"}], "corrected_brief": "the full corrected paragraph (or the original if ok)", "word_count": N}`. Work only inside your own folder; don't touch the git repository. Final message: one line per key (verdict, number of issues, the most important one).
