// End-to-end check that the desktop navbar fits on one line in every locale.
//
// The bug it guards against: from 997px (where the hamburger gives way to the full navbar) up
// to ~1440px, the five navbar items wrapped onto two or three lines and the site title was
// truncated, in every locale (see src/css/custom.css, "Navbar fit on desktop widths").
// Adding a course to the navbar is what tips it over, so run this when one is added.
//
// Usage:
//   npm run build && npm run serve -- --port 3210 --no-open &
//   BASE_URL=http://localhost:3210 node e2e/navbar-fit.mjs
//
// Requires Playwright's chromium: `npx playwright install chromium` (or set
// PLAYWRIGHT_CHANNEL=chrome to use an installed Chrome).

import {chromium} from 'playwright';

const BASE = (process.env.BASE_URL ?? 'http://localhost:3210').replace(/\/$/, '');
const SITE = `${BASE}/ai-engineering-handbook`;
const LOCALES = ['', 'ru/', 'sk/', 'de/'];
const WIDTHS = [997, 1024, 1099, 1100, 1180, 1199, 1200, 1279, 1280, 1366, 1439, 1440, 1920];

const browser = await chromium.launch(process.env.PLAYWRIGHT_CHANNEL ? {channel: process.env.PLAYWRIGHT_CHANNEL} : {});
let failures = 0;
for (const loc of LOCALES) {
  for (const width of WIDTHS) {
    const page = await browser.newPage({viewport: {width, height: 800}});
    await page.goto(`${SITE}/${loc}`);
    const problems = await page.evaluate(() => {
      const out = [];
      const visible = (e) => e.offsetParent !== null;
      for (const link of document.querySelectorAll('.navbar__inner .navbar__link')) {
        if (!visible(link)) continue;
        const lineHeight = parseFloat(getComputedStyle(link).lineHeight) || 24;
        if (link.getBoundingClientRect().height > 1.6 * lineHeight) out.push(`"${link.textContent.trim()}" wraps`);
      }
      const title = document.querySelector('.navbar__title');
      if (title && visible(title) && title.scrollWidth > title.clientWidth) out.push('site title truncated');
      const items = [...document.querySelectorAll('.navbar__inner .navbar__item, .navbar__inner .navbar__brand')]
        .filter(visible).map((e) => e.getBoundingClientRect()).sort((a, b) => a.left - b.left);
      for (let i = 1; i < items.length; i++) if (items[i].left < items[i - 1].right - 1) out.push('navbar items overlap');
      if (document.documentElement.scrollWidth > window.innerWidth) out.push('page scrolls sideways');
      return out;
    });
    if (problems.length) {
      failures++;
      console.log(`FAIL /${loc} @${width}px: ${[...new Set(problems)].join('; ')}`);
    }
    await page.close();
  }
}
await browser.close();
console.log(failures ? `navbar-fit: FAIL (${failures})` : `navbar-fit: PASS (${LOCALES.length * WIDTHS.length} checks)`);
process.exit(failures ? 1 : 0);
