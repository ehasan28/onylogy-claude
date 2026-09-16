#!/usr/bin/env python3
"""Voice gate + SEO/GEO lint for an Onylogy blog draft (.md in Blogs/<slug>/<slug>.md).

usage: audit-draft.py SLUG [--json] [--type TYPE] [--narrow]
       --narrow: repair mode "narrow fix" (structure and length kept): the word-count gate is skipped
       audit-draft.py --file path/to/post.md [--type TYPE]

Exit 0 = every GATE passes (warnings allowed). Exit 1 = at least one gate failed. Never upload a draft that exits 1.
Numbers come from references/blog-voice.md §3 (canon-derived) and references/seo-geo-checklist.md ([lint] rows).
"""
import json, os, re, sys, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))
RANGES = {  # words
    "roundup": (1100, 1500), "guide": (1200, 1800), "explainer": (1200, 1800), "pillar": (2500, 3200),
    "comparison": (1100, 1600), "deep-dive": (1500, 2200), "kadence": (1200, 1800), "mistakes": (1300, 1800),
}
REASSURE = r"\b(don'?t worry|no worries|not intimidating|plain and simple|that'?s it|that'?s cool|simple as that|you'?ve got this|you don'?t need to be|nothing to fear|easier than it sounds|takes (?:a|two|five|ten) minutes?|that'?s all|good news|the good news|relax|not as hard|not hard|dead simple|it'?s that simple|you'?re (?:done|set|covered|fine|safe)|easy|simple|no coding|no code|without (?:touching|writing) (?:any )?code|beginner-friendly|straightforward|in (?:a few |just a few |under )?minutes|the best part|you can'?t go wrong|you'?ll be fine|no tech(?:nical)? (?:skills|knowledge) (?:needed|required)|one click)\b"
TRANSITIONS = r"\b(because|so|then|first|second|third|next|finally|for example|for instance|however|but|also|instead|in short|in other words|that means|which means|as a result|meanwhile|still|besides|on top of that|either way|otherwise|once|when|if|unless|until|after|before|while|although|even if|the result|here'?s why|that'?s why|in practice|most important|above all|plus|and|or)\b"
PASSIVE = r"\b(is|are|was|were|be|been|being|get|gets|got)\s+(\w+ed|built|made|done|set|put|kept|left|found|held|shown|known|seen|given|taken|written|chosen|caught|broken|sent|paid|sold|told|run|hit|cut|read|cached|installed|hosted|backed|updated|loaded|served|blocked)\b"
AI_TELLS = ["delve", "tapestry", "landscape", "realm", "testament to", "navigate the complexities", "fast-paced world",
            "it's important to note", "at the end of the day", "ultimately", "the key takeaway is", "game-changer",
            "seamless", "robust", "leverage", "in today's", "the lesson here", "what this means for you", "in essence"]
ONYWRITES_DEVICES = [r"i (?:still )?don'?t know", r"the part every \w+ skips", r"i'?ll show my hand", r"^i (?:renamed|tested|built|set up|migrated)\b"]

def split_sents(t):
    t = re.sub(r"\b(e\.g|i\.e|vs|etc|Mr|Dr|St)\.", r"\1", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])", t) if s.strip()]

def syllables(w):
    w = w.lower(); w = re.sub(r"[^a-z]", "", w)
    if not w: return 0
    v = re.findall(r"[aeiouy]+", w); n = len(v)
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1: n -= 1
    return max(1, n)

def parse(md):
    meta = {}
    m = re.search(r"<!--\s*=+ POST META.*?-->", md, re.S)
    if m:
        key = None
        for line in m.group(0).split("\n"):
            st_ = line.strip()
            if st_.startswith(("=", "<!--", "-->")) or not st_: key = None; continue
            mm = re.match(r"^([A-Za-z][^:\n]{2,60}?):\s+(.*)$", st_)
            if key and line.startswith((" ", "\t")):
                meta[key] += " " + st_
            elif mm and not st_.startswith("STRUCTURAL"):
                key = mm.group(1).strip().lower(); meta[key] = mm.group(2).strip()
    body = md.split("-->", 1)[1] if m else md
    tail = body.rfind("<!--")
    if tail > 0: body = body[:tail]
    body = body.strip().rstrip("-").strip()
    return meta, body

