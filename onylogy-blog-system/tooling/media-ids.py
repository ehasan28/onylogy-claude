#!/usr/bin/env python3
"""After uploading a post's images through wp-admin/media-new.php, read back their attachment IDs and URLs.

usage: media-ids.py SLUG [--out media-ids.json] [--wait 120]

Looks for every .webp in Blogs/<slug>/ in the public media REST API (newest 100), keyed by filename without
extension, and writes {"<key>": {"id": .., "url": ..}}. Warns about "-1" duplicates (a filename that already
existed on the site: either reuse the older ID on purpose or rename the local file before uploading).
Polls for --wait seconds because the site's page cache can lag a few seconds behind the uploader.
"""
import json, os, sys, time, urllib.request

BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))
SITE = "https://onylogy.com"

def fetch():
    req = urllib.request.Request(f"{SITE}/wp-json/wp/v2/media?per_page=100&_fields=id,source_url,alt_text,media_details.width",
                                 headers={"User-Agent": "onylogy-blog-system/1.0", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)

def main():
    a = sys.argv[1:]; slug = a[0]
    out = a[a.index("--out") + 1] if "--out" in a else f"media-ids-{slug}.json"
    wait = int(a[a.index("--wait") + 1]) if "--wait" in a else 90
    want = sorted(f[:-5] for f in os.listdir(os.path.join(BLOGS, slug)) if f.endswith(".webp"))
    deadline = time.time() + wait; got = {}
    while True:
        have = {}
        for m in fetch():
            fn = m["source_url"].split("/")[-1]
            if fn.endswith(".webp"): have[fn[:-5]] = {"id": m["id"], "url": m["source_url"], "width": m.get("media_details", {}).get("width")}
        got = {w: have[w] for w in want if w in have}
        dup = {w: have[w + "-1"] for w in want if w + "-1" in have}
        if len(got) == len(want) or time.time() > deadline: break
        print(f"  {len(got)}/{len(want)} registered, waiting…"); time.sleep(8)
    json.dump(got, open(out, "w"), indent=1)
    print(f"{slug}: {len(got)}/{len(want)} images found -> {out}")
    for w in want:
        if w not in got: print("  MISSING:", w + ".webp")
    for w, m in dup.items(): print(f"  DUPLICATE: {w}-1.webp exists (id {m['id']}); the site already had {w}.webp")
    sys.exit(0 if len(got) == len(want) else 1)

if __name__ == "__main__":
    main()
