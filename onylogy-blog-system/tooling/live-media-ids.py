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

def novamira(pid):
    env = {**os.environ, "PATH": os.path.expanduser("~/.npm-global/bin") + ":" + os.environ["PATH"]}
    p = subprocess.run(["novamira", "--site", "onylogy.com", "run", "novamira/gutenberg-get-content", "--input", json.dumps({"post_id": pid}), "--json"], capture_output=True, text=True, env=env)
    d = json.loads(p.stdout); d = d.get("data", d)
    return d.get("content") or d.get("post_content") or d.get("rendered") or ""

def main():
    pid = int(sys.argv[1]); out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"media-ids-{pid}.json"
    c = public(pid) or novamira(pid)
    found = {}
    for m in re.finditer(r"<img\b[^>]*>", c):
        tag = m.group(0)
        i = re.search(r"wp-image-(\d+)", tag); s = re.search(r'src="([^"]+)"', tag)
        if i and s:
            url = s.group(1); key = re.sub(r"-\d+x\d+(?=\.\w+$)", "", url.split("/")[-1]); key = key.rsplit(".", 1)[0]
            found[key] = {"id": int(i.group(1)), "url": re.sub(r"-\d+x\d+(?=\.\w+$)", "", url)}
    json.dump(found, open(out, "w"), indent=1)
    print(f"post {pid}: {len(found)} images -> {out}"); [print("  ", k, v["id"]) for k, v in found.items()]

if __name__ == "__main__":
    main()
