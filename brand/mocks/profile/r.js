const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();
for (const n of ['A-cream','B-green','C-white']){const p=await b.newPage({viewport:{width:1080,height:1080}});await p.goto('file://'+path.join(__dirname,n+'.html'));await p.screenshot({path:path.join(__dirname,n+'.png')});await p.close();}
const p=await b.newPage({viewport:{width:1220,height:520},deviceScaleFactor:2});await p.goto('file://'+path.join(__dirname,'compare.html'));await p.waitForTimeout(300);await p.screenshot({path:path.join(__dirname,'compare.png'),fullPage:true});
await b.close();})();
