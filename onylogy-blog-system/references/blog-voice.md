# Onylogy Studio — Blog Voice (v2, 2026-09-14)

> **This file is the law for every onylogy.com blog post.** v1 (July 2026) described the voice in words; posts
> written against it in August and September drifted (audit in `../blog-write-publish.md` §1). v2 adds hard,
> lintable numbers taken from the six canon posts, worked opening/closing formulas, and an explicit precedence
> rule over every other writing instruction. `tooling/audit-draft.py` enforces the numbers; a draft that fails
> the gate is not uploaded.
>
> **Byline:** Ehasanul Haque · **Reader:** a nervous WordPress beginner (Cluster 5 Kadence posts: a beginner who
> already has a site and is building with Kadence Blocks) · **Niche:** WordPress, themes, hosting, plugins.
>
> **The canon** (read these before drafting, they are in `canon/`): What Is WordPress · Top 6 Hosting Providers ·
> Top 6 Free Themes · 6 Must-Have Plugins · Common WordPress Mistakes · Unlock KadenceWP.

---

## 0. Precedence (read first)

When two instructions disagree, the higher one wins:

1. **Honesty.** Never invent experience, numbers, prices, dates, versions, quotes or sources. Unknown → `[TK: …]`.
2. **This file, Part I** (voice, rhythm, structure).
3. **`seo-geo-checklist.md`** (Rank Math / Yoast / Google rules). It shapes headings, answer placement and meta,
   never the tone.
4. **`post-types.md`** (skeleton per post type) and Part II below (SEO layer, canon-shaped).
5. **The `onywrites` skill.** Demoted to a lint pass. Keep: honesty rules, `[TK:]` markers, named specifics, the
   no-dash rule, the banned-phrase list, "don't explain your own point" *inside a section*. Drop: non-linear
   entry, first-person anecdote openings, the unresolved-thread section, the digression section, the "hot"
   section, deliberately uneven sections, "no epilogue" (the canon always ends with a Conclusion + FAQ).

The onywrites structural devices were the cause of the drift. They may not appear as headings, openings or
whole sections. A post that reads like an experienced consultant's opinion piece has failed, however good it is.

---

## 1. Who is talking, to whom

- **Second person, always.** Talk *to* one beginner. "You want people to find your website, right?"
- **First person is rare and short.** The canon uses "I" about once per 1,500 words. Allowed: "I'm going to
  show you", "my coupon code", and **one or two short experience sentences per post** for E-E-A-T
  ("On the client sites I build, this is the plugin I keep installed."). Never open the post with an anecdote,
  never make a section out of it, never hedge with "I still don't know".
- **Reassuring.** The reader is worried. Remove the fear early and often: "Not intimidating." "Plain and simple."
  "You don't need to be a tech wizard." "That's it."
- **Conversational but authoritative.** Plain words; define any unavoidable term on first use, in the same
  sentence: "content management system (CMS)".
- **Contractions everywhere** (don't, it's, you'll, won't). Write like speech.
- **Light drama, one persona per item** in roundups: "The Bodyguard", "The Time Machine", "The Spam Killer".
- **Rhetorical questions** open sections and hook: "Nobody likes waiting for a page to load, right?"

## 2. Rhythm (this is what drifted most)

The canon is short lines with air between them, not essay paragraphs.

- **Paragraphs are 1 to 3 sentences.** Four is the hard maximum. Never five.
- **Roughly a third of paragraphs are a single sentence.** Punchy one-liners carry emphasis:
  *"But there's a catch."* / *"That's where plugins come in."* / *"Choose wisely, and everything else becomes easier."*
- **Sentences average 12 to 16 words.** Long sentence, then a short one. Never three long ones in a row.
- **Contrast couplets** are a signature: *"Choose wisely, and everything else becomes easier. Choose poorly, and
  problems follow you everywhere."* / *"If you install too many, your site breaks. If you install the wrong ones,
  you get hacked."*
- **Problem → Solution** in two beats: *"Bad hosting causes slow loading, downtime, and constant frustration."* →
  the fix in the next line.
- **Myth-buster lines:** "It's not hype." "That's rare in hosting."
- **Reassuring close to a section:** "Millions of creators use it because it works. Plain and simple."

## 3. The numbers (lint gate, from the canon)

`tooling/audit-draft.py` measures these on the body text. **Gate** = must pass before upload. **Target** = aim for it.

