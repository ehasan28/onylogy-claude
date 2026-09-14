# Content map: where a new title belongs

The living planning files stay in the workspace, not here:

- `Onylogy Studio Website/Blog Posts/blog-list.txt` — the running title list with status and WP IDs. **Update it
  for every post** (add the line when drafting, change the status when uploaded/scheduled/published).
- `Onylogy Studio Website/Blog Posts/blog-idea.md` — strategy: Parts A to F (first wave, pillar/cluster map,
  Cluster 4, Cluster 2 expansion, brand positioning, Cluster 5 Kadence). Read it when a title doesn't obviously
  fit an existing cluster.
- `Onylogy Studio Website/Blog Posts/Blogs/<slug>/` — one folder per post: `<slug>.md`, `research.md`,
  `<slug>-thumbnail.svg` + `.webp`, screenshots as 1200px `.webp`. Nothing loose in `Blog Posts/` except the
  planning files, `thumbnails/`, `tools/`.

## The architecture

```
PILLAR  What Is WordPress and Why Should You Use It?           /wordpress/what-is-wordpress/
  C1 Getting started: .com vs .org · install · dashboard · first post & page
  C2 Choosing your tools (BEST PERFORMER, roundup format): hosting · themes · plugins · KadenceWP ·
     security plugins · backup plugins · caching plugins · image optimization · SEO plugins ·
     domain registration sites · page builders · contact forms
  C3 Best practices: common mistakes · security checklist
  C4 Growing beyond the basics: speed (CWV) · backups · choose a domain name · WordPress SEO · Elementor vs Gutenberg
  C5 Kadence Blocks deep dives (specialist, hub /wp-plugins/kadence-blocks-guide/): settings · free vs pro ·
     palette & typography · 7 block posts · homepage build · vs Elementor · vs Spectra/Stackable · mistakes
     (+2 gated on a real benchmark: vs GenerateBlocks, SEO/speed)
  C6 (future) WordPress SEO cluster spun out of the C4 SEO post
BACKLOG WooCommerce for beginners · migrate a site · white screen of death · free vs paid themes
```

## Rules for placing a title

1. **Pair guide with roundup.** A concept guide ("How to back up…") pairs with a roundup ("Top 6 backup
   plugins"); each links to the other. If the pair doesn't exist yet, leave a placeholder link in POST META, not a
   broken link in the body.
2. **Roundups win.** When two titles compete for the next slot, the "Top 6" goes first (site's best format).
3. **Every post links up** to its pillar (or the C5 hub) and to at least one sibling; the pillar/hub gets a
   link down to the new post in its next refresh (note it in blog-list.txt as a to-do).
4. **Category decides the permalink** (`site-facts.md`), so decide the primary category before writing links.
5. **Sunday cadence.** Next free Sunday = last pinned date in blog-list.txt + 7 days. Confirm with the user before
   pinning; the site currently has drafts pinned through 2027-03-14 (Cluster 5), so a new post is normally slotted
   *before* those and the Cluster 5 dates shift, or after them, at the user's call.
6. **Two audiences, don't merge them.** Beginner posts (C1 to C4) and Kadence specialist posts (C5) cross-link only
   where genuinely relevant; "Elementor vs Gutenberg" (C4) and "Kadence Blocks vs Elementor" (C5) are distinct posts.
7. **Benchmark-gated titles** (anything with speed numbers) are not written until the test is run.

## blog-list.txt line format

```
[D] N. Title (Qualifier)   WP DRAFT #ID, date YYYY/MM/DD -> Blogs/<slug>/   (n TK: …)
```
Status keys: `[x]` published · `[S]` scheduled · `[D]` draft on WP with the date pinned · `[~]` drafted locally only ·
`[ ]` idea only.
