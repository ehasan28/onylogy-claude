// Public section screenshots: find the outermost Kadence row containing an H2/H1 with given text, screenshot it.
const { chromium } = require('/Users/ehasanulhaque/Claude Playground/onylogy-squeeze-wp/node_modules/playwright-core');
const os = require('os');
const jobs = JSON.parse(process.argv[2]); const out = process.argv[3];
(async () => {
  const exe = os.homedir() + '/Library/Caches/ms-playwright/chromium-1223/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing';
  const browser = await chromium.launch({ executablePath: exe, headless: false, args: ['--window-position=-3000,0'] });
  const ctx = await browser.newContext({ viewport: { width: 1360, height: 900 }, deviceScaleFactor: 1, locale: 'en-US' });
  const page = await ctx.newPage();
  let cur = '';
  for (const j of jobs) {
    if (j.url !== cur) { await page.goto(j.url, { waitUntil: j.wait || 'networkidle', timeout: 60000 }); cur = j.url; await page.waitForTimeout(j.pause || 1500); if (j.dismiss) { try { await page.locator(j.dismiss).first().click({ timeout: 3000 }); await page.waitForTimeout(800); } catch (e) {} } }
    let el;
    if (j.selector) el = page.locator(j.selector).first();
    else {
      const h = page.locator(`${j.tag || 'h2'}:has-text("${j.text}")`).first();
      el = h.locator(`xpath=ancestor::*[contains(@class,"${j.anc || 'wp-block-kadence-rowlayout'}")][${j.level || 'last()'}]`);
    }
    try {
      await el.scrollIntoViewIfNeeded(); await page.waitForTimeout(1200);
      // force lazy images inside to load
      await el.evaluate(e => { e.querySelectorAll('img[data-lazyloaded], img[loading="lazy"]').forEach(i => { i.loading = 'eager'; if (i.dataset.src) i.src = i.dataset.src; }); });
      await page.waitForTimeout(1500);
      await el.screenshot({ path: `${out}/${j.name}.png` }); console.log('saved', j.name);
    } catch (e) { console.error('FAIL', j.name, e.message.split('\n')[0]); }
  }
  await browser.close();
})();
