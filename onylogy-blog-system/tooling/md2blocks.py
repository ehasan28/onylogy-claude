#!/usr/bin/env python3
"""Convert Blogs/<slug>/<slug>.md into a Novamira Gutenberg block_spec of native core blocks.

usage: md2blocks.py SLUG --post-id ID --media media-ids.json --out spec-SLUG.json

- media-ids.json: {"<filename without .webp>": {"id": 123, "url": "https://onylogy.com/wp-content/uploads/2026/09/x.webp"}, ...}
  (produced by media-ids.py after the images are uploaded through the Media Library UI).
- Images are placed from the IMAGES block at the bottom of the .md:  label → file.webp  alt: "…"  [after "## Heading"]
  ("[top]" = featured image, not inserted in the body; "[after the intro]" = before the first H2).
- Internal links written as /slug/ or /category/slug/ are resolved through permalinks.json; unknown slugs abort.
- H1 and any *By …* byline line are skipped (the theme prints title, author and date).
- Output: {"post_id", "label", "agent_label", "agent_note", "block_spec": [...]} for novamira/gutenberg-add-pending-change.
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))
LINKS = json.load(open(os.path.join(HERE, "permalinks.json"))) if os.path.exists(os.path.join(HERE, "permalinks.json")) else {}
UNMAPPED = []

def esc(s): return html.escape(s, quote=False)

def inline(s):
    out = ""
    for p in re.split(r"(`[^`]+`)", s):
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out += "<code>" + esc(p[1:-1]) + "</code>"; continue
        t = esc(p)
        def link(m):
            text, url = m.group(1), m.group(2)
            mm = re.fullmatch(r"/(?:[a-z0-9-]+/)?([a-z0-9-]+)/", url)
            if mm:
                slug = mm.group(1)
                if slug in LINKS: url = LINKS[slug]["path"]
                elif url.count("/") == 2: UNMAPPED.append(url)  # bare /slug/ with no map
            return f'<a href="{url}">{text}</a>'
        t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
        out += t
    return out

def heading(level, text): return {"name": "core/heading", "attributes": {"level": level, "content": inline(text)}, "innerBlocks": []}
def para(text): return {"name": "core/paragraph", "attributes": {"content": inline(text)}, "innerBlocks": []}
def image(aid, url, alt): return {"name": "core/image", "attributes": {"id": aid, "url": url, "alt": alt, "sizeSlug": "large", "linkDestination": "none"}, "innerBlocks": []}
def code(text): return {"name": "core/code", "attributes": {"content": esc(text)}, "innerBlocks": []}
def listblock(items, ordered):
    return {"name": "core/list", "attributes": ({"ordered": True} if ordered else {}),
            "innerBlocks": [{"name": "core/list-item", "attributes": {"content": inline(i)}, "innerBlocks": []} for i in items]}
def table(rows):
    cells = lambda r, tag: {"cells": [{"content": inline(c.strip()), "tag": tag} for c in r]}
    return {"name": "core/table", "attributes": {"hasFixedLayout": True, "head": [cells(rows[0], "th")], "body": [cells(r, "td") for r in rows[1:]]}, "innerBlocks": []}

def images_for(md, media):
    seg = md[md.find("================= IMAGES"):] if "================= IMAGES" in md else ""
    after = {}; intro = None; featured = None
    for line in seg.split("\n"):
        m = re.match(r'^(\S[^→]*?)\s*→\s*(\S+)\s+alt:\s*"([^"]+)"\s*\[(.+?)\]', line)
        if not m: continue
        label, fn, alt, place = m.group(1).strip(), m.group(2), m.group(3), m.group(4)
        key = os.path.basename(fn)[:-5] if fn.endswith(".webp") else os.path.basename(fn)
        if place == "top" or label.lower() == "featured": featured = (key, alt); continue
        if key not in media: raise SystemExit(f"no media id for {fn} (upload it first, then media-ids.py)")
        item = (media[key]["id"], media[key]["url"], alt)
        pm = re.search(r'after "([^"]+)"', place)
        if pm: after.setdefault(pm.group(1), []).append(item)
        elif "intro" in place: intro = item
        else: print(f"  ?? unknown placement for {fn}: [{place}]", file=sys.stderr)
    return after, intro, featured

def convert(slug, media):
    md = open(os.path.join(BLOGS, slug, f"{slug}.md"), encoding="utf-8").read()
    after, intro, featured = images_for(md, media)
    body = md.split("-->", 1)[1] if md.lstrip().startswith("<!--") else md
    tail = body.rfind("<!--")
    if tail > 0: body = body[:tail]
    lines = body.rstrip().rstrip("-").rstrip().split("\n")
    blocks = []; i = 0; used = set(); intro_done = intro is None
    while i < len(lines):
        ln = lines[i]
        if not ln.strip(): i += 1; continue
        if ln.startswith("# ") or re.match(r"^\*By Ehasanul Haque", ln): i += 1; continue
        if ln.startswith("```"):
            buf = []; i += 1
            while i < len(lines) and not lines[i].startswith("```"): buf.append(lines[i]); i += 1
            i += 1; blocks.append(code("\n".join(buf))); continue
        m = re.match(r"^(#{2,4}) (.+)$", ln)
        if m:
            if not intro_done: blocks.append(image(*intro)); intro_done = True
            blocks.append(heading(len(m.group(1)), m.group(2).strip()))
            for prefix, items in after.items():
                if ln.startswith(prefix) and prefix not in used:
                    for it in items: blocks.append(image(*it))
                    used.add(prefix)
            i += 1; continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                r = lines[i].strip().strip("|").split("|")
                if not all(re.fullmatch(r"\s*:?-+:?\s*", c) for c in r): rows.append(r)
                i += 1
            blocks.append(table(rows)); continue
        if re.match(r"^[-*] ", ln):
            items = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i]): items.append(lines[i][2:].strip()); i += 1
            blocks.append(listblock(items, False)); continue
        if re.match(r"^\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]): items.append(re.sub(r"^\d+\. ", "", lines[i]).strip()); i += 1
            blocks.append(listblock(items, True)); continue
        if ln.startswith("!["):  # markdown image line: resolved through IMAGES block placement instead
            i += 1; continue
        buf = [ln]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6} |[-*] |\d+\. |\||```|!\[)", lines[i]):
            buf.append(lines[i]); i += 1
        blocks.append(para(" ".join(b.strip() for b in buf)))
    missing = [p for p in after if p not in used]
    return blocks, missing, featured

def main():
    a = sys.argv[1:]
    slug = a[0]; pid = int(a[a.index("--post-id") + 1]); media = json.load(open(a[a.index("--media") + 1]))
    out = a[a.index("--out") + 1] if "--out" in a else f"spec-{slug}.json"
    blocks, missing, featured = convert(slug, media)
    spec = {"post_id": pid, "label": f"Blog upload: {slug}", "agent_label": "Claude Code",
            "agent_note": "Native Gutenberg blocks converted from the local markdown draft (onylogy-blog-system md2blocks.py).", "block_spec": blocks}
    json.dump(spec, open(out, "w"), ensure_ascii=False)
    imgs = sum(1 for b in blocks if b["name"] == "core/image"); heads = sum(1 for b in blocks if b["name"] == "core/heading")
    print(f"{slug}: post {pid}, {len(blocks)} blocks ({heads} headings, {imgs} images) -> {out}")
    if featured: print(f"  featured image (set in the editor UI): {featured[0]}.webp  alt: {featured[1]}")
    if missing: print(f"  MISSING image placements (heading not found): {missing}"); sys.exit(1)
    if UNMAPPED: print(f"  UNMAPPED internal links (add to permalinks.json or fix the draft): {sorted(set(UNMAPPED))}"); sys.exit(1)

if __name__ == "__main__":
    main()
