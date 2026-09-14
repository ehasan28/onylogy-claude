# onylogy.com — facts the pipeline depends on

Verified 2026-09-14 against the public REST API and the 2026-09-12 upload sessions. Re-verify anything marked
(check) before relying on it; update this file when the site changes.

## WordPress

- Site: https://onylogy.com · WordPress 7.1 · theme "Onylogy - Kadence Child Theme" 1.5.2 · Kadence Blocks 3.7.10 ·
  Kadence Blocks Pro 2.8.18 · Rank Math SEO · LiteSpeed Cache (page cache is ON: cached REST/poll URLs go stale) ·
  Novamira bridge plugin 1.12.3.
- Author: **Ehasanul Haque**, user ID **2**, slug `ehasanul`. Every post is authored by ID 2.
- Permalinks: **`/<primary-category-slug>/<post-slug>/`**. Root-relative `/slug/` links 404. Always write the prefix.
- Posts are **native Gutenberg core blocks** (paragraph, heading, list, image, table, code). No Kadence wrappers
  in posts (Kadence Blocks are for pages only, per `onylogy-kadence-build-convention`).
- Comments closed on new posts (`comment_status closed`), pings open.
- Publish cadence: **Sundays 09:00 site time**, one post per week; drafts are created with that date pinned so the
  editor button reads "Schedule".

## Categories (ID · slug · use)

| ID | Name | Slug | Use |
|---|---|---|---|
| 1 | WordPress | `wordpress` | beginner guides, explainers, comparisons; also added as a second category on most posts |
| 17 | WP Plugins | `wp-plugins` | plugin roundups, plugin deep dives, all Cluster 5 Kadence Blocks posts |
| 18 | WP Themes | `wp-themes` | theme roundups, KadenceWP theme post |
| 15 | Hosting | `hosting` | hosting roundups |
| 16 | Domain | `domain` | domain guides and registrar roundups |
| 19 | Ecommerce | `ecommerce` | WooCommerce posts (none yet) |

Primary category decides the permalink; set it with Rank Math's **Select Primary Term** dropdown in the editor.

## Tags (ID · slug)

28 wordpress · 31 website-guide · 39 beginners · 40 beginer-guide (sic) · 29 kadencewp · 30 kadenceblocks · 36 install-wordpress ·
37 download-wordpress · 38 wordpress-dashboard · 41 security · 42 backup · 43 caching · 44 image-optimization · 45 seo ·
46 domain · 47 page-builders · 48 contact-forms · 49 speed. Reuse these; add a new tag only for a new topic family.

## Media

- Uploads land in `/wp-content/uploads/YYYY/MM/`. Filenames are kept as uploaded (keyword filenames matter).
- Uploading a filename that already exists gets `-1` appended: check `permalinks.py --media` before uploading.
- Reusable existing media: Kadence Blocks WP.org listing = ID 1965, Elementor WP.org listing = ID 1964 (2026/09).

## Rank Math (in the editor)

- Focus keyword field: click it **by screen coordinate** (ref clicks don't register), type, press Enter.
- **Never touch the Title field** in the snippet editor. Set **Description only** (130 to 145 chars).
- Pillar posts: tick "This post is Pillar Content".
- FAQ schema: Rank Math's FAQ block is not used; the H3 + paragraph FAQ is fine (Article schema is automatic).
  (check) whether Rank Math is set to add FAQPage from the JSON-LD comment; currently the JSON-LD in the .md is
  reference only and is not uploaded.

## Novamira CLI

- Installed at `~/.npm-global/bin/novamira` (add `export PATH="$HOME/.npm-global/bin:$PATH"`), version 1.2.0,
  profile **`onylogy.com`**. Abilities used: `novamira/execute-php` (needs the user's approval every time),
  `novamira/gutenberg-add-pending-change`, `novamira/gutenberg-enable-batch-finalization`,
  `novamira/gutenberg-list-pending-batches`, `novamira/gutenberg-get-content`, `rank-math/get-post-seo-meta`,
  `novamira/create-admin-access-link` (one-time admin login, needs approval).
- The Gutenberg batch finalizer runs in the **user's open browser tab** at
  `https://onylogy.com/wp-admin/admin.php?page=novamira-gutenberg-finalize`. Keep it open in the Chrome tab while
  batches finalize. Poll with `gutenberg-list-pending-batches`, **not** the returned `poll_url` (LiteSpeed caches it).

## Browser tooling

- **Chrome (Claude in Chrome extension)** is used for everything the user wants done through the real UI: media
  uploads (`wp-admin/media-new.php`, multi-file input; the `?browser-uploader` form is single-file), featured image,
  primary term, Rank Math fields, Save draft / Schedule. Novamira Visual cannot open editor frames.
- Screenshot browsers: headless shell `~/Library/Caches/ms-playwright/chromium_headless_shell-1223/…` (shot.py) and
  headed "Google Chrome for Testing" `~/Library/Caches/ms-playwright/chromium-1223/…` (pwshot.js, secshot.js,
  adminshots). `playwright-core` 1.61 is installed by `tooling/setup.sh`.

## Design tokens (for thumbnails and any UI in screenshots)

Palette: `#004BD1` brand blue (palette1) · `#146EF5` bright blue (palette2, thumbnail blue) · `#131513` near-black
(palette3, thumbnail black) · `#505050` body text · `#F3F3F3` light bg · `#FFFFFF`. Accents: green `#4CAF50`, cyan
`#03A9F4`, orange `#FF9800`, red `#EF5350`. Fonts: Bricolage Grotesque 700 (headings), Montserrat (body).

## Existing content (live on 2026-09-14)

26 published posts; 15 Cluster 5 Kadence drafts (IDs 2082 to 2096, dated Sundays 2026-12-06 → 2027-03-14) still
unpublished and **queued for a voice v2 rewrite**. Full map in `content-map.md`; slug → permalink map in
`tooling/permalinks.json` (regenerate with `tooling/permalinks.py`).
