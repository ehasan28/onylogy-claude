#!/usr/bin/env bash
# Repair-mode upload: replace the body of an EXISTING onylogy.com post with the rewritten local draft.
# usage: repair-upload.sh SLUG POST_ID [--narrow]
# Steps: audit gate -> media map from the live post -> md2blocks -> add-pending-change (replace-content)
#        -> enable finalization -> poll until finalized -> verify-post. Requires the finalize page open in Chrome.
set -euo pipefail
export PATH="$HOME/.npm-global/bin:$PATH"
HERE="$(cd "$(dirname "$0")" && pwd)"; SLUG="$1"; PID="$2"; NARROW="${3:-}"
W="${REPAIR_DIR:-/tmp/onylogy-repair}"; mkdir -p "$W"; cd "$W"
echo "== gate"; python3 "$HERE/audit-draft.py" "$SLUG" $NARROW | grep -E "GATE|RESULT"
echo "== media map from live post $PID"; python3 "$HERE/live-media-ids.py" "$PID" --out "media-$PID.json" | head -1
echo "== blocks"; python3 "$HERE/md2blocks.py" "$SLUG" --post-id "$PID" --media "media-$PID.json" --out "spec-$PID.json" | head -1
echo "== queue (keep the finalize tab fresh: reload it before a retry)"; novamira --site onylogy.com run novamira/gutenberg-add-pending-change --input "@spec-$PID.json" --json --yes > "add-$PID.json"
BID=$(python3 -c "import json; d=json.load(open('add-$PID.json')); print(d['data']['batch_id'] if d.get('ok') else 'ERR '+json.dumps(d)[:300])")
case "$BID" in ERR*) echo "$BID"; exit 1;; esac
echo "{\"batch_id\":$BID}" > "en-$PID.json"
novamira --site onylogy.com run novamira/gutenberg-enable-batch-finalization --input "@en-$PID.json" --json --yes > "enable-$PID.json"
echo "   batch $BID: $(python3 -c "import json; d=json.load(open('enable-$PID.json'))['data']; print(d.get('batch_status'), '| finalizer online:', d.get('finalizer_runtime',{}).get('online'))")"
echo '{}' > empty.json
for i in $(seq 1 60); do
  novamira --site onylogy.com run novamira/gutenberg-list-pending-batches --input @empty.json --json > lb.json
  ST=$(python3 -c "import json; d=json.load(open('lb.json'))['data']; bs=d.get('batches',d if isinstance(d,list) else []); b=[x for x in bs if x.get('batch_id')==$BID or x.get('id')==$BID]; print(b[0].get('status') if b else 'missing')")
  case "$ST" in finalized|failed|conflicted|missing) break;; esac
  sleep 8
done
echo "   batch $BID: $ST"
if [ "$ST" != "finalized" ]; then python3 -c "import json; d=json.load(open('lb.json'))['data']; bs=d.get('batches',d if isinstance(d,list) else []); b=[x for x in bs if x.get('batch_id')==$BID]; print(json.dumps(b[0],indent=1)[:1500] if b else '')"; exit 1; fi
echo "== verify"; python3 "$HERE/verify-post.py" "$SLUG" --post-id "$PID"
