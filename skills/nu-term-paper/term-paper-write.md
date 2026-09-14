# term-paper-write — NU (জাতীয় বিশ্ববিদ্যালয়) Bangla term paper, end to end

**Trigger:** the user gives a term-paper title (Bangla, sociology / social-problem style, e.g. “X — একটি সমাজতাত্ত্বিক বিশ্লেষণ”) and wants the full paper.
**Outcome:** a submission-ready NU-format Bangla term paper (.docx Unicode + PDF + Bijoy/SutonnyMJ copy), a source-verification sheet, a README, delivered as files and (if asked) as a native Google Doc — built exactly the way the first paper produced with this system (September 2026, gender-based cyberbullying on social media) was built.

Everything below is the checklist. Do not skip phases; do not improvise the template. Where this file says *verbatim*, copy the string exactly.

Folder layout of this skill (`$SKILL` = this folder):

```
nu-term-paper/
├── SKILL.md                       ← Claude Code entry point
├── term-paper-write.md            ← this playbook
├── skeleton/                      ← copy these to start a new paper (front.js + paper-part1..4.txt with {{slots}})
├── tooling/                       ← build.js, pagemap.js, render.sh, verification.js, SiyamRupali.ttf, package.json
└── references/
    ├── template-analysis-original-example.md   ← analysis of the scanned example paper the template was derived from
    ├── handwritten-sample-aims-migration.md    ← transcription of a handwritten 10-aims sample
    └── example-cyberbullying/                  ← research notes + README of the first paper built with this system
                                                  (the manuscript itself is kept private — it is a student's submission)
```

**NU crest:** the cover needs `src/nu-logo.png` (≈600×600 px, transparent). It is not redistributed here; download the crest from the Wikipedia article "National University, Bangladesh" (File: National_University,_Bangladesh_crest.svg → PNG, e.g. `rsvg-convert -w 600 -h 600`) and save it as `src/nu-logo.png`. If it is missing, `build.js` will fail at the cover — add the file, don't remove the ImageRun.

---

## Quick start (the whole run in 14 steps)
1. Read any example/slides/handwritten samples the user attaches — fully, page by page; transcribe handwriting into `reference/` before using it.
2. Intake rounds 1–2 (Phase 1). Apply defaults on "just go".
3. `mkdir` project, copy `skeleton/` + `tooling/`, `npm install` (Phase 2).
4. Decide the 8 ch.4 section titles for this topic (Phase 4.2 / 4.6) and write them into `front.js` toc + the `## ৪.x` headings.
5. Research (Phase 3): fill `research-notes.md` with keys; stop when every planned sub-point has ≥1 verified figure and ২.২ has ≥3 Bangladesh peer-reviewed studies.
6. Write part1 → part4 into the skeleton slots (Phase 5), footnote keys as you go, bibliography last.
7. Build preview → render → pagemap → final Unicode + Bijoy + PDF (Phase 6). Look at 5 pages.
8. Fix overflow/length; rebuild until front matter = 6 pages and body within budget.
9. `verification.js` rows → build the sheet (Phase 7).
10. README + folder hygiene (Phase 8). SendUserFile.
11. If asked: Google Docs upload + Save as Google Docs + rename (Phase 9). Ask before binning anything.
12. Final message: files, how it follows the template, before-you-submit list, honest page count.
13. Update memory (Phase 10).
14. Follow-ups (e.g. "add 10 aims"): edit the manuscript slot, rebuild all three outputs + pagemap, re-send, re-upload as a new Doc and offer to bin the old one.

---

## 0. Definition of done (check every box before saying "finished")

- [ ] Two intake rounds asked (Phase 1) or explicit "just go" received → defaults applied.
- [ ] Research notes file exists; every number in the paper traces to a line in it with a URL and a "how verified" note.
- [ ] Manuscript follows the structure spec in Phase 4 exactly (6 front pages, 5 chapters, ১.১–৫.৩ numbering, 10 aims, 8 sections in ch.4, 15 recommendations, গ্রন্থপঞ্জি).
- [ ] Every quoted scholar/organisation appears in গ্রন্থপঞ্জি; গ্রন্থপঞ্জি contains nothing that is not cited.
- [ ] Every statistic/quote has a footnote (once per paragraph; consecutive repeats = প্রাগুক্ত।).
- [ ] Built with tooling: Unicode .docx (Siyam Rupali), PDF, Bijoy .docx; rendered and eyeballed (cover, TOC, a body page with footnotes, a table page, bibliography).
- [ ] Front matter is exactly 6 pages; TOC page numbers computed by pagemap (two-pass build).
- [ ] Body length reported honestly (Siyam pages ≈ 1.35 × SutonnyMJ pages) with the quickest cuts named.
- [ ] Source-verification sheet .docx built; README written; out/ folder contains only deliverables + font.
- [ ] Files sent with SendUserFile; Google Doc created if requested (Phase 9) and leftovers handled with permission.
- [ ] Memory updated (project + any new feedback).

---

## 1. Intake (ask before writing — the user explicitly wants this)

Read the title. If the user attached an example paper or department slides, read them fully first (PDF pages ≤20 per Read; scanned Bangla needs `brew install poppler`). Then ask **round 1** with AskUserQuestion (4 questions):

