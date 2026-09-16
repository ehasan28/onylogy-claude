#!/usr/bin/env python3
"""Build a media-ids.json for md2blocks.py from a post that is ALREADY on the site (repair mode).

usage: live-media-ids.py POST_ID [--out media-ids.json]

Reads the post's rendered content from the public REST API (published posts) or, if not public, from
`novamira gutenberg-get-content`, and maps every <img class="wp-image-ID" src="…/name.webp"> to
{"name": {"id": ID, "url": src}}. Use it when re-uploading a rewritten body so the same attachments are reused.
"""
import json, os, re, subprocess, sys, urllib.request

def public(pid):
    req = urllib.request.Request(f"https://onylogy.com/wp-json/wp/v2/posts/{pid}?_fields=id,slug,content&n={os.getpid()}", headers={"User-Agent": "onylogy-blog-system/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)["content"]["rendered"]
    except Exception: return None

def novamira_ids(pid):
    """Drafts are not public: read the block tree (image IDs only) and resolve each ID through the public media API."""
    env = {**os.environ, "PATH": os.path.expanduser("~/.npm-global/bin") + ":" + os.environ["PATH"]}
    p = subprocess.run(["novamira", "--site", "onylogy.com", "run", "novamira/gutenberg-get-content", "--input", json.dumps({"post_id": pid}), "--json"], capture_output=True, text=True, env=env)
    d = json.loads(p.stdout); d = d.get("data", d)
    ids = [b.get("attributes", {}).get("id") for b in d.get("blocks", []) if b.get("name") == "core/image"]
    found = {}
    for i in ids:
        if not i: continue
        req = urllib.request.Request(f"https://onylogy.com/wp-json/wp/v2/media/{i}?_fields=id,source_url", headers={"User-Agent": "onylogy-blog-system/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r: m = json.load(r)
            url = m["source_url"]; key = url.split("/")[-1].rsplit(".", 1)[0]
            found[key] = {"id": int(i), "url": url}
        except Exception as e: print("  could not resolve media", i, e, file=sys.stderr)
    return found

def main():
    pid = int(sys.argv[1]); out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"media-ids-{pid}.json"
    c = public(pid)
    found = {} if c else novamira_ids(pid)
    for m in re.finditer(r"<img\b[^>]*>", c or ""):
        tag = m.group(0)
        i = re.search(r"wp-image-(\d+)", tag); s = re.search(r'src="([^"]+)"', tag)
        if i and s:
            url = s.group(1); key = re.sub(r"-\d+x\d+(?=\.\w+$)", "", url.split("/")[-1]); key = key.rsplit(".", 1)[0]
            found[key] = {"id": int(i.group(1)), "url": re.sub(r"-\d+x\d+(?=\.\w+$)", "", url)}
    json.dump(found, open(out, "w"), indent=1)
    print(f"post {pid}: {len(found)} images -> {out}"); [print("  ", k, v["id"]) for k, v in found.items()]

if __name__ == "__main__":
    main()
