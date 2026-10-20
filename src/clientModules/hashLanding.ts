/**
 * Keep a deep link on its section while the page settles (#816).
 *
 * The browser (on a full load) or Docusaurus (on client-side navigation) scrolls to `#id` once,
 * as soon as the element exists. Diagrams and other late content then grow the page above the
 * target, so a link to a section below a Mermaid diagram landed ~580px short, in every locale.
 * This pins the target at its scroll margin until the reader moves (src/lib/scrollPin.ts).
 */

import type {ClientModule} from '@docusaurus/types';
import {pinScroll, releaseScrollPin} from '@site/src/lib/scrollPin';

function pinToHeading(id: string): void {
  pinScroll(() => {
    const target = document.getElementById(id);
    if (!target) return null;
    const margin = parseFloat(getComputedStyle(target).scrollMarginTop) || 0;
    return target.getBoundingClientRect().top + window.scrollY - margin;
  });
}

const clientModule: ClientModule = {
  // Runs after Docusaurus's own scroll-to-hash on client navigation, and once after hydration
  // on a full load (where the browser did the first scroll).
  onRouteDidUpdate({location}) {
    if (typeof window === 'undefined') {
      return;
    }
    releaseScrollPin();
    if (location.hash.length > 1) {
      pinToHeading(decodeURIComponent(location.hash.slice(1)));
    }
  },
};

export default clientModule;
