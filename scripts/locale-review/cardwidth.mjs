/**
 * Measure every composed-infographic string on a page at 360 CSS px, in one locale.
 *
 * WHAT IT MEASURES, AND WHY IT IS NOT OVERFLOW. Three earlier metrics preceded this one, and
 * each looked like a working gate:
 *
 *   v1  el.right vs parent.right  -> 13 "overflows" on EN, SK and RU. IDENTICAL numbers for
 *       three different languages, which is the tell: badges are absolutely positioned
 *       outside their parent by design. The metric was structural, not textual.
 *   v2  el.scrollWidth vs el.clientWidth -> clean pass everywhere; a fault-injected
 *       48-character unbreakable German compound ALSO passed.
 *   v3  widest rendered line box vs available width -> the same fault ALSO passed, and that
 *       is when the mechanism became clear:
 *
 *   => THE CARD CSS BREAKS WORDS MID-WORD (`overflow-wrap`, editorial/infographics/STYLE.md
 *      §16). A card label therefore CANNOT overflow horizontally. Horizontal overflow is not
 *      the failure mode, and a gate built on it returns "pass" for every possible string.
 *      Only fault injection revealed that.
 *
 * The real German failure modes, which is what this measures:
 *   (a) LINE COUNT — a long unbreakable compound wraps to four or five lines and blows the
 *       node pitch and the card's vertical rhythm;
 *   (b) BREAK QUALITY — whether breaks land on syllable boundaries (`Multiagen-/tensysteme`)
 *       or mid-morpheme, which is what #273/#299 fixed by scoping `hyphens: auto` to
 *       `:lang(de)`;
 *   (c) the 11px legibility floor on labels.
 *
 * ---------------------------------------------------------------------------------------
 * THE SERVER IS PART OF THE GATE. This is the fourth way this measurement has been wrong,
 * and it was not the metric — it was the URL.
 *
 * A run served the build with `serve -s build`. The `-s` flag is SPA mode: it rewrites every
 * unresolved path to `index.html`. The site's real baseUrl is `/ai-engineering-handbook/`,
 * so every page path 404'd, got rewritten to the fallback, and the browser was handed the
 * English landing page — `lang="en"`, no card markup. The metric then measured whatever it
 * found there and reported a number.
 *
 * The tool's OWN sanity probe caught it, by printing the resolved `lang`. That probe is the
 * reason this is a footnote and not a shipped wrong measurement, so:
 *   * the probe STAYS, it runs FIRST, and its output is printed before any number;
 *   * the failure is LOUD and the exit code is non-zero — a wrong-page run must never be
 *     distinguishable from a pass only by careful reading;
 *   * the expected locale is an ARGUMENT and is asserted against the served `<html lang>`.
 *     A silent `lang=en` on a `de` run is now a hard failure, not a line of INFO;
 *   * the URL is composed from the site's real baseUrl here, so a caller cannot forget it.
 *
 * Serve it the way e2e/ does — `docusaurus serve` honours baseUrl, `serve -s` does not:
 *   npm run build && npm run serve -- --port 3210 --no-open &
 *   node scripts/locale-review/cardwidth.mjs /de/part-3-production/production-failures de
 *
 * usage: cardwidth.mjs <site-relative-path> [expected-lang] [maxLines]
 *        cardwidth.mjs --self-test
 *
 * NOTE ON THE LAZY IMPORT of playwright, below. It is imported on the MEASUREMENT path only, not
 * at module top level, so that `--self-test` runs with no dependencies installed at all. The
 * logic the self-test covers — composing the URL so it always carries the baseUrl — has nothing
 * to do with a browser, and a top-level import made the self-test fail in CI with
 * ERR_MODULE_NOT_FOUND on a checkout that had not run `npm ci`. A self-test that needs the
 * production dependency stack is a self-test that gets skipped.
 */

const SITE_PATH = '/ai-engineering-handbook';
const BASE = (process.env.BASE_URL ?? 'http://localhost:3210').replace(/\/$/, '');

/** Compose the page URL from the site's real baseUrl, so a caller cannot omit it. */
export function pageUrl(relPath, base = BASE) {
  if (/^https?:/i.test(relPath)) {
    // A full URL is accepted, but only if it actually carries the baseUrl — passing a bare
    // `http://localhost:3210/de/...` is exactly the mistake that produced the SPA fallback.
    if (!relPath.includes(SITE_PATH)) {
      throw new Error(
        `URL does not contain the site baseUrl "${SITE_PATH}": ${relPath}\n` +
        'Without it the server has nothing to resolve and an SPA fallback returns the EN landing page.',
      );
    }
    return relPath;
  }
  const p = relPath.startsWith('/') ? relPath : `/${relPath}`;
  return `${base}${SITE_PATH}${p}`;
}

