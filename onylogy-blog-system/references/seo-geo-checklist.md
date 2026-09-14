# Onylogy SEO + GEO Checklist (every post must pass)

> Built 2026-09-14 from the published guidance of **Rank Math** (the plugin onylogy.com runs), **Yoast SEO** and
> **Google Search Central**. Each rule names its source so it can be re-verified when the vendors change their
> advice. Rules marked **[lint]** are checked automatically by `tooling/audit-draft.py`; the rest are checked by
> hand in the pre-publish pass. The voice never bends to this list (`blog-voice.md` §0); this list decides
> *where* things go, not *how* they sound.
>
> Sources (fetched 2026-09-14):
> - RM-AIO: Rank Math, "How to Rank in AI Overviews" (June 2025) https://rankmath.com/blog/ranking-in-ai-overviews/
> - RM-AISEO: Rank Math, "Top AI SEO Strategies for 2026" https://rankmath.com/blog/ai-seo-strategies/
> - RM-GEO: Rank Math glossary, "Generative Engine Optimization" https://rankmath.com/seo-glossary/generative-engine-optimization/
> - RM-100: Rank Math KB, "How to score 100/100 in tests" https://rankmath.com/kb/score-100-in-tests/
> - Y-LLM1: Yoast, "How to optimize content for AI LLM comprehension" (May 2025) https://yoast.com/how-to-optimize-content-for-llms/
> - Y-LLM2: Yoast, "What is LLM SEO?" (Aug 2025) https://yoast.com/llm-seo-optimization-techniques-including-llms-txt/
> - Y-READ: Yoast readability checks (sentence length, paragraph length, passive voice, transition words,
>   subheading distribution, Flesch) https://yoast.com/the-sentence-length-check/ · https://yoast.com/paragraph-length-check/ ·
>   https://yoast.com/the-passive-voice-what-is-it-and-how-to-avoid-it/ · https://yoast.com/features/readability-analysis/
> - Y-SEO: Yoast SEO analysis (keyphrase density, meta description, subheadings, links) https://yoast.com/features/keyphrase-density/ ·
>   https://yoast.com/meta-descriptions/ · https://yoast.com/features/seo-analysis/ · https://yoast.com/seo-copywriting-checklist/
> - G-AI: Google Search Central, "Top ways to ensure your content performs well in Google's AI experiences on Search"
>   (May 2025) https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search

---

## A. Keyword and intent (before writing)

| # | Rule | Source | Check |
|---|---|---|---|
| A1 | One **primary keyword** per post, chosen query-first (how people type it into Google or ask an AI). Unique across the site: no two posts share a focus keyword. | RM-100 | hand + `permalinks.json` |
| A2 | Keyword matches **search intent** (what/why/how/best/top = informational; "vs", "best X" = commercial-informational). | RM-AIO | hand |
| A3 | 5 to 10 **semantic / secondary keywords** (synonyms, sub-questions, long-tail conversational phrases). Listed in POST META. | Y-LLM2, RM-GEO | hand |
| A4 | Post belongs to a **topic cluster** and links up to its pillar and across to siblings (topical authority). | RM-AIO, Y-LLM2 | `content-map.md` |

## B. Placement (Rank Math + Yoast tests)

| # | Rule | Source | Check |
|---|---|---|---|
| B1 | Primary keyword in the **H1**, in the first half of it. | RM-100 (title readability) | **[lint]** |
| B2 | Primary keyword in the **first 10% of the body** (first ~100 words for our lengths). | RM-100, Y-SEO | **[lint]** |
| B3 | Primary keyword in the **slug**; slug ≤ 75 characters, lowercase, hyphenated, keyword-only. | RM-100 | **[lint]** |
| B4 | Primary keyword in the **meta description**, near the front. | RM-100 | **[lint]** |
| B5 | Primary keyword in **30% to 75% of subheadings** (Yoast) and at least one H2 (Rank Math). Counted on descriptive H2/H3s, not "1. Hostinger". | Y-SEO, RM-100 | **[lint]** |
| B6 | Primary keyword in **at least one image alt** (the featured image). | RM-100 | **[lint]** |
| B7 | **Keyword density 0.5% to 1.5%**; warn above 2.5%. Secondary keywords appear naturally. | RM-100 (1 to 1.5%), Y-SEO (0.5 to 3%) | **[lint]** |
| B8 | H1 contains a **number** (roundups) and a **power word** or clear benefit; Rank Math scores both. Never force sentiment words into the voice. | RM-100 | hand |

