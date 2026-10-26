#!/usr/bin/env python3
"""Topic heat for the round-1 ideas (operator, 2026-10-26: "when the reference video was posted ... and how many times
topic has been uploaded since on that channel and competitor channels to gauge if topic is still hot").

For each idea in ideation/round-1-ideas.csv:
  - the source video's exact upload date (yt.py video);
  - YouTube search (relevance, views, this year, this month; logged out, US English) on 2-3 topic queries,
    plus the source channel's own Videos tab (latest first, back to the source date);
  - long-form only (5:00+); a title counts as the same topic when it matches every keyword group below (a reading);
  - counts uploaded after the source, in the last 12 months and in the last 90 days, how they did, and the best one.
Search returns a sample, not every upload, so counts are a floor. Relative ages ("2 years ago") are turned into date
ranges; an upload counts as "since the source" only when its whole range is after the source date.
Writes ideation/round-1-heat.csv and ideation/heat-raw/<n>.json. With --extra: the topics in ideation/extra-topics.csv
(dug out of the recent winners) -> ideation/extra-topics-heat.csv."""
import csv, json, os, re, statistics, sys, datetime as dt
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt

S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
TODAY = dt.date(2026, 10, 26)

SPEC = {  # n: (queries, keyword groups: a title must match one pattern from every group)
 1: (["add outlet to finished wall", "add an outlet existing wall"], [r"outlet|receptacle", r"finished wall|existing wall|add(ing)? (an? |new |another )?(electrical )?(outlet|receptacle)|new outlet|extend(ing)? (an? )?outlet"]),
 2: (["short wires electrical box", "extend short wires outlet"], [r"short wire|wires? (are |too )+short|too short|extend(ing)? (short |the )?wires?|wire extension"]),
 3: (["install ceiling light without existing wiring", "add ceiling light no wiring"], [r"ceiling light|light fixture|recessed|can light|pot light|ceiling fixture", r"no (existing )?wir|without (existing |any )?wir|no attic|where there (is|'s) no|add(ing)? (a |new )?(ceiling )?light"]),
 4: (["replace light with ceiling fan", "how to install a ceiling fan"], [r"ceiling fan", r"install|replac|hang|swap|put up"]),
 5: (["replace 2 prong outlet", "2 prong outlet to 3 prong", "ungrounded outlet fix"], [r"2[- ]?prong|two[- ]?prong|ungrounded|no ground"]),
 6: (["how to use a multimeter", "multimeter for beginners"], [r"multi[- ]?meter"]),
 7: (["connect generator to house", "generator interlock kit install", "generator transfer switch install"], [r"generator", r"interlock|transfer switch|inlet|connect|hook ?up|back ?feed|to (your|the|my) house|whole[- ]house"]),
 8: (["install 240v outlet ev charger", "nema 14-50 outlet install", "level 2 ev charger install home"], [r"240|14-50|ev charger|level 2|tesla (wall|charger)", r"install|wire|wiring|add|run"]),
 9: (["how to replace a circuit breaker", "change a bad breaker"], [r"breaker", r"replac|chang|install|swap"]),
 10: (["gfci keeps tripping", "gfci won't reset"], [r"gfci|gfi\b|gfic|ground fault", r"trip|won'?t reset|not reset|will not reset|keeps"]),
 11: (["outlets not working breaker not tripped", "outlet stopped working"], [r"outlet|receptacle|plug", r"not working|dead|no power|stopped working|won'?t work|quit working"]),
 12: (["plug won't stay in outlet", "loose outlet plug falls out"], [r"won'?t stay|falls? out|falling out|loose (outlet|plug|receptacle)|worn (out )?(outlet|receptacle)"]),
 13: (["breaker keeps tripping", "why does my breaker keep tripping"], [r"breaker", r"keeps? trip|tripping|trips"]),
 14: (["led bulb glows when switched off", "led light glowing when off"], [r"led|bulb|light", r"glow|ghost|dim(ly)? (when|after)|stays? on|when (switched |turned )?off|flicker"]),
 15: (["ceiling fan slow", "ceiling fan humming noise", "ceiling fan wobble fix"], [r"fan", r"slow|hum|wobbl|capacitor|noise|not spinning|won'?t spin"]),
 16: (["light switch not working", "light switch troubleshooting"], [r"switch", r"not working|doesn'?t work|stopped|troubleshoot|diagnos|bad switch|won'?t work|fix"]),
 17: (["getting shocked from faucet", "why am i getting shocked", "shock from appliance"], [r"shock|tingl|electrified|electrocut", r"faucet|sink|tap|appliance|washer|fridge|why|getting|water|shower|metal|touch"]),
 18: (["wire nut vs wago", "push in connectors vs wago"], [r"wago|wire ?nut|push[- ]?in|lever (nut|connector)", r"vs\.?|versus|which|best|better|test|fail|compar|differen"]),
 19: (["volts or amps kill", "volts vs amps"], [r"volt", r"amp"]),
 20: (["where does ground electricity go", "ground wire explained"], [r"\bground|earth", r"where|what|why|explain|how|go\b"]),
 21: (["what does the neutral wire do", "neutral wire explained"], [r"neutral"]),
 22: (["circuit breaker doesn't protect people", "breaker vs gfci shock protection"], [r"breaker|gfci", r"protect|shock|save|people|electrocut|kill"]),
 23: (["afci vs gfci", "afci breaker explained"], [r"afci|arc[- ]fault|cafci"]),
 24: (["why 2 prong outlets not allowed", "two prong outlets dangerous", "are 2 prong outlets legal"], [r"2[- ]?prong|two[- ]?prong|ungrounded|three[- ]prong|3[- ]prong", r"why|allowed|legal|code|dangerous|safe|banned|still|reason|grandfather"]),
 25: (["why do plugs have holes", "holes in plug prongs"], [r"hole", r"plug|prong"]),
 26: (["wire overheating in wall", "loose electrical connection overheating", "what happens when wires overheat"], [r"overheat|hot wire|melt|burn|loose connection|arcing|arc fault|scorch", r"wire|wiring|wall|outlet|connection"]),
 27: (["fake wago connectors", "wago copy test", "counterfeit wago"], [r"wago|lever (nut|connector)", r"fake|copy|counterfeit|knock[- ]?off|clone|cheap|amazon|real|original|test"]),
 28: (["how does a circuit breaker work", "circuit breaker explained"], [r"breaker|mcb", r"how|work|explain|inside|slow motion"]),
 29: (["outlet wiring mistakes", "receptacle wiring mistakes"], [r"outlet|receptacle|switch", r"mistake|wrong|error|fail"]),
 30: (["electrical panel mistakes", "breaker box mistakes"], [r"panel|breaker box|load cent|fuse box|consumer unit", r"mistake|wrong|violation|dangerous|fail"]),
 31: (["generator backfeed danger", "generator mistakes", "suicide cord generator"], [r"generator", r"back ?feed|mistake|suicide|dryer outlet|danger|kill|lineman|never|don'?t|wrong"]),
 32: (["backstab outlet", "push in wire outlet", "stop using backstab"], [r"back ?stab|push[- ]?in|quick[- ]?wire|stab[- ]?in|back[- ]?wir"]),
 33: (["electrical things every homeowner should know", "electrical tips for homeowners"], [r"homeowner|every home|everyone|should know|need to know|wish i knew|tips|hacks|tricks", r"electric"]),
 101: (["history of electricity in homes", "before circuit breakers", "history of electrical wiring"], [r"history|before|early|victorian|forgotten|old[- ]?time|invent|1900|19th|century|origin"]),
 102: (["light bulbs to get rid of", "dangerous light bulbs", "worst light bulbs"], [r"bulb", r"get rid|stop using|dangerous|worst|never|throw|avoid|replace|toxic|research|harm"]),
 103: (["identify circuits label panel", "breaker finder", "map electrical circuits"], [r"circuit|breaker", r"identify|label|map|find(er|ing)?|which breaker|trace|tracer|locat"]),
 104: (["sunken outlet fix", "outlet loose in wall", "outlet box extender"], [r"outlet|receptacle", r"sunken|recessed|loose in|wobbl|spacer|extender|too deep|sticking out|not flush"]),
 105: (["led flickering dimmer", "led lights flickering fix", "led dimmer strobing"], [r"led|light|bulb|dimmer", r"flicker|strob|buzz|dimmer"]),
 106: (["junction box mistakes", "junction box code", "junction box wiring"], [r"junction box|j[- ]box|electrical box", r"mistake|wrong|code|never|don'?t|danger|fire|hidden|buried|right way"]),
 107: (["electrical upgrades new home", "electrical upgrades worth it", "new build electrical must haves"], [r"electric|outlet|wiring", r"upgrade|new (home|house|build)|build(ing)? a|must[- ]have|regret|wish"]),
 108: (["3 way switch wiring", "how 3 way switches work"], [r"3[- ]?way|three[- ]?way"]),
 109: (["electrical tape wrong", "how to use electrical tape"], [r"electrical tape|tape"]),
 110: (["run power to shed", "run electrical to detached garage", "shed electrical wiring"], [r"shed|garage|outbuilding|barn|workshop", r"power|electric|wire|wiring|run|subpanel|sub[- ]panel"]),
 111: (["generator bonded neutral", "floating neutral generator", "generator neutral ground bond"], [r"bond|neutral|float", r"generator"]),
 112: (["how home electricity works", "how electricity gets to your home", "home electrical system explained"], [r"electric", r"home|house|works|explained|journey|grid|system"]),
 113: (["loose neutral", "lost neutral symptoms", "open neutral"], [r"neutral", r"loose|lost|open|bad|broken|symptom|flicker"]),
 34: (["test gfci outlet monthly", "home electrical safety check", "electrical maintenance homeowner"], [r"test(ing)? (your |a |the )?(gfci|gfi|outlets?)|electrical (safety )?(check|inspection|maintenance)|maintenance|check (your|these)", r"electric|gfci|gfi|outlet|panel|breaker"]),
}
SORTS = [("relevance", 3), ("views", 3), ("year", 4), ("month", 2)]

