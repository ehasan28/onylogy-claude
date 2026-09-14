# Onylogy Studio — Featured Image (Thumbnail) Style Guide

> **Purpose:** Reproduce Onylogy's blog featured images with AI, consistently, every time — no manual design.
> The style is a clean, modern **SaaS/tech flat-illustration** look inspired by Hostinger's blog thumbnails:
> a blue gradient background, a central white WordPress mark, and floating flat "glass" cards with minimal icons.
> This file gives you the exact spec **plus copy-paste AI prompts**. Pair with `blog-voice.md` and `blog-idea.md`.

Audited images (the visual canon):
1. **What Is WordPress** — blue gradient, central WP logo, flat UI cards + accent dots ✅ house style
2. **Top Hosting Providers** — dark-navy variant, 6 pastel icon cards on a blueprint grid ✅ house style
3. **Top Free Themes** — blue gradient, central WP logo + yellow "6" badge, ghost UI mockups ✅ house style
4. **6 Must-Have Plugins** — blue gradient, central WP logo, floating app-icon cards ✅ house style
5. **Common Mistakes** — cream background, hand-drawn doodle/stick-figure ⚠️ OFF-STYLE (see §8)
6. **KadenceWP** — the Kadence brand banner on topographic lines ⚠️ OFF-STYLE / product asset (see §8)

**The template below is built from images 1–4** (the consistent Hostinger-inspired look you like). Use it going
forward and, ideally, re-generate #5 and #6 to match.

---

## 1. Canvas & Format

- **Aspect ratio:** ~**1.91 : 1** (the standard OG / social-share ratio).
- **Dimensions:** **1200 × 630 px** (export target). The canon files are 1200×598–669; standardize on **1200×630**.
- **Safe zone:** keep the key subject within the centre ~80%; social platforms crop edges.
- **File:** export **.webp** (WordPress-friendly, light) at ~80–90% quality; keep under ~150 KB.
- **Filename:** keyword-descriptive, hyphenated (e.g. `how-to-install-wordpress.webp`).
- **Text in image:** mostly **none**. At most a tiny numeric badge (like the yellow "6" on roundups). Let the
  post title do the talking — a text-free thumbnail also reuses cleanly across social.

---

## 2. Background (the signature element)

Two approved variants. **Blue is the default; use Dark for security/technical/"under the hood" topics.**

**A) Royal-Blue Gradient (default — images 1, 3, 4)**
- Diagonal gradient, **brighter blue top-left → deeper indigo bottom-right.**
- Sampled hex: top-left **`#1B6FFE` / `#0D4FF3`** → bottom-right **`#193287` / `#3B27CF`** (a royal-blue-to-indigo blend).
- Optional soft purple/violet glow behind the centre subject.

**B) Dark Navy (variant — image 2)**
- Near-black navy gradient: **`#111727` → `#1B2339`**, with a subtle blue/purple radial glow in the middle.
- Use for hosting, security, performance, backups — anything "server/technical."

**Background texture (subtle, tone-on-tone, low opacity):** pick ONE per image —
- faint **dotted grid** of small dots (image 1),
- thin **blueprint grid + diagonal lines + constellation dots** (image 2),
- a few **4-point sparkles/stars** scattered (images 3, 4).
Keep texture at ~5–12% opacity so it never competes with the subject.

---

## 3. Composition Layouts

Three repeatable layouts. Pick by post type:

**Layout A — "Hero + Flanks" (for guides / single-topic posts)** — images 1, 4
- **Centre:** white WordPress logo inside a white circle (the anchor).
- **Left & right:** 2–4 floating flat cards holding minimal icons, symmetrically balanced.
- Best for: "What is…", "How to…", conceptual guides.

**Layout B — "Icon Grid" (for roundups / lists)** — image 2
- **2×3 grid of cards**, each a rounded card with one monoline icon + a row of 3 tiny colored dots underneath.
- Best for: "Top 6…", "X best…", comparison lists.

**Layout C — "Hero + Number Badge" (for numbered roundups)** — image 3
- Centre WP logo circle **plus a colored circular number badge** (e.g. yellow "6"), surrounded by faded
  low-opacity "ghost" UI wireframes (browser windows, layout blocks, lists).
- Best for: numbered "Top N" posts where you want the count visible.

Composition rules: **symmetrical, centred, generous negative space**, everything flat (no photos, no 3D realism).

