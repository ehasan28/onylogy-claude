// Compute body page numbers of each TOC entry from a rendered PDF.
// usage: node pagemap.js out/preview.pdf out/pagemap.json
const { execSync } = require('child_process');
const fs = require('fs');
const FRONT = require('./front');

const [pdf, outPath] = process.argv.slice(2);
const text = execSync(`pdftotext -layout "${pdf}" -`, { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
const pages = text.split('\f');

const bn = (n) => String(n).replace(/[0-9]/g, (d) => '০১২৩৪৫৬৭৮৯'[d]);
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

// body starts on the page whose text contains the 1.1 heading with its visarga
let bodyStart = pages.findIndex((p) => /১\.১\s+পটভূমিঃ/.test(p));
if (bodyStart < 0) throw new Error('could not find body start');

const map = {};
for (const [type, num, , key] of FRONT.toc) {
  if (type === 'section') {
    const re = new RegExp('^\\s*' + esc(num) + '\\s+\\S', 'm');
    const idx = pages.findIndex((p, i) => i >= bodyStart && re.test(p));
    if (idx >= 0) map[key] = bn(idx - bodyStart + 1);
  } else if (type === 'biblio') {
    const idx = pages.findIndex((p, i) => i > bodyStart && /^\s*গ্রন্থপঞ্জি\s*$/m.test(p));
    if (idx >= 0) map[key] = bn(idx - bodyStart + 1);
  }
}
map.__bodyStartPdfPage = bodyStart + 1;
map.__totalPdfPages = pages.filter((p) => p.trim()).length;
fs.writeFileSync(outPath, JSON.stringify(map, null, 2));
console.log(map);
