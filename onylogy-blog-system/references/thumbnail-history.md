# Hostinger Thumbnail Style Analysis & Merge Report

> **Purpose:** A firsthand audit of Hostinger's actual WordPress-category blog thumbnails (not assumptions from
> memory), compared against Onylogy's current thumbnail system (`featured-image-guide.md` v1), to explain why the
> current Onylogy thumbnails read as unclear/unprofessional and to define a merged v2 system that fixes it.

## Methodology

- Crawled `hostinger.com/blog/wordpress/` pages 1–8 (~50 post listings, some repeated as a pinned/featured post).
- Downloaded and visually inspected **18 representative thumbnail images** spanning every sub-type on the page:
  WordPress version-release announcements, "WordPress Experts" interview profiles, WordCamp/event posts, product
  update posts (WooCommerce), monthly news roundups, and a security-focused post.
- Sampled exact background hex values directly from the PNG pixel data (not estimated).

**Honest finding up front:** this specific category (`/blog/wordpress/`) turned out to be Hostinger's **community/
news/release-notes** section, not their "Top N tools" listicle section — the topics differ from Onylogy's beginner
tutorial content. But the *visual design system* is completely consistent across every sub-type on the page, and
that system is what matters here, regardless of topic. It is also a clearly deliberate, mature brand system —
useful to learn from regardless of topic mismatch.

---

## What Hostinger Actually Does (confirmed, not assumed)

### 1. One flat, solid, saturated brand color — not a gradient
Every single thumbnail sampled uses the **same flat, non-gradient background color**: `#673DE6` / `#673EE6`
(a confident blue-violet). No diagonal blend, no lighter-to-darker transition. One strong flat color, every time.
This is a deliberate brand-recognition choice — flip through their blog and every thumbnail is instantly
identifiable as "a Hostinger post" before you even read the title.

### 2. Big, bold, readable text directly on the image
Nearly every thumbnail carries **large white sans-serif text stating exactly what the post is about** — a person's
name ("Bernard Meyer"), a category label ("WordPress Experts"), a product name and version ("WooCommerce 7.1"), an
event and location ("WordCamp Europe — Kraków 2026"), or real interface copy mocked up inside a UI element ("Enable
overrides", "Add new template", "Roboto"). **This is the single biggest difference from Onylogy's current
thumbnails**, which deliberately avoid all text. Hostinger's approach directly solves "can a visitor tell what this
is about at a glance" — because the words are just... there.

### 3. Real photography and 3D-rendered objects, collaged with flat line art
Most thumbnails mix a **grayscale (B&W) photographic cutout** — a hand pointing, holding a magnifying glass,
painting with a brush, or a real portrait photo for profile posts — into an otherwise flat-illustration scene. The
security-focused post went further: a **real photographic/3D-rendered padlock and key** (not a flat vector icon)
placed directly over the illustration. This photographic layer is what gives the thumbnails a premium, editorial
feel that pure flat-vector icon art can't fully replicate.

### 4. Thin, minimal white line-art UI "chrome"
Scattered through nearly every image: browser-window dots, a close (×) button, a cursor arrow, a code bracket
`</>`, a plus-in-circle, a gear, an exclamation-mark alert badge, an image-placeholder box (rectangle with a
diagonal line). All outlined only (~1.5px stroke), no fill except small brand-accent blocks. This is the one
element Onylogy's current system already does reasonably well.

### 5. The WordPress logo as a thin-outline circle, not a solid white disc
Hostinger's WP mark is a **circular outline** (not a filled white circle) with a flat lavender/periwinkle "W"
inside — sometimes paired with a small circular version-number badge ("6.6", "6.5") snapped to its edge. Onylogy's
current system uses a solid white filled circle instead, which reads as more "generic app icon" than "WordPress
brand mark."

### 6. Layout adapts to content type, but the system stays constant
- **Release/how-to posts:** free-floating line-art UI elements + one photographic collage element (a hand) on the
  flat purple canvas, no enclosing frame.
- **Profile/interview posts:** everything sits inside a **browser-window frame** (rounded rect, dot chrome bar,
  close button) split into a left text panel (headline + name) and a right photo panel (real portrait).
- **Product-update posts:** browser-window frame again, with a literal object callout (shopping cart icons +
  "WooCommerce 7.1" wordmark) inside.
- **Event posts:** either a diagonal color-block banner with full-color event photography, or a browser-frame
  scene with line-art landmark silhouettes (a city's towers) plus the event name in bold text.

---

## Onylogy's Current System (v1) — Side-by-Side

| Trait | Hostinger (confirmed) | Onylogy v1 (current) |
|---|---|---|
| Background | Flat, solid, single brand color | Diagonal two-tone gradient |
| Text on image | Yes — bold, large, states the topic | None — deliberately avoided |
| Icons | Large, literal, sometimes photographic/3D | Small, abstract, flat-vector only, tucked in cards |
| WP logo | Thin outline circle | Solid filled white circle |
| Photography | Yes — B&W collage or real event photos | None |
| Structure | Browser-window frame (often) | Floating glass cards, no frame |
| Instant topic clarity | High — text + literal objects | Low — abstract icons only, no words |

This table is the direct answer to the feedback: **the current Onylogy thumbnails are unclear specifically because
they have no text and rely on small, abstract icons that don't literally depict the topic.** Hostinger solves both
problems at once — bold words plus large, recognizable objects.

---

## The Merged System (v2) — What Changes for Onylogy

Keep what's already working (the flat/clean aesthetic, the recurring WordPress-logo anchor, the accent-color
palette, the brand-blue family) and adopt Hostinger's clarity techniques — **without copying Hostinger's literal
purple brand color**, since that's their brand identity, not a generic technique. Onylogy stays in its own blue
family; the *technique* is what's borrowed, not the palette.

1. **Flat solid background, no gradient.** Default: flat Onylogy blue. Technical topics: flat dark navy. Same two
   variants as before, just flattened — no diagonal blend.
2. **Add bold, large white text stating the exact topic** — 2–5 words, e.g. "LiteSpeed Cache," "6 Security
   Plugins," a plugin/theme name. This is the highest-impact single change.
3. **Make the hero icon large and literal**, not a small abstract glyph in a card. A padlock should look like a
   padlock at a size you can't miss, not a thin 40px line icon.
4. **Redraw the WordPress mark as a thin-outline circle** with a flat-tint "W," optionally with a small
   version/number badge — replacing the solid white disc.
5. **Introduce an optional browser-window frame** (rounded rect, 3-dot chrome bar, close button) as a structural
   container for guide/tutorial posts — reinforces "this is about a web tool," and gives text a natural anchor spot.
6. **Keep the thin line-art UI chrome and the accent-color dot/badge palette** — these already work and match both
   systems' vocabulary.
7. **Photographic/3D collage elements (the hand, the rendered padlock) are Tier 2** — genuinely part of what makes
   Hostinger's thumbnails feel premium, but **not reproducible in hand-written SVG**. Reaching this exact effect
   requires an actual image-generation model (the AI-prompt workflow already in `featured-image-guide.md` §12–14)
   or real stock/product photography composited in. The two test thumbnails below use the SVG-only route (items
   1–6); if you want the photographic layer too, say so and I'll adapt the AI prompts to include it.

---

## Test Thumbnails (this report's proof)

Two thumbnails were generated in the v2 system as a direct comparison to the v1 versions already on file:

- **LiteSpeed Cache (Part 1 — beginner guide)** → `thumbnails/litespeed-cache-beginner-thumbnail-v2.svg`
- **Top 6 WordPress Security Plugins** → `thumbnails/top-6-wordpress-security-plugins-thumbnail-v2.svg`

Compare each against its v1 counterpart already in the `thumbnails/` folder. If v2 reads as clearer and more
professional, the plan is to regenerate the other 8 existing thumbnails in the same system and adopt v2 as the new
standard in `featured-image-guide.md`.

---

## Round 2 Feedback → v3 → Grid-Scale Test → v4

**Feedback on v2:** the browser-window frame (rounded border + 3-dot/close-X chrome bar + panel divider) made the
thumbnail look like "a background with a window on top" rather than one cohesive image — correct call. Re-checking
the source images: that frame device only belongs to Hostinger's *profile-card* format (WordPress Experts posts),
not their general guide/release thumbnails, which have no enclosing frame at all. **v3** dropped the frame entirely
and pulled exact colors/fonts from the live site (`onylogy.com`) instead of approximated values — confirmed via
the site's real Kadence global palette (blue `#146EF5`/`#004BD1`, black `#131513`, grays, semantic accents
`#4CAF50`/`#03A9F4`/`#FF9800`/`#EF5350`) and confirmed font-face usage (Bricolage Grotesque + Montserrat).