---

## 4. The Central WordPress Mark

- Classic **WordPress "W" logo**, in its dark **teal-blue** (~`#1E5B7B`/`#21759B`), sitting inside a **solid white
  circle** with a soft shadow.
- Often decorated with a tiny badge on the circle's edge: a **green shield-check**, a **purple lightbulb**, etc.
- Size: roughly **18–26%** of the image width, centred.

---

## 5. Cards, Icons & Accent Dots

**Cards / tiles:**
- Rounded rectangles or squares, **corner radius ~16–24px.**
- Two finishes: **solid white / pastel-tinted** (mint, lavender, peach, sky) OR **translucent "glass"**
  (white at ~10–15% opacity with a soft border) over the blue.
- Soft, diffuse drop shadow; slight float. Occasionally one card is **tilted** a few degrees for energy (image 4).
- Optionally highlight one card with a **thin amber/yellow outline** to draw the eye (image 3).

**Icons:**
- **Flat, minimal, single-concept** — either monoline (image 2) or simple filled glyphs (image 4).
- One icon per card. Represent the topic literally: magnifier = SEO, shield = security, lightning = speed,
  document = content, server/database/cloud/chip = hosting, globe = website, layout blocks = themes.

**Accent status dots / badges (the "pop"):**
- Small circles in the corner of cards or under grid tiles.
- Palette: **green `#22C55E`** (check), **amber `#F5B301`**, **pink `#EC4899`**, **cyan `#38BDF8`**,
  **violet `#8B5CF6`**, **orange `#F97316`**.
- Used **sparingly** as accents against the dominant blue — 1 dot/badge per card at most.

---

## 6. Master Color Palette (hex)

| Role | Hex | Use |
|------|-----|-----|
| Blue gradient (light) | `#1B6FFE` / `#0D4FF3` | background top-left |
| Blue gradient (deep) | `#193287` / `#3B27CF` | background bottom-right |
| Dark navy (variant) | `#111727` → `#1B2339` | technical/security backgrounds |
| WordPress teal | `#1E5B7B` / `#21759B` | the central W logo |
| White | `#FFFFFF` | logo circle, solid cards |
| Green accent | `#22C55E` | checks / success dots |
| Amber accent | `#F5B301` | number badges, highlight outline |
| Pink accent | `#EC4899` | dots |
| Cyan accent | `#38BDF8` | dots |
| Violet accent | `#8B5CF6` | badges/dots |
| Orange accent | `#F97316` | dots |

---

## 7. Reusable AI Prompt (copy, fill the blanks)

> **MASTER PROMPT (Layout A — hero + flanks):**
> "Modern flat vector tech illustration, blog featured image, 1200x630, 1.91:1 wide banner. Background: smooth
> diagonal gradient from royal blue `#1B6FFE` (top-left) to deep indigo `#193287` (bottom-right), with a very
> subtle low-opacity dotted grid and a few small 4-point sparkles. Centre: the WordPress 'W' logo in dark teal
> inside a clean white circle with a soft shadow. Flanking the centre on the left and right: floating rounded-corner
> flat cards (white and translucent glass, radius ~20px, soft drop shadows), each holding one simple minimal icon
> representing **[TOPIC ICONS: e.g. a download arrow, a server, a gear, a checklist]**, with tiny green/amber/cyan
> accent status dots. Symmetrical, centred, lots of negative space, clean SaaS style, flat design, no photorealism,
> no 3D, no text. Style inspired by Hostinger blog thumbnails."
>
> **Then append a negative prompt (see §9).**

**Layout B (icon grid, for roundups):** replace the centre/flanks sentence with:
> "Composition: a neat 2×3 grid of six rounded flat cards, each pastel-tinted, each holding one minimal monoline
> icon (**[LIST 6 ICONS]**), with a row of three small colored dots under each card, on a dark navy blueprint-grid
> background with faint diagonal lines and constellation dots."

**Layout C (hero + number badge):** append:
> "Add a solid **[COLOR]** circular badge showing the number **[N]** near the centre, and scatter faded
> low-opacity white UI wireframe shapes (browser windows, layout blocks, lists) around the background."

Fill-in variables each time: **[TOPIC ICONS]**, **[Layout A/B/C]**, **[background: blue default / dark navy]**,
**[number N if roundup]**.

---

## 8. Two Images to Re-Generate (currently off-style)

