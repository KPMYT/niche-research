exec(open('/tmp/claude-0/-home-user/d458a124-a50e-58e9-88d0-4274a40ceaa0/scratchpad/oldheat/tables.py').read().split('print("## pool")')[0])
READ = {
 "Ripped Off Britain": "faceless, graphics (no persona)",
 "Weirdward Bound": "faceless, AI-illustrated old craftsman; history story",
 " Fred - Money Historian": "faceless, cartoon mascot; money/news",
 "WiseMoney": "faceless, AI-made presenter image",
 "Sketchy Survival": "faceless, illustration",
 "Sylvie Mercer": "faceless persona, AI woman at a radiator",
 "The Old House Fix": "faceless persona, AI old man bleeding a radiator",
 "Handy Leo": "faceless persona, AI man (copies The DIY Guy's title)",
 "Arthur Weber": "faceless persona, AI old man in work clothes, '(The German Way)'",
 "Building Secrets": "faceless persona, AI old man in a 'Steam Heating Pro' cap",
 "Forgotten Survival": "faceless, AI image",
 "Halden Row": "faceless persona, AI old man",
 "Walt's Workshop": "faceless persona, AI old man in flannel",
 "Prime Energy UK": "faceless, AI old man; drama story series",
 "Simple Savings at Home": "faceless persona, AI woman",
 "Underwritten": "faceless, graphics; money/news",
 "Faded Labels": "faceless, AI image; history story",
 "Quarter Turn": "faceless, graphic",
 "brother Q": "faceless, icon graphic",
 "Boiler Room Detective": "faceless; mix of text cards and an illustrated cap-wearing man with a detective mascot logo",
}
H = jsonable(res['heat']['vids'])
print("| Channel | Subs (About) | Joined | Title (original) | Views | Age | Length | Type (my reading, from thumbnail) |")
print("|---|---|---|---|---|---|---|---|")
rowsout = []
for v in H:
    name = v.get('collab') or v['channel'] or ''
    key = next((k for k in READ if name.startswith(k) or (v['channel'] or '').startswith(k)), None)
    if not key: continue
    a = A.get(v['channelId'], {})
    rowsout.append(f"| {name.strip()} | {a.get('subscriberCountText','not found')} | {a.get('joinedDateText','not found').replace('Joined ','')} | {(v['orig_title'] or v['title']).replace('|','/')} | {fmt(v['views_n'])} | {v['age']} | {v['length']} | {READ[key]} |")
print("\n".join(rowsout))
