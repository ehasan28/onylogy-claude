# Onylogy blog: from a title to a live post (the playbook)

> **Trigger:** the user gives a blog title (or says "write a blog about X") for onylogy.com.
> **Deliverable:** a post in the canon voice, researched with dated sources, thumbnail and screenshots made,
> uploaded to onylogy.com as a date-pinned draft with every editor field set, verified, planning files updated,
> and the user asked whether to schedule it. Nothing is published without the user's yes.
> **Rule zero:** read this file to the end before starting. Then work through §2 in order. Skipping a phase is
> how the September 2026 posts drifted.

Layout: **system** = this folder (static: rules, references, tooling). **Workspace** =
`~/Claude Playground/Onylogy Studio Website/Blog Posts/` (living: `blog-list.txt`, `blog-idea.md`,
`Blogs/<slug>/…`, `thumbnails/`). The system never stores post drafts; the workspace never stores rules.

---

## 0. Definition of done (tick every box before saying "done")

- [ ] `Blogs/<slug>/` holds `<slug>.md` (POST META + body + JSON-LD + IMAGES block), `research.md`,
      `<slug>-thumbnail.svg` + `.webp`, every screenshot as 1200px `.webp` with a keyword filename.
- [ ] `tooling/audit-draft.py <slug>` exits 0 (voice gate + SEO lint), and the hand checks in
      `references/blog-voice.md` §10 and `references/seo-geo-checklist.md` "Pre-publish pass" are ticked in the report.
