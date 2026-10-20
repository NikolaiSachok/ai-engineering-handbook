// End-to-end check that a deep link lands on its section after the page has settled
// (src/clientModules/hashLanding.ts).
//
// The behaviour it guards (#816): the browser scrolls to `#id` first, then Mermaid renders its
// diagrams client-side and grows the page ABOVE the target, so a reader following a section link
// ended up ~580px short, with scrollY unchanged. Each case opens a section that sits below a
// diagram, waits for every diagram to render, and asserts the heading sits at its scroll margin
// (just under the sticky navbar). The last case asserts the reverse: once the reader scrolls
// away, a later layout change must not pull them back to the target.
//
// Usage:
//   npm run build && npm run serve -- --port 3210 --no-open &
//   BASE_URL=http://localhost:3210 node e2e/deep-link-landing.mjs
//
// Requires Playwright's chromium: `npx playwright install chromium` (or set
// PLAYWRIGHT_CHANNEL=chrome to use an installed Chrome).

import {chromium} from 'playwright';

const BASE = (process.env.BASE_URL ?? 'http://localhost:3210').replace(/\/$/, '');
const SITE = `${BASE}/ai-engineering-handbook`;
const GUARDRAILS = 'rag-agents/part-1-rag/cross-cutting/guardrails/deep-dive';
const TOLERANCE = 4; // px between the heading's top and its scroll margin

const CASES = [
  // [label, path, viewport width]
  ['EN, below a diagram', `/${GUARDRAILS}/#where-pii-gets-caught-and-how-its-masked`, 1280],
  ['RU, same shared id', `/ru/${GUARDRAILS}/#where-pii-gets-caught-and-how-its-masked`, 1280],
  ['SK, phone width', `/sk/${GUARDRAILS}/#where-pii-gets-caught-and-how-its-masked`, 390],
  ['AI SDLC intro', '/ai-sdlc/#the-honest-headline-and-the-honest-method', 1280],
  ['Azure, RU', '/ru/azure-dotnet/part-1-azure-foundations/compute/#choosing-and-tradeoffs', 1280],
];

const browser = await chromium.launch(process.env.PLAYWRIGHT_CHANNEL ? {channel: process.env.PLAYWRIGHT_CHANNEL} : {});
let failures = 0;
const check = (label, ok, detail) => {
  if (!ok) failures++;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${label} — ${detail}`);
};

// Settled = at least `expectedDiagrams` diagrams have rendered their SVG and the page height has
// then held still for ten frames. The server HTML carries no diagram markup at all (Mermaid
// renders client-side only), so a minimum count plus the stability wait is the honest signal.
async function settle(page, expectedDiagrams) {
  await page.waitForLoadState('load');
  await page.waitForFunction(
    (n) => document.querySelectorAll('.docusaurus-mermaid-container svg').length >= n,
    expectedDiagrams,
    {timeout: 15000},
  );
  await page.evaluate(
    () =>
      new Promise((resolve) => {
        let last = -1;
        let stable = 0;
        const tick = () => {
          const h = document.documentElement.scrollHeight;
          stable = h === last ? stable + 1 : 0;
          last = h;
          if (stable >= 10) resolve();
          else requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      }),
  );
}

const probe = (id) => {
  const el = document.getElementById(id);
  if (!el) return null;
  return {
    top: Math.round(el.getBoundingClientRect().top),
    margin: Math.round(parseFloat(getComputedStyle(el).scrollMarginTop) || 0),
    atBottom: Math.ceil(window.scrollY + window.innerHeight) >= document.documentElement.scrollHeight - 1,
    diagrams: document.querySelectorAll('.docusaurus-mermaid-container svg').length,
  };
};

for (const [label, path, width] of CASES) {
  const page = await browser.newPage({viewport: {width, height: 800}});
  const id = path.split('#')[1];
  await page.goto(`${SITE}${path}`, {waitUntil: 'domcontentloaded'});
  await settle(page, 1);
  const r = await page.evaluate(probe, id);
  check(
    `deep link lands on its section: ${label}`,
    !!r && r.diagrams > 0 && (Math.abs(r.top - r.margin) <= TOLERANCE || (r.atBottom && r.top >= r.margin)),
    r ? `top=${r.top} scroll-margin=${r.margin} diagrams=${r.diagrams}` : `#${id} not found`,
  );
  await page.close();
}

// ---- The reader's own scrolling wins: no yank-back after they move ----
{
  const page = await browser.newPage({viewport: {width: 1280, height: 800}});
  const id = 'where-pii-gets-caught-and-how-its-masked';
  await page.goto(`${SITE}/${GUARDRAILS}/#${id}`, {waitUntil: 'domcontentloaded'});
  await settle(page, 1);
  await page.mouse.move(640, 400);
  await page.mouse.wheel(0, -900);
  await page.waitForFunction((id) => document.getElementById(id).getBoundingClientRect().top > 600, id);
  // A late layout change above the reader (a diagram, an image, an embed loading).
  await page.evaluate(() => {
    const spacer = document.createElement('div');
    spacer.style.height = '400px';
    document.querySelector('.theme-doc-markdown').prepend(spacer);
  });
  await settle(page, 1);
  const r = await page.evaluate(probe, id);
  check(
    'after the reader scrolls away, a later layout change does not pull them back',
    !!r && Math.abs(r.top - r.margin) > 100,
    r ? `top=${r.top} scroll-margin=${r.margin}` : `#${id} not found`,
  );
  await page.close();
}

await browser.close();
console.log(failures ? `deep-link-landing: FAIL (${failures})` : 'deep-link-landing: PASS');
process.exit(failures ? 1 : 0);