// ---------------------------------------------------------------------------- self-test
if (process.argv[2] === '--self-test') {
  let fails = 0;
  const check = (label, got, want) => {
    if (got === want) console.log(`  ok   ${label} -> ${got}`);
    else { console.log(`  FAIL ${label} -> got ${got}, want ${want}`); fails++; }
  };
  const throws = (label, fn) => {
    try { fn(); console.log(`  FAIL ${label} -> did not throw`); fails++; }
    catch { console.log(`  ok   ${label} -> threw`); }
  };
  console.log('cardwidth --self-test: the URL must always carry the baseUrl');
  check('a site-relative path gets the baseUrl',
    pageUrl('/de/part-3-production/production-failures', 'http://h:1'),
    'http://h:1/ai-engineering-handbook/de/part-3-production/production-failures');
  check('a leading slash is optional',
    pageUrl('de/x', 'http://h:1'), 'http://h:1/ai-engineering-handbook/de/x');
  check('a full URL carrying the baseUrl passes through',
    pageUrl('http://h:1/ai-engineering-handbook/de/x'), 'http://h:1/ai-engineering-handbook/de/x');
  throws('a full URL WITHOUT the baseUrl is rejected (the SPA-fallback trap)',
    () => pageUrl('http://h:1/de/x'));
  console.log('');
  if (fails) { console.log(`cardwidth --self-test: FAIL (${fails})`); process.exit(1); }
  console.log('cardwidth --self-test: PASS');
  process.exit(0);
}

// ---------------------------------------------------------------------------- run
const rel = process.argv[2];
const expectLang = process.argv[3] || null;
const maxLines = Number(process.argv[4] || 3);
if (!rel) {
  console.error('usage: cardwidth.mjs <site-relative-path> [expected-lang] [maxLines] | --self-test');
  process.exit(2);
}
const url = pageUrl(rel);

// Imported here, not at top level: see the note in the header. Fail with an actionable message
// rather than a bare ERR_MODULE_NOT_FOUND.
let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch (e) {
  console.error('FAIL: playwright is not installed — run `npm ci` before measuring.');
  console.error(`       (${e.code ?? e.message})`);
  process.exit(2);
}

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 360, height: 1400 }, deviceScaleFactor: 3 });
const die = async (msg) => { console.log(`\nFAIL: ${msg}`); await browser.close(); process.exit(1); };

let response;
try {
  response = await page.goto(url, { waitUntil: 'networkidle' });
} catch (e) {
  console.log(`=== SANITY PROBE ===\nurl: ${url}`);
  await die(`could not load the page: ${e.message}\n` +
    '      Is the server running? npm run build && npm run serve -- --port 3210 --no-open');
}
await page.waitForTimeout(600);

const probe = await page.evaluate(() => {
  const el = document.querySelector('[class*="nodeLabel"]');
  const base = {
    lang: document.documentElement.lang,
    path: location.pathname,
    title: document.title.slice(0, 80),
    scrollW: document.documentElement.scrollWidth,
    clientW: document.documentElement.clientWidth,
    cards: document.querySelectorAll('[class*="card"]').length,
    labels: document.querySelectorAll('[class*="nodeLabel"]').length,
  };
  if (!el) return base;
  const cs = getComputedStyle(el);
  return {
    ...base,
    fontFamily: cs.fontFamily.slice(0, 90) + '…',
    fontSize: cs.fontSize,
    hyphens: cs.hyphens || cs.webkitHyphens,
    overflowWrap: cs.overflowWrap || cs.wordWrap,
  };
});

console.log('=== SANITY PROBE — read this before any number below ===');
console.log(`url:    ${url}`);
console.log(`status: ${response?.status()}`);
console.log(JSON.stringify(probe, null, 2));

