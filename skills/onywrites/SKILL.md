---
name: onywrites
description: Write a blog post that reads as human-authored, or de-AI an existing draft. Use when the user gives a blog topic to write up, says a post "sounds like AI" or "reads like ChatGPT", asks to humanize/rewrite/update an old post, or wants content that will not be flagged as AI-generated. Built on StoryScope (Russell et al., COLM 2026, arXiv:2604.03136), which showed structural choices, not word choice, are what identify AI writing.
---

# Human blog writing

## The one finding that governs everything here

Russell et al. (COLM 2026) trained classifiers on 61,608 stories from human authors and five
LLMs. Two results decide how this skill works:

1. **Discourse-level structure alone identified AI at 93.2% macro-F1**, with every stylistic
   feature (word choice, rhythm, sentence shape, figurative density) withheld.
2. **Stripping surface artifacts barely helped.** They ran AI stories through a span-level
   rewriter that removed cliché, purple prose, and redundant exposition. Detection fell from
   95.5% to 93.9%. A 1.6-point drop.

So: swapping words, killing em-dashes, and banning "delve" is theater. It does not work,
and it is not the job here. **The structural decisions are made before any prose is written,
and they are the deliverable.** Word-level rules exist in this skill but they are secondary
and always come last.

Full evidence, with per-feature human/AI numbers, is in `references/evidence.md`. Load it
when calibrating a judgment call, when the user asks why a rule exists, or when auditing a
borderline draft.

## Two modes

- **Write.** User gives a topic. Run Intake → Plan → Draft → Audit.
- **Repair.** User gives an existing post/URL/file. Run Diagnose → Plan → Restructure → Audit.

Both end at the same Audit. Never skip it.

## Hard honesty rules

These are not stylistic preferences. Breaking them publishes lies under the user's name.

- **Never invent first-person experience.** No fabricated clients, jobs, failures,
  conversations, or "when I was building X."
- **Never invent specifics.** No made-up numbers, prices, dates, benchmarks, version numbers,
  quotes, study results, or named sources.
- Anything that needs the user's real input goes in as `[TK: ...]`, for example
  `[TK: what did this actually cost you?]`. Leave them visible. Do not smooth over a gap
  with plausible-sounding filler.
- If a factual claim needs a citation and none was given, mark it `[TK: source?]`.

Specificity is the highest-value human signal in the whole paper (see Intake Q3), which
means the temptation to fabricate it is strong. Resist it. A post with six `[TK:]` markers
the user fills in beats a fluent post built on invented detail.

## Voice: find the local voice file first

**Before intake, before drafting, look for a voice file in the user's working directory.**
Do not ask the user where it is and do not draft without checking. Search in this order and
read the first match, plus any blog-specific match:

```bash
find . -maxdepth 4 \( -iname "*voice*.md" -o -iname "*tone*.md" -o -iname "*style-guide*.md" \) \
  -not -path "*/node_modules/*" 2>/dev/null
```

Widen the depth or drop the name filter if that comes back empty and the repo looks like it
should have one. A voice file can be called anything.

Precedence when more than one exists:

1. A **blog-specific** voice file (`blog-voice.md`, or one whose heading says it covers
   long-form/blog writing). This is the authority for blog work.
2. A **general brand voice** file (`voice.md`, `voice-tone.md`). Use for anything the
   blog-specific file does not cover.
3. **Ignore voice files scoped to another content type.** A UI or interface voice file
   governs product copy; a case-study or portfolio voice file governs those. Take the shared
   traits (person, tone, contractions, attitude), ignore their format rules. The same writer
   sounds the same across formats; only the format changes.
4. A `my-writing-style` skill, if one exists.
5. Nothing found → say so, then offer once to read 2–3 published posts and extract a voice
   profile before drafting. Do not keep asking.

Read the voice file **in full**. Say which file you loaded before you draft.

**If a local voice file exists, pull it and follow it. Do not write from this skill's
defaults while an unread voice file is sitting in the folder.**

This skill is site-agnostic. Voice files are not. A voice file belongs to one website, so
work out which site the post is for before applying one, and never carry one site's voice
into another site's post. When a repo holds several sites, use the voice file nearest the
post you are writing, not merely the first one the search returns. If it is ambiguous which
site the post is for, ask.

Published posts sitting beside a voice file are usable as voice samples. Read two or three
when the voice file is thin on tone.

### When the voice file and this skill disagree

The voice file wins on **tone, diction, formatting, headings, SEO/AEO, schema, meta, links
and CTAs**. This skill wins on **structure**: angle, entry point, unresolved thread,
digression, uneven section weight, no moralizing closers, no epilogue.

One real conflict to expect: a voice file that specifies a **fixed article template or a
per-item pattern** for roundups and listicles. Follow the template. Consistency is the
point of a roundup, and breaking it damages the post. Apply this skill's anti-uniformity
rules *inside* each item instead: vary what goes in the slots, vary item length, let some
entries run short and one run long, and put the honest verdict where the template expects a
benefit. Never break a required per-item skeleton in the name of looking human.

