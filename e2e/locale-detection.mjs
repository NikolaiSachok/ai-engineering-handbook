// End-to-end check for the EN-canonical flip + browser-language auto-detection
// (see docusaurus.config.ts `localeDetectionScript`, src/lib/localePreference.ts,
// and the swizzled locale dropdown).
//
// It drives a real headless browser against a *production* build served locally,
// exercising exactly what a first-time visitor hits: the blocking <head> script
// reads navigator.languages, matches it against the configured locales (English
// fallback), and redirects — once — preserving path + hash, then remembers the
// choice in a cookie so it never fights the user again.
//
// Usage:
//   npm run build && npm run serve -- --port 3210 --no-open &
//   BASE_URL=http://localhost:3210 node e2e/locale-detection.mjs
//
// Requires Playwright's chromium: `npx playwright install chromium`.

import {chromium} from 'playwright';

const BASE = (process.env.BASE_URL ?? 'http://localhost:3210').replace(/\/$/, '');
const SITE = `${BASE}/ai-engineering-handbook`;
const LESSON = 'rag-agents/part-3-production/llmops';

const results = [];
function check(name, cond, detail) {
  results.push({name, ok: !!cond, detail});
  console.log(`${cond ? 'PASS' : 'FAIL'}  ${name}  — ${detail}`);
}

const htmlLang = (page) => page.evaluate(() => document.documentElement.lang);

// Navigate and let the (possible) blocking-redirect settle, then report final URL.
async function gotoSettled(page, url) {
  await page.goto(url, {waitUntil: 'load'}).catch(() => {});
  // A redirect via location.replace triggers a second navigation; give it a beat.
  await page.waitForLoadState('load').catch(() => {});
  await page.waitForTimeout(400);
  return page.url();
}

async function switchLocaleTo(page, linkText) {
  const dropdown = page.locator('.navbar__items--right .dropdown').first();
  await dropdown.hover();
  const link = dropdown.locator('a.dropdown__link', {hasText: linkText}).first();
  await link.waitFor({state: 'visible', timeout: 5000});
  await Promise.all([page.waitForNavigation({waitUntil: 'load'}), link.click()]);
  await page.waitForTimeout(300);
}

