# Round 3 census: what each channel sells (deliverable 1, "what it sells")

Pulled 2026-10-26 by the round 3 "what it sells" helper. Covers all 1,122 tier A-D rows of `data/raw/channels-master-2026-10-24.csv` (tiers are being redone by another helper; every A-D row was done, so the new tiers can be joined on `channel_id`).

**Files**

| File | What it is |
|---|---|
| `data/raw/census-sells-2026-10-26.csv` | One row per channel: categories, own products with names and prices, affiliate domains, sponsors, membership, merch, contractor, source video ids, pulled. |
| `data/raw/census-sells-desc-2026-10-26.jsonl` | The 2,193 video descriptions read (full text, every link target, page markers). |
| `data/raw/census-sells-candidates-2026-10-26.json` | Own-product candidates the rules found (228 channels). |
| `data/raw/census-sells-landing-2026-10-26.jsonl` | The product landing pages loaded (title, prices shown, price context, checkout host). |
| `data/raw/census-sells-review-2026-10-26.json` | My hand review of the candidates: product names and prices as written. |
| `data/raw/census-sells-nexlev-2026-10-26.json` | NexLev `get_channel_promotions` for 33 channels. |
| `data/raw/raydutton-com-page-2026-10-26.html` | Copy of raydutton.com as loaded 2026-10-26. |
| `data/tools/sells_fetch.py`, `sells_classify.py`, `sells_landing.py`, `sells_review_build.py`, `sells_report.py` | The scripts (run with `python3 -I`). |

## Method

1. **Videos.** For each channel, from its census JSON (`data/raw/census-2026-10-26/<id>.json`): the newest long-form video (first in the Latest sort with length 5:00 or more) and the most popular long-form video (first in the Popular sort with length 5:00 or more). Where the two are the same video it was read once. 2,193 videos on 1,121 channels; 3 channels had no long-form video in Latest, so their newest video was used; Ray Holton Secrets has no videos in its census file (marked "not pulled"). 0 fetch errors.
2. **Descriptions.** Each video's description from the innertube `/next` endpoint (logged out, 3 workers, about 0.7 s between requests per worker), 2026-10-26 07:13-07:57 UTC. The real link targets were taken from YouTube's redirect links (`q=`), so shortened display links still show their true domain.
3. **About.** The channel About text already pulled on 2026-10-24 (`channels-master-about-2026-10-24.json`). That file holds the description text only, not the link list, so About links were read from the text only.
4. **Rules** (`sells_classify.py`), by domain first, then the words on the same description line:
   - Amazon affiliate: amzn.to, amazon.*, a.co, link.amazon, amzlink.to. Other retailers by domain (Home Depot, eBay, SupplyHouse and the rest; full list in the script). geni.us and shorteners (bit.ly, tinyurl) are listed as they are, since the final shop isn't known.
   - Own product: gumroad, payhip, stan.store, etsy, lulu, books2read, liibro, thinkific, teachable, kajabi, skool, systeme and similar; or any other site whose line says book / e-book / guide / manual / PDF / course / plans / "my complete…" / 📘 and so on. These were only candidates: every one was checked by hand (below).
   - Membership: patreon, YouTube `/join`, "channel member(ship)", "become a member", skool, locals. Tips (buymeacoffee, ko-fi, PayPal donate, cash app, venmo) are counted separately.
   - Merch: teespring, spreadshirt, fourthwall, bonfire, creator-spring, printify, "merch", "t-shirt", "hoodie", "gear store".
   - Sponsor: "sponsored by", "this video is sponsored", "our/today's sponsor", "paid partnership", "promo / discount / coupon code", "use code". Lines saying "not sponsored" are skipped. Discount-code lines with another company's link are counted here too, so this category is "sponsor or promo code".
   - Consulting: consultation, 1-on-1, book a call, calendly, coaching, hire me.
   - Contractor (rule): a phone number plus strong service wording (service area, free estimate/quote, licensed and insured, schedule service, book online/your visit, housecallpro, "Serving <Place>", call today) = "y (rule)"; strong wording alone, or a phone with weak wording = "possible (rule)". 10 channels were set by hand.
