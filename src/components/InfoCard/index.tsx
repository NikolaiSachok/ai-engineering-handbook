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
 *
 * The drawing has no intrinsic size: CSS gives it `--flow-h`, a multiple of the card's own scale
 * unit, and the line rides its midpoint (`y="50%"`). So the line weight, the dash rhythm and the
 * head shrink with the card instead of surviving as a hairline when everything around them halves.
 */
export function Flow({kind = 'dashed'}: {kind?: FlowKind}): React.JSX.Element {
  const id = `ic-arrow-${React.useId().replace(/[^a-zA-Z0-9]/g, '')}-${kind}`;
  return (
    <span className={cx(styles.flow, styles[kind])} aria-hidden="true">
      <svg className={styles.flowSvg} width="100%" focusable="false">
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
        <line markerEnd={`url(#${id})`} x1="0" x2="100%" y1="50%" y2="50%" />
      </svg>
    </span>
  );
}

/**
 * The vertical pitch of a branch's outcomes. It has to be a constant, not content-driven, because
 * every other number in the fork derives from it: an outcome's centre line, the fork's axis, and
 * the offset the rest of the lane needs so that axis meets the incoming connector. Two label lines
 * fit; a third would overflow, which is what the label budget is for.
 */
const BRANCH_ROW = 'var(--branch-row)';
const BRANCH_PITCH = `calc(${BRANCH_ROW} + var(--branch-gap))`;

/** Distance from the branch's top to outcome `i`'s icon centre line. `i` may be fractional. */
const centreLine = (i: number) => `calc(${i} * ${BRANCH_PITCH} + var(--ic-box) / 2)`;

/** How far the fork's axis sits below the first outcome's centre line. */
export const forkOffset = (count: number) => `calc(${(count - 1) / 2} * ${BRANCH_PITCH})`;

/**
 * One input, N legitimate fates. `Branch` owns its outcome nodes, which is the whole point: only
 * then can the fork size to them. A standalone brace beside two nodes in the same flex row puts the
 * outcomes side by side, runs their labels together as one line, and leaves the brace attached to
 * nothing — the card stops saying what it means.
 *
 * The fork is **symmetric about the incoming connector's axis**: with two outcomes, one sits above
 * the line and one below, so the lane has no dead region beneath the nodes that precede the branch
 * and — the part that matters for meaning — **neither outcome is collinear with the incoming
 * arrow**, so neither reads as the primary path and the other as an afterthought. An earlier fork
 * hung entirely below the axis and a blind reader duly read it as "flow continues into outcome A,
 * with outcome B bracketed underneath".
 *
 * Geometry is arithmetic, not guesswork, because the outcome rows have a fixed pitch: outcome `i`'s
 * centre line is `i × pitch + half the icon box`, and the axis is the midpoint of the first and last
 * of those. `Lane` pushes everything else in the row down by `forkOffset` so the connector arrives
 * exactly on that axis.
 */
export function Branch({children}: {children: React.ReactNode}): React.JSX.Element {
  const outcomes = React.Children.toArray(children).filter(
    (child) => typeof child !== 'string' || child.trim() !== '',
  );
  const n = outcomes.length;
  const axis = centreLine((n - 1) / 2);
  const half = forkOffset(n);
  return (
    <div className={styles.branch}>
      <span aria-hidden="true" className={styles.fork}>
        {/* Up-elbow to the first outcome and down-elbow to the last, each half the fork's height —
            the same shape mirrored, which is what makes the two outcomes read as equals. */}
        <span className={cx(styles.elbow, styles.elbowUp)} style={{top: centreLine(0), height: half}} />
        <span className={cx(styles.elbow, styles.elbowDown)} style={{top: axis, height: half}} />
        {outcomes.slice(1, -1).map((_, i) => (
          <span className={styles.tick} key={`tick-${i}`} style={{top: centreLine(i + 1)}} />
        ))}
        <span className={styles.junction} style={{top: axis}} />
      </span>
      {outcomes}
    </div>
  );
}

/**
 * Keep a connector and the `Branch` it feeds in one flex item. They are authored as siblings, but
 * a wrapping lane (a phone) will otherwise break the line between them and leave the arrow
 * pointing off the end of the row at nothing.
 */
function groupFlowWithBranch(children: React.ReactNode): {
  items: React.ReactNode[];
  offset?: string;
} {
  const items = React.Children.toArray(children).filter(
    (child) => typeof child !== 'string' || child.trim() !== '',
  );
  const out: React.ReactNode[] = [];
  let offset: string | undefined;
  for (let i = 0; i < items.length; i += 1) {
    const child = items[i];
    const next = items[i + 1];
    if (
      React.isValidElement(child) &&
      child.type === Flow &&
      React.isValidElement(next) &&
      next.type === Branch
    ) {
      const props = next.props as {children?: React.ReactNode};
      offset = forkOffset(
        React.Children.toArray(props.children).filter(
          (c) => typeof c !== 'string' || c.trim() !== '',
        ).length,
      );
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
  return {items: out, offset};
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
  const {items, offset} = groupFlowWithBranch(children);
  return (
    <div className={cx(styles.lane, styles[kind])}>
      <span className={styles.pill}>{label}</span>
      <div
        className={styles.laneBody}
        style={offset ? ({'--fork-offset': offset} as React.CSSProperties) : undefined}>
        {items}
      </div>
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