**Feedback on v3:** too much of the canvas reads as empty/white space, and at real three-column blog-grid size the
secondary text (badge pill, subtitle line, "WordPress Guide" caption, small status pills like "CACHE: ON") and the
scattered micro line-art icons would be illegible or invisible.

**Self-test performed:** rendered v3's LiteSpeed Cache and Security Plugins thumbnails, plus the original v1
Install-WordPress thumbnail, inside an actual three-column card grid at realistic width (~370px cards, matching a
~1160px content area) with a real post-title caption underneath, mimicking a genuine archive page. At that scale:
- Badge/subtitle/caption text (set at 15–23px in the 1200px-wide source) renders at roughly **4–7px on screen** —
  illegible.
- Scattered micro line-art icons (toggle, cursor, gear, code bracket, loading ring, ~20–60px in source) shrink to
  sub-pixel specks — pure noise, and the reason the canvas *reads* as empty even though it technically has content.
- Only the main headline and the WP-logo blob survived at all, and the headline itself was smaller than ideal.

**v4 fixes, driven directly by that test:**
1. **Cut to exactly two text lines** — one bold topic headline (56–58px) + one short bold qualifier line (40px,
   e.g. "Beginner Guide" / "Top 6 Compared"). No separate badge pill, no thin subtitle, no caption under the WP
   logo, no small status pills on the hero icon. Every remaining text element is full-opacity, not dimmed.
2. **Hero icon scaled up substantially** — gauge radius 150→230, shield height ~343→~400, roughly 40–55% larger —
   so it reads as a clear, unmistakable shape even scaled down to card size, exactly because bold+large survives
   scaling in a way small detail never does.
3. **Removed every scattered micro-icon** (toggle, cursor, gear, code bracket, loading ring, server lines, browser
   tab, magnifier, login-card, key, firewall, accent dots). Down to three elements total: headline block, small
   WP-logo corner mark, one large hero icon with its one fused badge.
4. **Added one large soft background circle** (7% white opacity) behind the hero icon for depth/richness without
   adding anything that could vanish at small scale.
5. Re-ran the same three-column grid test with the v4 versions — headline and hero icon both read clearly at card
   size; no illegible text remains because none of the remaining text is small enough to be at risk.

**Casing fix:** kept Title Case consistent across all three test posts ("LiteSpeed Cache" / "Security Plugins" /
"Install WordPress" / "Beginner Guide" / "Top 6 Compared"), matching the blog's own H1 convention.

**v4 test files:** `litespeed-cache-beginner-thumbnail-v4.svg`, `top-6-wordpress-security-plugins-thumbnail-v4.svg`,
`how-to-install-wordpress-thumbnail-v4.svg`.
