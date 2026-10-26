#!/usr/bin/env python3
"""Round 3 what-it-sells: writes raw/census-sells-review-2026-10-26.json, the hand review of own-product candidates
(names and prices as written on the description or the landing page loaded 2026-10-26). Usage: python3 -I sells_review_build.py"""
import json, csv
# Hand review, 2026-10-26, by the round 3 'what it sells' helper. Product names as written in the description
# or on the landing page; prices only where the landing page (direct load 2026-10-26) or the description shows them.
# P(name, kind, price, domain, free=False)
def P(name, kind, price, domain, free=False):
    return {'name': name, 'kind': kind, 'price': price, 'domain': domain, 'free': free}
NF = 'price not found'
R = {}
def own(n, prods, note='', add=(), contractor=None):
    R[n] = {'own_products': prods, 'note': note, 'add': list(add)}
    if contractor: R[n]['contractor'] = contractor
def none(n, note='', add=(), contractor=None):
    own(n, [], note, add, contractor)

# ---- tier A
none('Taddy Digest', 'Signature Solar discount code via solartoolpro.com (third-party code page)', ['affiliate', 'sponsor'])
own('HVAC Guide for Homeowners', [P('New HVAC Guide (access to the guide)', 'online guide', '$29 limited time, shown as "$79 x $29" (newhvacguide.com home page)', 'newhvacguide.com')],
    'NexLev also lists "MasterMind Group" (community) and "HVAC Guide monthly support" $1/month on buymeacoffee', ['membership', 'tips'])
own('KungFuMaintenance', [P('Kung Fu Maintenance album "Entropy"', 'music album (Amazon)', NF, 'amzn.to')], 'own music album, not a book')
none('Atlas AC', '"Buyers Guide" is a free article on the company site', contractor='y')
own("Ray Dutton's Garage", [P('The HVAC Survival Guide', 'e-book (illustrated, 160+ pages, PDF)', '$27 launch price, one-time (list $59; page says "Total value $130")', 'raydutton.com -> rayduttonsgarage.gumroad.com')],
    'NexLev (scraped 2026-08-20): ebook, $27')
none('SaveGreenHere', 'T-Mobile / Sprint plan links with promo code', ['affiliate', 'sponsor'])
none('EdgeTek HVAC', 'manufacturer literature link')
own('HVAC Exposed', [P('The Quote Defense Kit', 'e-book (PDF)', '$27 launch price, "instead of $60"', 'askfrankhvac.com -> clearfieldpress.gumroad.com')])
none('Tom Bray', 'mailing list + "Book in a call" (calendly) + "Work with me" (sb-energy.co.uk)', ['consulting', 'newsletter'])
own('John The HVAC Guy', [P('The 30-Year HVAC Bible', 'e-book', '$27', 'liibro.com')])
own('Home Caprice', [P('FREE cheat sheet: 28 tricks to save on your electricity and heating bill', 'free guide (email sign-up)', 'free', 'mailerlite.com', True)], add=['newsletter'])
own('Jay Of All Trades', [P('Payhip shop (product not named in the description)', 'digital product', NF + ' (Payhip blocked, 403)', 'payhip.com')])
none('Home Comfort Guy', 'BathExhaust.com review site (own website, no product)')
none("Hartzell's Heat & Air", 'online booking (housecallpro)', contractor='y')
own('DuC', [P('Maintenance Tracker for Home & Business (and other spreadsheet trackers/calculators)', 'spreadsheet template (Etsy)', NF + ' (Etsy blocked, 403)', 'digitalpixelbyduc.etsy.com')])
own('Richard Nakamura Secrets', [P('The Appliance Blueprint', 'e-book', '$19 launch offer, was $48 (landing page); Gumroad data shows 29.00', 'nakamurasecrets.com -> richardnakamura.gumroad.com')])
own('Exposi', [P('The Fall Changeover Field Manual (Vol. I)', 'e-book (PDF)', '$34.99', 'exposi.pages.dev'),
               P('Field Manual Vol. II', 'e-book (PDF)', '$49.99', 'exposi.pages.dev'),
               P('Complete Bundle (Vol. I-III incl. Contractor Defense)', 'e-book bundle', '$97', 'exposi.pages.dev')])
own('HVAC Mike', [P('THE REAL HVAC GUIDE', 'e-book', NF + ' (Payhip blocked, 403); description: "It costs less than a single service call."', 'payhip.com')])
own('Hank Cole', [P("Hank's Shop Notes", 'e-book (PDF, 56 pages; car checks, not HVAC)', '$19 launch price, one-time', 'hanksheatguide.com (Stripe)')])
own('Coil Exposed', [P('The Coil Exposed HVAC Defense Vault', 'e-book bundle', '$29.99 launch discount, was $49.99', 'coilexposed.com')])
own('Nick Salermo', [P('The Salermo Set — The Two-Bottle Manual + The Barrel Filter', 'e-books (2)', '$27, was $94', 'nicksalermo.netlify.app')])
own('Ask Big Jim.', [P("The AC Owner's Guide", 'e-book', '$37', 'ask-big-jim.netlify.app -> payhip.com')], 'also "Grab the E-Book: 18 straight answers for smarter appliance choices" (link in comments)')
own('The Old House Fix', [P('The Old House Field Set (3 PDF guides, 161 pages)', 'e-books (3)', '$37', 'ohf-landing.vercel.app'),
                          P('The Plain Almanac (90 old methods)', 'e-book', '$47 launch price, was $77', 'theplainalmanac.vercel.app')])