| Measure | Canon range | Gate | Target |
|---|---|---|---|
| "you / your" per 100 words | 2.7 to 5.9 | ≥ 3.0 | 4.0 |
| "I / my / me" per 100 words | 0.0 to 0.15 | ≤ 0.35 | ≤ 0.2 |
| One-sentence paragraphs (share of all paragraphs) | 31% to 90% | ≥ 30% | 40% |
| Paragraphs with more than 4 sentences | 0 | 0 | 0 |
| Paragraphs over 120 words | 0 | 0 (Rank Math "short paragraphs") | 0 |
| Average sentence length (words) | 9 to 17 | ≤ 17 | 13 |
| Sentences over 20 words (share) | – | ≤ 25% (Yoast) | ≤ 20% |
| Rhetorical questions in body | 1 to 12 | ≥ 2 | 4 |
| Reassurance beats (see §1 phrases) | 1 to 8 | ≥ 2 | 3 |
| Em dashes, en dashes as dashes, `--` | (canon used them) | **0** (house rule, 2026-09-04) | 0 |
| FAQ pairs | 6 to 7 (Kadence 13) | 6 to 7 (pillar ≤ 13) | 7 |
| Bold phrases per 100 words | 1.2 to 2.5 | 1 to 3 | 1.7 |
| Word count | see `post-types.md` | within the type's range | middle of range |

Word count by type (canon-matched, decided 2026-09-14): **roundup 1,100 to 1,500 · guide / how-to 1,200 to 1,800 ·
comparison ("vs") 1,100 to 1,600 · single-tool deep dive 1,500 to 2,200 · Kadence block deep dive 1,200 to 1,800 ·
pillar / cornerstone 2,500 to 3,200.** Depth over padding: stop when the beginner has what they need.

## 4. Article structure (the template)

1. **H1** — see §5.
2. **Intro, 4 to 8 short paragraphs**, most of them one line. Formula, in this order:
   - Hook: a rhetorical question or a bold claim. *"Building a WordPress site?"* / *"Choosing the right hosting is
     one of the most important decisions you'll make for your WordPress website."*
   - The stakes in one contrast couplet.
   - Reassurance: *"You don't need 50 plugins. You just need the right ones."*
   - The promise: *"In this post, I'm going to show you the 6 essential WordPress plugins every beginner needs."*
   - Optional authority stat with source and year: *"WordPress powers about 43% of all websites (W3Techs, 2026)."*
   - A one-line send-off: *"Let's dive right in."*
   The primary keyword appears in the first 100 words.
3. **Key Takeaways** (H2, 4 bullets, bold lead + short line) — **guides and pillars over ~1,400 words only.**
   Not on roundups, not on short guides. (Canon: 2 of 6 posts.)
4. **Context section** — "What Is WordPress Hosting? (Quick Explanation)", "Why the Right Theme Matters".
   First sentence is a self-contained plain-English definition (the AI-citable line), then the usual rhythm.
5. **"How We Chose"** on roundups (3 to 5 bullets of criteria). Builds trust.
6. **Main body** — numbered items (roundup) or topical H2s (guide). Per-item pattern in `post-types.md`.
7. **Decision helper** — "Which Hosting Provider Should You Choose?": scenario → pick bullets
   (*"On a tight budget: Hostinger or DreamHost."*). Every roundup and comparison has one.
8. **Conclusion** — H2 named **Conclusion**, **Final Thoughts** or **Wrapping It Up** (rotate; don't use
   "Conclusion" on every post). 2 to 4 short paragraphs: restate the picks, encourage, end with an engagement
   line: *"Over to you: which of these mistakes did you make on your first site? Let me know in the comments."*
9. **FAQ** — H2 "Frequently Asked Questions", "FAQ: Common … Questions" or "Common … Questions (FAQ)".
   Each question an H3, answer 1 to 3 sentences, answer-first. Never skip.
10. Site chrome (You May Also Like, footer) is the theme's job. **No byline line in the body** (the theme prints
    author and date).

## 5. Headings

- **H1:** `[Number/Topic] + [benefit] + ([beginner-facing qualifier])`, Title Case. *"Top 6 Hosting Providers for
  WordPress (Beginner-Friendly Guide)"*, *"What Is WordPress and Why Should You Use It? (Beginner Guide)"*.
  Roundups use **6**. Keep the primary keyword in the first half of the H1 (Rank Math "keyword at beginning").
- **H2:** either the numbered item or a plain-language question/statement. Question H2s are a signature and
  match how people ask AI: *"Is WordPress Free?"*, *"Which Hosting Provider Should You Choose?"*
- **Numbered item H2:** `N. [Name]: [Persona or benefit]` — use a colon, not a dash. *"2. Wordfence Security: The Bodyguard"*.
- **H3 inside items:** the same labels on every item in the post. Roundup default: **Why You Need It** /
  **Key Features** / **Alternative:** (plugins) or **Best for:** (hosts, themes, registrars). Mistakes post:
  **The Issue** / **The Fix**.
- Put the primary keyword in 30% to 75% of subheadings (Yoast) — naturally; a "1. Hostinger" heading doesn't count.
- One H1 only. H2 → H3, no skipped levels. A subheading at least every 300 words (Yoast).

