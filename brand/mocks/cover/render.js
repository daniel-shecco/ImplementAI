const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1640,height:624},deviceScaleFactor:1});
for (const f of fs.readdirSync(__dirname).filter(f=>f.endsWith('.html'))){await p.goto('file://'+path.join(__dirname,f),{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:path.join(__dirname,f.replace('.html','.png'))});}
await b.close();})();