none('Quarter Turn', 'source links only (CPSC)')
own('Practical Homeowner', [P("The Homeowner's Field Manual", 'e-book (95 pages)', '$39 one-time', 'homeownersfieldmanual.com -> practicalhomeowner.gumroad.com')])
own('Dale Kirkwood', [P('Home Heating Survival Guide', 'e-book bundle', '$37, regularly $57', 'dale-kirkwood.netlify.app -> gumroad')], 'free 18-point checklist too')
# ---- tier B
none('Home RenoVision DIY', 'newsletter; NexLev: channel membership "DIY Crew" $5/month', ['newsletter', 'membership'])
own('DIY Creators', [P('Woodworking Plans (Big Bundle)', 'plans (Gumroad)', NF, 'gumroad.com/diycreators')])
none('This Old House', 'free newsletter', ['newsletter'])
own('Fix This Build That', [P('FTBT Woodworking Plans', 'plans', 'from $10; "The Everything Bundle" $99 (was $400)', 'fixthisbuildthat.com')])
own('RR Buildings', [P('Building Plans', 'plans (Big Cartel)', 'page lists $100-$450', 'rrplans.bigcartel.com')])
own('April Wilkerson', [P('DIY Plans', 'plans', '$6.99-$19.99', 'wilkerdos.com')])
own('Clean That Up', [P('Clean That Up Microfiber towels (10 pack)', 'own-brand physical product', '$24.99 (Shopify data)', 'shop.cleanthatup.com')], add=['newsletter', 'merch'])
own('Everyday Home Repairs', [P('Free Home Maintenance Checklist', 'free guide', 'free', 'everydayhomerepairs.com', True)])
none('LRN2DIY', '"projects and plans" blog (no paid plan seen on the page)')
own('Crafted Workshop', [P('Jumpstart Your Woodworking', 'course', NF + ' ("Get 50% off")', 'bit.ly')])
own('seejanedrill', [P("Homeowner's Survival Guide", 'book (signed print)', '$39.99 signed copy; Book + Community Bundle $99.99 then $19.99/mo', 'book.seejanedrill.com'),
                     P('free masterclass on building your dream home', 'free class', 'free', 'sjdmasterclass.com', True)], add=['membership'])
own('Jon Peters - Longview Woodworking', [P('Woodworking design plans (e.g. Long Hive Plans)', 'plans', '$19.99-$24.99', 'jonpeters.com')])
own('The Honest Carpenter', [P('FREE GUIDE: 25 Must-Have Carpentry Tools...Under $25 Each!', 'free guide', 'free', 'thehonestcarpenter.com', True)])
own('Mr. Build It', [P('Outdoor Chair Plans / Sauna plans', 'plans', '$10 sale (was $30); Sauna $25', 'mrbuilditandco.com')])
own('The Excellent Laborer', [P('All DIY Courses & Downloads – $5 Membership', 'course membership', '$5/month', 'excellentlaborer.thinkific.com')], add=['membership'])
none('NoNonsenseKnowHow', 'Bolt Depot ("Where I Get My Hardware")', ['affiliate'])
own('Helpful DIY', [P('DIY Advice: 51 Tips for Do It Yourselfers', 'free e-book', 'free ($0 on Gumroad)', 'gumroad.com', True)])
none('The DIY Guy', 'LED Space Iris Kit (LEDSpace collaboration page)', ['affiliate'])
none('Skill Builder', 'newsletter', ['newsletter'])
own('FarmCraft101', [P('Etsy Store "MadeByFarmCraft101"', 'own physical products (Etsy)', NF + ' (Etsy blocked)', 'etsy.com')])
none('Roger Wakefield Plumbing Education', 'leak-detection equipment link', ['affiliate'])
none('MR Post Frame', 'Back Forty Buildings plans and kits (ownership not stated)')
own('plumberparts', [P('Learn Plumbing Online (8 week course)', 'course', '£195.00', 'learnplumbingonline.com')])
own('HandyDadTV', [P('blueprints (e.g. IKEA hack platform bed)', 'plans', NF + ' (page blocked, 406)', 'handydad.tv')])
none('Gosforth Handyman', 'free newsletter; "Our little shop (official Tape Measure, pencils etc.)"', ['newsletter', 'merch'])
own('AdamDIY', [P('PDF (not named; "Link to download the PDF")', 'PDF', NF + ' (Payhip blocked)', 'payhip.com')])
none('HouseCalls', 'weekly newsletter', ['newsletter'])
none("The Kelley's Country Life", 'merchandise (T-shirts $19.99-$26.99)', ['merch'])
own('A Glimpse Inside', [P('plans (Etsy shop)', 'plans', NF + ' (Etsy blocked)', 'etsy.com')])
own('Home With Stefani', [P('Home DIY With Stefani', 'course (launches November 10)', NF + ' (waitlist 25% off; page blocked)', 'homewithstefani.com')])
none('AmplifyDIY', 'free PDF of written instructions made by a viewer')
own('JAMIE AND SARAH', [P('Our Flipping Guide', 'guide', NF + ' (link opens a realtor page)', 'jamieandsarah.us')])
own('PatriotDIY', [P('Etsy shop PatriotDIY', 'own products (Etsy)', NF, 'etsy.com')])
own('Mason Dixon Acres', [P('The No Regrets Build Guide', 'guide (waitlist, reopening)', 'Shopify page data shows 897.00 (not shown as text)', 'buylandbuilddreams.com')])
own('Snowstead', [P('Off-Grid Bathroom Plans', 'plans', 'CA$12.99', 'stan.store'), P('Tiny Home Plans', 'plans', '$59.99 (was $99.99)', 'stan.store'),
                  P('Ultimate Guide to Starting Your Homestead', 'e-book', 'CA$14.99 (was CA$24.99)', 'stan.store'), P('FREE Emergency Kit E-Book', 'free e-book', 'free', 'stan.store', True)])
