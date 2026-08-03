// Diagram legibility & fit gate — every mermaid diagram, phone and desktop.
//
// Why this exists. Mermaid's default `useMaxWidth: true` scaled whole diagrams down to their
// container, label type included, so a wide diagram did not become small — it became a grey
// smear. Measured 2026-08-03 against the shipped site: **37 of 42 diagrams rendered below the
// 11px legibility floor at 360px**, several at 2.4px, and had done since the first one shipped.
// Nothing measured it, so nobody knew.
//
// TWO things are asserted, because passing one and failing the other still ships a bad page:
//   1. LEGIBILITY — effective label size (CSS font-size x the scale the SVG was squashed to)
//      must clear 11px. A diagram can be present and unreadable.
//   2. FIT — how many diagrams need horizontal scrolling. A legible diagram that opens with
//      its first node off-screen is still awkward; that was a real defect (#438), found by
//      screenshot after this gate's first version passed it.
//
// Only (1) FAILS the run. Fit is REPORTED against a baseline, not asserted, because most of
// these diagrams are genuinely wider than a 360px column and no layout setting changes that —
// a responsive LR/TB switcher was built and measured and moved the number from 37 to 33, which
// did not justify overriding a core theme component. Driving the count down is authoring work:
// simpler diagrams, shorter labels, fewer parallel branches. The baseline exists so that work
// shows up as progress and a REGRESSION still fails the gate.
//
// Usage:
//   npm run build && npm run serve -- --port 3312 --no-open &
//   node e2e/diagram-legibility.mjs
//
// Requires Playwright chromium: npx playwright install chromium
import {chromium} from 'playwright';
import {readFileSync, readdirSync, statSync} from 'fs';
import {join} from 'path';

const LOCAL = process.env.BASE_URL
  ? `${process.env.BASE_URL.replace(/\/$/, '')}/ai-engineering-handbook/`
  : 'http://localhost:3313/ai-engineering-handbook/';
const FLOOR = 11;
// Measured 2026-08-03 over all four locales (336 measurements). The authoring pass took it from
// 267 to 147 — long chains re-authored as `TB`, fan-outs stacked inside a `direction LR` subgraph,
// sub-labels moved into the prose that already carried them. Lower it as diagrams get simplified;
// NEVER raise it to make a red run green.
const SCROLL_BASELINE = 147;
const WIDTHS = [[360, 'phone'], [1440, 'desktop']];

const pages = [];
function walk(dir, base, strip) {
  for (const f of readdirSync(dir)) {
    const p = join(dir, f);
    if (statSync(p).isDirectory()) walk(p, base, strip);
    else if (f.endsWith('.md') && readFileSync(p, 'utf8').includes('```mermaid')) {
      const route = p.slice(strip.length).replace(/\.md$/, '').replace(/\/index$/, '/');
      pages.push(base + route);
    }
  }
}
// Every locale, not just English. The locale renders are SEPARATE FILES that drift from the
// English source — measured 2026-08-03, a Russian diagram was 2 062px while its English
// counterpart was 635px, because the two had been authored into different shapes. A gate that
// reads only `docs/` cannot see that, and three of the four readerships were unmeasured.
const COURSES = [
  ['docs', 'rag-agents/', 'docusaurus-plugin-content-docs'],
  ['docs-ai-sdlc', 'ai-sdlc/', 'docusaurus-plugin-content-docs-ai-sdlc'],
  ['docs-design-scenarios', 'design-scenarios/', 'docusaurus-plugin-content-docs-design-scenarios'],
];
const LOCALES = ['', 'ru/', 'sk/', 'de/'];
for (const [dir, base, plugin] of COURSES) {
  for (const loc of LOCALES) {
    const root = loc ? `i18n/${loc.slice(0, -1)}/${plugin}/current` : dir;
    try {
      statSync(root);
    } catch {
      continue; // a course need not be translated into every locale
    }
    walk(root, loc + base, root + '/');
  }
}

