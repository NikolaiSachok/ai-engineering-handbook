import useBaseUrl from '@docusaurus/useBaseUrl';
import React from 'react';
import styles from './styles.module.css';

/**
 * Composed infographic cards — the labelled-node diagram, built in the browser.
 *
 * Why this exists alongside the generated-raster cards: a whole-card image cannot localise its
 * labels (image models mangle Cyrillic and Slovak diacritics), cannot guarantee that a recurring
 * concept is drawn identically twice, and turns "colour this node differently" into a
 * regeneration. Here the labels are HTML text, so translators edit Markdown; the icons are a
 * fixed set, so `the model` is the same chip on every card; and an encoding is a prop.
 *
 * Deliberate limitation: the icon assets are raster with a baked outline, so a card renders as a
 * light plate on both themes rather than adapting. Swapping `icons/` for an SVG set would fix that
 * without touching any card markup. See editorial/infographics/CSS-CARDS-PLAN.md.
 */

/** The icon lexicon. One asset per concept — that is the whole point; do not add near-duplicates. */
export const ICONS = [
  'document', 'documentStack', 'spreadsheet', 'browserPage',
  'database', 'clipboard', 'calendar', 'dashboard',
  'speechBubble', 'speechBubbleGroup', 'magnifier', 'sortedList',
  'gauge', 'gate', 'chip', 'sliders',
] as const;

/** Small overlay glyphs, composed onto a base icon so 24 assets cover ~36 concepts. */
export const BADGES = [
  'tick', 'cross', 'bang', 'padlock', 'pin', 'tag', 'refresh', 'crack',
] as const;

export type IconName = (typeof ICONS)[number];
export type BadgeName = (typeof BADGES)[number];

/** Position on an ordering ramp. `1` is the first resort, `last` the de-emphasised final one. */
export type Rank = '1' | '2' | '3' | '4' | 'last';

function Asset({name, className}: {name: string; className: string}): React.JSX.Element {
  return (
    <img
      className={className}
      src={useBaseUrl(`/img/infographics/icons/${name}.webp`)}
      alt=""
      aria-hidden="true"
      loading="lazy"
      decoding="async"
    />
  );
}

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
  return (
    <figure className={`${styles.node}${rank ? ` ${styles[`rank${rank}`]}` : ''}`}>
      <span className={styles.iconWrap}>
        <Asset name={icon} className={styles.icon} />
        {badge && <Asset name={badge} className={styles.badge} />}
      </span>
      <figcaption className={styles.nodeLabel}>{label}</figcaption>
    </figure>
  );
}

export function Flow({kind = 'dashed'}: {kind?: 'dashed' | 'solid' | 'fail'}): React.JSX.Element {
  return <span className={`${styles.flow} ${styles[kind]}`} aria-hidden="true" />;
}

export function Brace(): React.JSX.Element {
  return <span className={styles.brace} aria-hidden="true" />;
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
    <div className={`${styles.lane} ${styles[kind]}`}>
      <span className={styles.pill}>{label}</span>
      <div className={styles.laneBody}>{children}</div>
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
