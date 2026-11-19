const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1672,height:900},deviceScaleFactor:1});
await p.goto('file://'+path.join(__dirname,process.argv[2]||'logo-options.html'),{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:path.join(__dirname,(process.argv[3]||'logo-options.png')),fullPage:true}); await b.close(); })();