none('Tomahawk DIY', "Tom's Key Company free tool (third party)", ['affiliate'])
own('Visual Thinker', [P('Etsy Shop MidwoodMaps', 'own products (Etsy)', NF, 'etsy.com')])
none('Brent Hull', 'newsletter (Substack "The Blueprint")', ['newsletter'])
none('Apartment Maintenance Pro', 'own blog post with manuals')
own('HouseBarons', [P('Free Home Maintenance Checklist', 'free guide (newsletter sign-up)', 'free', 'beehiiv.com', True)], add=['newsletter'])
own('Roger the Pipe Guy', [P('100 Old-House Fixes That Save You Thousands', 'e-book (PDF, 200 pages)', '$19.99 (was $29.99); launch code LAUNCH25', 'rogerthepipeguybooks.com')], "the operator's own sister channel")
own('HomePro Hero', [P('DETAILED WORKBENCH PLANS (and metric)', 'plans (Etsy)', NF + ' (Etsy blocked)', 'etsy.com'),
                     P('FREE BASIC DIY WORKBENCH PLANS', 'free plans', 'free', 'kit.com', True)])
none('Ali Dymock', 'weekly newsletter', ['newsletter'])
own('The Craftsman Blog', [P('DIY Window Screen Plans (books & plans shop, courses)', 'plans', '$10', 'thecraftsmanstore.com')])
none('Homebuilding & Renovating', 'magazine website')
own('The 3D Handyman', [P('Kits (Etsy shop The3DHandyman)', 'own physical products', NF + ' (Etsy blocked)', 'etsy.com')])
own('Caliber8 Tools & DIY', [P('Power Tool Mastery Course', 'course', '$149.99', 'caliber8.com'), P('Home Improvement Planner', 'e-book', NF, 'caliber8.com')])
none('Help At My Home', 'own website')
none('Lifey Guy', 'third-party product links')
none('The Gizmo Garage', 'CATLINK product link (collabs.shop)', ['affiliate'])
none('Structure Tech Home Inspections', 'ROII initiative link')
none('These are quick reviews', 'VPN discount link', ['affiliate'])
own('DIY WISCO', [P('FREE cut list', 'free plans (email sign-up)', 'free', 'kit.com', True)])
none('Behind Your Walls', 'Inspector Swag Merchandise Store (store unavailable on 2026-10-26)', ['merch'])
own('Arthur Weber', [P("Arthur's Manual: 75 simple checks that catch small home problems early", 'e-book', NF + ' (page needs JavaScript)', 'arthurweberhome.com (Gumroad files)')])
# ---- tier C
own('Undecided with Matt Ferrell', [P('Become Energy Independent (solar guide, Undecided Academy)', 'video course', '$125 one-time', 'undecided.link')])
own('City Prepping', [P("The Prepper's Roadmap", 'course', NF + ' (page lists bonuses only)', 'cityprepp.ing'),
                      P('Start Preparing Survival Guide', 'free guide', 'free', 'cityprepp.ing', True)], 'sponsor: Incogni, "Use code PREPPING"', ['sponsor'])
none('Matt Risinger', 'newsletter; BUILD GEAR STORE', ['newsletter', 'merch'])
own('DIY Solar Power with Will Prowse', [P('guidebook to off-grid 12V solar', 'free e-book', 'free', 'willapproved.com', True)])
none('Just Have a Think', 'third-party free mini-courses')
own('Melissa K. Norris - Modern Homesteading', [P('The Family Garden Plan', 'book (retailers + bonuses)', NF, 'melissaknorris.com'),
                                                 P('Homemade Bread and Baking Course', 'course', NF + ' (page 404)', 'lpages.co')])
own('Artisan Electrics', [P('Electricians Business Academy (Skool community)', 'community/membership', NF, 'skool.com')], add=['membership'])
none('HomeSteadHow', 'newsletter', ['newsletter'])
own('Elias Yoder', [P('The Amish Home Savings Manual (700+ pages, Second Edition)', 'e-book', '$47 ("earn the $47 back")', 'eliasyoder.com -> eliasyoder.gumroad.com')])
own('Joshua De Lisle', [P('Sculpture designs (Etsy)', 'own products', NF, 'etsy.com')])
own('TheUrbanPrepper', [P('100 Preps Every Urban Family Should Have (field guide)', 'guide', 'page shows "$ 7" (not confirmed as the price)', 'theurbanprepper.com'),
                        P('20 Preps Gear Guide', 'free guide', 'free', 'bit.ly (Dropbox)', True)])
