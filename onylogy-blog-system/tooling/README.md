# Tooling

All scripts assume the workspace at `~/Claude Playground/Onylogy Studio Website/Blog Posts/` (override with
`ONYLOGY_BLOGS=/path/to/Blogs` and `ONYLOGY_WORKSPACE=/path/to/Blog Posts`). Run `./setup.sh` once.

| Script | Phase | What it does |
|---|---|---|
| `setup.sh` | 0 | venv + Pillow, `playwright-core`, browser check, `rsvg-convert` check, Novamira profile check, refresh permalinks |
| `check-sync.sh` | 0 | reports drift between the system's reference files and the workspace copies |
| `permalinks.py` | 0, 3 | `permalinks.json` (slug → `/category/slug/`) from the live site + local drafts; `--check SLUG…`; `--media` lists recent uploads |
| `audit-draft.py SLUG` | 4 | **the gate**: voice numbers (canon) + SEO/GEO lint. Exit 1 = do not upload. `--json` for machine output |
| `thumb.py SLUG "Line 1" "Line 2" --bg blue\|black --icon NAME` | 5 | v4 featured image, SVG + WEBP into `Blogs/<slug>/` (+ copy to `thumbnails/`). `--list-icons`, `--sheet out.png` |
| `shot.py URL out.webp wporg\|hero [h]` | 6 | headless capture; `wporg` pixel-crops a WordPress.org plugin listing edge to edge; `hero` crops the top of a page. 1200px webp |
| `pwshot.js URL out.png [h] [waitMs] [dismissSel]` | 6 | headed Chrome for Testing (off-screen) for sites that block headless capture; then resize with Pillow |
| `secshot.js jobs.json outdir` | 6 | element screenshots of onylogy.com sections (ancestor Row Layout of an H2 text) |
| `adminshots-example.js` | 6 | example: one-time admin login via `novamira/create-admin-access-link` (needs the user's approval) + editor screenshots |
| `media-ids.py SLUG` | 8a | after the Media Library upload, reads back attachment IDs/URLs for every `.webp` in the post folder |
| `make-draft-php.py SLUG --date YYYY-MM-DD` | 8b | builds the one `wp_insert_post` snippet (draft, date pinned). **Ask before running.** |
| `md2blocks.py SLUG --post-id ID --media media-ids.json --out spec.json` | 8c | `.md` → core Gutenberg blocks for `novamira/gutenberg-add-pending-change` |
| `verify-post.py SLUG --post-id ID` | 8e | read-only verification of the uploaded post (headings, images, links, byline, dashes, Rank Math meta) |

## Novamira CLI one-liners (profile `onylogy.com`; `export PATH="$HOME/.npm-global/bin:$PATH"`)

```bash
novamira --site onylogy.com doctor --json                                                    # must be all pass
novamira --site onylogy.com run novamira/execute-php --input @php-in.json --json --yes        # ONLY after the user says yes
novamira --site onylogy.com run novamira/gutenberg-add-pending-change --input @spec.json --json --yes   # returns batch_id
echo '{"batch_id":N}' > en.json; novamira --site onylogy.com run novamira/gutenberg-enable-batch-finalization --input @en.json --json --yes
echo '{}' > empty.json; novamira --site onylogy.com run novamira/gutenberg-list-pending-batches --input @empty.json --json   # poll THIS
novamira --site onylogy.com run novamira/gutenberg-get-content --input '{"post_id":N}' --json
novamira --site onylogy.com run rank-math/get-post-seo-meta --input '{"post_id":N}' --json
```

The finalizer runs inside the user's browser: keep `https://onylogy.com/wp-admin/admin.php?page=novamira-gutenberg-finalize`
open in the Chrome tab until `gutenberg-list-pending-batches` reports `finalized`. Never trust the `poll_url` (cached).

## Troubleshooting

- `doctor` says `oauth.resource_metadata … server_unsupported`, "OAuth resource does not match this WordPress site"
  (seen 2026-09-14: the site advertised `wp-json/mcp/mcp-oauth-server`, the CLI expects `mcp/novamira-oauth`): the
  Novamira plugin on the site was updated or another MCP/OAuth plugin is active. Stop, tell the user, do not
  work around it with other endpoints. Fix is on the site (plugin settings) or `novamira update` + `novamira auth login`.
- Uploaded images show up as `name-1.webp`: the filename already existed. Either reuse the old ID
  (`permalinks.py --media`) or rename locally and re-upload.
- Batch stuck at `running`: the finalize tab isn't open or was reloaded; open it and wait; check with
  `gutenberg-list-pending-batches`, then `gutenberg-delete-pending-batch` and re-add if it is `failed`.
- `shot.py` returns a blank/cookie-wall image: use `pwshot.js` with a dismiss selector; GoDaddy needs
  `?currencyType=USD&marketId=en-US`; Google SERPs can't be captured (reCAPTCHA), flag for manual capture.
- Thumbnail text overflows: shorten line 1 (≤ ~18 characters at 60px) rather than shrinking below 46px.
