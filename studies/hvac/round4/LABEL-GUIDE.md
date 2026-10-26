# Round 4 labelling guide (2026-10-26)

For the round 4 labelling helpers. The full definitions are in `../labels.md` (sections 1-4); this page fixes the codes and the output so 8 helpers label the same way.

**Read the title only** (no thumbnails, descriptions or transcripts in this pass; there are about 16,900 titles). Label what the title *sells*, not what may happen in the video. Every label is a reading.

## Output: one CSV row per input row

`video_id,scope_ok,subniche,format,e1,e2,e3,villain,note`

- **scope_ok:** `y` if the title is about home HVAC / heating / cooling / energy bills / insulation for heat or bills / outage heat / off-grid heat for a home; `n` if it is off-topic (cars, kids' games, cooking, trade-only training, commercial HVAC, non-home) or not English; `?` if you can't tell. Label the rest of the row only when `y` or `?`.
- **subniche:** one code from the list below.
- **format:** one code from the list below, taking the **first** rule that matches, in the `labels.md` order.
- **e1, e2, e3:** up to three emotion codes (E1-E20), strongest first; leave unused ones blank. Use at least one when the title carries any feeling; plain topic labels ("Furnace Filters") can have none.
- **villain:** one code (`none` is the default).
- **note:** optional, short (e.g. a list shape "Top 5", a persona name, a dollar figure, "old ways", "(The X Way)").

## Sub-niche codes

`ac-central`, `ac-window`, `ac-portable`, `mini-split`, `heat-pump`, `furnace`, `boiler-oldheat` (boilers, radiators, steam, baseboard, oil burners), `fuel-choice`, `thermostat`, `filter`, `ducts-vents`, `parts` (capacitors, contactors etc.), `seasonal-maint`, `energy-bill`, `drafts-insulation`, `humidity-air` (dehumidifiers, humidifiers, mould, purifiers, ventilation), `outage-heat` (warm or cool with no power), `offgrid-heat` (wood/pellet stoves, diesel heaters, space heaters, "free heat" tricks), `brand-verdict`, `buy-replace` (quotes, sizing, repair or replace, cost, contractor choice), `scam-upsell` (the title is about being ripped off), `cooling-no-ac` (cooling tricks, DIY coolers, evaporative coolers, fans), `noise-smell-error` (noises, smells, error codes as the subject), `hvac-general` (no equipment named), `adjacent` (water heaters, frozen pipes, solar, generators not about heat).

Proposed codes not yet in `labels.md` (to put to the operator): `scam-upsell`, `cooling-no-ac`, `noise-smell-error`, `hvac-general`.

## Format codes (first match, in this order)

`test`, `x-vs-y`, `only-x` (the best / only X worth buying), `review`, `myth`, `secret` (Y doesn't want you to know: secret, hidden, they don't tell you, banned, forgotten), `mistakes`, `before-you`, `news-warning`, `cheap-hack`, `symptom-fix`, `install-diy`, `how-to`, `explainer`, `story`, `plain` (a topic label with no promise).

Close calls: see `labels.md` section 3. "Make it cold again" = how-to; "not cooling" = symptom-fix. "Forgotten / old-timers' / Amish trick" = `secret` when it promises hidden knowledge, `cheap-hack` when the promise is a cheap substitute ("$5 trick", "use THIS instead"); if both, `secret` (it comes first).

## Emotion codes

E1 fear of the big bill · E2 resentment of the service call · E3 distrust of the store shelf · E4 dread of silent, hidden damage · E5 emergency dread and urgency · E6 frustration of failed attempts · E7 disgust · E8 satisfaction of the clear payoff · E9 embarrassment and household shame · E10 insider curiosity · E11 being let in · E12 vindication and the myth-bust · E13 pride in self-reliance · E14 relief and reassurance · E15 nostalgia and inherited wisdom · E16 protectiveness (family, pets, parents) · E17 safety fear · E18 rule-curiosity and mild defiance · E19 comfort (a house too hot or too cold) · E20 new-gadget wonder. Definitions: `labels.md` section 1.

## Villain codes

`hvac-company`, `service-call`, `upsell`, `utility` (the bill-sender), `maker-shelf`, `last-owner`, `own-habit`, `none`, `insider`. One main villain, picked by where the title's money goes; named or plainly implied only.
