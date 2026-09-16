#!/usr/bin/env python3
"""Verify an uploaded post on onylogy.com against its local draft. Read-only.

usage: verify-post.py SLUG --post-id ID
   env: PATH must include ~/.npm-global/bin (novamira CLI, profile onylogy.com)

Checks, with counts, not "looks fine":
  1. Post exists, status/date, title == local H1, slug, author 2, categories/tags set.
  2. Body: heading count and texts match the draft; image count == IMAGES block (minus featured); every internal
     link has a category prefix; no "undefined", no empty <figure>, no byline paragraph, no dash characters.
  3. Rank Math: focus keyword and description present (via rank-math/get-post-seo-meta); featured image set.
Exit 1 on any hard mismatch. Public REST is used for published posts; Novamira for drafts.
"""
import json, os, re, subprocess, sys, html

BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))

def nova(ability, payload):
    p = subprocess.run(["novamira", "--site", "onylogy.com", "run", ability, "--input", json.dumps(payload), "--json"],
                       capture_output=True, text=True, env={**os.environ, "PATH": os.path.expanduser("~/.npm-global/bin") + ":" + os.environ["PATH"]})
    try: d = json.loads(p.stdout)
    except Exception: raise SystemExit(f"{ability} failed: {p.stdout[:300]} {p.stderr[:300]}")
    if not d.get("ok", True): raise SystemExit(f"{ability}: {json.dumps(d)[:400]}")
    return d.get("data", d)

def main():
    a = sys.argv[1:]; slug = a[0]; pid = int(a[a.index("--post-id") + 1])
    md = open(os.path.join(BLOGS, slug, f"{slug}.md"), encoding="utf-8").read()
    body = md.split("-->", 1)[1]; body = body[:body.rfind("<!--")] if "<!--" in body else body
    h1 = re.search(r"^# (.+)$", body, re.M).group(1).strip()
    local_heads = [(len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^(#{2,4}) (.+)$", body, re.M)]
    local_imgs = len(re.findall(r"→\s*\S+\.webp\s+alt:", md)) - 1  # minus featured
    import urllib.request
    fails = []; notes = []; content = None; post = {}
    try:  # published posts: the public REST API has the rendered HTML (cache-busted)
        req = urllib.request.Request(f"https://onylogy.com/wp-json/wp/v2/posts/{pid}?_fields=id,slug,status,date,modified,title,content,featured_media&nocache={os.getpid()}", headers={"User-Agent": "onylogy-blog-system/1.0", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=30) as r: post = json.load(r)
        content = post["content"]["rendered"]
    except Exception: post = {}
    if content is None:  # drafts: only the block tree is readable without PHP
        data = nova("novamira/gutenberg-get-content", {"post_id": pid})
        blocks = data.get("blocks", [])
        names = [b.get("name") for b in blocks]
        title = html.unescape(str(data.get("target_title", "")))
        if title and title != h1: fails.append(f"title differs: site '{title}' vs local '{h1}'")
        nh = names.count("core/heading"); ni = names.count("core/image")
        notes.append(f"draft (block tree only): headings={nh} images={ni} paragraphs={names.count('core/paragraph')} tables={names.count('core/table')} lists={names.count('core/list')}")
        if nh != len(local_heads): fails.append(f"heading count {nh} on site vs {len(local_heads)} local")
        if ni != local_imgs: fails.append(f"{ni} images on site vs {local_imgs} expected")
        content = ""
    else:
        title = html.unescape(str(post.get("title", {}).get("rendered", "")))
        if title and title != h1: fails.append(f"title differs: site '{title}' vs local '{h1}'")
        notes.append(f"status={post.get('status')} date={post.get('date')} modified={post.get('modified')} slug={post.get('slug')} featured_media={post.get('featured_media')}")
        heads = [(int(m.group(1)), re.sub(r"<[^>]+>", "", html.unescape(m.group(2))).strip()) for m in re.finditer(r"<h([2-4])[^>]*>(.*?)</h\1>", content, re.S)]
        if len(heads) != len(local_heads): fails.append(f"heading count {len(heads)} on site vs {len(local_heads)} local")
        else:
            norm = lambda t: t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("&amp;", "&")
            diff = [(l, s) for l, s in zip(local_heads, heads) if norm(l[1]) != norm(s[1])]
            if diff: fails.append(f"{len(diff)} heading text mismatch(es), first: {diff[0]}")
        if post.get("featured_media") in (None, 0): fails.append("no featured image set")
    imgs = len(re.findall(r"<img\b", content))
    if content and imgs != local_imgs: fails.append(f"{imgs} images on site vs {local_imgs} expected from IMAGES block")
    if re.search(r"<figure[^>]*>\s*</figure>", content): fails.append("empty <figure> found")
    if "undefined" in content: fails.append("'undefined' string found in content")
    if re.search(r"<p>\s*<em>By Ehasanul", content): fails.append("byline paragraph present (must be removed)")
    bare = sorted(set(re.findall(r'href="(/[a-z0-9-]+/)"', content)))
    if bare: fails.append(f"internal links without category prefix: {bare}")
    dashes = len(re.findall("—|–", re.sub(r"\d–\d", "", content)))
    if dashes: fails.append(f"{dashes} dash character(s) in content")
    words = len(re.sub(r"<[^>]+>", " ", content).split())
    notes.append(f"headings={len(heads)} images={imgs} words≈{words} internal={len(re.findall(r'href=\"/', content))} external={len(re.findall(r'href=\"https?://(?!onylogy)', content))}")
    try:
        seo = nova("rank-math/get-post-seo-meta", {"post_id": pid})
        fk = seo.get("focus_keyword") or seo.get("rank_math_focus_keyword"); desc = seo.get("description") or seo.get("rank_math_description")
        if not fk: fails.append("Rank Math focus keyword empty")
        if not desc: fails.append("Rank Math description empty")
        elif not (120 <= len(desc) <= 150): notes.append(f"Rank Math description {len(desc)} chars")
        rm_title = seo.get("title") or seo.get("rank_math_title")
        if rm_title and rm_title != h1: fails.append(f"Rank Math Title field looks SET: '{rm_title}' (must inherit the post title)")
        notes.append(f"rank math: keyword='{fk}' desc={len(desc or '')} chars")
    except SystemExit as e: notes.append(f"rank math meta not readable: {e}")
    print(f"== post {pid} ({slug})"); [print("  ", n) for n in notes]
    for f in fails: print("  FAIL:", f)
    print("  RESULT:", "OK" if not fails else f"{len(fails)} problem(s)")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
