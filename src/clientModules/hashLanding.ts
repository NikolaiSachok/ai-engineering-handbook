/**
 * Keep a deep link on its section while the page settles (#816).
 *
 * The browser (on a full load) or Docusaurus (on client-side navigation) scrolls to `#id`
 * once, as soon as the element exists. Mermaid then renders every diagram client-side — the
 * server HTML carries none of them — and each one grows the page. When that happens ABOVE the
 * target the section slides down while `scrollY` stays put: a link to a section below a
 * diagram landed ~580px short, in every locale. Native scroll anchoring does not catch it, and
 * Safari has none.
 *
 * Docusaurus's Mermaid component exposes no render-complete signal, and diagrams are not the
 * only late content (images, embeds). So the signal used here is the layout change itself: a
 * ResizeObserver on the app root re-aligns the target whenever the page resizes, for as long as
 * the reader has not moved. (Not <body>: the theme sets `height: 100%` on it, so it never
 * resizes.) No timer: it acts exactly when the layout moves and never otherwise.
 *
 * "Has not moved" is read off the target, not off input events: after each alignment we note
 * where the heading sits, and any scroll that leaves it somewhere else is the reader's (wheel,
 * keys, scrollbar, touch alike), so the pin is released and nothing pulls them back.
 */

import type {ClientModule} from '@docusaurus/types';

let release: (() => void) | null = null;

function pin(id: string): void {
  const target = document.getElementById(id);
  if (!target || typeof ResizeObserver === 'undefined') {
    return;
  }

  let rest = 0;
  const align = () => {
    target.scrollIntoView({block: 'start'});
    rest = target.getBoundingClientRect().top;
  };
  const moved = () => Math.abs(target.getBoundingClientRect().top - rest) > 2;

  const observer = new ResizeObserver(() => {
    if (moved()) {
      align();
    }
  });
  const onScroll = () => {
    if (moved()) {
      release?.();
    }
  };

  release = () => {
    observer.disconnect();
    window.removeEventListener('scroll', onScroll);
    release = null;
  };

  align();
  observer.observe(document.getElementById('__docusaurus') ?? document.body);
  window.addEventListener('scroll', onScroll, {passive: true});
}

const clientModule: ClientModule = {
  // Runs after Docusaurus's own scroll-to-hash on client navigation, and once after hydration
  // on a full load (where the browser did the first scroll).
  onRouteDidUpdate({location}) {
    if (typeof window === 'undefined') {
      return;
    }
    release?.();
    if (location.hash.length > 1) {
      pin(decodeURIComponent(location.hash.slice(1)));
    }
  },
};

export default clientModule;
