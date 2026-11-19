// Export PNG versions of the logo SVGs into brand/png.
const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
const dir = path.join(__dirname, '..'); const out = path.join(dir, 'png'); fs.mkdirSync(out, {recursive:true});
const jobs = [ // [svg, png, width, transparent]
  ['logo.svg','logo.png',2000,true], ['logo-dark.svg','logo-dark.png',2000,true], ['logo-on-green.svg','logo-on-green.png',2000,false],
  ['profile-picture.svg','profile-picture-1080.png',1080,false], ['favicon.svg','favicon-512.png',512,true],
  ['favicon.svg','favicon-180.png',180,true], ['favicon.svg','favicon-32.png',32,true], ['spark.svg','spark.png',512,true]];
(async()=>{ const b=await chromium.launch();
  for (const [s,n,w,transp] of jobs) {
    const svg=fs.readFileSync(path.join(dir,s),'utf8'); const m=svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/); const h=Math.round(w*m[2]/m[1]);
    const p=await b.newPage({viewport:{width:w,height:h}});
    await p.setContent(`<style>html,body{margin:0;background:transparent}svg{width:${w}px;height:${h}px;display:block}</style>${svg}`);
    await p.screenshot({path:path.join(out,n), omitBackground:transp}); await p.close(); console.log(n,`${w}x${h}`);
  } await b.close(); })();
