#!/usr/bin/env python3
"""Generate an Onylogy v4 featured image (SVG + WEBP) for a post. Spec: references/thumbnail-guide.md

usage: thumb.py SLUG "Line one" "Line two" [--bg blue|black] [--icon NAME] [--accent2] [--out DIR]
       thumb.py --list-icons
       thumb.py --sheet OUT.png            render every icon on a contact sheet (for picking / adding icons)

Writes Blogs/<slug>/<slug>-thumbnail.svg and .webp (and a copy to Blog Posts/thumbnails/<slug>-thumbnail-v4.svg).
Needs rsvg-convert (brew install librsvg) and Pillow in tooling/.venv (run setup.sh).
"""
import os, re, subprocess, sys, tempfile
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))
THUMBS = os.path.join(os.path.dirname(BLOGS), "thumbnails")
BLUE, BLACK, CYAN, ORANGE, DARK, W = "#146EF5", "#131513", "#03A9F4", "#FF9800", "#131513", "#FFFFFF"
FONT = "'Bricolage Grotesque','Poppins',Arial,sans-serif"

def icons(acc):
    I = {}
    I["stack"] = f'<g fill="none"><rect x="740" y="290" width="190" height="190" rx="18" stroke="{W}" stroke-width="9" opacity="0.45"/><rect x="790" y="330" width="190" height="190" rx="18" stroke="{W}" stroke-width="10" opacity="0.72"/><rect x="840" y="370" width="190" height="190" rx="18" stroke="{W}" stroke-width="14"/></g>'
    I["vs"] = f'<rect x="720" y="220" width="150" height="150" rx="20" fill="none" stroke="{W}" stroke-width="12"/><rect x="920" y="300" width="150" height="150" rx="20" fill="none" stroke="{W}" stroke-width="12"/><circle cx="895" cy="335" r="52" fill="{acc}"/><text x="895" y="352" font-family="Arial,sans-serif" font-weight="800" font-size="46" fill="{DARK}" text-anchor="middle">VS</text>'
    I["three"] = f'<rect x="720" y="380" width="330" height="110" rx="18" fill="none" stroke="{W}" stroke-width="12"/><rect x="760" y="290" width="250" height="110" rx="18" fill="none" stroke="{W}" stroke-width="12" opacity="0.75"/><rect x="800" y="200" width="170" height="110" rx="18" fill="{acc}"/>'
    I["palette"] = f'<rect x="720" y="230" width="150" height="150" rx="20" fill="{W}"/><rect x="900" y="230" width="150" height="150" rx="20" fill="{W}" opacity="0.7"/><rect x="720" y="410" width="150" height="150" rx="20" fill="{W}" opacity="0.45"/><rect x="900" y="410" width="150" height="150" rx="20" fill="{acc}"/><text x="975" y="505" font-family="Arial,sans-serif" font-weight="800" font-size="44" fill="{DARK}" text-anchor="middle">Aa</text>'
    I["H"] = f'<rect x="740" y="210" width="300" height="300" rx="24" fill="none" stroke="{W}" stroke-width="12"/><text x="890" y="425" font-family="Arial,sans-serif" font-weight="800" font-size="200" fill="{W}" text-anchor="middle">H</text><circle cx="1030" cy="230" r="34" fill="{acc}"/><text x="1030" y="243" font-family="Arial,sans-serif" font-weight="800" font-size="34" fill="{DARK}" text-anchor="middle">2</text>'
    I["grid"] = f'<g fill="none" stroke="{W}" stroke-width="12"><rect x="720" y="200" width="330" height="90" rx="16"/><rect x="720" y="320" width="150" height="200" rx="16"/><rect x="900" y="320" width="150" height="200" rx="16"/></g><rect x="740" y="340" width="110" height="14" rx="7" fill="{acc}"/><rect x="920" y="340" width="110" height="14" rx="7" fill="{acc}"/>'
    I["infobox"] = f'<rect x="740" y="190" width="290" height="340" rx="24" fill="none" stroke="{W}" stroke-width="12"/><circle cx="885" cy="290" r="50" fill="{acc}"/><rect x="800" y="370" width="170" height="20" rx="10" fill="{W}"/><rect x="780" y="415" width="210" height="14" rx="7" fill="{W}" opacity="0.6"/><rect x="800" y="450" width="170" height="14" rx="7" fill="{W}" opacity="0.6"/>'
    I["quote"] = f'<rect x="740" y="190" width="300" height="330" rx="24" fill="none" stroke="{W}" stroke-width="12"/><text x="890" y="400" font-family="Georgia,serif" font-weight="bold" font-size="260" fill="{W}" text-anchor="middle">&#8221;</text><circle cx="800" cy="470" r="26" fill="{acc}"/><rect x="840" y="458" width="150" height="14" rx="7" fill="{W}" opacity="0.7"/>'
    I["accordion"] = f'<g fill="none" stroke="{W}" stroke-width="12"><rect x="720" y="190" width="330" height="70" rx="14"/><rect x="720" y="290" width="330" height="150" rx="14"/><rect x="720" y="470" width="330" height="70" rx="14"/></g><polyline points="1000,215 1015,235 1030,215" fill="none" stroke="{acc}" stroke-width="10" stroke-linecap="round"/><rect x="745" y="330" width="220" height="14" rx="7" fill="{acc}"/><rect x="745" y="365" width="180" height="14" rx="7" fill="{W}" opacity="0.6"/>'
    g = ""
    for i, (x, y) in enumerate([(720, 220), (840, 220), (960, 220), (720, 340), (840, 340), (960, 340)]):
        g += f'<rect x="{x}" y="{y}" width="100" height="100" rx="14" fill="{acc if i == 4 else W}" opacity="{"1" if i in (0, 4) else "0.6"}"/>'
    I["gallery"] = g + f'<rect x="720" y="470" width="340" height="60" rx="14" fill="none" stroke="{W}" stroke-width="10"/>'
    I["form"] = f'<g fill="none" stroke="{W}" stroke-width="12"><rect x="720" y="200" width="330" height="70" rx="14"/><rect x="720" y="300" width="330" height="70" rx="14"/><rect x="720" y="400" width="330" height="110" rx="14"/></g><rect x="720" y="545" width="180" height="56" rx="12" fill="{acc}"/><text x="810" y="583" font-family="Arial,sans-serif" font-weight="700" font-size="30" fill="{DARK}" text-anchor="middle">Send</text>'
    I["page"] = f'<rect x="720" y="170" width="330" height="390" rx="20" fill="none" stroke="{W}" stroke-width="12"/><rect x="750" y="205" width="270" height="90" rx="12" fill="{W}" opacity="0.85"/><rect x="750" y="320" width="80" height="80" rx="12" fill="{acc}"/><rect x="845" y="320" width="80" height="80" rx="12" fill="{W}" opacity="0.5"/><rect x="940" y="320" width="80" height="80" rx="12" fill="{W}" opacity="0.5"/><rect x="750" y="430" width="270" height="20" rx="10" fill="{W}" opacity="0.6"/><rect x="750" y="470" width="180" height="20" rx="10" fill="{W}" opacity="0.6"/>'
    I["warn"] = f'<rect x="740" y="190" width="300" height="300" rx="24" fill="none" stroke="{W}" stroke-width="12"/><polygon points="890,240 1000,440 780,440" fill="{acc}"/><rect x="880" y="300" width="20" height="80" rx="8" fill="{DARK}"/><circle cx="890" cy="410" r="12" fill="{DARK}"/>'
    I["gauge"] = f'<path d="M660,470 A230,230 0 0 1 1120,470" fill="none" stroke="{W}" stroke-width="26" stroke-linecap="round"/><path d="M660,470 A230,230 0 0 1 760,300" fill="none" stroke="{acc}" stroke-width="26" stroke-linecap="round"/><line x1="890" y1="470" x2="1010" y2="330" stroke="{W}" stroke-width="18" stroke-linecap="round"/><circle cx="890" cy="470" r="30" fill="{W}"/>'
    I["shield"] = f'<path d="M890,170 L1060,230 L1060,370 C1060,470 980,540 890,570 C800,540 720,470 720,370 L720,230 Z" fill="none" stroke="{W}" stroke-width="16" stroke-linejoin="round"/><circle cx="890" cy="380" r="70" fill="{acc}"/><polyline points="850,380 880,410 935,350" fill="none" stroke="{DARK}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
    I["frame"] = f'<rect x="700" y="240" width="360" height="300" rx="28" fill="none" stroke="{W}" stroke-width="16"/><circle cx="800" cy="330" r="34" fill="{W}"/><path d="M740,500 L850,380 L920,450 L960,415 L1020,500 Z" fill="{W}"/><circle cx="1050" cy="270" r="50" fill="{acc}"/><path d="M1024,244 l16,0 l0,16 M1040,244 l-20,20" fill="none" stroke="{DARK}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M1076,296 l-16,0 l0,-16 M1060,296 l20,-20" fill="none" stroke="{DARK}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    I["cloud"] = f'<path d="M780,470 a80,80 0 0 1 20,-158 a120,120 0 0 1 230,-20 a90,90 0 0 1 30,178 Z" fill="none" stroke="{W}" stroke-width="16" stroke-linejoin="round"/><line x1="890" y1="530" x2="890" y2="380" stroke="{acc}" stroke-width="18" stroke-linecap="round"/><polyline points="840,430 890,380 940,430" fill="none" stroke="{acc}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>'
    I["globe"] = f'<circle cx="890" cy="380" r="170" fill="none" stroke="{W}" stroke-width="14"/><ellipse cx="890" cy="380" rx="75" ry="170" fill="none" stroke="{W}" stroke-width="10" opacity="0.8"/><line x1="720" y1="380" x2="1060" y2="380" stroke="{W}" stroke-width="10" opacity="0.8"/><path d="M745,290 Q890,340 1035,290" fill="none" stroke="{W}" stroke-width="10" opacity="0.8"/><path d="M745,470 Q890,420 1035,470" fill="none" stroke="{W}" stroke-width="10" opacity="0.8"/><rect x="960" y="480" width="150" height="56" rx="12" fill="{acc}"/><text x="1035" y="519" font-family="Arial,sans-serif" font-weight="800" font-size="30" fill="{DARK}" text-anchor="middle">.com</text>'
    I["server"] = f'<g fill="none" stroke="{W}" stroke-width="14"><rect x="730" y="210" width="320" height="100" rx="18"/><rect x="730" y="330" width="320" height="100" rx="18"/><rect x="730" y="450" width="320" height="100" rx="18"/></g><circle cx="1005" cy="260" r="14" fill="{acc}"/><circle cx="1005" cy="380" r="14" fill="{acc}"/><circle cx="1005" cy="500" r="14" fill="{acc}"/><rect x="765" y="250" width="120" height="18" rx="9" fill="{W}" opacity="0.7"/><rect x="765" y="370" width="120" height="18" rx="9" fill="{W}" opacity="0.7"/><rect x="765" y="490" width="120" height="18" rx="9" fill="{W}" opacity="0.7"/>'
    I["search"] = f'<circle cx="860" cy="350" r="130" fill="none" stroke="{W}" stroke-width="20"/><line x1="955" y1="445" x2="1070" y2="560" stroke="{W}" stroke-width="30" stroke-linecap="round"/><polyline points="800,380 840,330 880,360 930,290" fill="none" stroke="{acc}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
    I["plug"] = f'<rect x="760" y="330" width="260" height="170" rx="30" fill="none" stroke="{W}" stroke-width="16"/><rect x="810" y="230" width="40" height="110" rx="12" fill="{W}"/><rect x="930" y="230" width="40" height="110" rx="12" fill="{W}"/><rect x="860" y="500" width="60" height="70" rx="14" fill="{acc}"/>'
    I["brush"] = f'<path d="M1040,200 L900,340" stroke="{W}" stroke-width="34" stroke-linecap="round"/><path d="M900,340 C860,380 880,440 820,470 C780,490 740,470 720,500 C760,520 830,540 880,500 C930,460 920,400 900,340 Z" fill="{W}"/><circle cx="760" cy="290" r="40" fill="{acc}"/>'
    I["download"] = f'<rect x="720" y="470" width="340" height="80" rx="20" fill="none" stroke="{W}" stroke-width="14"/><line x1="890" y1="190" x2="890" y2="410" stroke="{W}" stroke-width="26" stroke-linecap="round"/><polyline points="800,330 890,420 980,330" fill="none" stroke="{acc}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>'
    I["dashboard"] = f'<rect x="700" y="200" width="380" height="330" rx="22" fill="none" stroke="{W}" stroke-width="14"/><rect x="700" y="200" width="110" height="330" rx="22" fill="{W}" opacity="0.85"/><rect x="840" y="240" width="200" height="60" rx="12" fill="{acc}"/><rect x="840" y="330" width="90" height="70" rx="12" fill="{W}" opacity="0.6"/><rect x="950" y="330" width="90" height="70" rx="12" fill="{W}" opacity="0.6"/><rect x="840" y="430" width="200" height="60" rx="12" fill="{W}" opacity="0.6"/>'
    I["pen"] = f'<rect x="720" y="190" width="300" height="360" rx="22" fill="none" stroke="{W}" stroke-width="14"/><rect x="760" y="240" width="220" height="22" rx="11" fill="{W}"/><rect x="760" y="300" width="180" height="16" rx="8" fill="{W}" opacity="0.6"/><rect x="760" y="340" width="200" height="16" rx="8" fill="{W}" opacity="0.6"/><rect x="760" y="380" width="150" height="16" rx="8" fill="{W}" opacity="0.6"/><path d="M1080,300 L1000,380 L985,455 L1060,440 L1140,360 Z" fill="{acc}" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>'
    I["mail"] = f'<rect x="720" y="230" width="340" height="240" rx="24" fill="none" stroke="{W}" stroke-width="16"/><polyline points="720,250 890,380 1060,250" fill="none" stroke="{W}" stroke-width="16" stroke-linejoin="round"/><circle cx="1050" cy="250" r="44" fill="{acc}"/><text x="1050" y="265" font-family="Arial,sans-serif" font-weight="800" font-size="40" fill="{DARK}" text-anchor="middle">1</text>'
    I["cart"] = f'<path d="M700,230 L760,230 L810,450 L1030,450 L1070,300 L780,300" fill="none" stroke="{W}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/><circle cx="850" cy="520" r="28" fill="{W}"/><circle cx="1000" cy="520" r="28" fill="{W}"/><rect x="880" y="330" width="90" height="80" rx="12" fill="{acc}"/>'
    I["lock"] = f'<rect x="740" y="320" width="300" height="230" rx="28" fill="none" stroke="{W}" stroke-width="16"/><path d="M800,320 V260 a90,90 0 0 1 180,0 V320" fill="none" stroke="{W}" stroke-width="16" stroke-linecap="round"/><circle cx="890" cy="425" r="30" fill="{acc}"/><rect x="878" y="440" width="24" height="50" rx="10" fill="{acc}"/>'
    I["wp"] = f'<circle cx="890" cy="380" r="170" fill="none" stroke="{W}" stroke-width="14"/><text x="890" y="445" font-family="Georgia,\'Times New Roman\',serif" font-weight="bold" font-size="190" fill="{W}" text-anchor="middle">W</text><circle cx="1030" cy="260" r="40" fill="{acc}"/>'
    return I

