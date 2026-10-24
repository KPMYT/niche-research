p='/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/build.py'
s=open(p).read()
s=s.replace('''# per side: dict id -> video (max views seen)''','''# collab rows ("X and Y" / "X and 3 more") carry no channelId: map to the first-named channel when it is known
NAME2ID = {}
for r in rows:
    for v in r["rows"]:
        if v.get("channelId") and v.get("channel"): NAME2ID.setdefault(v["channel"], v["channelId"])
for r in rows:
    for v in r["rows"]:
        if not v.get("channelId") and v.get("channel"):
            m = re.match(r"(.+?) and (\\d+ more|.+)$", v["channel"])
            if m and m.group(1) in NAME2ID:
                v["collab"] = v["channel"]; v["channel"] = m.group(1); v["channelId"] = NAME2ID[m.group(1)]
            else:
                v["collab"] = v["channel"]; v["channelId"] = "collab:" + v["channel"]
# per side: dict id -> video (max views seen)''')
open(p,'w').write(s)
