#!/usr/bin/env python3
"""Recount topic heat after the on-topic check (2026-10-26).
topic_heat.py matched titles by keywords; three helpers then judged every matched title (since the source or in the
last 12 months) as on topic or not (ideation/heat-judged.csv). Non-Latin-script titles are dropped as not English.
Writes ideation/topic-heat.csv: one row per topic (round-1 ideas 1-34, deeper topics 101-113) with the cleaned counts
and a heat label (reading; rule below)."""
import csv, json, os, re, statistics

S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ideation")
PARTIAL = {1, 6, 9, 11, 14, 22, 24, 26, 30, 32, 101, 104, 105, 109}  # some page loads failed: counts are a floor
NONLATIN = re.compile(r'[ऀ-෿؀-ۿ฀-๿က-႟぀-ヿ一-鿿가-힯Ѐ-ӿ]')

judged = {(int(r["topic"]), r["video_id"]): r["on_topic"].strip().lower() == "y" for r in csv.DictReader(open(os.path.join(S, "heat-judged.csv")))}
names = {int(r["n"]): r["our_title"] for r in csv.DictReader(open(os.path.join(S, "round-1-ideas.csv")))}
names.update({int(r["n"]): r["topic"] for r in csv.DictReader(open(os.path.join(S, "extra-topics.csv")))})
SHORT = {1: "Adding an outlet to a finished wall", 2: "Wires too short in the box", 3: "Ceiling light where there's no wiring",
         4: "Replacing a light with a ceiling fan", 5: "Replacing 2-prong outlets", 6: "Using a multimeter at home",
         7: "Connecting a generator to the house", 8: "240V outlet for an EV charger", 9: "Replacing a circuit breaker",
         10: "GFCI keeps tripping", 11: "Outlets dead, breaker not tripped", 12: "Plug won't stay in the outlet",
         13: "Breaker keeps tripping", 14: "LED bulbs glowing when switched off", 15: "Ceiling fan slow, humming or wobbling",
         16: "Light switch not working", 17: "Shocks from a faucet or appliance", 18: "Wire nut vs Wago vs push-in",
         19: "Volts vs amps", 20: "Where ground electricity goes", 21: "What the neutral wire does",
         22: "Breakers don't protect people from shock", 23: "AFCI vs GFCI", 24: "Why 2-prong outlets aren't allowed",
         25: "Holes in plug prongs", 26: "Wires overheating inside the wall", 27: "Fake vs real Wago",
         28: "How a circuit breaker works", 29: "Outlet wiring mistakes", 30: "Breaker panel mistakes",
         31: "Generator backfeed and mistakes", 32: "Push-in (backstab) outlet wiring", 33: "Electrical basics every homeowner should know",
         34: "Yearly electrical safety checks"}
for k, v in SHORT.items(): names[k] = v

def label(n12, med, big):
    """Heat label (main session's rule): Hot, few uploads = 5 or fewer on-topic uploads found in 12 months, typically 10,000+;
    Quiet = 5 or fewer, typically under 10,000 (little new supply, untested); Hot = a 100K+ upload in 12 months and a
    typical 12-month upload of 1,000+; Warm = one of the two; Cold = more than 5 uploads, none over 100K, typical under 1,000."""
    if n12 <= 5: return "Hot, few uploads" if med >= 10000 else "Quiet"
    if big and med >= 1000: return "Hot"
    if big or med >= 1000: return "Warm"
    return "Cold"

out = []
for fn in sorted(os.listdir(os.path.join(S, "heat-raw")), key=lambda f: int(f.split(".")[0])):
    d = json.load(open(os.path.join(S, "heat-raw", fn))); s = d["summary"]; n = s["n"]
    ok = [v for v in d["matched"] if (v["since"] or v["last12"]) and not NONLATIN.search(v.get("title") or "") and judged.get((n, v["id"]), False)]
    def st(L):
        vs = [v["views"] for v in L if v.get("views") is not None]
        b = max(L, key=lambda v: v.get("views") or 0) if L else None
        return len(L), (int(statistics.median(vs)) if vs else 0), sum(1 for x in vs if x >= 100_000), b
    since = [v for v in ok if v["since"]]
    n12, med12, big12, best12 = st([v for v in ok if v["last12"]])
    n90, med90, big90, _ = st([v for v in ok if v["last90"]])
    out.append(dict(n=n, topic=names[n], source_id=s["source_id"], source_date=s["source_date"], source_views_now=s["source_views_now"],
                    since_total=len(since), since_same_channel=sum(1 for v in since if v["same_channel"]), since_other_channels=sum(1 for v in since if not v["same_channel"]),
                    last12_uploads=n12, last12_typical_views=med12, last12_over_100k=big12,
                    last12_best=(f'{best12["title"]} | {best12.get("channel")} | {best12.get("views")} | {best12.get("age")}' if best12 else ""),
                    last12_best_title=best12["title"] if best12 else "", last12_best_channel=best12.get("channel") if best12 else "",
                    last12_best_views=best12.get("views") if best12 else "", last12_best_age=best12.get("age") if best12 else "",
                    last90_uploads=n90, last90_typical_views=med90,
                    heat=label(n12, med12, big12), partial="yes" if n in PARTIAL else "",
                    same_channel_titles=" ; ".join(f'{v["title"]} ({v.get("views")}, {v.get("age")})' for v in since if v["same_channel"])))
with open(os.path.join(S, "topic-heat.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out:
    print(f'{r["n"]:>3} {r["heat"]:<5} {r["partial"]:<3} src {r["source_date"]} since {r["since_total"]:>3} ({r["since_same_channel"]}) | 12mo {r["last12_uploads"]:>3} typ {r["last12_typical_views"]:>7,} 100K+ {r["last12_over_100k"]} | 90d {r["last90_uploads"]:>3} | {r["last12_best"][:70]}')