If the conflict is genuinely unresolvable, raise it rather than silently picking a side.

---

## Mode A: Write

### 1. Intake

Ask these before drafting. Batch them in one message. If the user answers only some, proceed
with `[TK:]` markers rather than stalling, but tell them which answers would have mattered
most.

1. **Topic, reader, and the action** you want the reader to take.
2. **What do you know about this firsthand?** A job, a client, a migration, a bug, a bill,
   a thing you shipped. This is the raw material; without it the post will be generic no
   matter how it is phrased.
3. **Named specifics you can use.** Actual tools and version numbers, prices, dates, place
   names, people, competitor names, real numbers. Humans name things at roughly double the
   AI rate (47% vs 24% explicit named reference); AI defaults to vague allusion (72% vs 50%).
4. **What do most posts on this topic get wrong, or refuse to say?** The post needs a
   position, not a summary.
5. **Where did you fail, guess, or stay unsure?** What still does not work? What would you
   do differently? Human writing carries unresolved threads; AI resolves everything.
6. **Constraints.** Length, target keyword, CTA, publishing platform, internal links.

### 2. Structural plan

Write this out and show it to the user before drafting. It is short, about a dozen lines. Every
item below is a decision, not a suggestion.

- **Angle.** List the three angles every post on this topic already takes. Discard all three.
  Human writing sits in rarer regions of feature space (rarity percentile 0.71 vs 0.49); the
  obvious angle is the AI angle.
- **Entry point.** Do not open with a definition, market context, or "in today's landscape."
  Open in the middle, at the moment it broke, at the number that surprised you, at the
  conclusion. Then go back and fill in. Humans use nonlinear framing and time jumps
  measurably more than AI does.
- **The unresolved thread.** Name one thing you will not resolve: a tradeoff you won't
  settle, a case where your advice fails, something you still don't understand. Carry it
  through the post and leave it open at the end. AI resolves via tidy internal understanding
  47% of the time vs 27% for humans; morally ambivalent framing runs 59% human vs 38% AI.
- **One digression.** A tangent that connects thematically but is not strictly necessary.
  79% of AI stories have no subplot at all, against 57% of human ones.
- **Uneven shape.** Plan section lengths deliberately unequal. Some one paragraph, some
  six. Never a uniform run of same-weight H2 blocks. Uniform section rhythm is one of the
  loudest structural tells.
- **Concrete inventory.** List the named entities from Intake Q3 you will actually place,
  and roughly where.
- **Reader address.** Plan at least two moments of direct address or aside, acknowledging
  the reader is skimming, skeptical, or has already tried the obvious fix. Humans address the
  reader directly 28% of the time vs 7% for AI. As the paper puts it, AI "writes as though no
  one is watching."

### 3. Draft

Structure is already fixed. Now the prose-level rules, in priority order.

**Do not explain your own point.** This is the largest single human/AI gap in nonfiction-
transferable terms. AI narrators state the theme explicitly 77% of the time vs 52% for
humans, and score 3.94 vs 3.28 on thematic explicitness. Concretely:

- Ban: "This shows that", "The lesson here is", "At the end of the day", "Ultimately",
  "What this means for you is", "The key takeaway is", "In essence".
- No section may end by restating what the section just demonstrated. **Draft the section,
  then delete its final sentence**. That sentence is almost always the moralizing one.
- Trust the reader to draw the conclusion. Show the thing; stop.

**Name the feeling; don't perform it.** Counterintuitive but strongly evidenced: humans use
plain emotion labels 29% of the time vs 8% for AI, while AI conveys emotion through embodied
metaphor 81% vs 38%. Write "this was annoying" or "I was stuck for two days," not "a familiar
frustration settled in my chest."

**Cut the atmosphere.** AI over-describes sensory environment across every measure: sensory
density 3.93 vs 3.66, olfactory imagery 82% vs 57%, setting-as-psychological-mirror 4.07 vs
3.58. Delete scene-setting paragraphs. No "the glow of the monitor at 2am." No weather.

**Let the causal chain break.** AI causal continuity runs 4.20 vs 3.92. Real work has dead
ends: "I tried X. It didn't work, and I still don't know why. I did Y instead." Do not
retrofit a clean narrative of cause and effect onto messy work.

**No balance theater.** Skip staged "some argue X, while others contend Y" framing. AI uses
dialogue for philosophical debate 59% of the time vs 34% for humans. Take the position.

**Get to it.** Don't build investment before the point arrives. Cut throat-clearing openings.

**No unnecessary dashes or hyphens.** House rule, non-negotiable, applies to every draft.

- **Never use an em dash (—).** Not once. It is the most recognisable AI punctuation tell and
  the user does not want it. Replace with a full stop, a comma, a colon, or brackets. Two
  short sentences almost always beat one dashed sentence.
- **Never use an en dash (–) as a dash.** Number and date ranges only ("2021–2024"), and even
  there "to" reads better in prose.