def svg(l1, l2, bg, icon, accent2=False, size1=None):
    acc = CYAN if bg == BLUE else ORANGE
    I = icons(acc)
    if icon not in I: raise SystemExit(f"unknown icon {icon}; try --list-icons")
    size1 = size1 or (60 if len(l1) <= 14 else 52 if len(l1) <= 18 else 46)
    color2 = ORANGE if (accent2 or bg == BLACK) else W
    return f'''<svg width="1200" height="630" viewBox="0 0 1200 630" role="img" xmlns="http://www.w3.org/2000/svg">
<title>{escape(l1)} {escape(l2)} featured image, v4 style</title>
<desc>Flat Onylogy banner with headline {escape(l1)}, {escape(l2)}, a small WordPress logo mark, and a large literal hero icon ({icon}).</desc>
<rect width="1200" height="630" fill="{bg}"/>
<circle cx="880" cy="390" r="300" fill="{W}" opacity="{'0.05' if bg == BLACK else '0.07'}"/>
<text x="90" y="250" font-family="{FONT}" font-weight="700" font-size="{size1}" fill="{W}">{escape(l1)}</text>
<text x="90" y="305" font-family="{FONT}" font-weight="700" font-size="40" fill="{color2}">{escape(l2)}</text>
<circle cx="112" cy="540" r="34" fill="none" stroke="{W}" stroke-width="3" opacity="0.85"/>
<text x="112" y="554" font-family="Georgia,'Times New Roman',serif" font-weight="bold" font-size="34" fill="{W}" text-anchor="middle">W</text>
{I[icon]}
</svg>
'''

