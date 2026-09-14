#!/usr/bin/env python
"""Capture a page with headless Chromium, crop by pixel-sampling, resize to 1200 wide, save webp.

usage: shot.py URL OUT.webp [wporg|hero] [hero_height]
  wporg: WordPress.org plugin page. Detect the banner by pixel-sampling (fixed side padding, never eyeball),
         crop banner + title/author/download block, edge to edge.
  hero:  marketing/homepage. Crop the top hero_height px full width.
"""
import os, subprocess, sys, tempfile
from PIL import Image

CH = os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-mac-arm64/chrome-headless-shell")
W = 1360

def capture(url, height):
    tmp = tempfile.mktemp(suffix=".png")
    cmd = [CH, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
           f"--window-size={W},{height}", "--virtual-time-budget=10000",
           "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36",
           f"--screenshot={tmp}", url]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
    return Image.open(tmp).convert("RGB")

def nonwhite(p, t=245):
    return not (p[0] > t and p[1] > t and p[2] > t)

def crop_wporg(im):
    w, h = im.size
    l0, r0 = 100, W - 101          # known content bounds at 1360; verified by sampling below
    xs = list(range(l0 + 20, r0 - 20, 8))
    def frac(y):
        return sum(1 for x in xs if nonwhite(im.getpixel((x, y)))) / len(xs)
    y = 200                        # below the search box row
    while y < h and frac(y) < 0.5: y += 1
    top = y
    while y < h and frac(y) > 0.02: y += 1
    bot = y
    if bot - top < 150:            # no banner on this listing
        top, bot = 200, 200
    rows = [top + d for d in (20, 60, 120, 200, 300) if top + d < bot] if bot > top else [230]
    l, r = w, 0
    for row in rows:
        li = 0
        while li < w and not nonwhite(im.getpixel((li, row))): li += 1
        ri = w - 1
        while ri > 0 and not nonwhite(im.getpixel((ri, row))): ri -= 1
        l, r = min(l, li), max(r, ri)
    if r - l < 600: l, r = l0, r0
    bottom = min(h, bot + 150) if bot > top else min(h, top + 520)
    return im.crop((l, top, r + 1, bottom)), (l, r, top, bot, bottom)

def main():
    url, out = sys.argv[1], sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else "wporg"
    hero_h = int(sys.argv[4]) if len(sys.argv) > 4 else 800
    if mode == "wporg":
        im = capture(url, 1100)
        im, info = crop_wporg(im)
    else:
        im = capture(url, hero_h)
        im, info = im.crop((0, 0, W, hero_h)), (0, W - 1, 0, 0, hero_h)
    ratio = 1200 / im.width
    im = im.resize((1200, round(im.height * ratio)), Image.LANCZOS)
    im.save(out, "WEBP", quality=82, method=6)
    print(f"{os.path.basename(out)}: crop l/r/top/bot/bottom={info} -> {im.size} {os.path.getsize(out)//1024}KB")

if __name__ == "__main__":
    main()
