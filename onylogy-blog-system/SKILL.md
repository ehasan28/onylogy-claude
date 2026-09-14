---
name: onylogy-blog
description: Write, research, illustrate, upload and (on approval) schedule a blog post for onylogy.com from just a title, in the exact Onylogy canon voice (six original beginner posts) and passing the Rank Math / Yoast / Google SEO+GEO checklist. Use when the user gives a blog title or topic for Onylogy Studio, asks to "write a blog about X", to fix/rewrite an existing Onylogy post so it reads like the originals, or to upload a drafted post to onylogy.com.
---

# Onylogy blog system

This folder is a complete, self-contained skill (copy it to `~/.claude/skills/onylogy-blog/` or point a thin
wrapper at it). The authoritative procedure is **`blog-write-publish.md`** in this folder. **Read it in full
before doing anything**, then work through its phases 0 to 9 and tick every box in its §0 Definition of done.

| Path | Purpose |
|---|---|
| `blog-write-publish.md` | The playbook: definition of done, the drift audit, phases 0 to 9 (setup → intake → research → structure → draft + gate → thumbnail → screenshots → planning files → upload → report), repair mode, guard rails |
| `references/blog-voice.md` | **The voice, v2**: precedence rule, who/whom, rhythm, the canon numbers (lint gate), article template, headings, formatting, images, links, SEO layer canon-shaped, checklist |
| `references/seo-geo-checklist.md` | Rank Math + Yoast + Google rules with sources; every post passes it |
| `references/post-types.md` | Skeleton, length, images, table/takeaways rules per post type |
| `references/post-template.md` | The `.md` skeleton (POST META, body, JSON-LD, IMAGES block) |
| `references/site-facts.md` | onylogy.com: categories/IDs, tags, author, permalinks, Rank Math rules, Novamira CLI, browsers, tokens |
| `references/firsthand-facts.md` | The only experience claims allowed (real, dated); everything else is `[TK:]` |
| `references/thumbnail-guide.md` | v4 featured image spec (+ `thumbnail-history.md`, v1 archive) |
| `references/content-map.md` | Clusters, pairing rules, Sunday cadence, `blog-list.txt` line format |
| `references/canon/` | The six canon posts as extracted from the live site, for calibration |
| `tooling/` | `audit-draft.py` (gate), `thumb.py`, `shot.py`, `pwshot.js`, `secshot.js`, `media-ids.py`, `make-draft-php.py`, `md2blocks.py`, `verify-post.py`, `permalinks.py`, `check-sync.sh`, `setup.sh`, README |

Workspace (living data, not in this folder): `~/Claude Playground/Onylogy Studio Website/Blog Posts/`
(`blog-list.txt`, `blog-idea.md`, `Blogs/<slug>/`, `thumbnails/`).

Non-negotiables (restated so they survive skimming): title-only is enough, don't block on a questionnaire;
canon voice wins over `onywrites` on everything except honesty, dashes and named specifics; run
`tooling/audit-draft.py` and fix every gate line before upload; no PHP without a fresh yes; images, Rank Math
and featured image through the real editor UI; Rank Math Title field empty; no byline in the body; nothing
published without the user's explicit go; report counts, not adjectives.