## 6. Formatting

- **Bold** on: product names at first mention, defined terms, statistics, menu paths (**Settings > Permalinks**),
  the one line to remember. Never decorative.
- *Italics* for soft emphasis.
- **Bullets** for features, criteria, scenarios, takeaways. **Numbered lists** only for real sequential steps.
- **Tables:** one comparison table per roundup (Quick Comparison: name / price / best for / free tier) placed
  before the decision helper. Guides use a table only for real head-to-head specs.
- **No em dash, no en dash used as a dash, no `--`.** Use a full stop, a comma, a colon or brackets. Hyphens only
  where meaning requires them (well-known plugin, third-party) and never after "-ly" adverbs.
- Keep paragraphs to the §3 numbers. When a paragraph reaches a fourth sentence, split it.

## 7. Images

- Featured image at the top (v4 thumbnail, `thumbnail-guide.md`).
- **One image right after each item H2** in roundups (the tool's WordPress.org listing or homepage hero);
  one per major concept in guides (3 to 4). Rank Math wants ≥ 4 media for full marks; hit it on roundups,
  don't force it on short guides.
- Alt text = `[subject/product] + [what's shown] + [WordPress/beginner keyword]`, and the primary keyword in at
  least one alt (usually the featured image).
- Keyword filenames, 1200px wide `.webp`, captured per `../blog-write-publish.md` §6.

## 8. Links and CTAs

- **Internal:** 3 to 6, woven into sentences with descriptive anchors ("beginner-friendly WordPress hosting"),
  always with the category prefix (`/wp-plugins/slug/`, never `/slug/`). Spokes link up to the pillar; the
  pillar links down. Roundups link to their paired guide and back.
- **External:** 1 to 3 authoritative, followed links: the tool's official page (linked from the **bolded name
  in the first paragraph under its heading**, never from the heading), WordPress.org, W3Techs, web.dev.
- **CTAs are soft:** "check out the features", "grab it today". A mid-article CTA link is common
  ("View which hosting will be best for you"). Affiliate/coupon lines are personal and low-pressure:
  *"Get 10% off with my coupon code: hosten"*. Never "BUY NOW".

## 9. Word-level tells to remove on the last pass

Delve, tapestry, landscape, realm, testament to, navigate the complexities, in today's fast-paced world, "it's
important to note", "at the end of the day", "ultimately", "the key takeaway is", stacked tricolons, every
sentence the same length, staged "some say X, others say Y" balance. Also: "game-changer", "seamless",
"robust", "leverage" (as a verb), "unlock" outside a title that already uses it.

---

# PART II — SEO / AEO layer (canon-shaped)

The full, sourced rule set is `seo-geo-checklist.md`; this is how it sits inside the voice.

- **One primary keyword**, chosen query-first, in: H1 (first half), first 100 words, ≥ 1 H2, slug, meta
  description. Density 0.5% to 1.5%, never above 2.5%. If it reads awkwardly, rewrite the sentence.
- **5 to 10 semantic keywords** through H2s and body.
- **Answer first.** The first sentence under every H2 and every FAQ answer stands alone as a plain answer
  (a "X is a Y that does Z" line for concepts). Then continue in the short canon rhythm. Do not write dense
  40 to 60 word definition blocks; two short sentences that together answer the question do the same job.
- **Experience proof:** 1 to 2 short first-person sentences per post, real, or `[TK:]`. Own screenshots where
  possible. Every statistic carries a source and a year in the sentence.
- **Freshness:** "Last updated" is set by WordPress; refresh numbers on republish.
- **Schema:** Rank Math outputs Article automatically; the FAQ block is written so Rank Math's FAQ schema (or
  the JSON-LD kept in the .md comment) matches the visible text exactly.
- **Meta:** Title tag left to Rank Math's default (never set the Title field). Meta description 130 to 145
  characters, keyword near the front, plain punctuation, in voice.

---

## 10. Pre-publish checklist (voice)

- [ ] Reads like the canon: to one nervous beginner, reassuring, punchy, contractions, one persona per item.
- [ ] `audit-draft.py` gate passes (all §3 gate rows green).
- [ ] Intro follows the §4 formula; opens with a hook, not an anecdote or a thesis.
- [ ] No onywrites structural devices visible (no unresolved-thread heading, no digression section, no
      "I still don't know", no "the part every roundup skips").
- [ ] Same H3 labels on every item; decision helper present; Conclusion heading rotated; engagement line last.
- [ ] FAQ 6 to 7, answer-first, 1 to 3 sentences each.
- [ ] `seo-geo-checklist.md` passes.
- [ ] Zero dashes. Zero `[TK:]` left unreported. Byline Ehasanul Haque set on the post, not in the body.
