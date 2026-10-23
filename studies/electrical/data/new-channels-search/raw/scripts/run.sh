#!/bin/bash
T=/home/user/niche-research/studies/electrical/data/tools/yt.py
R=/home/user/niche-research/studies/electrical/data/new-channels-search/raw
while IFS=$'\t' read -r kw src core; do
  slug=$(echo "$kw" | tr 'A-Z ' 'a-z_' | tr -cd 'a-z0-9_-')
  for s in views_year month $( [ "$core" = core ] && echo relevance ); do
    f="$R/search__${slug}__${s}.json"
    [ -s "$f" ] && continue
    python3 $T search "$kw" $s 1 > "$f" 2>"$f.err" || echo "FAIL $kw $s"
    sleep 1
  done
done < /tmp/claude-0/-home-user/bd54f07e-8fa6-5773-8636-91dde80d17df/scratchpad/h7/kw.tsv
echo DONE