1. **Format** — Word .docx Unicode (Recommended) / Bijoy .docx / Google Docs / plain text.
2. **Length** — ~25–30 body pages (Recommended; NU honours guideline says 20–25) / ~20 / 35+.
3. **Citations** — footnotes + গ্রন্থপঞ্জি like the example (Recommended) / bibliography only / APA in-text.
4. **Personal details** — keep [placeholders] (Recommended) / user supplies name, roll, reg, class roll, session, college, district, supervisor, dept head, month/year.

**Round 2** (4 questions):

5. **Ch.4 outline** — the 8-section outline in Phase 4 (Recommended) / mirror the example's two-halves pattern.
6. **Data recency** — verifiable published reports first, newspapers only with exact article (Recommended) / newest numbers even from newspapers.
7. **NU Bangla textbooks** (সামাজিক সমস্যা; সমাজবিজ্ঞান পরিচিতি, লেখাপড়া প্রকাশনী) — cite with [পৃষ্ঠা] placeholders (Recommended) / skip / user sends page numbers.
8. **Verification sheet** — yes (Recommended) / no.

**Round 3** only if the department requires SutonnyMJ (it does — NU slide): 9. Unicode + Bijoy-converted copy (Recommended) / Unicode only. 10. Extra front pages: inside cover + ঘোষণা পত্র (required by NU slide; add both), abstract (skip unless asked).

If the user dismisses a round or says "not sure": use the (Recommended) options and say so in one line. Preferences observed with the original user (good defaults): **content over font fidelity; plain, easy Bangla; ask questions first; placeholders for personal details.**

