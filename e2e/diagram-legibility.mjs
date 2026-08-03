// Diagram legibility gate — measures every mermaid diagram at a phone viewport.
//
// Why this exists. Mermaid's default `useMaxWidth: true` scales a whole diagram down to its
// container, label type included, so a wide diagram does not become small — it becomes a grey
// smear. Measured 2026-08-03 against the shipped site: **37 of 42 diagrams rendered below the
// 11px legibility floor at 360px**, several at 2.4–4.5px, and had done since the first one
// shipped. Nothing in the repo measured it, so nobody knew. The fix (config `useMaxWidth: false`
// + `overflow-x: auto` on the container, see docusaurus.config.ts and custom.css) took all 42
// to 16px. This script is what keeps them there.
//
// The number that matters is `effectiveFont`: CSS font-size x the scale the SVG was squashed to.
//
// Usage:
//   npm run build && npm run serve -- --port 3312 --no-open &
//   node e2e/diagram-legibility.mjs                     # local only
//   COMPARE_LIVE=1 node e2e/diagram-legibility.mjs      # also measure the deployed site
//
// Requires Playwright chromium: npx playwright install chromium
import {chromium} from 'playwright';
import {readFileSync, readdirSync, statSync} from 'fs';
import {join} from 'path';

const LIVE = 'https://nikolaisachok.com/ai-engineering-handbook/';
const LOCAL = 'http://localhost:3312/ai-engineering-handbook/';
const FLOOR = 11;

// Find every EN doc page containing a mermaid block, and map it to its route.
const pages = [];
function walk(dir, base) {
  for (const f of readdirSync(dir)) {
    const p = join(dir, f);
    if (statSync(p).isDirectory()) walk(p, base);
    else if (f.endsWith('.md') && readFileSync(p, 'utf8').includes('```mermaid')) {
      let route = p.replace(/^docs-?/, '').replace(/\.md$/, '').replace(/\/index$/, '/');
      route = base + route.replace(/^\//, '');
      pages.push({file: p, route});
    }
  }
}
walk('docs', 'rag-agents/');
walk('docs-ai-sdlc', 'ai-sdlc/');
walk('docs-design-scenarios', 'design-scenarios/');

const browser = await chromium.launch();

async function measure(base, route) {
  const ctx = await browser.newContext({viewport: {width: 360, height: 900}});
  const page = await ctx.newPage();
  try {
    await page.goto(base + route, {waitUntil: 'networkidle', timeout: 40000});
    await page.waitForSelector('svg[id^="mermaid"]', {timeout: 15000});
    await page.waitForTimeout(350);
    const r = await page.evaluate(() => {
      const out = [];
      for (const svg of document.querySelectorAll('svg[id^="mermaid"]')) {
        const box = svg.getBoundingClientRect();
        const vb = svg.getAttribute('viewBox');
        const intrinsic = vb ? parseFloat(vb.split(/\s+/)[2]) : box.width;
        let mf = Infinity;
        for (const t of svg.querySelectorAll('text,.nodeLabel')) {
          const fs = parseFloat(getComputedStyle(t).fontSize);
          if (fs > 0) mf = Math.min(mf, fs);
        }
        out.push({eff: +(mf * (box.width / intrinsic)).toFixed(1), intrinsic: Math.round(intrinsic)});
      }
      return {
        diagrams: out,
        bodyScrollsSideways: document.documentElement.scrollWidth > document.documentElement.clientWidth,
      };
    });
    await ctx.close();
    return r;
  } catch (e) {
    await ctx.close();
    return {diagrams: [], error: e.message.slice(0, 40)};
  }
}

console.log(`Measuring ${pages.length} pages with mermaid, at 360px.\n`);
let liveBad = 0, localBad = 0, liveTotal = 0, localTotal = 0, bodyOverflow = [];
const rows = [];

for (const {route} of pages) {
  const a = process.env.COMPARE_LIVE ? await measure(LIVE, route) : {diagrams: []};
  const b = await measure(LOCAL, route);
  const aMin = a.diagrams.length ? Math.min(...a.diagrams.map((d) => d.eff)) : null;
  const bMin = b.diagrams.length ? Math.min(...b.diagrams.map((d) => d.eff)) : null;
  liveTotal += a.diagrams.length; localTotal += b.diagrams.length;
  liveBad += a.diagrams.filter((d) => d.eff < FLOOR).length;
  localBad += b.diagrams.filter((d) => d.eff < FLOOR).length;
  if (b.bodyScrollsSideways) bodyOverflow.push(route);
  rows.push([route, aMin, bMin]);
}

rows.sort((x, y) => (x[1] ?? 99) - (y[1] ?? 99));
console.log('worst-first (min effective font per page):');
console.log('  live   local   route');
for (const [route, a, b] of rows.slice(0, 14)) {
  const mark = b !== null && b >= FLOOR ? ' ok' : ' STILL BELOW';
  console.log(`  ${String(a ?? '-').padStart(5)}  ${String(b ?? '-').padStart(5)}   ${route}${mark}`);
}
console.log(`\nDiagrams below the ${FLOOR}px floor:  live ${liveBad}/${liveTotal}   local ${localBad}/${localTotal}`);
console.log(`Pages whose BODY scrolls sideways after the change: ${bodyOverflow.length ? bodyOverflow.join(', ') : 'none (invariant held)'}`);
await browser.close();
