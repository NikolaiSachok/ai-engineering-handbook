import React from 'react';
import {
  BADGE_ICONS,
  BADGE_TOP_RIGHT,
  OBJECT_ICONS,
  type BadgeName,
  type IconName,
} from './icons';
import styles from './styles.module.css';

/**
 * Composed infographic cards — the labelled-node diagram, built in the browser.
 *
 * Why this exists alongside the generated-raster cards: a whole-card image cannot localise its
 * labels (image models mangle Cyrillic and Slovak diacritics), cannot guarantee that a recurring
 * concept is drawn identically twice, and turns "colour this node differently" into a
 * regeneration. Here the labels are HTML text, so translators edit Markdown; the icons are a
 * fixed inline-SVG lexicon, so `the model` is the same chip on every card; and an encoding is a
 * prop — `rank` tints the icon *and* its label, which no raster set can do.
 *
 * Because the icons are `currentColor`-driven the card is theme-adaptive rather than a light
 * plate: ground, panels, ink and icon fills all shift on the dark theme (styles.module.css).
 */

export {BADGES, ICONS} from './icons';
export type {BadgeName, IconName} from './icons';

/** Position on an ordering ramp. `1` is the first resort, `last` the de-emphasised final one. */
export type Rank = '1' | '2' | '3' | '4' | 'last';

/** A connector's meaning. `fail` is the consequence of the fault and nothing else. */
export type FlowKind = 'dashed' | 'solid' | 'fail';

const cx = (...parts: (string | false | undefined)[]) => parts.filter(Boolean).join(' ');

export function Node({
  icon,
  label,
  badge,
  rank,
}: {
  icon: IconName;
  label: string;
  badge?: BadgeName;
  /** Encodes position on a ramp as colour + emphasis. Omit when the nodes are peers. */
  rank?: Rank;
}): React.JSX.Element {
  const Icon = OBJECT_ICONS[icon];
  const Badge = badge ? BADGE_ICONS[badge] : undefined;
  if (!Icon) throw new Error(`InfoCard: unknown icon "${icon}"`);
  return (
    <figure className={cx(styles.node, rank && styles[`rank${rank}`])}>
      <span className={styles.iconWrap}>
        <Icon className={styles.icon} aria-hidden="true" focusable="false" />
        {Badge && (
          <span
            className={cx(
              styles.badge,
              styles[`badge_${badge!}`],
              BADGE_TOP_RIGHT.has(icon) && styles.badgeTop,
            )}>
            <Badge aria-hidden="true" focusable="false" />
          </span>
        )}
      </span>
      <figcaption className={styles.nodeLabel}>{label}</figcaption>
    </figure>
  );
}

/**
 * A connector. Real SVG with a real `marker-end`, sized to its slot — so the arrow spans the
 * actual gap instead of being a fixed-length stub, and the head is part of the same path rather
 * than a triangle faked from CSS borders. Percentage coordinates work because the `<svg>` has no
 * viewBox, so user units are CSS pixels; `markerUnits="strokeWidth"` keeps the head proportional.
 *
 * Every connector sits on the icon box's centre line — a fixed fraction of the icon box, never of
 * the node, whose height changes whenever a label wraps. A `Branch` puts its brace's nub on that
 * same line, so connectors into a branch need no special case.
 */
export function Flow({kind = 'dashed'}: {kind?: FlowKind}): React.JSX.Element {
  const id = `ic-arrow-${React.useId().replace(/[^a-zA-Z0-9]/g, '')}-${kind}`;
  return (
    <span className={cx(styles.flow, styles[kind])} aria-hidden="true">
      <svg className={styles.flowSvg} height="10" width="100%" focusable="false">
        <defs>
          <marker
            id={id}
            markerHeight="5"
            markerUnits="strokeWidth"
            markerWidth="5"
            orient="auto"
            refX="5"
            refY="2.5">
            <path d="M0 0L5 2.5L0 5z" fill="currentColor" />
          </marker>
        </defs>
        <line markerEnd={`url(#${id})`} x1="0" x2="100%" y1="5" y2="5" />
      </svg>
    </span>
  );
}