NU department rules (from the user's slides, apply always): computer-composed print, **A4**, Bangla in **SutonnyMJ/SutonnyEM** (English in Times New Roman), **1.5 line spacing**, **heading 14pt bold, sub-heading 13pt bold, body 12pt, গ্রন্থপঞ্জি/appendix 10–11pt**, cover shows title + student name/roll + supervisor name/designation + preparation date, an **inside cover page**, a **student's declaration**, a **supervisor's approval**, book binding. Specimen: Ch1 3–4 pp, Ch2 3–4, Ch3 2, Ch4 10–14, Ch5 2–3; body 20–25 pp excluding bibliography.

---

## 2. Setup (5 minutes)

```bash
# new project folder next to the system
SKILL="$(dirname "$(realpath "$0")")"   # or the absolute path of this skill folder
P="$HOME/term-papers/term-paper-<slug>"
mkdir -p "$P/src" "$P/out"
cp "$SKILL/skeleton/"* "$P/src/"
cp "$SKILL/tooling/"{build.js,pagemap.js,render.sh,verification.js} "$P/src/"
# add src/nu-logo.png yourself (see note above)
cp "$SKILL/tooling/package.json" "$P/"
cd "$P" && npm install          # docx, @codesigntheory/bnunicode2ansi, bijoy2unicode
chmod +x src/render.sh
```

One-time machine prerequisites (already done on this Mac; re-check with `ls`):
- `brew install poppler` (pdftoppm/pdftotext) and `brew install --cask libreoffice`.
- Siyam Rupali font (`tooling/SiyamRupali.ttf`) in **both** `~/Library/Fonts/` and `/Applications/LibreOffice.app/Contents/Resources/fonts/truetype/` (LibreOffice headless on macOS only sees its bundled font dir; the docx skill's `soffice.py` wrapper forces svp mode and sees even less — **always render with `src/render.sh`**, which calls the native binary).
- Start the scratchpad notes file: `research-notes.md` (Phase 3 format) and keep it updated as you go — context can be compacted mid-task.

---

## 3. Research protocol (the longest phase — 60–90 minutes)

### 3.1 What to collect (map to sections)
| Need | Typical Bangladesh source | Typical global source |
|---|---|---|
| Scale / access numbers (১.১, ৪.১) | BTRC monthly subscriber data (via BSS/Xinhua/Daily Star), **BBS** ICT/household surveys (New Age/BSS/Observer write-ups), DataReportal "Digital 20XX: Bangladesh", NapoleonCat | ITU, World Bank |
| Victim / prevalence figures (৪.১, ৪.৫) | CCAF *Cybercrime Trends in Bangladesh* (annual, TBS write-up), ActionAid Bangladesh surveys (Dhaka Tribune/UNB/TBS), Police Cyber Support for Women (Prothom Alo Eng), BLAST/ASK/Mahila Parishad, Manusher Jonno, NETZ | Plan International *Free to Be Online?* 2020, EIU 2021, UN Women, Pew |
| Peer-reviewed studies (২.২ and throughout) | **Google Scholar via the in-app browser** (`scholar.google.com/scholar?hl=en&q=...`) → then Crossref API for exact metadata: `https://api.crossref.org/works?query.bibliographic=<title+authors>&rows=2` → open-access PDFs (White Rose eprints, Springer/BMC, ResearchGate) → `pdftotext -layout file.pdf out.txt` and grep the Results tables | same |
| Law (২.১, ৪.৬) | **bdlaws.minlaw.gov.bd** via browser: `act-details-NNNN.html` (title page with act number/date), `act-NNNN.html` (section index), `act-NNNN/section-NNNNN.html`. Always check the *current* act — ordinances get re-enacted (e.g. সাইবার সুরক্ষা অধ্যাদেশ ২০২৫ → সাইবার সুরক্ষা আইন ২০২৬, Act 81, 10 Apr 2026, deemed effective 21 May 2025). Check the repeal section and the cognizable/bailable/compoundable section. | — |
| Conviction / enforcement | Siddiqua 2024 (IJHSSE 11(7)) for Dhaka Cyber Tribunal 2.86%; Dhaka Tribune 20 Apr 2019; BenarNews 16 Mar 2021 | — |
| Definitions (২.১) | law text | Kaplan & Haenlein 2010 (p. 61), Belsey cyberbullying.ca, Hinduja & Patchin (cyberbullying.org), UNICEF, WHO gender page, UN Women EGM 2023 TF-GBV definition, Oakley 1972 p. 16 (annoakley.co.uk extract PDF) |
| Theory (৪.৪) | NU textbooks with [পৃষ্ঠা] | Walby 1990 p. 20 (six structures), Hirschi 1969 (four bonds), Becker 1963 p. 9, Goffman 1959 / 1963 p. 3, Durkheim 1893/1897, Merton 1938, Citron 2009 MLR abstract |
| Country comparisons (৪.৮) | — | Plan International country press releases (Philippines 68 %, Australia 65 % w/ perpetrator split), eSafety Commissioner (est. 2015, Online Safety Act 2021), EIU |

### 3.2 Tool tactics that worked
- **WebSearch** first for each claim; it returns summaries + URLs. Then **verify on the page**.
- **WebFetch** fails with 403 on Daily Star, TBS, Financial Express, BSS, Dhaka Tribune (sometimes), Prothom Alo. For those use the **in-app browser**: `preview_start {url}` once, then `browser_batch` with `navigate` + `get_page_text` (max_chars 6000–12000). Google Scholar, bdlaws, UNICEF, Merriam-Webster, Plan International, Springer, eSafety all read fine in the browser. ACM DL and tandfonline show a bot wall — use Crossref/Semantic Scholar/White Rose instead.
- **Semantic Scholar** for abstracts: `https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,abstract,year,venue,authors` (WebFetch works).
- **PDF reports**: `curl -sL -o x.pdf <url>` then `pdftotext -layout x.pdf x.txt` then `grep -n -i` for percentages/keywords; read the exact lines (`sed -n a,bp`). Do not rely on WebFetch's PDF summariser — it returns "binary data".
- Wikipedia is acceptable only for the NU logo and dates of well-known launches; prefer BCS blog / Daily Star for BD internet history (VSAT Jun 1996, SEA-ME-WE 4 May 2006, 4G 19 Feb 2018).

### 3.3 Verification rules (non-negotiable)
1. A number goes in the paper only if you saw it on a page/PDF you can name. Record: figure → source → URL → how verified → date.
2. Prefer the primary report or peer-reviewed paper; a newspaper is acceptable when it is the only public write-up of a report (say so in the sheet).
3. When two sources disagree, keep both with their exact framing (e.g. PCSW 42,642 *complaints* to Dec 2024 vs 60,808 *women who sought help* to May 2024) — never average or pick silently.
4. Read the methodology line: sample size, age range, period, countries (Plan International: 22 survey countries; 31 incl. qualitative; 14,071 girls 15–24). Put that in the table's "যাদের উপর জরিপ" column.
5. Drop anything you cannot trace, and list the dropped items in the verification sheet ("আগের খসড়ার যে সংখ্যাগুলো মেলানো যায়নি").
6. Quotes: verbatim, in the original language, inside “ ”; page number when you have it.
7. Laws: quote the operative clause verbatim in the Act's সাধু ভাষা; give act number, date, section.

### 3.4 research-notes.md format
```
# Verified research notes (checked YYYY-MM-DD)
## A. <theme>
- **Source name, year** URL — figure; figure; figure (exact wording of the measure)
...
## F. Dropped as unverifiable (do NOT use)
- claim — why
```
Give every source a short footnote key now (e.g. `ccaf2024`, `law2026s25`) — you will use the same keys in the manuscript.

---

## 4. Structure spec — the template (100 %)

### 4.1 Page architecture
| # | Page | Roman/Bangla no. | Notes |
|---|---|---|---|
| 1 | শিরোনাম (cover) | i (not printed) | double-line page border; "টার্ম পেপার" 26pt bold; NU crest 105×105 px; title in “ ” 15pt bold; two-column block তত্ত্বাবধায়ক ‖ উপস্থাপনায় separated by a vertical rule; bottom rule + সমাজবিজ্ঞান বিভাগ / [কলেজ], [জেলা]। / [মাস] [সাল] ইং |
| 2 | ইনসাইড কাভার পেজ | ii | identical content, no page border |
| 3 | ঘোষণা পত্র | iii | one paragraph (verbatim in skeleton front.js) + student signature block + "তত্ত্বাবধায়ক কর্তৃক প্রত্যয়িত" block |
| 4 | অনুমোদন পত্র | iv | one paragraph (verbatim) + তত্ত্বাবধায়ক block + বিভাগীয় প্রধান block |
| 5 | মুখবন্ধ | v | two paragraphs (verbatim formula) + student name |
| 6 | সূচিপত্র | vi | 3-column bordered table; chapter bands shaded; page numbers in Bangla numerals |
| 7… | body | ১, ২, … | footer page number centred |
| last | গ্রন্থপঞ্জি | continues | 10.5pt, hanging indent |

Front matter must fit in exactly 6 pages (check `__bodyStartPdfPage: 7` in pagemap output).

### 4.2 Chapter/section skeleton (headings verbatim, visarga ঃ at the end)
```
প্রথম অধ্যায়
  ১.১  পটভূমিঃ                         3–4 pages, 4 paragraphs (scene / history / scale / term+evidence)
  ১.২  সমস্যার বিবরণঃ                   ~1 page, 2 paragraphs (fixed opening & closing formulas)
  ১.৩  লক্ষ্য ও উদ্দেশ্যঃ               lead paragraph + 10 numbered aims "(১) … করা।"
দ্বিতীয় অধ্যায়
  ২.১  প্রত্যয় সমূহের কার্যকরী সংজ্ঞাঃ  3–4 terms; each: plain definition + 2–3 named quoted definitions with (উদ্ধৃতি- …)
  ২.২  সাহিত্য পর্যালোচনাঃ             5–6 scholar paragraphs + "উপরের গবেষণাগুলো থেকে তিনটি বিষয় স্পষ্ট হয়…" paragraph
তৃতীয় অধ্যায়
  ৩.১  তথ্যের প্রকৃতিঃ  ৩.২  তথ্যের উৎসঃ  ৩.৩  ব্যবহৃত পদ্ধতিঃ   (fixed text, ~1 page total)
চতুর্থ অধ্যায়   (10–14 pages)
  ৪.১  বাংলাদেশে [context] ও [TOPIC]-এর পরিস্থিতিঃ     intro + ক–ঙ + Table 1 + "উপরোক্ত সারণি থেকে…"
  ৪.২  [TOPIC]-এর ধরনঃ                                intro + ১–৭/৮ + Table 2 + reading
  ৪.৩  [TOPIC] সৃষ্টির কারণঃ                            intro + (১)–(৭)
  ৪.৪  সমাজতাত্ত্বিক তত্ত্বের আলোকে বিশ্লেষণঃ           intro + ক–ঙ (5 theories)
  ৪.৫  [TOPIC]-এর প্রভাব ও ফলাফলঃ                      intro + ১–৬ + summary paragraph
  ৪.৬  আইনি কাঠামো ও প্রাতিষ্ঠানিক প্রতিকার ব্যবস্থাঃ    intro + law Table + ক. আইনি কাঠামো / খ. প্রাতিষ্ঠানিক ব্যবস্থা / গ. কাঠামোর দুর্বলতা
  ৪.৭  [TOPIC] প্রতিরোধের উপায়ঃ                       intro + (১)–(৭)
  ৪.৮  [TOPIC] পরিস্থিতির বিভিন্নতাঃ                   বাংলাদেশ + 2 countries (+ optional বৈশ্বিক চিত্র) + comparison Table + reading
পঞ্চম অধ্যায়
  ৫.১  সারাংশঃ        one dense paragraph re-stating the numbers
  ৫.২  সুপারিশমালাঃ   lead line + exactly 15 items "১. … করতে হবে।", #15 is the "local realities, not imported policy" item
  ৫.৩  উপসংহারঃ       one paragraph with the fixed closing move
গ্রন্থপঞ্জি          numbered ১) ২) …; Bangla books → English books → journal articles → reports → laws → newspapers → websites
```
Sub-point label conventions: **ক. খ. গ.** for "picture/situation" and theory sections; **১. ২. ৩.** for types and impacts; **(১) (২)** for causes, remedies and the aims. Sub-heading text ends with " ঃ" (space + visarga). Intro sentence of every ch.4 section ends "…আলোচনা করা হলো।" or "…আলোচনা করা হলোঃ".

### 4.3 Tables (4 in the paper)
`[TABLE] <title> ঃ` line → header row → rows → `[/TABLE] উৎসঃ <sources>।` → a paragraph starting **"উপরোক্ত সারণি থেকে লক্ষ্য করা যায় যে, …"**. Numeric cells centred automatically. Tables: ৪.১ gender picture (সূচক | পুরুষ | নারী | উৎস ও সাল), ৪.২ official breakdown by type, ৪.৬ laws (আইনের নাম | সাল | সংশ্লিষ্ট প্রধান বিষয় | বর্তমান অবস্থা), ৪.৮ regional comparison (অঞ্চল / দেশ | % | যাদের উপর জরিপ | উৎস).

### 4.4 Footnotes & bibliography
- Marker `{{fn:key}}` immediately after the sentence's দাড়ি; one per source per paragraph (build.js drops duplicates in the same paragraph and prints **প্রাগুক্ত।** for consecutive repeats).
- Footnote text pattern (10pt): `Author/Org, Title, place/journal, year, পৃষ্ঠা নং N।` or `Outlet, ‘Headline’, date।` — short, one line where possible.
- Inline `(উদ্ধৃতি- Author, Work, year, পৃষ্ঠা নং N)` is used **only** in ২.১ and ২.২ (that is the example's convention); everywhere else footnotes.
- গ্রন্থপঞ্জি entry formats (see skeleton part4). English titles italic via `*…*`. Bangla months/years in Bangla numerals; English sources keep Western digits.
- Every source quoted anywhere must be in গ্রন্থপঞ্জি; remove entries whose text was cut (renumber).

### 4.5 Numbers, language, typography
- Bangla numerals everywhere in Bangla text (২০২৬, ৫৯ শতাংশ, ৭৮.৭৮%); "শতাংশ" in prose, "%" in tables. Write decimals in prose as "৭৮ দশমিক ৭৮ শতাংশ".
- English loanwords/technical terms may stay in Latin script (Cyberbullying, ICTD, DOI) — build.js sets Times New Roman for Latin runs automatically; quotes “ ” ‘ ’ and dashes —/– are treated as Latin so they render correctly in the Bijoy copy too.
- A4; margins top/bottom 1", left 1.25", right 1"; 1.5 line spacing; headings 14/13/12pt; body 12pt; footnotes 10pt; bibliography 10.5pt; tables 11pt.

### 4.6 Adapting chapter 4 to the topic type
The 8-section shape is fixed; only the *labels* change. Pick the row that matches the title and keep ৪.৪ (theory) and ৪.৮ (বিভিন্নতা) always.

| Topic type | ৪.১ | ৪.২ | ৪.৩ | ৪.৫ | ৪.৬ | ৪.৭ |
|---|---|---|---|---|---|---|
| Deviance / violence / harassment (cyberbullying, eve-teasing, drug abuse, child marriage) | বাংলাদেশে … পরিস্থিতি | …-এর ধরন | … সৃষ্টির কারণ | …-এর প্রভাব ও ফলাফল | আইনি কাঠামো ও প্রাতিষ্ঠানিক প্রতিকার ব্যবস্থা | … প্রতিরোধের উপায় |
| Economic / demographic process (migration, remittance, urbanisation, unemployment, poverty) | বাংলাদেশে … বর্তমান পরিস্থিতি ও প্রবণতা | …-এর ধরন ও প্রকৃতি | … সৃষ্টির কারণ | …-এর ইতিবাচক ও নেতিবাচক প্রভাব | সরকারি নীতি ও প্রাতিষ্ঠানিক ব্যবস্থা | … সমস্যা সমাধানের উপায় |
| Institution / policy (education system, health service, local government) | বাংলাদেশে … বর্তমান অবস্থা | …-এর কাঠামো ও ধরন | … সমস্যার কারণ | … সমস্যার প্রভাব | আইন, নীতি ও প্রাতিষ্ঠানিক কাঠামো | … উন্নয়নের উপায় |

Theory menu for ৪.৪ (choose 5): কার্যবাদ (Durkheim/Parsons), দ্বন্দ্ব তত্ত্ব (Marx), নারীবাদী তত্ত্ব ও পিতৃতন্ত্র (Walby), সামাজিক বন্ধন (Hirschi), লেবেলিং (Becker), অ্যানোমি/চাপ তত্ত্ব (Durkheim/Merton), নাট্যতাত্ত্বিক ও কলঙ্ক (Goffman), পুশ-পুল তত্ত্ব (Lee 1966, for migration), আধুনিকীকরণ ও নির্ভরশীলতা তত্ত্ব (for development topics), সামাজিক শিক্ষণ (Bandura, for media/violence).

For the 10 aims (১.৩), mirror `references/handwritten-sample-aims-migration.md`: aim 1 পরিস্থিতি ও প্রবণতা → ধারণা লাভ করা; aims 2–8 map one-to-one onto ৪.১–৪.৭; aim 9 বিভিন্নতা → তুলনামূলকভাবে জানা; aim 10 সম্ভাব্য করণীয় চিহ্নিত করা.

---

## 5. Writing rules (voice)

- **Plain চলিত Bangla, short sentences, common words** (বাড়ছে, ভয়, লজ্জা, থানা, জিডি, মামলা, সাজা). The user's top concern is readability and "does not read like AI".
- Keep the template's own idioms: "নিম্নে … আলোচনা করা হলো", "উপরোক্ত সারণি থেকে লক্ষ্য করা যায় যে", "এভাবে দিন দিন … বাড়তে থাকলে … বিপন্ন হতে থাকবে", "কিন্তু শুধু সরকার বা জনগণ কারো একার পক্ষে তা সম্ভব নয়", "মূলত এসব তথ্য থেকেই … ভয়াবহ রূপ লক্ষ্য করা যায়".
- Anti-AI habits: no formulaic triads every sentence, no "উল্লেখযোগ্য যে/উল্লেখ্য", no hedging stacks, vary sentence length, use concrete Bangladeshi texture (ইমো, টিকটক, মেসেঞ্জার, ৯৯৯, ইউনিয়ন ডিজিটাল সেন্টার, থানায় জিডি). Open ১.১ with a real reported scene, anonymised, footnoted.
- Let the numbers do the arguing; one interpretation sentence after each cluster of figures.
- Never invent statistics, named people, or quotes. Named officials/activists only with the article that quoted them.
- Word budget for ~28–32 SutonnyMJ pages: whole manuscript ≈ 8,000–8,500 words incl. bibliography (~600). Per part: part1 ≈ 2,300, part2 ≈ 2,900, part3 ≈ 2,300, part4 ≈ 1,300. Footnotes ≈ 90–100.
- Known converter landmine: the word **বিষণ্ন/বিষণ্ণ** crashes the Bijoy converter — write **মানসিক অবসাদ** instead. Avoid ZWNJ/ZWJ (উদ্‌ঘাটন → উদ্ঘাটন).

---

## 6. Build & QA

Manuscript markup (build.js): `=== CHAPTER: <name>` · `## ১.১  <title>ঃ` · `### ক. <sub> ঃ` · plain paragraph per line · `[TABLE] … [/TABLE] উৎসঃ …` · `=== BIBLIO: গ্রন্থপঞ্জি` then one entry per line · `=== FOOTNOTES` then `@@fn key: text`. `*italic*` supported. List-like lines `(১)`, `১.`, `১)` get a hanging indent.

```bash
cd "$P"
# 1) preview build (Siyam Rupali, placeholder TOC numbers) → render → compute page map
BN_FONT="Siyam Rupali" node src/build.js --out out/preview.docx
src/render.sh out/preview.docx                    # prints "Pages: N"
node src/pagemap.js out/preview.pdf src/pagemap.json
# 2) final builds with real TOC numbers
BN_FONT="Siyam Rupali" node src/build.js --pagemap src/pagemap.json --out "out/টার্ম পেপার - <short> (Unicode).docx"
node src/build.js --bijoy --pagemap src/pagemap.json --out "out/টার্ম পেপার - <short> (Bijoy SutonnyMJ).docx"
src/render.sh "out/টার্ম পেপার - <short> (Unicode).docx"      # PDF for the user
rm -f out/preview.*
# 3) look at it
cd out && pdftoppm -jpeg -r 70 -f 1 -l 12 "<pdf>" page   # then Read page-01.jpg (cover), page-06 (TOC), a body page, a table page
```
Tooling warnings: keep heading spacing exactly `## ১.১  পটভূমিঃ` (two spaces, visarga) — `pagemap.js` finds the body start by that string; keep `front.js` toc keys (`১.১` …) identical to the `##` numbers; never rename `=== BIBLIO:` / `=== FOOTNOTES`. The Bijoy copy cannot be visually verified on this Mac (no SutonnyMJ) — say so and ask the user to check one page.
QA checklist: cover frame + crest + two columns; TOC on one page with Bangla numerals; ঘোষণা/অনুমোদন/মুখবন্ধ each one page; footnotes at page bottom numbered continuously; tables not overflowing; bibliography hanging indents; `pagemap.json.__bodyStartPdfPage === 7`; body page count = total − 6 − bibliography pages.
Page-count honesty: Siyam Rupali lines are ~1.5 em tall vs ~1.2 em for SutonnyMJ, so **SutonnyMJ pages ≈ Siyam pages × 0.75**. Report both. Quickest cuts if too long: drop dictionary/UNICEF-type extra definitions in ২.১, drop the ৪.৫ table, shorten ৪.৮ country paragraphs, cite once per sub-section.
If the Bijoy build prints `bijoy fail: <word>`, replace that word in the manuscript (Phase 5 landmine) and rebuild.

---

## 7. Source-verification sheet
Edit the `S` array in `src/verification.js` (one row per source: #, source, what the paper uses from it, URL, how/when verified), keep sections খ (what the student must fill) and গ (number caveats + dropped claims), then `node src/verification.js`. Output: `out/উৎস যাচাই তালিকা (Source Verification).docx` (7pt-ish table, 7 pages). It is **not** part of the submission.

---

## 8. Delivery
- `out/` must contain only: Unicode .docx, Unicode .pdf, Bijoy .docx, verification .docx, `SiyamRupali (font - install once).ttf`, `README - পড়ুন.txt` (copy `references/example-cyberbullying/README - পড়ুন.txt` and adapt title/page counts). Move `pagemap.json` to `src/`.
- `SendUserFile` the Unicode .docx + PDF + Bijoy .docx (+ verification sheet the first time), `display: attach`.
- Final message: what's in each file; how it follows the template; before-you-submit list (fill [brackets], fill [পৃষ্ঠা] footnotes, Ctrl+A → F9 in Word, page-count note with the quickest cuts).

---

## 9. Google Docs (only when asked — "add it to my Google Docs")
No Google connector exists; use **Claude in Chrome** (user's own logged-in Chrome). Load tools once:
`ToolSearch select:mcp__claude-in-chrome__tabs_context_mcp,…navigate,…computer,…read_page,…find,…file_upload,…javascript_tool,…browser_batch`.

1. `tabs_context_mcp {createIfEmpty:true}` → navigate the tab to `https://drive.google.com/drive/my-drive`; screenshot to confirm the user is signed in (never sign in yourself).
2. Drive's "File upload" opens a native picker you cannot drive, and synthetic `drop` events are ignored. **Intercept instead**: run this JS once on the Drive page:
   ```js
   (() => { if (window.__ccPatched) return 'ok'; const orig = HTMLInputElement.prototype.click;
     HTMLInputElement.prototype.click = function () { if (this.type === 'file') { window.__ccInput = this; this.id = 'cc_drive_input';
       this.setAttribute('aria-label', 'cc drive upload input'); this.style.cssText = 'position:fixed;top:4px;left:4px;opacity:1;z-index:2147483647;display:block;width:320px;height:28px;';
       if (!this.isConnected) document.body.appendChild(this); return; } return orig.apply(this, arguments); }; window.__ccPatched = true; return 'patched'; })()
   ```
   Then click **New** (by coordinate ≈ (77,114) on a 1487×812 frame; `find` the "File upload" menuitem → click it) → `find "cc drive upload input"` → `file_upload {ref, paths:[docx]}` → wait 7 s → "1 upload complete" appears.
3. Get the new file's ID: `document.querySelectorAll('[data-id]')` → element whose textContent includes the filename → `data-id`.
4. Open `https://docs.google.com/document/d/<id>/edit` (opens in .DOCX compatibility mode), wait ≥10 s, **File → Save as Google Docs** (find the menuitem; click by ref). Wait 10 s + 10 s, then re-query Drive Recent for the Google-Docs-typed item with the same name → that is the native Doc; open it and scroll-check cover, TOC, a footnoted page.
5. Naming/cleanup: each upload + conversion leaves a `.docx` and a Doc. Tell the user which is final; **only move leftovers to bin with explicit permission** (File → Move to bin inside each file by ID). Rename the final Doc via the title textbox (`find "document title text box"`, click, cmd+a, type, Return). Name used: `টার্ম পেপার - <title> (চূড়ান্ত)`.
6. Never type into the document body: the find box (cmd+f) may not take focus — if text lands in the doc, Escape then cmd+z ×8 and zoom-verify.

---

## 10. Memory & wrap-up
If your Claude Code setup has persistent memory, record for the new paper: project folder, verified facts worth reusing (laws with act numbers/dates, national survey figures), and the student's open to-dos; record any new user feedback about voice or format.

---

## Appendix A — fixed template strings (verbatim; slots in {{ }})

**ঘোষণা পত্র, অনুমোদন পত্র, মুখবন্ধ** → see `skeleton/front.js` (they are built from LEVEL/DEGREE_CLAUSE constants; for honours use `অনার্স ২য় বর্ষ` / `অনার্স ডিগ্রী লাভের জন্য অনার্স ২য় বর্ষের`).

**১.২ opening:** `{{English term}} বা {{বাংলা}} কথাটি {{origin time}} চালু হলেও উন্নত বিশ্বের অভিজ্ঞতার আলোকে বাংলাদেশের মতো উন্নয়নশীল দেশের {{TOPIC}} চিহ্নিত করতে গেলে সমস্যা সৃষ্টি হবে। কেননা …`
**১.২ middle:** `{{TOPIC}} তাই এমন একটি জটিল সমস্যা যার কবল থেকে জীবনের পারিবারিক, সামাজিক, শিক্ষাগত ও অর্থনৈতিক কোনো দিকই মুক্ত নয়।`
**১.২ close:** `… এই প্রবণতা সমাজের কল্যাণকে প্রশ্নের সম্মুখীন করছে।`
**১.৩ lead:** `এই টার্ম পেপারে {{TOPIC}}-এর ফলে বাংলাদেশের {{GROUP}}-এর ব্যক্তিগত, পারিবারিক ও সামাজিক জীবনে সৃষ্ট পরিবর্তন, এর কারণ ও প্রভাব এবং প্রতিকারের সম্ভাবনাকে আলোচনার মাধ্যমে তুলে ধরা হয়েছে। সাথে সাথে সংশ্লিষ্ট সমস্যাগুলো মোকাবিলার প্রয়োজনীয়তার বিষয়টি গুরুত্বের সঙ্গে বিবেচনা করা হয়েছে। টার্ম পেপারের বিষয় হিসাবে “{{TITLE}}” নির্বাচনের লক্ষ্য ও উদ্দেশ্য নিম্নরূপঃ`
**১.৩ aims verbs:** ধারণা লাভ করা · তুলে ধরা · চিহ্নিত করা · ব্যাখ্যা দেওয়া · বিশ্লেষণ করা · অনুসন্ধান করা · মূল্যায়ন করা · তুলনামূলকভাবে জানা · সম্ভাব্য করণীয় চিহ্নিত করা (10 aims; aim 9 is always the বিভিন্নতা one; aim 10 always the করণীয় one).
**২.২ close:** `উপরের গবেষণাগুলো থেকে তিনটি বিষয় স্পষ্ট হয়। প্রথমত, …। দ্বিতীয়ত, …। তৃতীয়ত, …। বর্তমান টার্ম পেপারে এই তিনটি সূত্র ধরেই সমস্যাটি বিশ্লেষণ করা হয়েছে।`
**৩.১–৩.৩:** see skeleton (only the lists of sources/indicators change).
**ch.4 intro sentence:** `নিম্নে … সম্পর্কে আলোচনা করা হলো।` / `নিম্নে … আলোচনা করা হলোঃ`
**table reading:** `উপরোক্ত সারণি থেকে লক্ষ্য করা যায় যে, …`
**৪.৫ close:** `একটি সমস্যা অন্য সমস্যার জন্ম দেয়; … এই শৃঙ্খলই {{TOPIC}}কে একটি সামাজিক সমস্যায় পরিণত করেছে।`
**৪.৬ open:** `… কিন্তু আইন থাকা আর আইন কাজ করা এক কথা নয়। নিম্নে বিদ্যমান কাঠামো আলোচনা করা হলো।` / close of গ: `ফলে আইন থাকা সত্ত্বেও … অব্যাহত রয়েছে।`
**৪.৮ close:** `অর্থাৎ সমস্যা সর্বজনীন হলেও তার সামাজিক পরিণতি ও প্রতিকারের সুযোগ দেশভেদে ভিন্ন।`
**৫.১ frame:** `{{TOPIC}} বর্তমান সমাজের একটি আলোচিত বিষয়। মানব জীবনের কোনো দিকই এর কবল থেকে মুক্ত নয়। … মূলত এসব তথ্য থেকেই {{TOPIC}}-এর ভয়াবহ রূপ লক্ষ্য করা যায়।`
**৫.২ lead:** `{{TOPIC}} সমস্যা সমাধানের সুপারিশসমূহ নিম্নরূপঃ` — 15 items ending `…করতে হবে।`
**৫.৩ frame:** `{{TOPIC}} বর্তমান বিশ্বের একটি প্রধান সামাজিক সমস্যা। এটি মানব জীবনকে ব্যাপকভাবে প্রভাবিত করে। মানব জীবনের সামাজিক, রাজনৈতিক ও অর্থনৈতিক কোনো দিকই এর কবল থেকে মুক্ত নয়। … একটি সমস্যা অন্য সমস্যার সঙ্গে জড়িত। … তাই এটিকে প্রতিরোধ করতে হবে। কিন্তু শুধু সরকার বা জনগণ কারো একার পক্ষে তা সম্ভব নয়। তাই সরকার, …, পরিবার ও জনসাধারণ ঐক্যবদ্ধ প্রচেষ্টা গ্রহণ করে এ সমস্যা সমাধানের পদক্ষেপ নিতে হবে। তবেই … সম্ভব।`

## Appendix B — footnote & bibliography examples (copy the punctuation)
```
@@fn ccaf2024: Cyber Crime Awareness Foundation, Cybercrime Trends in Bangladesh 2024, ঢাকা, জুন ২০২৪।
@@fn ds2026: The Daily Star, ‘Laws exist, but online violence against women continues’, ১৭ এপ্রিল ২০২৬।
@@fn sheikh2023: Sheikh, Hossan and Menih, Journal of School Violence, 22(2), 2023, পৃষ্ঠা নং 198–214।
@@fn law2026s25: সাইবার সুরক্ষা আইন, ২০২৬ (২০২৬ সনের ৮১ নং আইন), ধারা ২৫।
@@fn hirschi1969: Travis Hirschi, Causes of Delinquency, University of California Press, 1969; মোহাম্মদ রফিকুল ইসলাম ও মুহাম্মদ জাকির আল ফারুকী, সমাজবিজ্ঞান পরিচিতি, পৃষ্ঠা নং [পৃষ্ঠা]।

১) আবু শামীম, শেখ মোহাম্মদ এবং সুলতানা, মোসাঃ পারভীন, *সামাজিক সমস্যা*, ঢাকা: লেখাপড়া, ফেব্রুয়ারী ২০১৩।
৪) Citron, Danielle Keats, *Hate Crimes in Cyberspace*, Cambridge, MA: Harvard University Press, 2014.
১৭) Sheikh, Md. Mamunur Rashid, Hossan, Md. Rony and Menih, Helena, ‘Cyberbullying victimization and perpetration among university students in Bangladesh: Prevalence, impact and help-seeking practices’, *Journal of School Violence*, 22(2), 2023, pp. 198–214.
২১) Cyber Crime Awareness Foundation, *Cybercrime Trends in Bangladesh 2024*, ঢাকা, জুন ২০২৪।
২৭) সাইবার সুরক্ষা আইন, ২০২৬ (২০২৬ সনের ৮১ নং আইন), আইন, বিচার ও সংসদ বিষয়ক মন্ত্রণালয়, bdlaws.minlaw.gov.bd/act-details-1710.html
৩০) The Daily Star, ‘77pc women victims of online abuse’, ২৪ নভেম্বর ২০২১; ‘Laws exist, but online violence against women continues’, ১৭ এপ্রিল ২০২৬, www.thedailystar.net
৩৬) World Health Organization, ‘Gender’, www.who.int/health-topics/gender (প্রবেশের তারিখ: ১৩ সেপ্টেম্বর ২০২৬)।
```

## Appendix C — pitfalls log (each cost real time once)
- WebFetch 403 on most BD newspapers → browser. ACM/T&F bot walls → Crossref/White Rose/Semantic Scholar.
- Read tool on scanned PDF needs poppler; the "93 pages" count was wrong (36); duplicated scans of the same page happen.
- LibreOffice: skill wrapper (svp) sees only bundled fonts → blank Bangla; native binary sees `~/Library/Fonts` only after copying the TTF into the app's `fonts/truetype` dir; kill stale `soffice` processes before re-rendering.
- Word footnote/page-number digits cannot be Bangla via numFmt; Unicode file shows Western digits in footers (TOC uses static Bangla text); the Bijoy copy shows Bangla digits automatically because SutonnyMJ maps ASCII digits.
- docx-js: tables need `columnWidths` + per-cell DXA widths; page border only on the cover section; `pageBreakBefore` off for the first chapter; footnote ids must be unique per reference.
- Bijoy converter: recursion overflow on long strings → convert word-by-word; normalise য়/ড়/ঢ় to precomposed; strip ZWNJ; `।`→`|`; `&h`→`¨`; fails on বিষণ্ন.
- First draft came out 9,600 words / 129 footnotes / 57 Siyam pages — cut to ~8,200 words / 96 footnotes by citing once per paragraph and trimming repeats; keep the four tables, drop the fifth.
- TOC overflowed by one row → row size 10.5pt, cell margins 15 twips, line 240.
- Drive: no `<input type=file>` exists until "File upload" is clicked; the intercept trick works; `Save as Google Docs` needs the doc fully loaded (wait ≥10 s) or nothing happens; it never overwrites → duplicates.
- cmd+f in Docs did not focus the find box once → text typed into the document → undo immediately.

## Appendix D — timing (what it actually took)
Intake 10 min · example analysis 15 min · research 90 min (≈35 sources) · writing 60 min · tooling + first build 45 min · trimming/rebuilds 40 min · verification sheet + README 15 min · Google Docs upload 20 min · follow-up (10 aims) 20 min · cleanup 10 min. Budget ≈ 5 hours for a new title with a fresh research base; ≈ 2.5 hours if the topic shares sources with an existing paper.
