# LUXE Cosmetics: Facebook video ads and YouTube thumbnails, broken down

Pulled and analysed 2026-11-07. Audience: women 50+.

## Failed downloads (read first)
| # | Link | Error |
|---|---|---|
| 1 | https://www.facebook.com/share/r/1M5aty5ZFw/ | yt-dlp 2026.10.26: `ERROR: [facebook] 1382518750622132: Cannot parse data; please report this issue on https://github.com/yt-dlp/yt-dlp/issues?q= ...` The `/reel/` and `/watch/?v=` forms of the link failed the same way. The other 14 needed no login. The next step would be `--cookies-from-browser chrome` on a computer logged into Facebook; this cloud machine has none, so nothing else was tried. |

YouTube also blocked yt-dlp here ("Sign in to confirm you're not a bot"), so the **titles come from YouTube's public oEmbed page** and the views, likes and descriptions from NexLev. The thumbnails downloaded normally (maxresdefault for 10, hqdefault for 9vnKwyKh08Q).

## Duplicates (measured, by MD5)
- **#6 and #7 are the same video file** posted twice by Minho Makeup & Beauty.
- **#13, #14 and #15 are the same video file** posted three times by Jiho Beauty. **#12** is the same edit re-encoded (identical audio and transcript, no visible difference). **#10 and #11** are likewise one edit encoded twice.
- The full breakdown is written once in the earliest or master post's section; the duplicate sections give their own metadata and point there.

## How this was made
- **Download:** `yt-dlp` with `--write-info-json`. The metadata table is in `videos/METADATA.md` (repeated below).
- **Transcripts:** faster-whisper `medium.en` with segment timestamps, in `transcripts/<n>.txt`. Brand names are machine-heard; the breakdowns correct them from the packaging and say so.
- **Frames:** `ffmpeg`, 1 per second for 0–4 s, then every 2 s (5, 7, 9 …). They are in `frames/<n>/tNNN.jpg` (NNN = seconds). Labelled contact sheets are in `frames/<n>/sheets/`.
- **Checks:** every sheet was looked at. A second helper re-checked a sample from 8 of the breakdowns against the transcripts, frames and metadata: 40 quotes, 24 on-screen texts, the metadata, product timings and the watermark. No material errors; 3 small label/position errors were fixed.
- **Views:** Facebook shows two numbers. `view_count` is yt-dlp's field; the "title line" figure is the one Facebook prints at the start of the page title, about 2× higher. Both are given as returned.
- **Labels:** "(reading)" marks interpretation, as opposed to what is measured or quoted.

## Metadata, all 15

| # | Share URL | Video ID | Page | Upload date | Duration (s) | view_count | Title-line views · reactions | Comments |
|---|---|---|---|---|---|---|---|---|
| 1 | https://www.facebook.com/share/r/1M5aty5ZFw/ | 1382518750622132 | FAILED | | | | | |
| 2 | https://www.facebook.com/share/v/1DQyqmaRUQ/ | 1845911869739973 | Minho Makeup & Beauty | 2026-10-31 | 139.3 | 32955 | 61K views · 292 reactions | not found |
| 3 | https://www.facebook.com/share/v/19uYSpQDLB/ | 1409132951246633 | Minho Makeup & Beauty | 2026-10-30 | 146.7 | 33317 | 61K views · 289 reactions | not found |
| 4 | https://www.facebook.com/share/v/1EJtNPoaKR/ | 28198446163154521 | Minho Makeup & Beauty | 2026-09-08 | 147.9 | 21791 | 42K views · 224 reactions | not found |
| 5 | https://www.facebook.com/share/v/1JTghxd7ii/ | 807894659075122 | Minho Makeup & Beauty | 2026-09-02 | 148.8 | 30810 | 62K views · 432 reactions | not found |
| 6 | https://www.facebook.com/share/v/1B8kDn1stW/ | 898472679696406 | Minho Makeup & Beauty | 2026-08-30 | 139.7 | 32422 | 60K views · 367 reactions | not found |
| 7 | https://www.facebook.com/share/v/1DfiwTsQnp/ | 1084335064173234 | Minho Makeup & Beauty | 2026-08-26 | 139.7 | 40391 | 70K views · 479 reactions | not found |
| 8 | https://www.facebook.com/share/v/19t4sHPWsn/ | 1774209123716254 | Minho Makeup & Beauty | 2026-08-23 | 146.1 | 94109 | 149K views · 488 reactions | not found |
| 9 | https://www.facebook.com/share/v/1AcZwn4zG7/ | 2586437711783517 | Jiho Beauty | 2026-10-23 | 120.7 | 86728 | 181K views · 3.2K reactions | not found |
| 10 | https://www.facebook.com/share/v/1PseTywRdi/ | 1818694942613295 | Jiho Beauty | 2026-10-22 | 128.8 | 72893 | 148K views · 821 reactions | not found |
| 11 | https://www.facebook.com/share/v/19LvPLPe16/ | 1906443924098073 | Jiho Beauty | 2026-10-21 | 128.8 | 61754 | 124K views · 1.3K reactions | not found |
| 12 | https://www.facebook.com/share/v/1FDQFvHFWD/ | 1400995212201059 | Jiho Beauty | 2026-10-12 | 108.5 | 45530 | 89K views · 1.2K reactions | not found |
| 13 | https://www.facebook.com/share/v/1DwtLuy5BL/ | 1104086958770697 | Jiho Beauty | 2026-10-11 | 108.5 | 111727 | 203K views · 3.5K reactions | not found |
| 14 | https://www.facebook.com/share/v/1Kc2NwWeat/ | 1725073855253851 | Jiho Beauty | 2026-10-11 | 108.5 | 102119 | 191K views · 3K reactions | not found |
| 15 | https://www.facebook.com/share/v/1Bi7GsR1MQ/ | 2071496550177997 | Jiho Beauty | 2026-10-07 | 108.5 | 650286 | 1.1M views · 18K reactions | not found |


# Part 1: Facebook videos (numbered as in your list)

## Video 1 — FAILED TO DOWNLOAD
**Link:** https://www.facebook.com/share/r/1M5aty5ZFw/ (a Facebook *reel* share link; it resolves to video ID 1382518750622132)
**Error (yt-dlp 2026.10.26):** `ERROR: [facebook] 1382518750622132: Cannot parse data; please report this issue on https://github.com/yt-dlp/yt-dlp/issues?q= ...`
**Tried:** the share link, `facebook.com/reel/1382518750622132`, `facebook.com/watch/?v=1382518750622132` and `m.facebook.com/watch/?v=...`, all with the same error. The other 14 links downloaded without a login. My reading: this reel is restricted (login, age or region) or uses a page layout yt-dlp can't read. Running yt-dlp with `--cookies-from-browser chrome` on a computer logged into Facebook would be the next step. This cloud machine has no logged-in browser, so per the instructions I did not try anything else.
No breakdown is possible without the video.

---

## Video 2 — Minho Makeup & Beauty — "Get rid of that matte lipstick" (5-step mature routine, foundation saved for last)
**Link:** https://www.facebook.com/share/v/1DQyqmaRUQ/ (video ID 1845911869739973) · **Page:** Minho Makeup & Beauty · **Uploaded:** 2026-10-31 (info.json timestamp 1793464932 = 16:42 UTC) · **Duration:** 2:19 (139.3 s) · **Views:** view_count 32,955 (page title line says "61K views") · **Reactions:** 292 (from title line "61K views · 292 reactions") · **Comments:** not found (comment_count = None in metadata)
*(All metadata from videos/2.info.json, yt-dlp pull 2026-11-07.)*

**Caption (verbatim):** "adl Comment "GLOW" for complete and I will send you the full list of these products and more. With exactly how to use them. ❤️🚨🤯 #maturemakeuproutine #makeupartist #makeupforolderwomen #wrinkles #makeup #maturemakeup #womenover60 #womenover50 #womenover40 #matureskinmakeup"

Note (measured): the caption's comment word is "GLOW"; the spoken and on-screen comment word is "natural" (2:13–2:16). The caption starts with "adl" (meaning not clear; see Compliance).

### HOOK (0:00–0:05)
- Spoken: 0:00–0:04.9 "If you look decades older, completely drained, and like your makeup is working against you," → 0:04.9–0:10.2 "and your goal is to look youthful, confident, and beautiful even at 50, 60, or 70," → 0:10.2–0:11.4 "get rid of that matte lipstick."
- On-screen text (burned-in captions, white, lower-middle, no separate headline): 0:00–0:01 "if you look decades older"; 0:02 "completely drained and like"; 0:03–0:04 "your makeup is working against you"; 0:05 "and your goal is to look youthful"; 0:07 "confident and beautiful even at 50"; 0:09 "60 or 70". No headline/title card at any point.
- Visual: two-shot, vertical, ring light directly behind. 0:00–0:04 = "before" woman: grey curly bob, very heavy black smoky eye, strong pink blush, deep wrinkles, unsmiling, in a black tee; a young platinum-blond man in wire aviator glasses and black tee leans in at right, hand holding her chin (0:00–0:01), then pointing at camera (0:02–0:03). Hard cut at 0:05 to a different-looking "after" woman (straight dark-brown shoulder-length hair, soft natural makeup, eyes closed at 0:05), man again cupping her chin. Reading: the cut functions as an instant before/after; the two women look like different people / heavily altered versions. 0:11 he holds up a matte red-brown lipstick (silver bullet, brand not visible).

### FORMAT
"Stop using X / do this instead" mature-makeup routine, with the sold product held back as the "missing step" at the end.
Opens by banning three products (matte lipstick, heavy mascara, primer), teases "the last one" under a covered basket, walks four real-brand products (Clinique, NARS, Makeup by Mario, Too Faced, plus an e.l.f. gloss), then reveals Luxe foundation as the step "most women miss".

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:10–0:19 | Ban list: "get rid of that matte lipstick." / "Throw away the heavy mascara and stop using primer altogether," / "because these products were made for 20-year-olds, not for your mature skin." | 0:11 man holds matte lipstick (silver bullet, no visible brand), caption "get rid of that matte lipstick"; 0:13–0:19 he holds a black-capped clear-blue gel tube (primer, no legible brand), captions "and stop using primer all together", "because these products were made for 20 year olds", "not for your mature skin". Mascara not shown in sampled frames. |
| 0:19–0:24 | Tease: "The last one may be the one thing standing between you and looking 20 years younger." | 0:21–0:23 woman holds a wicker basket covered with gold satin cloth; man points at it. Captions "the last one may be the one thing standing between you", "and looking 20 years younger". |
| 0:24–0:34 | 1. Eye cream: "First, under eye cream with a concealer, I use Clinique All About Eyes." "Just a small amount pressed gently under the eye." "Let it absorb for a moment before anything goes on top." | Woman holds pink Clinique jar with silver lid (label "CLINIQUE", sub-line not legible) in right hand and a NARS concealer wand in left; man points under her eye. Captions "first under eye cream with a concealer", "I use Clinique all about eyes", "just a small amount press gently under the eye", "let it absorb for a moment before anything goes on top". No application shown. |
| 0:34–0:49 | 2. Concealer: "Then NARS concealer under the eye." "Most concealers on mature skin compress into every crease and sink into the corner of the eye." "This one doesn't." "It diffuses light instead of sitting in the crease, so the eye looks lifted and rested instead of tired and heavy." | Same two products held; captions "then NARS concealer under the eye", "most concealers on mature skin", "compress into every crease", "and sink into the corner of the eye", "it diffuses light instead of sitting in the crease", "so the eye looks lifted and rested". |
| 0:49–1:08 | 3. Bronzer: "Next, by Mario Cream Bronzer." "The older you get, the more your face loses warmth and dimension." "A face without bronzer after 50 reads as flat and tired no matter how good the rest of your makeup is." "Take a brush, blend it out, and do not use a sponge, always a brush on mature skin, and suddenly there is life back in the face." | 0:49 white round compact, open, brown cream bronzer (lid text appears mirrored, "MARIO" readable backwards). Caption reads "next by Mario Cream Bronzer" (brand = Makeup by Mario; caption/transcript drop "Makeup"). Captions "the older you get", "the more your face loses warmth and dimension", "a face without bronzer after 50 reads as flat and tired", "take a brush blend it out and do not use a sponge", "always a brush on mature skin", "and suddenly there is life back in the face". No brush or blending shown. |
| 1:08–1:19 | 4. Blush: "Then Too Faced blush." "Press it into the cheek and pull it all the way toward the nose." "Chef's kiss." "That is the difference between color that sits on the face and color that looks like it belongs there." | 1:09 gold heart-clasp compact, coral blush embossed "Too Faced" (caption misspells it "then two faced blush"). Man kisses fingertips ~1:11. Captions "and pull it all the way toward the nose", "that is the difference between color", "and color that looks like it belongs there". |
| 1:19–1:29 | 5. Lip gloss: "Now finish the lips." "A lip gloss on top reflects off the shine and makes the lips appear fuller." "On mature skin, the lips lose volume." "This is the easiest fix most women never think of." | 1:21–1:29 woman holds square-bottle rose/mauve shimmer gloss labelled "e.l.f." (brand shown, not said). Captions "a lip gloss on top reflects off the shine", "and makes the lips appear fuller", "on mature skin the lips lose volume", "this is the easiest fix most women never think of". |
| 1:29–1:55 | 6. REVEAL, Luxe foundation: "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." "foundation." "Most foundations on mature skin look like makeup." "Luxe foundation is specifically developed for mature skin." "It helps blur fine lines, smooth texture, and look natural, not heavy." "And it almost never settles into wrinkles." "It is the number one best-selling foundation on Amazon right now." | From 1:31 woman holds a beige squeeze tube with vertical black "Luxe" wordmark (small print above/below not legible/garbled). Captions "and this is the step that makes you look less tired", "and yet most women miss it completely", "foundation" (1:37), "most foundations on mature skin look like makeup", "Lux Foundation" (1:41 — caption misspells; tube reads "Luxe"), "is specifically developed for mature skin", "it helps blur fine lines", "smooth texture and look natural", "and it almost never settles into wrinkles", "it is the No. 1 best selling foundation on Amazon" (1:51–1:53), "right now" (1:55). No application, no swatch, no before/after on the foundation. The covered basket is never opened on camera. |
| 1:55–2:19 | CTA block (see CTA). | Tube held to 2:01; 2:03 onward no product, man cupping chin / gesturing; 2:15 a larger quoted word ""natural"" appears above the caption. |

**Rehooks / open loops**
- 0:19–0:24 "The last one may be the one thing standing between you and looking 20 years younger." (with covered basket prop 0:21–0:23)
- 0:41–0:42 "This one doesn't." (mini-reversal inside concealer beat)
- 1:26–1:29 "This is the easiest fix most women never think of."
- 1:29–1:37 "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." → "foundation."
- 2:00–2:03 "Sometimes there's a coupon available, so hurry up."

### PRODUCT
- Product sold: foundation — brand "Luxe" (spoken "Luxe foundation"; tube wordmark "Luxe"; burned-in caption spells it "Lux Foundation" at 1:41). Exact product name beyond "Luxe foundation": not said; tube small print not legible.
- First appears: 1:40.4 spoken ("Luxe foundation is specifically developed for mature skin"; the category "foundation." is spoken at 1:36.8); 1:31 on screen (first sampled frame with it: woman holds the beige "Luxe" tube upright beside her face, left of frame; not in the 1:29 frame, where she holds the e.l.f. gloss).
- Bridge line (verbatim): 1:29.2–1:36.8 "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." 1:36.8 "foundation." 1:37.5 "Most foundations on mature skin look like makeup."
- Saved for last? Yes — step 6 of 6 (after eye cream, concealer, bronzer, blush, gloss); pitch starts 1:29 of 2:19 (reveal word 1:37), and was teased at 0:19 as "the last one".
- Product shots: single static hold of a matte beige soft tube (cap down), vertical black "Luxe" logotype, two lines of tiny unreadable print above the logo and two below; held by the woman 1:31–2:01 while the man points at her cheek. No texture shot, no application, no before/after tied to the product. (The only before/after in the video is the 0:00–0:04 vs 0:05 face cut, which is not attributed to any one product.)

### CTA
- Spoken (verbatim): 1:55.3–2:00.0 "Link is on my profile, and I also added the link in the comments for anyone who could not find it." 2:00.0–2:02.7 "Sometimes there's a coupon available, so hurry up." 2:02.7–2:09.3 "If you are over 60 and give this routine a chance, I think you will never want to use anything else again." 2:09.3–2:16.2 "And if you would like the list of these products and a quick explanation of what each one does, just comment natural and I will send it to you." 2:16.2–2:19.2 "But you have to follow me first so I can message you."
- On-screen text (verbatim): 1:57 "and I also added the link in the comments"; 1:59 "for anyone who could not find it"; 2:01 "sometimes there's a coupon available"; 2:03 "so hurry up if you are over 60"; 2:05 "and give this routine a chance"; 2:07–2:09 "I think you will never want to use anything else again"; 2:11 "and if you would like the list of these products"; 2:13 "and a quick explanation of what each one does"; 2:15 ""natural"" (large, in quotes) + "just comment natural and I will send it to you"; 2:17–2:19 "but you have to follow me first so I can message you". (Caption: "Comment "GLOW" ... I will send you the full list of these products".)
- Where it points: (1) link on the page's profile ("link is on my profile"); (2) link in the comments; (3) "comment natural" DM automation (caption says "GLOW") with a follow-first gate ("you have to follow me first so I can message you"). Amazon named as the store in the claim ("best-selling foundation on Amazon") but no Amazon search term given.

### AVATAR
- Who: expert framing — a male makeup artist doing a client's routine. Credentials implied, not stated: first person "I use Clinique All About Eyes" (0:28), hands-on posture with the model, page name "Minho Makeup & Beauty", caption hashtag "#makeupartist". No title or years claimed. Approx age: 20s (reading). Apparent ethnicity: white (reading). Gender: male. Clothing: black crew tee, silver wire aviator glasses, short curly platinum-blond hair, visible foundation/lip colour on his own face. Model: woman, apparent 55–65 (reading), white, black tee, small gold hoop earrings, ring on right hand.
- Setting & lighting: studio/salon — large ring light directly behind the pair, dark green wall, black salon chair. Fixed/near-fixed frame, selfie-style two-shot at face height (could be phone on tripod; no visible handheld shake in stills). Even, bright frontal light.
- Real or AI-looking (reading, not proven): several AI/edit tells — (a) mirrored text on the NARS concealer label (0:25 onward) and on the bronzer lid ("MARIO" reads backwards, 0:49); (b) small print on the Luxe tube and the Clinique jar sub-line is garbled/unreadable; (c) the "before" woman (0:00–0:04: grey curly bob, extreme smoky eye, deep wrinkles) and "after" woman (0:05+: straight dark hair) look like different people, with an instant hard cut; (d) the face never changes during the "routine" — no product is ever applied on camera; the after-face is finished from 0:05. No "syntheticmedia" or other AI watermark seen in any frame. Lip-sync can't be judged from stills. Mirroring alone could also come from a flipped selfie camera; the garbled print is the stronger AI signal.
- Delivery: fast, punchy, didactic; short imperative lines ("get rid of", "Throw away", "do not use a sponge"). Slang: "Chef's kiss." (1:13). No swearing. Very expressive face/hand acting from the man (open-mouth surprise, finger kiss, thumbs-up). Casual-authoritative.
- Who else appears: only the one woman (model, two versions before/after) and the man's hands. No other people.

### CLAIMS & COMPLIANCE
- 0:00–0:10 "If you look decades older ... and your goal is to look youthful, confident, and beautiful even at 50, 60, or 70"
- 0:15–0:19 "these products were made for 20-year-olds, not for your mature skin." (matte lipstick, heavy mascara, primer)
- 0:19–0:24 "The last one may be the one thing standing between you and looking 20 years younger." (result promise, hedged "may")
- 0:41–0:48 NARS concealer: "This one doesn't." "It diffuses light instead of sitting in the crease, so the eye looks lifted and rested"
- 0:54–1:00 "A face without bronzer after 50 reads as flat and tired no matter how good the rest of your makeup is."
- 1:20–1:24 lip gloss "makes the lips appear fuller."
- 1:29–1:36 foundation step "makes you look less tired, brings your face to life, and yet most women miss it completely."
- 1:37–1:40 comparative: "Most foundations on mature skin look like makeup."
- 1:40–1:43 "Luxe foundation is specifically developed for mature skin."
- 1:43–1:48 "It helps blur fine lines, smooth texture, and look natural, not heavy."
- 1:48–1:51 "And it almost never settles into wrinkles."
- 1:51–1:55 bestseller: "It is the number one best-selling foundation on Amazon right now." (on-screen "it is the No. 1 best selling foundation on Amazon")
- 2:00–2:02 scarcity/urgency: "Sometimes there's a coupon available, so hurry up."
- 2:02–2:09 "If you are over 60 and give this routine a chance, I think you will never want to use anything else again."
- Prices: none said or shown. Ingredient/stat claims: none. "Same company owns": none. Client story: none spoken (implied by the artist-and-model set-up).
- "Ad"/"#ad"/"Sponsored"/"paid partnership": none on screen, none spoken, no "AD |" prefix on the page title line. The caption begins "adl" — unclear whether this is a garbled "ad" disclosure, a typo or a code (my reading; not a clear disclosure either way).
- AI disclosure: none seen (no "syntheticmedia" or similar watermark in any frame; no AI label in caption).
- Risk notes (my reading): "number one best-selling foundation on Amazon right now" needs substantiation (category, date) and is the riskiest claim; "specifically developed for mature skin" and "almost never settles into wrinkles" are performance claims needing support; the before/after cut (0:00→0:05) implies a transformation not shown to come from these products — misleading-impression risk, especially if the faces are AI; no material-connection disclosure while selling one brand alongside named third-party brands (Clinique, NARS, Makeup by Mario, Too Faced, e.l.f.); "coupon ... hurry up" is soft urgency; comment word mismatch ("GLOW" in caption vs "natural" spoken) may break the DM automation for one of the two. No profanity.

### WHY IT WORKS
Fear-of-looking-old opener plus an instant before/after cut, then a "throw away" list and a covered basket, gives a strong reason to stay until "the last one".
Four trusted prestige brands earn credibility before the unknown brand arrives as the "missing step" with a #1-on-Amazon claim and a two-way CTA (profile link + comment-for-list DM with follow gate).

### OBSERVER NOTES (optional)
- Measured: views differ by source — view_count 32,955 vs title line "61K views" (~1.85x).
- Measured: brand spellings — transcript "by Mario Cream Bronzer" (on-screen same; real brand Makeup by Mario), on-screen "two faced blush" vs packaging "Too Faced", on-screen "Lux Foundation" (1:41) vs tube "Luxe". The e.l.f. gloss is shown but never named.
- Measured: the three "banned" products in the hook (matte lipstick, heavy mascara, primer) are never mentioned again; the routine itself has no on-camera application at all — every beat is "hold product + point at face".
- Reading: the covered basket (0:21–0:23) is the visual open loop for the saved-for-last product but is never opened; the Luxe tube just appears in hand at 1:31.
- Reading: "If you are over 60" at 2:03 narrows the audience late, while the hook says "50, 60, or 70".
- Per the task note, this page posts several near-identical videos (3–8 are from the same page); only video 2 was analysed here.

---

## Video 3 — Minho Makeup & Beauty — "If you look decades older… stop using primer"
**Link:** https://www.facebook.com/share/v/19uYSpQDLB/ · **Page:** Minho Makeup & Beauty · **Uploaded:** 2026-10-30 (info.json timestamp 1793403922 = 23:45 UTC) · **Duration:** 2:27 (146.7 s) · **Views:** view_count 33,317 (page title line says "61K views") · **Reactions:** 289 (from title line "61K views · 289 reactions") · **Comments:** not found (comment_count null in metadata). All figures from yt-dlp info.json, pulled 2026-11-07.
**Caption (verbatim):** "adl Comment "GLOW" for complete and I will send you the full list of these products and more. With exactly how to use them. ❤️🚨🤯
These cheap Target finds beat luxury all the time...☺️
#maturemakeuproutine #makeupartist #makeupforolderwomen #wrinkles   #makeup #maturemakeup #womenover60 #womenover50 #womenover40 #matureskinmakeup"

(Note, measured: the caption says comment "GLOW" and "cheap Target finds"; the video says comment "natural" and the products shown are Clinique, NARS, Makeup by Mario, Too Faced, e.l.f. and Luxe — not presented as Target finds. The caption appears to be reused from another post; my reading.)

### HOOK (0:00–0:05)
- Spoken: 0:00–0:04.9 "If you look decades older, completely drained, and like your makeup is working against you," → 0:04.9 "and your goal is to look youthful, confident, and beautiful even at 50, 60, or 70,"
- On-screen text (burned-in captions, white lower-third, no separate headline): 0:00–0:01 "if you look decades older"; 0:02 "completely drained and like"; 0:03–0:04 "your makeup is working against you"; 0:05 "and your goal is to look youthful"
- Visual: Two-shot, tripod/fixed camera, ring light directly behind the pair. Seated older woman (short curly grey-brown hair, heavy smoky black eye makeup, strong pink blush, deep wrinkles — a deliberately "aged-looking" made-up face) faces camera; blond male makeup artist in wire glasses leans in from right, holding her chin (0:00–0:01) then pointing at her (0:02–0:04). Hard cut at 0:05 to the "after" woman: long straight dark hair, soft natural makeup, eyes closed then open — same framing, artist still holding her chin. The before→after swap lands exactly on "your goal is to look youthful".

### FORMAT
"Stop using X / here's the mature-skin routine, missing step saved for last." A makeup-artist-and-client routine: open with what to throw away (matte lipstick, heavy mascara, primer), promise "the exact products used on every client", walk through 5 named-brand steps, then announce "one step is missing" and reveal the sponsored foundation (Luxe) as the final step, followed by a link + comment-for-list CTA.

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:10–0:15 | "get rid of that matte lipstick, throw away the heavy mascara, and stop using primer altogether." | 0:11 artist holds up a matte red-brown lipstick (silver bullet tube, brand not legible); 0:13–0:19 a clear-blue gel tube with black cap (brand not visible) held up as the "primer". Text: "get rid of that matte lipstick", "and stop using primer all together" |
| 0:15–0:19 | "Because these products were made for 20-year-olds, not for your mature skin." | Text: "because these products were made for 20 year olds" (0:17), "not for your mature skin" (0:19); blue tube still in hand |
| 0:19–0:31 | "These are the exact products used on every client who walks in looking decades older, and leaves feeling confident and complete again. The last one may be the one thing standing between you and looking 20 years younger." | 0:21–0:31 woman holds a wicker basket covered with a gold satin cloth (products hidden); artist points at it. Text: "these are the exact products used on every client", "who walks in looking decades older", "and leaves feeling confident and complete again", "the last one may be the one thing standing between you", "and looking 20 years younger" |
| 0:31–0:56 | Step 1 "First, under eye cream with a concealer, I use Clinique All About Eyes. Just a small amount pressed gently under the eye. Let it absorb for a moment before anything goes on top. Then NARS concealer under the eye. Most concealers on mature skin compress into every crease and sink into the corner of the eye. This one doesn't. It diffuses light instead of sitting in the crease, so the eye looks lifted and rested instead of tired and heavy." | 0:33 woman holds NARS concealer wand (left hand) + Clinique "all about eyes" pink jar (right hand) up to camera; artist points under her eye. Text: "first under eye cream with a concealer", "I use Clinique all about eyes", "then NARS concealer under the eye", "this one doesn't", "it diffuses light instead of sitting in the crease". No application shown on camera |
| 0:56–1:15 | Step 2 "Next, by Mario Cream Bronzer. The older you get, the more your face loses warmth and dimension. A face without bronzer after 50 reads as flat and tired… Take a brush, blend it out, and do not use a sponge, always a brush on mature skin, and suddenly there is life back in the face." | 0:57–1:13 white round open compact with brown cream bronzer held up; lid logo not legible at frame resolution. Text: "next by Mario Cream Bronzer" (spoken/on-screen both read "by Mario" — brand appears to be Makeup by Mario, my reading), "a face without bronzer after 50 reads as flat and tired", "take a brush blend it out and do not use a sponge". No brush or application shown |
| 1:15–1:26 | Step 3 "Then Too Faced blush. Press it into the cheek and pull it all the way toward the nose. Chef's kiss. That is the difference between color that sits on the face and color that looks like it belongs there." | 1:17–1:25 gold compact, coral-orange blush embossed "Too Faced" (legible in zoom of 1:21 frame). Text: "press it into the cheek", "and pull it all the way toward the nose", "chef's kiss" |
| 1:26–1:36 | Step 4 "Now finish the lips. A lip gloss on top reflects off the shine and makes the lips appear fuller. On mature skin, the lips lose volume. This is the easiest fix most women never think of." | 1:27–1:35 pink-shimmer lip gloss, square bottle, black cap, "e.l.f." printed on bottle (brand shown on screen only, not said). Text: "now finish the lips", "a lip gloss on top reflects off the shine", "this is the easiest fix most women never think of" |
| 1:36–1:44 | Reveal setup: "But one step is missing. And this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." | 1:37 cut to Luxe tube in woman's hand. Text: "but one step is missing", "and this is the step that makes you look less tired", "brings your face to life", "and yet most women miss it completely" |
| 1:44–2:02 | Step 5 / product: "foundation. Most foundations on mature skin look like makeup. Luxe foundation is specifically developed for mature skin. It helps blur fine lines, smooth texture, and look natural, not heavy. And it almost never settles into wrinkles. It is the number one best-selling foundation on Amazon right now." | 1:37–2:09 beige squeeze tube, vertical "Luxe" wordmark, small print above/below not legible. Text: "most foundations on mature skin look like makeup", "is specifically developed for mature skin", "smooth texture and look natural", "and it almost never settles into wrinkles", "it is the No. 1 best selling foundation on Amazon" (1:59–2:01). No application or before/after on this step |
| 2:02–2:26 | CTA (see below) | Text: "link is on my profile", "and I also added the link in the comments", "for anyone who could not find it", "so hurry up if you are over 60", "and give this routine a chance", "I think you will never want to use anything else again", "and if you would like the list of these products", "and a quick explanation of what each one does", larger "\"natural\"" above "just comment natural and I will send it to you" (2:23), "but you have to follow me first so I can message you" (2:25) |

**Rehooks / open loops**
- 0:19–0:26 "These are the exact products used on every client who walks in looking decades older, and leaves feeling confident and complete again." (covered basket = visual open loop, 0:21–0:31)
- 0:26–0:31 "The last one may be the one thing standing between you and looking 20 years younger."
- 0:43–0:49 "Most concealers on mature skin compress into every crease… This one doesn't."
- 1:33–1:36 "This is the easiest fix most women never think of."
- 1:36–1:44 "But one step is missing. And this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely."
- 2:07–2:10 "Sometimes there's a coupon available, so hurry up."

### PRODUCT
- Product sold: foundation — Luxe — "Luxe foundation" (spoken 1:47.8); tube shows "Luxe" wordmark (spelled "Luxe" on screen; the transcript also has "Luxe"). Full product name beyond "Luxe foundation" not said; tube small print not legible.
- First appears: 1:47.8 spoken ("Luxe foundation is specifically developed for mature skin"; the category word "foundation." comes at 1:44.2); 1:37 on screen (woman holds the beige Luxe tube up beside her face at "but one step is missing").
- Bridge line (verbatim): 1:36.6–1:44.8 "But one step is missing. And this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely. foundation." Set up at 0:26.8 "The last one may be the one thing standing between you and looking 20 years younger."
- Saved for last? Yes — step 5 of 5 (the "missing step"; 6 products in all, because step 1 pairs Clinique All About Eyes with NARS concealer), reveal starts 1:36 of 2:27; product pitch runs 1:44–2:02, CTA to 2:26.
- Product shots: held-up tube only (woman holds it at cheek height, artist points at her cheek/jaw). No swatch, no application, no texture shot, no dedicated before/after for the foundation. The only before/after in the video is the 0:00–0:04 "before" face vs the 0:05 onward "after" face.

### CTA
- Spoken: 2:02.7–2:07.4 "Link is on my profile and I also added the link in the comments for anyone who could not find it." 2:07.4–2:10.1 "Sometimes there's a coupon available, so hurry up." 2:10.1–2:16.7 "If you are over 60 and give this routine a chance, I think you will never want to use anything else again." 2:16.7–2:26.6 "And if you would like the list of these products and a quick explanation of what each one does, just comment natural and I will send it to you. But you have to follow me first so I can message you."
- On-screen text: 2:03 "link is on my profile"; 2:05 "and I also added the link in the comments"; 2:07 "for anyone who could not find it"; 2:09–2:11 "so hurry up if you are over 60" (on-screen merges the two spoken sentences); 2:13 "and give this routine a chance"; 2:15 "I think you will never want to use anything else again"; 2:17 "and if you would like the list of these products"; 2:19–2:21 "and a quick explanation of what each one does"; 2:23 "\"natural\"" (larger, in quotes) + "just comment natural and I will send it to you"; 2:25 "but you have to follow me first so I can message you".
- Where it points: (1) link in profile; (2) link in comments; (3) "comment natural" DM automation with follow-first gate. The pitch names Amazon ("number one best-selling foundation on Amazon") so the link presumably goes to Amazon — not confirmed (link not visible). Caption instead says comment "GLOW" (mismatch).