/**
 * One input, N legitimate fates. The brace owns its branches as children, which is the whole
 * point: only then can it size to them. A standalone brace beside two nodes in the same flex row
 * puts the outcomes side by side, runs their labels together as one line, and leaves the brace
 * attached to nothing — the card stops saying what it means.
 *
 * The brace is drawn as two independently stretched halves so its **nub lands exactly on the icon
 * centre line** — the same line every connector sits on. That is why the incoming arrow needs no
 * special case: one alignment rule governs the whole grammar. Aiming the arrow at a symmetric
 * brace's midpoint instead leaves it floating a label's height below the node it comes from, which
 * a label-stripped read called the worst mechanical error on the card.
 */
export function Branch({children}: {children: React.ReactNode}): React.JSX.Element {
  return (
    <div className={styles.branch}>
      <span className={styles.brace} aria-hidden="true">
        {/* preserveAspectRatio="none" stretches each half to whatever height it is given;
            vector-effect keeps the stroke at its authored width while it stretches. */}
        <svg
          className={cx(styles.braceSvg, styles.braceTop)}
          focusable="false"
          preserveAspectRatio="none"
          viewBox="0 0 14 50">
          <path d="M13 1.5C7 1.5 7 12 7 26c0 14-6 14-6 24" vectorEffect="non-scaling-stroke" />
        </svg>
        <svg
          className={cx(styles.braceSvg, styles.braceBottom)}
          focusable="false"
          preserveAspectRatio="none"
          viewBox="0 0 14 50">
          <path d="M1 0c0 10 6 10 6 24 0 14 0 24.5 6 24.5" vectorEffect="non-scaling-stroke" />
        </svg>
        {/* The junction. Without it the brace floats: the arrow appears to point at the first
            branch rather than at the fork, and a label-stripped reader called the brace
            structurally unanchored. */}
        <span className={styles.braceNode} />
      </span>
      <div className={styles.branchNodes}>{children}</div>
    </div>
  );
}

/**
 * Keep a connector and the `Branch` it feeds in one flex item. They are authored as siblings, but
 * a wrapping lane (a phone) will otherwise break the line between them and leave the arrow
 * pointing off the end of the row at nothing.
 */
function groupFlowWithBranch(children: React.ReactNode): React.ReactNode[] {
  const items = React.Children.toArray(children).filter(
    (child) => typeof child !== 'string' || child.trim() !== '',
  );
  const out: React.ReactNode[] = [];
  for (let i = 0; i < items.length; i += 1) {
    const child = items[i];
    const next = items[i + 1];
    if (
      React.isValidElement(child) &&
      child.type === Flow &&
      React.isValidElement(next) &&
      next.type === Branch
    ) {
      out.push(
        <div className={styles.flowBranch} key={`fb-${i}`}>
          {child}
          {next}
        </div>,
      );
      i += 1;
    } else {
      out.push(child);
    }
  }
  return out;
}

export function Lane({
  kind,
  label,
  children,
}: {
  kind: 'demo' | 'production';
  label: string;
  children: React.ReactNode;
}): React.JSX.Element {
  return (
    <div className={cx(styles.lane, styles[kind])}>
      <span className={styles.pill}>{label}</span>
      <div className={styles.laneBody}>{groupFlowWithBranch(children)}</div>
    </div>
  );
}

export default function InfoCard({
  title,
  caption,
  children,
}: {
  title: string;
  caption?: string;
  children: React.ReactNode;
}): React.JSX.Element {
  return (
    <figure className={styles.card}>
      <div className={styles.plate}>
        <h4 className={styles.title}>{title}</h4>
        {children}
      </div>
      {caption && <figcaption className={styles.caption}>{caption}</figcaption>}
    </figure>
  );
}
