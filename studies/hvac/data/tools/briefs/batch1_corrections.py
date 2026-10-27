"""Batch 1 brief corrections from the HVAC price and facts research (2026-10-27).
Reads the signed-off briefs (batch1-briefs-2026-10-26.tsv, kept as they are), applies each correction below,
and writes batch1-briefs-2026-10-27-corrected.{tsv,xlsx} plus batch1-brief-corrections-2026-10-27.md (before and after).
The evidence is script-system's studies/hvac/price-research-2026-10/ (A-D research, A-D verify) and the price guide built from it,
hvac-scripts/references/price-guide.md. Usage (from this folder): python3 batch1_corrections.py"""
import csv, os
IDE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'ideation')
SRC = 'script-system studies/hvac/price-research-2026-10/'
# (brief numbers, old text, new text, why and source)
C = [
 ((1,), "a blower motor runs about $300-$1,100 installed for a standard motor, $600-$1,500+ for a variable-speed ECM",
        "a blower motor runs about $400-$900 installed for a standard motor, $600-$1,500 (up to about $2,000) for a variable-speed ECM",
        "Checker A: standard (PSC) $400-$900, ECM $600-$1,500, up to $2,000 (A-verify)"),
 ((1,), "add a C-wire or adapter ($20-$30)", "add a C-wire or adapter (about $25-$35)",
        "Adapter $25-$35 at Home Depot, read live (A-research flag; A-verify)"),
 ((3,), "a plain pleated MERV 8 filter (about $5-$8 each in a multipack)", "a plain pleated MERV 8 filter (about $6-$10 each in a multipack)",
        "MERV 8 $6-$10 a filter (C-research; C-verify, confirmed)"),
 ((3,), "MERV 11-13 filter at $20-$35", "MERV 11-13 filter at about $10-$25",
        "C-research and C-verify: the brief's $20-$35 is too high; about $10-$25 a filter"),
 ((3,), "a standalone HEPA room purifier ($100-$250)", "a standalone HEPA room purifier (about $100-$200 for one room)",
        "Price guide section 5, in words (C-research thin; C-verify)"),
 ((3,), "A blower motor replacement runs about $300-$1,100 (variable-speed ECM $600-$1,500+)",
        "A blower motor replacement runs about $400-$900 (variable-speed ECM $600-$1,500, up to about $2,000)",
        "Checker A (A-verify)"),
 ((4,), "(a $10-$25 part, cleaned", "(a $10-$30 part, cleaned", "Flame sensor part $10-$30 (A-verify, Home Depot read live)"),
 ((4,), "a hot-surface igniter is a $20-$60 part, about $120-$350 installed",
        "a hot-surface igniter is a $20-$50 part (brand-name up to about $90), about $150-$400 installed",
        "Checker A: three sources start the installed price at $150 or more; a viewer who paid $350 will dispute $120 (A-verify)"),
 ((5,), "a few gallons a day in cold weather", "several gallons a day in cold weather, up to about 8-10 when it runs hard",
        "D-research and D-verify: a few gallons is low; York and ASHI put a typical furnace at up to about 8 a day"),
 ((6,), "a few gallons of slightly acidic water a day in cold weather", "several gallons of slightly acidic water a day in cold weather, up to about 8-10 when it runs hard",
        "D-research and D-verify: a few gallons is low; York and ASHI put a typical furnace at up to about 8 a day"),
 ((5,6,8), "about $150-$300", "about $100-$250",
        "A clogged-condensate call: $100-$250 (A-research flag 'too high'; A-verify, confirmed)"),
 ((5,6), "about $150-$400 installed", "about $150-$450 installed", "Condensate pump installed $150-$450 (A-verify)"),
 ((7,), "a pro coil cleaning runs $100-$200+", "a pro coil cleaning runs $100-$400",
        "B-research flag 6: an indoor or standalone cleaning runs up to about $400"),
 ((8,), "(about $175-$350 installed)", "(about $150-$400 installed)", "Pressure switch installed $150-$400 (A-verify)"),
 ((8,), "no condensate pump (about $150-$400 installed)", "no condensate pump (about $150-$450 installed)", "Condensate pump installed $150-$450 (A-verify)"),
 ((9,), "Washable / electrostatic ($20-$50 once)", "Washable / electrostatic ($25-$40 once)", "C-research ($25-$40); C-verify keeps it"),
 ((9,), "real HEPA belongs in a standalone room purifier ($100-$250)", "real HEPA belongs in a standalone room purifier (about $100-$200 for one room)",
        "Price guide section 5, in words"),
 ((9,), "Pleated MERV 8 (about $5-$8 each in a multipack)", "Pleated MERV 8 (about $6-$10 each in a multipack)", "C-verify, confirmed"),
 ((9,), "a blower motor at about $300-$1,100 (variable-speed $600-$1,500+)", "a blower motor at about $400-$900 (variable-speed $600-$1,500, up to about $2,000)",
        "Checker A (A-verify)"),
 ((10,), "($5-$8 for a pleated MERV 8)", "($6-$10 for a pleated MERV 8)", "C-verify, confirmed"),
 ((11,), "canned spray foam (about $5-$10 a can)", "canned spray foam (about $5-$8 a can)", "C-verify, confirmed: $5-$8, under $10"),
 ((12,), "Door weatherstripping and a door sweep ($10-$25 a door)", "Door weatherstripping and a door sweep (about $10-$25 each, $25-$50 a door for both)",
        "C-research flag: each part is $10-$25; C-verify agrees $25-$50 together"),
 ((12,), "($5-$10 a tube)", "(about $3-$6 a tube)", "Acrylic latex caulk $3-$6 (C-research; C-verify, confirmed)"),
 ((12,), "Seal the basement rim joist with canned foam ($5-$10 a can)", "Seal the basement rim joist with canned foam ($5-$8 a can)", "C-verify, confirmed"),
 ((12,), "a chimney plug ($30-$80)", "a chimney plug ($35-$90)", "C-research ($35-$90)"),
 ((13,), "Fact for the script: space heaters (fixed and portable) were involved in about one-third of US home heating fires but 88% of home heating fire deaths (NFPA, 2016-2020 annual averages). CPSC, the Red Cross and ESFI all say plug directly into the wall.",
        "Fact for the script: space heaters and heating stoves cause about 3 in 10 US home heating fires but more than 7 in 10 of the deaths (NFPA, 2020-2024 annual averages: 30% of the fires, 73% of the deaths; never '88%' or '9 out of 10', the older 2016-2020 figure). CPSC and the US Fire Administration say plug directly into the wall.",
        "D-research flag 1 and D-verify: NFPA's live page (updated 2025-12-03) gives 2020-2024; the Red Cross wording seen only via search, ESFI's not found"),
 ((14,), "A new sensor costs about $10-$25; a service call to clean or replace it typically runs $100-$250, $300 or more after hours.",
        "A new sensor costs about $10-$30; a service call to clean or replace it typically runs $100-$250, up to about $300 at night or on a weekend.",
        "A-research flag ('$300' is the top, not typical: say 'up to $300') and A-verify (part $10-$30); added 2026-10-27 after it was missed in the first pass"),
 ((15,), "(the DOE's setback figure works out to roughly 1% a year per degree for 8 hours a day; keep the claim soft, never 'cuts your bill')",
        "(the DOE's heating and cooling guide says about 1% off the heating bill for each degree set back for eight hours; 'a degree or two lower' itself isn't DOE wording, so it's said in words; keep the claim soft, never 'cuts your bill')",
        "D-verify: the 1% figure is on a live DOE file (2021), for the heating bill, not 'a year'; the fan line stays in words"),
 ((16,), "but it only needs about 300-800 watts", "but it only needs about 400-800 watts to run, with a start-up surge that can reach 1,400 or more on an older blower motor",
        "D-research and D-verify (in words; check the blower's label)"),
 ((16,), "(about $100-$250 for a 1,000-1,500 watt model)", "(about $150-$300 for a decent 1,000-1,500 watt pure sine model)",
        "C-verify: pure sine $150-$300; the $90-$130 ones are modified sine"),
 ((16,), "(often $200-$500)", "(the switch is about $100-$150, plus a few hundred dollars for the electrician; no checked installed figure)",
        "C-research and C-verify: '$200-$500 installed' not confirmed; in words"),
 ((16,), "at least 20 feet from doors, windows and vents (CPSC's distance for generators)",
        "well away from the house (20 feet from doors, windows and vents is the CPSC and CDC distance for generators; there's no official distance for a car, so the script says it in words)",
        "D-research flag 2: 20 feet is the generator distance; no official car distance"),
]
rows = list(csv.reader(open(f'{IDE}/batch1-briefs-2026-10-26.tsv'), delimiter='\t'))
head, B = rows[0], [list(r) for r in rows[1:]]
log = []
for nums, old, new, why in C:
    for n in nums:
        b = B[n-1][2]
        assert b.count(old) >= 1, (n, old)
        B[n-1][2] = b.replace(old, new); log.append((n, B[n-1][0], old, new, why, b.count(old)))
