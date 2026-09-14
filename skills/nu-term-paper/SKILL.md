---
name: nu-term-paper
description: Write a complete National University of Bangladesh (জাতীয় বিশ্ববিদ্যালয়) Bangla sociology term paper from just a title, in the exact NU format — cover, ইনসাইড কাভার, ঘোষণা পত্র, অনুমোদন পত্র, মুখবন্ধ, সূচিপত্র, five chapters ১.১–৫.৩, 10 aims, 15 recommendations, bottom-of-page footnotes, গ্রন্থপঞ্জি — with every statistic verified against a named source, a Word/PDF build plus a Bijoy/SutonnyMJ copy, a source-verification sheet, and optional upload to Google Docs. Use when the user gives a টার্ম পেপার title, asks for an NU honours/masters sociology term paper, or wants an existing one extended or fixed.
---

# NU term paper (জাতীয় বিশ্ববিদ্যালয় টার্ম পেপার) — skill wrapper

This skill is the entry point for a full production **system** that lives at the root of the
[onylogy-claude](https://github.com/ehasan28/onylogy-claude) repository:

```
onylogy-claude/
├── skills/nu-term-paper/SKILL.md      ← you are here
└── nu-term-paper-system/              ← the system
    ├── term-paper-write.md            ← the playbook (authoritative procedure)
    ├── skeleton/                      ← manuscript skeleton with all fixed template strings
    ├── tooling/                       ← docx build pipeline (footnotes, TOC page map, Bijoy copy)
    └── references/                    ← template analysis, sample aims, research notes
```

**Setup once:** clone the repository somewhere permanent and remember the path, e.g.
`SYSTEM=~/onylogy-claude/nu-term-paper-system`. If you copy only this `skills/nu-term-paper`
folder into `~/.claude/skills/`, edit the path below to the absolute location of the system folder.

**Do this, in order:**
1. `Read` `$SYSTEM/term-paper-write.md` completely (~350 lines — read all of it, not the first screen).
2. Follow its **Quick start** (14 steps) and tick every box in **§0 Definition of done** before reporting completion.
3. Copy `$SYSTEM/skeleton/` and `$SYSTEM/tooling/` into the new paper's project folder as the playbook instructs; never rebuild the pipeline from scratch.
4. Consult `$SYSTEM/references/` whenever unsure how a section should read.

Prerequisites on the machine: Node ≥ 18, Poppler (`pdftoppm`, `pdftotext`), LibreOffice (native
binary), the Siyam Rupali font (shipped in `tooling/`) installed for LibreOffice, and
`src/nu-logo.png` (see the playbook's crest note). In Claude Code you also need web search, a
browser tool for sites that block plain fetches, and — only for the Google Docs step — the
Claude in Chrome extension.

Non-negotiables (restated so they survive skimming): ask the intake questions first; every number
footnoted and traceable to `research-notes.md`; plain, easy Bangla; template strings verbatim;
front matter exactly 6 pages; two-pass build so the সূচিপত্র page numbers are real; report the
page count honestly; never delete anything in the user's Drive without explicit permission.
