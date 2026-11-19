const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1500, height: 900 }, deviceScaleFactor: 1.6 });
await p.goto('file://' + path.join(__dirname, 'ads-compare.html'), { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
console.log(await p.evaluate(()=>document.body.scrollHeight));
await p.screenshot({ path: path.join(__dirname, 'ads-register-interest.png'), fullPage: true }); await b.close(); })();
