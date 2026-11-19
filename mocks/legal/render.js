const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const f of ['imprint', 'privacy', 'impressum', 'datenschutz']) {
    const p = await b.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.join(__dirname, f + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(__dirname, f + '.png'), fullPage: true });
  }
  const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  await m.goto('file://' + path.join(__dirname, 'privacy.html'), { waitUntil: 'networkidle' });
  console.log('phone overflow', await m.evaluate(() => document.documentElement.scrollWidth));
  await b.close();
})();
