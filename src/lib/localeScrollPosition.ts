/**
 * Preserve the reader's position across a language switch.
 *
 * Every course heading carries the same explicit id in every locale (#813), so a section is
 * named the same way on both sides of the switch. What the reader is looking at is captured as
 * a path of headings, from the innermost section they are in out to its H2, each with how far
 * into that heading's section they are (0..1). A fraction rather than pixels, because the two
 * languages render a section at different heights.
 *
 *   1. On a locale-switch click (the swizzled locale dropdown) the path is recorded in
 *      `sessionStorage`, keyed by the DESTINATION pathname — the switch is a full page load.
 *   2. When the destination mounts (src/theme/Root.tsx) the record is consumed: the first id on
 *      the path that exists there is the target, and the reader lands the same fraction into it.
 *
 * Why a path and not one id: a locale may subdivide below H2 (four Russian deep dives do), so the
 * innermost section can exist on one side only. Its parent H2 always exists on both — check 2 of
 * scripts/locale-parity-check.sh holds H1/H2 equal — so the walk outward always finds a section,
 * and the reader lands proportionally inside it rather than at its top. Above the first heading,
 * the "section" is the page top; on a page with no headings it is the whole page.
 *
 * Diagrams render after the page mounts and push content down, so the position is held by the
 * shared scroll pin (src/lib/scrollPin.ts) until the reader scrolls, not applied once.
 */

import {pinScroll} from '@site/src/lib/scrollPin';

const STORAGE_PREFIX = 'localeScrollPos:';

/** Records older than this (ms) are ignored — they mean the navigation never
 *  actually happened, so a later plain reload shouldn't teleport the reader. */
const MAX_AGE_MS = 30_000;

/** One heading on the reader's path: its id ('' = the page top) and how far into its section. */
type Step = {id: string; offset: number};

type PositionRecord = {
  /** Innermost section first, out to its H2, then the page top. */
  path: Step[];
  /** Capture time, for the freshness guard. */
  ts: number;
};

function canUseDom(): boolean {
  return typeof window !== 'undefined' && typeof document !== 'undefined';
}

/** Normalize a pathname so the write key (from the dropdown href) and the read
 *  key (from `window.location`) match: decoded, without a trailing slash. */
export function normalizePathname(pathname: string): string {
  let p = pathname;
  try {
    p = decodeURIComponent(p);
  } catch {
    // Leave as-is if it isn't valid percent-encoding.
  }
  return p.length > 1 ? p.replace(/\/+$/, '') : p;
}

function storageKey(pathname: string): string {
  return STORAGE_PREFIX + normalizePathname(pathname);
}

/** The article's section headings, in document order. Restricted to the doc
 *  content so navbar/TOC/footer headings never enter the mapping. */
function getSectionHeadings(): HTMLElement[] {
  const container =
    document.querySelector('.theme-doc-markdown') ??
    document.querySelector('article');
  if (!container) return [];
  return Array.from(container.querySelectorAll<HTMLElement>('h2[id], h3[id], h4[id]'));
}

const level = (h: HTMLElement): number => Number(h.tagName.slice(1));

/** Height of the sticky navbar — content below this line is what the reader
 *  actually sees at the top of the viewport. */
function navbarHeight(): number {
  const navbar = document.querySelector<HTMLElement>('.navbar');
  return navbar?.offsetHeight ?? 60;
}

/** Absolute (document-relative) top of an element. */
function absoluteTop(el: HTMLElement): number {
  return el.getBoundingClientRect().top + window.scrollY;
}

function pageEnd(): number {
  return Math.max(document.documentElement.scrollHeight - window.innerHeight, 1);
}

/** A heading's section in absolute document coordinates: from the heading to the next heading at
 *  the same or a higher level, so it includes its own subsections. `i === -1` is the page top,
 *  which ends at the first heading. */
function sectionBounds(headings: HTMLElement[], i: number): {start: number; end: number} {
  const start = i < 0 ? 0 : absoluteTop(headings[i]);
  const next = i < 0 ? headings[0] : headings.slice(i + 1).find((h) => level(h) <= level(headings[i]));
  const end = next ? absoluteTop(next) : pageEnd();
  return {start, end: Math.max(end, start + 1)};
}

/**
 * Capture the reader's current position and persist it against the destination
 * pathname. Called from the locale dropdown's click handler, before the browser
 * navigates away.
 */
export function capturePosition(destinationPathname: string): void {
  if (!canUseDom()) return;
  const headings = getSectionHeadings();

  // The line just under the sticky navbar is the reader's effective "top".
  const line = window.scrollY + navbarHeight();
  const fraction = (i: number) => {
    const {start, end} = sectionBounds(headings, i);
    return Math.min(Math.max((line - start) / (end - start), 0), 1);
  };

  // The innermost section is the last heading at/above the line; each step outward is the
  // nearest earlier heading of a higher level, up to the H2.
  let current = -1;
  for (let i = 0; i < headings.length; i += 1) {
    if (absoluteTop(headings[i]) <= line) current = i;
    else break;
  }
  const path: Step[] = [];
  for (let i = current; i >= 0; i -= 1) {
    if (path.length === 0 || level(headings[i]) < level(headings[current])) {
      path.push({id: headings[i].id, offset: fraction(i)});
      current = i;
    }
  }
  path.push({id: '', offset: fraction(-1)});

  const record: PositionRecord = {path, ts: Date.now()};
  try {
    window.sessionStorage.setItem(storageKey(destinationPathname), JSON.stringify(record));
  } catch {
    // Private mode / quota — the feature simply degrades to top-of-page.
  }
}

/** Read and remove the record for this path, so a later plain reload never re-triggers. */
function takeRecord(pathname: string): PositionRecord | null {
  let raw: string | null = null;
  try {
    raw = window.sessionStorage.getItem(storageKey(pathname));
    window.sessionStorage.removeItem(storageKey(pathname));
  } catch {
    return null;
  }
  if (!raw) return null;
  try {
    const parsed = JSON.parse(raw) as PositionRecord;
    return Array.isArray(parsed?.path) && typeof parsed.ts === 'number' ? parsed : null;
  } catch {
    return null;
  }
}

/** Where the record says the reader should be on this page, measured from the current DOM. */
function resolve(record: PositionRecord): number | null {
  const headings = getSectionHeadings();
  for (const {id, offset} of record.path) {
    const i = id === '' ? -1 : headings.findIndex((h) => h.id === id);
    if (id === '' || i >= 0) {
      const {start, end} = sectionBounds(headings, i);
      return start + offset * (end - start) - navbarHeight();
    }
  }
  return null;
}

/**
 * Restore the reader's position for the current page, if a fresh record exists.
 * Called once after the destination page mounts. It is a no-op on every ordinary
 * page load — there is simply no record to consume.
 */
export function restorePosition(pathname: string): void {
  if (!canUseDom()) return;
  const record = takeRecord(pathname);
  if (!record || Date.now() - record.ts > MAX_AGE_MS) return; // stale → leave at top
  pinScroll(() => resolve(record));
}