own('Jill Winger - Old Fashioned on Purpose', [P('Old-Fashioned on Purpose', 'book (retailers)', NF, 'oldfashionedbook.com')])
own('An American Homestead', [P('Homestead smoker building plans', 'plans', NF + ' (page 404)', 'anamericanhomestead.com')])
own('The Provident Prepper', [P('Integrated Passive Energy Greenhouse (IPEG) plans', 'plans', NF + ' (Payhip blocked)', 'payhip.com')])
own('Frugal Solutions', [P('Amish cookbooks (Digital Cookbook PDF)', 'e-books', '$9.99-$11.99', 'frugal-solutions.com')])
none('DavidPoz', 'affiliate battery kit links', ['affiliate'])
own('Eli Yoder Secrets', [P('The Complete Winter Library (incl. The One Warm Room Plan)', 'e-book bundle', '$97 (was $141)', 'eliyodersecrets.com -> payhip'),
                          P('The Borax Field Manual (and other single books)', 'e-book', '$27 (was $47)', 'eliyodersecrets.com')], 'also "The Warm Room Letter (for members)"')
none('Rockhill farm', 'newsletter', ['newsletter'])
own('Under the Median', [P('e-books shop (Frugal Finance Planner Bundle; Goal Wise: The Frugal Life Planner)', 'e-books/planners', '$47 each', 'underthemedian.com'),
                         P('Home Energy Savings Guide; Pantry Stock Up Workbook; grocery guide', 'free guides', 'free', 'underthemedian.com', True)])
none('Piney Grove Homestead', 'VEVOR product link', ['affiliate'])
own('Wonders', [P('The $0 Household Bible', 'e-book', '$27 (compare at $47)', 'householdbible.com')])
own('Dirtpatcheaven', [P('Compost Hotbed Instructions (Etsy)', 'instructions/plans', NF, 'etsy.com')])
own('Medieval Way', [P('The Medieval Bakery · The Complete Collection (3 e-books)', 'e-books', '$47 collection; single books $27-$29', 'medievalway.store')])
# fix 3.5 (round 3 fixer, 2026-10-26): the period comes from the round 3 checker's load of eivinandevekilcher.com/kilcher-camp
# on 2026-10-26 ("$25 JOIN MONTHLY"; "$250 JOIN FOR THE YEAR"; check-round3.md part 3 row 12).
own('Eivin Kilcher Homestead', [P('Kilcher Camp', 'membership community', '$25 a month or $250 a year ("$25 JOIN MONTHLY", "$250 JOIN FOR THE YEAR"; kilcher-camp page loaded 2026-10-26)', 'eivinandevekilcher.com')], add=['membership', 'merch'])
own('Everything Electric TECH', [P('The Fully Charged Guide to Electric Vehicles & Clean Energy', 'book (Amazon)', NF, 'buff.ly -> amazon.co.uk')])
none('The Solar Lab', 'review site with discount codes', ['affiliate'])
own('Medieval Wisdom', [P("The Medieval Wisdom Builder's Manual (PDF, 911 pages)", 'e-book', '$47 launch price through Oct 21, then $67', 'medieval-wisdom.com')])
own('Silas Mercer', [P('The Forgotten Frontier Journal ("Survive Any Crisis")', 'e-book', '$37 first-edition launch price', 'silasmercer.shop')], 'same site as Sylvie Mercer')
own('Greenhill Forge', [P('Project Notes', 'plans/notes', '£2-£11', 'greenhillforge.com')])
own('Bailey Line Road', [P('Cabin Building Course (Build your own tiny home)', 'course', NF, 'baileylineroad.com'), P('How-To & DIY eBooks', 'e-books', NF, 'baileylineroad.com'),
                         P('DIY Hoop House Plans', 'free plans', 'free', 'bit.ly', True)])
own("Bertha's House Hacks", [P('The Old Mexican Way', 'e-book (PDF)', '$39.99 today, was $59.99', 'oldmexicanway.com')])
own('Zach Of All Trades', [P('The 50 Dollar Food Plan', 'free guide', 'free', 'zachofalltrades.io', True)])
own('Hidden Homestead', [P('The Vault (22 forgotten Amish home formulas)', 'e-book', '$27 (was $47); Full Bundle $97', 'hidden-homestead-vault.pages.dev -> payhip')])
own('Forgotten American Survival', [P('Forgotten American Survival Library (5 Preparedness Manuals)', 'e-books', '$59 library; single books from $19', 'forgottenamericansurvival.com')])
own('Family DIY', [P('Etsy store terafoxua', 'own products', NF, 'etsy.com')])
none("There's A Trick For That", 'Ko-fi: "Have a personal question for me?" and "Book a consultation"', ['consulting'])
own('The Ready Life', [P('The Emergency Power Toolkit', 'workbook (digital)', '$9', 'thereadylife.com'),
                       P('CLASS: How to Heat & Power Your Home In a Long Term Blackout', 'class', NF, 'thereadylife.com'),
                       P('5:21 Preparedness Plan', 'program', NF, 'thereadylife.com')])
