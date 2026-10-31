# Check of 05-brand-audience-and-selling-rules.md

Checking helper, 2026-10-31. I re-pulled every source myself today and did not rely on the first helper's saved files. Pages were loaded once each with plain curl. Trustpilot and ftc.gov refused scripted loads (403 / 404), so I read them through WebFetch, which returns a model summary and not the raw page. Amazon.com product pages were not touched. The Amazon Associates help pages (affiliate-program.amazon.com) loaded normally with no bot check.
Budget used: 2 web searches; 7 WebFetch loads; NexLev: 2 video-detail calls and 2 comment pulls.
My own downloads are in the session scratchpad and are not committed.

Verdicts: **Confirmed** = the source says what the report says. **Wrong** = the source says something different. **Partly** = the core is right, but a detail is wrong or overstated. **Unverifiable** = the primary source could not be checked.

---

## Summary table

| # | Claim in report | Verdict |
|---|---|---|
| 1a | Luxe Cosmetics B.V., Helmond, KvK 89968336, founded 19-04-2023, Micro, 1 FTE | Confirmed (imprint + liza.nl KvK mirror; not the KvK register itself) |
| 1b | Postcode mismatch, 5708 HN (imprint) vs 5707 CW (mirror) | Confirmed |
| 1c | "Luxecosmetics LLC" named in the luxe.com terms; "state not found" | Partly. The name is right, but the terms give a **Wyoming** address and Wyoming courts (see below), which the report missed |
| 1d | Luxe Research LLC, 30 N Gould St Ste R, Sheridan WY 82801, +1 (385)-454-6193 | Confirmed |
| 1e | 30 N Gould St is a registered-agent hub | Not re-checked (no search spent; the report relies on a search snippet) |
| 1f | SellerRatings: LuxeCosmetics 4.2/5 from 1,386, since 2023, ranked 317th (from 532nd) | Confirmed |
| 1g | luxe.com and luxeresearchlab.com are one business | Confirmed as a reading, with new evidence. **They do not share a checkout**: they are two separate Shopify stores. Their contact details differ, and so do their refund policies |
| 2a | The same six "Verified Buyer" testimonials on the balm and pads pages (same names and dates, stories rewritten) | Confirmed |
| 2b | Diane K. is 52 on the balm page and 42 on the pads page | Confirmed (the other five ages match) |
| 2c | The pads testimonials carry the balm price "$34.99 $39.95" | Confirmed |
| 2d | "Rated 4.86 (10,839 reviews)" on "every page checked" | Partly. On the pads page and the luxe.com balm page, yes. The luxeresearchlab.com balm page shows only "Rated 4.8/5 based on +10,839 Total Ratings" |
| 2e | Mascara feed tag "static_reviews_658" | Confirmed, and it is not a one-off: about 34 luxe.com products carry a "static_reviews_N" tag |
| 3a | Trustpilot 3.8, 4,322 reviews, 17% one-star, domain luxe-cosmetics.com | Confirmed (via WebFetch summary) |
| 3b | One-star quotes | Two confirmed (short sentences), but only through the summariser. Raw text is unverifiable |
| 4a | FTC Endorsement Guides / Disclosures 101 / FAQ lines ("in the video", "paid link", audible) | Confirmed |
| 4b | June 2023 release: platform tool "might not be an adequate disclosure"; virtual influencers | Confirmed |
| 4c | 16 CFR 465: announced 14 Aug 2024, effective 21 Oct 2024 | Confirmed (Federal Register: "This rule is effective October 21, 2024.") |
| 4d | 465 bans testimonials from people who "lacked real experience" | Partly. The meaning is right, but the quoted words are not the FTC's (see below) |
| 4e | Civil penalty $53,088 per violation ("not checked against the CFR text") | Confirmed against 16 CFR 1.98, **and still current**: the FTC published on 15 Sep 2026 that there is no 2026 adjustment |
| 4f | Amazon required statement; agreement dated Oct 15, 2025; policies dated Apr 14, 2026 | Confirmed |
| 4g | Amazon prices: "allowed only with a date/time stamp" / "Never speak prices" | Partly wrong. The date/time stamp rule is a condition of the API licence. The core rule is different (see below) |
| 4h | Amazon reviews/star ratings only through Creators API / PA API | Confirmed |
| 4i | Amazon cookie: "Amazon's standard 24-hour rule was not found on the pulled pages" | Wrong. The 24-hour session is in the Program Policies |
| 4j | Commission: Luxury Beauty 10%, Beauty 3%, Health & Personal Care 1% | Confirmed |
| 4k | YouTube paid-promotion wording | Confirmed |
| 4l | FDA cosmetic vs drug: "restore hair growth"; collagen/wrinkle lines; page dates | Confirmed. FDA's pages have no eyelash-specific example; the 2011 Lifetech letter is secondary-sourced only |
| 4m | MoCRA: small-business exemption does not cover eye-mucous-membrane products; final recall guidance 29 Oct 2026 | Confirmed |
| 5a | "Eye Doctor Explains How to Get Rid of Under EYE BAGS": 9,090,612 views | Confirmed (9,090,668 today; normal growth) |
| 5b | "Why I Don't Use Lash Growth Serums as a Dermatologist": 539,346 views | Confirmed (exactly 539,346 today) |
| 5c | @marystewart5555, 334 likes | Confirmed, word for word |
| 5d | @Anne-ux3ex, 509 likes | Confirmed likes. The quote is an excerpt without ellipses (it drops "Well Holy Mackerel!" at the start and "Bless you!" at the end) |

