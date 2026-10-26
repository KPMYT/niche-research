#!/usr/bin/env python3
"""Print a query label (query + filters) from a saved niche-finder result. Usage: python3 -I r2_label.py file"""
import json, sys
d = json.load(open(sys.argv[1])); js = json.loads(d[-1]['text']); f = dict(js.get('filters', {}))
q = f.pop('query', js.get('niche')); [f.pop(k, None) for k in ('limit', 'minScore', 'excludeSeenVideos', 'sortDirection')]
if f.get('page') == 1: f.pop('page')
print(q + (' [' + '; '.join(f"{k}={v}" for k, v in f.items()) + f"; total {js.get('totalResults')}]" if f else ''))
