p='/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/build.py'
s=open(p).read()
s=s.replace('''rows = [json.loads(l) for l in open(S + "search.jsonl")]''','''rows = [json.loads(l) for l in open(S + "search.jsonl")]
OE = {}
for l in open(S + "oembed.jsonl"):
    j = json.loads(l)
    if j.get("orig_title"): OE[j["id"]] = j["orig_title"]''')
s=s.replace('''            if not english(v["title"]): continue''','''            ot = OE.get(v["id"], v["title"])
            if not english(ot) or not english(v["channel"] or "") or not english(v["title"]): continue''')
s=s.replace('''d = vids.setdefault(v["id"], dict(v, views_n=vw,''','''d = vids.setdefault(v["id"], dict(v, orig_title=OE.get(v["id"]), translated=(v["id"] in OE and OE[v["id"]] != v["title"]), views_n=vw,''')
open(p,'w').write(s)