def secs(d):
    if not d: return 0
    p = [int(x) for x in d.split(":")]
    return sum(v * 60 ** i for i, v in enumerate(reversed(p)))

UNIT = {"second": 1 / 86400, "minute": 1 / 1440, "hour": 1 / 24, "h": 1 / 24, "day": 1, "d": 1, "week": 7, "w": 7, "month": 30.44, "mo": 30.44, "year": 365.25, "y": 365.25}
def age_range(a):
    """'3 years ago' / '3y ago' -> (earliest, latest) possible upload date."""
    if not a: return None
    m = re.search(r"(\d+)\s*(second|minute|hour|day|week|month|year|mo|h|d|w|y)s?\b", a)
    if not m: return None
    n, u = int(m.group(1)), UNIT[m.group(2)]
    return TODAY - dt.timedelta(days=(n + 1) * u), TODAY - dt.timedelta(days=n * u)

MON = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
def exact_date(s):
    m = re.search(r"([A-Z][a-z]{2}) (\d{1,2}), (\d{4})", s or "")
    return dt.date(int(m.group(3)), MON[m.group(1)], int(m.group(2))) if m else None

def matches(title, groups):
    t = (title or "").lower()
    return all(re.search(g, t) for g in groups)

def one(idea):
    n = int(idea["n"]); qs, groups = SPEC[n]
    src = yt.video(idea["source_id"]); sdate = exact_date(src.get("date"))
    found = {}
    for q in qs:
        for sort, pages in SORTS:
            try:
                for v in yt.search(q, sort, pages, "video"): found.setdefault(v["id"], dict(v, via=f"search:{sort}"))
            except Exception as e: print("search fail", n, q, sort, e, file=sys.stderr)
    own = []
    try:  # source channel, latest first, until older than the source
        ch = yt.channel(src.get("channel_id") or idea["source_id"], "latest", 1)
        own = ch.get("videos", [])
        pages = 1
        while own and pages < 25:
            r = age_range(own[-1].get("age"))
            if r and sdate and r[1] < sdate: break
            pages += 1; ch = yt.channel(src["channel_id"], "latest", pages);
            if len(ch.get("videos", [])) <= len(own): break
            own = ch["videos"]
        for v in own: found.setdefault(v["id"], dict(v, via="channel"))
    except Exception as e: print("channel fail", n, e, file=sys.stderr)
    rows = []
    for v in found.values():
        if v["id"] == idea["source_id"] or not matches(v.get("title"), groups) or secs(v.get("dur")) < 300: continue
        r = age_range(v.get("age"))
        if not r: continue
        v["earliest"], v["latest"] = r[0].isoformat(), r[1].isoformat()
        v["since"] = bool(sdate and r[0] >= sdate)
        v["last12"] = r[0] >= TODAY - dt.timedelta(days=365)
        v["last90"] = r[0] >= TODAY - dt.timedelta(days=90)
        v["same_channel"] = v.get("channel_id") == src.get("channel_id")
        rows.append(v)
    def stats(L):
        vs = [x["views"] for x in L if x.get("views") is not None]
        best = max(L, key=lambda x: x.get("views") or 0) if L else None
        return dict(n=len(L), median=int(statistics.median(vs)) if vs else None, over100k=sum(1 for x in vs if x >= 100_000),
                    best=(f'{best["title"]} | {best.get("channel")} | {best.get("views")} | {best.get("age")}' if best else ""))
    since = [x for x in rows if x["since"]]
    out = dict(n=n, source_id=idea["source_id"], source_date=sdate.isoformat() if sdate else src.get("date"), source_views_now=src.get("views"),
               source_channel_id=src.get("channel_id"),
               since_all=len(since), since_same=sum(1 for x in since if x["same_channel"]), since_others=sum(1 for x in since if not x["same_channel"]),
               **{f"y12_{k}": v for k, v in stats([x for x in rows if x["last12"]]).items()},
               **{f"d90_{k}": v for k, v in stats([x for x in rows if x["last90"]]).items()},
               same_titles=" ; ".join(f'{x["title"]} ({x.get("views")}, {x.get("age")})' for x in since if x["same_channel"])[:1500])
    json.dump(dict(summary=out, matched=rows, pool=len(found)), open(os.path.join(S, "ideation", "heat-raw", f"{n}.json"), "w"), indent=1, ensure_ascii=False)
    print("done", n, out["since_all"], out["y12_n"], file=sys.stderr)
    return out

if __name__ == "__main__":
    os.makedirs(os.path.join(S, "ideation", "heat-raw"), exist_ok=True)
    extra = len(sys.argv) > 1 and sys.argv[1] == "--extra"
    args = sys.argv[2:] if extra else sys.argv[1:]
    ideas = list(csv.DictReader(open(os.path.join(S, "ideation", "extra-topics.csv" if extra else "round-1-ideas.csv"))))
    only = set(int(x) for x in args)
    if only: ideas = [i for i in ideas if int(i["n"]) in only]
    with ThreadPoolExecutor(6) as ex: res = list(ex.map(one, ideas))
    res.sort(key=lambda r: r["n"])
    p = os.path.join(S, "ideation", "extra-topics-heat.csv" if extra else "round-1-heat.csv")
    old = {int(r["n"]): r for r in csv.DictReader(open(p))} if os.path.exists(p) and only else {}
    for r in res: old[r["n"]] = r
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys())); w.writeheader()
        for k in sorted(old): w.writerow(old[k])
