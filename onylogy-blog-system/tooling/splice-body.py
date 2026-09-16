#!/usr/bin/env python3
"""Repair helper: replace the BODY of Blogs/<slug>/<slug>.md (from the H1 to the closing JSON-LD/IMAGES comment)
with a rewritten body file, keep POST META / JSON-LD / IMAGES, set Type:, add a REWRITE NOTE, and add missing
image placement tags in the IMAGES block ("featured" -> [top], "N. Name" -> [after "## N. Name"]).

usage: splice-body.py SLUG NEW_BODY.md --type roundup|guide|... --note "what changed"
"""
import os, re, sys
BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))

def main():
    a = sys.argv[1:]; slug = a[0]; new_body = open(a[1], encoding="utf-8").read().strip() + "\n"
    ptype = a[a.index("--type") + 1] if "--type" in a else None
    note = a[a.index("--note") + 1] if "--note" in a else ""
    path = os.path.join(BLOGS, slug, f"{slug}.md"); md = open(path, encoding="utf-8").read()
    head, rest = md.split("\n# ", 1)
    tail_i = rest.rfind("\n<!--")
    tail = rest[tail_i:] if tail_i >= 0 else ""
    # META edits
    if ptype and not re.search(r"^Type:", head, re.M):
        head = re.sub(r"^(Slug:.*\n)", r"\1Type:              " + ptype + "\n", head, count=1, flags=re.M)
    if note and "REWRITE NOTE" not in head:
        head = head.replace("====================================================================\n-->", f"\nREWRITE NOTE ({note})\n====================================================================\n-->")
    # IMAGES placements
    def fix(line):
        m = re.match(r'^(\S[^→]*?)\s*→\s*(\S+)\s+alt:\s*"([^"]+)"\s*$', line)
        if not m: return line
        label = m.group(1).strip()
        if label.lower().startswith("featured"): return line + "   [top]"
        if re.match(r"^\d+\. ", label): return line + f'   [after "## {label}"]'
        return line + "   [PLACEMENT NEEDED]"
    tail = "\n".join(fix(l) for l in tail.split("\n"))
    out = head + "\n" + new_body + "\n---\n" + tail
    open(path, "w", encoding="utf-8").write(out)
    need = tail.count("[PLACEMENT NEEDED]")
    print(f"{slug}: body replaced ({len(new_body.split())} words); IMAGES placements needing a hand edit: {need}")

if __name__ == "__main__":
    main()
