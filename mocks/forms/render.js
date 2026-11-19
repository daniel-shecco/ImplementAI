const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const [w, tag] of [[1280, 'desktop'], [390, 'phone']]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.resolve(__dirname, '../../pilot.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => { document.querySelectorAll('.reveal').forEach(e => e.classList.add('in')); document.querySelector('.sticky-cta')?.remove(); return document.fonts.ready; });
    await p.waitForTimeout(1200);
    await p.locator('#apply form').screenshot({ path: path.join(__dirname, `site-${tag}.png`) });
    const g = await b.newPage({ viewport: { width: w === 1280 ? 760 : 390, height: 900 }, deviceScaleFactor: 2 });
    await g.goto('file://' + path.join(__dirname, 'gform.html'), { waitUntil: 'networkidle' });
    await g.evaluate(() => document.fonts.ready);
    await g.screenshot({ path: path.join(__dirname, `gform-${tag}.png`), fullPage: true });
  }
  const c = await b.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 2 });
  await c.goto('file://' + path.join(__dirname, 'compare.html'), { waitUntil: 'networkidle' });
  await c.evaluate(() => document.fonts.ready);
  await c.screenshot({ path: path.join(__dirname, 'form-options.png'), fullPage: true });
  await b.close();
})();