none('Off Grid with Jay and Jen', 'Shopify store (unavailable on 2026-10-26)', ['merch'])
own('Stefano Creatini', [P('Homestead Community (Skool, "complimentary $1,500 course")', 'community', NF + ' (page 404)', 'skool.com')], add=['membership'])
own('Wild Line', [P('The Passive Home Blueprint', 'e-book', NF + ' (page needs JavaScript)', 'passivehomeblueprint.com -> gumroad')])
own('Heat Geek', [P('COURSES - Become a MASTER of renewable heating', 'trade courses', NF + ' (page blocked, 429)', 'heatgeek.com')])
own('The Passive House Files', [P('The Complete Passive House Vault', 'e-book bundle', '$97 (was $200)', 'passivehousefiles.com -> stan.store'),
                                P('The Heat Files', 'e-book', '$37', 'passivehousefiles.com')])
own('ASIRI Designs', [P('A Design Guide To Dry & Comfortable Basements; A Guide To Moisture Management For Residential Remodels; Flat Roof Design Guides and CAD Details', 'e-books/design guides', NF, 'asiri-designs.com (teachable)')])
own('David McLuckie', [P('Ramp Plans', 'plans', NF, 'davidmcluckie.com')])
own('Builds With Eli Yoder', [P('The Energy Trap — Full Off-Grid Manual', 'e-book', '$27 (was $47)', 'energy-trap-vol1.netlify.app -> payhip'),
                              P('The Alternator Power Manual', 'e-book (41 pages)', '$49', 'manual.eliyodersecrets.com'),
                              P('The Complete Winter Power Library', 'e-book bundle', '$97 (was $230)', 'energy-trap-vol1.netlify.app')])
none('Build Show Network', 'newsletter', ['newsletter'])
none('Lone Star Prepping', 'product data sheet')
own('Earl Knows How', [P("Earl's Home Repair Manual", 'e-book', '$29.99, one time', 'earlknowshow.com -> gumroad')])
own('Ray Sutter', [P('When the Lights Go Out — The All-Hazards Home Survival Playbook', 'e-book (315 pages)', '$47 launch price (goes to $67)', 'raysutter.com -> gumroad')])
own('Healthy Home Guide', [P('Healthy Home Method', 'course', NF + ' (page lists module values only)', 'teachable.com'),
                           P('DIY Mold Inspection Guide and Checklist', 'e-book', '$29 (Gumroad)', 'healthyhomeguide.gumroad.com'),
                           P('Free masterclass: 5 mistakes...', 'free class', 'free', 'renegadeairquality.com', True)], add=['consulting'])
own('Mr iPoo', [P("The Mini AC Builder's Course", 'course', '$2.99 (was $15)', 'stan.store')], 'also "Become a channel sponsor" (membership)', ['membership'])
own('Frugal Frannie', [P("Frannie's Bill Book (120 tricks, 73 pages)", 'e-book', '$26 (was $47); 2-book bundle $46', 'frugalfrannie.com')])
own('Elias Homestead', [P('Elias Homestead Four-Volume Library', 'e-books', '$99 (was $191); single volumes $27 (was $44)', 'eliashomestead.shop -> gumroad')])
own('Prime Rundown', [P("The No-BS Buyer's Vault (7 guides)", 'e-books', '$47 launch price (was $79)', 'primerundown.com -> payhip')])
none('Construction Odyssey with Eddie', 'source links (ASHRAE)')
own('Jhon Construction', [P('The Complete Home Ledger (full bundle) / "The complete home library"', 'e-book bundle', '$97', 'jhon-construction.com -> payhip')])
own('UnpluggedTexan', [P('free wiring schematic pdf', 'free PDF', 'free', 'solarpdfdownload.com', True)])
own('Caleb Greer — Off-Grid Water & Power', [P('The Off-Grid Manual (368 pages)', 'e-book', '$47 (was $97)', 'calebgreeroffgrid.com -> gumroad')])
own('Grain & Gravity', [P('Grain & Gravity Field Manuals', 'e-books', NF, 'grainandgravity.com')])
own('Backyard Low Tech', [P('The Backyard LowTech Systems Manual (615 pages)', 'e-book', '$47', 'backyardlowtech.com -> gumroad')])
none('Everything Home', 'Heat Geek heat pump survey referral link', ['affiliate'])
none('Survival Smart HQ', 'links to the free guide on zachofalltrades.io (the channel Zach Of All Trades); cross-promotion, owner not stated')
own('Forgotten Home Engineering', [P('The Ultimate Thermal Retention Blueprint ("The Forgotten Blueprint")', 'e-book', '$47 launch price', 'pages.dev -> payhip')])
own('Sylvie Mercer', [P('The Forgotten Frontier Journal ("Survive Any Crisis")', 'e-book', '$37 first-edition launch price', 'silasmercer.shop')], 'same site as Silas Mercer')
own('Renewable Heating Hub', [P('The Ultimate Guide to Heat Pumps', 'book', NF, 'renewableheatinghub.co.uk'),
                              P('Heat Pump Fundamentals For Homeowners', 'course', '£19.95 one-time', 'learn.renewableheatinghub.co.uk')],
    'also "Buy Bodge Buster: Heat Pump Guide for Homeowners" (Amazon; authorship not confirmed)')