def render(svg_path, webp_path):
    png = tempfile.mktemp(suffix=".png")
    subprocess.run(["rsvg-convert", "-w", "1200", "-h", "630", svg_path, "-o", png], check=True)
    py = os.path.join(HERE, ".venv", "bin", "python")
    if not os.path.exists(py): py = sys.executable
    subprocess.run([py, "-c", f"from PIL import Image; Image.open('{png}').convert('RGB').save('{webp_path}','WEBP',quality=85)"], check=True)
    os.remove(png)

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"): print(__doc__); return
    if a[0] == "--list-icons": print(" ".join(sorted(icons(CYAN)))); return
    if a[0] == "--sheet":
        out = a[1]; names = sorted(icons(CYAN)); tmp = tempfile.mkdtemp(); paths = []
        for n in names:
            p = os.path.join(tmp, n + ".svg"); open(p, "w").write(svg(n, "icon", BLUE, n)); q = p[:-4] + ".png"
            subprocess.run(["rsvg-convert", "-w", "400", "-h", "210", p, "-o", q], check=True); paths.append(q)
        py = os.path.join(HERE, ".venv", "bin", "python")
        subprocess.run([py, "-c", f"""
from PIL import Image; ps={paths!r}; cols=4; rows=(len(ps)+cols-1)//cols
sheet=Image.new('RGB',(cols*400,rows*210),'white')
for i,p in enumerate(ps): sheet.paste(Image.open(p),((i%cols)*400,(i//cols)*210))
sheet.save({out!r})"""], check=True); print("sheet:", out); return
    slug, l1, l2 = a[0], a[1], a[2]
    bg = BLACK if "--bg" in a and a[a.index("--bg") + 1] == "black" else BLUE
    icon = a[a.index("--icon") + 1] if "--icon" in a else "stack"
    outdir = a[a.index("--out") + 1] if "--out" in a else os.path.join(BLOGS, slug)
    if "—" in l1 + l2 or "–" in l1 + l2: raise SystemExit("no dashes in thumbnail text")
    os.makedirs(outdir, exist_ok=True)
    s = svg(l1, l2, bg, icon, accent2="--accent2" in a)
    svg_path = os.path.join(outdir, f"{slug}-thumbnail.svg"); open(svg_path, "w").write(s)
    webp_path = os.path.join(outdir, f"{slug}-thumbnail.webp"); render(svg_path, webp_path)
    if os.path.isdir(THUMBS): open(os.path.join(THUMBS, f"{slug}-thumbnail-v4.svg"), "w").write(s)
    print(f"{svg_path}\n{webp_path} ({os.path.getsize(webp_path)//1024} KB)")

if __name__ == "__main__":
    main()