### AVATAR
- Who: "expert" — male makeup artist; implied credentials via "every client who walks in" (0:19), "I use Clinique All About Eyes" (0:31), and hashtag "#makeupartist" in caption. No explicit title/years claimed. Approx age: 20s (my reading). Apparent ethnicity: white. Gender: male. Clothing: black crew-neck T-shirt, thin silver/wire aviator-style glasses, bleached-platinum curly crop, small hoop earring, visible base makeup. Client/model: woman, approx 55–65 (my reading), white, black T-shirt, small hoop earrings, wedding-type ring on left hand; she holds every product.
- Setting & lighting: makeup studio look — dark green wall with tan/beige graphic shapes, large ring light visible directly behind them (in frame the whole video). Fixed/tripod-style front camera (not handheld), front ring-light lighting, eye-level. One continuous set; jump cuts between lines.
- Real or AI-looking (my reading): no "syntheticmedia" or other AI watermark seen on any frame. Faces, hands and product handling look like real video; artist's mouth movements look consistent with speech. Notable: the "before" woman (0:00–0:04: short curly grey hair, heavy smoky eyes, deep wrinkles) and the "after" woman (0:05 on: long straight dark hair, smoother skin) differ strongly in hair and skin — could be heavy aging makeup/wig on the same person, or a different person/edited image; cannot confirm from frames. Voice/lip-sync not verifiable from stills.
- Delivery: fast, punchy, exaggerated facial expressions (wide mouth, eyebrow raises, mock-grimaces at 1:01, 1:03, 2:13); short declarative lines; casual with one slang line "Chef's kiss." (1:20.4). No swearing.
- Who else appears: the client/model (both "before" and "after" look); her hands hold all products; artist's hands point/hold her chin. No other people.

### CLAIMS & COMPLIANCE
- 0:00–0:10 "If you look decades older… and your goal is to look youthful, confident, and beautiful even at 50, 60, or 70"
- 0:10–0:19 "get rid of that matte lipstick, throw away the heavy mascara, and stop using primer altogether. Because these products were made for 20-year-olds, not for your mature skin."
- 0:19–0:26 "These are the exact products used on every client who walks in looking decades older, and leaves feeling confident and complete again." (implied professional/client testimonial)
- 0:26–0:31 "The last one may be the one thing standing between you and looking 20 years younger." (result promise, applies to Luxe foundation)
- 0:43–0:56 NARS concealer: "Most concealers on mature skin compress into every crease… This one doesn't. It diffuses light… so the eye looks lifted and rested"
- 1:01–1:08 "A face without bronzer after 50 reads as flat and tired no matter how good the rest of your makeup is."
- 1:27–1:31 lip gloss "makes the lips appear fuller"
- 1:44–1:47 "Most foundations on mature skin look like makeup." (comparative vs category)
- 1:47.8–1:51 "Luxe foundation is specifically developed for mature skin."
- 1:51–1:56 "It helps blur fine lines, smooth texture, and look natural, not heavy."
- 1:56–1:58 "And it almost never settles into wrinkles."
- 1:58–2:02 "It is the number one best-selling foundation on Amazon right now." (on-screen "it is the No. 1 best selling foundation on Amazon")
- 2:07–2:10 "Sometimes there's a coupon available, so hurry up." (urgency/scarcity)
- 2:10–2:16 "If you are over 60 and give this routine a chance, I think you will never want to use anything else again."
- Prices: none said or shown. Ingredient/percentage stats: none.
- "Ad"/"#ad"/"Sponsored"/"paid partnership" shown? Not found — no on-screen disclosure, none in caption, page title line has no "AD |" prefix. The caption begins "adl" — this is not a recognisable ad disclosure (reads as a typo/fragment; my reading).
- AI disclosure shown? None seen (no "syntheticmedia" or similar watermark on any frame).
- Risk notes (my reading): (a) "number one best-selling foundation on Amazon right now" needs substantiation and is time-bound; (b) "looking 20 years younger" is a result promise; (c) the Luxe pitch sits in a routine of genuine named brands (Clinique, NARS, Makeup by Mario, Too Faced, e.l.f.) — borrowed credibility, and a paid placement without disclosure would be an FTC problem; (d) "every client" implies professional endorsement/testimonial; (e) caption mismatch ("GLOW", "cheap Target finds") vs video ("natural", premium brands) could be seen as misleading; (f) "coupon… hurry up" is unverified urgency. No profanity.

### WHY IT WORKS
A dramatic before→after face swap at 0:05, paired with "throw away" commands and a covered basket, makes the viewer wait for "the last one".
Four trusted name brands earn credibility before the sponsored foundation arrives as the "one step… most women miss", with three CTA routes (profile, comments, comment-for-DM).

### OBSERVER NOTES (optional)
- Measured: view_count (33,317) is about half the title-line "61K views", consistent with the METADATA.md note.
- Measured: the lip gloss is shown as e.l.f. on screen but its brand is never said; it is the only product not named aloud.
- Measured: no product is applied on camera; the "after" face is already finished from 0:05 — the routine is told, not demonstrated.
- Reading: the Luxe tube is styled to match the beige/neutral premium look of the other products; it is held the same way as the real brands, so it reads as "one of the kit".
- Reading: the opening "stop using primer" holds up a generic-looking blue gel tube with no visible brand, avoiding knocking a named brand.

---

## Video 4 — Minho Makeup & Beauty — "The reason you look twice your age"
**Link:** https://www.facebook.com/share/v/1EJtNPoaKR/ · **Page:** Minho Makeup & Beauty · **Uploaded:** 2026-09-08 (timestamp 1788860092 = 09:34:52 UTC) · **Duration:** 2:28 (147.864 s) · **Views:** view_count 21791 (page title line says "42K views") · **Reactions:** 224 (title line "224 reactions") · **Comments:** not found (comment_count null in metadata)
Source: videos/4.info.json (yt-dlp, pulled 2026-11-07); transcript transcripts/4.txt (faster-whisper medium.en); frames/4/.

**Caption (verbatim):** "adl COMMENT "natural" and I will send you the exact ROUTINE EXPLAINED with a LIST of the PRODUCTS PLUS all the proven MAKEUP TIPS for MATURE women.🤯🥰❤️ But you have to follow me first so i can message you. ☺️🤍 Link for the foundation is on my profile (bio) and in the comments. #maturemakeuproutine #makeupartist #makeupforolderwomen #wrinkleshack #makeup #maturemakeup #womenover60 #womenover50 #womenover40makeup"

### HOOK (0:00–0:05)
- Spoken: "The reason you look twice your age is not because you are old, tired, or past your prime," (0:00–0:04) → "but because your outdated makeup techniques and products are quietly and brutally working against you." (0:04–0:11)
- On-screen text (burned-in captions only, white lower-third, no headline/sub-headline): "the reason you look twice your age" (0:00–0:01), "is not because you are old" (0:02–0:03), "tired or past your prime" (0:04), "but because your outdated makeup techniques" (0:05–0:07), "and products are quietly" (0:09), "and brutally working against you" (0:11). (Caption reads "tired or past" where audio is "tired, or past".)
- Visual: "BEFORE" woman — older woman (reading: 65–75), short grey-brown curly hair, heavy black smoky eye, very dark drawn brows, strong pink blush, black top, deadpan expression. A young man with platinum-blond curly hair, wire aviator glasses and a black T-shirt leans in behind her shoulder, holding her chin with his hand (0:00–0:01, 0:05), then gesturing/grimacing at the camera (0:02–0:11, exaggerated pulled faces at 0:07–0:11). Large ring light directly behind, dark green wall. Static tight vertical two-shot. Hard cut at ~0:12–0:13 to the "AFTER" look.

### FORMAT
"Makeup-artist before/after + 'throw these out' + client routine, house product saved for last."
Opens on an over-done "aged" makeup look, cuts to a polished "after", tells viewers to bin three product types, then walks through a 6-step routine of real-brand products held up one by one, with the sold product (Luxe foundation) framed as the "missing step" at the end, then a link + comment-for-DM CTA.

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:11–0:16 | "The goal is simple, youthful, confident, and beautiful, even at 50, 60, or 70." | Cut (~0:12–0:13) to AFTER: woman with long layered brown/honey-highlight blowout, soft natural makeup, cream satin robe, small hoop earrings, smiling; same man leaning in. Wider studio (green panels, ceiling downlights, ring light at right edge). Captions "the goal is simple youthful" (0:13), "confident and beautiful even at 50" (0:15). |
| 0:16–0:24 | "Get rid of that matte lipstick, throw away the heavy mascara, and stop using primer altogether, because these products were made for 20-year-olds, not for your mature skin." | Man holds up a black bullet lipstick (0:17), a black mascara with green-ish logo (0:19), a clear tube of blue primer gel (0:21–0:23). Brands not legible. Captions "60 or 70 get rid of that matte lipstick", "throw away the heavy mascara", "and stop using primer altogether", "because these products were made for 20 year olds". |
| 0:24–0:36 | "These are the exact products used on every client who walks in looking decades older and leaves feeling confident and complete again. The last one may be the one thing standing between you and looking 20 years younger." | Woman holds a wicker basket covered with gold satin cloth (0:25–0:35). Captions "these are the exact products used on every client", "who walks in looking decades older", "and leaves feeling confident and complete again", "the last one may be the one thing standing between you", "and looking 20 years younger". |
| 0:36–0:46 | Item 1 — "First, under eye cream with a concealer, I use Clinique All About Eyes. Just a small amount, press gently under the eye, let it absorb for a moment before anything goes on top." | 0:37 woman holds pink-lidded jar labelled "CLINIQUE" (left) and a NARS concealer wand (right); 0:39–0:45 jar alone, man points at it. Captions "first under eye cream with a concealer", "I use Clinique all about eyes", "just a small amount press gently under the eye", "let it absorb for a moment before anything goes on top". |
| 0:46–0:59 | Item 2 — "Then NARS concealer under the eye. Most concealers on mature skin compress into every crease and sink into the corner of the eye. This one doesn't. It diffuses light instead of sitting in the crease, so the eye looks lifted and rested instead of tired and heavy." | NARS concealer tube (black cap, "NARS" printed on tube) held up 0:47–0:59. Captions "then NARS concealer under the eye", "most concealers on mature skin", "compress into every crease", "and sink into the corner of the eye", "it diffuses light instead of sitting in the crease", "so the eye looks lifted and rested", "instead of tired and heavy". |
| 0:59–1:17 | Item 3 — "Next, by Mario Cream Bronzer. The older you get, the more your face loses warmth and dimension. A face without bronzer after 50 reads as flat and tired, no matter how good the rest of your makeup is. Take a brush, blend it out, and do not use a sponge. Always a brush on mature skin, and suddenly there is life back in the face." | Open white compact, lid shows "by MARIO" (text appears mirror-reversed: "OIЯAM") — i.e. Makeup by Mario; tan cream bronzer pan (1:01–1:17). Captions "next by Mario Cream Bronzer", "the more your face loses warmth and dimension", "a face without bronzer after 50 reads as flat and tired", "no matter how good the rest of your makeup is", "take a brush blend it out and do not use a sponge", "and suddenly there is life back in the face". |
| 1:17–1:28 | Item 4 — "Then Too Faced blush. Press it into the cheek and pull it all the way toward the nose. Chef's kiss. That is the difference between color that is on the face and color that looks like it belongs there." | Gold-rimmed compact with bright pink pan and script logo (brand script not legible at frame size) 1:19–1:27; man does a chef's-kiss gesture at 1:23. Captions spell it "then two faced blush press it into the cheek", "and pull it all the way toward the nose", "chef's kiss that is the difference between color", "that it's on the face", "and color that looks like it belongs there". |
| 1:28–1:38 | Item 5 — "Now finish the lips. A lip gloss on top reflects off the shine and makes the lips appear fuller. On mature skin, the lips lose volume. This, this is the easiest fix most women never think of." | Pink liquid lip product with black cap, "e.l.f." printed on tube (1:29–1:37) — brand is NOT said aloud. Captions "now finish the lips a lip gloss on top", "reflects off the shine and makes the lips appear fuller", "on mature skin the lips lose volume", "this this is the easiest fix most women never think of". |
| 1:38–2:04 | Item 6 (sold product) — "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely. Foundation. Most foundations on mature skin look like makeup. Luxe foundation is specifically developed for mature skin. It helps blur fine lines, smooth texture, and look natural, not heavy. And it almost never settles into wrinkles. It is the number one best-selling foundation on Amazon right now." | Woman holds a cream/beige squeeze tube printed vertically "Luxe" (1:39–1:59). Captions "but one step is missing", "and this is the step that makes you look less tired", "brings your face to life", "and yet most women miss it completely foundation", "most foundations on mature skin look like makeup", "is specifically developed for mature skin", "smooth texture and look natural", "not heavy and it almost never settles into wrinkles", "it is the No. 1 best selling foundation on Amazon" (2:01–2:03). Tube put down by 2:01. |
| 2:04–2:28 | CTA (see below) | Two-shot, no product, captions only. |

Rehooks / open loops:
- 0:00–0:11 "The reason you look twice your age is not because you are old ... but because your outdated makeup techniques and products are quietly and brutally working against you." (problem/curiosity open)
- 0:16–0:24 "Get rid of that matte lipstick, throw away the heavy mascara, and stop using primer altogether" (contrarian "throw out" list)
- 0:24–0:31 "These are the exact products used on every client who walks in looking decades older" + covered basket prop (reveal tease)
- 0:31–0:36 "The last one may be the one thing standing between you and looking 20 years younger." (saved-for-last loop)
- 0:53 "This one doesn't." (micro-contrast)
- 1:35–1:38 "This, this is the easiest fix most women never think of."
- 1:38–1:46 "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." (pivot into pitch)

### PRODUCT
- Product sold: foundation — brand Luxe — "Luxe foundation" as said (1:49.84); tube printed "Luxe" (small print on tube not legible). No shade or full product name said or shown.
- First appears: 1:45.84 spoken ("Foundation."), brand named 1:49.84 ("Luxe foundation"); on screen first in the 1:39 frame (not in the 1:37 frame) — woman holds the beige tube upright beside her face, "Luxe" printed vertically.
- Bridge line (verbatim, with timestamp): "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." (1:38.60–1:45.84) → "Foundation." (1:45.84)
- Saved for last? yes — item 6 of 6 (after Clinique, NARS, Makeup by Mario, Too Faced, e.l.f.), starts at 1:38.60 of 2:27.9; flagged early at 0:31 ("The last one may be the one thing...").
- Product shots: single held-up tube, static, no application, no swatch, no texture shot, no price. The only "before/after" is the hook (0:00–0:11 heavy-makeup look vs. 0:13 onward polished look); it is not tied to the foundation specifically.

### CTA
- Spoken (verbatim + timestamps):
  - "It is the number one best-selling foundation on Amazon right now." (2:00.32–2:04.64)
  - "Link is on my profile, and I also added the link in the comments for anyone who could not find it." (2:04.64–2:09.76)
  - "Sometimes there's a coupon available, so hurry up if you are over 60 and give this routine a chance." (2:09.76–2:15.12)
  - "I think you will never want to use anything else again." (2:15.12–2:18.00)
  - "And if you would like the list of these products and a quick explanation of what each one does, just comment natural and I will send it to you. But you have to follow me first so I can message you." (2:18.00–2:27.84)
- On-screen text (verbatim + timestamp): captions only — "it is the No. 1 best selling foundation on Amazon" (2:01–2:03), "right now link is on my profile" (2:05), "and I also added the link in the comments" (2:07), "for anyone who could not find it" (2:09), "so sometimes there's a coupon available" (2:11), "so hurry up if you are over 60" (2:13), "and give this routine a chance" (2:15), "I think you will never wanna use anything else again" (2:17), "and if you would like the list of these products" (2:19), "and a quick explanation of what each one does" (2:21), "just comment natural and I will send it to you" (2:23), "but you have to follow me first so I can message you" (2:25–2:27). No button, URL or Amazon search term on screen.
- Where it points: link on profile/bio + link in comments (foundation; Amazon implied by "best-selling foundation on Amazon"); "comment natural" DM automation for the product list, with follow-first gate. Caption repeats both ("COMMENT "natural"", "follow me first", "Link for the foundation is on my profile (bio) and in the comments").

### AVATAR
- Who: "expert" — positioned as a makeup artist working on clients: "every client who walks in looking decades older" (0:24–0:29), "I use Clinique All About Eyes" (0:36), hashtag "#makeupartist". No named credential, salon or years of experience stated. The speaker is a young man (reading: early-mid 20s), white/European-looking, platinum-blond curly hair, wire aviator glasses, black T-shirt; in the hook (0:00–0:11) his skin looks heavily made up (contoured, matte), later more natural. The woman (the "client"/model) is silent: reading 60s, white/European-looking; before = short grey curly hair, heavy smoky eye, black top; after = long brown highlighted blowout, cream satin robe, hoop earrings, thin gold necklace.
- Setting & lighting: makeup studio/salon — dark green panelled walls with a small gold/white floral emblem at left, white ceiling with downlights, ring light. Hook shot is tighter with the ring light directly behind; rest is a wider two-shot. Looks like a fixed camera at face height (selfie-style framing, man leaning into frame), soft even front light.
- Real or AI-looking (my reading): no "syntheticmedia" or other AI watermark seen on any sheet. Faces look like filmed people with natural movement (head tilts, blinks, hand gestures); lip-sync not checkable from stills. Points that could be checked: the hook "before" woman and the "after" woman differ in hair length, colour and texture and in face shape detail — could be the same woman (wig/styling) or a different person or an edited/generated "before"; the man's skin also changes between segments. The Luxe tube's small print is illegible/garbled at this resolution; the Mario lid text reads mirror-reversed (could be print on the outside of a clear lid). Not enough to call it AI either way.
- Delivery: brisk, energetic, exaggerated facial expressions (grimaces 0:07–0:11, wide-eyed "oh" 2:03), conversational; slang "Chef's kiss" (1:23) with gesture; no swearing. Strong words: "quietly and brutally working against you" (0:04–0:11). Only the man speaks.
- Who else appears: the woman (before and after looks) holding every product; man's hands touching her chin and pointing at products. No other people.

### CLAIMS & COMPLIANCE
- 0:00–0:11 "The reason you look twice your age is not because you are old ... but because your outdated makeup techniques and products are quietly and brutally working against you."
- 0:16–0:24 "Get rid of that matte lipstick, throw away the heavy mascara, and stop using primer altogether, because these products were made for 20-year-olds, not for your mature skin."
- 0:24–0:31 "These are the exact products used on every client who walks in looking decades older and leaves feeling confident and complete again." (client/testimonial framing)
- 0:31–0:36 "The last one may be the one thing standing between you and looking 20 years younger." (result promise)
- 0:53–0:59 NARS: "This one doesn't. It diffuses light instead of sitting in the crease, so the eye looks lifted and rested"
- 1:08–1:10 "A face without bronzer after 50 reads as flat and tired"
- 1:29–1:33 lip gloss "makes the lips appear fuller"
- 1:46–1:49 "Most foundations on mature skin look like makeup." (comparative vs. category)
- 1:49–1:53 "Luxe foundation is specifically developed for mature skin."
- 1:53–1:58 "It helps blur fine lines, smooth texture, and look natural, not heavy."
- 1:57–2:00 "And it almost never settles into wrinkles."
- 2:00–2:04 "It is the number one best-selling foundation on Amazon right now." (bestseller claim)
- 2:09–2:15 "Sometimes there's a coupon available, so hurry up if you are over 60" (urgency/discount)
- 2:15–2:18 "I think you will never want to use anything else again."
- No prices, percentages, ingredient counts or "same company owns" claims.
- "Ad"/"#ad"/"Sponsored"/"paid partnership" shown? No "Sponsored" or "paid partnership" label in the metadata, and none on screen. The caption (and page title) begins "adl COMMENT ..." — reading: possibly an "ad |" disclosure that has been rendered/typed as "adl"; as written it is not a clear disclosure. No "AD |" prefix on the page title line.
- AI disclosure shown? None seen (no watermark, no caption note).
- Risk notes (my reading): "number one best-selling foundation on Amazon right now" needs substantiation (and a date/category); "blur fine lines", "almost never settles into wrinkles", "looking 20 years younger" are performance/result claims; the page presents itself as an independent makeup artist with real-brand picks (Clinique, NARS, Makeup by Mario, Too Faced, e.l.f.) while the link and pitch go only to Luxe — if there is a brand relationship, the "adl" caption opener is a weak disclosure; the before/after is not shown to be the same person or the result of these products; "every client" implies an artist practice not evidenced.

### WHY IT WORKS
A shocking "twice your age" before/after plus a "throw these out" list hooks women 50+ through fear of looking old, then trusted department-store brands build credibility one by one.
The house product is held back as the "missing step" that was teased at 0:31, so the pitch lands as the payoff, and two CTAs (link + "comment natural" behind a follow gate) turn viewers into followers and buyers.

### OBSERVER NOTES (optional)
- Measured: view_count 21,791 vs title-line "42K views" (about 1.9x), 224 reactions; posted 2026-09-08.
- Measured: 6 products in 1:38 of body; the Luxe segment (1:38.6–2:04.6) is about 26 s, the longest single item, and the CTA tail is about 23 s (2:04.6–2:27.8).
- Reading: the e.l.f. gloss is shown but never named, while every other item is named — the brand mentions look chosen for prestige.
- Reading: the covered-basket prop at 0:25–0:35 is a visual "mystery box" for the product list but is never opened on camera.
- Reading: "comment natural" keyword matches the "look natural, not heavy" claim; the follow-first gate is a follower-growth mechanic.
- Transcript spellings checked against captions/packaging: "by Mario Cream Bronzer" (caption same; lid reads "by MARIO" = Makeup by Mario); "Too Faced" (transcript) vs caption "two faced"; "Luxe" (transcript and tube agree).

---

## Video 5 — Minho Makeup & Beauty — "If your eyes make you look decades older" (3-step mature eye routine, concealer ban turns into Luxe foundation pitch)
**Link:** https://www.facebook.com/share/v/1JTghxd7ii/ (video ID 807894659075122) · **Page:** Minho Makeup & Beauty · **Uploaded:** 2026-09-02 (info.json timestamp 1788391232 = 23:20 UTC) · **Duration:** 2:29 (148.8 s) · **Views:** view_count 30,810 (page title line says "62K views") · **Reactions:** 432 (from title line "62K views · 432 reactions") · **Comments:** not found (comment_count = None in metadata)
*(All metadata from videos/5.info.json, yt-dlp pull 2026-11-07.)*

**Caption (verbatim):** "adl COMMENT "eyes" and I will send you the exact ROUTINE EXPLAINED with a LIST of the PRODUCTS PLUS all the proven MAKEUP TIPS for MATURE women.🤯🥰😘

But you have to follow me first so i can message you. ☺️

Link for the foundation is on my profile (bio) and in the comments.

#maturemakeuproutine #makeupartist #makeupforolderwomen #wrinkleshack  #makeup #maturemakeup #womenover60 #womenover50 #womenover40"

Note (measured): caption comment word "eyes" matches the spoken and on-screen word (2:17–2:22). Caption starts with "adl" (same as video 2; meaning not clear). The caption names "the foundation" but not the brand.

### HOOK (0:00–0:05)
- Spoken: 0:00.0–0:03.4 "If your eyes makes you look decades older, tired," → 0:03.4–0:06.0 "like your makeup is working against you" → 0:06.0–0:08.6 "and you wanna look youthful, confident and beautiful" → 0:08.6–0:12.1 "even at 50, 60 or 70, here's what nobody tells you."
- On-screen text (burned-in white captions, lower-middle; no separate headline or title card at any point): 0:00–0:02 "if your eyes makes you look decades older"; 0:03–0:05 "tired like your makeup is working against you"; 0:07 "and you wanna look youthful"; 0:09 "confident and beautiful even at 50"; 0:11 "here's what nobody tells you".
- Visual: vertical two-shot in a makeup studio (Hollywood bulb mirror, brush cups, foundation bottles, eyeshadow display behind). 0:00–0:05 = "before" woman: silver/grey straight bob, very heavy black smoky eye with false lashes, deep forehead and cheek wrinkles, unsmiling, dark green tee. A young platinum-blond man in large wire aviator glasses and a black tee stands behind her, hand on top of her head (0:00–0:01), cupping her chin, gesturing at camera. Hard cut at ~0:06/0:07 to the "after" woman: honey-blonde straight bob, soft winged liner, light makeup, beige top, man cupping her chin. Reading: works as an instant before/after; the two women look like different people (different face shape and hairline), not the same woman restyled.

