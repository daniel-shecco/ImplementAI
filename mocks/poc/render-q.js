const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1500, height: 900 }, deviceScaleFactor: 2 });
await p.goto('file://' + path.join(__dirname, 'question-options.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
await p.screenshot({ path: path.join(__dirname, 'question-options.png'), fullPage: true }); await b.close(); })();
