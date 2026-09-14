// Build the term paper .docx from the marked-up manuscript.
// usage: node build.js [--bijoy] [--pagemap out/pagemap.json] --out out/file.docx
const fs = require('fs');
const path = require('path');
const docx = require('docx');
const FRONT = require('./front');

const {
  Document, Packer, Paragraph, TextRun, FootnoteReferenceRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, ShadingType, PageBreak, PageNumber, Footer,
  ImageRun, NumberFormat, VerticalAlign, Bookmark, SimpleField, LineRuleType,
  PageBorderDisplay, PageBorderOffsetFrom, PageBorderZOrder, UnderlineType,
} = docx;

// ---------- CLI ----------
const argv = process.argv.slice(2);
const opt = (name, def) => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : def; };
const BIJOY = argv.includes('--bijoy');
const OUT = opt('--out', path.join(__dirname, '..', 'out', BIJOY ? 'term-paper-bijoy.docx' : 'term-paper-unicode.docx'));
const PAGEMAP = (() => { const p = opt('--pagemap', null); if (p && fs.existsSync(p)) return JSON.parse(fs.readFileSync(p, 'utf8')); return {}; })();

const FONT_BN = BIJOY ? 'SutonnyMJ' : (process.env.BN_FONT || 'SutonnyOMJ');
const FONT_EN = 'Times New Roman';

// ---------- Bijoy conversion ----------
let toBijoy = (t) => t;
if (BIJOY) {
  const { bnUnicode2ANSI } = require('@codesigntheory/bnunicode2ansi');
  const pre = (t) => t
    .replace(/য়/g, 'য়').replace(/ড়/g, 'ড়').replace(/ঢ়/g, 'ঢ়')
    .replace(/[‌‍]/g, '');
  const post = (a) => a.replace(/।/g, '|').replace(/&h/g, '¨');
  toBijoy = (t) => pre(t).split(/(\s+)/).map((tok) => {
    if (!tok || /^\s+$/.test(tok)) return tok;
    try { return post(bnUnicode2ANSI(tok)); } catch (e) { console.error('bijoy fail:', tok); return tok; }
  }).join('');
}

// ---------- text → runs ----------
const isBn = (c) => c >= 'ঀ' && c <= '৿';
const isLa = (c) => /[A-Za-z0-9À-ɏ–—‘’“”]/.test(c);

function splitScript(text) {
  const segs = []; let cur = null; let pending = '';
  for (const ch of text) {
    let s = isBn(ch) ? 'bn' : isLa(ch) ? 'la' : null;
    if (s === null) { if (cur) cur.text += ch; else pending += ch; continue; }
    if (!cur || cur.script !== s) { cur = { script: s, text: pending + ch }; pending = ''; segs.push(cur); }
    else cur.text += ch;
  }
  if (pending) { if (cur) cur.text += pending; else segs.push({ script: 'bn', text: pending }); }
  return segs;
}

// Convert one plain string (no markup) into TextRuns with the right font per script.
function scriptRuns(text, o = {}) {
  const size = o.size || 24;
  return splitScript(text).map((seg) => {
    const bn = seg.script === 'bn';
    const font = bn ? FONT_BN : FONT_EN;
    return new TextRun({
      text: bn && BIJOY ? toBijoy(seg.text) : seg.text,
      font: { ascii: font, hAnsi: font, cs: font, eastAsia: font },
      size, sizeComplexScript: size,
      bold: !!o.bold, italics: !!o.italics,
      underline: o.underline ? { type: UnderlineType.SINGLE } : undefined,
      superScript: !!o.superScript,
    });
  });
}

// Footnotes registry
const FN_TEXT = {};
const footnotes = {};
let fnId = 0; let lastKey = null; let paraKeys = new Set();
const unknownFn = new Set();
function fnRef(key) {
  if (!FN_TEXT[key]) { unknownFn.add(key); return new TextRun({ text: '[?fn:' + key + ']', superScript: true, color: 'C00000', size: 18 }); }
  if (paraKeys.has(key)) return null; // already cited in this paragraph
  paraKeys.add(key);
  fnId += 1;
  const text = key === lastKey ? 'প্রাগুক্ত।' : FN_TEXT[key];
  lastKey = key;
  footnotes[fnId] = { children: [new Paragraph({ alignment: AlignmentType.BOTH, spacing: { after: 0, line: 240 }, children: runs(text, { size: 20 }) })] };
  return new FootnoteReferenceRun(fnId);
}

