<!--
================= POST META (for WordPress / Rank Math) =================
Slug:              {{slug}}                      (lowercase, hyphens, keyword-only, ≤ 75 chars; folder name = slug)
Type:              {{roundup | guide | explainer | pillar | comparison | deep-dive | kadence | mistakes}}
Primary keyword:   {{primary keyword, query-first}}
Secondary/semantic: {{5 to 10 related terms, comma separated}}
Title tag:         (leave Rank Math's Title field EMPTY; the H1 is the title)
Meta description (130-145 chars, no dashes): {{…}}
Category:          {{WP Plugins | WordPress | Hosting | WP Themes | Domain | Ecommerce}} (primary first)  → permalink /{{category-slug}}/{{slug}}/
Tags:              {{3 to 5 from the existing tag list in site-facts.md}}
Author:            Ehasanul Haque (user ID 2)
Featured image alt: {{post summary with the primary keyword}}
Internal links:    {{slugs, with category prefixes}}
External links:    {{official pages to link from bolded tool names}}
Cluster:           {{n, phase, position}}
Publish slot:      {{next free Sunday 09:00, from blog-list.txt}}
Thumbnail:         {{slug}}-thumbnail.svg / .webp  (v4: {{blue|black}}, "{{line 1}}" / "{{line 2}}", icon {{name}})
Facts checked:     {{YYYY/MM/DD}}: {{what was verified where}}  (details in research.md)
Voice gate:        {{audit-draft.py result summary, filled after the audit}}
====================================================================
-->

# {{H1: [Topic] + [benefit] + ([qualifier])}}

{{Intro. Hook line. Stakes couplet. Reassurance line. Promise line with the primary keyword. Optional sourced stat. Send-off.}}

## Key Takeaways
{{only for guides/pillars ≥ ~1,400 words; otherwise delete this section}}
- **{{Bold lead}}:** {{short line}}
- **{{Bold lead}}:** {{short line}}
- **{{Bold lead}}:** {{short line}}
- **{{Bold lead}}:** {{short line}}

## {{Context H2, e.g. "What Is X? (Quick Explanation)"}}

{{First sentence = plain definition that stands alone. Then the canon rhythm.}}

## {{How We Chose … (roundups) | What You Need Before You Start (guides)}}

- {{criterion}}
- {{criterion}}
- {{criterion}}

## 1. {{Name}}: {{Persona or benefit}}

**[{{Name}}]({{official URL}})** {{one-line intro}}. {{hook question}}

### Why You Need It

{{2 to 4 short paragraphs}}

### Key Features

- {{feature}}
- {{feature}}
- {{feature}}

### Alternative: {{Name}}   <!-- or: **Best for:** … -->

{{… items 2 to 6 with identical H3 labels …}}

## Quick Comparison

| {{Thing}} | Free tier | Paid from | Best for |
|---|---|---|---|
| {{…}} | {{…}} | {{…, checked Month YYYY}} | {{…}} |

## Which {{Thing}} Should You Choose?

- **{{Scenario}}:** {{pick}}
- **{{Scenario}}:** {{pick}}
- **{{Scenario}}:** {{pick}}

## {{Final Thoughts | Conclusion | Wrapping It Up}}

{{2 to 4 short paragraphs. Restate the picks. Encourage.}}

{{Engagement line, e.g. "Over to you: which one are you installing first? Let me know in the comments."}}

## Frequently Asked Questions

### {{Question written the way people ask it?}}
{{1 to 3 sentences, answer first.}}

### {{…}}
{{…}}

{{6 to 7 pairs}}

<!--
================= JSON-LD SCHEMA (reference only; Rank Math emits Article. Keep FAQ text identical to the visible FAQ.) =================
<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":"Article","headline":"{{H1}}","author":{"@type":"Person","name":"Ehasanul Haque"},"publisher":{"@type":"Organization","name":"Onylogy Studio"},"datePublished":"{{YYYY-MM-DD}}","dateModified":"{{YYYY-MM-DD}}","image":"https://onylogy.com/wp-content/uploads/{{YYYY}}/{{MM}}/{{slug}}-thumbnail.webp","mainEntityOfPage":"https://onylogy.com/{{category-slug}}/{{slug}}/"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"{{Q1}}","acceptedAnswer":{"@type":"Answer","text":"{{A1}}"}}
]}]}
</script>

================= IMAGES (captured {{YYYY/MM/DD}}; all 1200px-wide .webp in this folder; featured = thumbnail webp) =================
featured        → {{slug}}-thumbnail.webp                 alt: "{{featured alt}}"   [top]
1. {{Name}}     → {{keyword-filename}}.webp               alt: "{{alt}}"            [after "## 1. {{Name}}"]
2. {{Name}}     → {{keyword-filename}}.webp               alt: "{{alt}}"            [after "## 2. {{Name}}"]
====================================================================
-->
