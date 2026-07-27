/**
 * The icon lexicon — one asset per concept, imported as inline SVG (svgr), so a recurring
 * concept is the same drawing on every card and can be recoloured per node.
 *
 * Sourcing is hybrid and deliberate (see ../../../../editorial/infographics/CSS-CARDS-PLAN.md):
 * generic objects are vendored from Tabler Icons (MIT) and normalised; the domain metaphors no
 * icon set ships are hand-authored here. Both obey the same grid, so they are indistinguishable
 * in use: 48x48 viewBox, effective stroke 3, `stroke="currentColor"`, fills via
 * `var(--ic-fill, #3b82f6)` / `var(--ic-tint, #93c5fd)` — always with the literal fallback,
 * because a non-browser rasteriser cannot resolve `var()`.
 *
 * Provenance and licence: ./NOTICE.md.
 */

import branchSplit from './branchSplit.svg';
import browserPage from './browserPage.svg';
import calendar from './calendar.svg';
import chainSteps from './chainSteps.svg';
import chip from './chip.svg';
import chunkedPage from './chunkedPage.svg';
import clipboard from './clipboard.svg';
import cloud from './cloud.svg';
import codeFile from './codeFile.svg';
import coins from './coins.svg';
import dashboard from './dashboard.svg';
import database from './database.svg';
import document from './document.svg';
import documentStack from './documentStack.svg';
import driftCurves from './driftCurves.svg';
import funnel from './funnel.svg';
import gate from './gate.svg';
import gauge from './gauge.svg';
import globe from './globe.svg';
import lockOpen from './lockOpen.svg';
import magnifier from './magnifier.svg';
import mixedSources from './mixedSources.svg';
import plug from './plug.svg';
import retrieval from './retrieval.svg';
import scales from './scales.svg';
import sliders from './sliders.svg';
import sortedList from './sortedList.svg';
import speechBubble from './speechBubble.svg';
import speechBubbleEmpty from './speechBubbleEmpty.svg';
import speechBubbleGroup from './speechBubbleGroup.svg';
import spreadsheet from './spreadsheet.svg';
import traceSpans from './traceSpans.svg';

import bang from './badges/bang.svg';
import crack from './badges/crack.svg';
import cross from './badges/cross.svg';
import padlock from './badges/padlock.svg';
import pin from './badges/pin.svg';
import refresh from './badges/refresh.svg';
import tag from './badges/tag.svg';
import tick from './badges/tick.svg';

/** Base objects. Ordered as the lexicon sheet reads, not alphabetically by accident. */
export const OBJECT_ICONS = {
  // containers and records
  document,
  documentStack,
  spreadsheet,
  browserPage,
  mixedSources,
  database,
  clipboard,
  calendar,
  codeFile,
  chunkedPage,
  // instruments and controls
  dashboard,
  gauge,
  sliders,
  magnifier,
  retrieval,
  sortedList,
  funnel,
  gate,
  scales,
  // conversation, reach, plumbing
  speechBubble,
  speechBubbleEmpty,
  speechBubbleGroup,
  globe,
  plug,
  chip,
  cloud,
  coins,
  lockOpen,
  // domain metaphors — hand-authored, because no set ships them
  driftCurves,
  branchSplit,
  chainSteps,
  traceSpans,
} as const;

/** Small overlay glyphs, composed onto a base object so 28 objects cover far more concepts. */
export const BADGE_ICONS = {tick, cross, bang, padlock, pin, tag, refresh, crack} as const;

/**
 * Icons whose own drawing occupies the bottom-right corner — a shift arrow, a sort arrow, the last
 * span, a barrier base. Their badge moves to the top-right so the overlay never covers the part of
 * the icon that carries the meaning.
 */
export const BADGE_TOP_RIGHT: ReadonlySet<string> = new Set([
  'driftCurves',
  'sortedList',
  'gate',
  'branchSplit',
  'traceSpans',
  'speechBubble',
  'speechBubbleEmpty',
  // The magnifier IS the meaning here; a bottom-right badge would sit exactly on the lens.
  'retrieval',
]);

export type IconName = keyof typeof OBJECT_ICONS;
export type BadgeName = keyof typeof BADGE_ICONS;

export const ICONS = Object.keys(OBJECT_ICONS) as IconName[];
export const BADGES = Object.keys(BADGE_ICONS) as BadgeName[];
