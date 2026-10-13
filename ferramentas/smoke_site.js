const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('http://localhost:8765/index.html');await p.waitForSelector('.enun');
 await p.keyboard.press('c');await p.waitForSelector('.res');
 await p.keyboard.press('g');await p.keyboard.press('Enter');await p.waitForSelector('.resp');
 await p.keyboard.press('e');await p.keyboard.press('x');await p.waitForSelector('.resp');
 await p.click('#nPainel');await p.waitForSelector('table');
 console.log('linhas painel',await p.locator('tbody tr').count());
 console.log(await p.locator('.top').innerText());
 console.log('erros:',errs.filter(e=>!/fonts|ERR_|net::/.test(e)));
 await b.close();})();