## C. Structure for readers and machines

| # | Rule | Source | Check |
|---|---|---|---|
| C1 | **Descriptive H2/H3 headings** that read like the queries people type: "What Is…", "How to…", "Which … Should You Choose?" | RM-AIO, RM-AISEO, Y-LLM1 | hand |
| C2 | **Answer first:** the question implied by each H2 is answered in its first one or two sentences (Rank Math: first 40 to 60 words). No burying the lead. | RM-AISEO, Y-LLM1 | hand |
| C3 | **One idea per section**, a subheading at least every **300 words**. | Y-LLM1, Y-READ | **[lint]** |
| C4 | **Short paragraphs:** none over 120 words (Rank Math); Yoast green under 150. Our voice gate is stricter (≤ 4 sentences). | RM-100, Y-READ | **[lint]** |
| C5 | **Short sentences:** no more than 25% of sentences over 20 words. | Y-READ | **[lint]** |
| C6 | **Passive voice** in under 10% of sentences. | Y-READ | **[lint]** (approximate) |
| C7 | **Transition words** in ≥ 30% of sentences (because, so, then, for example, first, next, however…). The canon's short lines already do this; don't stuff them. | Y-READ | **[lint]** (approximate) |
| C8 | **Flesch Reading Ease ≥ 60** (plain English; Yoast's target for content you want quoted by LLMs). | Y-LLM1, Y-READ | **[lint]** |
| C9 | **Lists** for criteria, features and steps; each bullet self-contained so it can be lifted on its own. | Y-LLM1, Y-LLM2, RM-AIO | hand |
| C10 | **One comparison table** per roundup (name · price · free tier · best for). | RM-AIO (extractable formats), house rule | **[lint]** on roundups |
| C11 | **Key Takeaways / TL;DR** near the top on long guides and pillars (≥ ~1,400 words) only. Bold lead phrase per bullet. | RM-AIO, Y-LLM1, Y-LLM2 | **[lint]** |
| C12 | **FAQ section** with 6 to 7 questions written the way people ask them; answers **1 to 3 sentences**, standalone. | Y-LLM2, RM-GEO | **[lint]** |
| C13 | **Cover the follow-up questions** inside the post so the page is the complete answer (body + FAQ). | Y-LLM2 | hand |
| C14 | Content length: Rank Math scores 100% only at 2,500+ words, but Google and Yoast reward completeness over length. **We follow the canon ranges in `blog-voice.md` §3** and accept the lower Rank Math length score. Cornerstone/pillar posts go 2,500+. | RM-100 vs G-AI | **[lint]** |

## D. E-E-A-T, originality, freshness

| # | Rule | Source | Check |
|---|---|---|---|
| D1 | **Unique, non-commodity content**: at least one thing a competitor page cannot copy (own screenshot, own numbers, a real client-build detail, a verified current price with the month). | G-AI, RM-AISEO ("information gain") | hand |
| D2 | **Experience proof:** 1 to 2 real first-person sentences per post (`blog-voice.md` §1). Never invented; `[TK:]` if missing. | G-AI, Y-LLM2, RM-AIO | hand |
| D3 | **Every statistic has a named source and a year** in the sentence ("about 43% of all websites (W3Techs, 2026)"). | RM-AIO, Y-LLM2 | **[lint]** (numbers near % / million without a bracket flag a warning) |
| D4 | **Prices, limits, versions, install counts checked on the vendor's own page or WordPress.org on the day of writing**, cited with the month. Recorded in `research.md` in the post folder. | RM-AIO (freshness), house rule | hand |
| D5 | **Author** = Ehasanul Haque, with the site's author bio; the theme prints byline and date, so no byline line in the body. | RM-AIO, RM-AISEO | hand |
| D6 | **Freshness:** when a post is republished or updated, refresh numbers and examples and let WordPress update the modified date. | RM-AIO, G-AI | hand |
| D7 | **Original media:** at least 1 image, 4+ on roundups (Rank Math media test); own screenshots preferred; every image has descriptive alt. | RM-100, G-AI | **[lint]** |

## E. Links

| # | Rule | Source | Check |
|---|---|---|---|
| E1 | **3 to 6 internal links** with descriptive anchors, including the pillar and at least one sibling; always the full `/<category>/<slug>/` path. | RM-100, Y-SEO, Y-LLM2 | **[lint]** |
| E2 | **1 to 3 external, followed links** to authoritative pages (the tool's official page from its bolded name, WordPress.org, web.dev, W3Techs). Rank Math requires ≥ 1 followed external link. | RM-100, Y-SEO | **[lint]** |
| E3 | Link **tool names, not headings**. | house rule | hand |
| E4 | No broken links; internal targets exist in `permalinks.json` or are new posts in this wave. | RM-AIO | **[lint]** |

## F. Meta and schema

| # | Rule | Source | Check |
|---|---|---|---|
| F1 | **Meta description 130 to 145 characters** (Yoast: 120 to 156 shown; Rank Math also measures pixel width, so stay under), keyword near the front, plain punctuation, no dashes, in voice. | Y-SEO, RM-100, house rule | **[lint]** |
| F2 | **SEO Title field left empty** in Rank Math (inherits the global template). The H1 carries the keyword. | house rule (2026-08-04) | hand |
| F3 | **Structured data matches the visible page.** Rank Math emits Article; the FAQ block is the exact FAQ text. No schema for things not on the page. | G-AI, RM-AIO | hand |
| F4 | **Schema types:** Article on all; FAQPage from the FAQ; HowTo only for genuine step lists. | RM-AIO, RM-GEO | hand |
| F5 | **Categories and tags** set: primary category decides the permalink prefix; 3 to 5 relevant tags from the existing tag list. | Y-SEO (taxonomy) | hand |
| F6 | **Featured image** 1200×630 v4 thumbnail, alt = post summary with the keyword. | RM-100 (alt), house | hand |

## G. Site-level (already true on onylogy.com; re-verify quarterly)

| # | Rule | Source | Status |
|---|---|---|---|
| G1 | HTTPS, mobile-friendly, Core Web Vitals green (PageSpeed mobile 86 on 2026-09-12; LCP 2.7s). Images light (webp ≤ 150 KB). | RM-AIO, G-AI | keep images light per post |
| G2 | XML sitemap submitted in Search Console; clean URLs `/<category>/<slug>/`. | RM-AIO | done |
| G3 | **llms.txt** generated (Rank Math and Yoast both ship a generator). | RM-AISEO, Y-LLM2, RM-GEO | [TK: confirm it is enabled on onylogy.com] |
| G4 | Author bio page with credentials; Organization schema for Onylogy Studio. | RM-AIO, RM-AISEO | [TK: confirm author box + org schema] |
| G5 | Brand mentions and backlinks from relevant sites (guest posts, media) raise AI citation odds. Out of scope per post; tracked separately. | RM-AISEO, RM-GEO | ongoing |
| G6 | Track AI citations: search the post's question in ChatGPT, Perplexity, Gemini, Google AI Mode a month after publishing; note which competitor is cited instead. | Y-LLM2, RM-AISEO | monthly |

---

## Pre-publish pass (copy into the report)

```
SEO/GEO: A1 keyword __ · A3 semantics __ · B1-B7 placement __ · C2 answer-first __ · C10 table __ · C11 takeaways __ ·
C12 FAQ __ · D1 unique __ · D2 experience __ · D3 sources __ · D4 prices dated __ · E1 internal __ · E2 external __ ·
F1 meta __ · F3 schema matches __ · F5 taxonomy __ · F6 featured __
```

Anything not passable from the draft alone (G3, G4, live Rank Math score) is reported as "not verified", never
as done.
