# Featured image (thumbnail) spec — v4 (current standard)

> v4 is the result of a real three-column archive-grid test (`thumbnail-history.md`): at card size only a big
> headline and one large literal icon survive; everything small becomes noise. Every post since August 2026 uses
> v4. `tooling/thumb.py` generates it; do not hand-draw a thumbnail from scratch when the tool can.
> v1 (gradient + glass cards + no text) is archived in `thumbnail-guide-v1-archive.md` and is **not** used.

## Canvas

- **1200 × 630** SVG, exported to `.webp` (quality 85, typically 15 to 25 KB). Both files live in `Blogs/<slug>/`
  as `<slug>-thumbnail.svg` and `<slug>-thumbnail.webp`; the SVG is also copied to `thumbnails/<slug>-thumbnail-v4.svg`.
- Filename = slug (keyword filename). Alt text = the post's featured-image alt from POST META.

## Exactly four elements, nothing else

1. **Flat background**, one solid color, no gradient:
   - **Blue `#146EF5`** (default: guides, explainers, comparisons, most roundups, Kadence posts).
   - **Black `#131513`** for "under the hood" topics: security, speed/caching, backups, hosting, image
     optimization, layout-heavy Kadence blocks (Row Layout, Accordion, homepage build), mistakes posts.
   Plus one large soft circle behind the icon (`r=300` at 880,390, white at 7% on blue / 5% on black).
2. **Two lines of text, left-aligned at x=90**, Bricolage Grotesque 700 (fallback Poppins/Arial), white:
   - Line 1, the topic, **48 to 60px** at y=250: "LiteSpeed Cache", "Info Box", "Image Optimization".
     Keep it to what fits the left half (≈ 18 characters at 60px, 24 at 48px). Three-line titles allowed for
     "X vs Y" (50/50/36px at y=235/290/340).
   - Line 2, the qualifier, **36 to 40px** at y=305: "Beginner Guide", "Top 6 Compared", "Block Explained",
     "Free vs Pro". White on blue; on black, or for roundups, orange `#FF9800` is allowed on line 2 for pop.
   Title Case. No other text anywhere (no badges, pills, captions, status labels).
3. **WordPress mark, small, bottom-left:** outline circle r=34 at (112,540), stroke white 3px, 85% opacity, a
   serif bold "W" 34px centred inside.
4. **One large literal hero icon** on the right (≈ x 700 to 1080, y 170 to 560): white strokes 10 to 16px or white
   fills, radius 14 to 28, optionally one accent shape in cyan `#03A9F4` or orange `#FF9800` (a badge, a button, a
   highlighted card). It must read as the object at 370px card width: a padlock that looks like a padlock, a
   gauge, a stack of blocks, a picture frame, a form with a Send button, a VS badge between two cards.

## Icon library (in `tooling/thumb.py --list-icons`)

`stack` (three offset cards: guides/hubs) · `vs` (two cards + VS badge) · `three` (three stacked cards: 3-way
comparison) · `palette` (four swatches + Aa) · `H` (framed letter + level badge: headings/text) · `grid` (row
layout) · `infobox` · `quote` (testimonials) · `accordion` · `gallery` (2×3 tiles) · `form` (fields + Send) ·
`page` (homepage wireframe) · `warn` (triangle: mistakes) · `gauge` (speed) · `shield` (security) · `frame`
(image optimization) · `cloud` (backup) · `globe` (domain) · `server` (hosting) · `search` (SEO) · `plug`
(plugins) · `brush` (themes) · `download` (install) · `dashboard` · `pen` (first post) · `mail` (contact forms) ·
`cart` (ecommerce). Add a new icon to the library rather than inlining one; keep it to ≤ 6 primitives.

## Choosing per post type

| Post type | Background | Line 2 | Icon |
|---|---|---|---|
| Roundup "Top 6 X" | blue (black if security/speed/backup/hosting/images) | "Top 6 Compared" (orange) | the category object |
| How-to guide | blue | "Beginner Guide" / "Step by Step" | the action object |
| Comparison | blue | "Compare and Choose" / "Which to Pick" | `vs` or `three` |
| Kadence block deep dive | blue (black for layout blocks) | "Block Explained" | the block's shape |
| Deep dive / setup | black if technical | "Beginner Guide" / "Advanced Guide" | the tool's object |
| Mistakes | black | "Common Mistakes" | `warn` |

## Checklist before upload

- [ ] 1200×630, flat blue or black, exactly two text lines, WP corner mark, one big icon. Nothing else.
- [ ] Both lines readable when the SVG is viewed at 370px wide (open the webp at 30% zoom and look).
- [ ] Title Case, no dash, line 1 ≤ ~24 characters.
- [ ] Files named `<slug>-thumbnail.svg/.webp`, webp under 60 KB, alt text set in POST META.
- [ ] Matches the other thumbnails in the archive grid (blue/black alternation looks intentional).
