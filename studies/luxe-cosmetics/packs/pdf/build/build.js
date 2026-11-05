const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [html, pdf] of process.argv.slice(2).map(a => a.split('='))) {
    const p = await b.newPage();
    await p.goto('file://' + html, { waitUntil: 'load', timeout: 300000 });
    await p.pdf({ path: pdf, format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: '<div style="font-size:8pt;width:100%;text-align:center;color:#888"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
      margin: { top: '16mm', bottom: '18mm', left: '15mm', right: '15mm' }, timeout: 0 });
    console.log(pdf); await p.close();
  }
  await b.close();
})();