### FORMAT
"Throw away X / use this instead" mature eye routine, with the sold product slipped in as the replacement for a banned item (concealer → Luxe foundation).
Opens by banning concealer, eyeshadow and heavy mascara for women over 50, promises "the exact products used on every client", walks two real-brand products (Clinique eye balm, MAC eyeliner), then a "nobody is telling women over 50" concealer myth-bust that resolves into Luxe foundation as the last item. Same page template as video 2 (covered basket prop, chin-cup, store settings, "comment X" + follow gate).

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:12–0:23 | Problem set-up: "After 50, the skin around your eyes changes completely." "It thins out, it loses elasticity and everything you used to put on it starts working against you instead of for you." | After-woman, man behind; captions "after 50 the skin around your eyes changes completely" (0:13–0:15), "it thins out it loses elasticity" (0:17), "and everything you used to put on" (0:19), "it starts working against you instead of for you" (0:21–0:23). 0:15 man adjusts his glasses. |
| 0:23–0:33 | Ban list: "Throw away the concealer, throw away the eyeshadow and stop using heavy mascara altogether because these products were made for 20-year-olds, not for your mature skin." | 0:25 man holds up a 9-pan nude/shimmer eyeshadow palette (black case, no legible brand), caption "throw away the eyeshadow". 0:27–0:31 he holds a pink Maybelline "Lash Sensational" mascara tube (brand and name legible on tube, not said), captions "and stop using heavy mascara all together", "because these products were made for 20 year olds". "throw away the concealer" caption and any concealer product: not captured in sampled frames (would fall between 0:23 and 0:25). |
| 0:33–0:40 | Promise: "These are the exact products used on every client who walks in looking decades older and leaves feeling confident and complete again." | 0:33–0:39 woman holds a black-and-white chevron wicker basket covered with a beige linen cloth; captions "these are the exact products used on every client", "who walks in looking decades older", "and leaves feeling confident and complete again". Basket is never uncovered in any sampled frame. |
| 0:40–1:02 | 1. Eye balm: "First, Clinique All About Eyes Under Eye Balm." "Press a small amount gently under the eye using your ring finger, not your index finger, too much pressure." "Pat it in, do not rub." "Wait a moment for it to fully absorb before anything goes on top." "This hydrates, plumps and creates a base so everything actually holds instead of creasing and settling into every fold." | Scene change to a Clinique counter (green/white Clinique shelves). Man holds peach/pink Clinique jar with silver lid (label "CLINIQUE", sub-line not legible) beside the smiling woman; points under his own eye (0:45–0:47). Captions "first Clinique" (0:41), "all about eyes under Eye Balm" (0:43), "press a small amount gently under the eye", "using your ring finger not your index finger", "Pat it in do not rub", "wait a moment for it to fully absorb", "before anything goes on top", "this hydrates plumps", "and creates a base so everything actually holds", "instead of creasing and settling into every fold" (1:01). No application shown. |
| 1:02–1:23 | 2. Eyeliner: "Next, MAC Eyeliner, applied close to the lash line using small strokes, not one long drag." "Draw as close to the lashes as possible." "This defines and lifts the eye without adding weight." "It makes the eye appear larger and more awake." "No heavy shadow, no thick liner, just a clean line that does more than any eyeshadow ever could on mature skin." | Scene change to a dark makeup counter (eye-product display, man's tee shows "MAC" logo on sleeve at 1:05–1:07). Man holds a black liquid-liner pen and mimes lining near her upper lash line (1:05, 1:07, 1:11); woman's eyes closed at 1:17. Captions "next Mac eyeliner" (1:03), "applied close to the lash line using small strokes", "not one long drag", "draw as close to the lashes as possible", "this defines and lifts the eye without adding weight", "it makes the eye appear larger and more awake", "no heavy shadow no thick liner", "just a clean line", "that does more than any eyeshadow ever could", "on mature skin" (1:23). Reading: pen touches near the lash line but no clear line visibly drawn. |
| 1:23–1:47 | 3. Concealer myth-bust → foundation: "And here is something nobody is telling women over 50, stop using concealer under your eyes." "Concealer on mature skin sits on top, compresses into every crease and makes the eye bags look worse, not better." "What you actually need is the right foundation applied with a brush, never a sponge in light dabbing motions under the eye." "One that hydrates, integrates and covers without sitting heavy on the skin." | Scene change at 1:25 to a store foundation wall (orange/grey fixture, partial sign "…RA" top right). Man holds beige squeeze tube with vertical black "Luxe" wordmark from 1:25 onward. Captions "and here is something nobody is telling women over 50" (1:25), "stop using concealer under your eyes", "concealer on mature skin sits on top", "compresses into every crease", "and makes the eye bags look worse", "not better", "what you actually need is the right foundation" (1:37, man points at tube), "applied with a brush never a sponge", "in light dabbing motions under the eye", "integrates and covers without sitting heavy on the skin" (1:45). No brush shown. |
| 1:47–2:04 | 4. PITCH, Luxe foundation: "The reason I recommend Luxe Foundation is because it is specifically developed for mature skin." "It matches your skin tone correctly, hydrates as it covers and rarely ever feels heavy on the skin." "It almost never settles into wrinkles and it is the number one best selling foundation on Amazon right now." | Tube held up at chest/face height throughout. Captions "the reason I recommend Lux Foundation" (1:47 — caption misspells; tube reads "Luxe"), "is because it is specifically developed for mature skin", "it matches your skin tone correctly", "hydrates as it covers", "and rarely ever feels heavy on the skin", "it almost never settles into wrinkles", "and it is the No. 1 best selling foundation on Amazon" (2:01–2:03). No application, swatch or before/after of the foundation. |
| 2:04–2:29 | CTA block + close (see CTA): "If you are over 50 and give this routine a chance, I think you will never want to use anything else again." | Tube held to the end. 2:19–2:21 larger quoted word ""eyes"" above caption. Last captions "if you are over 50 and give this routine a chance" (2:23–2:25), "I think you will never want to use anything else again" (2:27). |

**Rehooks / open loops**
- 0:08.6–0:12.1 "here's what nobody tells you."
- 0:23.4–0:32.8 "Throw away the concealer, throw away the eyeshadow and stop using heavy mascara altogether" (ban list sets up "so what do I use instead?")
- 0:32.8–0:40.2 "These are the exact products used on every client who walks in looking decades older and leaves feeling confident and complete again." (with covered basket 0:33–0:39, never opened)
- 1:23.2–1:28.5 "And here is something nobody is telling women over 50, stop using concealer under your eyes."
- 1:35.1–1:37.4 "What you actually need is the right foundation" (pays off the concealer ban)
- 2:09.8–2:13.8 "Sometimes there is a coupon available so hopefully you can grab it."

### PRODUCT
- Product sold: foundation — brand "Luxe" (spoken "Luxe Foundation"; tube wordmark "Luxe"; burned-in caption spells it "Lux Foundation" at 1:47). Exact product name beyond "Luxe Foundation": not said; tube small print not legible (crop of 1:53 frame shows blurred/garbled lines above and below the wordmark).
- First appears: 1:46.6 spoken ("The reason I recommend Luxe Foundation"; the category "the right foundation" is spoken at 1:35.1); 1:25 on screen (first sampled frame with it: man holds the beige "Luxe" tube upright at chest height in front of a store foundation wall, woman at right; not in the 1:23 frame, which is still the eyeliner counter).
- Bridge line (verbatim): 1:23.2–1:28.5 "And here is something nobody is telling women over 50, stop using concealer under your eyes." → 1:35.1–1:41.8 "What you actually need is the right foundation applied with a brush, never a sponge in light dabbing motions under the eye." → 1:41.8–1:46.6 "One that hydrates, integrates and covers without sitting heavy on the skin." → 1:46.6 "The reason I recommend Luxe Foundation…"
- Saved for last? yes — item 3 of 3 named products (Clinique balm, MAC liner, Luxe foundation; plus the banned palette and mascara shown earlier); on screen from 1:25 and named from 1:46.6 of 2:28.9; the tube stays in hand through the whole CTA to the end.
- Product shots: beige/nude squeeze tube, white flip cap at bottom, large vertical black "Luxe" wordmark, small unreadable print above and below. Only ever held up to camera by the man (tilted, pointed at); never opened, applied, swatched or compared. No before/after tied to it. The opening before/after (0:00–0:07) is the only transformation shown, and it is not attributed to any product.

### CTA
- Spoken: 2:03.8–2:09.8 "Link is on my profile and I also added the link in the comments for anyone who could not find it." 2:09.8–2:13.8 "Sometimes there is a coupon available so hopefully you can grab it." 2:13.8–2:20.0 "And if you would like the list of these products and a quick explanation of how to use them, just comment eyes and I will message you." 2:20.0–2:22.4 "But you have to follow me so I can message you." Also earlier, 2:01.9–2:03.8 "on Amazon right now."
- On-screen text: 2:05 "link is on my profile"; 2:07 "and I also added the link in the comments"; 2:09 "for anyone who could not find it"; 2:11 "sometimes there is a coupon available"; 2:13 "so hopefully you can grab it"; 2:15 "and if you would like the list of these products"; 2:17 "and a quick explanation of how to use them"; 2:19 large ""eyes"" + "just comment eyes and I will message you"; 2:21 large ""eyes"" + "but you have to follow me so I can message you". Caption repeats: "COMMENT "eyes"…", "But you have to follow me first so i can message you.", "Link for the foundation is on my profile (bio) and in the comments."
- Where it points: link in profile/bio + link in comments (Amazon implied by "number one best selling foundation on Amazon"; destination URL not visible in the video); "comment eyes" DM automation with a follow-first gate; coupon tease.

### AVATAR
- Who: "expert" — implied professional makeup artist. Words used: "every client who walks in looking decades older" (0:35); "The reason I recommend" (1:46); hashtag "#makeupartist" in caption. No name, title or certification stated. Approx age: 20s (reading). Apparent ethnicity: white (reading). Gender: male. Clothing: plain black crew-neck tee (MAC logo on the sleeve visible 1:05–1:09), large clear wire aviator glasses, small earring, bleached platinum crop. The "client" women: "before" ~70s grey bob in green tee; "after"/demo woman ~60s honey-blonde bob in beige top (ages are reading).
- Setting & lighting: four settings, cut by product — (1) makeup studio with bulb mirror and brushes (0:00–0:39); (2) Clinique counter (0:41–1:01); (3) dark MAC-style counter with eye-product display (1:03–1:23); (4) retail foundation wall with partial sign "…RA" (1:25–end; reading: looks like a Sephora-type store, sign not fully visible). Selfie-height framing, man leaning into frame as if holding the phone; even bright retail/ring lighting.
- Real or AI-looking: no "syntheticmedia" or other AI watermark seen on any sampled frame (zoomed 0:01). My reading: likely AI-generated or heavily composited — (a) the man and the after-woman are relocated into a new branded store for each product with identical clothing/poses, (b) the before-woman and after-woman are clearly different faces, (c) small print on the Luxe tube is garbled rather than real text, (d) very smooth, highly expressive face with exaggerated mouth shapes, (e) same man/basket/chin-cup template as video 2 on this page. Not confirmed.
- Delivery: fast, energetic, exaggerated facial expressions (wide-open mouth, teeth-baring grins); instructional imperative tone ("Throw away…", "Pat it in, do not rub"). No slang or swearing. Casual-confident, not formal. Minor grammar slip "If your eyes makes you look" (spoken and captioned).
- Who else appears: the grey-haired "before" woman (0:00–0:05); the blonde "after"/model woman (0:07–end, silent, smiling, holds the basket); the man's hands on the women's chins/heads.

### CLAIMS & COMPLIANCE
- 0:12.1–0:23.4 "After 50, the skin around your eyes changes completely. It thins out, it loses elasticity and everything you used to put on it starts working against you instead of for you."
- 0:28.8–0:32.8 "these products were made for 20-year-olds, not for your mature skin." (about concealer, eyeshadow, heavy mascara; a Maybelline Lash Sensational tube is shown at 0:27–0:31)
- 0:32.8–0:40.2 "These are the exact products used on every client who walks in looking decades older and leaves feeling confident and complete again." (implied client results / credential)
- 0:54.5–1:02.0 Clinique: "This hydrates, plumps and creates a base so everything actually holds instead of creasing and settling into every fold."
- 1:09.5–1:23.2 MAC: "This defines and lifts the eye without adding weight. It makes the eye appear larger and more awake." "does more than any eyeshadow ever could on mature skin."
- 1:28.5–1:35.1 "Concealer on mature skin sits on top, compresses into every crease and makes the eye bags look worse, not better."
- 1:46.6–1:52.3 "it is specifically developed for mature skin."
- 1:52.3–1:57.6 "It matches your skin tone correctly, hydrates as it covers and rarely ever feels heavy on the skin."
- 1:57.6–1:59.5 "It almost never settles into wrinkles"
- 1:59.5–2:03.8 "it is the number one best selling foundation on Amazon right now." (on-screen "No. 1 best selling foundation on Amazon")
- 2:09.8–2:13.8 "Sometimes there is a coupon available so hopefully you can grab it." (price/discount tease, no price given)
- 2:22.4–2:28.9 "If you are over 50 and give this routine a chance, I think you will never want to use anything else again."
- Prices: none said or shown.
- "Ad"/"#ad"/"Sponsored"/"paid partnership": none found in caption, page title line or on-screen text. The only odd marker is the caption prefix "adl" — not a recognisable ad disclosure (reading).
- AI disclosure: none seen (no "syntheticmedia" or similar watermark on sampled frames; caption has no AI label).
- Risk notes (my reading): (1) "number one best selling foundation on Amazon right now" is a ranking claim that would need substantiation; (2) "every client" + "I recommend" implies a professional artist endorsement with no disclosed relationship to Luxe; (3) recommendation framed as independent advice alongside real brands (Clinique, MAC, Maybelline) while the Luxe tube is the only product linked — material-connection disclosure missing; (4) filmed in what look like branded retail counters (Clinique, MAC, a "…RA" store), which can imply retailer/brand association; (5) disparages concealer, eyeshadow and heavy mascara in general ("made for 20-year-olds"); (6) the opening before/after uses two different women and is not tied to any product; if AI-generated, there is no AI disclosure.

### WHY IT WORKS
A shock before/after plus "throw away your concealer" turns a habit every viewer has into a fear, and the "nobody is telling women over 50" reveal makes the foundation feel like the fix rather than an ad.
The two real prestige brands (Clinique, MAC) lend borrowed credibility before Luxe appears, and the tube sits in frame for the last minute while the CTA stacks link, coupon and "comment eyes".

### OBSERVER NOTES (optional)
- Measured: the Luxe tube is on screen from 1:25, ~21 s before the brand is spoken (1:46.6), so it is in view for ~64 s of 149 s (~43%).
- Measured: title-line views (62K) are ~2x yt-dlp view_count (30,810), same pattern as METADATA.md notes.
- Measured: the caption says "Link for the foundation", and the video never names Clinique or MAC as linked; only the foundation gets a link.
- Reading: near-identical script skeleton to video 2 from the same page ("look decades older… makeup is working against you… youthful, confident and beautiful even at 50, 60 or 70", "made for 20-year-olds, not for your mature skin", covered basket, "number one best-selling foundation on Amazon right now", "Sometimes there is a coupon", "comment X… follow me"), with the eyes as the angle instead of the full face. Looks like a templated series.
- Reading: the "concealer → use foundation under the eyes instead" swap is the key mechanism: it converts a banned category into demand for the sold product.

---

## Video 6 — Minho Makeup & Beauty — "Throw away the matte lipstick" (mature-makeup routine, Luxe foundation saved for last) — MASTER BREAKDOWN FOR VIDEOS 6 AND 7
**Link:** https://www.facebook.com/share/v/1B8kDn1stW/ (video ID 898472679696406) · **Page:** Minho Makeup & Beauty (uploader_id 61589098220612) · **Uploaded:** 2026-08-30 (info.json timestamp 1788070972 = 06:22:52 UTC) · **Duration:** 2:19 (139.67 s) · **Views:** view_count 32,422 (page title line says "60K views") · **Reactions:** 367 (from title line "60K views · 367 reactions") · **Comments:** not found (comment_count = None in metadata)
*(All metadata from videos/6.info.json and videos/7.info.json, yt-dlp pull 2026-11-07.)*

**Caption (verbatim):** "adl COMMENT "glow" and I will send you the exact ROUTINE EXPLAINED with a LIST of the PRODUCTS PLUS all the proven MAKEUP TIPS for MATURE women.🤯🥰😘 But you have to follow me first and like the video so i can message you. ❤️ #maturemakeuproutine #makeupartist #makeupforolderwomen #wrinkleshack #makeup #maturemakeup #womenover60 #womenover50 #womenover40makeup"

**Video 7 = same file (measured).** videos/6.mp4 and videos/7.mp4 have the same MD5 (5954f911362019f4d8de7bd9026143a6), same duration (139.668 s), both 1080x1920. Everything below (hook, beats, product, CTA, avatar, claims) applies to both.

| | Video 6 | Video 7 |
|---|---|---|
| Share URL | https://www.facebook.com/share/v/1B8kDn1stW/ | https://www.facebook.com/share/v/1DfiwTsQnp/ |
| Video ID | 898472679696406 | 1084335064173234 |
| Upload (UTC) | 2026-08-30 06:22:52 | 2026-08-26 23:26:45 |
| view_count | 32,422 | 40,391 |
| Title line | "60K views · 367 reactions" | "70K views · 479 reactions" |
| Last hashtag in caption | "#womenover40makeup" | "#womenover40" |
| Thumbnail URL | different fbcdn file (…788791605_…) | different fbcdn file (…787760641_…) |

- Caption text is otherwise character-for-character identical (checked with a diff: the only difference is "#womenover40makeup" vs "#womenover40"; both include the same double space after "#wrinkleshack").
- Order (measured): **7 was posted first** (Aug 26); 6 is the re-post, 3 days 7 hours later. The re-post got fewer views (32,422 vs 40,391 view_count; 60K vs 70K title line).
- Video 8's caption (from METADATA.md) is also the same text with "🤍" in place of "😘" and ends "#womenover40" — same caption template; not analysed here.

### HOOK (0:00–0:05)
- Spoken: 0:00.00–0:04.72 "If you look decades older and like your makeup is working against you, don't worry." → 0:04.72–0:09.76 "You can absolutely look youthful and sexy after 50, 60, or 70."
- On-screen text (burned-in white captions with thin dark outline, middle of frame, lower-case; no headline or title card at any point): 0:00–0:01 "if you look decades older"; 0:02–0:04 "and like your makeup is working against you"; ~0:04.2–0:04.7 "don't worry"; 0:05–0:07 "you can absolutely look youthful and sexy after 50".
- Visual: vertical two-shot inside a black-and-white cosmetics store (Hollywood-bulb vanity mirror and makeup gondolas behind). 0:00–0:04 a "before" woman: auburn/brown bob with fringe, heavy dark eye shadow, strong pink blush, deep wrinkles, unsmiling, sage-green button shirt. A young platinum-blond man (clear wire glasses, black polo) stands behind her, one hand resting on top of her head, the other gesturing at camera. Hard cut at 0:04.73 (scene cut measured with ffmpeg) to a different, younger-looking "after" woman (honey-blonde bob, soft natural makeup, cream satin V-neck blouse), smiling, same man and same store backdrop; he points a finger up on "absolutely". Reading: the cut works as an instant before/after, but the two women look like different people, not one woman made over.

### FORMAT
"Throw these away / use these instead" mature-makeup routine with the sold product hidden as "the last one" / "the one step most women miss".
Bans three products (matte lipstick, heavy mascara, primer), teases a covered basket ("The last one may be the one thing standing between you and looking 20 years younger"), walks five real-brand items (Clinique, NARS, a Makeup by Mario-looking bronzer, Too Faced, a lip gloss), then reveals Luxe foundation as the missing step and closes with link-in-comments + "comment GLOW" DM automation. Same script skeleton as video 2 (a few lines trimmed/moved; see Observer notes).

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:09–0:20 | Ban list: "Throw away the matte lipstick, throw away the heavy mascara, and stop using primer altogether." / "Because these products were made for 20-year-olds, not for your mature skin." | 0:09–0:11 caption "60 or 70 throw away the matte lipstick"; 0:11 man holds a mauve/brown bullet lipstick in a silver case (no brand visible). 0:13 caption "throw away the heavy mascara", he holds a glossy black mascara with a mint-green ornate heart/bow design on the cap (no legible brand). 0:15–0:19 captions "and stop using primer altogether", "because these products were made for 20 year olds", "not for your mature skin"; he holds a clear-blue gel tube with black caps at BOTH ends (no brand). |
| 0:20–0:29 | Promise + tease: "Let me show you what products to use so you can finally feel beautiful and confident again." / "The last one may be the one thing standing between you and looking 20 years younger." | Cut at 0:20.17. Woman holds a wire shopping basket covered with red satin cloth; man gestures at it (0:21) and points at camera (0:25). Captions "let me show you what products to use", "so you can finally feel beautiful and confident again", "the last one may be the one thing standing between you", "and looking 20 years younger". Basket is never opened on camera. |
| 0:29–0:41 | 1. Eye cream: "First, under eye cream with a concealer." "I use Clinique All About Eyes." "Just a small amount pressed gently under the eye." "Let it absorb for a moment before anything goes on top." | Cut at 0:29.67 to a new aisle ("SEP…" sign behind), woman now in a sage-green V-neck blouse. Man holds a small peach jar with silver lid; label reads "CINQIJE"-like garbled letters (hi-res frame 0:33), not a clean "CLINIQUE". Clip-on lapel mic visible on his polo at 0:33. Captions "first under eye cream with a concealer", "I use Clinique all about eyes", "just a small amount press gently under the eye", "let it absorb for a moment before anything goes on top". No application shown. |
| 0:39–0:54 | 2. Concealer: "Then NARS concealer under the eye." "Most concealers on mature skin compress into every crease and sink into the corner of the eye." "This one doesn't." "It diffuses light instead of sitting in the crease, so the eye looks lifted and rested instead of tired and heavy." | Cut at 0:39.50. Man holds a slim tan concealer wand with dark cap (brand mark not legible), taps under his own eye (0:45). Woman in a round-neck green top. Captions "then NARS concealer under the eye", "most concealers on mature skin", "and into the corner of the eye", "this one doesn't", "it diffuses light instead of sitting in the crease", "so the eye looks lifted and rested", "instead of tired and heavy". |
| 0:53–1:17 | 3. Cream bronzer (brand not said): "So next, cream bronzer." "The older you get, the more your face loses warmth and dimension." "A face without bronzer after 50 reads as flat and tired, no matter how good the rest of your makeup is." "That is the difference between color that sits on the face and color that looks like it belongs there." "Take a brush, blend it out, and do not use a sponge. Always a brush, and suddenly there is life back in the face." | Cut at 0:53.80 to a busier aisle with shoppers walking behind (one in a blue face mask). Open white round compact with brown cream bronzer; lid text appears upside-down/mirrored and reads like "MARIO" (reading: Makeup by Mario packaging; brand never said). Captions "so next cream bronzer", "the more your face loses warmth and dimension", "a face without bronzer after 50 reads as flat and tired", "no matter how good the rest of your makeup is". 1:04.47–1:09.37 a separate clip shows him holding the PINK Too Faced blush while the bronzer lines "that is the difference between color" / "that sits on the face" / "and color that looks like it belongs there" play (product/script mismatch). 1:09.37 back to bronzer: "take a brush blend it out and do not use a sponge", "always a brush", "and suddenly there is life back in the face". No brush or blending shown. |
| 1:16–1:23 | 4. Blush: "Then Too Faced blush." "Press it into the cheek and pull it all the way toward the nose." "Chef's kiss." | Cut at 1:16.30. Round pink compact with cursive gold "Too Faced"-like script (letters garbled at hi-res). At 1:21 he holds a plain pink round object with no lid text. Captions "then Too Faced blush", "and pull it all the way toward the nose", "Chef's Kiss now finish the lips". |
| 1:22–1:32 | 5. Lip gloss: "Now finish the lips." "A lip gloss on top reflects off the shine and makes the lips appear fuller." "On mature skin, the lips lose volume." "This is the easiest fix most women never think of." | Cut at 1:22.23. Man holds a square-bottle rosy-nude gloss with black cap; logo on the bottle not legible/garbled (video 2 shows an e.l.f. gloss in the same beat; not confirmed here). Woman in a green cowl-neck blouse. Captions "a lip gloss on top reflects off the shine", "and makes the lips appear fuller", "on mature skin the lips lose volume", "yeah this is the easiest fix most women never think of" (caption adds "yeah"; transcript does not have it). |
| 1:32–1:59 | 6. REVEAL, Luxe foundation: "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." "Foundation." "Most foundations on mature skin look like makeup." "Luxe Foundation is specifically developed for mature skin." "It helps blur fine lines, smooth texture, and look natural, not heavy." "It almost never settles into wrinkles, and it is the number one best-selling foundation on Amazon right now." | Cut at 1:32.40 to a "SEPHORA"-signed aisle (one sign reads "SEPHURA"-like at 1:33; reading: garbled signage). Man holds a beige squeeze tube with vertical black "Luxe" wordmark; small print above/below is unreadable pseudo-text. Captions "but one step is missing", "and this is the step that makes you look less tired", "brings your face to life", "and yet most women miss it completely foundation", "most foundations on mature skin look like makeup", "Lux Foundation" (~1:44, caption misspells; tube reads "Luxe"), "is specifically developed for mature skin", "it helps blur fine lines", "smooth texture and look natural", "not heavy it almost never settles into wrinkles", "and it is the No. 1 best selling foundation on Amazon" (1:55–1:57). No application, swatch, price or before/after for the foundation. Tube stays in hand to the end. |
| 1:59–2:19 | CTA block (see CTA). | Captions "right now I added the link in the comments", "for anyone who could not find it", "sometimes", "there is a coupon available for a limited time", "so hopefully you can grab it if you are over 60", "and give this routine a chance", "I think you will never wanna use anything else again", "and if you would like the list of these products", "and a quick explanation of what each one does", "just comment glow", "and I will send it to you in a message" (to 2:19). |

**Rehooks / open loops**
- 0:20.16–0:24.48 "Let me show you what products to use so you can finally feel beautiful and confident again."
- 0:24.48–0:29.68 "The last one may be the one thing standing between you and looking 20 years younger." (with the covered red-satin basket on screen 0:21–0:29)
- 0:46.48–0:47.44 "This one doesn't." (contrast mini-loop after "Most concealers… sink into the corner of the eye")
- 1:29.52–1:32.40 "This is the easiest fix most women never think of."
- 1:32.40–1:39.68 "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." → 1:39.68 "Foundation."

### PRODUCT
- Product sold: foundation — brand "Luxe" (said "Luxe Foundation" at 1:43.84; transcript spells "Luxe"; tube wordmark reads "Luxe"; burned-in caption misspells it "Lux Foundation"). No shade, size or fuller product name said or legible.
- First appears: 1:43.84 spoken ("Luxe Foundation is specifically developed for mature skin"); category word "Foundation." at 1:39.68. On screen from 1:33 (first frame after the 1:32.40 cut): man holds the beige "Luxe" tube upright at chest height beside the woman. Arguably teased earlier as the hidden item in the covered basket (0:21–0:29), never shown in it.
- Bridge line (verbatim): 1:32.40–1:39.68 "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." → 1:39.68–1:43.84 "Foundation. Most foundations on mature skin look like makeup."
- Saved for last? Yes: item 6 of 6 recommended products (after 3 banned products), starts at 1:32 of 2:19 (sold-product section 1:32–2:19 = ~47 s, about one third of the video).
- Product shots: only hand-held, static, label-to-camera; beige matte squeeze tube, flip cap at bottom, vertical "Luxe" in black, small garbled text above and below. No swatch, no application, no before/after, no Amazon page or price shown. The other five items are real brands named aloud (Clinique All About Eyes, NARS concealer, Too Faced blush) or shown (bronzer lid reads like "MARIO"); none are linked.

### CTA
- Spoken: 1:59.36–2:03.12 "I added the link in the comments for anyone who could not find it." 2:03.12–2:07.44 "Sometimes there is a coupon available for a limited time, so hopefully you can grab it." 2:07.44–2:12.64 "If you are over 60 and give this routine a chance, I think you will never want to use anything else again." 2:12.64–2:19.52 "And if you would like the list of these products and a quick explanation of what each one does, just comment GLOW and I will send it to you in a message."
- On-screen text: 1:59–2:01 "right now I added the link in the comments"; 2:03 "for anyone who could not find it"; ~2:03.3 "sometimes"; 2:05 "there is a coupon available for a limited time"; 2:07 "so hopefully you can grab it if you are over 60"; ~2:17 "just comment glow"; 2:19 "and I will send it to you in a message". No separate CTA graphic, button or keyword card.
- Caption CTA: "COMMENT "glow" and I will send you the exact ROUTINE EXPLAINED with a LIST of the PRODUCTS PLUS all the proven MAKEUP TIPS for MATURE women." + gate "But you have to follow me first and like the video so i can message you."
- Where it points: (1) product link in the comments (spoken; link itself not in metadata, not checked); (2) "comment GLOW" → DM with product list (comment-keyword automation), gated in the caption by follow + like. Amazon named as the proof of popularity ("number one best-selling foundation on Amazon"), implying the link goes to Amazon (reading; not verified). Unlike videos 4 and 5, the caption does NOT say "Link for the foundation is on my profile (bio)".

### AVATAR
- Who: "expert" makeup-artist figure (implied, not stated: no name, title or credential is said; the hashtag "#makeupartist" in the caption carries the implication). Young man, approx. 20s, white, platinum-blond short hair, clear wire-frame glasses, black short-sleeve polo, small clip-on lapel mic (seen 0:33). He holds every product. Peer element supplied by the woman beside him.
- Setting & lighting: inside a large beauty store styled as Sephora (black/white striped columns, "SEPHORA" signage from 1:33, makeup gondolas, vanity mirror with bulbs, shoppers walking behind). Bright overhead store lighting. Framing looks like a handheld/gimbal selfie-height two-shot, slight movement; 11 separate clips (cuts measured at 0:04.7, 0:20.2, 0:29.7, 0:39.5, 0:53.8, 1:04.5, 1:09.4, 1:16.3, 1:22.2, 1:32.4), each a different aisle/position.
- Real or AI-looking (my reading, with evidence):
  - No "syntheticmedia" or other watermark seen (checked top and bottom strips at 0:00, 0:05, 1:53, 2:19 at full 1080x1920, and all 73 sampled frames).
  - Garbled packaging text: Clinique jar reads like "CINQIJE" (0:33); Too Faced lid script is malformed (1:17); gloss logo unreadable (1:23); Luxe tube small print is pseudo-text (1:33–2:19); a store sign reads like "SEPHURA" (1:33).
  - Impossible object: the "primer" tube has a black cap at both ends (0:15–0:19).
  - Continuity: the "after" woman's top changes in every clip (cream satin V-neck → green V-neck → green round-neck → green wrap → green cowl) while she is presented as one person; the hook "before" woman is a different face.
  - Product/script mismatch: pink blush held during bronzer lines (1:04–1:09); at 1:21 the blush becomes a plain pink disc with no lid text.
  - Clip lengths of ~5–14 s per shot match typical AI-video generation lengths (reading).
  - Overall reading: likely AI-generated video (people, store and products) with a single voice-over track; the lapel mic and walking shoppers are realistic touches. Not proven.
- Delivery: fast, upbeat, enthusiastic; wide-eyed expressions, constant hand gestures. Casual/instructional register; slang "Chef's kiss" (1:21.28) and "sexy" (0:04.72). No swearing.
- Who else appears: (1) "before" woman, approx. 65–75, white, auburn bob, heavy makeup (0:00–0:04); (2) "after"/model woman, approx. 55–65, white, honey-blonde bob, natural makeup, cream then sage-green blouses (0:05–2:19), silent, smiling, holds the covered basket (0:21–0:29); (3) background shoppers. No hands-on application to either woman's face.

### CLAIMS & COMPLIANCE
- 0:00–0:04.72 "If you look decades older and like your makeup is working against you, don't worry."
- 0:04.72–0:09.76 "You can absolutely look youthful and sexy after 50, 60, or 70."
- 0:09.76–0:20.16 "Throw away the matte lipstick, throw away the heavy mascara, and stop using primer altogether. Because these products were made for 20-year-olds, not for your mature skin."
- 0:24.48–0:29.68 "The last one may be the one thing standing between you and looking 20 years younger." (result promise, hedged with "may")
- 0:41.44–0:53.60 (NARS concealer) "Most concealers on mature skin compress into every crease and sink into the corner of the eye. This one doesn't. It diffuses light instead of sitting in the crease, so the eye looks lifted and rested…"
- 0:58.48–1:02.08 "A face without bronzer after 50 reads as flat and tired"
- 1:23.44–1:29.52 "A lip gloss on top… makes the lips appear fuller. On mature skin, the lips lose volume."
- 1:32.40–1:39.68 "this is the step that makes you look less tired, brings your face to life"
- 1:43.84–1:46.96 "Luxe Foundation is specifically developed for mature skin." (formulation claim)
- 1:46.96–1:52.08 "It helps blur fine lines, smooth texture, and look natural, not heavy." (performance claim)
- 1:52.08–1:54.40 "It almost never settles into wrinkles" (performance claim, hedged "almost")
- 1:54.40–1:59.36 "it is the number one best-selling foundation on Amazon right now." (on screen 1:55–1:57 "and it is the No. 1 best selling foundation on Amazon") — bestseller ranking claim
- 2:03.12–2:07.44 "Sometimes there is a coupon available for a limited time, so hopefully you can grab it." (scarcity/discount)
- 2:07.44–2:12.64 "If you are over 60 and give this routine a chance, I think you will never want to use anything else again."
- No stats, ingredient lists, prices, "dermatologist" or "same company" claims. No client/testimonial story. Implied credential only via the makeup-artist look, the store setting and "#makeupartist".
- "Ad"/"#ad"/"Sponsored"/"paid partnership" shown? No "AD |" prefix, no "#ad", no "Sponsored"/"paid partnership" label in the caption, title line or on screen. The caption starts with the literal string "adl" (meaning not clear; could be an internal tag or a disguised ad marker; not a standard disclosure). Same in video 7.
- AI disclosure shown? None found: no "syntheticmedia"/"AI-generated" watermark, label or caption text.
- Risk notes (my reading):
  - "number one best-selling foundation on Amazon right now" needs substantiation (category, date, marketplace); a fixed video re-posted twice makes "right now" hard to keep true.
  - "specifically developed for mature skin", "blur fine lines", "almost never settles into wrinkles" need product testing to back them.
  - "looking 20 years younger" is an implied result promise tied to "the last one" (the sold product).
  - Real brands (Clinique, NARS, Too Faced, Makeup by Mario-style packaging, Sephora store branding) are used as the credible frame around an unrelated brand; if the video is AI-generated, this is synthetic depiction of real brands' packaging and a real retailer, with no AI disclosure.
  - Before/after implied with two different women.
  - Undisclosed commercial content (link-in-comments, coupon, comment-for-DM funnel) with no ad label.
  - Caption gate "you have to follow me first and like the video so i can message you" = engagement bait.
  - "sexy" is a mild word for some ad review systems. No profanity.

### WHY IT WORKS
It opens on a fear the 50+ viewer already has ("look decades older… makeup is working against you"), then gives an easy "throw these away" list from an expert-looking artist in a real-looking Sephora, with an unopened basket as the hook to stay.
Five trusted real brands come first, so the unknown Luxe foundation inherits their credibility when it is revealed as "the one step most women miss", then gets a bestseller claim, a coupon and two ways to act (comment link, "comment GLOW").

### OBSERVER NOTES (optional)
- Measured: scene cuts via ffmpeg scene filter (threshold 0.25): 0:04.73, 0:20.17, 0:29.67, 0:39.50, 0:53.80, 1:04.47, 1:09.37, 1:16.30, 1:22.23, 1:32.40. The last clip (1:32–2:19, ~47 s) has no cut at that threshold.
- Measured: script compared with video 2 (sections/2.md). Same skeleton and most lines word for word. Video 6 differences: hook adds "don't worry" and "sexy" ("youthful and sexy" vs "youthful, confident, and beautiful"); "Throw away the matte lipstick" vs "get rid of that matte lipstick"; bronzer brand dropped ("So next, cream bronzer" vs "Next, by Mario Cream Bronzer"); the "That is the difference between color…" line moved from blush to bronzer; "always a brush on mature skin" shortened to "Always a brush"; the man holds all products here (in 2 the woman holds several); basket cloth red satin (gold in 2); gloss logo not legible (e.l.f. in 2). CTA keyword is "GLOW" in both speech and caption here (in 2 caption said "GLOW" but speech said "natural").
- Measured: burned-in captions differ from speech in four places: "Lux Foundation" (brand misspelled), "yeah this is the easiest fix" (extra "yeah"), "Chef's Kiss now finish the lips" (two sentences merged), "right now I added the link in the comments" ("right now" carried over from the Amazon sentence, which makes it read as "right now I added the link").
- Measured: the same file was posted twice by the page (7 on Aug 26, 6 on Aug 30) with one hashtag changed; the re-post earned fewer views. Reading: the page re-posts winning creatives rather than making new ones, and the caption template (comment keyword + follow/like gate) is reused across videos 4–8.
- Reading: the "over 60" line in the CTA ("If you are over 60 and give this routine a chance") narrows the target to 60+ even though the hook says "50, 60, or 70".

---

## Video 7 — Minho Makeup & Beauty — same file as video 6 (re-post)
**Link:** https://www.facebook.com/share/v/1DfiwTsQnp/ (video ID 1084335064173234) · **Page:** Minho Makeup & Beauty · **Uploaded:** 2026-08-26 23:26 UTC · **Duration:** 139.7 s · **Views:** view_count 40,391 (page title line says "70K views · 479 reactions") · **Comments:** not found
**Caption (verbatim):** "adl COMMENT "glow" and I will send you the exact ROUTINE EXPLAINED with a LIST of the PRODUCTS PLUS all the proven MAKEUP TIPS for MATURE women.🤯🥰😘

But you have to follow me first and like the video so i can message you. ❤️

#maturemakeuproutine #makeupartist #makeupforolderwomen #wrinkleshack  #makeup #maturemakeup #womenover60 #womenover50 #womenover40"

**Measured:** `videos/7.mp4` is byte-identical to `videos/6.mp4` (same size and MD5), so the hook, format, body, product, CTA, avatar and claims are exactly as in the **Video 6** section; read that section for the full breakdown. The transcript is saved as `transcripts/7.txt` (a copy of 6's). The caption is different from video 6's caption (shown in full above).
**Performance against the other post:** video 6: view_count 32,422 ("60K views · 367 reactions"), uploaded 2026-08-30 06:22 UTC. Video 7: view_count 40,391 ("70K views · 479 reactions"), uploaded 2026-08-26 23:26 UTC.

---

## Video 8 — Minho Makeup & Beauty — "Never use matte lipstick again (mature-skin routine)"
**Link:** https://www.facebook.com/share/v/19t4sHPWsn/ · **Page:** Minho Makeup & Beauty · **Uploaded:** 2026-08-23 (info.json timestamp 1787473662) · **Duration:** 2:26 (146.1 s) · **Views:** view_count 94,109 (page title line says "149K views · 488 reactions") · **Reactions:** 488 (from title line) · **Comments:** not found (comment_count null in metadata)
**Caption (verbatim):** "adl COMMENT "glow" and I will send you the exact ROUTINE EXPLAINED with a LIST of the PRODUCTS PLUS all the proven MAKEUP TIPS for MATURE women.🤯🥰🤍 But you have to follow me first and like the video so i can message you. ❤️ #maturemakeuproutine #makeupartist #makeupforolderwomen #wrinkleshack #makeup #maturemakeup #womenover60 #womenover50 #womenover40"

Source: transcript `transcripts/8.txt` (faster-whisper), frames `frames/8/` + extra frames pulled from `videos/8.mp4` at 0:05.0–0:06.4, 0:37.5–0:38.5, 1:38–1:39, 2:24–2:26 (pulled 2026-11-07). On-screen burned-in captions run about 0.5–1 s ahead of the audio.

### HOOK (0:00–0:05)
- Spoken: "If you look decades older, completely drained," (0:00–0:03) / "and like your makeup is working against you," (0:03–0:05) / continues "and you wanna look useful [on-screen: "youthful"], confident, and beautiful even at 50, 60, or 70, never use matte lipstick again." (0:05–0:14)
- On-screen text: burned-in captions only (white, centred, lower third), no separate headline: "if you look decades older" (0:00–0:01), "completely drained" (0:02–0:03), "and like your makeup is working against you" (0:04–~0:05.5), then "and you wanna look youthful" (0:06–0:07), "confident and beautiful even at 50" (0:09), "60 or 70 never use matte lipstick again" (0:11–0:13). Small "syntheticmedia" watermark under the caption throughout.
- Visual: tripod-style static vertical shot in a makeup store/studio (Hollywood bulb vanity mirrors, product counters behind). A young platinum-blond man in aviator-style clear glasses and grey polo stands behind a seated older woman, one hand on top of her head, the other cupping her chin/jaw. Woman 0:00–~0:05.5: grey-blonde bob, maroon top, heavy dark smoky eye and bright pink blush (the "bad makeup" look). Hard cut at ~0:05.6 (between frames 0:05.5 and 0:05.6) to a different-looking woman, dark brown shoulder-length hair, green satin blouse, soft natural makeup, same pose (his hand on her head) — an implied before/after. He gestures with a fist on "confident". 0:13 he holds up a lipstick (matte red/berry, silver-and-black bullet — reading: MAC-style, brand not said); 0:15–0:17 a powder blush compact (coral); 0:19–0:25 a liquid foundation/concealer bottle (label small; reading: MAC-style bottle, not said).

### FORMAT
"Never use X, use these instead" mature-skin makeup routine, sponsor product saved for last as the "missing step".
A makeup-artist avatar bans three common products (matte lipstick, powder blush, heavy concealer) as "tested on 20-year-olds", then walks through a 6-step routine with real big-brand products (Clinique, NARS, bronzer, Too Faced, e.l.f.), and slots Luxe foundation in as step 6, framed as the step "most women miss".

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:00–0:05 | Problem hook: "If you look decades older, completely drained, and like your makeup is working against you," | Before woman (grey bob, heavy makeup); captions as above |
| 0:05–0:14 | Desire + ban 1: "and you wanna look useful, confident, and beautiful even at 50, 60, or 70, never use matte lipstick again." | Cut to "after" woman ~0:05.6; matte lipstick held up 0:13 |
| 0:14–0:17 | Ban 2: "Never use powder blush." | Coral powder blush compact, open, held up 0:15–0:17 |
| 0:17–0:25 | Ban 3 + reason: "And never use heavy concealer again, because these were tested on 20-year-olds with perfect skin, never made for your mature skin." | Liquid bottle held 0:19–0:25; caption "because these were tested on 20 year olds" (0:21), "with perfect skin never made for your mature skin" (0:23–0:25) |
| 0:25–0:35 | Promise + open loop: "Let me show you what products to use so you can finally feel confident and complete again. The last one may be the one thing standing between you and looking 20 years younger." | Woman holds a gold-satin-lined wire basket (contents not shown) 0:27–0:35; captions "the last one may be the one thing standing between you" (0:31–0:33), "and looking 20 years younger" (0:35) |
| 0:35–0:45 | Item 1, eye cream: "First, under eye cream with a concealer. I use Clinique All About Eyes. Just a small amount pressed gently under the eye. Let it absorb for a moment before anything goes on top." | Scene change ~0:36: handheld selfie two-shot (him left, her right) in a store aisle; Clinique jar (pink lid, "CLINIQ…" legible) held up 0:37–0:45. Caption "I use Clinique all about eyes just" (0:39) |
| 0:45–1:00 | Item 2, concealer: "Then NARS concealer under the eye. Most concealers on mature skin compress into every crease and sink into the corner of the eye. This one doesn't. It diffuses light instead of sitting in the crease so the eye looks lifted and rested instead of tired and heavy." | Different store (wood panelling, "CHANEL" sign) 0:47–0:59; NARS wand concealer (black cap, "NARS" on tube) held up |
| 1:00–1:18 | Item 3, cream bronzer: "Next, cream bronzer. The older you get, the more your face loses warmth and dimension. A face without bronzer after 50 reads as flat and tired no matter how good the rest of your makeup is. Take a brush, blend it out, and do not use a sponge. Always a brush on mature skin, and suddenly there is life back in the face." | Back to first store; white compact, lid reads "…MARIO" (brand not said; reading: Makeup by Mario) 1:01–1:17 |
| 1:18–1:28 | Item 4, blush: "Then two-faced blush. Press it into the cheek and pull it all the way toward the nose. Chef's kiss. That is the difference between color that sits on the face and color that looks like it belongs there." | Pink round compact with "Too Faced" script logo 1:19–1:27 (transcript spells "two-faced"; packaging shows "Too Faced"). Caption typo "all the may toward the nose" (1:21) |
| 1:28–1:38 | Item 5, lip gloss: "Now finish the lips. A lip gloss on top reflects off the shine and makes the lips appear fuller. On mature skin, the lips lose volume. This is the easiest fix most women never think of," | Pink/nude gloss tube with "e.l.f." logo 1:29–1:37 (brand not said) |
| 1:38–1:47 | Bridge / rehook: "but one step is missing. And this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." | Scene change ~1:39 to a third store (black shelving, sign top-left reads roughly "FENTY BEAUTY" — reading, blurry); Luxe tube now in his hand |
| 1:47–2:04 | Item 6, sponsor: "Foundation. Most foundations on mature skin look like makeup. Luxe foundation is specifically developed for mature skin. It helps blur fine lines, smooth texture, and look natural, not heavy. It almost never settles into wrinkles, and it is the number one best-selling foundation on Amazon right now." | Cream squeeze tube, vertical "Luxe" wordmark, small print illegible, held at chest height 1:39–2:26. Caption spells it "Lux Foundation" (1:51); "and it is the No. 1 best selling foundation on Amazon" (2:03) |
| 2:04–2:11 | CTA 1 + urgency: "I added the link in the comments for anyone who could not find it. Sometimes there is a coupon available for a limited time, so hopefully you can grab it." | Captions "right now I added the link in the comments" (2:05), "there is a coupon available for a limited time" (2:09), "so hopefully you can grab it" (2:11) |
| 2:11–2:17 | Reassurance: "If you are over 60 and give this routine a chance, I think you will never wanna use anything else again." | Captions match |
| 2:17–2:26 | CTA 2 (DM automation): "Thank you for watching all the way to the end. And if you would like the list of these products and a quick explanation of what each one does, just comment, glow, and I will send it to you in a message." | Caption "just comment glow" (~2:24), "and I will send it to you in a message" (2:25–2:26) |

**Rehooks / open loops**
- 0:25–0:30 "Let me show you what products to use so you can finally feel confident and complete again."
- 0:30–0:35 "The last one may be the one thing standing between you and looking 20 years younger." (main open loop, paid off at 1:47)
- 0:52–0:54 "This one doesn't." (mini-reveal inside item 2)
- 1:35–1:38 "This is the easiest fix most women never think of,"
- 1:38–1:46 "but one step is missing. And this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely."
- 2:17–2:19 "Thank you for watching all the way to the end." (rewards completion, sets up the DM CTA)

### PRODUCT
- Product sold: foundation — Luxe (spoken "Luxe foundation"; packaging wordmark "Luxe"; on-screen caption misspells it "Lux Foundation" at 1:51). Exact product/shade name: not said, not legible.
- First appears: 1:47 spoken ("Foundation.", brand name at 1:50 "Luxe foundation"); ~1:39 on screen (scene cuts to a new store, he holds the cream "Luxe" squeeze tube at chest height beside the woman).
- Bridge line (verbatim, with timestamp): "This is the easiest fix most women never think of, but one step is missing. And this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely. Foundation." (1:35–1:47)
- Saved for last? yes — item 6 of 6; pitch starts 1:39 (bridge) / 1:47 (named) of 2:26. Pre-announced at 0:30 as "The last one".
- Product shots: one tube only, held static in his hand for the whole last 47 s, never opened, never applied, no swatch, no texture, no before/after on the woman during the pitch. Every other product is also only held up, never applied. The only before/after is the hook cut at ~0:05.6 (grey-bob woman with heavy makeup → dark-haired woman with soft makeup).

### CTA
- Spoken: "I added the link in the comments for anyone who could not find it." (2:04–2:07); "Sometimes there is a coupon available for a limited time, so hopefully you can grab it." (2:07–2:11); "if you would like the list of these products and a quick explanation of what each one does, just comment, glow, and I will send it to you in a message." (2:19–2:26)
- On-screen text: "right now I added the link in the comments" (2:05), "for anyone who could not find it" (2:07), "there is a coupon available for a limited time" (2:09), "just comment glow" (~2:24), "and I will send it to you in a message" (2:25). No button, sticker or price graphic.
- Where it points: link in comments (spoken, 2:04) + "comment glow" DM automation (spoken and caption). Caption adds a follow-and-like gate: "But you have to follow me first and like the video so i can message you." Amazon named only as a claim ("number one best-selling foundation on Amazon"), not as a search instruction.

### AVATAR
- Who: "expert" — implied makeup artist (hands on the client's head/chin in the hook, store/studio setting, "I use Clinique All About Eyes", hashtag "#makeupartist"); no spoken credential or title. Young man, approx 20s, white, platinum-blond cropped curly hair, clear wire aviator glasses, small earring, charcoal grey polo. Co-star: woman approx 50s (reading), white, dark brown shoulder-length hair, green satin blouse; she never speaks.
- Setting & lighting: three or four different beauty-store/studio backdrops — hook in a studio with bulb vanity mirrors (tripod-style, static, woman seated); 0:36 onward a handheld-selfie-style two-shot in a store aisle with bright retail lighting; 0:47–0:59 a wood-panelled store with a "CHANEL" sign; 1:39 onward a black-shelved store. Even, bright overhead retail light.
- Real or AI-looking (my reading): AI-generated. Evidence: "syntheticmedia" watermark visible in every frame (small white text under the captions, left side, low contrast but readable); the woman's outfit, hair and pose are identical across stores that change between cuts; backgrounds jump store to store mid-routine with no transition; products are never applied; the "after" woman in the hook is visibly a different face/hair from the "before" woman; skin on both is very smooth. Lip-sync looks close but mouth shapes are exaggerated (e.g. grimace at 0:15, 0:01).
- Delivery: fast, energetic, enthusiastic; casual ("wanna", "Chef's kiss" at 1:22); no swearing. Lots of "most women" / "mature skin" framing.
- Who else appears: the silent woman (two different-looking women in the hook: before 0:00–0:05, after from 0:05.6); his hands holding each product; background shoppers in the store shots (0:47–1:17). No other speakers.

### CLAIMS & COMPLIANCE
- 0:00–0:05 "If you look decades older, completely drained, and like your makeup is working against you"
- 0:09–0:14 "never use matte lipstick again." / 0:14 "Never use powder blush." / 0:17 "And never use heavy concealer again"
- 0:19–0:25 "because these were tested on 20-year-olds with perfect skin, never made for your mature skin." (testing claim about competitor product categories, no source)
- 0:30–0:35 "The last one may be the one thing standing between you and looking 20 years younger." (result promise tied to the sponsored product)
- 0:39 "I use Clinique All About Eyes." (implied personal use / artist endorsement)
- 0:47–1:00 NARS concealer: "Most concealers on mature skin compress into every crease… This one doesn't. It diffuses light…" (comparative claim about a named third-party brand)
- 1:05 "A face without bronzer after 50 reads as flat and tired"
- 1:32 "A lip gloss on top reflects off the shine and makes the lips appear fuller."
- 1:47 "Most foundations on mature skin look like makeup."
- 1:50 "Luxe foundation is specifically developed for mature skin."
- 1:53–1:59 "It helps blur fine lines, smooth texture, and look natural, not heavy."
- 1:59 "It almost never settles into wrinkles"
- 2:00–2:04 "it is the number one best-selling foundation on Amazon right now." (ranking claim; on-screen "No. 1 best selling foundation on Amazon")
- 2:07–2:11 "Sometimes there is a coupon available for a limited time, so hopefully you can grab it." (scarcity/discount)
- 2:11–2:17 "If you are over 60 and give this routine a chance, I think you will never wanna use anything else again."
- No prices said or shown. No ingredient claims, no stats/percentages, no "client" story, no dermatologist claim.
- "Ad"/"#ad"/"Sponsored"/"paid partnership" shown? Not on screen, not spoken, no "AD |" prefix in the page title line. The caption begins "adl COMMENT…" — "adl" is the first word as scraped; it is not a clear "#ad" or "Ad" label (could be a truncated/mistyped "ad", reading only). No paid-partnership label found in the metadata.
- AI disclosure shown? Yes, the "syntheticmedia" watermark, small low-contrast white text at left under the captions in every frame from 0:00 to 2:26. Not mentioned in caption or speech.
- Risk notes (my reading): (1) "number one best-selling foundation on Amazon right now" needs substantiation. (2) "looking 20 years younger" is an anti-ageing result promise. (3) "tested on 20-year-olds with perfect skin" is an unsupported claim against whole product categories. (4) It uses real third-party brands (Clinique, NARS, Too Faced, e.l.f., a "MARIO" compact) in an AI-generated "I use" endorsement, which makes Luxe look like part of an artist's real kit. (5) A "limited time" coupon is mentioned with no terms. (6) The AI "after" face in the hook is a different person, not a real result. (7) No clear ad disclosure; the follow-and-like gate in the caption is engagement bait.

### WHY IT WORKS
Fear-then-ban hook ("decades older… never use matte lipstick again") plus a visible before/after cut gets the 50+ viewer to stop within 5 s, and "the last one" open loop holds her through 5 credible big-brand steps.
The sponsor arrives as the "missing step most women miss", borrowing trust from Clinique/NARS/Too Faced, then closes with a double CTA (link in comments + "comment glow" DM) that also grows comments and followers.

### OBSERVER NOTES (optional)
- Measured: the transcript says "you wanna look useful" (0:05), but the on-screen caption reads "youthful" (0:06); the caption is likely right.
- Measured: brand spellings differ: transcript "two-faced" vs packaging "Too Faced"; caption "Lux Foundation" vs packaging "Luxe". Caption typo "all the may toward the nose" (1:21).
- Measured: title line says 149K views while yt-dlp view_count is 94,109. These are different counters; both are reported as found.
- Reading: the three "never use" props in the hook (matte lipstick, powder blush, liquid bottle) look like MAC-style packaging, but no brand is said or legible. The "heavy concealer" prop is a foundation-style bottle, not a concealer.
- Reading: the gold-satin basket the woman holds (0:27–0:35) works as a "bag of products" reveal device but is never opened.
- Measured: page note says videos 2–8 on this page are similar; this is the highest-view one in the set. Only video 8 is analysed here.

---

## Video 9 — Jiho Beauty — "Cheap shit from Dollar Tree that's better than luxury"
**Link:** https://www.facebook.com/share/v/1AcZwn4zG7/ · **Page:** Jiho Beauty · **Uploaded:** 2026-10-23 (16:46 UTC, from info.json timestamp 1792773972) · **Duration:** 2:01 (120.65 s) · **Views:** view_count 86,728 (page title line says "181K views") · **Reactions:** 3.2K (from title line "181K views · 3.2K reactions") · **Comments:** not found (comment_count = None in metadata)
(Source: videos/9.info.json and videos/METADATA.md, yt-dlp pull dated 2026-11-07.)

**Caption (verbatim):** "AD | Over 50? These cheap Dollar Tree finds are just as good, if not better, than the luxury stuff

Comment "LINK" for all my picks

#usa #dollartreefinds #skincare #matureskin #maturewoman"

### HOOK (0:00–0:05)
- Spoken: "Cheap shit from Dollar Tree that's just as good," (0:00–0:02) "if not better, than the luxury stuff." (0:02–0:04) "And if you're over 50, you're gonna wanna save this list." (0:04–0:06) "Let's go." (0:06–0:07)
- On-screen text:
  - Headline (pink outlined caps, from 0:01, stays through 0:05; not on the 0:00 frame): "CHEAP SHIT FROM 🌳 DOLLAR TREE THAT'S BETTER THAN LUXURY" (tree emoji after "FROM"; small mirror and camera emoji decorations)
  - Sub-headline (pink script, from 0:01; partly cut off at 0:01, full by 0:02): "A must-have for women over 50+"
  - Burned-in word captions (white caps, current word boxed): "CHEAP SHIT FROM DOLLAR TREE" (0:00–0:01), "THAT'S JUST AS GOOD" (0:02), "IF NOT BETTER THAN" (0:03), "THE LUXURY STUFF" (0:04), "AND IF YOU'RE OVER 50" (0:05)
  - "syntheticmedia" small white watermark, left-centre, on every frame from 0:00
- Visual: handheld selfie, chest-up, man in round wire glasses and white button-down shirt with a clip-on lav mic, standing on the sidewalk outside a Dollar Tree storefront (green "DOLLAR TREE" sign top-left, parking lot with cars right), overcast daylight. Points at camera with a finger at 0:00 and 0:05. Swear word ("shit") is the first spoken word and in the headline.

### FORMAT
"Dollar Tree dupes for luxury skincare, luxury-brand pick saved for last."
Six "luxury product $X vs Dollar Tree product $1.25 that shares N ingredients" comparisons shot hand-held in the aisle, then a pivot ("I saved the best dupe for last") to a $260 Korean luxury eye cream whose one key ingredient (adenosine) is the bridge into LUXE's Korean under-eye balm, which is not a Dollar Tree product and is sold on Amazon.

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:00–0:07 | Hook (see above), "Let's go." | Outside Dollar Tree, selfie; headline + sub-headline |
| 0:07–0:20 | 1. "Drunk Elephant Lala Retro is gorgeous, but it's $68." "Dermacil Whipped Recovery Cream shares 11 ingredients with it. Same Marula oil, same Baobab oil, same size jar. And the Dermacil one adds Metrixyl peptides, $1.25." | Inside Dollar Tree aisle. Inset top-left: purple Drunk Elephant-style "Lala Retro Whipped Cream" jar on lavender background, with sparkly pink "68$" tag from 0:11. Hand holds white jar with lavender lid, label "Dermasil / Whipped Recovery Cream", with smaller lines reading "Marule Oil | Rauhsb | Metricyl® 5000" and a band reading "Deroloped with Dermatologics" (all garbled; fact-check correction). Shelf tag "$1.25" visible. Captions spell it "DERMASIL WHIPPED RECOVERY CREAM" (0:11), "SHARES 11 INGREDIENTS WITH IT" (0:13), "BAOBAB OIL" (0:15) |
| 0:20–0:29 | 2. "Medicate Liquid Peptides is a $68 serum. Skin Nutrition Multi-Peptide Serum shares 10 ingredients with it. Same Metrixyl peptides, same hyaluronic acid, $1.25." | Inset: Medik8 box + white dropper bottle (packshot reads "Mediks"/"Medik8"), "68$" tag from 0:23. Hand holds dark-blue dropper bottle "Skin Nutrition Botanicals / Multi-Peptide Anti-aging Serum". Captions: "MEDIC 8 LIQUID PEPTIDES" (0:21), "SKIN NUTRITION MULTI PEPTIDE" (0:23), "SERUM SHARES 10 INGREDIENTS" (0:25), "SAME MATRICIAL PEPTIDES SAME" (0:27), "$1 25 CLINIQUE SMART" (0:29). Machine transcript "Medicate" = Medik8 (on-screen packshot + caption) |
| 0:29–0:44 | 3. "Clinique Smart Clinical Repair Cream is $78. Global Beauty Care Smooth and Lift Collagen Cream is the same size and shares 10 ingredients with it. That includes the same peptide, Acetyl hexapeptide 8, plus collagen and hyaluronic acid, $1.25." | Inset: purple Clinique "smart clinical repair" jar, "78$" tag from 0:33. Hand holds light-blue jar "SMOOTH & LIFT COLLAGEN SKIN CREAM / With Peptides, Hyaluronic Acid & Squalane / GlobalBeautyCare / 1.7 fl. oz. (50mL)", pushed close to lens at 0:33 and 0:41. Captions: "GLOBAL BEAUTY CARE SMOOTH" (0:33), "AND SHARES 10 INGREDIENTS" (0:37), "THAT INCLUDES THE SAME PEPTIDE" (0:39), "ACETYL HEXAPEPTIDE EIGHT PLUS" (0:41) |
| 0:44–0:54 | 4. "If you love Drunk Elephant B-Hydra, it's $56. Dermacil Face Serum Oil shares seven ingredients with it. Same niacinamide, same Marula oil, plus ceramides, $1.25." | Inset: pale blue tube on aqua background with water droplets, "56$" tag from 0:47. Hand holds clear bottle with pink dropper "Dermasil / Face Serum Oil" (smaller label lines garbled). Captions: "IF YOU LOVE DRUNK" (0:45), "IT'S $56 DERMASIL FACE" (0:47), "SERUM OIL SHARES SEVEN" (0:49), "SAME NIACINAMIDE" (0:51), "CERAMIDES $1 25 SKIN" (0:53) |
| 0:54–1:03 | 5. "SkinCeutical C Plus AHA is $145. Global Beauty Care Vitamin C Facial Serum shares seven ingredients with it. Same vitamin C, same glycolic acid, $1.25." | Inset: amber SkinCeuticals-style dropper bottle on white, "145$" tag from 0:57. Hand holds silver/orange bottle "VITAMIN C / FACIAL SERUM / 1.7 OZ (50 ml)"; brand logo on the bottle is not legible (letters garbled). Captions: "SHARES SEVEN INGREDIENTS WITH IT" (0:59), "SAME VITAMIN C" (1:01) |
| 1:03–1:14 | 6. "Kate Somerville's Moisturizer is $119. Global Beauty Care Power Moisturizer shares 14 ingredients with it. Same retinol, same vitamin C, same hyaluronic acid, $1.25." | Inset: Kate Somerville white/gold jar on orange slices; price tag animates in ("1" at 1:05, "119$" from 1:07). Hand holds black jar "POWER MOISTURIZER / WITH RETINOL, ANTIONCANTS & GLICHON" (sic), brand line reads "GilebarBeautrCare" at 1:07 and "GlobalBeautyCare" at 1:09. Captions: "GLOBAL BEAUTY CARE POWER" (1:07), "MOISTURIZER SHARES 1 4 INGREDIENTS" (1:09), "SAME RETINOL SAME VITAMIN" (1:11), "C SAME HYALURONIC ACID" (1:13) |
| 1:14–1:30 | Pivot: "Hey, but I saved the best dupe for last. Amora Pacific is a Korean luxury brand. Their Time Response Eye Reserve Cream is lovely, but it's $260 for half an ounce. One of its key ingredients is adenosine. Adenosine is a molecule your body naturally makes and in skincare, it helps smooth wrinkles." | Back to selfie, walking the Dollar Tree aisle pushing a green shopping cart. Inset from 1:17: gold "AMORE PACIFIC / TIME RESPONSE" eye cream jar on white; "260$" tag from 1:23. Captions: "BUT I SAVED THE" (1:15), "AMARA PACIFIC IS A" (1:17), "KOREAN LUXURY BRAND" (1:19), "RESERVE CREAM IS LOVELY" (1:21), "BUT IT'S $260 FOR" (1:23), "INGREDIENTS IS ADENOSINE" (1:25), "ADENOSINE IS A MOLECULE" (1:27), "AND IN SKINCARE IT" (1:29). Spoken "Amora Pacific" / caption "AMARA" = Amorepacific per packshot "AMORE PACIFIC" |
| 1:30–1:45 | 7. LUXE: "Luxe makes a Korean under eye balm with that same adenosine, plus hyaluronic acid to plump, argan oil to soften, and PDRN and collagen extract for firmer looking skin. It reduces the look of wrinkles by 30% in four weeks and it's a fraction of the price." | Hand holds light-blue twist-up stick "Luxe Korean under-eye balm / Luxe / PDRN extract" in front of a "SKINCARE" shelf (Dollar Tree-style green chevron shelf strips), pushed close to lens at 1:33, 1:35, 1:43, 1:45. No luxury inset, no price tag. Captions: "LUX MAKES A KOREAN" (1:31), "THAT SAME ADENOSINE" (1:33), "PLUS HYALURONIC ACID TO PLUMP" (1:35), "ARGAN OIL TO SOFTEN" (1:37), "EXTRACT FOR FIRMER LOOKING SKIN" (1:39), "IT REDUCES THE LOOK" (1:41), "IN FOUR WEEKS" (1:43) |
| 1:45–2:01 | CTA (see CTA section) | 1:47–1:53 in a parked car, seatbelt on, Dollar Tree visible through the windshield, holding the Luxe stick up beside his face. 1:55–1:59 back outside the Dollar Tree storefront (same setting as the hook). Final ~1 s black |

Rehooks / open loops:
- "And if you're over 50, you're gonna wanna save this list." (0:04–0:06)
- "Let's go." (0:06–0:07)
- "If you love Drunk Elephant B-Hydra, it's $56." (0:44–0:47): direct-address re-grab mid-list
- "Hey, but I saved the best dupe for last." (1:14–1:16): main rehook into the pitch
- Visual rehook (reading): each item opens with a luxury packshot inset and a pink sparkly price tag ("68$", "78$", "56$", "145$", "119$", "260$"), so each beat restarts the "how much cheaper?" question.

### PRODUCT
- Product sold: eye balm. LUXE (spoken "Luxe"; caption "LUX"; packaging "Luxe") "Korean under eye balm" (spoken 1:30.88–1:32.80); packaging reads "Luxe Korean under-eye balm" and "PDRN extract".
- First appears: 1:31 spoken ("Luxe makes a Korean under eye balm", 1:30.88); 1:31 on screen (first frame showing it: hand-held light-blue stick in front of a "SKINCARE" shelf; the 1:29 frame is still the talking-head selfie with the Amore Pacific inset).
- Bridge line (verbatim): "Hey, but I saved the best dupe for last." (1:14.64–1:16.72) ... "One of its key ingredients is adenosine. Adenosine is a molecule your body naturally makes and in skincare, it helps smooth wrinkles." (1:23.84–1:30.88) "Luxe makes a Korean under eye balm with that same adenosine, ..." (1:30.88–1:35.40)
- Saved for last? Yes. Item 7 of 7 (the Amore Pacific/LUXE pair). Pivot starts at 1:14, LUXE named at 1:31 of 2:01; it is the only non-Dollar-Tree "dupe" and the only one with no price stated ("a fraction of the price").
- Product shots: single light-blue cylindrical stick (cap on), vertical "Luxe" wordmark, small "Luxe Korean under-eye balm" and "PDRN extract" text; held one-handed in a store aisle, alternating normal distance and pushed close to lens (1:31–1:46); then held up beside the face in a car (1:47–1:53). Not opened, not applied: no demo, no swatch, no before/after. Shot in front of shelves that look like Dollar Tree's (same green chevron shelf strips) though no Luxe shelf tag or price is shown (reading: framing implies it sits in the same store).

### CTA
- Spoken: "If you wanna give it a try, I don't think you'll regret it." (1:44.88–1:46.80) "It's way cheaper on Amazon than anywhere else." (1:46.80–1:48.96) "Search Luxe or click the link in my bio" (1:48.96–1:51.44) "and if you're watching on Facebook, the link will be in the comments." (1:51.44–1:54.04) "Comment link below and I'll send you the links to everything I just mentioned." (1:54.04–1:57.84) "Just make sure you're following me first so I can message you." (1:57.84–2:00.56)
- On-screen text: burned-in captions only, no separate CTA graphic: "IF YOU WANNA GIVE" (1:45), "IT'S WAY CHEAPER ON" (1:47), "THE LINK IN MY BIO" (1:51), "THE LINK WILL BE" (1:53), "AND I'LL SEND YOU" (1:55), "FOLLOWING ME FIRST SO" (1:59). Caption text: "Comment "LINK" for all my picks".
- Where it points: Amazon search "Luxe"; "link in my bio"; on Facebook "the link will be in the comments"; "Comment link" DM automation for all products; follow-first gate ("make sure you're following me first so I can message you").

### AVATAR
- Who: peer/shopper "found these" voice, no stated credentials (no "dermatologist", "esthetician" etc. said). Implied expertise from naming ingredients and counting shared ingredients ("Acetyl hexapeptide 8", "Metrixyl peptides"). The jar band reads, garbled, "Deroloped with Dermatologics": an implied dermatologist cue on the product, not a claim about him, and further garbled-text evidence. Man, apparent East Asian, approx. 45–55 (reading), dark side-parted hair, round thin gold wire-frame glasses, white button-down shirt open at the collar, black clip-on lav mic.
- Setting & lighting: three settings: (1) outside a Dollar Tree store, overcast daylight, handheld selfie (0:00–0:07, 1:55–2:00); (2) inside Dollar Tree, POV hand-held product shots (0:07–1:14, 1:31–1:46) and walking selfie with shopping cart (1:15–1:30), overhead fluorescent lighting; (3) parked car, daylight through windshield, selfie (1:47–1:53).
- Real or AI-looking (reading): "syntheticmedia" watermark (small white lowercase text, left-centre, roughly at the height of the captions) appears on every frame from 0:00 to 1:59, including the in-store POV shots. Product label text is garbled in places, consistent with AI-generated imagery: "GilebarBeautrCare" at 1:07 vs "GlobalBeautyCare" at 1:09 on the same jar; "ANTIONCANTS & GLICHON" on the Power Moisturizer; illegible brand letters on the Vitamin C bottle; a garbled middle ingredient on the Dermasil jar. Face is smooth and evenly lit; lip-sync looked aligned on the stills (cannot judge motion from stills). The hands in the POV shots look natural. Same outdoor shot used at start and end.
- Delivery: upbeat, quick, conversational, list cadence ("Same ..., same ..., $1.25" repeated). Swearing: "Cheap shit" (0:00). Casual: "Let's go.", "gonna wanna", "Hey, but I saved the best dupe for last."
- Who else appears: only his hand(s) in the POV product shots. No models, no other faces, no before/after faces.

### CLAIMS & COMPLIANCE
- "Cheap shit from Dollar Tree that's just as good, if not better, than the luxury stuff." (0:00–0:04); headline "...THAT'S BETTER THAN LUXURY" (0:01–0:05)
- "Drunk Elephant Lala Retro is gorgeous, but it's $68." (0:07); "Dermacil Whipped Recovery Cream shares 11 ingredients with it. Same Marula oil, same Baobab oil, same size jar." (0:10–0:16); "the Dermacil one adds Metrixyl peptides, $1.25." (0:16–0:20)
- "Medicate [Medik8] Liquid Peptides is a $68 serum." (0:20); "Skin Nutrition Multi-Peptide Serum shares 10 ingredients with it. Same Metrixyl peptides, same hyaluronic acid, $1.25." (0:22–0:29)
- "Clinique Smart Clinical Repair Cream is $78." (0:29); "Global Beauty Care Smooth and Lift Collagen Cream is the same size and shares 10 ingredients with it. That includes the same peptide, Acetyl hexapeptide 8, plus collagen and hyaluronic acid, $1.25." (0:32–0:44)
- "If you love Drunk Elephant B-Hydra, it's $56." (0:44); "Dermacil Face Serum Oil shares seven ingredients with it. Same niacinamide, same Marula oil, plus ceramides, $1.25." (0:47–0:54)
- "SkinCeutical C Plus AHA is $145." (0:54); "Global Beauty Care Vitamin C Facial Serum shares seven ingredients with it. Same vitamin C, same glycolic acid, $1.25." (0:57–1:03)
- "Kate Somerville's Moisturizer is $119." (1:03); "Global Beauty Care Power Moisturizer shares 14 ingredients with it. Same retinol, same vitamin C, same hyaluronic acid, $1.25." (1:06–1:14)
- "Amora Pacific [Amorepacific] is a Korean luxury brand. Their Time Response Eye Reserve Cream is lovely, but it's $260 for half an ounce." (1:16–1:23)
- "Adenosine is a molecule your body naturally makes and in skincare, it helps smooth wrinkles." (1:25–1:30)
- LUXE balm "with that same adenosine, plus hyaluronic acid to plump, argan oil to soften, and PDRN and collagen extract for firmer looking skin." (1:32–1:40)
- "It reduces the look of wrinkles by 30% in four weeks" (1:40–1:43): result stat, no source given on screen or spoken
- "and it's a fraction of the price." (1:43–1:44): no LUXE price stated
- "I don't think you'll regret it." (1:45–1:46)
- "It's way cheaper on Amazon than anywhere else." (1:46–1:48)
- "Ad" disclosure: caption begins "AD |" and the page title line also contains "AD |" ("181K views · 3.2K reactions | AD | Over 50? ..."). Nothing saying "Ad", "#ad", "Sponsored" or "paid partnership" is visible on screen in any frame.
- AI disclosure: "syntheticmedia" watermark on every frame (small, white, lower-left/centre-left; legible but easy to miss). No spoken or caption AI disclosure.
- Risk notes (reading):
  - "30% in four weeks" needs a study behind it; no source is shown.
  - Seven named-brand price comparisons (Drunk Elephant, Medik8, Clinique, SkinCeuticals, Kate Somerville, Amorepacific) plus "just as good, if not better" are comparative claims against real brands; ingredient-count overlaps (11, 10, 10, 7, 7, 14) would need checking against INCI lists.
  - The LUXE "dupe" is linked to Amorepacific only by one shared ingredient (adenosine), yet framed as "the best dupe".
  - The LUXE balm is shot in a Dollar Tree aisle inside a "Dollar Tree finds" video but is sold via Amazon; a viewer could read it as a Dollar Tree product.
  - "Cheap shit" profanity in the first word and in the headline (possible ad-review / brand-safety issue).
  - Price "way cheaper on Amazon than anywhere else" is an unsubstantiated price-superiority claim.
  - If the presenter is AI-generated (watermark), a presenter shown "shopping" in a real store and "holding" products could be read as a fake demonstration.

### WHY IT WORKS
Six fast "$68 vs $1.25, shares 11 ingredients" proofs build trust and a money-saving payoff for over-50 viewers before any selling starts.
"I saved the best dupe for last" plus the $260 Korean luxury anchor makes LUXE's balm feel like the list's prize rather than an ad.

### OBSERVER NOTES (optional)
- Measured: view_count 86,728 vs title line "181K views" (about 2.1x), consistent with the METADATA.md note that the title figure runs roughly 2x.
- Measured: brand spellings differ between transcript, captions and packaging: "Dermacil" (transcript) / "DERMASIL" (caption) / "Dermasil" (jar); "Medicate" / "MEDIC 8" / "Medik8"; "Amora Pacific" / "AMARA PACIFIC" / "AMORE PACIFIC"; "Luxe" / "LUX" / "Luxe".
- Measured: luxury price tags use the "68$" style (number then dollar sign) in pink sparkly lettering; Dollar Tree "$1.25" is spoken and on shelf tags but never added as an overlay graphic.
- Reading: structurally the same script template as video 15 described in the brief (cheap-store finds vs luxury, ending on LUXE's Korean under-eye balm, "syntheticmedia" watermark), swapped from Target to Dollar Tree.
- Reading: the 1:15–1:30 walking-with-cart selfie gives the pivot a different look from the hand-only product beats, marking the shift to the pitch.

---

## Video 10 — Jiho Beauty — "Cheap shit from Walmart that's better than luxury"
**Link:** https://www.facebook.com/share/v/1PseTywRdi/ (video ID 1818694942613295) · **Page:** Jiho Beauty · **Uploaded:** 2026-10-22 (20:55:12 UTC, from info.json `timestamp`) · **Duration:** 2:08 (128.8 s) · **Views:** view_count 72,893 (page title line says "148K views") · **Reactions:** "821 reactions" (from title line) · **Comments:** not found (comment_count not in metadata)
**Caption (verbatim):** "AD | Over 50? These cheap Walmart finds are just as good, if not better, than the luxury stuff

Comment "DM" for all my picks

#usa #walmartfinds #skincare #matureskin #maturewoman"

**File check (measured).** 10.mp4 is its own file: 21,885,482 bytes, MD5 756f037d32b66431395eb4c0aea4f2a3. Video 11 has the same caption and the same 128.8 s length, but it is a different file (21,400,260 bytes, MD5 8d15a977…), posted a day earlier (2026-10-21; view_count 61,754; title line "124K views · 1.3K reactions"). Video 11 is not covered here. This is the Walmart version of the Target ad in video 15: same presenter, same script skeleton, same CTA block, different store and different swaps. Metadata was pulled 2026-11-07 (videos/METADATA.md).

### HOOK (0:00–0:05)
- **Spoken:** "Cheap shit from Walmart that's just as good, if not better, than the luxury stuff." (0:00–0:03.5) / "And if you're over 50, you're gonna want to save this list. Let's go!" (0:03.5–0:06.2)
- **On-screen text:**
  - Headline, 0:01–0:05 (not in the 0:00 frame; gone by 0:07, when the shot cuts to the product). Pink rounded caps on light-pink highlighter strips, with small star doodles and a curly pink arrow, upper half of the frame: "CHEAP SHIT FROM WALMART THAT'S BETTER THAN LUXURY".
  - Sub-headline, same style and timing, sentence case: "(A must-have for women over 50+)".
  - Burned-in captions: white condensed caps with a dark outline, one word at a time on a black box:
    - none at 0:00
    - "CHEAP SHIT FROM WALMART" (0:01)
    - "IF NOT BETTER THAN" (0:02)
    - "THE LUXURY STUFF" (0:03)
    - "AND IF YOU'RE OVER 50" (0:04)
    - "YOU'RE GONNA WANNA SAVE" (0:05)
  - The headline says "BETTER THAN LUXURY". The spoken line is softer: "just as good, if not better".
- **Visual:**
  - The avatar stands outside a Walmart store in daylight. The blue facade and the "Walmart" logo with its yellow spark are top left; the entrance doors, cart corrals, blue bollards and parked cars are behind him.
  - Handheld selfie at arm's length, chest-up, slight upward angle. He wears a white button-down and a black DJI-style lav mic clipped to the placket.
  - He talks straight to camera, gestures with his free hand and points at the lens at 0:05 ("save").
  - At 0:07 there is a hard cut to the first product in his hand inside the store.

### FORMAT
**A Walmart "cheap swaps for luxury" list, with the sponsored product slotted in as "the best for last."**
Six real drugstore swaps from Walmart shelves (Aquaphor, CeraVe, L'Oréal ×2, La Roche-Posay, RoC), each set against a named luxury product with a price tag graphic. Item 7 is LUXE's Korean under-eye balm, set against La Prairie and bridged by a shared ingredient (PDRN).

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:06–0:17 | **Swap 1:** "Instead of La Mer's lip balm at $85, grab Aquaphor Lip Repair. The second ingredient in La Mer is the first ingredient in Aquaphor. They share six ingredients. La Mer is gorgeous, but Aquaphor is about five bucks." | First-person hand (white shirt cuff) holds a white Eucerin "Aquaphor SOS LIP REPAIR" tube (pack: "DRY, CRACKED LIPS · MEDICAL SKINCARE") in front of an Aquaphor/Eucerin shelf with Walmart "Rollback" tags. Top left: a thumbnail of the La Mer lip balm tin; the pink bubbly "85$" tag appears by 0:09 with pink heart sparkles. Captions: "INSTEAD OF LA MER'S" (0:07), "GRAB AQUAPHOR LIP REPAIR" (0:09), "THE SECOND INGREDIENT IN" (0:11), "THEY SHARE SIX INGREDIENTS" (0:13), "LAMAIR IS GORGEOUS BUT" (0:15, misspelt), "AQUAPHOR IS ABOUT 5 BUCKS" (0:17). No price tag graphic for Aquaphor. |
| 0:17–0:29 | **Swap 2:** "If you love EltaMD UV Clear, try CeraVe AM Facial Moisturizing Lotion. Same zinc oxide, same octinoxate, same niacinamide. It's SPF 30 instead of 46, but it's under $15 for almost twice the size." | Hand holds the CeraVe AM Facial Moisturizing Lotion pump bottle in front of a full CeraVe bay. Top left: an EltaMD UV Clear bottle thumbnail ("elta MD UV Clear", "46"). **No price tag on the EltaMD thumbnail** in any frame, 0:19–0:29. Captions: "U V CLEAR TRY" (0:19), "CERAVE AM FACIAL MOISTURIZING LOTION" (0:21), "SAME ZINC OXIDE SAME OCTINOXATE" (0:23), "IT'S SPF 30 INSTEAD" (0:25). No caption in the 0:27 and 0:29 frames. |
| 0:29–0:41 | **Swap 3:** "Lancôme Absolu Rich Cream is $280. L'Oréal Age Perfect Rosy Tone shares 24 ingredients with it. Same squalane, same LHA. Fun fact, L'Oréal owns both. Rosy Tone is about 18 bucks." | Hand holds a pink L'Oréal "AGE PERFECT" jar with a gold lid ("…FRAGRANCE-FREE / SANS PARFUM") in front of the L'Oréal shelf, where the shelf tags read "$17.97". Top left: a gold Lancôme "ABSOLUE" jar thumbnail, with "280$" from 0:33. Captions: "LANCOME ABSOLUTE RICH CREAM" (0:31), "L'OREAL AGE PERFECT ROSY" (0:33), "TONE SHARES 24 INGREDIENTS" (0:35), "SAME SQUALANE SAME LHA" (0:37), "L'OREAL OWNS BOTH" (0:39), "18 BUCKS" (0:41). |
| 0:41–0:55 | **Swap 4:** "Augustinus Bader's Rich Cream is beautiful, but it's $195 for one ounce. La Roche-Posay Cicoplas[t] Balm B5 has the same panthenol, the same shea butter, and the same vitamin E. And both are fragrance-free. Under $14," | Hand holds a white La Roche-Posay "CICAPLAST BAUME B5+" tube in the LRP aisle, where the shelf tags read "$13.97". Top left: a navy Augustinus Bader bottle thumbnail, with "195$" from 0:47 (no tag at 0:43 and 0:45). Captions: "AUGUSTINUS BADER'S RICH CREAM" (0:43), "LA ROCHE POSAY CICAPLAST" (0:49), "SAME PANTHENOL" (0:51), "AND THE SAME VITAMIN E" (0:53), "UNDER $14" (0:55). No caption in the 0:45 and 0:47 frames. |
| 0:55–1:11 | **Swap 5:** "instead of Strivectin's Advanced Retinol Nightly Renewal at $119, try Rock [RoC] Retinol Correction Deep Wrinkle Night Cream. 20 of the same ingredients, including retinol, shea butter, and vitamin E. Strivectin adds retinol, which Rock doesn't have, but Rock is about $22." | Hand holds a gold RoC "RETINOL CORREXION DEEP WRINKLE NIGHT CREAM" tube in the RoC aisle, where the shelf tags read "$21.97". Top left: a pink-purple StriVectin "NIA-114 Advanced Retinol Nightly Renewal Moisturizer" tube thumbnail. Its tag shows "11" at 0:59 (mid-animation) and "119$" from 1:01. Captions: "INSTEAD OF STRIVECTIN 'S ADVANCED" (0:57), "RETINOL NIGHTLY RENEWAL AT $119" (0:59), "TRY ROCK RETINOL CORRECTION" (1:01), "20 OF THE SAME" (1:03), "INGREDIENTS INCLUDING RETINOL" (1:05), "STRIVECTIN ADDS RETINOL WHICH" (1:07). No caption at 1:09 and 1:11. |
| 1:11–1:27 | **Swap 6:** "Kiehl's Super Multicorrective Cream is lovely, but it's $76. L'Oréal owns Kiehl's, and their Revitalift Triple Power Fragrance Free shares 19 ingredients with it. Same hyaluronic acid, same adenosine, same LHA. Plus, Pro Retinol and Vitamin C. About 24 bucks?" | Hand holds a dark-red L'Oréal "REVITALIFT TRIPLE POWER, FRAGRANCE FREE MOISTURIZER [PRO-RETINOL + HYALURONIC ACID + VITAMIN C]" jar in front of the Revitalift shelf, where the shelf tags read "$23.97". Top left: a purple Kiehl's "SUPER MULTI-CORRECTIVE SOFT CREAM" jar thumbnail, with "76$" from 1:15 (no tag at 1:13). Captions: "CREAM IS LOVELY BUT" (1:13), "IT'S $76" (1:15), "SHARES 19 INGREDIENTS WITH IT" (1:19), "SAME HYALURONIC ACID SAME ADENOSINE" (1:21), "SAME LHA PLUS PRO" (1:23). No caption at 1:17, 1:25 and 1:27. |
| 1:27–1:29 | **Rehook:** "Okay, but I saved the best for last." | Cut to the avatar's selfie inside Walmart: he pushes a blue Walmart cart, with a "beauty" aisle sign and shelves behind him, under fluorescent lights. Caption: "BEST FOR LAST" (1:29). |
| 1:29–1:40 | **Luxury setup for item 7:** "La Prairie's Skin Caviar Eye Lift is $575. La Prairie says it uses PDRN. PDRN is made from fragments of DNA, and it's a big trend in Korean skincare." | Same in-store selfie. Top left: a La Prairie Skin Caviar Eye Lift bottle thumbnail (blue and gold), with "575$" from 1:33 (no tag at 1:31). Captions: "EYE LIFT IS $575" (1:31), "LA PRAIRIE SAYS IT USES PDRN" (1:35), "PDRN IS MADE FROM" (1:37), "TREND IN KOREAN SKINCARE" (1:39). No caption at 1:33. |
| 1:40–1:53 | **Item 7, the sponsored product:** "Lux[e] makes a Korean under-eye balm with PDRN, plus adenosine to smooth wrinkles, hyaluronic acid to plump, argan oil to soften, and collagen extract for elasticity." | First-person hand holds a pale-blue LUXE stick tube. The print is legible: "Luxe Korean under-eye balm", "Luxe" running vertically, and "PDRN extract". Behind it is an ordinary Walmart shelf of mixed products (pumps, boxes) with "Rollback" tags. It is **not** a LUXE-only display. Captions: "LUX MAKES A KOREAN" (1:41), "HYALURONIC ACID TO PLUMP" (1:45), "AND COLLAGEN EXTRACT FOR ELASTICITY" (1:47). No caption at 1:43. |
| 1:48–1:56 | **Result claim:** "It reduces the look of wrinkles by 30% in four weeks, and it's made for mature skin." / "If you want to give it a try, I don't think you'll regret it." | Same hand-held LUXE tube shot. Captions: "IT REDUCES THE LOOK" (1:49), "OF WRINKLES BY 30%" (1:51), "AND IT'S MADE FOR" (1:53), "I DON'T THINK YOU'LL" (1:55). **No before/after, no application demo and no other face** in any sampled frame. |
| 1:56–2:08 | **CTA** (see the CTA section) | 1:57–2:01: a car selfie (driver's seat, seatbelt on) with the Walmart storefront visible through the side window; he holds the LUXE tube up beside his face. 2:03–2:07: back outside the Walmart entrance, the same setting and framing as the opening. Captions: "AMAZON THAN ANYWHERE ELSE" (1:57), "SEARCH LUX OR CLICK" (1:59), "ON FACEBOOK" (2:01), "COMMENT DM BELOW" (2:03), "THE LINKS TO EVERYTHING" (2:05), "FOLLOWING ME FIRST SO" (2:07). |

**Rehooks and open loops**
- 0:03.5: "And if you're over 50, you're gonna want to save this list." (an instruction to save, plus an age call-out)
- 0:05: "Let's go!"
- 0:38: "Fun fact, L'Oréal owns both." (an insider aside)
- 1:15: "L'Oréal owns Kiehl's…" (a second "same company" aside)
- 1:27.5: **"Okay, but I saved the best for last."** (the main open loop; it bridges to the product)
- 1:33.7–1:40: "La Prairie says it uses PDRN. PDRN is made from fragments of DNA, and it's a big trend in Korean skincare." (a curiosity setup that is paid off by the LUXE reveal)
- 2:02.6: "Comment DM below, and I'll send you the links to everything I just mentioned." (rewards watching the whole list)
- The rising price ladder of the luxury items ($85 → … → $575, with the most expensive saved for item 7) works as an escalation device (reading).

### PRODUCT
- **Product sold:** an eye balm (under-eye stick balm) from LUXE. Spoken: "Lux makes a Korean under-eye balm with PDRN" (1:40.10). The transcript and the captions say "Lux" / "LUX"; the pack reads **"Luxe"**, so the on-screen spelling is used here. Pack text (1:43, zoomed): "Luxe Korean under-eye balm", "Luxe", "PDRN extract". This pack print is cleaner than the garbled tube in video 15.
- **First appears:** spoken at 1:40.10 ("Lux makes a Korean under-eye balm…"). On screen in the 1:41 frame (the first sampled frame after 1:39): a first-person hand holds the pale-blue LUXE tube upright in a Walmart aisle.
- **Bridge line (verbatim):**
  - "Okay, but I saved the best for last." (1:27.50)
  - "La Prairie's Skin Caviar Eye Lift is $575. La Prairie says it uses PDRN. PDRN is made from fragments of DNA, and it's a big trend in Korean skincare." (1:29.5–1:40.1)
  - "Lux makes a Korean under-eye balm with PDRN…" (1:40.10)
- **Saved for last?** Yes. It is item 7 of 7. The "best for last" loop opens at 1:27.5, the La Prairie setup runs from about 1:29.5, and LUXE is named at 1:40 of a 2:08.8 video. The product sits in the last 29 s; counting the setup, the last 41 s.
- **Product shots:**
  - Hand-held tube in a Walmart aisle: 1:41, 1:43, 1:45, 1:47, 1:49, 1:51, 1:53 (closer), 1:55.
  - The avatar holds the tube beside his face in the car: 1:57, 1:59, 2:01.
  - The tube is a slim, matte pale-blue cylinder with a cap, "Luxe" printed vertically in white.
  - No box is shown, no demo, no before/after, no texture shot.
  - **No LUXE price is said or shown.** Every luxury item gets a "$" tag graphic; LUXE gets none. The background shelf tags are for other products.

### CTA
- **Spoken:**
  - "If you want to give it a try, I don't think you'll regret it." (1:53.60)
  - "It's way cheaper on Amazon than anywhere else." (1:55.70)
  - "Search Lux or click the link in my bio." (1:58.00)
  - "And if you're watching on Facebook, the link will be in the comments." (2:00.20)
  - "Comment DM below, and I'll send you the links to everything I just mentioned." (2:02.60)
  - "Just make sure you're following me first so I can message you." (2:06.20)
- **On-screen text:**
  - Burned captions: "I DON'T THINK YOU'LL" (1:55), "AMAZON THAN ANYWHERE ELSE" (1:57), "SEARCH LUX OR CLICK" (1:59), "ON FACEBOOK" (2:01), "COMMENT DM BELOW" (2:03), "THE LINKS TO EVERYTHING" (2:05), "FOLLOWING ME FIRST SO" (2:07).
  - Unlike video 15, no large '"DM"' graphic with down arrows appears in the sampled frames (2:03, 2:05, 2:07). The frames are 2 s apart, so a brief graphic between them can't be ruled out.
  - The caption repeats it: 'Comment "DM" for all my picks'.
- **Where it points:** several destinations at once.
  1. Amazon search "Lux" (spoken). The pack spells it "Luxe".
  2. "link in my bio".
  3. A link in the Facebook comments.
  4. A "comment DM" keyword that triggers a DM, gated on following the page first ("make sure you're following me first so I can message you").

### AVATAR
- **Who:** a peer shopper persona, not a stated expert. He claims no credentials and borrows no "dermatologist" line in this version.
  - Man, East Asian in appearance, about 40s to early 50s (reading).
  - Neat dark side-parted hair with volume on top; thin round gold wire-frame glasses.
  - White button-down shirt.
  - Black DJI-style wireless lav mic clipped to the shirt placket.
  - The page name "Jiho Beauty" is a Korean given name, which fits with "Korean under-eye balm" and "big trend in Korean skincare" (reading).
- **Setting and lighting:**
  - 0:00–0:05 and 2:03–2:07: outside the Walmart entrance, overcast daylight, handheld selfie.
  - 0:07–1:27 and 1:41–1:55: first-person product shots in Walmart beauty aisles (blue/grey shelving, yellow price tags, red "Rollback" flags), flat fluorescent light.
  - 1:29–1:39: in-store selfie pushing a blue Walmart cart, with a "beauty" aisle sign.
  - 1:57–2:01: a parked car, driver's seat, seatbelt on, with the Walmart storefront in the window.
- **Real or AI-looking (my reading, based on what is visible):**
  - **"syntheticmedia" watermark (measured):** small white lowercase text with a thin dark shadow, lower-left, about 84% of the way down the frame. It appears in **every one of the 67 sampled frames, 0:00–2:07**: outside selfie, product point-of-view, in-store selfie and car. Visibility: legible if you look for it, but far smaller than the captions and not animated. In a feed it would read as a faint creator tag rather than a disclosure (reading).
  - **The face changes between scenes (reading):** the in-store selfie face (1:29–1:39), with a longer face, slicker hair and a broader grin, does not look quite the same as the outside face (0:00–0:05, 2:03–2:07) or the car face (1:57–2:01). It looks like different renders under the same styling. Same pattern as video 15.
  - **Shirt marks (reading):** in the outside shots (0:00–0:05 and 2:03–2:07) the white shirt has a few dark spots around the lower placket. They are identical in the opening and closing clips, which suggests one source clip split in two. The spots are absent in the store and car scenes.
  - **Packaging text:** mostly coherent in this version (Aquaphor, CeraVe, Age Perfect, Cicaplast, RoC, Revitalift and LUXE are all legible). Small print on the CeraVe back panel looks scrambled at 0:21 ("Sen a Facial loisturizing… entraite an enfermers…"), a typical generation artifact (reading). The product shots may be real footage with a generated or composited presenter, or fully generated; it can't be told from stills.
  - The hand point-of-view shots keep a consistent white shirt cuff. Lip-sync can't be judged from stills.
- **Delivery:** fast, punchy list rhythm, about one swap every 11–14 s. Casual. Profanity in the very first words: "Cheap shit from Walmart". Conversational asides: "Fun fact", "Okay, but", "is gorgeous, but", "is beautiful, but", "is lovely, but", "About 24 bucks?" (rising intonation in the transcript), "I don't think you'll regret it." Compliments each luxury brand before undercutting it.
- **Who else appears:** only hands holding the products (presented as his own: white cuff) and the luxury product photos as thumbnails. No demo person and no before/after faces, unlike video 15.

### CLAIMS & COMPLIANCE
- "Cheap shit from Walmart that's just as good, if not better, than the luxury stuff." (0:00). Headline: "BETTER THAN LUXURY" (0:01–0:05). "(A must-have for women over 50+)" (0:01–0:05).
- "La Mer's lip balm at $85" (0:06); "The second ingredient in La Mer is the first ingredient in Aquaphor." (0:10); "They share six ingredients." (0:12.8); "Aquaphor is about five bucks." (0:15)
- EltaMD UV Clear vs CeraVe AM: "Same zinc oxide, same octinoxate, same niacinamide." (0:21.4); "It's SPF 30 instead of 46, but it's under $15 for almost twice the size." (0:24.5)
- "Lancôme Absolu Rich Cream is $280." (0:29.5); L'Oréal Age Perfect Rosy Tone "shares 24 ingredients with it. Same squalane, same LHA." (0:32.7–0:38); "Fun fact, L'Oréal owns both." (0:38); "Rosy Tone is about 18 bucks." (0:40)
- "Augustinus Bader's Rich Cream… it's $195 for one ounce." (0:41.9); Cicaplast "has the same panthenol, the same shea butter, and the same vitamin E. And both are fragrance-free. Under $14" (0:48.3–0:55.8)
- "Strivectin's Advanced Retinol Nightly Renewal at $119" (0:55.8); RoC: "20 of the same ingredients, including retinol, shea butter, and vitamin E." (1:02.9); "Strivectin adds retinol, which Rock doesn't have, but Rock is about $22." (1:06.9). This line contradicts the line before it (both are said to contain retinol). The caption at 1:07 also reads "STRIVECTIN ADDS RETINOL WHICH", so it is in the burned-in text, not only a transcript slip (measured; whether the voice says something else can't be checked beyond the transcript).
- "Kiehl's Super Multicorrective Cream… it's $76." (1:11.3); "L'Oréal owns Kiehl's, and their Revitalift Triple Power Fragrance Free shares 19 ingredients with it. Same hyaluronic acid, same adenosine, same LHA. Plus, Pro Retinol and Vitamin C. About 24 bucks?" (1:15.1–1:27.5)
- "La Prairie's Skin Caviar Eye Lift is $575." (1:30); "La Prairie says it uses PDRN." (1:33.7); "PDRN is made from fragments of DNA, and it's a big trend in Korean skincare." (1:35.8)
- LUXE "Korean under-eye balm with PDRN, plus adenosine to smooth wrinkles, hyaluronic acid to plump, argan oil to soften, and collagen extract for elasticity." (1:40.1–1:48.8)
- **"It reduces the look of wrinkles by 30% in four weeks, and it's made for mature skin."** (1:48.8). No source, study or footnote is shown.
- The implied comparison: LUXE is placed as the "dupe" for a $575 La Prairie eye product on the strength of one shared ingredient (PDRN). There is no explicit "does the same job" line in this version (video 15 had one).
- "It's way cheaper on Amazon than anywhere else." (1:55.7). A price-comparison claim; no LUXE price is given.
- "I don't think you'll regret it." (1:53.6)
- Before/after images, testimonial or "client" stories: none.
- Implied credentials: none.
- **"Ad" labels:** the caption begins "AD |", so the page title line reads "148K views · 821 reactions | AD | Over 50? These cheap Walmart finds…". Nothing on screen in the video says "ad", "#ad", "sponsored" or "paid partnership" (none seen in any of the 67 sampled frames). Whether Facebook showed a "Sponsored" or "Paid partnership" label: not found in the metadata.
- **AI disclosure:** only the "syntheticmedia" watermark, in the lower-left, small, on every sampled frame. There is no spoken or caption disclosure, and no AI label field was found in info.json.
- **Risk notes (my reading):**
  - The "30% in four weeks" result claim needs clinical substantiation.
  - Placing LUXE as the cheaper equivalent of La Prairie on one shared ingredient implies comparable efficacy against a named luxury brand.
  - The ingredient-overlap claims about third-party brands (6, 24, 20, 19 shared ingredients; "same zinc oxide, same octinoxate"; "second ingredient… is the first ingredient") are factual comparative claims about named brands and need to be accurate. The StriVectin/RoC retinol line is self-contradictory as captioned. "La Prairie says it uses PDRN" attributes a claim to La Prairie.
  - The quoted luxury prices ($85, $280, $195, $119, $76, $575) are shown as graphics with no date or source.
  - "Way cheaper on Amazon than anywhere else" needs price proof.
  - The "Cheap shit" profanity is in both the spoken hook and the headline.
  - The "Walmart finds" framing, with the LUXE tube filmed in a Walmart aisle, implies it is a Walmart product, but the CTA sends people to Amazon. That could mislead about where it is sold.
  - If the presenter is AI-generated, a small watermark may not count as clear disclosure. Showing a synthetic "real shopper" endorsing a product raises endorsement and disclosure questions (FTC endorsement-guide territory; reading only).

### WHY IT WORKS
Six genuinely recognisable Walmart swaps with big price gaps ($85→~$5, $280→~$18) and "same company owns both" insider asides build trust and a "save this list" reflex before any selling starts.
The "saved the best for last" loop, a $575 La Prairie anchor and a PDRN "Korean skincare trend" bridge make LUXE feel like the list's payoff, and the four-way CTA (Amazon search, bio, comments, comment-DM with a follow gate) catches every kind of viewer.

### OBSERVER NOTES (optional)
- **Measured:** it is the same template as video 15 (Target). The hook and CTA lines are word-for-word the same apart from the store name: "Cheap shit from ___ that's just as good, if not better, than the luxury stuff", "you're gonna want to save this list", "Okay, but I saved the best…", "It's way cheaper on Amazon than anywhere else", "Search Lux[e] or click the link in my bio", "Comment DM below…", "make sure you're following me first". The differences:
  - The headline style changes from white outlined caps to pink highlighter strips.
  - The rehook says "best for last" (Walmart) instead of "best dupe for last" (Target).
  - The luxury anchor for LUXE is La Prairie $575 (Walmart) instead of Chanel $85 (Target).
  - The bridge ingredient is PDRN instead of adenosine.
  - This version drops the demo clip, the before/afters and the "does the same job" line, and it is 20 s longer.
- **Measured:** the price tags use a "number then $" format ("85$", "280$", "195$", "119$", "76$", "575$"), in pink bubble text with heart sparkles, animating in about 2–4 s after each luxury thumbnail appears. EltaMD alone gets no tag. The cheap swaps get no tag graphic; their prices are only spoken or captioned ("ABOUT 5 BUCKS", "18 BUCKS", "UNDER $14").
- **Measured:** the luxury prices climb roughly toward the end, and the most expensive item ($575) is the one the sponsored product is set against.
- **Measured:** the Walmart shelf tags in the background match the spoken swap prices: Age Perfect "$17.97" against "about 18 bucks"; Cicaplast "$13.97" against "Under $14"; RoC "$21.97" against "about $22"; Revitalift "$23.97" against "about 24 bucks". The cheap-side prices look grounded in real shelf footage (reading).
- **Measured, spelling corrections from the pack and on-screen text:**
  - "Lux" → "Luxe" (pack). The captions also say "LUX".
  - "Cicoplas Balm B5" → "CICAPLAST BAUME B5+" (pack).
  - "Rock" → "RoC" (pack). The caption says "ROCK".
  - "Absolu" → the thumbnail reads "ABSOLUE"; the caption reads "ABSOLUTE".
  - "La Mer" → the caption reads "LAMAIR" at 0:15.
  - "Aquaphor Lip Repair" → the pack reads "Eucerin Aquaphor SOS LIP REPAIR".
- **Measured:** view_count 72,893 against video 15's 650,286. The title-line reactions (821) are low relative to its views compared with the Target version (18K) (reading on engagement; the figures are as returned).

---

## Video 11 — Jiho Beauty — "Cheap shit from Walmart that's better than luxury"
**Link:** https://www.facebook.com/share/v/19LvPLPe16/ (video ID 1906443924098073) · **Page:** Jiho Beauty (uploader_id 61592837168330) · **Uploaded:** 2026-10-21, 20:25:55 UTC (yt-dlp `timestamp` 1792614355) · **Duration:** 128.8 s (2:08.8) · **Views:** view_count 61,754 (page title line says "124K views") · **Reactions:** "1.3K reactions" (title line) · **Comments:** not found (comment_count not in metadata)
*(All metadata from videos/11.info.json, pulled 2026-11-07.)*

**Caption (verbatim):** "AD | Over 50? These cheap Walmart finds are just as good, if not better, than the luxury stuff

Comment "DM" for all my picks

#usa #walmartfinds #skincare #matureskin #maturewoman"

### HOOK (0:00–0:05)
- Spoken: "Cheap shit from Walmart that's just as good, if not better, than the luxury stuff." (0:00–0:03) / "And if you're over 50, you're gonna want to save this list. Let's go!" (0:03–0:06)
- On-screen text:
  - Headline (pink highlighter boxes, white handwritten-style font, top of frame, types on from ~0:00.5, complete by 0:01, stays to 0:06): "CHEAP SHIT FROM WALMART THAT'S BETTER THAN LUXURY"
  - Sub-headline under it: "(A must-have for women over 50+)"
  - Burned-in word captions (centre, white bold, one word highlighted in a black box): 0:01 "CHEAP SHIT FROM WALMART" · 0:02 "IF NOT BETTER THAN" · 0:03 "THE LUXURY STUFF" · 0:04 "AND IF YOU'RE OVER 50" · 0:05 "YOU'RE GONNA WANNA SAVE"
  - 0:00 frame: no headline or caption yet; "syntheticmedia" watermark already present lower-left.
- Visual: handheld selfie, chest-up, a man in a white dress shirt and round gold wire glasses stands outside a Walmart store entrance (blue "Walmart" façade top-left, carts, parking lot, cars). Daylight, slightly overcast. A small black clip-on wireless mic (DJI logo) on his shirt placket. He gestures with one hand toward camera. Hard cut to the first in-store product shot at 0:06.2.

### FORMAT
"Walmart drugstore dupes for luxury skincare, 6 swaps, then the 'best for last' pivot to the product."
Six "instead of [luxury product + price], grab [Walmart product]" swaps, each with an ingredient-overlap or "same company owns it" fact. Item 7 names a $575 luxury eye cream and swaps it for LUXE's Korean under-eye balm (no LUXE price given), then a multi-route CTA.

### BODY (beats)
Scene cuts measured with ffmpeg scene detection (threshold 0.25) at: 0:06.2, 0:17.1, 0:29.5, 0:41.9, 0:55.8, 1:11.3, 1:27.5, 1:40.1, 1:48.8 (jump cut inside the LUXE shot), 1:55.7, 2:02.6. Every swap shot is the same: a POV hand (white shirt cuff) holds the cheap product in a Walmart aisle with yellow price tags and "Rollback" signs; a white-box cut-out image of the luxury product sits top-left, and a pink bubble price badge ("85$" style, with the $ after the number) pops in about 2 s later.

| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:00–0:06 | Hook (see above) | Outside Walmart, selfie. Headline + sub-headline. |
| 0:06–0:17 | #1 "Instead of La Mer's lip balm at $85, grab Aquaphor Lip Repair. The second ingredient in La Mer is the first ingredient in Aquaphor. They share six ingredients. La Mer is gorgeous, but Aquaphor is about five bucks." | Hand holds a tube labelled "Eucerin -Aquaphor- SOS LIP REPAIR" (spoken as "Aquaphor Lip Repair"). Inset: La Mer lip balm jar (lid "LA MER"), 0:07; badge "85$" from 0:09. Captions: 0:07 "INSTEAD OF LA MER'S", 0:09 "GRAB AQUAPHOR LIP REPAIR", 0:11 "THE SECOND INGREDIENT IN", 0:13 "THEY SHARE SIX INGREDIENTS", 0:15 "LAMAIR IS GORGEOUS BUT" (misspelled caption), 0:17 "AQUAPHOR IS ABOUT 5 BUCKS". The shelf tag for this exact item is not legible. |
| 0:17–0:29 | #2 "If you love EltaMD UV Clear, try CeraVe AM Facial Moisturizing Lotion. Same zinc oxide, same octinoxate, same niacinamide. It's SPF 30 instead of 46, but it's under $15 for almost twice the size." | Hand holds "CeraVe AM Facial Moisturizing Lotion" in a CeraVe-stocked aisle. Inset: EltaMD UV Clear bottle ("elta MD … UV Clear … 46"). **No price badge** in any sampled frame from 0:19 to 0:29, matching the script (no EltaMD price said). Captions: 0:19 "U V CLEAR TRY", 0:21 "CERAVE AM FACIAL MOISTURIZING LOTION", 0:23 "SAME ZINC OXIDE SAME OCTINOXATE", 0:25 "IT'S SPF 30 INSTEAD". |
| 0:29–0:42 | #3 "Lancôme Absolute Rich Cream is $280. L'Oréal Age Perfect Rosy Tone shares 24 ingredients with it. Same squalane, same LHA. Fun fact, L'Oréal owns both. Rosy Tone is about 18 bucks." | Hand holds a pink "L'ORÉAL PARIS AGE PERFECT" jar with a gold lid ("…FRAGRANCE-FREE / SANS PARFUM"). Inset: gold Lancôme jar labelled "LANCÔME ABSOLUE", 0:31; badge "280$" from 0:33. Shelf tag "$17.97" visible beside the jars. Captions: 0:31 "LANCOME ABSOLUTE RICH CREAM" (jar says "ABSOLUE"), 0:33 "L'OREAL AGE PERFECT ROSY", 0:35 "TONE SHARES 24 INGREDIENTS", 0:37 "SAME SQUALANE SAME LHA", 0:39 "L'OREAL OWNS BOTH", 0:41 "18 BUCKS". |
| 0:42–0:56 | #4 "Augustinus Bader's Rich Cream is beautiful, but it's $195 for one ounce. La Roche-Posay Cicoplas Balm B5 has the same panthenol, the same shea butter, and the same vitamin E. And both are fragrance-free. Under $14," | Hand holds a tube labelled "LA ROCHE-POSAY CICAPLAST BAUME B5+" (the transcript's "Cicoplas Balm" is the machine spelling). Inset: navy Augustinus Bader bottle, 0:43; badge "195$" from 0:47. Shelf tags "$13.97". Captions: 0:43 "AUGUSTINUS BADER'S RICH CREAM", 0:49 "LA ROCHE POSAY CICAPLAST", 0:51 "SAME PANTHENOL", 0:53 "AND THE SAME VITAMIN E", 0:55 "UNDER $14". (No caption in the 0:45 and 0:47 frames.) |
| 0:56–1:11 | #5 "instead of Strivectin's Advanced Retinol Nightly Renewal at $119, try Rock Retinol Correction Deep Wrinkle Night Cream. 20 of the same ingredients, including retinol, shea butter, and vitamin E. Strivectin adds retinol, which Rock doesn't have. But Rock is about $22." | Hand holds a gold tube labelled "RoC RETINOL CORREXION DEEP WRINKLE NIGHT CREAM" (spoken and captioned as "Rock"). Inset: pink-purple StriVectin tube ("NIA114 … Advanced Retinol Nightly Renewal Moisturizer"), 0:57; badge "119$" animating in at 0:59. Shelf tags "$21.97". Captions: 0:57 "INSTEAD OF STRIVECTIN'S ADVANCED", 0:59 "RETINOL NIGHTLY RENEWAL AT $119", 1:01 "TRY ROCK RETINOL CORRECTION", 1:03 "20 OF THE SAME", 1:05 "INGREDIENTS INCLUDING RETINOL", 1:07 "STRIVECTIN ADDS RETINOL WHICH". |
| 1:11–1:27 | #6 "Kiehl's Super Multicorrective Cream is lovely, but it's $76. L'Oréal owns Kiehl's, and their Revitalift Triple Power Fragrance Free shares 19 ingredients with it. Same hyaluronic acid, same adenosine, same LHA. Plus Pro-Retinol and Vitamin C. About $24?" | Hand holds a red "L'ORÉAL PARIS REVITALIFT TRIPLE POWER … FRAGRANCE FREE MOISTURIZER [PRO-RETINOL + HYALURONIC ACID + VITAMIN C]" jar. Inset: purple Kiehl's jar ("Kiehl's SUPER MULTI-CORRECTIVE SOFT CREAM"), 1:13; badge "76$" from 1:15. Shelf tags "$23.97". Captions: 1:13 "CREAM IS LOVELY BUT", 1:15 "IT'S $76", 1:19 "SHARES 19 INGREDIENTS WITH IT", 1:21 "SAME HYALURONIC ACID SAME ADENOSINE", 1:23 "SAME LHA PLUS PRO". |
| 1:27–1:40 | #7 pivot: "Okay, but I saved the best for last. La Prairie's Skin Caviar Eye Lift is $575. La Prairie says it uses PDRN. PDRN is made from fragments of DNA, and it's a big trend in Korean skincare." | Cut back to the presenter: selfie, pushing a Walmart cart down the "beauty" aisle (aisle sign reads "beauty"). Inset: blue/gold La Prairie bottle, 1:31; badge "575$" from 1:33. Captions: 1:29 "BEST FOR LAST", 1:31 "EYE LIFT IS $575", 1:35 "LA PRAIRIE SAYS IT USES PDRN", 1:37 "PDRN IS MADE FROM", 1:39 "TREND IN KOREAN SKINCARE". |
| 1:40–1:56 | PRODUCT: "Luxe makes a Korean under-eye balm with PDRN, plus adenosine to smooth wrinkles, hyaluronic acid to plump, argan oil to soften, and collagen extract for elasticity. It reduces the look of wrinkles by 30% in four weeks, and it's made for mature skin. If you want to give it a try, I don't think you'll regret it." | POV hand holds a pale-blue stick or bottle printed "Luxe Korean under-eye balm" / "Luxe" (vertical) / "PDRN extract", in front of a Walmart shelf (Rollback signs, yellow tags). **No inset and no price badge.** Jump cut at 1:48.8; the bottle is held closer from about 1:53. Captions: 1:41 "LUX MAKES A KOREAN" (the caption says "LUX"; the bottle says "Luxe"), 1:45 "HYALURONIC ACID TO PLUMP", 1:47 "AND COLLAGEN EXTRACT FOR ELASTICITY", 1:49 "IT REDUCES THE LOOK", 1:51 "OF WRINKLES BY 30%", 1:53 "AND IT'S MADE FOR", 1:55 "I DON'T THINK YOU'LL". |
| 1:56–2:03 | CTA 1: "It's way cheaper on Amazon than anywhere else. Search Luxe or click the link in my bio. And if you're watching on Facebook, the link will be in the comments." | New setting: the presenter sits in the driver's seat of a parked car with his seatbelt on. The Walmart storefront shows through the passenger window. He holds the LUXE bottle up beside his face. Captions: 1:57 "AMAZON THAN ANYWHERE ELSE", 1:59 "SEARCH LUX OR CLICK", 2:01 "ON FACEBOOK". |
| 2:03–2:09 | CTA 2: "Comment DM below, and I'll send you the links to everything I just mentioned. Just make sure you're following me first so I can message you." | Back outside the Walmart entrance (the same spot and framing as the hook). Captions: 2:03 "COMMENT DM BELOW", 2:05 "THE LINKS TO EVERYTHING", 2:07 "FOLLOWING ME FIRST SO". Ends 2:08.8 with no end card. |

**Rehooks / open loops**
- 0:03 "And if you're over 50, you're gonna want to save this list. Let's go!" (save prompt plus list promise)
- 0:39 "Fun fact, L'Oréal owns both." (insider reveal)
- 1:15 "L'Oréal owns Kiehl's" (second insider reveal)
- 1:27 "Okay, but I saved the best for last." (caption 1:29 "BEST FOR LAST")
- 1:29 "La Prairie's Skin Caviar Eye Lift is $575." (the highest price in the video, used as the anchor right before the product)
- Structural loop (my reading): each luxury inset shows first and its price badge lands about 2 s later, so every swap is a small "how much?" reveal.

### PRODUCT
- Product sold: eye balm. LUXE (bottle reads "Luxe"), "Luxe Korean under-eye balm", "PDRN extract" (as printed on the bottle). Spoken: "Luxe makes a Korean under-eye balm with PDRN" (1:40). The burned-in captions spell it "LUX" (1:41, 1:59), and the bottle spelling is "Luxe".
- First appears: spoken 1:40.1 ("Luxe makes a Korean under-eye balm…"). On screen 1:40.1 (scene cut). First sampled frame 1:41: POV hand holding the pale-blue bottle in a Walmart aisle. It is not seen anywhere earlier in the video.
- Bridge line (verbatim): "Okay, but I saved the best for last." (1:27) → "La Prairie's Skin Caviar Eye Lift is $575." (1:29) → "La Prairie says it uses PDRN." (1:33) → "PDRN is made from fragments of DNA, and it's a big trend in Korean skincare." (1:35–1:40) → "Luxe makes a Korean under-eye balm with PDRN," (1:40)
- Saved for last? Yes. It is item 7 of 7. The item-7 setup starts at 1:27 and the product itself at 1:40 of 2:08.8 (78% of the way through).
- Product shots: a single pale-blue cylindrical stick or bottle with a ribbed cap, white text ("Luxe Korean under-eye balm", large vertical "Luxe", "PDRN extract"). Handheld POV in a Walmart aisle (1:40–1:56), then held by the presenter in the car (1:56–2:03). No application or demo, no before/after, no texture shot, no price badge, no Amazon screenshot. Unlike the six dupes, the LUXE shot has no luxury-product inset.

### CTA
- Spoken: "If you want to give it a try, I don't think you'll regret it." (1:53.6) · "It's way cheaper on Amazon than anywhere else." (1:55.7) · "Search Luxe or click the link in my bio." (1:58.0) · "And if you're watching on Facebook, the link will be in the comments." (2:00.2) · "Comment DM below, and I'll send you the links to everything I just mentioned." (2:02.6) · "Just make sure you're following me first so I can message you." (2:06.2–2:08.6)
- On-screen text: 1:55 "I DON'T THINK YOU'LL", 1:57 "AMAZON THAN ANYWHERE ELSE", 1:59 "SEARCH LUX OR CLICK", 2:01 "ON FACEBOOK", 2:03 "COMMENT DM BELOW", 2:05 "THE LINKS TO EVERYTHING", 2:07 "FOLLOWING ME FIRST SO". These are burned-in speech captions; there is no separate CTA graphic or button.
- Caption CTA: "Comment "DM" for all my picks"
- Where it points: (1) Amazon search "Luxe"; (2) "link in my bio"; (3) on Facebook, "the link will be in the comments"; (4) "Comment DM" keyword DM automation for links to all products; (5) follow-first gate ("make sure you're following me first so I can message you").

### AVATAR
- Who: peer or "savvy shopper" insider, not a credentialed expert. No credentials are claimed or implied in words. The "insider" signals are ingredient-list comparisons and parent-company facts ("L'Oréal owns both", "L'Oréal owns Kiehl's"). He is a man presenting to women: the headline says "(A must-have for women over 50+)" and the script says "if you're over 50", but the presenter never says his own age. Approximate age (my reading): mid-40s to mid-50s. Apparent ethnicity (my reading): East Asian (the page name "Jiho Beauty" suggests a Korean name, which fits the "Korean skincare" angle). Clothing: crisp white long-sleeve button-down dress shirt, round thin gold-rim glasses, swept-back black hair, black clip-on wireless mic with a DJI logo.
- Setting & lighting: four settings. (a) Outside a Walmart entrance in daylight (0:00–0:06, 2:03–2:09). (b) Walmart aisles, POV hand-held product shots under store fluorescents (0:06–1:27, 1:40–1:56). (c) The Walmart "beauty" aisle, selfie while pushing a cart (1:27–1:40). (d) A parked car facing the Walmart storefront, selfie (1:56–2:03). All handheld selfie or POV, no tripod look, natural or store lighting.
- Real or AI-looking (my reading): a small white "syntheticmedia" text watermark sits lower-left of frame (around x=40–175, y=715 at 480 px width) in **every sampled frame from 0:00 to 2:07**. That points to AI-generated or AI-altered footage. Otherwise the footage looks highly realistic: natural hand texture and veins on the POV hands, consistent shirt cuffs, believable shelf clutter and legible real price tags, and small marks on the shirt front in the outdoor scenes (hook and 2:03–2:07). I saw no obvious lip-sync drift or finger errors at contact-sheet resolution. One thing that reads as a possible composite (reading only): the LUXE bottle is shown on Walmart shelves, although the script sends viewers to Amazon.
- Delivery: quick, upbeat, conversational list pace (about 2 s per caption chunk, one swap every 11–16 s). Profanity: "Cheap shit from Walmart" (0:00, spoken and in the headline, uncensored). Casual phrasing: "about five bucks", "Fun fact", "Let's go!", "Okay, but I saved the best for last." It is casual, not formal.
- Who else appears: no other people on camera. The POV hands holding products (white shirt cuff, so presumably the presenter's own) and a few distant shoppers in the parking-lot background. No models and no before/after faces.

### CLAIMS & COMPLIANCE
- 0:06 "Instead of La Mer's lip balm at $85" (price; inset badge "85$" 0:09)
- 0:09.9 "The second ingredient in La Mer is the first ingredient in Aquaphor."
- 0:12.8 "They share six ingredients."
- 0:15 "La Mer is gorgeous, but Aquaphor is about five bucks."
- 0:21.4 "Same zinc oxide, same octinoxate, same niacinamide." (EltaMD UV Clear vs CeraVe AM)
- 0:24.5 "It's SPF 30 instead of 46, but it's under $15 for almost twice the size."
- 0:29.4 "Lancôme Absolute Rich Cream is $280." (badge "280$")
- 0:32.6 "L'Oréal Age Perfect Rosy Tone shares 24 ingredients with it." / 0:36 "Same squalane, same LHA."
- 0:39.8 "Fun fact, L'Oréal owns both." ("same company owns")
- 0:41.8 "Rosy Tone is about 18 bucks." (shelf tag "$17.97" visible)
- 0:41.8 "Augustinus Bader's Rich Cream is beautiful, but it's $195 for one ounce." (badge "195$")
- 0:48.2 "La Roche-Posay Cicoplas Balm B5 has the same panthenol, the same shea butter, and the same vitamin E." / 0:53.5 "And both are fragrance-free." / 0:54.8 "Under $14" (shelf tags "$13.97")
- 0:54.8 "Strivectin's Advanced Retinol Nightly Renewal at $119" (badge "119$")
- 1:02.8 "20 of the same ingredients, including retinol, shea butter, and vitamin E."
- 1:06.8 "Strivectin adds retinol, which Rock doesn't have." This contradicts 1:02.8 ("including retinol"), as the audio is transcribed and captioned (caption 1:07 "STRIVECTIN ADDS RETINOL WHICH").
- 1:09.4 "But Rock is about $22." (shelf tags "$21.97")
- 1:11.2 "Kiehl's Super Multicorrective Cream is lovely, but it's $76." (badge "76$")
- 1:15.0 "L'Oréal owns Kiehl's" ("same company owns")
- 1:15–1:20 "their Revitalift Triple Power Fragrance Free shares 19 ingredients with it." / 1:20.2 "Same hyaluronic acid, same adenosine, same LHA." / 1:23.7 "Plus Pro-Retinol and Vitamin C." / 1:26.2 "About $24?" (shelf tags "$23.97")
- 1:29.2 "La Prairie's Skin Caviar Eye Lift is $575." (badge "575$")
- 1:33.6 "La Prairie says it uses PDRN."
- 1:35.7 "PDRN is made from fragments of DNA, and it's a big trend in Korean skincare."
- 1:40–1:48 LUXE ingredient and function claims: "PDRN", "adenosine to smooth wrinkles", "hyaluronic acid to plump", "argan oil to soften", "collagen extract for elasticity"
- 1:48.7 "It reduces the look of wrinkles by 30% in four weeks" (stat with no source, study or fine print on screen) (caption 1:51 "OF WRINKLES BY 30%")
- 1:52.2 "and it's made for mature skin."
- 1:53.6 "If you want to give it a try, I don't think you'll regret it." (soft result assurance)
- 1:55.7 "It's way cheaper on Amazon than anywhere else." (price-comparison claim; the LUXE price itself is not said or shown)
- Implied (reading): putting LUXE in a "cheap … Walmart" list straight after a $575 La Prairie eye cream implies a comparison of equivalence or value with La Prairie via PDRN. No direct "same ingredients" number is given for LUXE vs La Prairie.
- No bestseller or scarcity line, no "dermatologists love", no client or testimonial story.

- "Ad"/"#ad"/"Sponsored"/"paid partnership" shown? The caption begins "AD | Over 50? …", and the page title line carries the same "AD |" prefix. Spoken: not said. On-screen: no "Ad"/"#ad" text in any sampled frame. "Sponsored" or "paid partnership" label: not found in the metadata. The scrape cannot show Facebook's own Sponsored label.
- AI disclosure shown? Only the "syntheticmedia" watermark: small, white, lower-left, low-contrast, present in every sampled frame 0:00–2:07. There is no spoken or caption AI disclosure.
- Risk notes (my reading):
  - Uncensored profanity in the opening line and the headline ("Cheap shit").
  - Comparative claims against named luxury brands (La Mer, EltaMD, Lancôme, Augustinus Bader, StriVectin, Kiehl's, La Prairie), with specific prices and ingredient-overlap counts (6, 24, 20, 19). These would need dated substantiation (INCI lists, retail prices).
  - The 1:02.8 vs 1:06.8 retinol contradiction undercuts the comparison's accuracy.
  - The "30% in four weeks" efficacy stat for LUXE has no visible substantiation.
  - "Way cheaper on Amazon than anywhere else" is an unsupported superlative price claim.
  - LUXE is filmed on a Walmart shelf inside a "Walmart finds" video, which may imply in-store Walmart availability. Not verified; the script points to Amazon.
  - The relationship disclosure is limited to the caption "AD |"; the presenter doesn't state a connection to LUXE.
  - The presenter's gender and age (a man) are not the stated audience ("women over 50+"). That is not a compliance issue, just noted.

### WHY IT WORKS
Six fast, concrete "luxury price → Walmart dupe → shared-ingredient fact" swaps build trust in the presenter's frugality and expertise before any sell, so the LUXE pitch lands as swap #7 rather than an ad.
The $575 La Prairie anchor and "PDRN … big trend in Korean skincare" bridge make an unpriced LUXE balm feel like the obvious smart buy, and the CTA covers every route (Amazon search, bio link, comments link, comment-DM).

### OBSERVER NOTES (optional)
- Measured: shelf price tags visible in the footage line up with the spoken dupe prices (Age Perfect "$17.97" ↔ "about 18 bucks"; Cicaplast "$13.97" ↔ "Under $14"; RoC "$21.97" ↔ "about $22"; Revitalift "$23.97" ↔ "About $24?").
- Measured: the luxury price badges use a "number + $" order ("85$", "280$", "195$", "119$", "76$", "575$"). EltaMD is the only luxury item with no price badge, and no EltaMD price is spoken.
- Measured: caption spelling errors include "LAMAIR" (0:15), "LANCOME ABSOLUTE" (0:31, the pack says "ABSOLUE"), "ROCK" (1:01, the pack says "RoC") and "LUX" (1:41, 1:59, the pack says "Luxe"). They read as auto-captions left unedited.
- Reading: the audience mismatch (a male presenter, "a must-have for women over 50+") is unusual for this niche and is worth testing against female presenters on the same script.
- Measured: the title-line view figure (124K) is about 2x the yt-dlp view_count (61,754). This is the same pattern METADATA.md notes across the set.

### DIFFERENCES FROM VIDEO 10
**Result: no visible differences. Video 11 and video 10 are the same edit (same footage, overlays, captions, cuts and audio), encoded as two separate files.**

How this was checked (measured 2026-11-07 from the local files):
- **Contact sheets side by side:** I read 10/sheet_01, 07 and 09 next to 11/sheet_01, 07 and 09. They match frame for frame at every label: the same presenter, pose, mouth shape, hand position, background cars, headline, captions, insets, price badges and watermark position.
- **All 68 sampled frames (0, 1, 2, 3, 4, 5, 7, … 127 s), pixel comparison:** mean absolute difference per frame is 0.92–1.49 on a 0–255 scale. After an 8 px blur, the largest local difference anywhere in any frame is 3–5/255, and no region exceeds a 20/255 threshold. So there is no localized change: no different text, product, face or watermark anywhere.
- **Every frame of the full video (3,863 frames each), compared with ffmpeg PSNR at 270×480 grayscale:** the minimum is 43.3 dB (frame 1673, about 0:55.8, at a cut) and the mean is 47.8 dB. No frame falls below 35 dB. That level is consistent with two compressions of one master, not different footage.
- **Cut timing:** ffmpeg scene detection (threshold 0.25) gives the identical 11 cuts in both videos, to the frame: 6.23, 17.10, 29.47, 41.90, 55.77, 71.27, 87.47, 100.13, 108.80, 115.70 and 122.63 s.
- **Audio:** cross-correlation of the two soundtracks (mono, 16 kHz) is 0.9989 at zero lag. No 1-second window falls below 0.95 correlation. It is the same voice track, same take, same timing.
- **Transcript differences are transcription only:** the segment boundaries differ, plus "Absolute" (11) vs "Absolu" (10) at 0:29 and "Luxe" (11) vs "Lux" (10) at 1:40 and 1:58. The audio underneath is identical.
- **Element by element:** presenter or avatar the same; setting the same (Walmart exterior, aisles, beauty aisle with cart, car); on-screen text the same (headline, sub-headline and every caption, including the "LAMAIR" and "LUX" misspellings); product shots and insets the same; hook visual the same; "syntheticmedia" watermark the same, lower-left, present throughout both; cut timing the same.

What *does* differ (file and metadata level only):

| | Video 10 | Video 11 |
|---|---|---|
| Video ID | 1818694942613295 | 1906443924098073 |
| Uploaded (UTC) | 2026-10-22 20:55:12 | 2026-10-21 20:25:55 (about 24.5 h earlier) |
| view_count | 72,893 | 61,754 |
| Title line | "148K views · 821 reactions" | "124K views · 1.3K reactions" |
| File size / video bitrate | 21,885,482 bytes / 1,292,572 bps | 21,400,260 bytes / 1,264,097 bps |
| MD5 | 756f037d… | 8d15a977… |
| Codec / res / fps / frames | AV1 1080×1920, 30 fps, 3,863 | identical |
| Caption | identical text | identical text |

Reading: video 11 is the earlier post, and video 10 is the same creative reposted the next day, probably as a separate ad or post to test or extend delivery. Facebook re-encoded each upload, which is why the files differ. Video 11 has fewer views but more reactions (1.3K vs 821).

---

## Video 12 — Jiho Beauty — "Cheap shit from Target that's better than luxury"
**Link:** https://www.facebook.com/share/v/1FDQFvHFWD/ (video ID 1400995212201059) · **Page:** Jiho Beauty · **Uploaded:** 2026-10-12 (17:13:21 UTC, from info.json `timestamp`) · **Duration:** 1:48 (108.5 s) · **Views:** view_count 45,530 (page title line says "89K views") · **Reactions:** "1.2K reactions" (from title line) · **Comments:** not found (comment_count empty in metadata)
**Caption (verbatim):** "AD | These cheap Target finds beat luxury, and the under-eye secret nobody told you about 👀 Comment "DM" for all my picks 💌

#usa #skincare #matureskin #maturewoman #skincareroutine"

**Repost of video 15 (measured).** Same page, same caption, same length (108.508 s), same frame count (3,255 frames at 30 fps) and a word-for-word identical transcript. The audio track is bit-for-bit identical to 15's. The picture is the same edit, re-encoded (details under DIFFERENCES FROM VIDEO 15). Video 12 is the fourth and latest post of this ad on the page (15 on Oct 7, 13 and 14 on Oct 11, 12 on Oct 12) and the weakest: view_count 45,530, against 650,286 for 15. Metadata pulled 2026-11-07 (videos/METADATA.md). Everything below was checked against 12's own 57 sampled frames and 12's transcript.

### HOOK (0:00–0:05)
- **Spoken:** "Cheap shit from Target that's just as good, if not better, than the luxury stuff." (0:00–0:04) / "And if you're over 50, you're gonna want to save this list." (0:04–0:06) / "Let's go." (0:06–0:07)
- **On-screen text:**
  - Headline, 0:01–0:05 (not in the 0:00 frame, gone by 0:07). White heavy caps with a dark outline, at the top of the frame: "CHEAP SHIT FROM 🎯 TARGET THAT'S BETTER THAN LUXURY". The 🎯 emoji echoes Target's bullseye.
  - Sub-headline, 0:01–0:05, pink, sentence case: "A must-have for women over 50+".
  - Burned-in captions in white condensed caps, with one word at a time on a black box:
    - "CHEAP SHIT FROM TARGET" (0:00, 0:01)
    - "THAT'S JUST AS GOOD" (0:02)
    - "IF NOT BETTER THAN" (0:03)
    - "THE LUXURY STUFF" (0:04)
    - "50 YOU'RE GONNA WANNA" (0:05)
  - The headline says "BETTER THAN LUXURY". The spoken line is softer: "just as good, if not better".
- **Visual:** The avatar walks in a selfie shot, held at arm's length, chest-up, down a Target health and beauty aisle: red walls, a Target bullseye aisle sign, white shelves of skincare, fluorescent ceiling lights. He pushes a red Target cart holding several plain white boxes. A black DJI wireless lav mic with a furry windscreen is clipped to his shirt. He talks straight to camera with raised eyebrows.

### FORMAT
**A Target "dupes for luxury" swap list, with the sponsored product slotted in as "the best dupe saved for last."**
Six real drugstore swaps (Nivea, e.l.f. ×3, Olay, L'Oréal), each set against a named luxury product with a price tag; the 7th "dupe" is LUXE's under-eye balm, set against Chanel and introduced with the same ingredient-overlap logic.

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:07–0:15 | **Swap 1:** "Instead of La Mer at $200, grab Nivea Creme. Fourteen of its sixteen ingredients are in La Mer. Almost in the same order. La Mer is gorgeous, but Nivea is ten bucks for a huge tub." | First-person hand (white shirt cuff) holds the blue Nivea Creme tin in an aisle stocked with Nivea. Top left: La Mer jar thumbnail; pink outlined "$200" tag from 0:09. Captions: "INSTEAD OF LA MER" (0:07), "GRAB NIVEA CREAM" (0:09), "INGREDIENTS ARE IN LA MER" (0:11), "LA MER IS GORGEOUS" (0:13), "BUCKS FOR A HUGE TUB" (0:15). No tag for Nivea; its price is only spoken. |
| 0:15–0:24 | **Swap 2:** "If you love Supergoop Unseen, try Elf Sun Touchable Invisible. Same four sun filters, goes on clear, works like a primer, $15, not $38." | Hand holds an e.l.f. SKIN invisible sunscreen tube, SPF 35, in front of a sunscreen shelf. Top left: Supergoop tube thumbnail on yellow, "$38". Captions: "IF YOU LOVE SUPERGOOP UNSEEN" (0:17), "TRY ELF SUN TOUCHABLE INVISIBLE" (0:19), "GOES ON CLEAR WORKS" (0:21), "$15 NOT 38SK2" (0:23; the caption runs into the next line). |
| 0:24–0:37 | **Swap 3:** "SK-II Skin Power Cream is $170. Olay Regeneris[t] Micro-Sculpting Cream shares 23 ingredients with it. Same firming peptide, same niacinamide. Fun fact, the same company owns both. Olay is $24." | Hand holds a red Olay Regenerist Micro-Sculpting Cream jar (pack reads "REGENERIST") in front of an Olay wall. Top left: SK-II Skinpower red jar thumbnail (no tag at 0:25); tag animates in: "$17" at 0:27, "$170" from 0:29. Captions: "SKIN POWER CREAM IS $170" (0:25, 0:27), "OLAY REGENERIST MICRO SCULPTING" (0:29), "CREAM SHARES 23 INGREDIENTS" (0:31), "SAME FIRMING PEPTIDE SAME NIACINAMIDE" (0:33), "THE SAME COMPANY OWNS BOTH" (0:35), "OLAY IS 24 BUCKS" (0:37). |
| 0:37–0:46 | **Swap 4:** "Skinceutical[s] CE Ferulic is the vitamin C serum dermatologists love, but it's $185. Elf Bright Icon has the same big three. Vitamin C, vitamin E, ferulic acid, $17." | Hand holds an orange e.l.f. "Vitamin C + E + Ferulic Serum" (Bright Icon) in a cosmetics aisle. Top left: SkinCeuticals C E Ferulic dropper bottle thumbnail; "$185" tag from 0:43 (not at 0:39/0:41). Captions: "IS THE VITAMIN C" (0:39), "BUT IT'S $185 ELF" (0:41), "BRIGHT ICON HAS THE" (0:43), "FERULIC ACID $17" (0:45). |
| 0:46–0:55 | **Swap 5:** "Instead of Estee Lauder Advanced Night Repair at $88, try Elf Youth Boosting Night Retinoid Serum. Seventeen of the same ingredients, plus a retinoid for fine lines, $23." | Hand holds a lavender e.l.f. SKIN "Youth Boosting" pump bottle. Top left: Estée Lauder ANR bottle thumbnail; tag "$8" at 0:49 (mid-animation), "$88" from 0:51. Captions: "INSTEAD OF ESTEE LAUDER" (0:47), "ADVANCED NIGHT REPAIR AT $88" (0:49), "NIGHT RETINOL SERUM" (0:51), "INGREDIENTS PLUS A RETINOL" (0:53), "$23" (0:55). Captions say "RETINOL"; the transcript hears "retinoid". |
| 0:55–1:04 | **Swap 6:** "Lancôme Genifique is beautiful, but it's over $200. L'Oréal owns Lancôme, and their Revitalift serum has the same active ingredients. Get this one instead." | Hand holds a L'Oréal Revitalift Hyaluronic Acid 1.5% serum in front of a Revitalift shelf with red "Sale" tags. Top left: Lancôme Génifique bottle thumbnail (no tag at 0:57); "$200" from 0:59. Captions: "LANCOME GENIFIQUE IS BEAUTIFUL" (0:57), "L'OREAL OWNS LANCOME" (0:59), "AND THEIR REVITALIFT SERUM" (1:01), "GET THIS ONE INSTEAD" (1:03). No Revitalift price said or tagged. |
| 1:04–1:05 | **Rehook:** "Okay, but I saved the best dupe for last." | Cut back to the avatar's selfie in the aisle with the cart. Caption: "THE BEST DUPE FOR LAST" (1:05). |
| 1:05–1:19 | **Luxury setup for item 7:** "If you've seen Chanel's number one revitalizing eye cream, it's lovely, but it's $85 for a tiny jar. One of its key ingredients is adenosine. Adenosine is a molecule your body naturally makes, and in skincare, it helps smooth wrinkles." | Avatar selfie in the store. Top right: Chanel N°1 eye cream jar thumbnail (from 1:07), "$85" from 1:11. Open-hand gesture at 1:11 and 1:17. Captions: "NO. 1 REVITALIZING EYE CREAM" (1:07), "IT'S LOVELY" (1:09), "A TINY JAR" (1:11), "ADENOSINE IS A MOLECULE" (1:13), "AND IN SKINCARE IT" (1:17), "HELPS SMOOTH WRINKLES" (1:19). The 1:15 frame has no caption. |
| 1:19–1:28 | **Item 7, the sponsored product:** "Luxe makes a Korean under-eye balm with that same adenosine, plus hyaluronic acid to plump, argan oil to soften, and PDRN and collagen extract for firmer looking skin." | Hand holds a pale-blue LUXE stick tube ("Luxe" printed vertically) in front of a bay stocked with blue "Luxe" tubes and boxes plus other generic tubes; Target-style shelf tags read "17.99", "12.99", "11.99", "14.99" (and "10.99", "7.99", "14.99", "14.99" on the shelf above). Captions: "UNDER EYE BALM WITH" (1:21), "PLUS HYALURONIC ACID TO PLUMP" (1:23), "ARGAN OIL TO SOFTEN" (1:25), "EXTRACT FOR FIRMER LOOKING SKIN" (1:27). No "$" price graphic for LUXE. |
| 1:28–1:33 | **Result claim and demo:** "It reduces the look of wrinkles by 30% in four weeks. It does the same job for way less." | 1:29–1:31: cutaway to a different person, a brunette woman (about 40s, reading) in a black ribbed tank top in a bathroom/home, rubbing a light-blue stick under her eye (cap end printed roughly "HB EXP202905-10"), then pointing at her under-eye. Captions: "IT REDUCES THE LOOK" (1:29), "IN FOUR WEEKS" (1:31). 1:33: back to the avatar in the store with two **BEFORE / AFTER** insets top right: a full face of a woman (about 50s, reading) with a headband, and an eye-area close-up, each labelled "BEFORE" and "AFTER". |
| 1:33–1:48 | **CTA** (see CTA) | 1:35: avatar in the store, caption "REGRET IT". By 1:37 he is filming a selfie in the driver's seat of a car, seatbelt on, holding the LUXE tube to camera (1:37–1:41). Captions: "AMAZON THAN ANYWHERE ELSE" (1:37), "SEARCH LUX OR CLICK" (1:39), "ON FACEBOOK" (1:41), "COMMENT DM BELOW" (1:43), "THE LINKS TO EVERYTHING" (1:45), "FOLLOWING ME FIRST SO" (1:47). |

**Rehooks / open loops**
- 0:04: "And if you're over 50, you're gonna want to save this list." (save instruction plus age call-out)
- 0:06: "Let's go."
- 0:33: "Fun fact, the same company owns both." (insider aside)
- 1:04: "Okay, but I saved the best dupe for last." (main open loop; bridges to the product)
- 1:42: "Comment DM below, and I'll send you the links to everything I just mentioned." (rewards watching the whole list)
- Caption (not spoken): "the under-eye secret nobody told you about 👀" primes a payoff that only comes at the end.

### PRODUCT
- **Product sold:** eye balm (under-eye stick balm), brand LUXE. Spoken: "Luxe makes a Korean under-eye balm" (1:19). Tube print (1:23, partly garbled): "Luxe Fundet unten eye Balm", "50 mL ·1Z oz" (approximate reading of small text). Brand reads "Luxe" on tube and boxes; burned caption misspells it "LUX" at 1:39 ("SEARCH LUX OR CLICK"). The transcript's "Luxe" matches the pack.
- **First appears:** spoken 1:19.56 ("Luxe makes a Korean under-eye balm…"); on screen in the 1:21 frame (first sampled frame after 1:19): a hand holds the pale-blue LUXE tube in front of a shelf stocked with LUXE boxes and tubes. (The cart in the store selfies from 0:00 holds plain white/pale boxes that are not identifiable as LUXE.)
- **Bridge line (verbatim):**
  - "Okay, but I saved the best dupe for last." (1:04.04)
  - "If you've seen Chanel's number one revitalizing eye cream, it's lovely, but it's $85 for a tiny jar. One of its key ingredients is adenosine." (1:05.72–1:13.16)
  - "Luxe makes a Korean under-eye balm with that same adenosine…" (1:19.56)
- **Saved for last?** Yes: item 7 of 7. Loop opens 1:04, Chanel setup 1:05, LUXE named 1:19 of 1:48. The product holds the last 28 s; with the setup, the last 43 s.
- **Product shots:**
  - Hand-held tube in front of a full LUXE bay: 1:21, 1:23 (close, label legible), 1:25, 1:27.
  - Application demo by a different woman: 1:29–1:31.
  - Before/after insets (face and eye area): 1:33.
  - Avatar holds the tube up in the car: 1:37–1:41.
  - Tube: slim matte pale-blue cylinder, "Luxe" printed vertically. Boxes: darker blue, "Luxe" printed vertically.
  - **No LUXE price is said or shown** as a "$" tag. Only background shelf labels (e.g. "14.99", "11.99") sit near it.

### CTA
- **Spoken:**
  - "If you want to give it a try, I don't think you'll regret it." (1:33.34)
  - "It's way cheaper on Amazon than anywhere else." (1:35.50)
  - "Search Luxe or click the link in my bio." (1:37.90)
  - "And if you're watching on Facebook, the link will be in the comments." (1:40.18)
  - "Comment DM below, and I'll send you the links to everything I just mentioned." (1:42.74)
  - "Just make sure you're following me first so I can message you." (1:46.22)
- **On-screen text:**
  - Burned captions: "REGRET IT" (1:35), "AMAZON THAN ANYWHERE ELSE" (1:37), "SEARCH LUX OR CLICK" (1:39), "ON FACEBOOK" (1:41), "COMMENT DM BELOW" (1:43), "THE LINKS TO EVERYTHING" (1:45), "FOLLOWING ME FIRST SO" (1:47).
  - Large white '"DM"' graphic with two red arrows pointing down (toward the comments), bottom-right quarter, in the 1:43 and 1:45 frames; absent at 1:41 and 1:47.
  - Post caption repeats it: 'Comment "DM" for all my picks 💌'.
- **Where it points:** four routes at once: (1) Amazon search "Luxe"; (2) "link in my bio"; (3) a link in the Facebook comments; (4) a "comment DM" keyword that triggers a DM, gated on following first ("make sure you're following me first so I can message you").

### AVATAR
- **Who:** peer shopper persona, not a stated expert; no credentials claimed. The only borrowed authority is "the vitamin C serum dermatologists love" (0:37), about a competitor product, not about him.
  - Man, East Asian in appearance, about 40s to early 50s (reading).
  - Neat dark side-parted hair; thin round gold wire-frame glasses.
  - White button-down oxford shirt with a chest pocket; DJI lav mic clipped on.
  - Page name "Jiho Beauty" is a Korean given name, which fits "Korean under-eye balm" (reading).
- **Setting and lighting:**
  - 0:00–1:35: Target aisle (red walls, bullseye signage, red cart), handheld; selfie for face shots, first-person POV for product shots; flat fluorescent light.
  - 1:37–1:47: parked car, driver's seat, seatbelt on, handheld selfie, soft daylight, brick building outside.
- **Real or AI-looking (my reading, from what is visible):**
  - **"syntheticmedia" watermark (measured):** small white lowercase text with a thin dark outline, lower-left, about 83% of the way down the frame (about x 30–165, y 700–715 on the 480×854 extracted frames). Present in **all 57 sampled frames, 0:00–1:47**: store selfies, product POV, the demo woman, the before/after shot and the car. Legible if you look for it; far smaller than the captions; static. On a phone feed it reads as a faint creator tag rather than a disclosure (reading).
  - **Garbled packaging text** (typical of AI image/video generation, reading):
    - e.l.f. sunscreen, 0:21: "EUNTOUCHABLE", "BVOBE WACTINAL IOP DE SUNSCREEN", "INVIDR HENSTANT LES PANOTEN", "STONE + POINCE".
    - e.l.f. serum, 0:41: "ERIGHT ICON", "70% Vitamin C", "11 5% Ferulic sera" (approximate).
    - LUXE tube, 1:23: "Luxe Fundet unten eye Balm", "50 mL ·1Z oz".
  - **Face changes between scenes (reading):** the face in the car (1:37–1:47) looks narrower, with a different hairline and features, from the store face (0:00–1:35): a different render or a different person under the same styling.
  - **Implausible shelf (reading):** a full Target bay of "Luxe" boxes and tubes with shelf tags looks generated or composited, and conflicts with "way cheaper on Amazon than anywhere else".
  - POV shots keep a consistent white cuff. Lip-sync can't be judged from stills.
  - **Probably real stock/UGC (reading):** the 1:29–1:31 demo (real skin texture, red eye rims, printed lot code on the cap) and the before/after photos.
- **Delivery:** fast list rhythm, about one swap every 8–9 s; casual. Profanity in the first words: "Cheap shit from Target". Asides: "Fun fact", "Okay, but", "it's lovely", "I don't think you'll regret it". Praises each luxury brand before undercutting it ("La Mer is gorgeous, but…", "Lancôme Genifique is beautiful, but…").
- **Who else appears:** hands holding every product (presented as his, white cuff); an unnamed brunette woman applying the balm (1:29–1:31); an unnamed woman (about 50s) in the full-face before/after, plus an eye-area before/after that may or may not be the same woman (1:33); luxury product photos as thumbnails.

### CLAIMS & COMPLIANCE
- "Cheap shit from Target that's just as good, if not better, than the luxury stuff." (0:00); headline "BETTER THAN LUXURY" (0:01–0:05)
- "La Mer at $200" (0:07); "Fourteen of its sixteen ingredients are in La Mer. Almost in the same order." (0:09); "Nivea is ten bucks for a huge tub" (0:12)
- Supergoop Unseen vs e.l.f.: "Same four sun filters, goes on clear, works like a primer, $15, not $38." (0:19)
- "SK-II Skin Power Cream is $170" (0:24); Olay "shares 23 ingredients with it. Same firming peptide, same niacinamide." (0:27–0:33); "Fun fact, the same company owns both." (0:33); "Olay is $24" (0:35)
- SkinCeuticals CE Ferulic is "the vitamin C serum dermatologists love, but it's $185" (0:37); e.l.f. Bright Icon "has the same big three. Vitamin C, vitamin E, ferulic acid, $17." (0:41–0:46)
- "Estee Lauder Advanced Night Repair at $88" (0:46); e.l.f. Youth Boosting: "Seventeen of the same ingredients, plus a retinoid for fine lines, $23." (0:52)
- "Lancôme Genifique… it's over $200." (0:55); "L'Oréal owns Lancôme, and their Revitalift serum has the same active ingredients." (0:58)
- Chanel N°1 eye cream: "$85 for a tiny jar" (1:05); "One of its key ingredients is adenosine." (1:11)
- "Adenosine is a molecule your body naturally makes, and in skincare, it helps smooth wrinkles." (1:13–1:19)
- LUXE: "Korean under-eye balm with that same adenosine, plus hyaluronic acid to plump, argan oil to soften, and PDRN and collagen extract for firmer looking skin." (1:19–1:28)
- **"It reduces the look of wrinkles by 30% in four weeks."** (1:28). No source, study or footnote shown.
- **"It does the same job for way less."** (1:31). Comparative claim vs Chanel; no LUXE price given.
- "It's way cheaper on Amazon than anywhere else." (1:35). Price-comparison claim.
- "I don't think you'll regret it." (1:33)
- Before/after images (1:33): no timeframe, product attribution or "results may vary" label visible.
- Testimonial/"client" stories: none said. Implied credentials: none for the avatar; "dermatologists love" applied to a competitor (0:37).
- **"Ad" labels:** caption begins "AD |", so the page title line reads "89K views · 1.2K reactions | AD | These cheap Target finds…". No "ad", "#ad", "sponsored" or "paid partnership" text on screen in any of the 57 sampled frames. Facebook "Sponsored"/"Paid partnership" label: not found in metadata.
- **AI disclosure:** only the small "syntheticmedia" watermark, lower-left, every sampled frame (see AVATAR). No spoken or caption AI disclosure; no Facebook "AI info" label found in metadata.
- **Risk notes (my reading):**
  - "30% in four weeks" needs clinical substantiation.
  - "Does the same job" as Chanel is a comparative efficacy claim against a named brand.
  - Before/after imagery may not be of this product or a real user.
  - Ingredient-count claims about named third-party brands (14 of 16, 23, 17), "same company owns" and "same active ingredients" must be accurate.
  - "Way cheaper on Amazon than anywhere else" needs price proof.
  - Profanity ("Cheap shit") in both spoken hook and headline.
  - Framing a paid Amazon product as one of the "Target finds", shown on what looks like a Target shelf, could mislead about where it is sold.
  - If the presenter is AI-generated, a small watermark may not be clear disclosure; a synthetic "real shopper" endorsement raises FTC endorsement-guide questions (reading only).

### WHY IT WORKS
Six real, recognisable drugstore swaps with big price gaps ($200→$10, $185→$17) earn trust and a "save this list" reflex, so the 7th "dupe" borrows that credibility without feeling like an ad.
The "best dupe for last" loop plus the Chanel→adenosine→LUXE ingredient bridge makes the pitch feel like the list's payoff, and a four-way CTA (Amazon search, bio, comments, comment-DM with follow gate) catches every kind of viewer.

### OBSERVER NOTES (optional)
- **Measured:** same ad, four posts on one page, decaying with each repost: 15 (Oct 7) 650,286; 13 (Oct 11) 111,727; 14 (Oct 11) 102,119; 12 (Oct 12) 45,530 view_count. Video 12 got about 7% of 15's views. Title-line figures: 15 "1.1M views · 18K reactions" vs 12 "89K views · 1.2K reactions".
- **Measured:** for 12, the title-line "89K views" is about 2× its view_count (45,530). The same gap pattern shows on 15 (1.1M vs 650,286), so the two counters measure different things; which one Facebook ranks on is not found.
- **Measured:** transcript spellings corrected from pack/captions: "Regeneris" → Regenerist (pack); "Skinceutical" → SkinCeuticals; "retinoid" → captions say "RETINOL"; "Luxe" (spoken, pack) vs "LUX" (caption).
- **Reading:** the hook names Target, but the buying route is Amazon; the ad gets the store's "cheap find" credibility without the product being sold there.
- **Reading:** reposting an identical creative a day after two other reposts shows the page testing re-uploads rather than new creative; returns fell sharply.

### DIFFERENCES FROM VIDEO 15
**Result: no visible difference found. Video 12 is the same edit as video 15, re-encoded.**

Visual check (measured): I viewed all 8 contact sheets of 12 and all 8 of 15 side by side (57 sampled frames each, 0:00–1:47). Every sampled frame matches on each point:

| Checked | 12 vs 15 |
|---|---|
| Presenter/avatar | Same man, same white oxford shirt, glasses, DJI mic; same poses and expressions frame for frame (e.g. mouth open at 0:00, open-hand gesture at 1:11, smile at 1:43). The same store-vs-car face change (1:35 → 1:37) is in both. |
| Setting | Same Target aisle and cart (0:00–1:35), same car (1:37–1:47), same demo bathroom (1:29–1:31). |
| Headline / sub-headline | Same "CHEAP SHIT FROM 🎯 TARGET THAT'S BETTER THAN LUXURY" / "A must-have for women over 50+", same window 0:01–0:05. |
| Burned captions | Same words in every sampled frame, including the "$15 NOT 38SK2" run-on (0:23) and "SEARCH LUX OR CLICK" (1:39). |
| Product shots | Same Nivea, e.l.f. ×3, Olay, L'Oréal, LUXE shots, same hand positions, same garbled pack text. |
| Price tags | Same tags and the same animation states in the same frames: "$200" from 0:09; "$38"; "$17"→"$170" (0:27→0:29); "$185" from 0:43; "$8"→"$88" (0:49→0:51); "$200" from 0:59; "$85" from 1:11. |
| Hook visual | Same selfie walk with cart, same framing. |
| Before/after insets | Same two insets at 1:33. |
| "DM" arrow graphic | Same, 1:43 and 1:45 only. |
| "syntheticmedia" watermark | Same text, same lower-left position, present in all 57 frames of both. |
| Cut timing | Same cuts at the same sampled times (store→Nivea between 0:05 and 0:07; →e.l.f. 0:15–0:17; →Olay 0:23–0:25; →e.l.f. serum 0:37–0:39; →ANR 0:45–0:47; →Revitalift 0:55–0:57; →selfie 1:03–1:05; →LUXE 1:19–1:21; →demo 1:27–1:29; →store 1:31–1:33; →car 1:35–1:37). Both have exactly 3,255 frames. |

Pixel check (measured, ffmpeg + numpy):
- Frame-by-frame SSIM between 12.mp4 and 15.mp4 over all 3,255 frames: mean 0.9965, lowest 0.9897 (around 1:28–1:31, the noisy demo clip). A changed caption, price or face would push SSIM far lower in that stretch.
- Difference images at 2 fps (217 frame pairs, 540×960): the largest 20×20-pixel block difference anywhere is 8 out of 255 (mean whole-frame difference about 1/255). That is compression noise, not an edited element; an added or changed text overlay would give block differences in the tens or hundreds.
- The 57 extracted frame JPGs of 12 vs 15: largest 16×16 block difference 7.7/255 (t105.jpg).

Why the file differs (measured with ffprobe and md5):

| | 12.mp4 | 15.mp4 |
|---|---|---|
| File size | 17,190,365 bytes | 18,784,636 bytes |
| MD5 (whole file) | ad38eed987fb456d4771e68588144ffd | 03de931e12d082279e338ea69d089d43 |
| Video | AV1 Main, 1080×1920, 30 fps, 3,255 frames, encoder tag "AOM Coding" | same |
| Video bitrate | 1,196,744 bit/s (yt-dlp tbr 1197.962) | 1,314,294 bit/s (tbr 1315.512) |
| Audio | HE-AAC, 44.1 kHz stereo, 65,910 bit/s | same |
| Audio stream MD5 (stream copy) | ab4434e28bd5a3bcb2cf2172c6f10a5b | ab4434e28bd5a3bcb2cf2172c6f10a5b (identical) |
| Container | isom/av01, muxer Lavf60.16.100 | same |
| Duration | 108.508005 s | 108.508005 s |
| Facebook format IDs | 1773000373985320v + 1772922397326451a | 1120432520500446v + 1117140107496354a |

Reading: the audio is bit-identical and the picture matches frame for frame, but the AV1 video stream differs (about 9% lower bitrate on 12). This is what you get when the same source file is uploaded again as a new post: Facebook runs its own AV1 transcode for each upload, and the encoder settles on a slightly different bitrate. 13, 14 and 15 happen to be byte-identical (per 15.md); 12 is the one post whose transcode came out differently. There is no sign of a re-edit, a different presenter or changed text. Whether the page uploaded a fresh export (e.g. re-rendered with the same settings) or the identical file can't be told from what Facebook serves; the identical audio suggests the same source.

---

## Video 13 — Jiho Beauty — same file as video 15 (re-post)
**Link:** https://www.facebook.com/share/v/1DwtLuy5BL/ (video ID 1104086958770697) · **Page:** Jiho Beauty · **Uploaded:** 2026-10-11 22:01 UTC · **Duration:** 108.5 s · **Views:** view_count 111,727 (page title line says "203K views · 3.5K reactions") · **Comments:** not found
**Caption (verbatim):** "AD | These cheap Target finds beat luxury, and the under-eye secret nobody told you about 👀 Comment "DM" for all my picks 💌

#usa #skincare #matureskin #maturewoman #skincareroutine"

**Measured:** `videos/13.mp4` is byte-identical to `videos/15.mp4` (same size and MD5), so the hook, format, body, product, CTA, avatar and claims are exactly as in the **Video 15** section; read that section for the full breakdown. The transcript is saved as `transcripts/13.txt` (a copy of 15's). The caption is identical to video 15's caption.
**Performance against the other post:** video 15: view_count 650,286 ("1.1M views · 18K reactions"), uploaded 2026-10-07 16:49 UTC. Video 13: view_count 111,727 ("203K views · 3.5K reactions"), uploaded 2026-10-11 22:01 UTC.

---

## Video 14 — Jiho Beauty — same file as video 15 (re-post)
**Link:** https://www.facebook.com/share/v/1Kc2NwWeat/ (video ID 1725073855253851) · **Page:** Jiho Beauty · **Uploaded:** 2026-10-11 16:16 UTC · **Duration:** 108.5 s · **Views:** view_count 102,119 (page title line says "191K views · 3K reactions") · **Comments:** not found
**Caption (verbatim):** "AD | These cheap Target finds beat luxury, and the under-eye secret nobody told you about 👀 Comment "DM" for all my picks 💌

#usa #skincare #matureskin #maturewoman #skincareroutine"

**Measured:** `videos/14.mp4` is byte-identical to `videos/15.mp4` (same size and MD5), so the hook, format, body, product, CTA, avatar and claims are exactly as in the **Video 15** section; read that section for the full breakdown. The transcript is saved as `transcripts/14.txt` (a copy of 15's). The caption is identical to video 15's caption.
**Performance against the other post:** video 15: view_count 650,286 ("1.1M views · 18K reactions"), uploaded 2026-10-07 16:49 UTC. Video 14: view_count 102,119 ("191K views · 3K reactions"), uploaded 2026-10-11 16:16 UTC.

---

## Video 15 — Jiho Beauty — "Cheap shit from Target that's better than luxury"
**Link:** https://www.facebook.com/share/v/1Bi7GsR1MQ/ (video ID 2071496550177997) · **Page:** Jiho Beauty · **Uploaded:** 2026-10-07 (16:49:50 UTC, from info.json `timestamp`) · **Duration:** 1:48 (108.5 s) · **Views:** view_count 650,286 (page title line says "1.1M views") · **Reactions:** "18K reactions" (from title line) · **Comments:** not found (comment_count empty in metadata)
**Caption (verbatim):** "AD | These cheap Target finds beat luxury, and the under-eye secret nobody told you about 👀 Comment "DM" for all my picks 💌

#usa #skincare #matureskin #maturewoman #skincareroutine"

**Master breakdown for videos 13, 14 and 15 (measured).** 13.mp4, 14.mp4 and 15.mp4 are the same file: same size (18,784,636 bytes) and same MD5 (03de931e12d082279e338ea69d089d43). Same page, same caption. Video 15 is the earliest and biggest post:

| # | Upload (UTC) | view_count | Title line |
|---|---|---|---|
| 15 | 2026-10-07 | 650,286 | "1.1M views · 18K reactions" |
| 13 | 2026-10-11 | 111,727 | "203K views · 3.5K reactions" |
| 14 | 2026-10-11 | 102,119 | "191K views · 3K reactions" |

All three together: view_count 864,132; title-line figures add up to about 1.49M views and about 24.5K reactions. Video 12 has the same caption and the same 108.5 s length, but it is a different file (MD5 ad38eed9…). It is not covered here. Metadata was pulled 2026-11-07 (videos/METADATA.md).

### HOOK (0:00–0:05)
- **Spoken:** "Cheap shit from Target that's just as good, if not better, than the luxury stuff." (0:00–0:04) / "And if you're over 50, you're gonna want to save this list." (0:04–0:06) / "Let's go." (0:06–0:07)
- **On-screen text:**
  - Headline, 0:01–0:05 (not in the 0:00 frame, gone by 0:07). White heavy caps with a dark outline, at the top of the frame: "CHEAP SHIT FROM 🎯 TARGET THAT'S BETTER THAN LUXURY". The 🎯 emoji echoes Target's bullseye.
  - Sub-headline, 0:01–0:05, pink, sentence case: "A must-have for women over 50+".
  - Burned-in captions, word by word in white condensed caps, with one word at a time on a black box:
    - "CHEAP SHIT FROM TARGET" (0:00, 0:01)
    - "THAT'S JUST AS GOOD" (0:02)
    - "IF NOT BETTER THAN" (0:03)
    - "THE LUXURY STUFF" (0:04)
    - "50 YOU'RE GONNA WANNA" (0:05)
  - The headline says "BETTER THAN LUXURY". The spoken line is softer: "just as good, if not better".
- **Visual:** The avatar walks in a selfie shot, held at arm's length, chest-up, down a Target health and beauty aisle. You can see red walls, a Target bullseye aisle sign, white shelves of skincare and fluorescent ceiling lights. He pushes a red Target cart holding several plain white boxes. A black DJI wireless lav mic with a furry windscreen is clipped to his shirt. He talks straight to camera with raised eyebrows.

### FORMAT
**A Target "dupes for luxury" swap list, with the sponsored product slotted in as "the best dupe saved for last."**
The page lists 6 real drugstore swaps, each set against a named luxury product with a price tag: Nivea, e.l.f. ×3, Olay and L'Oréal. Then the 7th "dupe" is LUXE's under-eye balm, set against Chanel and introduced with the same ingredient-overlap logic.

### BODY (beats)
| Time | Beat (what's said, quoted) | On-screen (text overlays, product shots, price tags, before/afters) |
|---|---|---|
| 0:07–0:15 | **Swap 1:** "Instead of La Mer at $200, grab Nivea Creme. Fourteen of its sixteen ingredients are in La Mer. Almost in the same order. La Mer is gorgeous, but Nivea is ten bucks for a huge tub." | A first-person hand (white shirt cuff) holds the blue Nivea Creme tin in a Target aisle stocked with Nivea. Top left: a thumbnail of the La Mer jar, then a pink outlined "$200" tag (shown by 0:09). Captions include "INSTEAD OF LA MER", "GRAB NIVEA CREAM", "INGREDIENTS ARE IN LA MER", "LA MER IS GORGEOUS", "BUCKS FOR A HUGE TUB". No price tag for Nivea; its price is only spoken. |
| 0:15–0:24 | **Swap 2:** "If you love Supergoop Unseen, try Elf Sun Touchable Invisible. Same four sun filters, goes on clear, works like a primer, $15, not $38." | The hand holds an e.l.f. SKIN invisible sunscreen tube, SPF 35, in front of a sunscreen shelf. Top left: a Supergoop tube thumbnail on a yellow background and "$38". Captions: "IF YOU LOVE SUPERGOOP UNSEEN", "TRY ELF SUN TOUCHABLE INVISIBLE", "GOES ON CLEAR WORKS", "$15 NOT 38SK2" (the caption runs into the next line). |
| 0:24–0:37 | **Swap 3:** "SK-II Skin Power Cream is $170. Olay Regeneris[t] Micro-Sculpting Cream shares 23 ingredients with it. Same firming peptide, same niacinamide. Fun fact, the same company owns both. Olay is $24." | The hand holds a red Olay Regenerist Micro-Sculpting Cream jar (the pack spells it "REGENERIST") in front of an Olay wall. Top left: an SK-II Skinpower red jar thumbnail. Its tag animates in: "$17" at 0:27, "$170" from 0:29. Captions: "SKIN POWER CREAM IS $170", "OLAY REGENERIST MICRO SCULPTING", "CREAM SHARES 23 INGREDIENTS", "SAME FIRMING PEPTIDE SAME NIACINAMIDE", "THE SAME COMPANY OWNS BOTH", "OLAY IS 24 BUCKS". |
| 0:37–0:46 | **Swap 4:** "Skinceutical[s] CE Ferulic is the vitamin C serum dermatologists love, but it's $185. Elf Bright Icon has the same big three. Vitamin C, vitamin E, ferulic acid, $17." | The hand holds an orange e.l.f. "Bright Icon Vitamin C + E + Ferulic Serum" in a cosmetics aisle. Top left: a SkinCeuticals C E Ferulic dropper bottle thumbnail, with "$185" shown by 0:43. Captions: "IS THE VITAMIN C", "BUT IT'S $185 ELF", "BRIGHT ICON HAS THE", "FERULIC ACID $17". |
| 0:46–0:55 | **Swap 5:** "Instead of Estee Lauder Advanced Night Repair at $88, try Elf Youth Boosting Night Retinoid Serum. Seventeen of the same ingredients, plus a retinoid for fine lines, $23." | The hand holds a lavender e.l.f. SKIN "Youth Boosting" pump bottle. Top left: an Estée Lauder ANR bottle thumbnail. Its tag shows "$8" at 0:49 (mid-animation) and "$88" from 0:51. Captions: "INSTEAD OF ESTEE LAUDER", "ADVANCED NIGHT REPAIR AT $88", "NIGHT RETINOL SERUM", "INGREDIENTS PLUS A RETINOL", "$23". The captions say "RETINOL"; the transcript hears "retinoid". |
| 0:55–1:04 | **Swap 6:** "Lancôme Genifique is beautiful, but it's over $200. L'Oréal owns Lancôme, and their Revitalift serum has the same active ingredients. Get this one instead." | The hand holds a L'Oréal Revitalift Hyaluronic Acid 1.5% serum in front of a Revitalift shelf with red "Sale" tags. Top left: a Lancôme Génifique bottle thumbnail and "$200". Captions: "LANCOME GENIFIQUE IS BEAUTIFUL", "L'OREAL OWNS LANCOME", "AND THEIR REVITALIFT SERUM", "GET THIS ONE INSTEAD". No price for Revitalift is said or shown as a tag. |
| 1:04–1:05 | **Rehook:** "Okay, but I saved the best dupe for last." | Cut back to the avatar's selfie in the aisle with the cart. Caption: "THE BEST DUPE FOR LAST". |
| 1:05–1:19 | **Luxury setup for item 7:** "If you've seen Chanel's number one revitalizing eye cream, it's lovely, but it's $85 for a tiny jar. One of its key ingredients is adenosine. Adenosine is a molecule your body naturally makes, and in skincare, it helps smooth wrinkles." | Avatar selfie in the store. Top right: a thumbnail of the Chanel N°1 eye cream jar, with "$85" from 1:11. He gestures with an open hand at 1:11. Captions: "NO. 1 REVITALIZING EYE CREAM", "IT'S LOVELY", "A TINY JAR", "ADENOSINE IS A MOLECULE", "AND IN SKINCARE IT", "HELPS SMOOTH WRINKLES". |
| 1:19–1:28 | **Item 7, the sponsored product:** "Luxe makes a Korean under-eye balm with that same adenosine, plus hyaluronic acid to plump, argan oil to soften, and PDRN and collagen extract for firmer looking skin." | The hand holds a pale-blue LUXE stick tube ("Luxe" printed vertically). Behind it the top shelf holds blue "Luxe" boxes with Target-style shelf tags (17.99 / 12.99 / 11.99 / 14.99); the lower shelves hold beige, lavender and teal tubes with a garbled brand label. Captions: "UNDER EYE BALM WITH", "PLUS HYALURONIC ACID TO PLUMP", "ARGAN OIL TO SOFTEN", "EXTRACT FOR FIRMER LOOKING SKIN". There is no "$" price tag graphic for LUXE. |
| 1:28–1:33 | **Result claim and demo:** "It reduces the look of wrinkles by 30% in four weeks. It does the same job for way less." | 1:29–1:31: a cutaway to a different person. A brunette woman, about 40s, in a black tank top in a bathroom, rubs a light-blue stick (cap end printed "HB EXP202905-10" (as best it can be read)) under her eye, then points at her under-eye. Captions: "IT REDUCES THE LOOK", "IN FOUR WEEKS". 1:33: back to the avatar in the store, with two **BEFORE / AFTER** insets at top right. One is a full face of a woman, about 50s, with a headband; the other is a close-up of an eye area. Both are labelled "BEFORE" and "AFTER". |
| 1:33–1:48 | **CTA** (see the CTA section) | 1:35: the avatar in the store; caption "REGRET IT". By 1:37 he is filming a selfie in the driver's seat of a car with his seatbelt on, holding the LUXE tube up to camera. Captions: "AMAZON THAN ANYWHERE ELSE", "SEARCH LUX OR CLICK", "ON FACEBOOK", "COMMENT DM BELOW", "THE LINKS TO EVERYTHING", "FOLLOWING ME FIRST SO". |

**Rehooks and open loops**
- 0:04: "And if you're over 50, you're gonna want to save this list." (an instruction to save, plus an age call-out)
- 0:06: "Let's go."
- 0:33: "Fun fact, the same company owns both." (an insider aside)
- 1:04: "Okay, but I saved the best dupe for last." (the main open loop; it bridges to the product)
- 1:42: "Comment DM below, and I'll send you the links to everything I just mentioned." (rewards watching the whole list)
- Caption (not spoken): "the under-eye secret nobody told you about 👀". This primes a payoff that comes only at the end.

### PRODUCT
- **Product sold:** an eye balm (under-eye stick balm) from LUXE. Spoken: "Luxe makes a Korean under-eye balm" (1:19). The tube print is partly garbled (see AVATAR): "Luxe Fun[?]set unten eye Balm", "50 mL ·1Z oz". The brand reads "Luxe" on the tube and the boxes. The burned caption misspells it "LUX" at 1:39 ("SEARCH LUX OR CLICK").
- **First appears:** spoken at 1:19.56 ("Luxe makes a Korean under-eye balm…"). On screen in the 1:21 frame (first sampled frame after 1:19): a hand holds the pale-blue LUXE tube in front of a shelf stocked with LUXE boxes.
- **Bridge line (verbatim):**
  - "Okay, but I saved the best dupe for last." (1:04.04)
  - "If you've seen Chanel's number one revitalizing eye cream, it's lovely, but it's $85 for a tiny jar. One of its key ingredients is adenosine." (1:05.72–1:13.16)
  - "Luxe makes a Korean under-eye balm with that same adenosine…" (1:19.56)
- **Saved for last?** Yes. It is item 7 of 7. The "best dupe" loop opens at 1:04, the Chanel setup starts at 1:05, and LUXE is named at 1:19 of a 1:48 video. The product sits in the last 28 s; counting the setup, the last 43 s.
- **Product shots:**
  - Hand-held stills of the tube in front of a full LUXE shelf: 1:21, 1:23 (close, label legible), 1:25 and 1:27.
  - Application demo by a different woman in a bathroom: 1:29–1:31.
  - Before/after insets of a face and of an eye area: 1:33.
  - The avatar holds the tube up in the car: 1:37–1:41.
  - The tube is a slim, matte pale-blue cylinder with "Luxe" printed vertically. The boxes are darker blue, also with "Luxe" printed vertically.
  - **No LUXE price is said or shown** as a "$" tag graphic. The only prices near it are shelf labels in the background ("14.99", "11.99").

### CTA
- **Spoken:**
  - "If you want to give it a try, I don't think you'll regret it." (1:33.34)
  - "It's way cheaper on Amazon than anywhere else." (1:35.50)
  - "Search Luxe or click the link in my bio." (1:37.90)
  - "And if you're watching on Facebook, the link will be in the comments." (1:40.18)
  - "Comment DM below, and I'll send you the links to everything I just mentioned." (1:42.74)
  - "Just make sure you're following me first so I can message you." (1:46.22)
- **On-screen text:**
  - Burned captions: "REGRET IT" (1:35), "AMAZON THAN ANYWHERE ELSE" (1:37), "SEARCH LUX OR CLICK" (1:39), "ON FACEBOOK" (1:41), "COMMENT DM BELOW" (1:43), "THE LINKS TO EVERYTHING" (1:45), "FOLLOWING ME FIRST SO" (1:47).
  - A large white graphic, '"DM"' with two red arrows pointing down (toward the comment area), sits in the bottom-right quarter in the 1:43 and 1:45 frames. It is absent at 1:41 and 1:47.
  - The caption repeats it: 'Comment "DM" for all my picks 💌'.
- **Where it points:** several destinations at once.
  1. Amazon search "Luxe".
  2. "link in my bio".
  3. A link in the Facebook comments.
  4. A "comment DM" keyword that triggers a DM, gated on following the page first ("make sure you're following me first so I can message you").

### AVATAR
- **Who:** a peer shopper persona, not a stated expert. He claims no credentials. The only authority borrowed is "the vitamin C serum dermatologists love" (0:37), which is about the product, not about him.
  - Man, East Asian in appearance, about 40s to early 50s (reading).
  - Neat dark side-parted hair; thin round gold/clear wire-frame glasses.
  - Crisp white button-down oxford shirt with a chest pocket.
  - DJI lav mic clipped to his shirt.
  - The page name "Jiho Beauty" is a Korean given name, which fits with "Korean under-eye balm" (reading).
- **Setting and lighting:**
  - 0:00–1:35: a Target store aisle (red walls, bullseye signage, red cart), filmed handheld. Selfie for the face shots; first-person point-of-view for the product shots. Flat fluorescent store light.
  - From about 1:36 (by the 1:37 frame): a parked car, driver's seat, seatbelt on, handheld selfie, soft daylight from the windows, a brick building outside.
- **Real or AI-looking (my reading, based on what is visible):**
  - **"syntheticmedia" watermark (measured):** small white lowercase text with a thin dark outline, in the lower-left of the frame. It sits about 4% in from the left edge and about 83% of the way down (about x 30–165, y 700–712 on the 480×854 extracted frames). It appears in **every one of the 57 sampled frames, 0:00–1:47**: store selfie, product point-of-view, the demo woman, the before/after shot and the car. Visibility: legible if you look for it. It is roughly the size of a phone status-bar label, much smaller than the captions, and not animated. On a phone feed it would read as a faint creator tag rather than a disclosure (reading).
  - **Garbled packaging text** (a typical sign of AI image or video generation, reading):
    - e.l.f. sunscreen at 0:21: "EUNTOUCHABLE", "BVOBE WACTINAL IOP DE SUNSCREEN", "INVIDE HENSTANT LES PANOTEN", "STORE + POINGS".
    - e.l.f. Bright Icon at 0:41: "ERIGHT ICON", "70% Vitamin C", "11 5% Ferulic sers".
    - LUXE tube at 1:23: "Luxe Fun[f]set unten eye Balm", "50 mL ·1Z oz".
  - **The face changes between scenes (reading):** the face in the car (1:37–1:47) looks narrower, with different hairline and features, from the face in the store (0:00–1:35). It looks like a different render or a different person under the same styling.
  - **Implausible shelf (reading):** the top shelf of a Target-style bay is stocked with blue "Luxe" boxes (shelf tags 17.99 / 12.99 / 11.99 / 14.99); the lower shelves hold beige, lavender and teal tubes with a different, garbled brand label (fact-check correction). This looks generated or composited. Note it conflicts with the claim that the product is "way cheaper on Amazon than anywhere else".
  - The hand point-of-view shots keep a consistent white shirt cuff. Lip-sync can't be judged from stills.
  - **Probably real stock or UGC (reading):** the demo clip at 1:29–1:31 shows a real-looking skin texture, red eye rims and a printed lot code "HB EXP202905-10" (as best it can be read) on the stick's cap end. The before/after photos look the same.
- **Delivery:** fast, punchy list rhythm, about one swap every 8–9 s. Casual. Profanity in the very first words: "Cheap shit from Target". Conversational asides: "Fun fact", "Okay, but", "it's lovely", "I don't think you'll regret it". Compliments each luxury brand before undercutting it ("La Mer is gorgeous, but…", "Lancôme Genifique is beautiful, but…").
- **Who else appears:**
  - Hands holding every product (presented as his own: white cuff).
  - An unnamed brunette woman, about 40s, applying the balm (1:29–1:31).
  - An unnamed woman, about 50s, in the full-face before/after, and an eye-area before/after (1:33). That one may be the same woman as the full-face pair or someone else; it can't be told.
  - Luxury product photos as thumbnails.

### CLAIMS & COMPLIANCE
- "Cheap shit from Target that's just as good, if not better, than the luxury stuff." (0:00). Headline: "BETTER THAN LUXURY" (0:01–0:05).
- "La Mer at $200" (0:07); "Fourteen of its sixteen ingredients are in La Mer. Almost in the same order." (0:09); "Nivea is ten bucks for a huge tub" (0:12)
- Supergoop Unseen "$38" vs e.l.f.: "Same four sun filters, goes on clear, works like a primer, $15, not $38." (0:19)
- "SK-II Skin Power Cream is $170" (0:24); Olay "shares 23 ingredients with it. Same firming peptide, same niacinamide." (0:27–0:33); "Fun fact, the same company owns both." (0:33); "Olay is $24" (0:35)
- SkinCeuticals CE Ferulic is "the vitamin C serum dermatologists love, but it's $185" (0:37); e.l.f. Bright Icon "has the same big three. Vitamin C, vitamin E, ferulic acid, $17." (0:41–0:46)
- "Estee Lauder Advanced Night Repair at $88" (0:46); e.l.f. Youth Boosting: "Seventeen of the same ingredients, plus a retinoid for fine lines, $23." (0:52)
- "Lancôme Genifique… it's over $200." (0:55); "L'Oréal owns Lancôme, and their Revitalift serum has the same active ingredients." (0:58)
- Chanel N°1 eye cream: "$85 for a tiny jar" (1:05); "One of its key ingredients is adenosine." (1:11)
- "Adenosine is a molecule your body naturally makes, and in skincare, it helps smooth wrinkles." (1:13–1:19)
- LUXE "Korean under-eye balm with that same adenosine, plus hyaluronic acid to plump, argan oil to soften, and PDRN and collagen extract for firmer looking skin." (1:19–1:28)
- **"It reduces the look of wrinkles by 30% in four weeks."** (1:28). No source, study or footnote is shown.
- **"It does the same job for way less."** (1:31). A comparative claim against Chanel; no LUXE price is given.
- "It's way cheaper on Amazon than anywhere else." (1:35). A price-comparison claim.
- "I don't think you'll regret it." (1:33)
- Before/after images (1:33): no timeframe, product attribution or "results may vary" label is visible.
- Testimonial or "client" stories: none said.
- Implied credentials: none for the avatar. "dermatologists love" is applied to a competitor (0:37).
- **"Ad" labels:** the caption begins "AD |", so the page title line reads "… | AD | These cheap Target finds…". Nothing on screen in the video says "ad", "#ad", "sponsored" or "paid partnership" (none seen in any sampled frame). Whether Facebook showed a "Sponsored" or "Paid partnership" label: not found in the metadata.
- **AI disclosure:** only the "syntheticmedia" watermark, in the lower-left, small, on every frame (details under AVATAR). There is no spoken or caption disclosure that the presenter or footage is AI-generated, and no Facebook "AI info" label was found in the metadata.
- **Risk notes (my reading):**
  - The "30% in four weeks" result claim needs clinical substantiation.
  - "Does the same job" as Chanel is a comparative efficacy claim against a named brand.
  - The before/after imagery may not be of the product or of an actual user.
  - The ingredient-count claims about third-party brands (14 of 16, 23, 17) are factual comparative claims about named brands and need to be accurate. So do the "same company owns" and "same active ingredients" claims.
  - "Way cheaper on Amazon than anywhere else" needs price proof.
  - The "Cheap shit" profanity is in both the spoken hook and the headline.
  - Framing a paid product as one of the "Target finds" when the CTA sends people to Amazon, and showing it on what appears to be a Target shelf, could mislead about where it is sold.
  - If the presenter is AI-generated, a small watermark may not count as clear disclosure. Showing a synthetic "real shopper" endorsing a product raises endorsement and disclosure questions (FTC endorsement-guide territory; reading only).

### WHY IT WORKS
Six real, recognisable drugstore swaps with a big price gap ($200→$10, $185→$17) earn trust and a "save this list" reflex, so the 7th "dupe" borrows that credibility without feeling like an ad.
The "best dupe for last" loop plus the Chanel→adenosine→LUXE ingredient bridge makes the pitch feel like the payoff to the list, and a four-way CTA (Amazon search, bio, comments, comment-DM with a follow gate) catches every kind of viewer.

### OBSERVER NOTES (optional)
- **Measured:** this video's view_count (650,286) is about 6× each of its byte-identical reposts (13: 111,727; 14: 102,119), all posted within 4 days (Oct 7 → Oct 11). The first post did by far the best; the reposts still did 100K+ each.
- **Measured:** the luxury items get pink outlined "$" price tags that animate in (a "$17" → "$170" and "$8" → "$88" mid-frame). The cheap swaps get no tag graphic; their prices are only spoken or captioned. LUXE gets no price at all.
- **Measured:** the transcript spellings were corrected from the packaging and captions: "Regeneris" → Regenerist (pack); "Skinceutical" → SkinCeuticals (thumbnail); "Retinoid" → captions say "RETINOL"; "Sun Touchable" → the pack reads "…UNTOUCHABLE" (garbled, cut off); "Luxe" (spoken and pack) vs "LUX" (caption).
- **Reading:** the 6 non-LUXE swaps lean on e.l.f. (3 of 6). The format copies a known organic "Target dupes" trend, with a male Korean persona targeting "women over 50+". The caption's hashtags (#matureskin #maturewoman) confirm the target audience.
- **Reading:** the hook names Target, but the purchase route is Amazon. The ad gets the store's "cheap find" credibility without the product being sold there.

---

# Part 2: YouTube thumbnails

Views, likes, dates and lengths: NexLev `youtube_video_details`, pulled 2026-11-07. Images are in `thumbs/<ID>.jpg`; titles are in `thumbs/titles.txt`.

### T1. XKROvYsp0QM — "How to Treat Crepey Eyes Like a Dermatologist | Dr. Sam Ellis"
**Channel:** Dr. Sam Ellis · **Views:** 149,955 · **Likes:** 4,527 · **Published:** 2025-05-16 · **Length:** 18:50 (NexLev, pulled 2026-11-07) · **Image:** maxresdefault.jpg
- **Exact text:** "EYE CREAMS" (black on a yellow highlight bar), "WHAT REALLY WORKS" (huge black caps on white bars, two lines), "OMG!" (orange, hand-lettered, angled), "ACCORDING TO A DERMATOLOGIST" (black on a lilac box, bottom left).
- **Layout:** text stack on the left 60%; presenter's face on the right third. Under the headline, a two-panel **before/after** close-up of an older woman's crow's-feet (left: deep crinkled lines; right: smooth). An orange hand-drawn arrow points from "OMG!" at the "before" wrinkles. No product shown.
- **Face/expression:** a woman in her 30s with long blonde-brown hair, calm, knowing half-smile, head slightly tilted, index finger pointing at her own crow's-feet area. Composed, "trust me" look rather than shock.
- **Colours:** pale blush/cream background, black text, yellow + lilac label blocks, orange accent. Clean, clinical-but-friendly.
- **With the title:** the title promises a method ("Treat … Like a Dermatologist"); the thumbnail promises the verdict ("What REALLY works") plus proof (the before/after). The authority is said twice ("Dermatologist" in the title, "According to a dermatologist" on the image). The curiosity gap: *which* eye cream produced that after-shot? Neither the title nor the image names a product.

### T2. wgWdHoI9leI — "Best & Worst Korean Eye Creams 2026 (Tier List: Dark Circles, Wrinkles & Milia)"
**Channel:** CYoung · **Views:** 284,507 · **Likes:** 4,752 · **Published:** 2026-01-23 · **Length:** 14:56 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "BEST TO WORST" ("BEST TO" white with black outline, "WORST" yellow with black outline), across the full top width. The product labels are readable: Beauty of Joseon "Revive Eye Serum Ginseng + Retinal", K-Secret "SEOUL 1988 Eye Cream Retinal Liposome 4% + Fermented Bean", numbuzin "No.9 … Volumetox Eye Cream", AXIS-Y "Vegan Collagen …", "BLACK YUJA BEAN LIFTING AUTO EYE CREAM" (Heveblue), Mary & May "Tranexamic Acid + Glutathione Eye Cream", celimax "RETINAL SHOT Tightening Booster", SKIN1004 "Madagascar CENTELLA".
- **Layout:** a row of 8 cut-out eye-cream tubes fanned across the frame, 4 each side; the creator centred in front of them with both palms up in a "which one?" shrug. Flat grey background. No arrows, circles or before/after.
- **Face/expression:** a Korean woman, about 40, black bob, yellow jumper; mouth pressed in a sceptical, slightly unimpressed half-smile. It reads as "some of these are bad".
- **Colours:** neutral grey background so the white, cream, purple, green and brown packaging pops; the yellow jumper matches the yellow "WORST".
- **With the title:** the title is the format (a tier list, with 2026 for recency, and three named problems: dark circles, wrinkles, milia). The thumbnail stresses "WORST", the loss-aversion side, and shows real, recognisable K-beauty packs so viewers who own one click to see where theirs ranked.

### T3. 9vnKwyKh08Q — "Life Changing Under Eye CONCEALER HACK?!? Testing the VIRAL Aquaphor Concealer Hack Over 50!"
**Channel:** HotandFlashy · **Views:** 343,979 · **Likes:** 15,483 · **Published:** 2024-06-07 · **Length:** 16:07 (NexLev) · **Image:** hqdefault.jpg (maxres not available; 480×360 with letterbox)
- **Exact text:** "IWas NOT EXPECTING THAT!" (as rendered, "I" and "Was" run together): "IWas" and "NOT" in black, "EXPECTING THAT!" in red, all heavy condensed caps stacked on the right half.
- **Layout:** the presenter on the left holding an **Aquaphor Lip Repair** stick up to the camera (label readable: "Aquaphor LIP REPAIR Immediate Relief for very dry lips") and pointing at it with her other index finger. Text on the right. No before/after, arrows or circles.
- **Face/expression:** a woman in her 50s, blonde, wide-eyed, mouth open in an excited "can you believe it" surprise. Classic reaction face.
- **Colours:** pink gradient background, white/navy product, black + red text.
- **With the title:** the title names the hack and the audience ("Aquaphor Concealer Hack Over 50") and adds the doubt ("?!?"). The thumbnail withholds the result: "I was NOT expecting that!" with no verdict on whether it was good or bad. The cheap, familiar drugstore product in her hand plus the surprised face make viewers click to learn the outcome.

### T4. P0K6Eeo1biU — "What Korean Makeup Artists Use BEFORE Foundation to Make Women Over 60 Look 20 Years Younger"
**Channel:** Clemons Hays · **Views:** 479,061 · **Likes:** 4,925 · **Published:** 2026-09-19 · **Length:** 12:50 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "BEFORE" (white, black outline, huge), "FOUNDATION!" (white on a hot-pink/red rounded box with black outline).
- **Layout:** a salon scene. An older woman (about 60, blonde shoulder-length hair, black satin blouse) sits centre-frame; a young male makeup artist (curly hair, aviator glasses, dark blazer) stands behind her, holding a plain **unlabelled white bottle** in one hand and pressing a cotton pad to her cheek with the other. Her cheek shows a wet sheen. A white dashed arrow curves up toward the pad. Bulb-lit vanity mirror, brushes and white flowers behind.
- **Face/expression:** she is calm and composed with a closed-lip smile; he is focused on the work.
- **Colours:** warm cream/gold salon, black clothing, pink/red text box.
- **AI-looking (my reading):** the skin, hair and lighting have the smooth, uniform finish of AI-generated imagery; the product bottle has no label.
- **With the title:** the title asks "What … Use BEFORE Foundation", and the thumbnail shows the step being done with a deliberately **unlabelled** bottle, so the answer stays hidden. "20 Years Younger" and "Korean Makeup Artists" are in the title only; the image carries the authority visually (a pro artist working on her). The YouTube description sells **"Luxe Color Changing Foundation"** (Amazon link amzn.to/3SsqmPe) and ends with "#ad".

### T5. du597reEoRA — "Never Put Eyeshadow on Bare Eyelids Again. Try This Old Korean Trick Instead"
**Channel:** Clemons Hays · **Views:** 386,712 · **Likes:** 3,565 · **Published:** 2026-10-24 · **Length:** 11:34 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "DO THIS BEFORE" (white, black outline, three stacked lines: "DO THIS" / "BEFORE"), "EYESHADOW!" (white on a pink/red rounded box).
- **Layout:** the same young male makeup artist (curly hair, glasses, black zip polo) in the centre, applying a skin-tone product with a flat brush to the closed eyelid of an older woman (about 60, brown/grey bob, teal top) on the right, his other hand lifting her brow. Text on the left over a bokeh vanity-bulb background with white flowers. No before/after, no arrow.
- **Face/expression:** the woman's eyes are closed and she is serene, with a slight smile; he is concentrating.
- **Colours:** warm bokeh gold/white, black clothing, teal accent, pink/red text box.
- **AI-looking (my reading):** same AI-render look and the same "artist" character as T4 and T6.
- **With the title:** the title is the "Never do X … try this trick instead" pattern; the thumbnail turns it into a command ("DO THIS BEFORE EYESHADOW!") and shows the trick being done, without showing what the product is. Description again sells "Luxe Color Changing Foundation" (Amazon) with "#Ad".

### T6. uCH3zXRIKn8 — "Never Put Lipstick on Bare Lips Again. Try This Old Korean Trick Instead"
**Channel:** Clemons Hays · **Views:** 147,253 · **Likes:** 1,884 · **Published:** 2026-10-30 · **Length:** 12:54 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "DO THIS BEFORE LIPSTICK!" (one line; "LIPSTICK!" in a pink/red box), "LIP BALM" (label on the jar), "BEFORE" (white on a red label), "AFTER" (white on a green label).
- **Layout:** the same young male "artist" on the left, holding a small glass jar labelled "LIP BALM" and pointing at it. The right 55% is a **split before/after** of an older woman's mouth: before = dry, cracked lips with lines around them; after = smooth, plumper pink lips. A white curved arrow runs from BEFORE to AFTER.
- **Face/expression:** a slight smirk and raised brow: a "trust me" look.
- **Colours:** the same bokeh vanity background; red vs green labels (bad → good).
- **AI-looking (my reading):** an AI render; the before/after mouths also look generated.
- **With the title:** this is the only one of the three Clemons Hays thumbnails that **reveals the trick** (lip balm) and adds a before/after. That may be part of why it has the lowest views of the three (147K vs 387K and 479K; a correlation, not proven). The description again sells the Luxe foundation, although this video is about lips; the last hashtag reads "#adventure" rather than "#ad".

### T7. _6Y19q9USLg — "The Korean Eyeliner Trick for Hooded Eyes After 60"
**Channel:** Soojin Park · **Views:** 233,515 · **Likes:** 3,005 · **Published:** 2026-10-24 · **Length:** 16:43 (NexLev, pulled 2026-11-07) · **Image:** maxresdefault.jpg
- **Exact text:** "THE KOREAN EYELINER TRICK" (four stacked lines of heavy black condensed caps, no outline or box).
- **Layout:** the text fills the left half on a plain white background. On the right, a tight close-up of the presenter lifting her brow skin with one hand and drawing a thin brown pencil line along her upper lash line with the other. No product brand, arrows, circles or before/after.
- **Face/expression:** a Korean woman in her late 50s to 60s, dark shoulder-length hair with grey at the part, pearl earrings, beige linen top. Mouth slightly open mid-sentence, eyes on the camera: a "teaching you" look, not shock.
- **Colours:** stark white and black; the only colour is her mauve lipstick and skin. Very minimal, which stands out in a feed of red/yellow thumbnails.
- **AI-looking (my reading):** very smooth, evenly lit, studio-perfect skin; probably AI-generated or heavily retouched. The channel describes her as "a Seoul makeup artist and esthetician with thirty years of doing faces".
- **With the title:** the thumbnail repeats the first half of the title ("The Korean Eyeliner Trick"). The title adds who it's for ("Hooded Eyes After 60"). The image demonstrates the trick (lifting the lid and lining) without explaining it, so the "how" is the gap. No product is sold; the description promotes her own book (soojinparkbooks.com).

### T8. lUPAwO6GP8Y — "A Korean Makeup Artist Shows What to Use BEFORE Foundation to Look 20 Years Younger After 60"
**Channel:** Soojin Park · **Views:** 179,506 · **Likes:** 1,877 · **Published:** 2026-10-22 · **Length:** 20:02 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "BEFORE" (white, black outline), "FOUNDATION!" (white on a pink/red rounded box). This is the same type treatment as Clemons Hays (T4).
- **Layout:** a spa/salon scene. The Korean "artist" (about 60, dark bob, beige linen top) in the centre-left holds up a **clear, unlabelled toner bottle** and smiles at the camera. With her other hand she presses a cotton pad to the cheek of a grey-haired Asian client (about 65, white towel headband, white robe) on the right. A **red curved arrow** runs from the text box to the bottle; a white dashed arrow loops near the pad. Shelves of white bottles, a round lit mirror and dried pampas behind.
- **Face/expression:** the artist is warm and mid-speech; the client is content, eyes half-closed, with a dewy wet cheek.
- **Colours:** creamy white/beige spa palette; the red box and red arrow are the only strong colour.
- **AI-looking (my reading):** AI-rendered (uniform glow, generic unlabelled props).
- **With the title:** this is almost the same composition as T4 (same text treatment, cotton pad on cheek, an unlabelled bottle as the answer), here with an older Korean artist instead of the young man. The title's promise ("20 Years Younger After 60") plus the "Korean Makeup Artist Shows" authority, and the deliberately blank bottle, create the gap: what is in the bottle? The description promotes her book; no product link.

### T9. SnDAYIQNIlQ — "Korean Vaseline Tricks That Make Your Skin Look Years Younger"
**Channel:** Young-Hee Care · **Views:** 109,650 · **Likes:** 818 · **Published:** 2026-10-22 · **Length:** 9:25 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "this how we use vaseline" (all lower-case, as written, with the "is" missing: "this how we" in white with a dark outline, "use vaseline" in yellow), plus the numbers "1" to "5" in big white outlined numerals on each panel, and "Vaseline" on the jars.
- **Layout:** a numbered grid of five panels around a centre presenter: 1 = a Vaseline jar on a towel; 2 = glossy lips with a fingertip; 3 = jelly shining under an eye; 4 = cracked dry heel/elbow skin with jelly; 5 = jelly slicked through dark hair. In the centre, a Korean woman (about 65, short grey curly hair, linen robe) smiles, holding a **Vaseline** jar and dabbing cream on her cheek.
- **Face/expression:** a gentle, grandmotherly, reassuring smile.
- **Colours:** blue (Vaseline brand blue) and white, with yellow text accent; soft bathroom background.
- **AI-looking (my reading):** AI-rendered presenter and panels.
- **With the title:** the title says "Tricks" (plural) and "Years Younger"; the thumbnail turns that into a numbered list of 5 uses. The numbering signals "a list you can binge", and "we" (Korean women) sets up insider knowledge. The broken grammar reads as a native "grandmother" voice. The product is cheap and already in your drawer, so the barrier is low.

### T10. VPIyLxS_BJM — "9 French Makeup Secrets That Work After 60 (Most Americans Don't Know)"
**Channel:** Grace Sydney · **Views:** 98,582 · **Likes:** 1,233 · **Published:** 2026-10-08 · **Length:** 20:16 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "FRENCH TRICK!" (white, black outline, on a red rounded box: "FRENCH" on top, "TRICK!" below in the red box).
- **Layout:** a Paris salon. A brunette "French" artist (about 40, bangs, red lipstick, Breton stripe top) on the left holds an open **pink cream-blush pot** while the client (about 60, layered auburn/blonde hair, white blazer, pearl stud) pats blush onto her cheekbone. A **red curved arrow** points from the pot to the cheek. The **Eiffel Tower** is visible through the window on the right; vanity bulbs and white hydrangeas on the left.
- **Face/expression:** the client has a satisfied, confident closed-lip smile; the artist looks at the cheek with an approving smile.
- **Colours:** warm cream and gold, red text box and arrow, pink blush, a Breton stripe as a "French" signal.
- **AI-looking (my reading):** AI-rendered.
- **With the title:** the title says "9 Secrets" and an us-vs-them line ("Most Americans Don't Know"); the thumbnail narrows to one "FRENCH TRICK!" and shows the product type (cream blush) being placed high on the cheek. The Eiffel Tower and stripes are shorthand for "French". The gap: what is the trick, and what are the other 8?

### T11. i3GMXcXpPgQ — "What Korean Makeup Artists Do BEFORE Foundation (10 Years Younger at 60+)"
**Channel:** Grace Sydney · **Views:** 72,241 · **Likes:** 961 · **Published:** 2026-10-03 · **Length:** 16:29 (NexLev) · **Image:** maxresdefault.jpg
- **Exact text:** "KOREAN TRICK!" (same treatment as T10: "KOREAN" white with outline, "TRICK!" on a red box), plus "LANEIGE" printed on the cushion compact lid and the puff.
- **Layout:** almost the same as T10, with the **same client** (about 60, auburn/blonde layered hair, white blazer, diamond pendant) on the right. A Korean artist (about 30, black ponytail, black top) on the left holds an open **Laneige cushion compact** while the client presses the Laneige puff to her cheek. A red curved arrow runs from the compact to the cheek. Salon vanity bulbs and white flowers.
- **Face/expression:** the client has a soft, pleased smile with eyes on the camera; the artist looks on approvingly.
- **Colours:** cream/white, black clothing, red text box and arrow, beige compact.
- **AI-looking (my reading):** AI-rendered, and the client is the same rendered woman as T10.
- **With the title:** the title asks the "BEFORE foundation" question and promises "10 Years Younger at 60+"; the thumbnail answers partly (a cushion compact) with a recognisable K-beauty brand. The description says "Products shown are examples only. I'm not affiliated with any brand."; no product is sold. It has the lowest views of the 11 (72K), while the same channel's "French" version (T10) has 99K.

---

# Part 3 — Summary

All figures are from yt-dlp metadata (pulled 2026-11-07), the transcripts and the frames, unless marked *(reading)*.

## The 14 downloaded Facebook videos are really 2 advertisers × 5 distinct ads

| Group | Page | Videos | Distinct edits | Product sold | Total view_count |
|---|---|---|---|---|---|
| A. "Makeup artist: throw these away" | Minho Makeup & Beauty | 2, 3, 4, 5, 6, 7, 8 | 6 (6 = 7 same file) | **LUXE foundation** (color-adapting), last of the list | 285,795 |
| B. "Cheap [store] stuff as good as luxury" | Jiho Beauty | 9, 10, 11, 12, 13, 14, 15 | 3 (Dollar Tree = 9; Walmart = 10 & 11, same edit re-encoded; Target = 12–15, same edit; 13–15 byte-identical) | **LUXE Korean under-eye balm** (stick), last of the list | 1,131,037 |

Group B outperformed Group A by about 4×, on fewer distinct edits. The Target edit alone has 909,662 view_count across its 4 posts; its first post (#15, 650,286) is the top video of the set. In both groups the **first post of an edit beat its re-posts by a wide margin**: #15 650K vs 112K / 102K / 46K; #7 40K vs re-post #6 32K; #11 62K vs #10 73K is the one exception (posted a day apart).

## Most common HOOK patterns (Facebook)
1. **Swearing + store + "better than luxury" (all 7 Group B posts).** "Cheap shit from Target / Walmart / Dollar Tree that's just as good, if not better, than the luxury stuff." (0:00–0:04), then the age call-out "And if you're over 50, you're gonna want to save this list. Let's go." (0:04–0:07). On screen: a headline that names the store ("CHEAP SHIT FROM 🎯 TARGET THAT'S BETTER THAN LUXURY"), the sub-line "A must-have for women over 50+", and a selfie walking a store aisle.
2. **"You look older" pain + age range + "throw this away" (all 6 Group A edits).** "If you look decades older, completely drained, and like your makeup is working against you…" (2, 3, 8), "If your eyes makes you look decades older…" (5), "If you look decades older… don't worry" (6), "The reason you look twice your age is not because you are old…" (4). Then "even at 50, 60, or 70" and a ban: "get rid of that matte lipstick" / "never use matte lipstick again". Visual: a **before/after face cut in the first ~5 s** (an aged, heavily made-up "before", then a polished "after"). In every edit the helpers judged the two women to be visibly different people *(reading)*.
3. **A built-in save/keep-watching cue** in the first 6–30 s: "save this list" (B); a covered basket with "The last one may be the one thing standing between you and looking 20 years younger" (A, about 0:19–0:31).

## Most common FORMATS
- **"Dupes for luxury" list, with the paid product as "the best dupe saved for last"** (Group B). Six real, recognisable drugstore swaps, each set against a named luxury product with a pink "$" price tag (La Mer $200 → Nivea; SkinCeuticals $185 → e.l.f.; La Prairie $575; Amorepacific $260…), each with an ingredient-overlap stat ("Fourteen of its sixteen ingredients"). Then item 7: a luxury eye cream → one shared ingredient (adenosine or PDRN) → LUXE.
- **"Never use X / throw these away — a makeup artist's routine for mature skin"** (Group A). Three products are banned as "tested on 20-year-olds", then five real prestige products (Clinique All About Eyes, NARS concealer, Makeup by Mario bronzer, Too Faced blush, e.l.f. gloss), then LUXE foundation as "the one step most women miss".
- Both formats **borrow trust from real brands first and put the paid product last**, phrased as the payoff of the list.

## Most common PRODUCT placement
- **Always last**, in all 14 videos: item 7 of 7 (B) or the last step of A's routine (6 products in 2, 4, 6/7 and 8; #3 counts the same 6 products as 5 steps; #5 is a shorter eye routine with Luxe as the 3rd named product).
- **When it first appears:** B, spoken at 1:19 (Target), 1:31 (Dollar Tree) and 1:40 (Walmart) of 1:48–2:08, so about 72–78% of the way in. A, the tube first on screen at 1:25–1:39 and named at 1:40–1:50 of 2:19–2:29, so about 65–75% of the way in.
- **Bridge lines:**
  - B: "Okay, but I saved the best dupe for last." (Target; Dollar Tree: "Hey, but…"; Walmart: "…the best for last.") → luxury eye cream + "One of its key ingredients is adenosine" / "La Prairie says it uses PDRN" → "Luxe makes a Korean under-eye balm with that same…"
  - A: "But one step is missing, and this is the step that makes you look less tired, brings your face to life, and yet most women miss it completely." → "Foundation." → "Luxe foundation is specifically developed for mature skin."
- **No LUXE price is ever given** in either group, while every competitor gets a price.
- **Signs the shots are generated *(reading)*:** the LUXE packaging has garbled small print in several videos, and LUXE is filmed on a Target, Walmart or Dollar Tree shelf although it is sold through Amazon.

## Most common CTAs
- **Several routes at once, every time.** "Search Luxe [on Amazon] or click the link in my bio. And if you're watching on Facebook, the link will be in the comments." (B); "Link is on my profile, and I also added the link in the comments." (A).
- **A comment keyword for an automated DM, gated on following:** B uses "Comment DM" (Dollar Tree: "LINK"); A uses "natural", "glow" or "eyes". Gate lines: "Just make sure you're following me first so I can message you." (B) / "you have to follow me first" (A). In #2 and #3 the caption keyword ("GLOW") does not match the spoken one ("natural").
- **Urgency:** A: "Sometimes there's a coupon available, so hurry up." B: "It's way cheaper on Amazon than anywhere else."

## Claims & compliance patterns
- **Unsourced result claims:** B, "It reduces the look of wrinkles by 30% in four weeks." A, "It is the number one best-selling foundation on Amazon right now" (spoken and on screen), "almost never settles into wrinkles", "specifically developed for mature skin".
- **Implied professional use:** A, "every client"; the presenter is styled as a makeup artist but no credential is stated.
- **Ad labels:** B posts start the caption with "AD |". Nothing on screen says "ad" in any video. A captions start with "adl", which is not a recognisable disclosure.
- **AI labels:** a small "syntheticmedia" watermark (lower-left) appears on every frame of 8, 9, 10/11 and 12–15; none was found on 2–6. There is no spoken or caption AI disclosure anywhere.

## Most common THUMBNAIL patterns (YouTube, 11)
1. **A "Do this BEFORE ___!" command headline** in white outlined block caps with the key noun in a pink/red rounded box: "BEFORE FOUNDATION!" (T4, T8), "DO THIS BEFORE EYESHADOW!" (T5), "DO THIS BEFORE LIPSTICK!" (T6). The **"BEFORE foundation/eyeshadow/lipstick"** idea also appears in 4 of 11 titles. The gap is *what* to do before.
2. **"[Culture] TRICK!" naming:** "KOREAN TRICK!" (T11), "FRENCH TRICK!" (T10), "THE KOREAN EYELINER TRICK" (T7). "Korean" appears in 7 of 11 titles, "French" in 1.
3. **An AI-rendered salon scene: an "artist" (young man, Korean woman or French woman) working on a 60-ish client**, with a red curved arrow from the product to the face (T4, T5, T8, T10, T11). The product is **unlabelled or only partly revealed** (blank bottle, cotton pad). The two thumbnails that reveal the answer (T6 lip balm with before/after; T11 Laneige cushion) are the lowest-viewed of their channels (147K and 72K).
4. **Real-creator thumbnails use different tools:** a credential badge plus before/after ("ACCORDING TO A DERMATOLOGIST", T1), a tier-list product wall ("BEST TO WORST", T2) and a surprised reaction face ("I Was NOT EXPECTING THAT!", T3).
5. **Age is in the title, not on the image:** "Over 60", "After 60", "60+" and "Over 50" are in 8 of 11 titles, but no age text appears on any thumbnail; age is shown by the client's face instead.
6. **Promises:** "20 Years Younger" (T4, T8), "10 Years Younger" (T11), "Years Younger" (T9).
7. **LUXE link:** the three Clemons Hays videos (T4–T6: 479K, 387K, 147K views) promote "Luxe Color Changing Foundation" (amzn.to link) in the description, whatever the video's topic. They are tagged "#ad" (T4), "#Ad" (T5), and "#adventure" (T6, likely a typo or garbled "#ad", *reading*).