with open(f'{IDE}/batch1-briefs-2026-10-27-corrected.tsv', 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(head); w.writerows(B)
import openpyxl
from openpyxl.styles import Alignment, Font
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'Batch 1 (corrected)'
ws.append(head)
for c in ws[1]: c.font = Font(bold=True)
for r in B: ws.append(r)
for col, wid in zip('ABC', (48, 45, 120)): ws.column_dimensions[col].width = wid
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical='top')
ws2 = wb.create_sheet('Corrections'); ws2.append(['#', 'Title', 'Before', 'After', 'Why (source)'])
for c in ws2[1]: c.font = Font(bold=True)
for n, t, o, nw, why, k in log: ws2.append([n, t, o, nw, why])
for col, wid in zip('ABCDE', (4, 40, 50, 50, 50)): ws2.column_dimensions[col].width = wid
for row in ws2.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical='top')
wb.save(f'{IDE}/batch1-briefs-2026-10-27-corrected.xlsx')
md = ["# Batch 1 briefs: corrections from the price and facts research (2026-10-27)", "",
      f"The signed-off briefs (`batch1-briefs-2026-10-26.tsv`) are kept as they are. These corrections come from the HVAC price research in script-system (`{SRC}`: four researchers, then four checkers on other publishers) and the price guide built from it (`hvac-scripts/references/price-guide.md`). The corrected briefs are `batch1-briefs-2026-10-27-corrected.tsv` and `.xlsx` (sheet 2 repeats this table). Titles are not changed: two title notes are at the end for the operator. Built by `data/tools/briefs/batch1_corrections.py`.", "",
      f"**{len(log)} corrections in {len({n for n, *_ in log})} briefs.**", "",
      "| # | Title | Before | After | Why (source) |", "|---|---|---|---|---|"]
for n, t, o, nw, why, k in log: md.append(f"| {n} | {t} | {o} | {nw} | {why} |")
md += ["", "## Title notes (not changed: operator, 2026-10-27, \"title always wins also\")", "",
       "- **#3 \"The $5 Filter ... Better Than the $30 One\":** a pleated MERV 8 filter is about $6-$10 each in a multipack, and a 1-inch MERV 11-13 filter about $10-$25 (C-verify). So \"$5\" is the cheapest multipack deal and \"$30\" sits above the usual top. The script can say \"under $10\" and \"$20 or more\" for the two.",
       "- **#14 \"The $12 Part Techs Charge $300 to Replace\":** a flame sensor is $10-$30; a tech's visit is usually $100-$250, and $300 is the top, at night or on a weekend (A-research, A-verify). The script says \"up to $300\".",
       "", "Collect and describe only: the research is not edited to fit a conclusion (`CLAUDE.md`)."]
open(f'{IDE}/batch1-brief-corrections-2026-10-27.md', 'w').write('\n'.join(md) + '\n')
print(len(log), 'corrections in', len({n for n, *_ in log}), 'briefs')
