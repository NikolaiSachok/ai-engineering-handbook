import React from 'react';
import styles from './styles.module.css';

type InfographicProps = {
  /** Path under `static/`, e.g. "/img/infographics/production-failures/02-retrieval.webp". */
  src: string;
  /**
   * What the card shows, in the page's language. Cards carry English labels in every locale
   * (see editorial/infographics/STYLE.md §5), so this — and `caption` — is where the meaning
   * localises. Never "infographic".
   */
  alt: string;
  /** The card's point in one line, in the page's language. Rendered under the card. */
  caption?: string;
};

/**
 * A generated infographic card.
 *
 * Cards are raster images with English labels baked in, so the prose around them carries the
 * meaning in the reader's language — this component only frames them. The frame matters: the
 * cards are designed on one ground, so on the opposite colour theme they need a border to read
 * as a deliberate plate rather than a pasted screenshot, and a touch less brightness so a light
 * card doesn't glare on a dark page (see `styles.module.css`).
 */
export default function Infographic({src, alt, caption}: InfographicProps): React.JSX.Element {
  return (
    <figure className={styles.figure}>
      <img className={styles.image} src={src} alt={alt} loading="lazy" decoding="async" />
      {caption && <figcaption className={styles.caption}>{caption}</figcaption>}
    </figure>
  );
}
