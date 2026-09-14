---
name: nu-term-paper
description: Write a complete National University of Bangladesh (জাতীয় বিশ্ববিদ্যালয়) Bangla sociology term paper from just a title, in the exact NU format — cover, ইনসাইড কাভার, ঘোষণা পত্র, অনুমোদন পত্র, মুখবন্ধ, সূচিপত্র, five chapters ১.১–৫.৩, 10 aims, 15 recommendations, bottom-of-page footnotes, গ্রন্থপঞ্জি — with every statistic verified against a named source, a Word/PDF build plus a Bijoy/SutonnyMJ copy, a source-verification sheet, and optional upload to Google Docs. Use when the user gives a টার্ম পেপার title, asks for an NU honours/masters sociology term paper, or wants an existing one extended or fixed.
---

# NU term paper (জাতীয় বিশ্ববিদ্যালয় টার্ম পেপার) — system

This folder is a complete, self-contained skill: it can be copied as-is into
`~/.claude/skills/nu-term-paper/`. The authoritative procedure is `term-paper-write.md`
in this same folder (~350 lines). **Read it in full before doing anything**, then follow
its *Quick start* (14 steps) and tick every box in *§0 Definition of done* before
reporting completion.

| Path (relative to this folder) | Purpose |
|---|---|
| `term-paper-write.md` | The playbook: intake questions, research protocol, 100 % structure spec, writing voice, build & QA, delivery, Google Docs procedure, pitfalls log |
| `skeleton/` | `front.js` + `paper-part1..4.txt` — every fixed template sentence verbatim, `{{slots}}` only where the topic changes |
| `tooling/` | `build.js` (docx with footnotes, tables, TOC, Bijoy conversion), `pagemap.js`, `render.sh`, `verification.js`, `package.json`, `SiyamRupali.ttf` (+ `FONT-LICENSE.txt`) |
| `references/` | `template-analysis-original-example.md` (the scanned example the template was derived from), `handwritten-sample-aims-migration.md` (10-aims pattern), `example-cyberbullying/` (research notes + README of the first paper built with this system) |

Prerequisites on the machine: Node ≥ 18 (`npm install` inside the project pulls `docx` and the
Bijoy converter), Poppler (`pdftoppm`, `pdftotext`), LibreOffice (native binary, used by
`render.sh`), the Siyam Rupali font installed for LibreOffice, and `src/nu-logo.png` (see the
playbook's crest note — the crest is not redistributed here). In Claude Code you also need
web search, a browser tool for sites that block plain fetches, and — only for the Google
Docs step — the Claude in Chrome extension.

Non-negotiables (restated so they survive skimming): ask the intake questions first; every
number footnoted and traceable to `research-notes.md`; plain, easy Bangla; template strings
verbatim; front matter exactly 6 pages; two-pass build so the সূচিপত্র page numbers are real;
report the page count honestly; never delete anything in the user's Drive without explicit
permission.

Language note: the paper is written in Bangla; these instructions are in English so they stay
precise for the model. Bangla numerals are used throughout the paper.
