// End-to-end check that the language pickers list only the locales the current page exists in.
//
// The bug it guards against: Docusaurus builds every route in every locale, so the desktop
// dropdown and the mobile drawer switcher offered Slovak and German on the Azure & .NET course
// (English + Russian only) and every language on the English-only Design Scenarios course and
// blog — each "translation" being the same English page (src/lib/availableLocales.ts).
//
// Usage:
//   npm run build && npm run serve -- --port 3210 --no-open &
//   BASE_URL=http://localhost:3210 node e2e/locale-dropdown-scope.mjs
//
// Requires Playwright's chromium: `npx playwright install chromium` (or set
// PLAYWRIGHT_CHANNEL=chrome to use an installed Chrome).

import {chromium} from 'playwright';

const BASE = (process.env.BASE_URL ?? 'http://localhost:3210').replace(/\/$/, '');
const SITE = `${BASE}/ai-engineering-handbook`;

// [route, expected desktop dropdown labels]. A locale-prefixed route a section lacks is moved to
// English first (e2e/locale-fallback-switch.mjs), so its picker is the English one.
const CASES = [
  ['/', ['English', 'Русский', 'Slovenčina', 'Deutsch']],
  ['/rag-agents/', ['English', 'Русский', 'Slovenčina', 'Deutsch']],
  ['/ai-sdlc/', ['English', 'Русский', 'Slovenčina']],
  ['/azure-dotnet/', ['English', 'Русский']],
  ['/ru/azure-dotnet/', ['English', 'Русский']],
  ['/sk/azure-dotnet/', ['English', 'Русский']],
  ['/design-scenarios/', ['English']],
  ['/ru/design-scenarios/', ['English']],
  ['/blog', ['English']],
  ['/de/blog', ['English']],
];
// [route, expected mobile drawer switcher codes]; the switcher is hidden with one locale.
const MOBILE = [
  ['/azure-dotnet/', ['EN', 'RU']],
  ['/design-scenarios/', []],
];

const browser = await chromium.launch(process.env.PLAYWRIGHT_CHANNEL ? {channel: process.env.PLAYWRIGHT_CHANNEL} : {});
let failures = 0;
const check = (label, got, want) => {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  if (!ok) failures++;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${label}: ${JSON.stringify(got)}${ok ? '' : ` (want ${JSON.stringify(want)})`}`);
};

for (const [route, want] of CASES) {
  const page = await browser.newPage({viewport: {width: 1440, height: 900}});
  await page.goto(`${SITE}${route}`);
  const got = await page.$$eval('.navbar__items--right .dropdown__menu a', (as) => as.map((a) => a.textContent.trim()));
  check(`dropdown ${route}`, got, want);
  await page.close();
}
for (const [route, want] of MOBILE) {
  const page = await browser.newPage({viewport: {width: 390, height: 844}});
  await page.goto(`${SITE}${route}`);
  await page.click('.navbar__toggle');
  const got = await page.$$eval('.mobileLangSwitch a', (as) => as.map((a) => a.textContent.trim()));
  check(`mobile switcher ${route}`, got, want);
  await page.close();
}
await browser.close();
console.log(failures ? `locale-dropdown-scope: FAIL (${failures})` : 'locale-dropdown-scope: PASS');
process.exit(failures ? 1 : 0);