async function run() {
  const browser = await chromium.launch();

  // ---- 1. Canonical rendering: root = EN, /ru/... = RU ----
  {
    const ctx = await browser.newContext({locale: 'en-US'});
    const page = await ctx.newPage();
    await gotoSettled(page, `${SITE}/`);
    check('root `/` renders EN', (await htmlLang(page)) === 'en', `html lang=${await htmlLang(page)} url=${page.url()}`);
    await gotoSettled(page, `${SITE}/ru/${LESSON}/`);
    check('`/ru/<lesson>` renders RU', (await htmlLang(page)) === 'ru', `html lang=${await htmlLang(page)} url=${page.url()}`);
    await ctx.close();
  }

  // ---- 2. Fresh ru-browser hitting a bare (default) path → redirected to /ru/ ----
  {
    const ctx = await browser.newContext({locale: 'ru-RU'});
    const page = await ctx.newPage();
    const url = await gotoSettled(page, `${SITE}/${LESSON}/`);
    check(
      'fresh ru-browser on default path → auto-redirected to /ru/',
      /\/ru\//.test(url) && (await htmlLang(page)) === 'ru',
      `landed ${url} (lang=${await htmlLang(page)})`,
    );
    await ctx.close();
  }

  // ---- 2b. Fresh de-browser → redirected to /de/, and the LESSON is really German ----
  //
  // The positive counterpart to case 4 below, and the assertion #287 asked for by name:
  // German launched on the RAG course alone (#383), so detection must actually route a German
  // browser to `/de/`. Before the launch this case could not exist — `de` was gated out of the
  // deployed locale list — and case 4 used a `de-DE` fixture to assert the OPPOSITE. Both
  // halves are now right, and they guard each other: if `de` were ever dropped from the served
  // locales, this case fails loudly instead of case 4 quietly starting to pass for the wrong
  // reason.
  //
  // `LESSON` is a RAG-course page on purpose. A German browser on an AI-SDLC path is a
  // different question (that course does not claim `de`), and mixing the two would make a
  // failure ambiguous.
  {
    const ctx = await browser.newContext({locale: 'de-DE'});
    const page = await ctx.newPage();
    const url = await gotoSettled(page, `${SITE}/${LESSON}/`);
    check(
      'fresh de-browser on default path → auto-redirected to /de/ (German RAG is live)',
      /\/de\//.test(url) && (await htmlLang(page)) === 'de',
      `landed ${url} (lang=${await htmlLang(page)})`,
    );
    await ctx.close();
  }

  // ---- 3. Fresh en-browser on root → stays EN (no redirect) ----
  {
    const ctx = await browser.newContext({locale: 'en-US'});
    const page = await ctx.newPage();
    const url = await gotoSettled(page, `${SITE}/${LESSON}/`);
    check('fresh en-browser stays on EN (no /ru/)', !/\/ru\//.test(url), `landed ${url}`);
    await ctx.close();
  }

  // ---- 4. Fresh browser in a language the site does NOT ship → English fallback ----
  //
  // The fixture used to be `de-DE`, asserting `!/\/ru\//`. Both halves were wrong, and both
  // failed in the same direction — towards a vacuous pass:
  //
  //   * German is a locale this site is actively translating, so the day it launches a
  //     `de-DE` browser correctly redirects to `/de/…` — which still contains no `/ru/`, so
  //     the assertion keeps passing while testing the OPPOSITE of what its name claims.
  //   * `!/\/ru\//` only ever ruled out one specific locale, so any other locale prefix
  //     satisfied it. It could not detect a wrong redirect in general.
  //
  // So: use a language the site will not plausibly ship (`ja-JP`), and assert the real
  // invariant POSITIVELY — no locale prefix at all, i.e. English served from the root.
  {
    const ctx = await browser.newContext({locale: 'ja-JP'});
    const page = await ctx.newPage();
    const url = await gotoSettled(page, `${SITE}/${LESSON}/`);
    const localePrefix = url.slice(SITE.length).match(/^\/([a-z]{2})(?:-[A-Za-z]{2,4})?\//);
    check(
      'a language the site does not ship falls back to English (no locale prefix)',
      localePrefix === null,
      `landed ${url}${localePrefix ? ` — unexpected locale prefix /${localePrefix[1]}/` : ''}`,
    );
    await ctx.close();
  }

  // ---- 5. Path + hash preserved across the detection redirect ----
  {
    const ctx = await browser.newContext({locale: 'ru-RU'});
    const page = await ctx.newPage();
    const url = await gotoSettled(page, `${SITE}/${LESSON}/#anchor-probe`);
    check(
      'redirect preserves path + hash',
      /\/ru\//.test(url) && url.endsWith('#anchor-probe') && url.includes(`/${LESSON}/`),
      `landed ${url}`,
    );
    await ctx.close();
  }

  // ---- 6. Cookie persists a manual switch across reloads (never bounced back) ----
  {
    const ctx = await browser.newContext({locale: 'ru-RU'});
    const page = await ctx.newPage();
    // First visit: ru-browser is auto-sent to /ru/.
    const first = await gotoSettled(page, `${SITE}/${LESSON}/`);
    check('cookie test — first visit auto-detects RU', /\/ru\//.test(first), `landed ${first}`);
    // User explicitly switches to English via the navbar dropdown.
    await switchLocaleTo(page, 'English');
    const afterSwitch = page.url();
    check('cookie test — manual switch lands on EN root path', !/\/ru\//.test(afterSwitch) && (await htmlLang(page)) === 'en', `url=${afterSwitch}`);
    // Reload the bare default path: the cookie must keep them on EN despite the
    // ru browser language (without the cookie, detection would bounce to /ru/).
    const afterReload = await gotoSettled(page, `${SITE}/${LESSON}/`);
    check(
      'cookie test — reload stays EN (detection suppressed by cookie)',
      !/\/ru\//.test(afterReload) && (await htmlLang(page)) === 'en',
      `reloaded ${afterReload} (lang=${await htmlLang(page)})`,
    );
    // And no redirect loop: URL is stable, not oscillating.
    await page.waitForTimeout(500);
    check('cookie test — no redirect loop', page.url() === afterReload, `stable at ${page.url()}`);
    await ctx.close();
  }

  await browser.close();

  const failed = results.filter((r) => !r.ok);
  console.log(`\n${results.length - failed.length}/${results.length} checks passed`);
  process.exit(failed.length ? 1 : 0);
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