own("The Sensei's Home", [P("The Sensei's Home Manual", 'e-book', '$29.95', 'thejapanesehomemanual.com -> gumroad'), P('The House of Sensei Manual', 'e-book', '$29.95; both $44.95', 'thejapanesehomemanual.com')])
own('Christopher Johnson', [P("Christopher's Home Security Guide", 'e-book (15 chapters)', '£19 one-time', 'netlify.app')])
own('Eric George | Home Performance Pro', [P('Home Comfort Advisor course', 'course (incl. 30 minute 1 on 1 call)', NF, 'myhomecomfortadvisor.com')], add=['consulting'])
own('Sketchsurvive', [P('72-Hour Survival Blueprint (Essential)', 'e-book', 'special offer $12.00', 'systeme.io')])
own('Emmett Boone Prepping', [P('The Blackout Playbook (353 pages)', 'e-book', '$37', 'blackout-playbook.netlify.app -> gumroad')])
own('Eli Forgotten Ways', [P('The Forgotten Cooling System (full bundle)', 'e-book bundle', '$97', 'eliforgottenways.com')])
own('Old Ways Restored', [P('The Old House Ledger', 'e-book', '$27 (Gumroad)', 'oldwaysrestored.gumroad.com'),
                          P('The Passive Cooling Vault (68 pages)', 'e-book', '$57', 'oldwaysrestored.com'),
                          P('The Fan Country Test', 'free printable', 'free', 'oldwaysrestored.com', True)])
none('Outside In', 'software download links')
own('Earl Sizemore', [P('The $0-Bill House Protocol', 'e-book', '$27', 'liibro.com')])
own('Dick Colter Winterproof', [P('The Alaskan Way · Everything 66 Alaska Winters Taught Me', 'e-book', '$37 launch price ($47 later)', 'dickcolter.com -> gumroad')])
own('Donna Fixes', [P("Donna's Home Book (large-print edition 2026)", 'e-book', '$9.99 (was $19.99)', 'donnafixes.com')], 'free chapter too')
own('Linda Fairbrook', [P('The Prepared Home (and the five-book collection)', 'e-books', '$27 launch price for the collection (then $49)', 'lindafairbrook.com')])
own('Elias Mercer', [P('The Old Ways Handbook (83 chapters)', 'e-book', '$27', 'eliasmercer.com')])
none('BIG TICKET TRUTH', 'source links only')
own('Earl Appalachia', [P('The Man They Call When the Power Goes Out (93 methods)', 'e-book', '$47', 'earl.myreads.store -> gumroad')])
none('Attic Airflow Lab', 'source links only')
own('Jhon Survival Mode', [P('The Blackout Winter Plan', 'e-book', '$27', 'jhonsurvivalmode.netlify.app -> payhip'), P('The Complete Survival Mode Library', 'e-book bundle', '$97', 'jhonsurvivalmode.netlify.app')])
own('TheUnknownMarks', [P('The Winter Bill Manual (5 books)', 'e-books', '$47 (was $105)', 'theunknownmark.com -> gumroad')])
own('Jake Holloway', [P('Before the First Frost — 181 tricks for a warm house and a lower heating bill', 'e-book (51 pages)', 'page shows $15 and $25 (launch price; not tied in the text)', 'beforethefirstfrost.com -> payhip')])
own('Hank Dockery', [P('Hank Dockery Books (set)', 'e-books', '$37 launch price (then $69)', 'hankdockery.com -> payhip')])
own('Shelved Science', [P("Hal's Guides (three books)", 'e-books', '$45 launch price ($59 for all three)', 'halthebricklayer.com')])
own('Ray Donnelly DIY', [P('How to Keep Your Car Alive Forever ("147 Secrets Mechanics Don\'t Want You to Know")', 'e-book', '$37', 'keepyourcaralive.com')])
own('Gary Miller', [P('The Complete Home Preparedness Plan', 'e-book', '$29.99 (was $59.99)', 'garymillerprep.com')])
none('Under Your Home', 'free web guide on yarddrainagefixes.com')
own('Gene Halvorsen', [P('A Thousand Cold Houses (154 pages)', 'e-book', '$37 launch price, ends October 31, 2026, then $59', 'genehalvorsen.com (Stripe)')])
own('Japanese Offgrid Survival', [P('The Japanese Blackout Home', 'e-book', NF + ' (Payhip blocked)', 'payhip.com')])
none('Keith Smith', 'calendly meeting booking', ['consulting'])
own('Practical Home Energy', [P('The Energy-Saving Manual (508-page PDF)', 'e-book', '$27 launch price (was $47)', 'thepracticalhomeenergy.site -> gumroad')])
own('Simple Savings at Home', [P('Home Bills & Savings Binder', 'web app + printable PDF', '$47 one-time', 'juliehartley.gumroad.com')])
# ---- tier D
own('AC Service Tech LLC', [P('Mini Split Book and E-Book', 'book + e-book', 'page lists $39.99 / $49.99 / $99.99 (formats not matched)', 'acservicetech.com'),
                            P('Refrigerant Charging Book and E-Book (A/C BOOK)', 'book + e-book', 'page lists $39.99 / $49.99 / $99.99 (formats not matched)', 'acservicetech.com')])
