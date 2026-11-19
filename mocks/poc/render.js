const { chromium } = require('playwright'); const path = require('path');
const R = path.resolve(__dirname, '../..');
(async () => {
  const b = await chromium.launch();
  async function shots(file, pre) {
    const p = await b.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 2 });
    await p.goto('file://' + file, { waitUntil: 'networkidle' });
    await p.evaluate(() => { document.querySelectorAll('.reveal').forEach(e => e.classList.add('in')); document.querySelector('.sticky-cta')?.remove(); return document.fonts.ready; });
    await p.waitForTimeout(1200);
    const clip = async (sel, name, extraTop = 0) => {
      const box = await p.evaluate(([s, t]) => { const e = document.querySelector(s); const r = e.getBoundingClientRect(); return { x: 0, y: r.top + scrollY - t, width: 1280, height: r.height + t }; }, [sel, extraTop]);
      await p.screenshot({ path: path.join(__dirname, `${pre}-${name}.png`), clip: box, fullPage: true });
    };
    return { p, clip };
  }
  for (const [file, pre] of [[R + '/pilot.html', 'cur'], [__dirname + '/pilot-interest.html', 'new']]) {
    const { p, clip } = await shots(file, pre);
    const hdr = await p.evaluate(() => document.querySelector('.lp-hero').getBoundingClientRect().top + scrollY);
    await clip('.lp-hero', 'pilot-hero', hdr);
    await clip('#apply', 'pilot-form');
    await p.evaluate(() => { document.querySelectorAll('section')[4].id = 'sel'; document.querySelector('.faq-wrap').closest('section').id = 'faqsec'; });
    await clip('#sel', 'pilot-faq'); 
    await p.close();
  }
  for (const [file, pre] of [[R + '/index.html', 'cur'], [__dirname + '/index-anon.html', 'new']]) {
    const { p, clip } = await shots(file, pre);
    const hdr = await p.evaluate(() => document.querySelector('.hero').getBoundingClientRect().top + scrollY);
    await clip('.hero', 'index-top', hdr);
    await clip('#team', 'index-team');
    await p.close();
  }
  const c = await b.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1.75 });
  await c.goto('file://' + __dirname + '/compare.html', { waitUntil: 'networkidle' });
  await c.evaluate(() => document.fonts.ready);
  await c.screenshot({ path: path.join(__dirname, 'interest-test.png'), fullPage: true });
  console.log(await c.evaluate(() => document.body.scrollHeight));
  await b.close();
})();
