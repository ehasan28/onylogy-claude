// Headed (non-headless) Chromium via playwright-core: passes bot checks the headless shell fails.
// usage: node pwshot.js URL OUT.png [height] [waitMs] [clickSelectorToDismiss]
const { chromium } = require('playwright-core');
const os = require('os');
(async () => {
  const [url, out, h = '800', wait = '6000', dismiss] = process.argv.slice(2);
  const exe = os.homedir() + '/Library/Caches/ms-playwright/chromium-1223/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing';
  const browser = await chromium.launch({ executablePath: exe, headless: false, args: ['--window-position=-3000,0'] });
  const ctx = await browser.newContext({ viewport: { width: 1360, height: parseInt(h) }, deviceScaleFactor: 1, locale: 'en-US' });
  const page = await ctx.newPage();
  try { await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 }); } catch (e) { console.error('goto:', e.message); }
  await page.waitForTimeout(parseInt(wait));
  if (dismiss) { for (const sel of dismiss.split('|')) { try { await page.locator(sel).first().click({ timeout: 2000 }); await page.waitForTimeout(800); } catch (e) {} } }
  try { await page.keyboard.press('Escape'); await page.mouse.move(5, 790); await page.waitForTimeout(600); } catch (e) {}
  await page.screenshot({ path: out, fullPage: false });
  console.log('saved', out, await page.title());
  await browser.close();
})();