// Inline markup: {{fn:key}} and *italic*
function runs(text, o = {}) {
  const out = [];
  const parts = text.split(/(\{\{fn:[a-z0-9_]+\}\}|\*[^*]+\*)/g);
  for (const p of parts) {
    if (!p) continue;
    let m;
    if ((m = p.match(/^\{\{fn:([a-z0-9_]+)\}\}$/))) { const r = fnRef(m[1]); if (r) out.push(r); }
    else if ((m = p.match(/^\*([^*]+)\*$/))) out.push(...scriptRuns(m[1], { ...o, italics: true }));
    else out.push(...scriptRuns(p, o));
  }
  return out;
}

// ---------- paragraph helpers ----------
const LINE = 360; // 1.5 lines
function P(text, o = {}) {
  paraKeys = new Set();
  return new Paragraph({
    alignment: o.align || AlignmentType.BOTH,
    spacing: { before: o.before || 0, after: o.after == null ? 120 : o.after, line: o.line || LINE, lineRule: LineRuleType.AUTO },
    indent: o.indent,
    keepNext: !!o.keepNext,
    pageBreakBefore: !!o.pageBreakBefore,
    children: [
      ...(o.bookmark ? [new Bookmark({ id: o.bookmark, children: runs(text, o) })] : runs(text, o)),
    ],
  });
}
const blank = (n = 1, line = 240) => Array.from({ length: n }, () => new Paragraph({ spacing: { after: 0, line }, children: [new TextRun('')] }));
const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

// ---------- tables ----------
const TEXT_WIDTH = 11906 - 1800 - 1440; // A4 minus margins (left 1.25", right 1")
const border = { style: BorderStyle.SINGLE, size: 6, color: '000000' };
const borders = { top: border, bottom: border, left: border, right: border };

function cell(text, { width, bold, align, shade, size = 22, vAlign = VerticalAlign.CENTER, colSpan, noBorders } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    columnSpan: colSpan,
    verticalAlign: vAlign,
    shading: shade ? { type: ShadingType.CLEAR, fill: shade, color: 'auto' } : undefined,
    borders: noBorders ? { top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } } : borders,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({ alignment: align || AlignmentType.LEFT, spacing: { after: 0, line: 276 }, children: runs(text, { bold, size }) })],
  });
}

function dataTable(header, rows) {
  const n = header.length;
  // proportional widths by longest cell per column (min 1100)
  const maxLen = header.map((h, i) => Math.max(h.length, ...rows.map((r) => (r[i] || '').length)));
  const weights = maxLen.map((l) => Math.sqrt(Math.max(l, 6)));
  const sum = weights.reduce((a, b) => a + b, 0);
  let widths = weights.map((w) => Math.max(1300, Math.round((w / sum) * TEXT_WIDTH)));
  const diff = TEXT_WIDTH - widths.reduce((a, b) => a + b, 0);
  widths[widths.indexOf(Math.max(...widths))] += diff;
  const numeric = (s) => /^[০-৯0-9.,%–\-\s]+$/.test(s.trim());
  return new Table({
    width: { size: TEXT_WIDTH, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: header.map((h, i) => cell(h, { width: widths[i], bold: true, align: AlignmentType.CENTER, shade: 'E7E6E6' })) }),
      ...rows.map((r) => new TableRow({ children: r.map((c, i) => cell(c, { width: widths[i], align: numeric(c) ? AlignmentType.CENTER : AlignmentType.LEFT })) })),
    ],
  });
}

// ---------- parse manuscript ----------
const SRC = ['paper-part1.txt', 'paper-part2.txt', 'paper-part3.txt', 'paper-part4.txt']
  .map((f) => fs.readFileSync(path.join(__dirname, f), 'utf8')).join('\n');