---

## 1. Company facts

### 1a/1b. Luxe Cosmetics B.V. (confirmed)
- https://luxe.com/pages/imprint (pulled 2026-10-31): "Onlineshop is managed by: Luxe Cosmetics B.V. / De Wieken 3 / 5708 HN HELMOND / Nordbrabant / KvK-number: 89968336 / E-Mail: info@luxe-cosmetics.com / Phone number: +49 17695833240". Footer: "Copyright © 2025 Luxe Cosmetics LLC All rights reserved".
- https://www.liza.nl/en/89968336/luxe-cosmetics (pulled 2026-10-31): "Luxe Cosmetics (BV) - Helmond (5707 CW) - 89968336"; "Luxe Cosmetics was founded on 19-04-2023."; "Micro", "1 FTE"; "The current registered office of Luxe Cosmetics is located at De Wieken 3, 5707 CW Helmond."
- Note: liza.nl is a third-party mirror of the KvK (Dutch Chamber of Commerce) data. The KvK register itself was not loaded.

### 1c. "Luxecosmetics LLC" (partly: the state is findable)
- https://luxe.com/policies/terms-of-service ("Last updated: October 30, 2026"): the site is "owned and maintained by Luxecosmetics LLC". The arbitration opt-out address is "LUXECOSMETICS LLC ATTN. LEGAL DEPARTMENT, 5830 E 2ND ST STE 7000 #9063 CASPER, WY 82609". The DMCA agent is "Luxecosmetics LLC … 5830 E 2nd St Ste 7000 #9063 Casper, WY 82609." The terms also say Luxe may sue "IN THE STATE OR FEDERAL COURTS OF WYOMING".
- The report says the LLC's state is "not found". The terms do not name a state of formation, but they do give a **Wyoming (Casper) legal address** and Wyoming courts. Reading: the LLC is very likely a Wyoming LLC. That is not confirmed from the Wyoming registry.

### 1d. Luxe Research LLC (confirmed)
- https://luxeresearchlab.com/ footer (pulled 2026-10-31): "Copyright 2026 Luxe Cosmetics LLC" … "Luxe Research LLC / 30 N Gould St Ste R Sheridan, WY 82801 United States / info@luxeresearchlab.com / +1 (385)-454-6193 (9:00-16:00 MST, UTC-7)".

