#!/usr/bin/env python3
"""Maintain tooling/permalinks.json: slug -> permalink path for every onylogy.com post, plus local drafts.

usage: permalinks.py            refresh from the public REST API (published posts) and local drafts, then write the file
       permalinks.py --media    list recent media (id, filename) to check for filename collisions before uploading
       permalinks.py --check SLUG ...   print the permalink for each slug (exit 1 if any is unknown)

Published posts come from /wp-json/wp/v2/posts (public, read-only). Unpublished local drafts are added from
Blogs/<slug>/<slug>.md using the POST META "Category:" line (primary category = first one listed), because a draft's
permalink is /<primary-category-slug>/<slug>/ once published.
"""
import json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "permalinks.json")
SITE = "https://onylogy.com"
BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))
CAT_SLUG = {"wordpress": "wordpress", "wp plugins": "wp-plugins", "wp themes": "wp-themes", "hosting": "hosting",
            "domain": "domain", "ecommerce": "ecommerce"}

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "onylogy-blog-system/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def refresh():
    links = {}
    page = 1
    while True:
        posts = get(f"{SITE}/wp-json/wp/v2/posts?per_page=100&page={page}&_fields=id,slug,link,date")
        if not posts: break
        for p in posts:
            links[p["slug"]] = {"path": p["link"].replace(SITE, ""), "id": p["id"], "status": "publish", "date": p["date"][:10]}
        if len(posts) < 100: break
        page += 1
    # published pages (contact, about, ...) so bare /slug/ page links resolve too
    for pg in get(f"{SITE}/wp-json/wp/v2/pages?per_page=100&_fields=id,slug,link,status"):
        links.setdefault(pg["slug"], {"path": pg["link"].replace(SITE, ""), "id": pg["id"], "status": "page", "date": None})
    # local drafts not yet public
    if os.path.isdir(BLOGS):
        for slug in sorted(os.listdir(BLOGS)):
            md = os.path.join(BLOGS, slug, f"{slug}.md")
            if slug in links or not os.path.isfile(md): continue
            head = open(md, encoding="utf-8").read(4000)
            m = re.search(r"^Category:\s*(.+)$", head, re.M)
            if not m: continue
            primary = re.split(r"[,(]", m.group(1))[0].strip().lower()
            cat = CAT_SLUG.get(primary)
            if cat:
                links[slug] = {"path": f"/{cat}/{slug}/", "id": None, "status": "local-draft", "date": None}
    json.dump(links, open(OUT, "w"), indent=1, sort_keys=True)
    pub = sum(1 for v in links.values() if v["status"] == "publish")
    print(f"permalinks.json: {pub} published, {len(links)-pub} local drafts")

def media():
    ms = get(f"{SITE}/wp-json/wp/v2/media?per_page=100&_fields=id,source_url,date")
    for m in sorted(ms, key=lambda m: m["id"]):
        print(m["id"], m["date"][:10], m["source_url"].split("/uploads/")[-1])

if __name__ == "__main__":
    if "--media" in sys.argv: media()
    elif "--check" in sys.argv:
        links = json.load(open(OUT)); bad = 0
        for s in sys.argv[sys.argv.index("--check")+1:]:
            if s in links: print(s, "->", links[s]["path"], f"({links[s]['status']})")
            else: print(s, "-> UNKNOWN"); bad = 1
        sys.exit(bad)
    else: refresh()