// --- the assertions that make a wrong-page run impossible to mistake for a pass ---------
if (response && response.status() >= 400) {
  await die(`the server returned HTTP ${response.status()} for ${url}`);
}
if (probe.path && !probe.path.includes(SITE_PATH)) {
  await die(`the served path "${probe.path}" is outside the baseUrl "${SITE_PATH}" — this is the\n` +
    '      SPA-FALLBACK failure: the server rewrote an unresolved path to the landing page.\n' +
    '      Use `docusaurus serve` (npm run serve), never `serve -s build`.');
}
if (expectLang && probe.lang !== expectLang) {
  await die(`expected <html lang="${expectLang}"> and got "${probe.lang}".\n` +
    '      A wrong lang means the requested page was never served — most often the SPA\n' +
    '      fallback handing back the EN landing page. EVERY NUMBER BELOW WOULD BE WORTHLESS.');
}
if (!probe.labels) {
  await die(`no card labels on this page (${probe.cards} card element(s) found).\n` +
    '      Either the URL is wrong, the page has no composed infographics, or the SPA\n' +
    '      fallback served a different document. This is a TOOL FAILURE, not a pass.');
}
const serif = /^\s*(serif|Times|"Times)/i.test(probe.fontFamily ?? '');
if (serif) {
  await die('the resolved font is a FALLBACK SERIF — the stylesheet never loaded. ' +
    'EVERY NUMBER BELOW WOULD BE WORTHLESS.');
}
console.log('ok: resolved font family is a real stack, not a fallback serif.');
if (probe.lang === 'de') {
  if (probe.hyphens !== 'auto') {
    await die(`lang=de but hyphens is "${probe.hyphens}" — #299's :lang(de) scoping did NOT apply.\n` +
      '      German compounds are breaking at arbitrary points and the labels cannot be judged.');
  }
  console.log('ok: lang=de AND hyphens:auto — #299 :lang(de) scoping is live, so compounds break on syllable boundaries.');
} else {
  console.log(`info: lang="${probe.lang}", hyphens="${probe.hyphens}" — expected; hyphenation is scoped to :lang(de) only (#299: global hyphenation regressed en/ru/sk).`);
}
if (probe.scrollW > probe.clientW) {
  await die(`the page scrolls horizontally at 360px (${probe.scrollW} > ${probe.clientW})`);
}
console.log('ok: no horizontal page scroll at 360px');

const rows = await page.evaluate(() => {
  const out = [];
  const lineBoxes = (el) => {
    const rng = document.createRange();
    rng.selectNodeContents(el);
    return [...rng.getClientRects()].filter((r) => r.width > 0 && r.height > 0);
  };
  for (const card of document.querySelectorAll('[class*="card"]')) {
    for (const sel of ['nodeLabel', 'title', 'caption', 'pill']) {
      card.querySelectorAll(`[class*="${sel}"]`).forEach((el) => {
        if (el.querySelector('[class*="nodeLabel"]')) return; // containers, not leaves
        const text = (el.textContent || '').trim();
        if (!text) return;
        const cs = getComputedStyle(el);
        const boxes = lineBoxes(el);
        out.push({
          kind: sel,
          text,
          lines: boxes.length,
          widest: boxes.length ? +Math.max(...boxes.map((b) => b.width)).toFixed(1) : 0,
          avail: +(el.clientWidth || 0).toFixed(1),
          fontSize: cs.fontSize,
          longestWord: text.split(/\s+/).reduce((a, w) => Math.max(a, w.length), 0),
        });
      });
    }
  }
  return out;
});

if (!rows.length) await die('no strings matched — tool failure, not a pass.');

console.log(`\n=== ${rows.length} card strings at 360px (label line budget: ${maxLines}) ===`);
let over = 0, tiny = 0, maxSeen = 0;
const byKind = {};
for (const r of rows) {
  byKind[r.kind] = (byKind[r.kind] || 0) + 1;
  const px = parseFloat(r.fontSize);
  const tooTall = r.kind === 'nodeLabel' && r.lines > maxLines;
  const small = r.kind === 'nodeLabel' && px < 11;
  if (r.kind === 'nodeLabel') maxSeen = Math.max(maxSeen, r.lines);
  if (tooTall) over++;
  if (small) tiny++;
  console.log(`${tooTall ? 'LINES! ' : '  ok   '}${small ? '<11px! ' : '       '}` +
    `${r.kind.padEnd(10)} lines=${r.lines} widest=${String(r.widest).padStart(6)}/${String(r.avail).padStart(6)} ` +
    `maxword=${String(r.longestWord).padStart(2)} «${r.text}»`);
}
console.log(`\nby kind: ${JSON.stringify(byKind)}   max label lines seen: ${maxSeen}`);
console.log(`SUMMARY: ${rows.length} strings · ${over} over the ${maxLines}-line label budget · ${tiny} below the 11px floor`);

await browser.close();
if (over === 0 && tiny === 0) {
  console.log('PASS: card strings within budget at 360px');
  process.exit(0);
}
console.log('FAIL: NOT within budget — SHORTEN the offending strings; do not shrink the type.');
console.log('      And re-check the SHORTENED string still says what the long one said: a width');
console.log('      gate measures pixels, and nothing here checks the claim survived the cut.');
process.exit(1);
