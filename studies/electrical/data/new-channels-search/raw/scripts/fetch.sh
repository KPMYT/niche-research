#!/bin/bash
cd /home/user/niche-research/studies/electrical/data
while read id; do
 f=new-channels-search/raw/ch__${id}__latest.json
 [ -s $f ] || { python3 tools/yt.py channel $id latest 1 > $f 2>/dev/null; sleep 1; }
 n=$(python3 -c "import json,re;d=json.load(open('$f'));v=(d.get('videos_count') or '0').split()[0].replace(',','');print(int(float(v[:-1])*1000) if v.endswith('K') else int(float(v or 0)))" 2>/dev/null)
 if [ "${n:-0}" -gt 30 ]; then
   g=new-channels-search/raw/ch__${id}__oldest.json
   [ -s $g ] || { python3 tools/yt.py channel $id oldest 1 > $g 2>/dev/null; sleep 1; }
 fi
 echo "$id $n"
done < /tmp/claude-0/-home-user/bd54f07e-8fa6-5773-8636-91dde80d17df/scratchpad/h7/cands.txt
echo DONE