def audit(md, ptype=None, narrow=False):
    meta, body = parse(md)
    lines = body.split("\n")
    h1 = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    h2 = [l[3:].strip() for l in lines if l.startswith("## ")]
    h3 = [l[4:].strip() for l in lines if l.startswith("### ")]
    subs = h2 + h3
    # paragraphs: blocks of prose (not headings, lists, tables, code, images, byline)
    paras = []; buf = []; in_code = False; lists = 0; tables = 0; images = 0
    for l in lines:
        if l.startswith("```"): in_code = not in_code; continue
        if in_code: continue
        s = l.strip()
        if not s:
            if buf: paras.append(" ".join(buf)); buf = []
            continue
        if s.startswith("#"):
            if buf: paras.append(" ".join(buf)); buf = []
            continue
        if re.match(r"^([-*]|\d+\.)\s", s): lists += 1; continue
        if s.startswith("|"): tables += 1; continue
        if s.startswith("!["): images += 1; continue
        if s.startswith("*By "): continue
        buf.append(s)
    if buf: paras.append(" ".join(buf))
    prose = " ".join(paras)
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", prose)
    plain = re.sub(r"[*_`]", "", plain).replace("’", "'")
    words_all = re.sub(r"[*_`#|>\[\]()-]", " ", body)
    wc = len(words_all.split())
    sents = split_sents(plain)
    psents = [len(split_sents(re.sub(r"[*_`]", "", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", p)))) for p in paras]
    pwords = [len(p.split()) for p in paras]
    n = max(len(plain.split()), 1)
    you = len(re.findall(r"\byou(?:r|'re|'ll|'ve|'d)?\b", plain, re.I))
    i_ = len(re.findall(r"\b(?:I|I'm|I've|I'd|I'll|my|me)\b", plain))
    qs = len(re.findall(r"\?", plain))
    reassure = len(re.findall(REASSURE, plain, re.I))
    long_s = sum(1 for s in sents if len(s.split()) > 20)
    avg_s = st.mean(len(s.split()) for s in sents) if sents else 0
    trans = sum(1 for s in sents if re.search(TRANSITIONS, s, re.I))
    passive = sum(1 for s in sents if re.search(PASSIVE, s, re.I))
    syl = sum(syllables(w) for w in plain.split())
    flesch = 206.835 - 1.015 * (n / max(len(sents), 1)) - 84.6 * (syl / n) if sents else 0
    dashes = len(re.findall(r"—|–|(?<=\s)--(?=\s)| -- ", body))
    dash_ranges_ok = len(re.findall(r"\d–\d", body))
    dashes -= dash_ranges_ok
    bolds = len(re.findall(r"\*\*[^*]+\*\*", body))
    faq_idx = next((i for i, h in enumerate(h2) if re.search(r"faq|frequently|questions", h, re.I)), None)
    faq_q = 0
    if faq_idx is not None:
        on = False
        for l in lines:
            if l.startswith("## "):
                on = re.search(r"faq|frequently|questions", l, re.I) is not None; continue
            if on and (l.startswith("### ") or re.match(r"^\*\*.+\?\*\*$", l.strip())): faq_q += 1
    concl = [h for h in h2 if re.search(r"^(conclusion|final thoughts|wrapping it up)", h, re.I)]
    takeaways = any(re.search(r"key takeaways", h, re.I) for h in h2)
    tk = re.findall(r"\[TK:[^\]]*\]", body)
    ai = [w for w in AI_TELLS if re.search(r"\b" + re.escape(w) + r"\b", plain, re.I)]
    devices = [d for d in ONYWRITES_DEVICES if re.search(d, plain + " " + " ".join(h2), re.I | re.M)]
    first_para = re.sub(r"[*_`]", "", paras[0]) if paras else ""
    anecdote_open = bool(re.match(r"^(I|My|We|Last (?:week|month|year)|In 20\d\d|This year)\b", first_para))
    # SEO
    kw = meta.get("primary keyword", "").strip().lower()
    kwre = re.compile(r"\b" + r"\W+".join(map(re.escape, kw.split())) + r"\b", re.I) if kw else None
    first100 = " ".join(plain.split()[:100])
    kw_h1 = bool(kwre and kwre.search(h1)); kw_h1_front = bool(kwre and kwre.search(h1[:max(len(h1)//2, 20)]))
    kw_first = bool(kwre and kwre.search(first100))
    slug = meta.get("slug", "")
    kw_slug = bool(kw and all(w in slug for w in re.findall(r"[a-z0-9]+", kw) if len(w) > 2))
    desc = next((v for k, v in meta.items() if k.startswith("meta description")), "")
    desc = re.sub(r"\s+", " ", desc).strip()
    kw_desc = bool(kwre and kwre.search(desc))
    desc_subs = [h for h in subs if not re.match(r"^\d+\.", h) and not re.search(r"faq|frequently|questions|conclusion|final thoughts|wrapping|key takeaways|key features|why you need|alternative|best for|the issue|the fix", h, re.I)]
    kw_subs = sum(1 for h in desc_subs if kwre and kwre.search(h)) if desc_subs else 0
    kw_sub_share = kw_subs / len(desc_subs) if desc_subs else 0
    kw_count = len(kwre.findall(plain)) if kwre else 0
    density = 100 * kw_count * max(len(kw.split()), 1) / n if kw else 0
    alt_kw = bool(kwre and kwre.search(meta.get("featured image alt", "")))
    internal = re.findall(r"\]\((/[a-z0-9-]+/[a-z0-9-]+/)\)", body)
    bare_internal = re.findall(r"\]\((/[a-z0-9-]+/)\)", body)
    external = re.findall(r"\]\((https?://(?!onylogy\.com)[^)\s]+)\)", body)
    stats_unsourced = [m.group(0) for m in re.finditer(r"[^.]{0,80}\b\d[\d,.]*\s?(?:%|percent|million|billion)\b(?:[^.(]|\([^)]*\)){0,60}", plain) if not re.search(r"\((?:[^)]*\b20\d\d\b[^)]*)\)|\b20\d\d\b|according to|source", m.group(0), re.I)]
    # gaps between subheadings (words)
    gaps = []; cur = 0; in_code = False
    for l in lines:
        if l.startswith("```"): in_code = not in_code; continue
        if in_code: continue
        if l.startswith("## ") or l.startswith("### "): gaps.append(cur); cur = 0
        elif l.strip() and not l.startswith("#"): cur += len(l.split())
    gaps.append(cur)
    ptype = ptype or meta.get("type", "").split()[0].strip("{}|") if meta.get("type") else ptype
    ptype = (ptype or ("roundup" if re.match(r"^(top \d|\d+ )", h1, re.I) else "guide")).lower()
    lo, hi = RANGES.get(ptype, (1100, 1800))

    G = []; W = []  # gates, warnings
    def gate(ok, msg): (G if not ok else []).append(msg); return ok
    def warn(ok, msg): (W if not ok else []).append(msg); return ok
    gate(you / n * 100 >= 3.0, f"'you' density {you/n*100:.2f}/100w < 3.0 (canon 2.7 to 5.9)")
    gate(i_ / n * 100 <= 0.35, f"'I/my' density {i_/n*100:.2f}/100w > 0.35 (canon ≤ 0.15; 1 to 2 experience sentences max)")
    gate(round(sum(1 for x in psents if x == 1) / max(len(paras), 1), 2) >= 0.30, f"one-sentence paragraphs {100*sum(1 for x in psents if x==1)/max(len(paras),1):.0f}% < 30%")
    gate(max(psents or [0]) <= 4, f"{sum(1 for x in psents if x>4)} paragraph(s) over 4 sentences (max {max(psents or [0])})")
    gate(max(pwords or [0]) <= 120, f"{sum(1 for x in pwords if x>120)} paragraph(s) over 120 words (Rank Math)")
    gate(avg_s <= 18, f"average sentence length {avg_s:.1f} > 18 words (canon 9 to 17)")
    warn(long_s / max(len(sents), 1) <= 0.25, f"{100*long_s/max(len(sents),1):.0f}% of sentences over 20 words (> 25%, Yoast orange)")
    gate(qs >= 1, f"no rhetorical question in the body (canon: 1 to 12)")
    warn(qs >= 3, f"only {qs} question(s) in the body (target 3+)")
    gate(reassure >= 2, f"only {reassure} reassurance beat(s) (need ≥ 2: 'plain and simple', 'that's it', 'you don't need to be…')")
    gate(dashes == 0, f"{dashes} dash(es) found (em/en dash or --); house rule is zero")
    if narrow: warn(lo <= wc <= hi, f"word count {wc} outside {ptype} range {lo} to {hi} (narrow fix: length kept on purpose)")
    else: gate(lo <= wc <= hi, f"word count {wc} outside {ptype} range {lo} to {hi}")
    gate(6 <= faq_q <= (13 if ptype == "pillar" else 7), f"FAQ has {faq_q} questions (need 6 to 7)")
    gate(bool(concl), "no Conclusion / Final Thoughts / Wrapping It Up H2")
    gate(not devices, f"onywrites structural device(s) visible: {devices}")
    gate(not anecdote_open, f"post opens with a first-person anecdote: '{first_para[:60]}…'")
    gate(bool(kw), "no Primary keyword in POST META")
    if narrow: warn(kw_h1, "primary keyword not in H1 (narrow fix keeps the live H1)")
    else: gate(kw_h1, "primary keyword not in H1")
    gate(kw_first, "primary keyword not in the first 100 words")
    kw_words = [w for w in re.findall(r"[a-z0-9]+", kw) if len(w) > 3]
    kw_slug_share = sum(1 for w in kw_words if w in slug) / max(len(kw_words), 1)
    gate(kw_slug_share >= 0.5, f"fewer than half of the keyword words are in slug '{slug}' (Rank Math: keyword in URL)")
    warn(kw_slug, f"not every keyword word is in the slug '{slug}'")
    gate(130 <= len(desc) <= 145, f"meta description {len(desc)} chars (need 130 to 145): '{desc[:60]}…'")
    gate(kw_desc, "primary keyword not in the meta description")
    gate("—" not in desc and "–" not in desc, "dash in meta description")
    gate(3 <= len(internal) <= 10, f"{len(internal)} internal links with category prefix (need 3 to 6, hard limit 10)")
    warn(len(internal) <= 6, f"{len(internal)} internal links (canon 3 to 6; fine on a hub or starter guide)")
    gate(not bare_internal, f"internal links without category prefix (will 404): {sorted(set(bare_internal))}")
    gate(len(external) >= 1, "no external link (Rank Math needs ≥ 1 followed external link)")
    gate(len(tk) == 0 or True, "")  # TKs are reported, not gated (the user fills them)
    if ptype == "roundup":
        gate(tables >= 2, "roundup has no comparison table")
        gate(not takeaways, "roundup has a Key Takeaways box (canon: guides/pillars only)")
        gate(images + len(re.findall(r"→\s*\S+\.webp", md)) >= 6, f"roundup needs ~6 item images; IMAGES block lists {len(re.findall(r'→\\s*\\S+\\.webp', md))}")
    else:
        gate(not (takeaways and wc < 1400), "Key Takeaways on a post under 1,400 words (canon: deeper guides only)")
    # warnings
    warn(kw_h1_front, "primary keyword not in the first half of the H1 (Rank Math title test)")
    warn(0.3 <= kw_sub_share <= 0.75, f"keyword in {100*kw_sub_share:.0f}% of descriptive subheadings (Yoast wants 30 to 75%)")
    warn(0.5 <= density <= 1.5, f"keyword density {density:.2f}% (Rank Math 1 to 1.5, Yoast 0.5 to 3)")
    warn(density <= 2.5, f"keyword density {density:.2f}% above 2.5% (stuffing warning)")
    warn(alt_kw, "primary keyword not in the featured image alt")
    warn(flesch >= 60, f"Flesch reading ease {flesch:.0f} < 60 (Yoast target for LLM-quotable content)")
    warn(trans / max(len(sents), 1) >= 0.30, f"transition words in {100*trans/max(len(sents),1):.0f}% of sentences (Yoast wants ≥ 30%)")
    warn(passive / max(len(sents), 1) <= 0.10, f"passive voice in ~{100*passive/max(len(sents),1):.0f}% of sentences (Yoast max 10%) [approximate]")
    warn(max(gaps or [0]) <= 300, f"a stretch of {max(gaps or [0])} words with no subheading (Yoast: every 300)")
    warn(1.0 <= bolds / n * 100 <= 3.0, f"bold density {bolds/n*100:.2f}/100w (canon 1.2 to 2.5)")
    warn(len(external) <= 3, f"{len(external)} external links (keep 1 to 3)")
    warn(not ai, f"AI-tell words: {ai}")
    warn(not stats_unsourced, f"{len(stats_unsourced)} statistic(s) without a source/year nearby: " + " | ".join(s.strip()[:70] for s in stats_unsourced[:3]))
    warn(len(h3) == 0 or len(set(h3)) < len(h3) or ptype not in ("roundup",), "roundup H3 labels are not repeated across items (canon: identical labels on every item)")
    warn(re.search(r"^\*By Ehasanul", body, re.M) is None or True, "")
    warn(len(desc_subs) == 0 or any("?" in h for h in h2), "no question-style H2 (canon signature, matches AI queries)")
    warn(len(tk) == 0, f"{len(tk)} [TK:] marker(s) to fill: " + "; ".join(t[:60] for t in tk[:5]))
    W[:] = [w for w in W if w]; G[:] = [g for g in G if g]
    summary = dict(type=ptype, words=wc, paragraphs=len(paras), you_per_100w=round(you/n*100, 2), i_per_100w=round(i_/n*100, 2),
                   one_liner_share=round(100*sum(1 for x in psents if x==1)/max(len(paras),1)), avg_sentence=round(avg_s, 1),
                   long_sentence_share=round(100*long_s/max(len(sents),1)), questions=qs, reassurance=reassure, dashes=dashes,
                   faq=faq_q, flesch=round(flesch), transitions=round(100*trans/max(len(sents),1)), passive=round(100*passive/max(len(sents),1)),
                   density=round(density, 2), internal=len(internal), external=len(external), images_listed=len(re.findall(r"→\s*\S+\.webp", md)),
                   tables=tables > 0, takeaways=takeaways, tk=len(tk), meta_desc_len=len(desc))
    return summary, G, W

def main():
    args = sys.argv[1:]
    as_json = "--json" in args; narrow = "--narrow" in args; args = [a for a in args if a not in ("--json", "--narrow")]
    ptype = None
    if "--type" in args:
        i = args.index("--type"); ptype = args[i+1]; del args[i:i+2]
    if args and args[0] == "--file": path = args[1]
    else:
        slug = args[0]; path = os.path.join(BLOGS, slug, f"{slug}.md")
    md = open(path, encoding="utf-8").read()
    summary, gates, warns = audit(md, ptype, narrow)
    if as_json:
        print(json.dumps(dict(summary=summary, gate_failures=gates, warnings=warns), indent=1)); sys.exit(1 if gates else 0)
    print(f"== {os.path.basename(path)}  ({summary['type']}, {summary['words']} words)")
    print("   " + "  ".join(f"{k}={v}" for k, v in summary.items() if k not in ("type", "words")))
    for g in gates: print("  GATE FAIL:", g)
    for w in warns: print("  warn:", w)
    print("  RESULT:", "PASS (upload allowed)" if not gates else f"FAIL ({len(gates)} gate failure(s); fix before upload)")
    sys.exit(1 if gates else 0)

if __name__ == "__main__":
    main()