- [ ] Every `[TK:]` is either filled by the user or listed in the report. No invented facts, prices, or experience.
- [ ] Images uploaded through the Media Library UI; `media-ids.py` found all of them.
- [ ] Draft post exists on onylogy.com with the pinned Sunday date (PHP run only after the user's explicit yes).
- [ ] Body uploaded as core blocks and the batch is `finalized`; `verify-post.py` exits 0.
- [ ] In the editor: featured image + alt, primary category, tags, Rank Math focus keyword and description
      (Title field untouched), Pillar Content ticked if a hub, **Save draft**.
- [ ] `blog-list.txt` line added/updated with the WP ID and date; `permalinks.py` refreshed; pillar/hub
      "link down to this post" to-do noted.
- [ ] Report sent: audit table, TKs, post ID + edit URL, and the question "schedule for <date>?"
- [ ] Memory updated if anything about the site or the process changed.

---

## 1. Why v2 exists (read once)

Audit of all 26 live posts, 2026-09-14, against the six canon posts:

| | Canon (6) | Sept 2026 (15) |
|---|---|---|
| "you" per 100 words | 3.8 | 2.5 |
| "I/my" per 100 words | 0.07 | 0.52 |
| one-sentence paragraphs per post | 22 | 10 |
| reassurance beats per post | 4.0 | 1.1 |
| words | 750 to 1,450 | 2,000 to 3,000 |
| Key Takeaways box | 2 of 6 | 15 of 15 |

Cause: the `onywrites` structural rules and the SEO layer were applied on top of a voice file that had no
numbers. Decisions (user, 2026-09-14): canon tone + 1 to 2 short experience sentences; canon length; SEO layer
kept but canon-shaped; the 15 unpublished Cluster 5 drafts get rewritten to v2; the live September posts stay.
The gate in `tooling/audit-draft.py` exists so this cannot happen silently again.

---

## 2. The phases

### Phase 0 — Setup (2 minutes, every time)

1. `tooling/check-sync.sh` (reference copies in sync?) and `tooling/permalinks.py` (fresh slug map).
2. Read, in full: `references/blog-voice.md`, `references/post-types.md`, `references/seo-geo-checklist.md`,
   `references/site-facts.md`, `references/firsthand-facts.md`. Skim two canon posts in `references/canon/` of
   the same type as the new post (a roundup → plugins + hosting; a guide → what-is-wordpress + mistakes).
3. Read the workspace `blog-list.txt` and the relevant part of `blog-idea.md` (`references/content-map.md`
   says where a title belongs).
4. Confirm the tooling runs: `tooling/setup.sh` (idempotent) if anything is missing.

### Phase 1 — Intake and slot (ask only what the title doesn't tell you)

The standing instruction is "title only → go". Do **not** block on the onywrites intake questionnaire.
Decide from the title, then ask at most one batched message, and only for things that change the work:

- **Post type** (`post-types.md`) and the primary category (→ permalink prefix). If a single-tool deep dive:
  one long post or a beginner + advanced pair? (ask; LiteSpeed became two).
- **Cluster placement, pairing and slot**: which cluster, which paired guide/roundup, next free Sunday from
  `blog-list.txt`. Propose; the user confirms the date before Phase 8.
- **Firsthand material**: check `firsthand-facts.md` first. If the post needs an experience beat the bank
  doesn't cover, plan a `[TK:]` and ask in the same message (one question, not a questionnaire).
- **Benchmarks**: if the title needs speed numbers, stop and ask for a real test before writing.

Write the answers (or your assumptions) into POST META. Create `Blogs/<slug>/` and copy
`references/post-template.md` to `<slug>.md`.

### Phase 2 — Research (all facts dated, all in `research.md`)

1. **SERP and angle:** WebSearch the exact title and the primary keyword. Note the top results' angles and
   H2s. Our post must answer the same questions more simply and with something they can't copy (D1).
2. **Facts:** for every tool, price, plan limit, install count, version: open the vendor's pricing page or the
   WordPress.org listing *today* and record value + URL + date in `research.md`. Cite the month in the body
   ("$2.99/month as of September 2026"). Never from memory.
3. **Statistics:** source + year in the sentence. W3Techs for WordPress share; web.dev for Core Web Vitals.
4. **Keywords:** primary (query-first) + 5 to 10 semantic terms; check `permalinks.json` that no existing post
   uses the same primary keyword. If `seo-dataforseo` is connected, pull volume/difficulty; if not, say so.
5. **Links:** pick 3 to 6 internal targets from `permalinks.json` (pillar/hub + siblings + paired post) and 1
   to 3 external official pages. Write them into POST META.
6. **Screenshot list:** decide the images now (roundup: one per item; guide: 3 to 4), with the capture method
   for each (`tooling/README.md`): WP.org listing → `shot.py wporg`; homepage hero → `shot.py hero`; blocked site
   → `pwshot.js`; onylogy.com section → `secshot.js`; editor screen → admin link (approval needed).

### Phase 3 — Structure

Fill the skeleton from `post-types.md` with real H2/H3 text: question-style H2s, identical H3 labels per item,
the persona per item, the decision-helper scenarios, the 7 FAQ questions (written the way people ask), the
Conclusion heading (rotate the three names). Note where each image goes. Show this outline to the user only if
the title was ambiguous; otherwise proceed.

### Phase 4 — Draft, then gate

Write the whole post in one pass in the canon voice (`blog-voice.md` §1 to §9), then:

1. **Self-edit for rhythm:** every paragraph ≤ 3 sentences (4 max); a third of them one line; contrast couplets;
   at least two reassurance beats; a rhetorical question per two or three sections; contractions everywhere.
2. **Experience beat:** 1 to 2 short first-person sentences from `firsthand-facts.md`, placed inside a section,
   never as the opening.
3. **SEO placement:** keyword in H1 (first half), first 100 words, one H2, slug, meta description, featured alt;
   answer-first sentence under every H2; Quick Comparison table on roundups; Key Takeaways only on long guides.
4. **Dashes:** search for `—`, `–`, `--`. Zero.
5. **Run `tooling/audit-draft.py <slug>`.** Fix every GATE line and re-run until it exits 0. Read the warnings;
   fix the cheap ones (keyword in subheadings, Flesch, transitions). Paste the summary line into POST META
   "Voice gate".
6. **Hand audit:** `blog-voice.md` §10 and the `seo-geo-checklist.md` pre-publish pass. Then the onywrites
   honesty pass only: no invented specifics, `[TK:]` where the user must fill.
7. Write the JSON-LD block (Article + FAQPage, FAQ text identical to the body) and the IMAGES block with
   final filenames and alt text.

### Phase 5 — Thumbnail

`tooling/thumb.py <slug> "Line 1" "Line 2" --bg blue|black --icon <name>` per `references/thumbnail-guide.md`.
Open the `.webp`, look at it at ~30% zoom (card size): two readable lines, one unmistakable icon. Put the
alt text in POST META.

### Phase 6 — Screenshots

Capture per the Phase 2 list into `Blogs/<slug>/`, 1200px wide `.webp`, keyword filenames. **Look at every
capture** (cookie bars, sign-in popovers, geo prices, cut-off banners). Pixel-check edges on WP.org crops
(`feedback-verify-screenshots-pixel-data`); never eyeball them. Update the IMAGES block. Editor screenshots
need a one-time admin access link → ask the user first, every time.

### Phase 7 — Planning files

Add the `blog-list.txt` line (`[~]` drafted locally, slot proposed), add the cluster note in `blog-idea.md` if
it's a new cluster, run `tooling/permalinks.py` so the new slug resolves for other drafts.

### Phase 8 — Upload (the approved hybrid pipeline, in this order)

**a. Images → Media Library UI (Chrome).** Open `https://onylogy.com/wp-admin/media-new.php` in the Claude in
Chrome tab (not `?browser-uploader`). `find` the multi-file input, `file_upload` every `.webp` in the post folder
(thumbnail included). Wait for the uploader to finish, then `tooling/media-ids.py <slug>` until all are found.
Duplicates (`-1`) → decide (reuse old ID or rename) before continuing.

**b. Empty draft → one PHP run (ASK FIRST).** `tooling/make-draft-php.py <slug> --date YYYY-MM-DD`, then tell
the user exactly what it does ("creates one draft post titled …, date pinned to Sunday …, nothing published;
undo = trash it") and wait for a yes. Then
`novamira --site onylogy.com run novamira/execute-php --input @php-in-<slug>.json --json --yes`.
Record the returned post ID in `blog-list.txt` (`[D]`).

**c. Body → Gutenberg batch.** `tooling/md2blocks.py <slug> --post-id ID --media media-ids-<slug>.json --out spec.json`
(exit 0 = all images placed, all links mapped). Open the finalize page
`https://onylogy.com/wp-admin/admin.php?page=novamira-gutenberg-finalize` in the Chrome tab and keep it open. Then
`gutenberg-add-pending-change` (@spec.json) → `gutenberg-enable-batch-finalization` ({"batch_id":N}) → poll
`gutenberg-list-pending-batches` every ~10 s until `finalized`. If `failed`/`conflicted`: read the item's
`validation_errors`, fix the draft or the converter, delete the batch, re-add.

**d. Editor fields → real UI (Chrome), per `feedback-rank-math-seo-via-ui` and `feedback-image-upload-via-ui`.**
Open `post.php?post=ID&action=edit`, wait ~7 s, then in this order (the exact click sequence that worked on
2026-09-12):
1. Set featured image → search the filename → click the tile → set Alt Text in the details panel → confirm.
2. Categories panel → Rank Math **Select Primary Term** → the primary category (permalink prefix).
3. Tags are already on the post from the PHP step; check.
4. Rank Math sidebar → **click the focus keyword field by screen coordinate** (ref clicks don't register) → type
   the primary keyword → Enter.
5. **Edit Snippet** → click the **Description** textarea → cmd+A → type the meta description → close. **Never
   touch the Title field.**
6. Hub/pillar only: tick "This post is Pillar Content".
7. **Save draft.** Confirm the toolbar shows the pinned date ("Schedule" button, not "Publish").
8. Remove Gutenberg's empty starter paragraph if one appears at the top; there must be no byline paragraph.

**e. Verify.** `tooling/verify-post.py <slug> --post-id ID` → exit 0. Open the post preview once and look at the
top of the post and one image. Report counts, not adjectives.

### Phase 9 — Report and hand-off

Send: the audit summary line, the SEO/GEO pass line, every open `[TK:]`, the post ID + edit URL, the proposed
Sunday, and one question: **"Schedule it for <date>?"** If yes → click **Schedule** in the editor (Chrome) and
change `blog-list.txt` to `[S]`. Then update memory (`onylogy-blog-system` note) if the site or the process
changed, and add any new real fact the user gave to `references/firsthand-facts.md`.

---

## 3. Repair mode (existing post → v2 voice)

Used for the 15 Cluster 5 drafts (IDs 2082 to 2096) and any future "this reads like AI" request.

1. Run `tooling/audit-draft.py <slug>`; paste the gate failures into the report so the user sees what was off.
2. Keep: slug, H1, primary keyword, the facts and their dates, screenshots, internal links, the FAQ questions.
3. Restructure to the canon skeleton: rewrite the intro with the §4 formula; cut the onywrites devices
   (anecdote opening, "I still don't know", digression sections, hot sections); shrink to the type's word range;
   break paragraphs to 1 to 3 sentences; raise "you", lower "I"; add reassurance beats and question H2s;
   Key Takeaways only if a long guide; keep the one comparison table on roundups.
4. Gate again until it passes, then Phase 8c (body batch replaces the content; `gutenberg-add-pending-change`
   on the same post ID), 8d step 5 if the description changed, 8e.
5. For a **published** post, say plainly if a restructure risks a ranking heading and offer the narrow fix
   (rhythm, "you", reassurance, dashes) first.

---

## 4. Guard rails (non-negotiable)

- **No PHP without a fresh yes**, even mid-task (`feedback-no-php-without-approval`).
- **Images, Rank Math, featured image, primary term through the real UI**, never REST/JS shortcuts.
- **No byline line in the body. Rank Math Title field empty. Description 130 to 145 chars, no dashes.**
- **No invented facts or experience.** `[TK:]` beats filler. Prices dated to the month.
- **Voice file wins** over onywrites on everything except honesty, dashes and named specifics.
- **Nothing published without the user's explicit "schedule"/"publish".**
- **Report counts** (headings, images, words, gate results), not "looks good".