### 1f. SellerRatings (confirmed)
- https://www.sellerratings.com/amazon/usa/luxecosmetics (pulled 2026-10-31): "LuxeCosmetics 1,386 reviews | 4.2 out of 5". "They have been selling on the Amazon.com marketplace since 2023. They offer several dozen products. They are a Top 500 Amazon.com seller, ranked 317th overall. They have improved from the 532nd position last month."

### 1g. One business? (confirmed as a reading; no shared checkout)

| Test | luxe.com | luxeresearchlab.com | Same? |
|---|---|---|---|
| Shopify store (checkout) | `luxe-cosmetics-us.myshopify.com`, shopId 65177583874 | `luxe-cosmetics-denmark.myshopify.com`, shopId 71803797810 | **No**: two separate stores and checkouts. Both store names start "luxe-cosmetics-" |
| Footer copyright | "Copyright © 2025 Luxe Cosmetics LLC" | "Copyright 2026 Luxe Cosmetics LLC" | Yes |
| Terms: owner | "Luxecosmetics LLC" | "Luxe Research LLC" | Different LLC names |
| Terms: legal address | "5830 E 2ND ST STE 7000 #9063 CASPER, WY 82609" | "5830 E 2ND ST STE 7000 #9063 CASPER, WY 82609" | **Yes, identical** |
| Terms text | Wyoming arbitration, "Last updated: October 30, 2026" | The same clauses, same date | Yes (one template) |
| Email / phone | info@luxe-cosmetics.com, support@luxe-cx.com, +49 17695833240 | info@luxeresearchlab.com, +1 (385)-454-6193 | No |
| Refund policy | 30 days; "Return shipping will be to the Netherlands as that is where our warehouse is located."; support@luxe-cx.com | "Our 30-Day "We'll Make It Right" Guarantee"; info@luxeresearchlab.com; "In most cases where the issue is product-related … we'll cover return shipping." | No: different policies |
| "Members" line | "Join over 1,197,000+ members…" | the same line | Yes |
| Shopify feed vendor crossover | luxe.com eye balm vendor = "Luxe Research" | luxeresearchlab PDRN pads vendor = "Luxe Cosmetics US" | Yes |

Sources: the home pages, terms and refund pages of both sites, plus https://luxe.com/products.json and https://luxeresearchlab.com/products.json, all pulled 2026-10-31. (The luxeresearchlab feed shows 30 products today; the report counted 31.)
**Verdict:** the report's "one business" reading holds, and the identical Casper legal address makes it stronger. The operator should know, though, that the two shops have **separate checkouts, separate support contacts and different refund rules**. A viewer's experience will differ depending on which shop they land on.

---

## 2. Testimonials and badges

### 2a–2c. Duplicated "Verified Buyer" testimonials (confirmed)

| Name | Balm page age / date | Pads page age / date | Balm text (opening) | Pads text (opening) |
|---|---|---|---|---|
| Margaret T. | 56 / Feb 11th, 2026 | 56 / Feb 11th, 2026 | "I'm 56. I sleep fine, drink water, do everything right. But my eyes never got the memo." | "I eat well. I sleep. I drink my water. My skin never got the memo." |
| Diane K. | **52** / Jan 24th, 2026 | **42** / Jan 24th, 2026 | "La Mer. Estée Lauder. … I'm genuinely angry nobody told me about this sooner tbh." | "La Mer. SkinCeuticals. … I'm genuinely annoyed nobody told me about PDRN sooner." |
| Susan L | 47 / Feb 18th, 2026 | 47 / Feb 18th, 2026 | "I've made peace with most of aging." | "I'd made peace with most of it." |
| Linda R. | 51 / Jan 13th, 2026 | 51 / Jan 13th, 2026 | "Every single morning. Put on concealer." | "My routine used to be: cleanse, apply three different products…" |
| Carol A | 63 / Feb 15th, 2026 | 63 / Feb 15th, 2026 | "…The dark circles are visibly lighter." | "Retinol made my skin peel for three weeks straight." |
| Barbara M | 43 / Dec 28th, 2025 | 43 / Dec 28th, 2025 | "I used to angle my face or insist on bad lighting…" | "I started early with SPF and serums." |