const lines = SRC.split('\n');

for (const l of lines) { const m = l.match(/^@@fn\s+([a-z0-9_]+):\s*(.+)$/); if (m) FN_TEXT[m[1]] = m[2].trim(); }

const body = [];
let chapterCount = 0; let mode = 'body'; let i = 0;
const secKey = (title) => { const m = title.match(/^([০-৯]+\.[০-৯]+)/); return m ? m[1] : null; };

while (i < lines.length) {
  const raw = lines[i]; const l = raw.trim(); i += 1;
  if (!l) continue;
  if (l.startsWith('=== FOOTNOTES')) break;
  let m;
  if ((m = l.match(/^=== CHAPTER:\s*(.+)$/))) {
    chapterCount += 1; mode = 'body';
    body.push(P(m[1], { align: AlignmentType.CENTER, bold: true, underline: true, size: 28, after: 240, pageBreakBefore: chapterCount > 1, bookmark: 'ch_' + chapterCount }));
    continue;
  }
  if ((m = l.match(/^=== BIBLIO:\s*(.+)$/))) {
    mode = 'biblio';
    body.push(P(m[1], { align: AlignmentType.CENTER, bold: true, underline: true, size: 28, after: 240, pageBreakBefore: true, bookmark: 'biblio' }));
    continue;
  }
  if ((m = l.match(/^##\s+(.+)$/))) {
    const k = secKey(m[1]);
    body.push(P(m[1], { align: AlignmentType.LEFT, bold: true, size: 26, before: 200, after: 120, keepNext: true, bookmark: k ? 'sec_' + k.replace('.', '_') : undefined }));
    continue;
  }
  if ((m = l.match(/^###\s+(.+)$/))) {
    body.push(P(m[1], { align: AlignmentType.LEFT, bold: true, underline: true, size: 24, before: 120, after: 60, keepNext: true }));
    continue;
  }
  if ((m = l.match(/^\[TABLE\]\s*(.+)$/))) {
    const caption = m[1]; const rows = [];
    let source = '';
    while (i < lines.length) {
      const t = lines[i].trim(); i += 1;
      if (t.startsWith('[/TABLE]')) { source = t.replace('[/TABLE]', '').trim(); break; }
      if (t.startsWith('|')) rows.push(t.slice(1, -1).split('|').map((c) => c.trim()));
    }
    body.push(P(caption, { align: AlignmentType.LEFT, bold: true, size: 24, before: 120, after: 80, keepNext: true }));
    body.push(dataTable(rows[0], rows.slice(1)));
    if (source) body.push(P(source, { align: AlignmentType.LEFT, size: 22, before: 60, after: 160, line: 276 }));
    continue;
  }
  if (mode === 'biblio') {
    body.push(P(l, { align: AlignmentType.BOTH, size: 21, after: 80, line: 276, indent: { left: 567, hanging: 567 } }));
    continue;
  }
  // list-like paragraphs get a hanging indent
  if (/^(\([০-৯]+\)|[০-৯]+[.)])\s/.test(l)) { body.push(P(l, { indent: { left: 567, hanging: 567 } })); continue; }
  body.push(P(l));
}

// ---------- front matter ----------
const F = FRONT;
const C = (text, o = {}) => P(text, { align: AlignmentType.CENTER, after: 0, line: 300, ...o });
const L = (text, o = {}) => P(text, { align: AlignmentType.LEFT, after: 0, line: 300, ...o });

function coverContent() {
  const logo = path.join(__dirname, 'nu-logo.png');
  const left = [
    L('তত্ত্বাবধায়ক', { bold: true, underline: true, size: 28, after: 120 }),
    L(F.supervisor.name, { bold: true, size: 24 }), L(F.supervisor.designation, { size: 24 }), L(F.dept, { size: 24 }), L(F.college + ',', { size: 24 }), L(F.district + '।', { size: 24 }),
  ];
  const right = [
    L('উপস্থাপনায়', { bold: true, underline: true, size: 28, after: 120 }),
    L('নামঃ ' + F.student.name, { bold: true, size: 24 }), L('শ্রেণিঃ ' + F.student.className, { size: 24 }), L('রোল নংঃ ' + F.student.roll, { size: 24 }),
    L('রেজিঃ নংঃ ' + F.student.reg, { size: 24 }), L('শিক্ষাবর্ষঃ ' + F.student.session, { size: 24 }), L(F.dept, { size: 24 }), L(F.college + ',', { size: 24 }), L(F.district + '।', { size: 24 }),
  ];
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  const mid = { style: BorderStyle.SINGLE, size: 8, color: '000000' };
  const half = Math.floor(TEXT_WIDTH / 2);
  const cols = new Table({
    width: { size: TEXT_WIDTH, type: WidthType.DXA }, columnWidths: [half, TEXT_WIDTH - half],
    rows: [new TableRow({ children: [
      new TableCell({ width: { size: half, type: WidthType.DXA }, borders: { top: none, bottom: none, left: none, right: mid }, margins: { left: 600, right: 200, top: 100, bottom: 100 }, children: left }),
      new TableCell({ width: { size: TEXT_WIDTH - half, type: WidthType.DXA }, borders: { top: none, bottom: none, left: mid, right: none }, margins: { left: 500, right: 200, top: 100, bottom: 100 }, children: right }),
    ] })],
  });
  return [
    ...blank(1),
    C('টার্ম পেপার', { bold: true, size: 52, after: 240 }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: [new ImageRun({ type: 'png', data: fs.readFileSync(logo), transformation: { width: 105, height: 105 } })] }),
    C(F.title, { bold: true, size: 30, after: 480, line: 360 }),
    cols,
    ...blank(3),
    new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 8, color: '000000', space: 8 } }, spacing: { after: 80 }, children: runs(F.dept, { size: 24, bold: true }) }),
    C(F.college + ', ' + F.district + '।', { size: 24 }),
    C(F.date, { size: 24 }),
  ];
}

