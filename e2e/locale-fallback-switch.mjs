// End-to-end check of the out-of-scope locale fallback (localeDetectionScript in
// docusaurus.config.ts + src/clientModules/localeRouting.ts).
//
// The behaviour it guards: a reader in German who opens a course that has no German (Azure &
// .NET is English + Russian) is moved to the English page instead of German chrome over
// English content; when they come back to a course that has German, they are moved back.
// The preference cookie is never rewritten by this, and an explicit choice ends it.
//
// Usage:
//   npm run build && npm run serve -- --port 3210 --no-open &
//   BASE_URL=http://localhost:3210 node e2e/locale-fallback-switch.mjs
//
// Requires Playwright's chromium: `npx playwright install chromium` (or set
// PLAYWRIGHT_CHANNEL=chrome to use an installed Chrome).

import {chromium} from 'playwright';

const BASE = (process.env.BASE_URL ?? 'http://localhost:3210').replace(/\/$/, '');
const SITE = `${BASE}/ai-engineering-handbook`;
const AZURE_LESSON = 'azure-dotnet/part-1-azure-foundations/entra-id';

const browser = await chromium.launch(process.env.PLAYWRIGHT_CHANNEL ? {channel: process.env.PLAYWRIGHT_CHANNEL} : {});
let failures = 0;
const check = (label, ok, detail) => {
  if (!ok) failures++;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${label} — ${detail}`);
};
const route = (page) => new URL(page.url()).pathname.replace('/ai-engineering-handbook', '') + new URL(page.url()).hash;
const lang = (page) => page.evaluate(() => document.documentElement.lang);
const cookie = async (ctx) => (await ctx.cookies()).find((c) => c.name === 'preferred_locale')?.value;

async function settle(page) {
  await page.waitForLoadState('load');
  await page.waitForTimeout(400);
}
async function clickNavbar(page, hrefPart) {
  await page.locator(`.navbar__items:not(.navbar__items--right) a.navbar__link[href*="${hrefPart}"]`).first().click();
  await settle(page);
}
async function newContext(preferred, browserLocale = 'en-US') {
  const ctx = await browser.newContext({locale: browserLocale, viewport: {width: 1440, height: 900}});
  if (preferred) {
    await ctx.addCookies([{name: 'preferred_locale', value: preferred, url: `${SITE}/`}]);
  }
  return ctx;
}

// 1. German reader: navbar click into a course without German, and back.
{
  const ctx = await newContext('de');
  const page = await ctx.newPage();
  await page.goto(`${SITE}/de/rag-agents/`);
  await settle(page);
  await clickNavbar(page, '/azure-dotnet/');
  check('de → Azure lands in English', route(page) === '/azure-dotnet/' && (await lang(page)) === 'en', `${route(page)} lang=${await lang(page)}`);
  await clickNavbar(page, '/rag-agents/');
  check('Azure → RAG returns to German', route(page) === '/de/rag-agents/' && (await lang(page)) === 'de', `${route(page)} lang=${await lang(page)}`);
  check('cookie untouched', (await cookie(ctx)) === 'de', `preferred_locale=${await cookie(ctx)}`);
  await ctx.close();
}

// 2. Direct arrival at a German URL of a course without German keeps the path and hash.
{
  const ctx = await newContext('de');
  const page = await ctx.newPage();
  await page.goto(`${SITE}/de/${AZURE_LESSON}/#probe`);
  await settle(page);
  check('direct /de/azure-dotnet/… → English', route(page) === `/${AZURE_LESSON}/#probe`, route(page));
  await page.goto(`${SITE}/de/blog`);
  await settle(page);
  check('direct /de/blog → English', route(page) === '/blog', route(page));
  await ctx.close();
}

// 3. A locale the course has is left alone.
{
  const ctx = await newContext('ru');
  const page = await ctx.newPage();
  await page.goto(`${SITE}/ru/rag-agents/`);
  await settle(page);
  await clickNavbar(page, '/azure-dotnet/');
  check('ru → Azure stays Russian', route(page) === '/ru/azure-dotnet/', route(page));
  await ctx.close();
}

// 4. Picking English explicitly ends the fallback: the next course stays English.
{
  const ctx = await newContext('de');
  const page = await ctx.newPage();
  await page.goto(`${SITE}/de/rag-agents/`);
  await settle(page);
  await clickNavbar(page, '/azure-dotnet/');
  const dropdown = page.locator('.navbar__items--right .dropdown').first();
  await dropdown.hover();
  await dropdown.locator('a.dropdown__link', {hasText: 'English'}).click();
  await settle(page);
  await clickNavbar(page, '/rag-agents/');
  check('explicit English sticks', route(page) === '/rag-agents/' && (await cookie(ctx)) === 'en', `${route(page)} preferred_locale=${await cookie(ctx)}`);
  await ctx.close();
}

// 4b. The mobile drawer switcher records the choice the same way.
{
  const ctx = await browser.newContext({viewport: {width: 390, height: 844}});
  await ctx.addCookies([{name: 'preferred_locale', value: 'de', url: `${SITE}/`}]);
  const page = await ctx.newPage();
  await page.goto(`${SITE}/de/rag-agents/`);
  await settle(page);
  await page.click('.navbar__toggle');
  await page.locator('.mobileLangSwitch a', {hasText: 'RU'}).click();
  await settle(page);
  check('mobile switcher records the choice', route(page) === '/ru/rag-agents/' && (await cookie(ctx)) === 'ru', `${route(page)} preferred_locale=${await cookie(ctx)}`);
  await ctx.close();
}

// 5. First visit from a German browser to a page without German: stays English, and the
//    first page that has German switches to it.
{
  const ctx = await newContext(null, 'de-DE');
  const page = await ctx.newPage();
  await page.goto(`${SITE}/azure-dotnet/`);
  await settle(page);
  check('first visit to Azure stays English', route(page) === '/azure-dotnet/' && (await cookie(ctx)) === 'de', `${route(page)} preferred_locale=${await cookie(ctx)}`);
  await clickNavbar(page, '/rag-agents/');
  check('then RAG opens in German', route(page) === '/de/rag-agents/', route(page));
  await ctx.close();
}

await browser.close();
console.log(failures ? `locale-fallback-switch: FAIL (${failures})` : 'locale-fallback-switch: PASS');
process.exit(failures ? 1 : 0);