- **Common Mistakes (#5):** cream background + hand-drawn stick-figure doodle. Charming but a totally different
  aesthetic — breaks the set. Re-make in Layout A with a "crossed-out vs checkmark" pair of cards on the blue bg.
- **KadenceWP (#6):** this is Kadence's own brand banner, not your house style. For product-specific posts it's
  defensible, but for consistency, wrap the product logo inside your blue-gradient template (Layout A) instead.

Keeping all thumbnails on one system makes your blog index and social feed look instantly cohesive.

---

## 9. Negative Prompt / Avoid List

Always exclude: `photorealistic, 3D render, realistic photo, hand-drawn, doodle, sketch, watercolor, grunge,
cluttered, busy background, drop-shadow text, spelling, paragraphs of text, watermark, stock-photo people,
gradients that are red/green/warm, low contrast, off-center, cartoon mascot`.

Keep it: **flat, vector, clean, blue, symmetrical, minimal, lots of space.**

---

## 10. Per-Post Icon Cheat-Sheet (for upcoming blogs)

| Post | Layout | Background | Suggested icons |
|------|--------|-----------|-----------------|
| How to Install WordPress | A | Blue | download/arrow, server, gear, checkmark, WP logo centre |
| WordPress.com vs .org | A | Blue | two mirrored cards: ".com" cloud vs ".org" server, balance/vs in centre |
| Dashboard Tour | A | Blue | admin sidebar, widgets, gear, bell, layout blocks |
| First Post / Gutenberg | A | Blue | block/plus icon, paragraph, image block, publish arrow |
| Security Checklist | A or B | **Dark navy** | shield-check, lock, key, firewall, eye |
| Speed / Core Web Vitals | A | **Dark navy** | lightning, gauge/speedometer, stopwatch, rocket |
| Hosting/Themes/Plugins roundups | B | Blue or Navy | 6 topic icons in a 2×3 grid |

---

## 11. Quick Checklist Before Using an Image

- [ ] 1200×630, 1.91:1, exported as light .webp with a keyword filename.
- [ ] Blue gradient (or dark navy for technical topics) with ONE subtle texture.
- [ ] Central white WP logo circle (Layout A/C) or 2×3 icon grid (Layout B).
- [ ] Flat cards, ~20px radius, soft shadows, 1 minimal icon each.
- [ ] Accent dots used sparingly (green/amber/cyan/pink/violet/orange).
- [ ] Symmetrical, centred, lots of negative space, NO text (except an optional number badge).
- [ ] Matches images 1–4; not the doodle (#5) or brand-banner (#6) look.

---

## 12. How to Actually Generate These (tooling reality)

**This file is a spec, not a one-click generator.** Two-step workflow:

1. **Get a filled prompt** — paste the *System Prompt* (§13) into any chat LLM (Claude, ChatGPT, Gemini), give it
   a blog topic, and it returns a ready-to-use image prompt tailored to that topic and on-brand.
2. **Render the image** — paste that prompt into a **text-to-image model**:
   - **Google Gemini / Imagen ("nano banana")**, **Midjourney**, **DALL·E 3 (in ChatGPT)**, **Ideogram**,
     **Leonardo**, or **Adobe Firefly**. Any of these produce the flat SaaS style well.
   - For a **wide 1.91:1 banner**: Midjourney add `--ar 191:100`; others, set size to 1536×640 / 1200×630 and crop.

> **Note on Claude:** Claude can't output a photographic PNG. But because your style is **flat vector**, Claude
> *can* generate the thumbnail directly as **SVG code** (infinitely consistent, editable, free) — a great
> alternative to an image model. Ask for "an SVG thumbnail using featured-image-guide.md" and you get a vector
> file. Use whichever route you prefer; the prompts below serve the image-model route.

---

## 13. SYSTEM PROMPT — "Onylogy Thumbnail Prompt Generator"

*Paste this whole block into Claude/ChatGPT/Gemini, then just send it a blog title. It outputs a finished image
prompt you paste into an image generator. This is what keeps every thumbnail on-brand.*

```
You are Onylogy Studio's blog-thumbnail prompt generator. When I give you a blog post title, you output ONE
ready-to-paste text-to-image prompt for a featured image in Onylogy's fixed brand style. Never change the brand
style; only change the topic-specific icons and layout choice.

FIXED BRAND STYLE (never alter):
- Modern flat vector tech illustration, clean SaaS look, inspired by Hostinger blog thumbnails. No photorealism,
  no 3D, no hand-drawn/doodle, no stock-photo people, and NO text in the image (a single small number badge is
  the only exception, allowed on numbered roundups).
- Canvas: 1200x630, 1.91:1 wide banner, subject centered, generous negative space, symmetrical.
- Background (default): smooth diagonal gradient from royal blue #1B6FFE (top-left) to deep indigo #193287
  (bottom-right), plus ONE subtle low-opacity texture (dotted grid OR blueprint grid with faint diagonal lines
  and constellation dots OR a few 4-point sparkles).
- Background (variant, use for security / speed / hosting / "technical" topics): dark navy gradient
  #111727 to #1B2339 with a soft blue-purple center glow and a faint blueprint grid.
- Center anchor (for guide/how-to/what-is posts): the WordPress "W" logo in dark teal (#1E5B7B) inside a solid
  white circle with a soft shadow, optionally a tiny green shield-check or purple lightbulb badge on its edge.
- Elements: floating rounded flat cards (radius ~20px), white or translucent glass, soft drop shadows, one
  minimal flat icon per card, tiny accent status dots in green #22C55E, amber #F5B301, cyan #38BDF8, pink
  #EC4899, or violet #8B5CF6 (used sparingly).

CHOOSE A LAYOUT based on the title:
- Layout A "hero + flanks" -> for how-to / what-is / single-topic guides: center WP logo circle with 2–4 icon
  cards on the left and right.
- Layout B "icon grid" -> for roundups/lists ("Top 6", "best"): a 2x3 grid of pastel cards, each with one
  monoline icon and a row of 3 small colored dots underneath. (Usually no center WP logo.)
- Layout C "hero + number badge" -> for numbered roundups where the count should show: center WP logo circle
  PLUS a colored circular badge with the number, surrounded by faded low-opacity white UI wireframe shapes.

TOPIC ICONS: pick 2–6 simple, literal flat icons that represent the post's subject (e.g. install = download
arrow/server/gear/checkmark; security = shield/lock/key/eye; speed = lightning/gauge/rocket; content = block/
paragraph/publish arrow; comparison = two mirrored cards with a "vs" element).

OUTPUT FORMAT: return only the final prompt as a single paragraph, then on a new line a NEGATIVE PROMPT line:
"Negative prompt: photorealistic, 3D, realistic photo, hand-drawn, doodle, sketch, watercolor, cluttered, busy,
text, paragraphs, spelling, watermark, stock-photo people, warm/red/green background, low contrast, off-center."
Also add a line suggesting the aspect ratio flag (e.g. "Midjourney: --ar 191:100").
```

---

## 14. MASTER IMAGE PROMPT (paste straight into an image model)

Fill the two **{BRACKETS}** and go. Everything else is locked to your brand.

```
Modern flat vector tech illustration, blog featured image, 1200x630, 1.91:1 wide banner, clean SaaS style
inspired by Hostinger blog thumbnails. Background: smooth diagonal gradient from royal blue #1B6FFE (top-left)
to deep indigo #193287 (bottom-right), with a subtle low-opacity dotted grid and a few faint 4-point sparkles.
Center: the WordPress "W" logo in dark teal #1E5B7B inside a clean solid white circle with a soft shadow.
Flanking left and right: floating rounded-corner flat cards (white and translucent glass, ~20px radius, soft
drop shadows), each holding one simple minimal flat icon representing {TOPIC ICONS: e.g. a download arrow, a
server, a gear, a checkmark}, with tiny green, amber and cyan accent status dots. Symmetrical, centered, lots of
negative space, flat design, no photorealism, no 3D, no text.
Negative prompt: photorealistic, 3D, realistic photo, hand-drawn, doodle, sketch, watercolor, cluttered, busy,
text, paragraphs, spelling, watermark, stock-photo people, warm/red/green background, low contrast, off-center.
Aspect ratio: 1.91:1 (Midjourney: --ar 191:100).
```

**Worked example — "How to Install WordPress":** replace `{TOPIC ICONS...}` with
`a download/cloud-arrow icon, a server stack, a gear, and a green checkmark` → paste and render.

**For a roundup** (e.g. "Top 6 …"), swap the center/flanks sentence for Layout B from §7 and list your six icons.