function signature(lines) { return lines.map((t, k) => L(t, { size: 24, bold: k === 0 })); }

function declarationPage() {
  return [
    ...blank(1), C('ঘোষণা পত্র', { bold: true, underline: true, size: 32, after: 360 }),
    P(F.declaration, { line: 360 }),
    ...blank(2),
    ...signature([F.student.name, 'রোল নংঃ ' + F.student.roll, 'রেজিঃ নংঃ ' + F.student.reg, F.dept, F.college + ', ' + F.district + '।', 'তারিখঃ ' + F.dateShort]),
    ...blank(3),
    L('তত্ত্বাবধায়ক কর্তৃক প্রত্যয়িত', { size: 24, bold: true, underline: true, after: 120 }),
    ...signature([F.supervisor.name, F.supervisor.designation, F.dept, F.college + ', ' + F.district + '।']),
  ];
}

function approvalPage() {
  return [
    ...blank(1), C('অনুমোদন পত্র', { bold: true, underline: true, size: 32, after: 360 }),
    P(F.approval, { line: 360 }),
    ...blank(4),
    ...signature(['তত্ত্বাবধায়ক', F.supervisor.name, F.supervisor.designation, F.dept, F.college + ', ' + F.district + '।']),
    ...blank(3),
    ...signature(['বিভাগীয় প্রধান', F.head.name, F.dept, F.college + ', ' + F.district + '।']),
  ];
}

function prefacePage() {
  return [
    ...blank(1), C('মুখবন্ধ', { bold: true, underline: true, size: 32, after: 360 }),
    ...F.preface.map((t) => P(t, { line: 360, after: 160 })),
    ...blank(4),
    L(F.student.name, { size: 24, bold: true }),
  ];
}

