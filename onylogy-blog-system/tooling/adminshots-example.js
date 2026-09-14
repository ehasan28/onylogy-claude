// One-time Novamira admin login + admin screenshots (headed Chrome for Testing off-screen, like pwshot.js)
const { chromium } = require('/Users/ehasanulhaque/Claude Playground/onylogy-squeeze-wp/node_modules/playwright-core');
const os = require('os'); const fs = require('fs');
(async () => {
  const aal = JSON.parse(fs.readFileSync(process.argv[2])).data;
  const out = process.argv[3];
  const r = await fetch(aal.exchange_url, { method: 'POST', headers: { [aal.token_header]: aal.access_token, [aal.nonce_header]: aal.access_nonce } });
  const j = await r.json(); const login = j.login_url || j.url || (j.data && (j.data.login_url || j.data.url));
  if (!login) { console.error('exchange failed', JSON.stringify(j).slice(0,400)); process.exit(1); }
  const exe = os.homedir() + '/Library/Caches/ms-playwright/chromium-1223/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing';
  const browser = await chromium.launch({ executablePath: exe, headless: false, args: ['--window-position=-3000,0'] });
  const ctx = await browser.newContext({ viewport: { width: 1360, height: 900 }, deviceScaleFactor: 1, locale: 'en-US' });
  const page = await ctx.newPage();
  await page.goto(login, { waitUntil: 'domcontentloaded', timeout: 60000 }); await page.waitForTimeout(5000);
  console.log('after login:', page.url(), '|', await page.title());
  const shot = async (name) => { await page.screenshot({ path: `${out}/${name}.png`, fullPage: false }); console.log('saved', name); };
  // 1. settings screen
  if (!page.url().includes('kadence-blocks')) await page.goto('https://onylogy.com/wp-admin/admin.php?page=kadence-blocks', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(3000); await shot('settings-screen');
  // 2. customizer colors
  await page.goto('https://onylogy.com/wp-admin/customize.php?autofocus[section]=kadence_customizer_general_colors', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(12000); await shot('customizer-colors');
  // 3. customizer typography
  await page.goto('https://onylogy.com/wp-admin/customize.php?autofocus[section]=kadence_customizer_general_typography', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(12000); await shot('customizer-typography');
  // 4. block editor: Home page, select first Advanced Text block, open settings sidebar
  await page.goto('https://onylogy.com/wp-admin/post.php?post=340&action=edit', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(12000);
  try { await page.keyboard.press('Escape'); } catch (e) {}
  try { const wel = page.locator('button:has-text("Close")').first(); if (await wel.isVisible({timeout:1500})) await wel.click(); } catch (e) {}
  const frames = page.frames(); let target = page;
  for (const f of frames) { if (await f.locator('.wp-block-kadence-advancedheading').count() > 0) { target = f; break; } }
  const blk = target.locator('.wp-block-kadence-advancedheading').first();
  try { await blk.scrollIntoViewIfNeeded(); await blk.click({ timeout: 5000 }); } catch (e) { console.error('block click:', e.message); }
  await page.waitForTimeout(2500);
  try { const sb = page.locator('button[aria-label="Settings"]'); if (!(await sb.getAttribute('aria-pressed')) || (await sb.getAttribute('aria-pressed')) === 'false') await sb.click(); } catch (e) {}
  await page.waitForTimeout(2500); await shot('advanced-text-sidebar');
  await browser.close();
})();