- **No double hyphen (--) standing in for a dash.** Same rule.
- **Hyphenate only where the meaning requires it.** Keep them in established compounds
  (real-time, third-party, plug-in) and in compound adjectives before a noun where dropping
  the hyphen changes the sense ("a well-known plugin", "60-second install"). Drop them
  everywhere else: after the noun ("the plugin is well known"), after adverbs ending in -ly
  ("a highly rated plugin", never "highly-rated"), and in stacked coinages invented for
  effect ("a set-it-and-forget-it-style workflow").
- Do not swap the em dash for a semicolon everywhere instead. That is the same tic wearing a
  different hat. Use full stops.

Run a literal search for `—`, `–` and `--` before delivering. Zero hits, every time.

**Last, and least: other surface tells.** "Delve", "tapestry", "landscape", "realm",
"testament to", "navigate the complexities", "in today's fast-paced world", tricolon
everywhere, and every sentence the same length. Fix these on a final pass. The paper is
explicit that these tells are *fleeting*, since models change them release to release, so
never let this list stand in for the structural work above.

### 4. Correct for Claude specifically

This skill runs on Claude, and the paper fingerprinted each model. Claude's profile was the
most distinctive of the five LLMs. Apply these as a deliberate pass:

- **Flat escalation.** Claude's single strongest fingerprint (SHAP 0.402, uniqueness ratio
  22.4, the highest in the paper). Everything sits at one register. Fix: make one section
  noticeably hotter than the rest: blunter, angrier, more urgent, or much shorter.
- **Low beat diversity** (0.491, 10.7). Claude repeats the same move. Fix: deliberately mix
  modes: a short story, a table, a blunt list, a quoted line, a code block, a one-sentence
  paragraph standing alone.
- **Epilogue endings** (uniqueness 8.9). Claude tacks on a tidy "where things stand now"
  coda. Fix: cut it. End on the last real point, or on the open question from the plan.
- **Reverence toward convention.** Claude takes a continuist stance toward tradition in 62%
  of stories vs 39–56% for other models. Fix: the post must disagree with something the
  field takes for granted, by name.
- **Uniform voice, quiet endings.** Claude avoids sharp turns. Let one land.

### 5. Audit

Run this before delivering, every time. Score each line pass/fail against the draft.

| # | Check | Fails if |
|---|-------|----------|
| 1 | Non-obvious angle | The post could be swapped with any top-10 result for the keyword |
| 2 | Non-linear entry | Opens with definition, context-setting, or "in today's world" |
| 3 | Unresolved thread | Every question raised gets answered |
| 4 | Digression present | Every paragraph is load-bearing |
| 5 | Uneven sections | Section lengths are within ~20% of each other |
| 6 | Named specifics | Fewer than 5 real named entities, or generic stand-ins ("a popular plugin") |
| 7 | Direct reader address | Fewer than 2 instances |
| 8 | No moralizing closers | Any section ends by restating its own point |
| 9 | Plain emotion labels | Feelings rendered as bodily metaphor |
| 10 | No atmosphere padding | Any paragraph exists mainly to set a scene |
| 11 | Intensity varies | Every section sits at the same register |
| 12 | No epilogue | Ends with a tidy wrap-up coda |
| 13 | Dashes | Any `—`, `–` or `--` present, or hyphens used where meaning doesn't need them |
| 14 | Voice file | Local voice file was not searched for, or not followed on tone and format |
| 15 | Honesty | Any invented specific, experience, or source survives unmarked |

**If 3 or more of checks 1 to 12 fail: rewrite structurally. Do not fix them word by word.**
That is exactly the intervention the paper showed to be worth 1.6 points. Go back to the
plan, change the decisions, redraft.

Checks 13, 14 and 15 are not scored, they are gates. Any one of them failing blocks delivery
on its own. Fix it first, then re-run the table.

Report the audit result to the user with the draft: which checks passed, what you changed on
revision, and every `[TK:]` still outstanding.

---

## Mode B: Repair an existing post

1. **Read the whole post first.** If a URL, fetch it. If a file, read all of it.
2. **Diagnose against the Audit table** and report the diagnosis *before* rewriting. Quote
   the specific passages that fail and name the check they fail. The user should see what was
   structurally AI about it, not just receive a new draft.
3. **Ask for the missing raw material**: the named specifics and firsthand experience the
   post lacks (Intake Q2, Q3, Q5). A repair cannot manufacture these. This is usually the
   step that decides whether the rewrite is worth anything.
4. **Restructure, don't reword.** Reorder sections. Cut every moralizing closer. Break the
   symmetry. Move the real insight out of the middle where it is buried. Add the unresolved
   thread. Delete the atmosphere and the epilogue.
5. **Preserve deliberately:** factual claims, the target keyword and heading structure if the
   post already ranks, any genuinely specific detail already present, internal links.
6. **Run the Audit** and report as in Mode A.

For a post that already ranks, say so plainly if a restructure risks the ranking, and offer
the narrower option: fix checks 6, 8, 9, 10 and 12 only, which are largely local edits.