function tocPage() {
  const w = [1000, 6266, 1400];
  const rows = [];
  const pageField = (key, roman) => {
    if (roman) return runs(roman, { size: 21 });
    const bm = key === 'গ্রন্থপঞ্জি' ? 'biblio' : 'sec_' + key.replace('.', '_');
    const cached = PAGEMAP[key] != null ? String(PAGEMAP[key]) : '০';
    if (!BIJOY) return runs(cached, { size: 21 });
    const shown = cached.replace(/[০-৯]/g, (d) => '০১২৩৪৫৬৭৮৯'.indexOf(d));
    return [new SimpleField('PAGEREF ' + bm + ' \\h', shown)];
  };
  const tcell = (children, width, { align = AlignmentType.LEFT, colSpan, shade } = {}) => new TableCell({
    width: { size: width, type: WidthType.DXA }, columnSpan: colSpan, borders, verticalAlign: VerticalAlign.CENTER,
    shading: shade ? { type: ShadingType.CLEAR, fill: shade, color: 'auto' } : undefined,
    margins: { top: 15, bottom: 15, left: 100, right: 100 },
    children: [new Paragraph({ alignment: align, spacing: { after: 0, line: 240 }, children })],
  });
  for (const [type, num, title, key] of F.toc) {
    if (type === 'chapter') {
      rows.push(new TableRow({ children: [tcell(runs(title, { bold: true, size: 22 }), TEXT_WIDTH, { align: AlignmentType.CENTER, colSpan: 3, shade: 'F2F2F2' })] }));
    } else if (type === 'front') {
      rows.push(new TableRow({ children: [tcell(runs(title, { bold: true, size: 21 }), w[0] + w[1], { colSpan: 2 }), tcell(pageField(null, key), w[2], { align: AlignmentType.CENTER })] }));
    } else {
      rows.push(new TableRow({ children: [tcell(runs(num, { size: 21 }), w[0], { align: AlignmentType.CENTER }), tcell(runs(title, { size: 21 }), w[1]), tcell(pageField(key), w[2], { align: AlignmentType.CENTER })] }));
    }
  }
  return [
    C('সূচিপত্র', { bold: true, underline: true, size: 30, after: 160 }),
    new Table({ width: { size: TEXT_WIDTH, type: WidthType.DXA }, columnWidths: w, rows }),
  ];
}

// ---------- document ----------
const pageMargins = { top: 1440, bottom: 1440, left: 1800, right: 1440 };
const footerNum = () => new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: { ascii: FONT_BN, hAnsi: FONT_BN, cs: FONT_BN, eastAsia: FONT_BN }, size: 22 })] })] });

const frameBorder = { style: BorderStyle.DOUBLE, size: 12, color: '000000', space: 14 };

const doc = new Document({
  creator: F.student.name,
  title: F.titlePlain,
  styles: { default: { document: { run: { font: { ascii: FONT_BN, hAnsi: FONT_BN, cs: FONT_BN, eastAsia: FONT_BN }, size: 24, sizeComplexScript: 24 } } } },
  footnotes,
  sections: [
    { // cover (page i, no number shown)
      properties: {
        page: {
          margin: pageMargins,
          pageNumbers: { start: 1, formatType: NumberFormat.LOWER_ROMAN },
          borders: { pageBorders: { display: PageBorderDisplay.ALL_PAGES, offsetFrom: PageBorderOffsetFrom.TEXT, zOrder: PageBorderZOrder.FRONT }, pageBorderTop: frameBorder, pageBorderRight: frameBorder, pageBorderBottom: frameBorder, pageBorderLeft: frameBorder },
        },
      },
      children: coverContent(),
    },
    { // inside cover .. TOC (ii–vi)
      properties: { page: { margin: pageMargins, pageNumbers: { formatType: NumberFormat.LOWER_ROMAN } } },
      footers: { default: footerNum() },
      children: [
        ...coverContent(), pageBreak(),
        ...declarationPage(), pageBreak(),
        ...approvalPage(), pageBreak(),
        ...prefacePage(), pageBreak(),
        ...tocPage(),
      ],
    },
    { // body (১ …)
      properties: { page: { margin: pageMargins, pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } } },
      footers: { default: footerNum() },
      children: body,
    },
  ],
});

fs.mkdirSync(path.dirname(OUT), { recursive: true });
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log('wrote', OUT, 'footnotes:', fnId, 'bijoy:', BIJOY); if (unknownFn.size) console.warn('WARNING undefined footnote keys (shown red in the document):', [...unknownFn].join(', ')); });
