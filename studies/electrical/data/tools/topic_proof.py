#!/usr/bin/env python3
"""Topic proof (operator's rule, 2026-10-26): a topic is proven only if at least one on-topic long-form video has
300K+ views on a faceless channel (AI personas count as faceless) or 1M+ on a real, on-camera channel. Any upload date.
Candidates: every video of 300K+ that topic_heat.py matched and a helper judged on topic (heat-judged.csv,
heat-judged-300k.csv), plus each topic's source video (proof-candidates.json). Channel types: the study's census
(channels.csv) where it has the channel, otherwise ideation/channel-types.csv (helpers, NexLev check_faceless_channel).
Unclear and organisation/brand channels get the stricter 1M bar. Writes ideation/topic-proof.csv."""
import csv, json, os

S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
I = os.path.join(S, "ideation")

def norm(t):
    t = (t or "").lower()
    if "ai persona" in t or "faceless persona" in t or t == "ai_persona": return "ai_persona"
    if "faceless" in t: return "faceless"
    if "on camera" in t or t == "real": return "real"
    return "unclear"

types = {r["channel_id"]: norm(r["type"]) for r in csv.DictReader(open(os.path.join(S, "channels.csv")))}
for r in csv.DictReader(open(os.path.join(I, "channel-types.csv"))):
    types.setdefault(r["channel_id"], norm(r["type"]))
names = {int(r["n"]): r["topic"] for r in csv.DictReader(open(os.path.join(I, "topic-heat.csv")))}
cand = json.load(open(os.path.join(I, "proof-candidates.json")))

# Main session's review of the proofs (2026-10-26): these "proofs" are off topic, so the topic is not proven on them.
NOT_PROOF = {(34, "9hlo87E_GdQ"): "the stand-in source (an electrical tricks video), not yearly checks",
             (107, "-Jk4xNnLJhQ"): "a 200-amp service upgrade, not upgrades for a new home"}

def bar(t): return 300_000 if t in ("faceless", "ai_persona") else 1_000_000

out = []
for n in sorted(names):
    seen, ok = set(), []
    for c in cand:
        if c["topic"] != n or c["video_id"] in seen: continue
        if (n, c["video_id"]) in NOT_PROOF or (n == 107 and "200-Amp" in (c["title"] or "")): continue
        seen.add(c["video_id"]); t = types.get(c["channel_id"], "unclear")
        if c["views"] >= bar(t): ok.append(dict(c, ctype=t))
    ok.sort(key=lambda c: -c["views"])
    fac = [c for c in ok if c["ctype"] in ("faceless", "ai_persona")]
    def show(c): return f'{c["title"]} | {c["channel"]} ({c["ctype"]}) | {c["views"]:,} | {c["age"]}' if c else ""
    out.append(dict(n=n, topic=names[n], proven="yes" if ok else "no", proof_videos=len(ok), faceless_proofs=len(fac),
                    best_proof=show(ok[0] if ok else None), best_faceless_proof=show(fac[0] if fac else None),
                    all_proofs=" ; ".join(show(c) for c in ok[:8])))
with open(os.path.join(I, "topic-proof.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out:
    print(f'{r["n"]:>3} {r["proven"]:<3} {r["proof_videos"]:>2} ({r["faceless_proofs"]} faceless) | {r["topic"][:38]:<38} | {r["best_proof"][:110]}')
