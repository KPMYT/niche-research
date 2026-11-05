import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
# drop intro text between a Part heading and its first ## heading
t = re.sub(r'(?ms)^(# Part [12])[^\n]*\n.*?(?=^## )', lambda m: '# ' + ('Part 1: The explainer' if m.group(1).endswith('1') else 'Part 2: The reviews') + '\n\n', t)
# drop "How to read this file" style blocks
t = re.sub(r'(?ms)^\*\*How to read this file\*\*.*?(?=^#|^---)', '', t)
t = re.sub(r'(?m)^(?:\*\*)?Themes?:(?:\*\*)?.*\n', '', t)
t = re.sub(r' ?\(link\)', '', t)
t = re.sub(r',? ?\bPMIDs? [\d, ]+\d', '', t)
t = re.sub(r',? ?\bPMC\d+', '', t)
t = re.sub(r'\(\s*[,;·]?\s*\)', '', t)
t = re.sub(r'[ \t]+([,.;:)])', r'\1', t)
t = re.sub(r'\n{3,}', '\n\n', t)
open(sys.argv[1], 'w', encoding='utf-8').write(t)
