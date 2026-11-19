const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
(async()=>{ const dir=path.join(__dirname,'..'); const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:900}});
const img=f=>`data:image/svg+xml;base64,${fs.readFileSync(path.join(dir,f)).toString('base64')}`;
await p.setContent(`<body style="margin:0;font-family:sans-serif;background:#eee">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:20px">
<div style="background:#F5F0E7;padding:50px;display:grid;place-items:center"><img src="${img('logo-horizontal.svg')}" height="90"></div>
<div style="background:#1F3B33;padding:50px;display:grid;place-items:center"><img src="${img('logo-horizontal-dark.svg')}" height="90"></div>
<div style="background:#fff;padding:40px;display:grid;place-items:center"><img src="${img('logo-stacked.svg')}" height="220"></div>
<div style="background:#fff;padding:40px;display:flex;gap:30px;align-items:center;justify-content:center">
<img src="${img('icon-cream.svg')}" height="200" style="border-radius:50%"><img src="${img('icon-forest.svg')}" height="200" style="border-radius:24px"><img src="${img('favicon.svg')}" height="32"><img src="${img('favicon.svg')}" height="16"></div>
</div></body>`);
await p.screenshot({path:process.argv[2],fullPage:true}); await b.close();})();
