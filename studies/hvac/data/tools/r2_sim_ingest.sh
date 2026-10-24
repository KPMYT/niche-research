#!/bin/sh
# Round 2: ingest saved get_similar_channels_status results, labelling each by its jobId (looked up in simjobs.json).
# Usage: sh r2_sim_ingest.sh <scratchdir> file1 [file2 ...]
S=$1; shift
for F in "$@"; do
  L=$(python3 -I -c "
import json,sys
d=json.load(open(sys.argv[1])); js=json.loads(d[-1]['text']); j=js.get('jobId')
m={x[3]:x for x in json.load(open(sys.argv[2]))}
x=m.get(j); print(f'similar: {x[0]} ({x[1]}) level {x[2]}' if x else 'similar: unknown job '+str(j))" "$F" "$S/simjobs.json")
  python3 -I "$(dirname "$0")/r2_nexlev_ingest.py" "$S" sim "$L" "$F"
done
