// End-to-end check for the "preserve reading position across a language switch"
// feature (see src/lib/localeScrollPosition.ts + the swizzled locale dropdown).
//
// It drives a real headless browser against a *production* build served locally,
// so it exercises exactly what a reader hits: open a long lesson, scroll into a
// mid/late section, switch locale via the navbar dropdown, and assert the new
// page lands in the SAME section — named by its heading id, which every locale
// shares (#813) — not at the top.
//
// The guardrails deep dive covers the two hard shapes (#818): it has Mermaid
// diagrams above the restored section, which render after the restore and grow
// the page, and its Russian side subdivides some H2s into H3s English lacks.
// One switch runs on a 10x-throttled CPU, where a position re-applied on timers
// landed a section or more early.
//
// Usage:
//   npm run build && npm run serve -- --port 3210 --no-open &
//   BASE_URL=http://localhost:3210 node e2e/locale-scroll-position.mjs
//
// Requires Playwright's chromium: `npx playwright install chromium`.

import {chromium} from 'playwright';

const BASE = (process.env.BASE_URL ?? 'http://localhost:3210').replace(/\/$/, '');
const SITE = `${BASE}/ai-engineering-handbook`;
const LLMOPS = 'rag-agents/part-3-production/llmops';
const GUARDRAILS = 'rag-agents/part-1-rag/cross-cutting/guardrails/deep-dive';

// "Which section am I in", evaluated in the page: the innermost h2/h3/h4 whose top has
// scrolled above the line just under the sticky navbar, and the H2 that contains it.
function pageSectionProbe() {
  const nav = document.querySelector('.navbar')?.offsetHeight ?? 60;
  const headings = Array.from(
    document.querySelectorAll(
      '.theme-doc-markdown h2[id], .theme-doc-markdown h3[id], .theme-doc-markdown h4[id]',
    ),
  );
  let current = null;
  let h2 = null;
  for (const h of headings) {
    if (h.getBoundingClientRect().top > nav + 1) break;
    current = h;
    if (h.tagName === 'H2') h2 = h;
  }
  return {id: current?.id ?? null, h2: h2?.id ?? null, scrollY: Math.round(window.scrollY)};
}

// Scroll so the reader is ~40px INTO the section headed by `id` (its heading has
// just passed above the navbar line), making that the unambiguous current section.
function scrollIntoSection(id) {
  const nav = document.querySelector('.navbar')?.offsetHeight ?? 60;
  const el = document.getElementById(id);
  window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - nav + 40);
}

async function switchLocaleTo(page, linkText) {
  // The only navbar dropdown is the locale switcher; hover to open, then click.
  const dropdown = page.locator('.navbar__items--right .dropdown').first();
  await dropdown.hover();
  const link = dropdown.locator('a.dropdown__link', {hasText: linkText}).first();
  await link.waitFor({state: 'visible', timeout: 5000});
  // A real pointer click at the link, not `link.click()`: Playwright scrolls its target into view
  // first, which moves the page under the reader before the position is captured (by 100-300px on
  // a throttled CPU). A reader's click never scrolls.
  const box = await link.boundingBox();
  await Promise.all([
    page.waitForNavigation({waitUntil: 'load'}),
    page.mouse.click(box.x + box.width / 2, box.y + box.height / 2),
  ]);
}