- Pads page price line under each testimonial: "Luxe - PDRN Toner Pads $34.99 $39.95". Those are the balm's prices; the pads sell for $59.95.
- Sources: https://luxeresearchlab.com/products/luxe-korean-under-eye-balm and https://luxeresearchlab.com/products/luxe-pads (pulled 2026-10-31). The same six names, ages and dates also appear on https://luxe.com/products/luxe-korean-under-eye-balm-1 ("Margaret T., 56 ✓ Verified Buyer 📅 Purchased on Feb 11th, 2026", "Diane K., 52", and so on).

### 2d. Badge (partly)
- "Rated 4.86 (10,839 reviews)" appears on the pads page and on the luxe.com balm page.
- The luxeresearchlab.com balm page does **not** show "4.86". It shows "Rated 4.8/5 based on +10,839 Total Ratings", a line that also appears on the pads page.
- The luxe.com balm page also says "10,839 women 45+ swapped their old eye cream…" and "Over 10,839 Women Already Reordered."
- The report's "same figure on every page checked" holds for the **10,839** count, but not for the exact "4.86" badge.

### 2e. static_reviews (confirmed, and wider than reported)
- https://luxe.com/products.json: "Luxe Conditioning Peptide Mascara", handle `conditioning-mascara`, created 2023-12-06, tags `['static_reviews_658']`.
- About 34 other luxe.com products carry the same kind of tag, for example `static_reviews_1792` (Hair Growth Shampoo), `static_reviews_1252` (Marula Oil) and `static_reviews_135` (Waterproof Eyeliner).
- Reading: the review counts look like fixed numbers set in the shop's tags, not live counts.

---

## 3. Trustpilot (confirmed through the summariser only)

- https://www.trustpilot.com/review/luxe-cosmetics.com?stars=1. Plain curl got 403, so I read it through WebFetch on 2026-10-31.
- Returned: "Company name: Luxe Cosmetics; Domain: luxe-cosmetics.com; TrustScore: 3.8; Total reviews: 4,322; Star distribution: 5-star 60%, 4-star 13%, 3-star 7%, 2-star 3%, 1-star 17%". Page title: "Luxe Cosmetics Reviews | Read Customer Service Reviews of luxe-cosmetics.com".
- The profile is for **luxe-cosmetics.com**, the old domain that now redirects to luxe.com. It is not the luxeresearchlab.com profile.
- Two one-star reviews, as returned by the summariser on two separate loads:
  1. Emily Berenback, 1★, October 23, 2026: "Purchased the buy 1 get 1 but only received 1 foundation."
  2. Carrianne Kuss, 1★, October 29, 2026: "This is translucent to my skin."
  - Also returned: Candy, 1★, Oct 28, 2026: "I have been trying to contact Luxe for a return and refund."
- Caveat: WebFetch would not return full review texts ("I can't reproduce the full review text verbatim"). These short sentences match the first helper's notes, but word-for-word accuracy against the raw page is **unverifiable** from this machine. Re-read them in a normal browser before quoting any of them on air.
- The 1-star filter page shows 20 one-star reviews (Sep 25 to Oct 30, 2026) plus 4 four-star reviews in a side block. The summaries are about foundation, checkout, subscriptions, support and BOGO orders. None was about the mascara, lash serum or pads, which agrees with the report. The report's quote "This is translucent to my skin. It does nothing whatsoever!!!!!" is consistent with the summary ("does nothing"); only the first sentence was confirmed verbatim.

---

## 4. The legal lines

### 4a. FTC Disclosures 101 and Endorsement Guides FAQ (confirmed)
- https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers (via WebFetch, 2026-10-31; page dated "November 2019"):
  - "the disclosure should be in the video and not just in the description uploaded with the video"
  - "Viewers are more likely to notice disclosures made in both audio and video."
  - "Don't use vague or confusing terms like "sp," "spon," or "collab,"" and stand-alone "thanks" or "ambassador"
  - "Disclose when you have any financial, employment, personal, or family relationship with a brand."
  - "such as scientific proof that a product can treat a health condition". The report has "treats"; the page says "can treat". The difference is trivial.
