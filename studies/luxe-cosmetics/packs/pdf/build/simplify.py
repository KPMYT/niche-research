import re, sys
src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding='utf-8').read().split('\n')
DROP = re.compile(r'^(#{1,3}) .*?(Contents|Sources|What I could not get|What could not be found|could not be found or read|Gaps and limits|Gaps|What was collected|Not found / open items)\b', re.I)
out = []; skip_level = None
# drop everything before "# Part 1"
start = next(i for i, l in enumerate(lines) if l.startswith('# Part 1'))
lines = lines[start:]
for l in lines:
    m = re.match(r'^(#{1,6}) ', l)
    if m:
        lvl = len(m.group(1))
        if skip_level is not None and lvl <= skip_level:
            skip_level = None
        if skip_level is None and DROP.match(l) and lvl >= 2:
            skip_level = lvl; continue
    if skip_level is not None: continue
    if l.startswith('**Themes:**') or l.startswith('> **Check') or 'checks/packs' in l: continue
    out.append(l)
t = '\n'.join(out)
t = re.sub(r'\*\*\[(?:M|R)[^\]\n]{0,80}\]\*\*', '', t)
t = re.sub(r' ?\[(?:M|R)(?:[ ,;:/][^\]\n]{0,80})?\]', '', t)
t = re.sub(r'\[([^\]\n]+)\]\((https?://[^)\s]+)\)', r'\1', t)
t = re.sub(r' ?· ?https?://\S+', '', t)
t = re.sub(r' ?\(https?://[^)\s]+\)', '', t)
t = re.sub(r' ?<?https?://[^\s|)>]+>?', '', t)
t = re.sub(r' ?\(?`[^`\n]*(?:/|\.md|\.json|\.txt|\.csv)[^`\n]*`\)?', '', t)
t = re.sub(r' ?\((?:PMID|PMC)[^)]*\)', '', t)
t = re.sub(r' ?\((?:S\d+[a-z]?(?:[,;–-] ?S?\d+)*)\)', '', t)
t = re.sub(r'\(\s*[,;·]?\s*\)', '', t)
t = re.sub(r'[ \t]+([,.;:])', r'\1', t)
t = re.sub(r'(?m)^(# Part \d+)[:.].*$', lambda m: m.group(0).split('. ')[0] if m.group(0).startswith('# Part 1. ') else m.group(0), t)
t = re.sub(r'\n{3,}', '\n\n', t)
open(dst, 'w', encoding='utf-8').write(t)
print(src, len(open(src).read().split()), '->', len(t.split()))