own('HVAC School', [P('HVAC School app', 'app', NF, 'hvacrschool.com')], add=['app'])
none('Google Nest', 'brand')
none('AwesomeFramers', 'Part 107 drone course link ("Save $100 with this link")', ['affiliate'])
none('A2Z Construction', 'third-party masterclass')
none('Magic Touch: Fire & Air', 'Phoenix installer, "Book online"', contractor='y')
none('NS Builders', 'Modern Craftsman newsletter', ['newsletter'])
own('MEP Academy', [P('HVAC Training & Courses (e.g. Certified HVAC Piping Estimator Course)', 'courses', '$39-$795', 'courses.mepacademy.com'),
                    P('HVAC & Plumbing - Commercial Estimating Spreadsheet (and other spreadsheets)', 'spreadsheet', '$245 (Gumroad)', 'mepacademy.gumroad.com')])
none('Wickes', 'retailer brand')
own('Crawl Space Ninja', [P('DIY store (Mold Test Kit, mold cleaner, fogger)', 'own physical products', NF + ' (product pages 404)', 'diy.crawlspaceninja.com')], contractor='y')
none('Zach of All Trades', 'CourseCareers referral links', ['affiliate'])
none('Blue Collar Edu', 'CourseCareers referral links', ['affiliate'])
none('Hook Agency', 'own marketing agency ("Book here for $1,000 off")', ['consulting'])
none('PEX Universe', "brand's own store")
none('Adrian Garcia', 'Uppbeat music link (discount)', ['affiliate'])
none('Koolin’ with Krauss', 'RISION thermal camera link', ['affiliate'])
own('Digital Constructive', [P('California contractor license course', 'course', '$295 Basic / $395 Crash Course', 'digitalconstructive.com'),
                             P('Free Course', 'free course', 'free', 'digitalconstructive.com', True)])
none('Nighthawk HVAC', 'CourseCareers referral link', ['affiliate'])
none('Insight Control System', 'own blog post')
none('Baxi - sustainable heating and hot water solutions', 'manufacturer training')
none('eMotors Direct', 'retailer brand')
none('Fire & Ice Home Services', 'learning center on the company site', contractor='y')
own('HVACmillionaire', [P('his book ("Grab my book to grow your business")', 'book (Amazon)', NF, 'a.co'),
                        P('THE MOMENT | HVAC MASTERY ("Get The complete offer")', 'coaching program', NF, 'themoment.kit.com')],
    'spot check 2026-10-26 also found amazon.com links "Busyness-Busin..." and "Go-Make-Money-..." (book titles cut off; authorship not confirmed)', ['consulting'])
none('Alternative Heating & Supplies', 'retailer brand')
none('John Wilson | Owned and Operated', 'Service Scalers, Quick Staffers, Avoca (contractor-business sponsors)', ['sponsor'])
none('eFIXX ENERGY', 'GTEC insulation course (partner)')
own('HVAC Greatness by Pete Ramsey', [P('HVAC Services Pricing Workshop', 'course', NF + ' (discount code sub30atoz, 30% off)', 'hvac-greatness.thinkific.com'),
                                      P('HVAC "Level of Service" Flat Rate Price Book', 'price book', NF, 'hvac-greatness.thinkific.com')])
none('RetroFoamofMichigan', 'brand buying guide', contractor='y')
none('American Window Concepts', '"Build a Multi-Million Dollar Contracting Business" sign-up (kit.com)', ['newsletter'], contractor='y')
own('Powlas HVAC', [P('his book ("Buy My Book")', 'book (Amazon)', NF, 'amzn.to')])
own('Tim DeStasio HVAC', [P('Manual J Fundamentals (or the Season Pass)', 'live classes', '$50 for the first class (Eventbrite)', 'eventbrite.com')])
none('WarmlyYours', 'brand')
own('HVAC Pro Blog', [P('Free Rule of Duct Design PDF', 'free PDF', 'free', 'ck.page', True)])
none('Miles Pellet Stoves', 'pellet stove repair and parts business', contractor='y')
own('Mechanical PE Exam Prep', [P('FE Mechanical Exam Prep Course', 'course', NF + ' (page blocked)', 'bit.ly')])
none('Fuse Service: HVAC, Electrical & Plumbing', 'San Jose contractor, "Book your visit"', contractor='y')
none('HVACJess - The HVAC Diaries', 'manufacturer product links')
own('ProbeLem®', [P('ProbeLem SkillVault v1', 'digital pack', '$49 one-time', 'skills.probelem.com')])
own('HVAC Guide for Pros', [P('New HVAC Guide (and growth groups)', 'online guide', '$29 limited time ("$79 x $29")', 'newhvacguide.com')])
none('Foam University by RetroFoam', 'brand buying guide')
own('HVAC Technician Sales Secrets', [P('The Book For Sales Scripting', 'book', NF + ' (site did not load)', 'salesscriptingbook.com')])
none('Adam FUSE MAN', 'Dakota Prep course link (third party)', ['affiliate'])
none('Brandon Does HVAC', 'CourseCareers referral link ("Get $50 OFF")', ['affiliate'])
none('Buy Insulation Online', 'retailer brand')
own('MichaelJamesJohnson', [P('HVAC Profit Lab (Skool: coaching, courses, pricing tools)', 'paid community/course', '$497 shown (period not captured)', 'skool.com')], add=['membership'])
own('HVAC 2.0', [P('free quote onboarding', 'free course', 'free', 'mykajabi.com', True)])
own('Learn Engineering MEP', [P('Cooling Tower Book; Chiller Complete Book; HVAC Commissioning Book; HVAC Installation Complete Guide; AHU, FCU & CSU Master Guide; ASHRAE HVAC Master Guide', 'e-books (6)', NF + ' (Payhip blocked)', 'payhip.com')])
none('WarmZilla', 'retailer blog')
own('Rosa The Female HVAC Tech', [P('Gumroad store (products not named in the description)', 'digital products', NF, 'rosafemalehvactech.gumroad.com')])
none('Service-First-HVAC-Solutions', 'source link (EPA)')
none('Aced It! Cooling & Heating', 'online booking (housecallpro)', contractor='y')
none('Clade Engineering Systems', 'brand brochure')
own('No Degree Needed', [P('Complete HVAC License Playbook 2026', 'e-book', '$30 (Gumroad)', 'tinyurl.com -> gumroad'), P('Complete CDL Starter Kit 2026', 'e-book bundle', '$30', 'gumroad'),
                         P('Complete NEC Exam Cheat Sheet 2026', 'e-book', '$19', 'gumroad'), P('Complete Plumbing Playbook 2026', 'e-book', NF + ' (link 404)', 'tinyurl.com')])