- https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking (via WebFetch):
  - "“Paid link” right next to an affiliate link should be an adequate disclosure of the nature of the link."
  - "“Commissionable link” is probably not a clear disclosure."
  - "I get commissions for purchases made through links in this post."
  - "You should disclose the affiliate relationship both in the videos and in the description near the links."
  - "If the representation is made audibly, the disclosure should be made at least audibly."
  - "the best place for the disclosure would be right before or at the beginning of the actual endorsement."
  - "You can’t talk about your experience with a product if you haven’t tried it."
- 16 CFR 255 (eCFR, current; source 88 FR 48102):
  - § 255.0 "clear and conspicuous": "if the representation is made through audible means, the disclosure should be made in at least the communication's audible portion".
  - The same definition adds a line the report does not use: **"When an endorsement targets a specific audience, such as older adults, “ordinary consumers” includes members of that group."** This bears directly on the 50+/60+ channels.
  - § 255.2: "Endorsers may be liable for statements made in the course of their endorsements … including when an endorser falsely represents that they personally used a product."

### 4b. FTC 29 June 2023 release (confirmed)
- https://www.ftc.gov/news-events/news/press-releases/2023/06/federal-trade-commission-announces-updated-advertising-guides-combat-deceptive-reviews-endorsements (via WebFetch): dated "June 29, 2023". It says "a platform's built-in disclosure tool might not be an adequate disclosure" and that the definition of "endorsements" was changed to clarify its scope regarding "virtual influencers".
- The word "virtual" does not appear in the 16 CFR 255 text itself; the clarification is in the release and preamble.

### 4c–4e. Consumer Review Rule, 16 CFR 465 (dates confirmed; one quote wrong; penalty confirmed)
- Federal Register API, document 2024-18519: published 2024-08-22, citation "89 FR 68034", "This rule is effective October 21, 2024." eCFR Part 465 source line: "89 FR 68077, Aug. 22, 2024".
- FTC release, 14 Aug 2024 (via WebFetch): "The rule will become effective 60 days after the date it’s published in the Federal Register." The rule lets the FTC "seek civil penalties against knowing violators."
- **Wording:** the phrase "lacked real experience" is **not** in the release or in the CFR.
  - Release: reviews that "misrepresent that they are by someone who does not exist, such as AI-generated fake reviews", or that come from people who "did not have actual experience with the business or its products or services".
  - 16 CFR 465.2(a)(2): "That the reviewer or testimonialist used or otherwise had experience with the product…"
  - The report should not put "lacked real experience" in quotation marks.
