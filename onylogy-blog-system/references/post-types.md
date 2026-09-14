# Post types: skeleton, length, per-item pattern

Pick the type from the title before anything else. Every type keeps the voice (`blog-voice.md`) and passes
`seo-geo-checklist.md`; this file only fixes the skeleton.

| Type | Title shape | Words | Images | Key Takeaways | Table | Thumbnail bg |
|---|---|---|---|---|---|---|
| **Roundup** | "Top 6 X for WordPress (…)", "6 Must-Have X" | 1,100 to 1,500 | 6 (one per item) + featured | no | 1 (Quick Comparison) | blue; black for security/speed/backup/hosting |
| **How-to guide** | "How to X (Beginner Guide)" | 1,200 to 1,800 | 3 to 4 | if ≥ 1,400 words | only for real specs | blue; black if technical |
| **Explainer / pillar** | "What Is X and Why …?", cluster hubs | 2,500 to 3,200 (hub) · 1,200 to 1,800 (explainer) | 3 to 4 | yes on hubs | optional | blue |
| **Comparison** | "X vs Y: Which …?" | 1,100 to 1,600 | 2 to 3 | no | 1 (side-by-side) | blue, VS split icon |
| **Single-tool deep dive** | "How to Set Up X", "X: The Complete Guide" | 1,500 to 2,200 | 4 to 6 (settings screens) | yes | settings table | black if technical |
| **Kadence block deep dive** (Cluster 5) | "Kadence X Block: …" | 1,200 to 1,800 | 2 to 4 (editor + live section) | no | defaults table | blue; black for layout-ish blocks |
| **Mistakes / checklist** | "Common X Mistakes (and How to Fix Them)" | 1,300 to 1,800 | 2 to 3 | yes | no | blue |

## Roundup skeleton (the proven best performer)

```
# Top 6 [Category] for WordPress ([Qualifier])
Intro (4 to 8 short paragraphs, §4 formula)
## What Is [Category]? (Quick Explanation)      ← definition first sentence
## How We Chose These [Things]                   ← 3 to 5 bullets
## 1. [Name]: [Persona]
[image]
**[Name]**(linked to official page) one-line intro. Rhetorical question or hook.
### Why You Need It          (2 to 4 short paragraphs; one-liners welcome)
### Key Features             (3 to 4 bullets)
### Alternative: [Name]      (plugins) | **Best for:** … (hosts/themes/registrars)
## 2. … (identical labels) … ## 6.
## Quick Comparison                               ← the one table
## Which [Thing] Should You Choose?               ← scenario → pick bullets
## Final Thoughts | Conclusion | Wrapping It Up   ← 2 to 4 short paras, engagement line last
## Frequently Asked Questions                     ← 7 × H3 + 1 to 3 sentence answer
```

Vary *inside* the fixed slots: let one item run a paragraph longer, give one a sharper verdict, but never change
the H3 labels between items. Ranking order is the recommendation order; say why #1 is #1 in one line.

## How-to guide skeleton

```
# How to [Do X]: [Benefit] ([Beginner Guide])
Intro (formula)
## Key Takeaways                                  ← only if the post will exceed ~1,400 words
## What You Need Before You Start                 ← short bullets
## Step 1: …  ## Step 2: …  (H2 per step, image where a screen changes; numbered list inside a step only for sub-clicks)
## Common Problems (and Fixes)                    ← 3 to 5 "The Issue / The Fix" pairs, optional
## What to Do Next                                ← links to the sibling posts (decision helper role)
## Conclusion / Final Thoughts
## FAQ
```
HowTo schema only if the steps are genuinely sequential.

## Comparison ("vs") skeleton

```
# X vs Y: Which One Do You Actually Need? (Beginner Guide)
Intro (formula; the one-line answer is allowed in the intro)
## What Is X? / ## What Is Y?                     ← definition-first sections
## X vs Y: The Key Differences                    ← the table
## When X Is the Right Choice / ## When Y Is the Right Choice
## Which Should You Choose?                       ← scenarios
## Final Thoughts
## FAQ
```

## Single-tool deep dive (user rule, 2026-07-19)

Cover, in this order, easiest first: what it is and who maintains it · what it depends on (server, PHP, host) ·
which hosts it works best with (link the hosting roundup) · the settings that work in practice, section by
section with screenshots · advanced configuration last, clearly labelled so a beginner can stop early. **Ask the
user at intake whether the topic should be one long post or a beginner + advanced pair** (LiteSpeed became two).

## Kadence block deep dive (Cluster 5 standing rule)

Written from real client-build experience: the block's defaults (from `block.json`), what we change and why,
one real screenshot from the editor and one from a live section, the gotchas from `onylogy-kadence-build-rules.md`.
Still the canon voice: talk to the reader, keep it short, reassure. "How we do it" is one or two sentences, not
the frame of the post. Links: up to the Kadence hub, sideways to one other block post.

## Pillar / hub

Longest form. Key Takeaways, question H2s, a definition line per concept, links down to every spoke, FAQ up to
13. Mark "Pillar Content" in Rank Math.