# ---- channels found only in the own-website pass (not rule candidates), hand-added
own('Lars Halvorsen', [P('The Warm Side (three books)', 'e-books', '$29 launch offer for all three; library $37', 'larshalvorsen.com -> gumroad')])
own('The Hillbilly Way', [P('The Hillbilly Way (3 books)', 'e-books', '$59 (was $81)', 'thehillbillyway.com')])
none('Green Where It Suits', 'links to The Hillbilly Way (thehillbillyway.com/v/wonders) and The $0 Household Bible (householdbible.com), the product sites of the channels The Hillbilly Way and Wonders; read as cross-promotion, owner not stated', ['affiliate'])
own('Kate Sullivan Ready Living', [P("Kate Sullivan's Home Emergency Handbook", 'e-book', '$29.99 one time', 'katesullivanready.com -> gumroad')])
own('TheCheapFix', [P('The Hydrogen Peroxide Handbook (55 pages)', 'e-book', '$49', 'thecheapfix.netlify.app -> gumroad')])
own('WiseMoney', [P('Prepping Guide 2026 (The Household Readiness Manual)', 'e-book', '$30 one-time', 'preppingguide2026.shop')])
own('Old Maine Firewood', [P('The Old Maine Heating Manual', 'e-book', '$27', 'vercel.app -> payhip')])
own('Our Self-Reliant Life', [P('Off-Grid Guides (Ko-fi shop)', 'guides', NF + ' (Ko-fi blocked)', 'ko-fi.com')], add=['merch'])
own("Walter's Tool Talk", [P('The Vintage Tackle collection (collector guides)', 'e-books', 'bundle $79; guide $19 (was $27)', 'walterstooltalk.com')])

none('AprilAire', 'manufacturer (phone + "call us today" are product support, not a contractor)', contractor='n (manufacturer)')
# Round 3 fixer, 2026-10-26: 4 candidates that appeared once shortener targets were resolved (fix 3.1), read by hand.
none('Myks Garage', 'teslaunch.net is a third-party Tesla accessory shop; the description says "the above links are my Amazon affiliate links"', add=['affiliate'])
none('The Successful Contractor | by CertainPath', '"Book a free strategy call" (bit.ly -> mycertainpath.com/book-a-call): a coaching sales call', add=['consulting'])
none('Consumer Pick', 'its bit.ly links resolve to its own review site consumer-picked.com (articles, not a product)')
none('Mechanical Hub', 'bit.ly -> mechanical-hub.com/enewsletter: a newsletter sign-up', add=['newsletter'])
# fix 3.3 (round 3 fixer, 2026-10-26): Las Vegas HVAC company; both descriptions end "please visit our website at
# SierraCoolsLV.com" (plain text, no link) and the census D check has it as a contractor (check-round3.md part 3 row 14).
none('Sierra LLC Air Conditioning & Plumbing', 'contractor; own site SierraCoolsLV.com named in plain text', add=['own_website'], contractor='y')
none("Obadiah's Woodstoves", 'stove retailer', contractor='n (retailer)')
master = {r['name']: r['channel_id'] for r in csv.DictReader(open('/home/user/niche-research/studies/hvac/data/raw/channels-master-2026-10-24.csv')) if r['tier'] in 'ABCD' and r['tier']}
out, missing = {}, []
for n, v in R.items():
    if n not in master:
        missing.append(n); continue
    prods = v['own_products']
    v2 = {'name': n, 'note': v['note'], 'add': v['add']}
    v2['own_products'] = [f"{p['name']} [{p['kind']}] — {p['price']} — {p['domain']}" for p in prods]
    v2['own_products_detail'] = prods
    if 'contractor' in v: v2['contractor'] = v['contractor']
    out[master[n]] = v2
json.dump({'reviewed': '2026-10-26', 'by': 'round 3 what-it-sells helper (hand review of rule candidates + landing pages loaded 2026-10-26)',
           'note': 'own_products are as written on the description or landing page; prices only where shown; "price not found" otherwise. Free items have free=true.',
           'channels': out}, open('/home/user/niche-research/studies/hvac/data/raw/census-sells-review-2026-10-26.json', 'w'), indent=1, ensure_ascii=False)
print(len(out), 'reviewed; missing names:', missing)