- **Penalty:** 16 CFR 1.98 (eCFR current, source "90 FR 5581, Jan. 17, 2025") says the amounts "apply only to penalties assessed after January 17, 2025" and lists "Section 5(m)(1)(A) of the FTC Act, 15 U.S.C. 45(m)(1)(A)—$53,088". The latest FTC notice is Federal Register 2026-18853, published 2026-09-15 (https://www.federalregister.gov/documents/2026/09/15/2026-18853/civil-penalty-inflation-adjustments): "the Federal Trade Commission ("FTC")'s civil penalty amounts will remain unchanged during 2026. The FTC will continue to apply the 2025 civil penalty levels." So **$53,088 per violation is current** as of 2026-10-31. The report's "not checked against the CFR text" caveat can now be dropped.

### 4f–4j. Amazon Associates (mostly confirmed; prices and cookie corrected)
- Operating Agreement, https://affiliate-program.amazon.com/help/operating/agreement: "Updated: October 15, 2025". "You must clearly and prominently state the following … “As an Amazon Associate I earn from qualifying purchases.”" "Site" covers "your website, social media user-generated content, online software application, or Alexa skill", so a YouTube channel counts as a "Site".
- Program Policies, https://affiliate-program.amazon.com/help/operating/policies: "Updated: April 14, 2026."
  - **Prices (report partly wrong):** "your Site may only show prices and availability if: (a) we serve the link in which that price and availability data are displayed, or (b) you obtain Product pricing and availability data via Creators API or PA API and you comply with the requirements…".
    - The date/time stamp line sits in the API licence and is conditional: "You will include a date/time stamp adjacent to your display of pricing or availability information on your application if you obtain Product Advertising Content from Data Feeds, or if you call Creators API, PA API or refresh … less frequently than hourly."
    - So the rule is not "prices allowed with a timestamp". The rule is "prices only through Amazon-served links or API data". A hand-typed or spoken price fits neither route. The report's practical advice ("check the link for today's price") still stands, and on a stricter basis.
  - Reviews: "(t) You will not display or otherwise use any of our customer reviews or star ratings, in part or in whole, on your Site unless you have obtained a link to that customer review or star rating through Creators API or PA API…". Confirmed.
  - "(v) You will not cloak, hide, spoof, or otherwise obscure the URL…" and "(w) You will not use a link shortening service, button, hyperlink or other ad placement in a manner that makes it unclear that you are linking to an Amazon Site." Confirmed.
  - Offline: "any printed material, ebook, mailing, or any oral solicitation". Confirmed.
  - "You must not make inaccurate, overbroad, deceptive or otherwise misleading claims about any Product…". Confirmed.
  - **Cookie (report wrong):** the 24-hour session **is** in the Policies. A qualifying session ends at the first of: "(x) 24 hours elapse from that click, (y) the customer places an order…".
- Commission table, https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ (footer "© 1996-2025"):
  - "Luxury Beauty, Luxury Stores Beauty, Amazon Explore 10.00%"
  - Beauty in the "3.00%" row
  - "Health & Personal Care" in the "1.00%" row
  - Confirmed. Which category the four products fall in is still a reading.

### 4k. YouTube paid promotion (confirmed)
- https://support.google.com/youtube/answer/154235 (pulled 2026-10-31): "If you feature branded content, sponsorships, endorsements, or other commercial relationships in your videos, you have to let YouTube know by selecting the paid promotion button in your video details. Selecting the paid promotion button adds a disclosure label that appears at the beginning of your video." "You and the partners you work with are also responsible for understanding and complying with all applicable legal requirements." The report drops the word "also"; this is trivial.

### 4l. FDA cosmetic vs drug (confirmed; eyelash example is secondary only)
- https://www.fda.gov/cosmetics/cosmetics-laws-regulations/it-cosmetic-drug-or-both-or-it-soap ("Content current as of: 09/11/2024"):
  - "articles (other than food) intended to affect the structure or any function of the body of man or other animals"
  - "for cleansing, beautifying, promoting attractiveness, or altering the appearance"
  - "Claims stated on the product labeling, in advertising, on the Internet, or in other promotional materials."
  - "Some examples are claims that products will restore hair growth, reduce cellulite, treat varicose veins, increase or decrease the production of melanin (pigment) in the skin, or regenerate cells."
  - Note: "regenerate cells" is relevant to the pads' "regenerative" wording, and "increase or decrease the production of melanin" to dark-spot claims. The report could add both.
- https://www.fda.gov/cosmetics/cosmetic-products/wrinkle-treatments-and-other-anti-aging-products ("Content current as of: 02/25/2022"):
  - "if a product is intended to make lines and wrinkles less noticeable, simply by moisturizing the skin, it’s a cosmetic."
  - "if a product is intended, for example, to remove wrinkles or increase the skin’s production of collagen, it’s a drug or a medical device."
  - Confirmed.
- **Eyelash growth:** neither FDA page gives an eyelash-specific example; the general "restore hair growth" line is the one that applies. The FDA eye-cosmetic page (https://www.fda.gov/cosmetics/cosmetic-products/eye-cosmetic-safety) covers tints ("…serious eye injuries, including blindness"), extensions and mascara disposal ("two to four months after purchase"), but not growth serums.
- The 2011 Lifetech/RapidLash warning letter is backed only by trade-press search results (cosmeticsdesign.com 2011-04-26, law360.com/articles/240624, cosmeticsandtoiletries.com). The FDA letter itself was not loaded: **unverifiable at primary level**.

### 4m. MoCRA (confirmed)
- https://www.fda.gov/cosmetics/cosmetics-laws-regulations/modernization-cosmetics-regulation-act-2022-mocra ("Content current as of: 10/29/2026"):
  - "MoCRA exempts certain small businesses from GMP, registration, and product listing requirements. However, such exemptions do not apply to manufacturers or facilities that manufacture or process the following cosmetic products: Products that regularly come into contact with mucus membrane of the eye under customary or usual conditions of use."
  - Adverse events must be reported "within 15 business days".
  - "October 29, 2026: FDA issued a final guidance document for the cosmetics industry…"
  - The page's entry does not name the guidance's subject; it links "Questions and Answers Regarding Mandatory Cosmetics Recalls". The report's "final guidance on mandatory cosmetic recalls on 29 October 2026" is likely right but is not stated in one sentence on the page.
- The report's reading that mascara and lash serum fall in the eye-mucous-membrane group is reasonable, but it is still a reading.

---

## 5. YouTube (NexLev, 2026-10-31)

| Item | Report | NexLev today | Verdict |
|---|---|---|---|
| hql6k88BKP8 "Eye Doctor Explains How to Get Rid of Under EYE BAGS" (Doctor Eye Health, published 2021-05-11) | 9,090,612 views | viewCount "9090668", likeCount "202636" | Confirmed (+56 views since the first pull) |
| tiRLNc6_A0E "Why I Don't Use Lash Growth Serums as a Dermatologist" (Dr. Sam Ellis, published 2021-06-09) | 539,346 views | viewCount "539346", likeCount "12668" | Confirmed exactly |
| @marystewart5555 on tiRLNc6_A0E | 334 likes; "Can you share brands that are safer that some of your patients have had success with please?" | likesCount "334"; the same text | Confirmed word for word |
| @Anne-ux3ex on mx6mhz5cqjU | 509 likes; "I am 64 years old … emphasized the bags." | likesCount "509"; full text: "Well Holy Mackerel! I am 64 years old and that was the first time anyone has shown me how to deal with my under eye bags. Every sales rep at every major cosmetics counter just sold me a concealer and told me to put it under my eyes which, of course, emphasized the bags. Bless you!" | Confirmed. The report's quote is a trimmed excerpt without "…" marks |

Also seen: the top comments on tiRLNc6_A0E include @Nini-tj6se, "Can you recommend serums that dont have these ingredients" (**290 likes**, 45 replies). That is the same "safe serum" theme as row 7 of the report's worry table, and the report does not quote it.

---

## Corrections the report needs (for the operator's approval; I have not edited the report)

1. §1.1 / §5: "state not found" for Luxecosmetics LLC. The terms give a Wyoming legal address (5830 E 2nd St Ste 7000 #9063, Casper, WY 82609), the same address Luxe Research LLC uses, and Wyoming courts.
2. §1.2: add that luxe.com and luxeresearchlab.com are **separate Shopify stores** (separate checkouts) with different support contacts and refund policies, although the legal address and copyright line are the same.
3. §1.4 / R2: the exact "4.86" badge is not on the luxeresearchlab balm page (it shows "4.8/5 … +10,839"). "static_reviews_N" tags are on about 35 products, not only the mascara.
4. §4.2: replace the quoted "lacked real experience" with the FTC's words, "did not have actual experience". The $53,088 figure is confirmed in 16 CFR 1.98, with no 2026 change (FR 2026-18853, 15 Sep 2026).
5. §0 item 9 / §4.4: Amazon's price rule is "prices only via Amazon-served links or Creators/PA API data". The date/time stamp is an API-licence condition, not a general permission.
6. §4.5: the Amazon cookie is a 24-hour session (Program Policies), not "not found".
7. §3.2: mark the @Anne-ux3ex quote as an excerpt.
8. Optional additions: 16 CFR 255.0 "older adults" line; FDA's "regenerate cells" and "melanin" drug-claim examples (relevant to the pads).
