// Phone-size screenshots of the pilot form: the whole form, and split into three parts, per language.
const { chromium } = require('playwright'); const path = require('path');
const R = path.resolve(__dirname, '../..');
(async () => {
  const b = await chromium.launch();
  for (const [f, tag] of [['pilot.html', 'en'], ['de/pilot.html', 'de']]) {
    const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3 });
    await p.goto('file://' + path.join(R, f), { waitUntil: 'networkidle' });
    await p.evaluate(() => { document.querySelectorAll('.reveal').forEach(e => e.classList.add('in')); document.querySelector('.sticky-cta')?.remove(); });
    await p.waitForTimeout(1500);
    const parts = await p.evaluate(() => {
      const form = document.querySelector('#apply form'), fs = form.querySelectorAll('fieldset');
      const top = el => el.getBoundingClientRect().top + scrollY;
      const fr = form.getBoundingClientRect(), x = fr.left, w = fr.width, end = top(form) + fr.height;
      const cuts = [top(form), top(fs[1]) - 8, top(fs[2]) - 8, end];
      return [0, 1, 2].map(i => ({ x, y: cuts[i], width: w, height: cuts[i + 1] - cuts[i] }));
    });
    for (const [i, clip] of parts.entries())
      await p.screenshot({ path: path.join(__dirname, 'form-phone', `${tag}-${i + 1}.png`), clip, fullPage: true });
    await p.locator('#apply form').screenshot({ path: path.join(__dirname, 'form-phone', `${tag}-full.png`) });
  }
  await b.close();
})();
