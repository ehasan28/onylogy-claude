#!/usr/bin/env bash
# The system's reference files are canonical; the workspace keeps copies where other tools expect them
# (onywrites auto-discovers blog-voice.md in the workspace; blog-list.txt points at the planning files).
# This script reports drift. Run it at the start of every blog task.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; SYS="$HERE/.."; WS="${ONYLOGY_WORKSPACE:-$HOME/Claude Playground/Onylogy Studio Website/Blog Posts}"
ok=0
pair() { # system-file workspace-file
  if [ ! -f "$2" ]; then echo "MISSING in workspace: $2  (copy from $1)"; ok=1
  elif ! diff -q "$1" "$2" >/dev/null; then echo "DRIFT: $2 differs from $1  (system copy is canonical: cp \"$1\" \"$2\")"; ok=1
  else echo "in sync: $(basename "$2")"; fi
}
pair "$SYS/references/blog-voice.md"          "$WS/blog-voice.md"
pair "$SYS/references/thumbnail-guide.md"     "$WS/blog-featured-image-guide.md"
pair "$SYS/references/seo-geo-checklist.md"   "$WS/seo-geo-checklist.md"
for t in shot.py pwshot.js secshot.js; do pair "$HERE/$t" "$WS/tools/$t"; done
echo "permalinks.json: $(python3 -c "import json;d=json.load(open('$HERE/permalinks.json'));print(len(d),'slugs')") (refresh: python3 $HERE/permalinks.py)"
exit $ok
