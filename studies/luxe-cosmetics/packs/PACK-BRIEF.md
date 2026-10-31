# Brief: the four research packs (round 2, 2026-10-31)

The operator, 2026-10-31: "i need more detail really. I have 0 knowledge on makeup. I do not care for brands red flags or any of that. find me also lists and lists of detailed reviews. i need 4 research packs, very detailed in simple english for a makeup and skincare idiot to understand."

One pack per product. Each pack has two parts, written by two helpers at the same time:
- **The explainer**: `packs/0N-<product>-pack.md`
- **The reviews**: `packs/reviews/0N-<product>-reviews.md`

They are joined into one pack afterwards.

| # | Product | ASIN | Earlier report to read first |
|---|---|---|---|
| 1 | Luxe Conditioning Peptide Mascara | B0GSXJCZ93 | `01-mascara.md` |
| 2 | Luxe PDRN Toner Pads (140) | B0HM229JP6 | `02-pdrn-toner-pads.md` |
| 3 | Luxe Korean Under Eye Balm (stick) | B0GYK3T766 | `03-under-eye-balm.md` |
| 4 | Luxe Eyelash Serum (3 mL) | B0C21JM5PY | `04-eyelash-serum.md` |

Also read `SUMMARY.md`, including section 7, the corrections. The earlier reports already hold much of the facts and comments. Reuse them and go much further.

## How to write (both parts)

- **The reader has never worn makeup or used skincare.**
  - Write as if explaining to a clever friend who knows nothing about the subject.
  - Use short sentences and everyday words.
  - Explain every beauty word the first time it appears, e.g. "lash line (the edge of the eyelid where lashes grow)".
  - Use examples and comparisons from daily life.
  - Use tables and numbered lists.
- **No extras.** Don't write about channel fit, video ideas or titles. The operator, mid-task: "dont tell me channel fits dont give me xtra things i just need you to perform this task".
- **Leave out the brand's red flags** (fake reviews, copied images, company structure); the operator doesn't want them. Two exceptions, each kept to one short line: what the operator **can't say** on camera (drug-type claims), and genuine **safety** points.
- **Keep the house rules** (CLAUDE.md):
  - Every figure says where it came from (URL) and when it was pulled.
  - Mark **[M]** for measured and **[R]** for your reading.
  - Never guess a number; write "not found".
- **Amazon blocks automated loads from this machine.** Don't try to get around that or any other site's bot check: no browser automation, no header tricks, no repeated retries. Reddit is blocked too.
- **Web search** is shared across helpers: keep to about 20 searches each.
- **NexLev and normal page loads don't count** against the search limit. Load the NexLev tools with ToolSearch: e.g. `mcp__NexLev__youtube_search`, `mcp__NexLev__youtube_video_comments`, `mcp__NexLev__get_video_transcript`, `mcp__NexLev__watch_youtube_video_and_ask`.

## The explainer: sections every pack has

1. **The basics from zero.**
   - What this kind of product is and what it's for.
   - How it works, plainly: the science in kitchen-table words.
   - The history and trend: why people are buying it now.
   - The types inside the category.
   - A glossary of every word the operator will hear.
2. **This exact product.**
   - Name, size, price, how long one lasts.
   - What it looks, feels and smells like (from reviews and videos).
   - **Every ingredient, one by one**: what it is in plain words and what it does.
   - The claims it makes.
3. **How to use it, step by step.** The common mistakes beginners make, and how long before you see anything.
4. **Where it fits in a routine.**
   - What to use before and after it, morning and night.
   - What it goes with, and what not to mix it with.
   - Simple example routines, including one for a woman over 60.
5. **Who it's for and who it isn't.**
   - By age, skin or lash type, eye type and budget.
   - How needs change with age, including what changes in the face, skin or lashes after 50 and 60, and why.
6. **Every problem the viewer has, one by one.** For each: what the problem is, why it happens, how it feels (with real quotes), what people have already tried and why that failed, and how this product helps or doesn't.
7. **How this product compares.**
   - The main alternatives, explained simply: what each is, price, what's different.
   - When someone should pick this product, and when something else.
8. **Questions viewers ask, with plain answers.** At least 25, taken from real comments and searches.
9. **Myths and truths.**
10. **The words viewers use.** Their phrases, complaints and wishes, word for word.
11. **Safety, and what you can and can't say on camera.** Short.
12. **Sources.**

## The reviews: what the review helper collects

- **"Lists and lists": aim for at least 150 real, detailed reviews or comments per product.**
  - Prefer long ones that tell a story: the problem before, what they tried, what happened, how long it took.
  - Quote each word for word, with:
    - the source (URL or video ID)
    - the date
    - the star rating or likes
    - the reviewer's stated age, skin, lash or eye type, if given
- **Label every review with the exact product it is about.** Order of preference:
  1. The Luxe product itself, from any source.
  2. The same formula elsewhere: for the pads, Anua PDRN 100 Hyaluronic Acid Glow Pad has the identical ingredient list.
  3. Close rivals of the same type.
  4. The category in general.
- **Where to look** (all normal page loads, no workarounds):
  - The Luxe stores' own review widgets: luxe.com, luxeresearchlab.com and other country stores. Many Shopify review apps (Judge.me, Yotpo, Okendo, Stamped, Loox, Reviews.io) serve public review data. Label these "brand's own site".
  - YouTube review videos and their comments (NexLev): the richest source.
  - Rival brands' own sites and their review widgets.
  - Ulta, Target, Walmart, Cult Beauty, YesStyle, Stylevana, Olive Young Global, dodoskin, iHerb and Trustpilot product pages, if they load normally.
  - Amazon review text that appears in search snippets.
- **Group the reviews by theme**, with a count for each theme:
  - the problem solved
  - results and how long they took
  - texture and feel
  - how easy it is to use
  - complaints and failures
  - side effects
  - price and value
  - reviews from people over 50
  - before-and-after stories
- **At the top:** a short "what the reviews tell us" summary in simple English.
- **Save raw pulls** in `data/reviews/<product>/`.
