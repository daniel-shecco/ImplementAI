// Render every ad HTML in ./html to a PNG in ../images at its exact pixel size.
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  // Optional arguments: HTML folder and output folder (defaults: ./html and ../images).
  const dir = process.argv[2] || path.join(__dirname, 'html'); const out = process.argv[3] || path.join(__dirname, '..', 'images');
  const jobs = JSON.parse(fs.readFileSync(path.join(dir, 'jobs.json')));
  const b = await chromium.launch();
  for (const j of jobs) {
    const p = await b.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.join(dir, j.name + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => { const f = document.querySelector('.frame'); return f.scrollHeight > f.clientHeight + 1 || [...document.querySelectorAll('h1,.sub,q,.cta,.langs')].some(e => e.getBoundingClientRect().right > innerWidth); });
    await p.screenshot({ path: path.join(out, j.name + '.png') });
    console.log(j.name, over ? 'OVERFLOW' : 'ok');
    await p.close();
  }
  await b.close();
})();