const browser = await chromium.launch();

async function measure(route, vw) {
  const ctx = await browser.newContext({viewport: {width: vw, height: 900}});
  const page = await ctx.newPage();
  try {
    await page.goto(LOCAL + route, {waitUntil: 'networkidle', timeout: 45000});
    await page.waitForSelector('svg[id^="mermaid"]', {timeout: 15000});
    // The responsive picker settles after its first container measurement.
    await page.waitForTimeout(500);
    const r = await page.evaluate(() => {
      const out = [];
      for (const svg of document.querySelectorAll('svg[id^="mermaid"]')) {
        const box = svg.getBoundingClientRect();
        const vb = svg.getAttribute('viewBox');
        const intrinsic = vb ? parseFloat(vb.split(/\s+/)[2]) : box.width;
        const cont = svg.closest('.docusaurus-mermaid-container');
        let mf = Infinity;
        for (const t of svg.querySelectorAll('text,.nodeLabel')) {
          const fs = parseFloat(getComputedStyle(t).fontSize);
          if (fs > 0) mf = Math.min(mf, fs);
        }
        out.push({
          eff: mf === Infinity ? null : +(mf * (box.width / intrinsic)).toFixed(1),
          scrolls: cont ? cont.scrollWidth > cont.clientWidth + 1 : false,
        });
      }
      return {
        diagrams: out,
        bodyScrollsSideways:
          document.documentElement.scrollWidth > document.documentElement.clientWidth,
      };
    });
    await ctx.close();
    return r;
  } catch (e) {
    await ctx.close();
    return {diagrams: [], error: e.message.slice(0, 50)};
  }
}

console.log(`Measuring ${pages.length} pages, at ${WIDTHS.map(([w]) => w + 'px').join(' and ')}.\n`);

let illegible = 0;
let scrolling = 0;
let total = 0;
const bodyBad = [];
const rows = [];

for (const route of pages) {
  let worst = 99;
  let anyScroll = false;
  for (const [vw] of WIDTHS) {
    const r = await measure(route, vw);
    total += r.diagrams.length;
    for (const d of r.diagrams) {
      if (d.eff !== null && d.eff < FLOOR) illegible++;
      if (d.eff !== null) worst = Math.min(worst, d.eff);
      if (d.scrolls) {
        scrolling++;
        anyScroll = true;
      }
    }
    if (r.bodyScrollsSideways) bodyBad.push(`${route} @${vw}px`);
  }
  rows.push([route, worst === 99 ? null : worst, anyScroll]);
}

rows.sort((a, b) => Number(b[2]) - Number(a[2]) || (a[1] ?? 99) - (b[1] ?? 99));
console.log('  font  scroll  route');
for (const [route, font, scroll] of rows.slice(0, 14)) {
  console.log(`  ${String(font ?? '-').padStart(4)}  ${scroll ? 'YES   ' : 'no    '}  ${route}`);
}

console.log(`\nBelow the ${FLOOR}px floor:      ${illegible}/${total}`);
console.log(`Needing horizontal scroll: ${scrolling}/${total}`);
console.log(`Page body scrolls sideways: ${bodyBad.length ? bodyBad.join(', ') : 'nowhere (invariant held)'}`);

await browser.close();
if (scrolling > SCROLL_BASELINE) {
  console.log(`\nREGRESSION — horizontal-scroll count rose above the ${SCROLL_BASELINE} baseline.`);
} else if (scrolling < SCROLL_BASELINE) {
  console.log(`\nIMPROVED — ${SCROLL_BASELINE - scrolling} fewer than baseline. Lower SCROLL_BASELINE to ${scrolling}.`);
}
const ok = illegible === 0 && bodyBad.length === 0 && scrolling <= SCROLL_BASELINE;
console.log(ok ? '\nPASS — legibility floor held, fit within baseline' : '\nFAIL');
process.exit(ok ? 0 : 1);
