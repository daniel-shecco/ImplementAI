const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();
for (const [f,n] of [[path.join(__dirname,'pilot-short.html'),'new'],['/home/user/ImplementAI/pilot.html','current']]){
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:3});await p.goto('file://'+f,{waitUntil:'networkidle'});
await p.evaluate(()=>{document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'));document.querySelector('.sticky-cta')?.remove();});await p.waitForTimeout(1500);
await p.locator('#apply form').screenshot({path:path.join(__dirname,`form-${n}.png`)});
console.log(n, await p.evaluate(()=>Math.round(document.querySelector('#apply form').getBoundingClientRect().height)));await p.close();}
await b.close();})();
