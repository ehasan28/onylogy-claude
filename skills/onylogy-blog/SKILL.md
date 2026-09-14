---
name: onylogy-blog
description: Write, research, illustrate, upload and (on approval) schedule a blog post for onylogy.com from just a title, in the exact Onylogy canon voice (six original beginner posts) and passing the Rank Math / Yoast / Google SEO+GEO checklist. Use when the user gives a blog title or topic for Onylogy Studio, asks to "write a blog about X", to fix/rewrite an existing Onylogy post so it reads like the originals, or to upload a drafted post to onylogy.com.
---

# Onylogy blog — skill wrapper

This skill is the entry point for a full production **system** that lives at the root of the
[onylogy-claude](https://github.com/ehasan28/onylogy-claude) repository:

```
onylogy-claude/
├── skills/onylogy-blog/SKILL.md        ← you are here (thin wrapper)
└── onylogy-blog-system/                ← the system (also a complete skill on its own: it has its own SKILL.md)
    ├── blog-write-publish.md           ← the playbook (authoritative procedure, phases 0 to 9, repair mode)
    ├── references/                     ← blog-voice.md (v2, lintable), seo-geo-checklist.md, post-types.md,
    │                                      post-template.md, site-facts.md, firsthand-facts.md, thumbnail-guide.md,
    │                                      content-map.md, canon/ (the six original posts)
    └── tooling/                        ← audit-draft.py (the gate), thumb.py, shot.py, pwshot.js, secshot.js,
                                           media-ids.py, make-draft-php.py, md2blocks.py, verify-post.py, permalinks.py
```

**Setup once:** clone the repository somewhere permanent, e.g. `SYSTEM=~/onylogy-claude/onylogy-blog-system`, and run
`$SYSTEM/tooling/setup.sh`. If you copy only this folder into `~/.claude/skills/`, edit the path below.

**Do this, in order:**
1. `Read` `$SYSTEM/blog-write-publish.md` completely, then `references/blog-voice.md`, `post-types.md`,
   `seo-geo-checklist.md`, `site-facts.md`, `firsthand-facts.md`.
2. Follow the playbook's phases 0 to 9 and tick every box in its **§0 Definition of done** before reporting completion.
3. Use `$SYSTEM/tooling/` (`audit-draft.py` is the gate: never upload a draft that fails it). Never rebuild the pipeline.
4. Calibrate against `references/canon/` whenever unsure how something should read.

Non-negotiables: title-only is enough (no questionnaire); the canon voice wins over the `onywrites` skill except on honesty,
dashes and named specifics; no PHP against the site without a fresh yes; images, Rank Math fields and the featured image
through the real editor UI; Rank Math Title field empty; no byline in the body; nothing published without the user's
explicit go; report counts, not adjectives.

The system is written for onylogy.com (Kadence theme, Rank Math, Novamira CLI, LiteSpeed). To reuse it for another
WordPress site, replace `references/site-facts.md`, `firsthand-facts.md`, `canon/` and regenerate `blog-voice.md` §3 from
that site's own best posts with the audit method in `blog-write-publish.md` §1.