5. **Landing pages.** Each own-product candidate link was loaded once (direct page load, no search; 2026-10-26) to read the product name and the price shown on the page. Payhip, Etsy, Ko-fi and a few others block this cloud (Cloudflare 403), so those prices are "price not found".
6. **Hand review.** All 228 candidate channels, plus 9 more found by reading the "own website" links of persona channels, were checked by hand (`sells_review_build.py`). Product names are quoted as written; a price is given only where the page or description shows it, with the crossed-out price where shown.
7. **NexLev.** `get_channel_promotions` (channelProfile; not the realtime tool) for the 29 biggest tier A channels, Ray Dutton's Garage and the 3 biggest A-D channels: 10 of the 33 are in NexLev's promotions database, 23 are not scraped. Of the 29 biggest tier A, only 6 were scraped, so NexLev adds little here. What it had matches the descriptions (Ray Dutton's Garage: "The HVAC Survival Guide", $27).
8. **Spot check.** 18 random rows (10 with an own product, 8 "not found") were re-pulled with the separate tool `desc.py`. All 18 matched. One addition came out of it: HVACmillionaire's newest video also sells a coaching offer ("THE MOMENT | HVAC MASTERY"), and that is now in the data. A second helper should still re-check a sample before this goes to the operator (working rule 3).

**Limits (measured vs my reading)**
- Only 2 descriptions per channel. A channel that sells only in other videos, in a pinned comment ("link below (comment section)", seen on Ask Big Jim.), in the About link list or on a Community post is missed. So "not found" means "not in these 2 descriptions or the About text", not "sells nothing".
- YouTube channel memberships show up only when the description mentions them. The Join button is not in the logged-out `/next` response (checked: no `sponsorButtonRenderer` on any of the 2,193 pages). Membership is therefore undercounted.
- Prices are what the landing page showed on 2026-10-26. Many pages run a countdown "launch price", so prices change.
- Kinds ("e-book", "course"), "cross-promotion" and contractor "possible" are my reading. The categories in the CSV come from rules, except own products, which were all checked by hand.
- `own_website` and `affiliate_disclosure` in the CSV are context only, not things sold.

## Round 3 fixes (2026-10-26, round 3 fixer)

The counts below are **as first built**. After the round 3 check, `sells_classify.py` was fixed and re-run (main session decisions, fix 3; details and before/after per channel in `round3/check-round3.md`, "Fixes applied (2026-10-26)"); `data/raw/census-sells-2026-10-26.csv` now holds the fixed version:
1. URL shorteners (bit.ly, tinyurl, rb.gy, goo.gl, shorturl.at) count as affiliate only when the line says so or the resolved target is a shop (368 shortener links resolved with curl redirect hops, `data/tools/sells_shorteners.py`, `data/raw/census-sells-shorteners-2026-10-26.json`).
2. A description that says "no affiliate links" counts none of its links as affiliate; "not affiliated with ..." and government "Commission" names are no longer affiliate disclosures.
3. Plain-text website names ("visit our website at X.com") are read for contractors.
4. Membership words gain "support our channel and get exclusive access".
5. Kilcher Camp: $25 a month or $250 a year ("$25 JOIN MONTHLY", "$250 JOIN FOR THE YEAR"; kilcher-camp page loaded 2026-10-26).
6. PDF / manual links (pdf.*, downloads.*) are not affiliate.

| Category (all 1,122) | As first built | After the fixes |
|---|---:|---:|
| own_product | 141 | 141 |
| membership | 119 | 120 |
| tips | 78 | 79 |
| affiliate | 532 | 498 |
| sponsor | 119 | 120 |
| contractor | 27 | 28 |
| affiliate_disclosure | 356 | 315 |
| not found | 325 | 335 |

For the 66 persona channels after the fixes: affiliate 0 (BIG TICKET TRUTH's Lowe's link is a PDF manual and its descriptions say "No affiliate links"), affiliate disclosure 0 (the 10 were "not affiliated with ...", "no affiliate commissions" or a government "Commission" in a source list), nothing found 39.

## Counts per category

| Category | All A-D (1,122) | A | B | C | D | Personas* |
|---|---|---|---|---|---|---|
| own_product | 141 | 18 | 27 | 79 | 17 | 26 |
| book_ebook_guide | 98 | 15 | 9 | 65 | 9 | 26 |
| course | 21 | 0 | 5 | 10 | 6 | 0 |
| free_lead_magnet | 21 | 1 | 8 | 9 | 3 | 1 |
| membership | 119 | 6 | 46 | 45 | 22 | 0 |
| tips | 78 | 7 | 33 | 23 | 15 | 0 |
| merch | 76 | 2 | 33 | 26 | 15 | 0 |
| affiliate | 532 | 47 | 181 | 173 | 131 | 1 |
| sponsor | 119 | 6 | 33 | 47 | 33 | 0 |
| consulting | 32 | 3 | 3 | 11 | 15 | 0 |
| app | 5 | 0 | 0 | 0 | 5 | 0 |
| newsletter | 43 | 3 | 15 | 16 | 9 | 0 |
| contractor | 27 | 5 | 0 | 0 | 22 | 0 |
| affiliate_disclosure | 356 | 38 | 134 | 144 | 40 | 10 |
| not found | 325 | 77 | 34 | 108 | 106 | 35 |
| not pulled | 1 | 0 | 0 | 1 | 0 | 0 |
| (channels) | 1122 | 157 | 244 | 379 | 342 | 66 |

How to read the counts. Each cell is the number of channels with at least one hit in their 2 descriptions or About text. Channels can be in several rows. Tiers are the tiers as of 2026-10-24, before the redo. *Personas = persona flag "yes" or type "faceless persona" / "AI avatar" (66 channels).
- `own_product` = any paid own product, hand-checked: books, e-books, guides, courses, plans, own-brand goods, spreadsheets, an app, an album. `book_ebook_guide` and `course` are the subsets of it. Free giveaways are in `free_lead_magnet` only.
- `membership` = Patreon, YouTube Join or a paid community. `tips` = Buy Me a Coffee, Ko-fi, PayPal donate.
- `sponsor` = sponsor wording or a promo-code line. `contractor` = "y" by rule or by hand: 10 hand-checked and 17 by rule. Another 41 are "possible (rule)" in the CSV and are not counted here.

What stands out (my reading of the counts):
- **Affiliate links are the default** in the wider DIY/trade pool: 532 of 1,122 channels have at least one (Amazon alone 373). By tier: B 181 of 244, C 173 of 379, D 131 of 342, but only 47 of 157 in tier A.
- **Own e-books cluster in tier C** (off-grid, outage, frugal, old-ways channels: 65 of the 98) **and among faceless personas** (26 of 66). Tier B channels (big on-camera DIY) sell plans, courses and merch instead, and use Patreon (46 have membership).
- **Tier A: 15 channels sell their own book or guide.** 12 of them are new in the last 12 months by the master CSV's new_12m flag (joined, or restarted, between 2026-02 and 2026-08), and almost all are faceless. The biggest is HVAC Guide for Homeowners (169,000 subs, on camera, "New HVAC Guide", $29); the biggest faceless one is Ray Dutton's Garage (31,700). 77 of the 157 tier A channels show nothing in the 2 descriptions.
- **Contractors** (22 in tier D, 5 in A) sell their service area, not products.

## Ray Dutton's Garage: what it sells, exactly

Measured on 2026-10-26: both descriptions and the landing page, plus NexLev.

- **Description (both videos read: newest `AglSKzOY2E8` "Do These 5 Things Before the First Hard Freeze (Or Pay for It in January)" and most popular `dOZ-8__G4uU` "Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring)").** The same two lines open both descriptions:
  > 🔧 Everything I learned fixing HVAC for 25 years, in one plain-English book.
  > 📘 THE HVAC SURVIVAL GUIDE - get it here: https://raydutton.com

  Both have one external link (raydutton.com) and nothing else: no Amazon or other affiliate links, no sponsor, no merch, no Patreon or membership. They end "I'm Ray Dutton. Keep your cool, and I'll see you in the next one."
- **Product (raydutton.com, page saved as `data/raw/raydutton-com-page-2026-10-26.html`).**
  - Name and format: "The HVAC Survival Guide", an "ILLUSTRATED EBOOK · 160+ PAGES · COMPLETE EDITION", "40+ illustrated fixes" (Cooling 17 fixes, Heating 12, Air & Ducts 13), "both diagnostic flowcharts", "every scam decoded".
  - Price: **"$27 launch price, today"**, one-time, instant PDF, with $59 crossed out. The page lists a bundle "Total value $130": the Guide $59, Both Diagnostic Flowcharts $19, Service-Call Defense Scripts $19, Print-and-Tape Cards $12, Free Lifetime Updates $21.
  - Terms: "INSTANT DOWNLOAD · PAY ONCE · YOURS FOREVER · 7-DAY GUARANTEE"; checkout via Visa, Mastercard, PayPal or Apple Pay.
  - Checkout: Gumroad (`rayduttonsgarage.gumroad.com/l/gmuzt`).
  - Proof shown: "★★★★★ 4.9 / 5 · 10 verified Gumroad ratings" with 5 named Gumroad reviews and 6 YouTube comments; "27,000+ subscribers · 4,500,000+ views".
  - Page sections: The Problem (overcharging scenarios: "$9,000 quote", "$6,000 zoning system for what's often a $30 fix", "$99 tune-up… $2,400 bill"), The Guide, The Math ("A typical household… Per year $2,500" vs "~$320" after the Guide; "Net savings: $1,500 to $2,500 a year, for a one-time $27"), What's Inside, What Homeowners Say, About Ray ("25 years in the attics and crawlspaces, working for the companies I now expose… This book is the channel, organized."), Order, Questions.
- **NexLev** (`get_channel_promotions`, NexLev's scrape of 2026-08-20): one product, "The HVAC Survival Guide", ebook, $27 one-time, first seen 2026-08-17, 4 mentions. No sponsors, no affiliates.

**So Ray Dutton sells exactly one thing: his own $27 e-book, linked in the first two lines of every description, from a one-page site with Gumroad checkout. No affiliate, sponsor or merch income shows anywhere.** Roger the Pipe Guy works the same way: "100 Old-House Fixes That Save You Thousands", $19.99 (was $29.99), on rogerthepipeguybooks.com.

## What the faceless personas sell

66 channels carry the master CSV's persona flag or the type "faceless persona" / "AI avatar".

| What | Persona channels (66) |
|---|---|
| Own e-book / guide (paid) | **26** (all 26 checked by hand) |
| Free lead magnet | 1 (Old Ways Restored, alongside paid books) |
| Amazon or other affiliate links | 1 (BIG TICKET TRUTH: one Lowe's link, given as a source) |
| Sponsor, merch, membership, course, consulting | 0 |
| Nothing found in the 2 descriptions + About | 39 (35 with no external links at all, for example Frank Coyle's Wrench, Gus Whitaker, Earl The Furnace Man, Gord The Tradesman, Shaun Meeker; 4 with only an affiliate-disclosure sentence and no link) |

What I read from this:
- The personas follow one model: **a single own e-book (or a bundle of 2-5 e-books), linked in line 1 or 2 of the description, on a one-page site** (own domain, netlify.app, vercel.app or pages.dev), with checkout on Gumroad, Payhip or Stripe. Not one persona uses sponsors, merch or memberships.
- **Entry price** (the lowest $ figure shown for a book, 24 persona channels with a price): median **$29.99**, range $9.99-$97. The most common figures are $27 (7) and $37 (5). Almost every page shows a "launch price" with a crossed-out higher price ($27 instead of $60, $37 regularly $57, $29.99 was $59.99) and a 7- or 30-day money-back guarantee.
- **Book titles in the HVAC lane:** "The HVAC Survival Guide" (Ray Dutton's Garage, $27), "The 30-Year HVAC Bible" (John The HVAC Guy, $27), "THE REAL HVAC GUIDE" (HVAC Mike, price blocked), "Home Heating Survival Guide" (Dale Kirkwood, $37), "The Old House Field Set" / "The Plain Almanac" (The Old House Fix, $37 / $47). The faceless channels without a stated persona sell the same thing: "The Quote Defense Kit" (HVAC Exposed, $27 instead of $60), "The Coil Exposed HVAC Defense Vault" ($29.99), "The Fall Changeover Field Manual" (Exposi, $34.99).
- **Repeated page patterns (my reading).** Six channels use the same landing template, "⚠ Launch Promo ends in 05:5x:xx … Field Edition 2026 · Get Full Bundle $97", with Payhip checkout and single books at "$47 → $27": Eli Yoder Secrets, Builds With Eli Yoder, Hidden Homestead, Jhon Construction, Eli Forgotten Ways and Jhon Survival Mode. Silas Mercer and Sylvie Mercer link the same site (silasmercer.shop). Green Where It Suits links the product sites of The Hillbilly Way and Wonders. These look like groups of channels run by the same sellers; the sites don't name the owners.

| Tier | Persona channel | Subs | Product (as written) | Price shown | Checkout |
|---|---|---|---|---|---|
| A | Ray Dutton's Garage | 31,700 | The HVAC Survival Guide | $27 launch (was $59) | Gumroad |
| A | John The HVAC Guy | 7,130 | The 30-Year HVAC Bible | $27 | liibro.com |
| A | HVAC Mike | 2,430 | THE REAL HVAC GUIDE | price not found (Payhip blocked) | Payhip |
| A | Hank Cole | 1,370 | Hank's Shop Notes (car checks) | $19 launch | Stripe |
| A | Nick Salermo | 663 | The Salermo Set — The Two-Bottle Manual + The Barrel Filter | $27, was $94 | netlify site |
| A | The Old House Fix | 341 | The Old House Field Set (3 guides) / The Plain Almanac | $37 / $47 (was $77) | vercel site |
| A | Dale Kirkwood | 4 | Home Heating Survival Guide | $37, regularly $57 | Gumroad |
| B | Arthur Weber | 15 | Arthur's Manual: 75 simple checks… | price not found | Gumroad |
| C | Bertha's House Hacks | 127,000 | The Old Mexican Way | $39.99, was $59.99 | own site |
| C | Earl Knows How | 43,600 | Earl's Home Repair Manual | $29.99 | Gumroad |
| C | Frugal Frannie | 26,500 | Frannie's Bill Book | $26 (was $47); bundle $46 | own site |
| C | Jhon Construction | 22,000 | The Complete Home Ledger (full bundle) | $97 | Payhip |
| C | Sylvie Mercer | 9,670 | The Forgotten Frontier Journal | $37 launch | silasmercer.shop |
| C | Emmett Boone Prepping | 4,510 | The Blackout Playbook (353 pages) | $37 | Gumroad |
| C | Eli Forgotten Ways | 3,910 | The Forgotten Cooling System (bundle) | $97 | own site |
| C | Old Ways Restored | 2,960 | The Old House Ledger / The Passive Cooling Vault | $27 / $57 | Gumroad |
| C | The Hillbilly Way | 2,430 | The Hillbilly Way (3 books) | $59 (was $81) | own site |
| C | Donna Fixes | 1,890 | Donna's Home Book | $9.99 (was $19.99) | own site |
| C | Linda Fairbrook | 894 | The Prepared Home (5-book collection) | $27 launch (then $49) | own site |
| C | Kate Sullivan Ready Living | 810 | Kate Sullivan's Home Emergency Handbook | $29.99 | Gumroad |
| C | Jhon Survival Mode | 396 | The Blackout Winter Plan / The Complete Survival Mode Library | $27 / $97 | Payhip |
| C | Lars Halvorsen | 304 | The Warm Side (three books) | $29 launch; library $37 | Gumroad |
| C | Jake Holloway | 280 | Before the First Frost — 181 tricks… | page shows $15 and $25 | Payhip |
| C | Hank Dockery | 276 | Hank Dockery Books (set) | $37 launch (then $69) | Payhip |
| C | Gary Miller | 213 | The Complete Home Preparedness Plan | $29.99 (was $59.99) | own site |
| C | Simple Savings at Home | 3 | Home Bills & Savings Binder | $47 one-time | Gumroad |

The full persona list (all 66, including the 33 with nothing found) is the last table below.

## Most common affiliate retailers

Channels with at least one link of that kind, measured from link targets in the 2 descriptions per channel:

| Retailer / network | Channels |
|---|---|
| Amazon (amzn.to, amazon.com, a.co, link.amazon, amzlink.to) | **373** |
| bit.ly (shortener, shop unknown) | 81 |
| geni.us (link wrapper, mostly Amazon) | 39 |
| Home Depot | 13 |
| TubeBuddy | 11 |
| Signature Solar | 10 |
| eBay | 9 |
| Lowe's | 8 |
| tinyurl (shortener) | 8 |
| Epidemic Sound | 7 |
| TruTech Tools | 7 |
| Kit.co | 6 |
| EcoFlow | 5 |
| Impact (sjv.io), tidd.ly, Harvest Right affiliates | 4 each |
| Walmart, AliExpress, ShareASale, Jobber, eufy, Starlink | 3 each |
| HVACDirect, vidIQ, Screwfix, Menards, Octopus Energy referral, VEVOR | 2 each |
| Filterbuy, PIA VPN | 1 each |

HVAC specialist retailers are rare. These are channels whose descriptions name the retailer anywhere (a link or a promo-code line):

| Retailer | Channels | Which |
|---|---|---|
| TruTech Tools | 8 | AC Service Tech LLC, HVAC Know It All, HVAC Overtime, HVAC School, HVACR Survival, HVACR VIDEOS, Quality HVACR, The HVAC Grapevine (all trade channels) |
| SupplyHouse | 5 | Chuck Barron, Coil Exposed, HVAC Know It All ("Use promo code HKIA5 to get 5% off your first order at Supplyhouse!"), Insulwise, Travis Poe |
| HVAC Tactical | 3 | HVAC Dean, Hall's HVAC, Quality HVACR |
| HVACDirect | 2 | HVACDirect (its own channel), The DIY HVAC Guy |
| Filterbuy | 2 | Fix This Build That, The DIY HVAC Guy |
| eComfort | 1 | Eric George, Home Performance Pro |
| AlpineHomeAir | 1 | alpinehomeair (its own brand channel) |
| AC Wholesalers, Sylvane | 0 | |

Tool brands named (raw word counts, so Milwaukee may be the city): Milwaukee 29, Klein 24, Fieldpiece 14, NAVAC 5. Affiliate disclosure wording ("As an Amazon Associate…", "affiliate", "commission") appears on 356 channels.

## Own products: book / e-book / guide / course, every channel (hand-checked)

Sorted by tier, then subscribers. Names are quoted as written on the description or landing page. Prices are as shown on 2026-10-26 (launch prices change). "price not found" = the page was blocked or showed no price.

| Tier | Channel | Type | Subs | Product (as written) | Kind | Price (as shown) | Link domain |
|---|---|---|---|---|---|---|---|
| A | HVAC Guide for Homeowners | on camera | 169000 | New HVAC Guide (access to the guide) | online guide | $29 limited time, shown as "$79 x $29" (newhvacguide.com home page) | newhvacguide.com |
| A | Ray Dutton's Garage | faceless persona (persona flag) | 31700 | The HVAC Survival Guide | e-book (illustrated, 160+ pages, PDF) | $27 launch price, one-time (list $59; page says "Total value $130") | raydutton.com -> rayduttonsgarage.gumroad.com |
| A | HVAC Exposed | faceless | 9590 | The Quote Defense Kit | e-book (PDF) | $27 launch price, "instead of $60" | askfrankhvac.com -> clearfieldpress.gumroad.com |
| A | Walter's Tool Talk | not checked | 8360 | The Vintage Tackle collection (collector guides) | e-books | bundle $79; guide $19 (was $27) | walterstooltalk.com |
| A | John The HVAC Guy | faceless persona (persona flag) | 7130 | The 30-Year HVAC Bible | e-book | $27 | liibro.com |
| A | Richard Nakamura Secrets | not checked | 3970 | The Appliance Blueprint | e-book | $19 launch offer, was $48 (landing page); Gumroad data shows 29.00 | nakamurasecrets.com -> richardnakamura.gumroad.com |
| A | Exposi | faceless | 2530 | The Fall Changeover Field Manual (Vol. I) | e-book (PDF) | $34.99 | exposi.pages.dev |
| A | Exposi | faceless | 2530 | Field Manual Vol. II | e-book (PDF) | $49.99 | exposi.pages.dev |
| A | Exposi | faceless | 2530 | Complete Bundle (Vol. I-III incl. Contractor Defense) | e-book bundle | $97 | exposi.pages.dev |
| A | HVAC Mike | faceless persona (persona flag) | 2430 | THE REAL HVAC GUIDE | e-book | price not found (Payhip blocked, 403); description: "It costs less than a single service call." | payhip.com |
| A | Hank Cole | faceless persona (persona flag) | 1370 | Hank's Shop Notes | e-book (PDF, 56 pages; car checks, not HVAC) | $19 launch price, one-time | hanksheatguide.com (Stripe) |
| A | Coil Exposed | faceless | 667 | The Coil Exposed HVAC Defense Vault | e-book bundle | $29.99 launch discount, was $49.99 | coilexposed.com |
| A | Nick Salermo | faceless persona (persona flag) | 663 | The Salermo Set — The Two-Bottle Manual + The Barrel Filter | e-books (2) | $27, was $94 | nicksalermo.netlify.app |
| A | Ask Big Jim. | not checked | 437 | The AC Owner's Guide | e-book | $37 | ask-big-jim.netlify.app -> payhip.com |
| A | The Old House Fix | faceless persona (persona flag) | 341 | The Old House Field Set (3 PDF guides, 161 pages) | e-books (3) | $37 | ohf-landing.vercel.app |
| A | The Old House Fix | faceless persona (persona flag) | 341 | The Plain Almanac (90 old methods) | e-book | $47 launch price, was $77 | theplainalmanac.vercel.app |
| A | Practical Homeowner | not checked | 26 | The Homeowner's Field Manual | e-book (95 pages) | $39 one-time | homeownersfieldmanual.com -> practicalhomeowner.gumroad.com |
| A | Dale Kirkwood | faceless persona (persona flag) | 4 | Home Heating Survival Guide | e-book bundle | $37, regularly $57 | dale-kirkwood.netlify.app -> gumroad |
| B | Crafted Workshop | not checked | 1110000 | Jumpstart Your Woodworking | course | price not found ("Get 50% off") | bit.ly |
| B | seejanedrill | not checked | 1090000 | Homeowner's Survival Guide | book (signed print) | $39.99 signed copy; Book + Community Bundle $99.99 then $19.99/mo | book.seejanedrill.com |
| B | The Excellent Laborer | not checked | 923000 | All DIY Courses & Downloads – $5 Membership | course membership | $5/month | excellentlaborer.thinkific.com |
| B | plumberparts | on camera | 421000 | Learn Plumbing Online (8 week course) | course | £195.00 | learnplumbingonline.com |
| B | AdamDIY | not checked | 246000 | PDF (not named; "Link to download the PDF") | PDF | price not found (Payhip blocked) | payhip.com |
| B | Home With Stefani | not checked | 212000 | Home DIY With Stefani | course (launches November 10) | price not found (waitlist 25% off; page blocked) | homewithstefani.com |
| B | JAMIE AND SARAH | not checked | 152000 | Our Flipping Guide | guide | price not found (link opens a realtor page) | jamieandsarah.us |
| B | Mason Dixon Acres | not checked | 125000 | The No Regrets Build Guide | guide (waitlist, reopening) | Shopify page data shows 897.00 (not shown as text) | buylandbuilddreams.com |
| B | Snowstead | not checked | 123000 | Ultimate Guide to Starting Your Homestead | e-book | CA$14.99 (was CA$24.99) | stan.store |
| B | Roger the Pipe Guy | not checked | 76500 | 100 Old-House Fixes That Save You Thousands | e-book (PDF, 200 pages) | $19.99 (was $29.99); launch code LAUNCH25 | rogerthepipeguybooks.com |
| B | Caliber8 Tools & DIY | not checked | 42700 | Power Tool Mastery Course | course | $149.99 | caliber8.com |
| B | Caliber8 Tools & DIY | not checked | 42700 | Home Improvement Planner | e-book | price not found | caliber8.com |
| B | Arthur Weber | faceless persona (persona flag) | 15 | Arthur's Manual: 75 simple checks that catch small home problems early | e-book | price not found (page needs JavaScript) | arthurweberhome.com (Gumroad files) |
| C | Undecided with Matt Ferrell | on camera | 1810000 | Become Energy Independent (solar guide, Undecided Academy) | video course | $125 one-time | undecided.link |
| C | City Prepping | not checked | 1270000 | The Prepper's Roadmap | course | price not found (page lists bonuses only) | cityprepp.ing |
| C | Melissa K. Norris - Modern Homesteading | not checked | 489000 | The Family Garden Plan | book (retailers + bonuses) | price not found | melissaknorris.com |
| C | Melissa K. Norris - Modern Homesteading | not checked | 489000 | Homemade Bread and Baking Course | course | price not found (page 404) | lpages.co |
| C | Artisan Electrics | not checked | 395000 | Electricians Business Academy (Skool community) | community/membership | price not found | skool.com |
| C | Elias Yoder | not checked | 369000 | The Amish Home Savings Manual (700+ pages, Second Edition) | e-book | $47 ("earn the $47 back") | eliasyoder.com -> eliasyoder.gumroad.com |
| C | TheUrbanPrepper | not checked | 333000 | 100 Preps Every Urban Family Should Have (field guide) | guide | page shows "$ 7" (not confirmed as the price) | theurbanprepper.com |
| C | Jill Winger - Old Fashioned on Purpose | not checked | 328000 | Old-Fashioned on Purpose | book (retailers) | price not found | oldfashionedbook.com |
| C | Frugal Solutions | not checked | 270000 | Amish cookbooks (Digital Cookbook PDF) | e-books | $9.99-$11.99 | frugal-solutions.com |
| C | Eli Yoder Secrets | faceless | 249000 | The Complete Winter Library (incl. The One Warm Room Plan) | e-book bundle | $97 (was $141) | eliyodersecrets.com -> payhip |
| C | Eli Yoder Secrets | faceless | 249000 | The Borax Field Manual (and other single books) | e-book | $27 (was $47) | eliyodersecrets.com |
| C | Under the Median | not checked | 227000 | e-books shop (Frugal Finance Planner Bundle; Goal Wise: The Frugal Life Planner) | e-books/planners | $47 each | underthemedian.com |
| C | Wonders | faceless | 181000 | The $0 Household Bible | e-book | $27 (compare at $47) | householdbible.com |
| C | Medieval Way | not checked | 179000 | The Medieval Bakery · The Complete Collection (3 e-books) | e-books | $47 collection; single books $27-$29 | medievalway.store |
| C | Eivin Kilcher Homestead | not checked | 171000 | Kilcher Camp | membership community | page shows $25 and $250 (period not captured) | eivinandevekilcher.com |
| C | Everything Electric TECH | not checked | 168000 | The Fully Charged Guide to Electric Vehicles & Clean Energy | book (Amazon) | price not found | buff.ly -> amazon.co.uk |
| C | Medieval Wisdom | not checked | 151000 | The Medieval Wisdom Builder's Manual (PDF, 911 pages) | e-book | $47 launch price through Oct 21, then $67 | medieval-wisdom.com |
| C | Silas Mercer | not checked | 149000 | The Forgotten Frontier Journal ("Survive Any Crisis") | e-book | $37 first-edition launch price | silasmercer.shop |
| C | Bailey Line Road | not checked | 137000 | Cabin Building Course (Build your own tiny home) | course | price not found | baileylineroad.com |
| C | Bailey Line Road | not checked | 137000 | How-To & DIY eBooks | e-books | price not found | baileylineroad.com |
| C | Bertha's House Hacks | faceless persona (persona flag) | 127000 | The Old Mexican Way | e-book (PDF) | $39.99 today, was $59.99 | oldmexicanway.com |
| C | Our Self-Reliant Life | not checked | 116000 | Off-Grid Guides (Ko-fi shop) | guides | price not found (Ko-fi blocked) | ko-fi.com |
| C | Hidden Homestead | not checked | 110000 | The Vault (22 forgotten Amish home formulas) | e-book | $27 (was $47); Full Bundle $97 | hidden-homestead-vault.pages.dev -> payhip |
| C | Forgotten American Survival | faceless | 106000 | Forgotten American Survival Library (5 Preparedness Manuals) | e-books | $59 library; single books from $19 | forgottenamericansurvival.com |
| C | The Ready Life | not checked | 89700 | The Emergency Power Toolkit | workbook (digital) | $9 | thereadylife.com |
| C | The Ready Life | not checked | 89700 | CLASS: How to Heat & Power Your Home In a Long Term Blackout | class | price not found | thereadylife.com |
| C | Stefano Creatini | not checked | 83700 | Homestead Community (Skool, "complimentary $1,500 course") | community | price not found (page 404) | skool.com |
| C | Wild Line | faceless | 80100 | The Passive Home Blueprint | e-book | price not found (page needs JavaScript) | passivehomeblueprint.com -> gumroad |
| C | Heat Geek | on camera | 78700 | COURSES - Become a MASTER of renewable heating | trade courses | price not found (page blocked, 429) | heatgeek.com |
| C | The Passive House Files | not checked | 73500 | The Complete Passive House Vault | e-book bundle | $97 (was $200) | passivehousefiles.com -> stan.store |
| C | The Passive House Files | not checked | 73500 | The Heat Files | e-book | $37 | passivehousefiles.com |
| C | ASIRI Designs | on camera | 68400 | A Design Guide To Dry & Comfortable Basements; A Guide To Moisture Management For Residential Remodels; Flat Roof Design Guides and CAD Details | e-books/design guides | price not found | asiri-designs.com (teachable) |
| C | TheCheapFix | faceless | 66300 | The Hydrogen Peroxide Handbook (55 pages) | e-book | $49 | thecheapfix.netlify.app -> gumroad |
| C | Builds With Eli Yoder | faceless | 58100 | The Energy Trap — Full Off-Grid Manual | e-book | $27 (was $47) | energy-trap-vol1.netlify.app -> payhip |
| C | Builds With Eli Yoder | faceless | 58100 | The Alternator Power Manual | e-book (41 pages) | $49 | manual.eliyodersecrets.com |
| C | Builds With Eli Yoder | faceless | 58100 | The Complete Winter Power Library | e-book bundle | $97 (was $230) | energy-trap-vol1.netlify.app |
| C | Earl Knows How | faceless persona (persona flag) | 43600 | Earl's Home Repair Manual | e-book | $29.99, one time | earlknowshow.com -> gumroad |
| C | Ray Sutter | not checked | 31500 | When the Lights Go Out — The All-Hazards Home Survival Playbook | e-book (315 pages) | $47 launch price (goes to $67) | raysutter.com -> gumroad |
| C | Healthy Home Guide | on camera | 31200 | Healthy Home Method | course | price not found (page lists module values only) | teachable.com |
| C | Healthy Home Guide | on camera | 31200 | DIY Mold Inspection Guide and Checklist | e-book | $29 (Gumroad) | healthyhomeguide.gumroad.com |
| C | Mr iPoo | faceless | 26700 | The Mini AC Builder's Course | course | $2.99 (was $15) | stan.store |
| C | Frugal Frannie | faceless persona (persona flag) | 26500 | Frannie's Bill Book (120 tricks, 73 pages) | e-book | $26 (was $47); 2-book bundle $46 | frugalfrannie.com |
| C | Elias Homestead | not checked | 26400 | Elias Homestead Four-Volume Library | e-books | $99 (was $191); single volumes $27 (was $44) | eliashomestead.shop -> gumroad |
| C | Prime Rundown | not checked | 23800 | The No-BS Buyer's Vault (7 guides) | e-books | $47 launch price (was $79) | primerundown.com -> payhip |
| C | Jhon Construction | faceless persona (persona flag) | 22000 | The Complete Home Ledger (full bundle) / "The complete home library" | e-book bundle | $97 | jhon-construction.com -> payhip |
| C | WiseMoney | faceless | 22000 | Prepping Guide 2026 (The Household Readiness Manual) | e-book | $30 one-time | preppingguide2026.shop |
| C | Caleb Greer — Off-Grid Water & Power | not checked | 19300 | The Off-Grid Manual (368 pages) | e-book | $47 (was $97) | calebgreeroffgrid.com -> gumroad |
| C | Grain & Gravity | not checked | 18200 | Grain & Gravity Field Manuals | e-books | price not found | grainandgravity.com |
| C | Backyard Low Tech | faceless | 12200 | The Backyard LowTech Systems Manual (615 pages) | e-book | $47 | backyardlowtech.com -> gumroad |
| C | Forgotten Home Engineering | faceless | 10200 | The Ultimate Thermal Retention Blueprint ("The Forgotten Blueprint") | e-book | $47 launch price | pages.dev -> payhip |
| C | Sylvie Mercer | faceless persona (persona flag) | 9670 | The Forgotten Frontier Journal ("Survive Any Crisis") | e-book | $37 first-edition launch price | silasmercer.shop |
| C | Renewable Heating Hub | on camera | 7690 | The Ultimate Guide to Heat Pumps | book | price not found | renewableheatinghub.co.uk |
| C | Renewable Heating Hub | on camera | 7690 | Heat Pump Fundamentals For Homeowners | course | £19.95 one-time | learn.renewableheatinghub.co.uk |
| C | The Sensei's Home | faceless | 6850 | The Sensei's Home Manual | e-book | $29.95 | thejapanesehomemanual.com -> gumroad |
| C | The Sensei's Home | faceless | 6850 | The House of Sensei Manual | e-book | $29.95; both $44.95 | thejapanesehomemanual.com |
| C | Christopher Johnson | faceless | 6100 | Christopher's Home Security Guide | e-book (15 chapters) | £19 one-time | netlify.app |
| C | Eric George / Home Performance Pro | on camera | 5780 | Home Comfort Advisor course | course (incl. 30 minute 1 on 1 call) | price not found | myhomecomfortadvisor.com |
| C | Sketchsurvive | faceless | 4560 | 72-Hour Survival Blueprint (Essential) | e-book | special offer $12.00 | systeme.io |
| C | Emmett Boone Prepping | faceless persona (persona flag) | 4510 | The Blackout Playbook (353 pages) | e-book | $37 | blackout-playbook.netlify.app -> gumroad |
| C | Eli Forgotten Ways | faceless persona (persona flag) | 3910 | The Forgotten Cooling System (full bundle) | e-book bundle | $97 | eliforgottenways.com |
| C | Old Ways Restored | faceless persona (persona flag) | 2960 | The Old House Ledger | e-book | $27 (Gumroad) | oldwaysrestored.gumroad.com |
| C | Old Ways Restored | faceless persona (persona flag) | 2960 | The Passive Cooling Vault (68 pages) | e-book | $57 | oldwaysrestored.com |
| C | The Hillbilly Way | faceless persona (persona flag) | 2430 | The Hillbilly Way (3 books) | e-books | $59 (was $81) | thehillbillyway.com |
| C | Earl Sizemore | faceless | 2410 | The $0-Bill House Protocol | e-book | $27 | liibro.com |
| C | Dick Colter Winterproof | faceless | 2010 | The Alaskan Way · Everything 66 Alaska Winters Taught Me | e-book | $37 launch price ($47 later) | dickcolter.com -> gumroad |
| C | Donna Fixes | faceless persona (persona flag) | 1890 | Donna's Home Book (large-print edition 2026) | e-book | $9.99 (was $19.99) | donnafixes.com |
| C | Linda Fairbrook | faceless persona (persona flag) | 894 | The Prepared Home (and the five-book collection) | e-books | $27 launch price for the collection (then $49) | lindafairbrook.com |
| C | Kate Sullivan Ready Living | faceless persona (persona flag) | 810 | Kate Sullivan's Home Emergency Handbook | e-book | $29.99 one time | katesullivanready.com -> gumroad |
| C | Elias Mercer | faceless | 585 | The Old Ways Handbook (83 chapters) | e-book | $27 | eliasmercer.com |
| C | Earl Appalachia | faceless | 414 | The Man They Call When the Power Goes Out (93 methods) | e-book | $47 | earl.myreads.store -> gumroad |
| C | Jhon Survival Mode | faceless persona (persona flag) | 396 | The Blackout Winter Plan | e-book | $27 | jhonsurvivalmode.netlify.app -> payhip |
| C | Jhon Survival Mode | faceless persona (persona flag) | 396 | The Complete Survival Mode Library | e-book bundle | $97 | jhonsurvivalmode.netlify.app |
| C | TheUnknownMarks | not checked | 377 | The Winter Bill Manual (5 books) | e-books | $47 (was $105) | theunknownmark.com -> gumroad |
| C | Lars Halvorsen | faceless persona (persona flag) | 304 | The Warm Side (three books) | e-books | $29 launch offer for all three; library $37 | larshalvorsen.com -> gumroad |
| C | Jake Holloway | faceless persona (persona flag) | 280 | Before the First Frost — 181 tricks for a warm house and a lower heating bill | e-book (51 pages) | page shows $15 and $25 (launch price; not tied in the text) | beforethefirstfrost.com -> payhip |
| C | Hank Dockery | faceless persona (persona flag) | 276 | Hank Dockery Books (set) | e-books | $37 launch price (then $69) | hankdockery.com -> payhip |
| C | Shelved Science | faceless | 247 | Hal's Guides (three books) | e-books | $45 launch price ($59 for all three) | halthebricklayer.com |
| C | Ray Donnelly DIY | not checked | 228 | How to Keep Your Car Alive Forever ("147 Secrets Mechanics Don't Want You to Know") | e-book | $37 | keepyourcaralive.com |
| C | Gary Miller | faceless persona (persona flag) | 213 | The Complete Home Preparedness Plan | e-book | $29.99 (was $59.99) | garymillerprep.com |
| C | Gene Halvorsen | faceless | 132 | A Thousand Cold Houses (154 pages) | e-book | $37 launch price, ends October 31, 2026, then $59 | genehalvorsen.com (Stripe) |
| C | Japanese Offgrid Survival | not checked | 99 | The Japanese Blackout Home | e-book | price not found (Payhip blocked) | payhip.com |
| C | Old Maine Firewood | not checked | 29 | The Old Maine Heating Manual | e-book | $27 | vercel.app -> payhip |
| C | Practical Home Energy | not checked | 7 | The Energy-Saving Manual (508-page PDF) | e-book | $27 launch price (was $47) | thepracticalhomeenergy.site -> gumroad |
| C | Simple Savings at Home | faceless persona (persona flag) | 3 | Home Bills & Savings Binder | web app + printable PDF | $47 one-time | juliehartley.gumroad.com |
| D | AC Service Tech LLC | on camera | 689000 | Mini Split Book and E-Book | book + e-book | page lists $39.99 / $49.99 / $99.99 (formats not matched) | acservicetech.com |
| D | AC Service Tech LLC | on camera | 689000 | Refrigerant Charging Book and E-Book (A/C BOOK) | book + e-book | page lists $39.99 / $49.99 / $99.99 (formats not matched) | acservicetech.com |
| D | MEP Academy | faceless | 113000 | HVAC Training & Courses (e.g. Certified HVAC Piping Estimator Course) | courses | $39-$795 | courses.mepacademy.com |
| D | Digital Constructive | not checked | 19300 | California contractor license course | course | $295 Basic / $395 Crash Course | digitalconstructive.com |
| D | HVACmillionaire | on camera | 14500 | his book ("Grab my book to grow your business") | book (Amazon) | price not found | a.co |
| D | HVACmillionaire | on camera | 14500 | THE MOMENT / HVAC MASTERY ("Get The complete offer") | coaching program | price not found | themoment.kit.com |
| D | HVAC Greatness by Pete Ramsey | on camera | 7260 | HVAC Services Pricing Workshop | course | price not found (discount code sub30atoz, 30% off) | hvac-greatness.thinkific.com |
| D | HVAC Greatness by Pete Ramsey | on camera | 7260 | HVAC "Level of Service" Flat Rate Price Book | price book | price not found | hvac-greatness.thinkific.com |
| D | Powlas HVAC | not checked | 7050 | his book ("Buy My Book") | book (Amazon) | price not found | amzn.to |
| D | Tim DeStasio HVAC | not checked | 6970 | Manual J Fundamentals (or the Season Pass) | live classes | $50 for the first class (Eventbrite) | eventbrite.com |
| D | Mechanical PE Exam Prep | brand | 6120 | FE Mechanical Exam Prep Course | course | price not found (page blocked) | bit.ly |
| D | HVAC Guide for Pros | faceless | 4040 | New HVAC Guide (and growth groups) | online guide | $29 limited time ("$79 x $29") | newhvacguide.com |
| D | HVAC Technician Sales Secrets | on camera | 2240 | The Book For Sales Scripting | book | price not found (site did not load) | salesscriptingbook.com |
| D | MichaelJamesJohnson | not checked | 959 | HVAC Profit Lab (Skool: coaching, courses, pricing tools) | paid community/course | $497 shown (period not captured) | skool.com |
| D | Learn Engineering MEP | not checked | 909 | Cooling Tower Book; Chiller Complete Book; HVAC Commissioning Book; HVAC Installation Complete Guide; AHU, FCU & CSU Master Guide; ASHRAE HVAC Master Guide | e-books (6) | price not found (Payhip blocked) | payhip.com |
| D | No Degree Needed | not checked | 18 | Complete HVAC License Playbook 2026 | e-book | $30 (Gumroad) | tinyurl.com -> gumroad |
| D | No Degree Needed | not checked | 18 | Complete CDL Starter Kit 2026 | e-book bundle | $30 | gumroad |
| D | No Degree Needed | not checked | 18 | Complete NEC Exam Cheat Sheet 2026 | e-book | $19 | gumroad |
| D | No Degree Needed | not checked | 18 | Complete Plumbing Playbook 2026 | e-book | price not found (link 404) | tinyurl.com |

134 book/e-book/guide/course products on 112 channels. This includes paid communities and coaching listed as courses, so it is more than the 98 in the `book_ebook_guide` count.

## Other own products (plans, physical, spreadsheets, apps, music)

| Tier | Channel | Product | Kind | Price | Domain |
|---|---|---|---|---|---|
| A | KungFuMaintenance | Kung Fu Maintenance album "Entropy" | music album (Amazon) | price not found | amzn.to |
| A | Jay Of All Trades | Payhip shop (product not named in the description) | digital product | price not found (Payhip blocked, 403) | payhip.com |
| A | DuC | Maintenance Tracker for Home & Business (and other spreadsheet trackers/calculators) | spreadsheet template (Etsy) | price not found (Etsy blocked, 403) | digitalpixelbyduc.etsy.com |
| B | DIY Creators | Woodworking Plans (Big Bundle) | plans (Gumroad) | price not found | gumroad.com/diycreators |
| B | Fix This Build That | FTBT Woodworking Plans | plans | from $10; "The Everything Bundle" $99 (was $400) | fixthisbuildthat.com |
| B | RR Buildings | Building Plans | plans (Big Cartel) | page lists $100-$450 | rrplans.bigcartel.com |
| B | April Wilkerson | DIY Plans | plans | $6.99-$19.99 | wilkerdos.com |
| B | Clean That Up | Clean That Up Microfiber towels (10 pack) | own-brand physical product | $24.99 (Shopify data) | shop.cleanthatup.com |
| B | Jon Peters - Longview Woodworking | Woodworking design plans (e.g. Long Hive Plans) | plans | $19.99-$24.99 | jonpeters.com |
| B | Mr. Build It | Outdoor Chair Plans / Sauna plans | plans | $10 sale (was $30); Sauna $25 | mrbuilditandco.com |
| B | FarmCraft101 | Etsy Store "MadeByFarmCraft101" | own physical products (Etsy) | price not found (Etsy blocked) | etsy.com |
| B | HandyDadTV | blueprints (e.g. IKEA hack platform bed) | plans | price not found (page blocked, 406) | handydad.tv |
| B | A Glimpse Inside | plans (Etsy shop) | plans | price not found (Etsy blocked) | etsy.com |
| B | PatriotDIY | Etsy shop PatriotDIY | own products (Etsy) | price not found | etsy.com |
| B | Snowstead | Off-Grid Bathroom Plans | plans | CA$12.99 | stan.store |
| B | Snowstead | Tiny Home Plans | plans | $59.99 (was $99.99) | stan.store |
| B | Visual Thinker | Etsy Shop MidwoodMaps | own products (Etsy) | price not found | etsy.com |
| B | HomePro Hero | DETAILED WORKBENCH PLANS (and metric) | plans (Etsy) | price not found (Etsy blocked) | etsy.com |
| B | The Craftsman Blog | DIY Window Screen Plans (books & plans shop, courses) | plans | $10 | thecraftsmanstore.com |
| B | The 3D Handyman | Kits (Etsy shop The3DHandyman) | own physical products | price not found (Etsy blocked) | etsy.com |
| C | Joshua De Lisle | Sculpture designs (Etsy) | own products | price not found | etsy.com |
| C | An American Homestead | Homestead smoker building plans | plans | price not found (page 404) | anamericanhomestead.com |
| C | The Provident Prepper | Integrated Passive Energy Greenhouse (IPEG) plans | plans | price not found (Payhip blocked) | payhip.com |
| C | Dirtpatcheaven | Compost Hotbed Instructions (Etsy) | instructions/plans | price not found | etsy.com |
| C | Greenhill Forge | Project Notes | plans/notes | £2-£11 | greenhillforge.com |
| C | Family DIY | Etsy store terafoxua | own products | price not found | etsy.com |
| C | The Ready Life | 5:21 Preparedness Plan | program | price not found | thereadylife.com |
| C | David McLuckie | Ramp Plans | plans | price not found | davidmcluckie.com |
| D | HVAC School | HVAC School app | app | price not found | hvacrschool.com |
| D | MEP Academy | HVAC & Plumbing - Commercial Estimating Spreadsheet (and other spreadsheets) | spreadsheet | $245 (Gumroad) | mepacademy.gumroad.com |
| D | Crawl Space Ninja | DIY store (Mold Test Kit, mold cleaner, fogger) | own physical products | price not found (product pages 404) | diy.crawlspaceninja.com |
| D | ProbeLem® | ProbeLem SkillVault v1 | digital pack | $49 one-time | skills.probelem.com |
| D | Rosa The Female HVAC Tech | Gumroad store (products not named in the description) | digital products | price not found | rosafemalehvactech.gumroad.com |

33 other products on 32 channels.

## Free lead magnets

- A Home Caprice: FREE cheat sheet: 28 tricks to save on your electricity and heating bill (mailerlite.com)
- B Everyday Home Repairs: Free Home Maintenance Checklist (everydayhomerepairs.com)
- B seejanedrill: free masterclass on building your dream home (sjdmasterclass.com)
- B The Honest Carpenter: FREE GUIDE: 25 Must-Have Carpentry Tools...Under $25 Each! (thehonestcarpenter.com)
- B Helpful DIY: DIY Advice: 51 Tips for Do It Yourselfers (gumroad.com)
- B Snowstead: FREE Emergency Kit E-Book (stan.store)
- B HouseBarons: Free Home Maintenance Checklist (beehiiv.com)
- B HomePro Hero: FREE BASIC DIY WORKBENCH PLANS (kit.com)
- B DIY WISCO: FREE cut list (kit.com)
- C City Prepping: Start Preparing Survival Guide (cityprepp.ing)
- C DIY Solar Power with Will Prowse: guidebook to off-grid 12V solar (willapproved.com)
- C TheUrbanPrepper: 20 Preps Gear Guide (bit.ly (Dropbox))
- C Under the Median: Home Energy Savings Guide; Pantry Stock Up Workbook; grocery guide (underthemedian.com)
- C Bailey Line Road: DIY Hoop House Plans (bit.ly)
- C Zach Of All Trades: The 50 Dollar Food Plan (zachofalltrades.io)
- C Healthy Home Guide: Free masterclass: 5 mistakes... (renegadeairquality.com)
- C UnpluggedTexan: free wiring schematic pdf (solarpdfdownload.com)
- C Old Ways Restored: The Fan Country Test (oldwaysrestored.com)
- D Digital Constructive: Free Course (digitalconstructive.com)
- D HVAC Pro Blog: Free Rule of Duct Design PDF (ck.page)
- D HVAC 2.0: free quote onboarding (mykajabi.com)

## Checkout and prices

- Checkout or hosting named in the paid product links (count of products): Gumroad 31, Payhip 17, Etsy 10, netlify.app 10, pages.dev 5, stan.store 5, vercel.app 3, Thinkific 3, Skool 3, Amazon 5 (author books), liibro 2, Stripe 2, Teachable 2, systeme 1, myreads 1. The rest are own domains with no checkout seen.
- Entry price of a paid book or guide (the lowest $ figure shown, 73 channels): median $30, range $7-$99. Most common: $27 (16 channels), $47 (12), $37 (11). Personas: median $29.99 (24 channels).

## All 66 persona channels (full list)

Counts: 26 own book or guide, 1 free lead magnet, 1 affiliate (a Lowe's source link), 35 nothing found, 4 an affiliate-disclosure sentence only. In the Sells column, `own_website` and `affiliate_disclosure` are left out.

| Tier | Channel | Type | Subs | Sells | Own product(s) |
|---|---|---|---|---|---|
| A | Ray Dutton's Garage | faceless persona | 31700 | own_product ; book_ebook_guide | The HVAC Survival Guide [e-book (illustrated, 160+ pages, PDF)] — $27 launch price, one-time (list $59; page says "Total value $130") — raydutton.com -> rayduttonsgarage.gumroad.com |
| A | John The HVAC Guy | faceless persona | 7130 | own_product ; book_ebook_guide | The 30-Year HVAC Bible [e-book] — $27 — liibro.com |
| A | HVAC Mike | faceless persona | 2430 | own_product ; book_ebook_guide | THE REAL HVAC GUIDE [e-book] — price not found (Payhip blocked, 403); description: "It costs less than a single service call." — payhip.com |
| A | Frank Coyle's Wrench | faceless persona | 2170 | not found | not found |
| A | Hank Cole | faceless persona | 1370 | own_product ; book_ebook_guide | Hank's Shop Notes [e-book (PDF, 56 pages; car checks, not HVAC)] — $19 launch price, one-time — hanksheatguide.com (Stripe) |
| A | Gus Whitaker | faceless persona | 823 | not found | not found |
| A | Nick Salermo | faceless persona | 663 | own_product ; book_ebook_guide | The Salermo Set — The Two-Bottle Manual + The Barrel Filter [e-books (2)] — $27, was $94 — nicksalermo.netlify.app |
| A | The Old House Fix | faceless persona | 341 | own_product ; book_ebook_guide | The Old House Field Set (3 PDF guides, 161 pages) [e-books (3)] — $37 — ohf-landing.vercel.app / The Plain Almanac (90 old methods) [e-book] — $47 launch price, was $77 — theplainalmanac.vercel.app |
| A | Building Secrets | faceless persona | 286 | not found | not found |
| A | Earl The Furnace Man | faceless persona | 185 | not found | not found |
| A | Gord The Tradesman | faceless persona | 164 | not found | not found |
| A | Peace TV Urdeo | AI avatar | 110 | not found | not found |
| A | Earl Whitaker | faceless persona | 108 | not found | not found |
| A | The Smart Way to Buy HVAC with Doug Cross | AI avatar | 75 | not found | not found |
| A | Frank From Maintenance | faceless persona | 68 | not found | not found |
| A | Walt Brenner's Boiler | faceless persona | 39 | not found | not found |
| A | Conditioned Air Secrets | AI avatar | 30 | not found | not found |
| A | Shaun Meeker | faceless persona | 20 | not found | not found |
| A | Heater Analyst | faceless persona | 17 | not found | not found |
| A | Homeowner Money | AI avatar | 14 | not found | not found |
| A | Dale Prosser | AI avatar | 9 | not found | not found |
| A | Caleb Vance | faceless persona | 9 | not found | not found |
| A | Dale Kirkwood | faceless persona | 4 | own_product ; book_ebook_guide | Home Heating Survival Guide [e-book bundle] — $37, regularly $57 — dale-kirkwood.netlify.app -> gumroad |
| A | Blueprint Archive | AI avatar | 3 | not found | not found |
| A | Leroy Bell's Repair | faceless persona | 1 | not found | not found |
| A | Vern Holt | Home Repair | faceless persona | 1 | not found | not found |
| A | The House Papers | AI avatar | not found | not found | not found |
| B | Arthur Weber | faceless persona | 15 | own_product ; book_ebook_guide | Arthur's Manual: 75 simple checks that catch small home problems early [e-book] — price not found (page needs JavaScript) — arthurweberhome.com (Gumroad files) |
| C | Bertha's House Hacks | faceless persona | 127000 | own_product ; book_ebook_guide | The Old Mexican Way [e-book (PDF)] — $39.99 today, was $59.99 — oldmexicanway.com |
| C | Earl Knows How | faceless persona | 43600 | own_product ; book_ebook_guide | Earl's Home Repair Manual [e-book] — $29.99, one time — earlknowshow.com -> gumroad |
| C | Frugal Frannie | faceless persona | 26500 | own_product ; book_ebook_guide | Frannie's Bill Book (120 tricks, 73 pages) [e-book] — $26 (was $47); 2-book bundle $46 — frugalfrannie.com |
| C | Jhon Construction | faceless persona | 22000 | own_product ; book_ebook_guide | The Complete Home Ledger (full bundle) / "The complete home library" [e-book bundle] — $97 — jhon-construction.com -> payhip |
| C | Ripped Off Britain | faceless persona | 10000 | not found | not found |
| C | Sylvie Mercer | faceless persona | 9670 | own_product ; book_ebook_guide | The Forgotten Frontier Journal ("Survive Any Crisis") [e-book] — $37 first-edition launch price — silasmercer.shop |
| C | Harlan Sawyer | faceless persona | 5730 | not found | not found |
| C | Emmett Boone Prepping | faceless persona | 4510 | own_product ; book_ebook_guide | The Blackout Playbook (353 pages) [e-book] — $37 — blackout-playbook.netlify.app -> gumroad |
| C | Wes Tucker Prepping | faceless persona | 4020 | not found | not found |
| C | Eli Forgotten Ways | faceless persona | 3910 | own_product ; book_ebook_guide | The Forgotten Cooling System (full bundle) [e-book bundle] — $97 — eliforgottenways.com |
| C | Living Like It's 1950 | faceless persona | 3550 | not found | not found |
| C | Old Ways Restored | faceless persona | 2960 | own_product ; book_ebook_guide ; free_lead_magnet | The Old House Ledger [e-book] — $27 (Gumroad) — oldwaysrestored.gumroad.com / The Passive Cooling Vault (68 pages) [e-book] — $57 — oldwaysrestored.com / The Fan Country Test [free printable] — free — oldwaysrestored.com |
| C | The Hillbilly Way | faceless persona | 2430 | own_product ; book_ebook_guide | The Hillbilly Way (3 books) [e-books] — $59 (was $81) — thehillbillyway.com |
| C | Donna Fixes | faceless persona | 1890 | own_product ; book_ebook_guide | Donna's Home Book (large-print edition 2026) [e-book] — $9.99 (was $19.99) — donnafixes.com |
| C | June's Kitchen Table | faceless persona | 1690 | not found | not found |
| C | David Bennett | faceless persona | 1690 | not found | not found |
| C | Harlan Pike Prepping | faceless persona | 1230 | not found | not found |
| C | Ivan’s Survival Journal | faceless persona | 1050 | not found | not found |
| C | Linda Fairbrook | faceless persona | 894 | own_product ; book_ebook_guide | The Prepared Home (and the five-book collection) [e-books] — $27 launch price for the collection (then $49) — lindafairbrook.com |
| C | Kate Sullivan Ready Living | faceless persona | 810 | own_product ; book_ebook_guide | Kate Sullivan's Home Emergency Handbook [e-book] — $29.99 one time — katesullivanready.com -> gumroad |
| C | Prairie Legacy | AI avatar | 540 | not found | not found |
| C | Walt Brandt | faceless persona | 461 | not found | not found |
| C | BIG TICKET TRUTH | AI avatar | 421 | affiliate | not found |
| C | Jhon Survival Mode | faceless persona | 396 | own_product ; book_ebook_guide | The Blackout Winter Plan [e-book] — $27 — jhonsurvivalmode.netlify.app -> payhip / The Complete Survival Mode Library [e-book bundle] — $97 — jhonsurvivalmode.netlify.app |
| C | Lars Halvorsen | faceless persona | 304 | own_product ; book_ebook_guide | The Warm Side (three books) [e-books] — $29 launch offer for all three; library $37 — larshalvorsen.com -> gumroad |
| C | Jake Holloway | faceless persona | 280 | own_product ; book_ebook_guide | Before the First Frost — 181 tricks for a warm house and a lower heating bill [e-book (51 pages)] — page shows $15 and $25 (launch price; not tied in the text) — beforethefirstfrost.com -> payhip |
| C | Hank Dockery | faceless persona | 276 | own_product ; book_ebook_guide | Hank Dockery Books (set) [e-books] — $37 launch price (then $69) — hankdockery.com -> payhip |
| C | Blackout Logic | AI avatar | 235 | not found | not found |
| C | Gary Miller | faceless persona | 213 | own_product ; book_ebook_guide | The Complete Home Preparedness Plan [e-book] — $29.99 (was $59.99) — garymillerprep.com |
| C | Darrin Stevenson | faceless persona | 202 | not found | not found |
| C | Mason Reed Preparedness | faceless persona | 190 | not found | not found |
| C | Del Rasmussen | faceless persona | 109 | not found | not found |
| C | Eli's Plain Heat | faceless persona | 45 | not found | not found |
| C | Wade Corbin | faceless persona | 13 | not found | not found |
| C | Simple Savings at Home | faceless persona | 3 | own_product ; book_ebook_guide | Home Bills & Savings Binder [web app + printable PDF] — $47 one-time — juliehartley.gumroad.com |
| C | Walt's Workshop | faceless persona | 1 | not found | not found |
| C | Old House Walt | faceless persona | not found | not found | not found |
| C | Dale's Winter Fixes | faceless persona | not found | not found | not found |
