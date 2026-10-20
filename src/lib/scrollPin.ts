/**
 * Hold a scroll position while the page settles, until the reader moves.
 *
 * Content above the reader keeps arriving after the first scroll: Mermaid renders every diagram
 * client-side (the server HTML carries none of them), and images and embeds load late. Each one
 * grows the page, so a position applied once drifts — a deep link landed ~580px short (#816),
 * and a locale switch restored on two timers landed a section or more early on a slow CPU (#818).
 *
 * Docusaurus's Mermaid component exposes no render-complete signal, so the signal used here is
 * the layout change itself: a ResizeObserver on the app root re-applies the position whenever
 * the page resizes. (Not <body>: the theme sets `height: 100%` on it, so it never resizes.) No
 * timer: it acts exactly when the layout moves and never otherwise.
 *
 * The pin is released by the first scroll that leaves the page somewhere other than where the pin
 * put it or wants it — that is the reader (wheel, keys, scrollbar, touch alike), and nothing pulls
 * them back. Our own scroll is recognised by its position, not by timing, because its scroll event
 * can arrive after the layout has already moved again. A new pin replaces the old one.
 */

let release: (() => void) | null = null;

/** Clamp to what the browser can actually scroll to, or a pin at the page bottom would read the
 *  browser's own clamping as the reader moving. */
function reachable(y: number): number {
  const max = Math.max(document.documentElement.scrollHeight - window.innerHeight, 0);
  return Math.min(Math.max(Math.round(y), 0), max);
}

/**
 * Scroll to `desired()` now, and again whenever the layout moves, until the reader scrolls.
 * `desired` is re-evaluated each time, so it should measure the DOM rather than close over
 * numbers; returning null releases the pin.
 */
export function pinScroll(desired: () => number | null): void {
  releaseScrollPin();
  if (typeof ResizeObserver === 'undefined') {
    const y = desired();
    if (y !== null) window.scrollTo(0, reachable(y));
    return;
  }

  const target = (): number | null => {
    const y = desired();
    return y === null ? null : reachable(y);
  };
  let applied = window.scrollY;
  const apply = () => {
    const y = target();
    if (y === null) {
      releaseScrollPin();
    } else if (Math.abs(window.scrollY - y) > 2) {
      window.scrollTo(0, y);
      applied = window.scrollY;
    }
  };

  const observer = new ResizeObserver(apply);
  const onScroll = () => {
    const y = target();
    const ours = Math.abs(window.scrollY - applied) <= 2;
    if (y === null || (!ours && Math.abs(window.scrollY - y) > 2)) {
      releaseScrollPin();
    }
  };

  release = () => {
    observer.disconnect();
    window.removeEventListener('scroll', onScroll);
    release = null;
  };

  apply();
  observer.observe(document.getElementById('__docusaurus') ?? document.body);
  window.addEventListener('scroll', onScroll, {passive: true});
}

export function releaseScrollPin(): void {
  release?.();
}