// Settled = the network is idle and the page height has then held still for ten frames, so
// every diagram has rendered and the pin has had its last layout change to answer.
async function settle(page) {
  await page.waitForLoadState('networkidle').catch(() => {});
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

// Open `from`, read into the section `id`, switch with `linkText`, and probe both sides.
async function switchFrom(page, from, id, linkText, {throttle = 0} = {}) {
  await page.goto(`${SITE}${from}`, {waitUntil: 'load'});
  await settle(page);
  await page.evaluate(scrollIntoSection, id);
  await page.waitForTimeout(150);
  const before = await page.evaluate(pageSectionProbe);
  const cdp = throttle ? await page.context().newCDPSession(page) : null;
  if (cdp) await cdp.send('Emulation.setCPUThrottlingRate', {rate: throttle});
  await switchLocaleTo(page, linkText);
  await settle(page);
  if (cdp) await cdp.send('Emulation.setCPUThrottlingRate', {rate: 1});
  const after = await page.evaluate(pageSectionProbe);
  const diagramsAbove = await page.evaluate((target) => {
    const el = document.getElementById(target);
    return Array.from(document.querySelectorAll('.docusaurus-mermaid-container svg')).filter(
      (svg) => el && svg.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING,
    ).length;
  }, after.h2);
  return {before, after, diagramsAbove, url: page.url()};
}

const results = [];
function check(name, cond, detail) {
  results.push({name, ok: !!cond, detail});
  console.log(`${cond ? 'PASS' : 'FAIL'}  ${name}  — ${detail}`);
}

const describe = ({before, after}) =>
  `was in "${before.id}" → is in "${after.id}" (H2 "${after.h2}", scrollY=${after.scrollY})`;

async function run() {
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport: {width: 1280, height: 820}});

  // ---- Same headings on both sides, from a late and an earlier section ----
  for (const [label, from, id, linkText] of [
    ['RU→EN', `/ru/${LLMOPS}/`, 'the-token-diet', 'English'],
    ['EN→RU', `/${LLMOPS}/`, 'monitoring-in-production', 'Русский'],
  ]) {
    const r = await switchFrom(page, from, id, linkText);
    check(`${label} lands in the same section`, r.before.id === id && r.after.id === id, describe(r));
  }

  // ---- A diagram above the restored section ----
  // The diagrams render after the restore and push the section down; the reader must still be in it.
  for (const [label, throttle] of [
    ['EN→RU below a diagram', 0],
    ['EN→RU below a diagram, 10x CPU throttle', 10],
  ]) {
    const r = await switchFrom(page, `/${GUARDRAILS}/`, 'where-pii-gets-caught-and-how-its-masked', 'Русский', {
      throttle,
    });
    check(
      `${label} lands in the same section`,
      r.after.id === r.before.id && r.diagramsAbove > 0,
      `${describe(r)}, ${r.diagramsAbove} diagram(s) above it`,
    );
  }

  // ---- A shared section on a page one locale subdivides ----
  // Russian splits the H2s of this page into H3s English lacks; this shared H2 used to be missed
  // by the count-based mapping, which fell back to a whole-page fraction.
  {
    const id = 'the-attack-catalogue-and-the-defence-trained-into-the-model';
    const r = await switchFrom(page, `/ru/${GUARDRAILS}/`, id, 'English');
    check('RU→EN on a subdivided page lands in the same section', r.after.id === id, describe(r));
  }

  // ---- A section only one locale has: land inside its parent H2 ----
  {
    const r = await switchFrom(page, `/ru/${GUARDRAILS}/`, 'the-precision-recall-tradeoff', 'English');
    check(
      'RU-only subsection → EN lands inside its parent H2 (not top)',
      r.before.h2 === 'where-pii-gets-caught-and-how-its-masked' && r.after.h2 === r.before.h2,
      `RU in "${r.before.id}" under "${r.before.h2}" → EN in "${r.after.id}" under "${r.after.h2}"`,
    );
  }

  // ---- The section hash survives the switch, and the reader's position still wins ----
  {
    const hash = '#how-spotlighting-marks-untrusted-text';
    const r = await switchFrom(page, `/${GUARDRAILS}/${hash}`, 'three-points-where-it-sits', 'Русский');
    check(
      'a #hash is kept across locales, the position restore overrides it',
      new URL(r.url).hash === hash && r.after.id === 'three-points-where-it-sits',
      `url=${r.url}, ${describe(r)}`,
    );
  }

  // ---- Regression: a plain load (no locale switch) must NOT teleport ----
  await page.goto(`${SITE}/${LLMOPS}/`, {waitUntil: 'load'});
  await settle(page);
  const plainLoad = await page.evaluate(pageSectionProbe);
  check('plain page load stays at the top (no teleport)', plainLoad.scrollY < 50, `scrollY=${plainLoad.scrollY}`);

  // ---- Regression: in-page TOC anchor navigation still works ----
  await page.goto(`${SITE}/${LLMOPS}/`, {waitUntil: 'load'});
  await settle(page);
  const tocLink = page.locator('.table-of-contents__link').nth(4);
  const tocHref = await tocLink.getAttribute('href');
  await tocLink.click();
  await page.waitForTimeout(400);
  const afterToc = await page.evaluate(() => ({
    scrollY: Math.round(window.scrollY),
    hash: window.location.hash,
  }));
  check(
    'in-page TOC anchor link still scrolls (not regressed)',
    afterToc.scrollY > 100 && !!afterToc.hash && tocHref?.endsWith(afterToc.hash),
    `clicked "${tocHref}" → hash=${afterToc.hash} scrollY=${afterToc.scrollY}`,
  );

  await browser.close();

  const failed = results.filter((r) => !r.ok);
  console.log(`\n${results.length - failed.length}/${results.length} checks passed`);
  process.exit(failed.length ? 1 : 0);
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
