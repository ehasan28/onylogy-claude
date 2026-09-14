#!/usr/bin/env bash
# One-time setup for the Onylogy blog tooling. Safe to re-run.
set -euo pipefail
cd "$(dirname "$0")"

echo "== Python venv with Pillow (thumbnails, screenshot crops)"
[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install -q --upgrade pip pillow
.venv/bin/python -c "import PIL; print('   Pillow', PIL.__version__)"

echo "== playwright-core (headed Chrome for Testing screenshots: pwshot.js, secshot.js, adminshots)"
[ -f package.json ] || echo '{"name":"onylogy-blog-tooling","private":true}' > package.json
npm install --silent --no-audit --no-fund playwright-core@1.61.1
node -e "console.log('   playwright-core', require('playwright-core/package.json').version)"

echo "== Browsers (installed by Playwright; used by shot.py and the .js tools)"
if [ ! -d "$HOME/Library/Caches/ms-playwright/chromium-1223" ] || [ ! -d "$HOME/Library/Caches/ms-playwright/chromium_headless_shell-1223" ]; then
  echo "   installing chromium 1223 via playwright-core..."; npx playwright-core install chromium
fi
ls -d "$HOME/Library/Caches/ms-playwright/chromium"* | sed 's/^/   /'

echo "== rsvg-convert (SVG -> PNG for thumbnails)"
command -v rsvg-convert >/dev/null || { echo "   missing: brew install librsvg"; exit 1; }
echo "   $(rsvg-convert --version)"

echo "== Novamira CLI (site profile onylogy.com)"
export PATH="$HOME/.npm-global/bin:$PATH"
command -v novamira >/dev/null && novamira sites list --json | python3 -c "import json,sys; print('   profiles:', [s['name'] for s in json.load(sys.stdin)['data']])" || echo "   missing: npm install -g @novamira/cli, then novamira auth login https://onylogy.com --name onylogy.com"

echo "== permalinks.json"
python3 permalinks.py
echo "done."
