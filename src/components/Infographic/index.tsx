import useBaseUrl from '@docusaurus/useBaseUrl';
import React from 'react';
import styles from './styles.module.css';

type InfographicProps = {
  /**
   * Path under `static/`, e.g. "/img/infographics/production-failures/02-retrieval.webp".
   * Written WITHOUT the site baseUrl — the component prepends it via `useBaseUrl`. Docusaurus
   * rewrites absolute asset paths in Markdown images, but not a `src` string handed to a
   * component, so a raw "/img/…" here 404s on a site served under a subpath.
   */
  src: string;
  /**
   * What the card shows, in the page's language. Cards carry English labels in every locale
   * (see editorial/infographics/STYLE.md §5), so this — and `caption` — is where the meaning
   * localises. Never "infographic".
   */
  alt: string;
  /** The card's point in one line, in the page's language. Rendered under the card. */
  caption?: string;
  /**
   * Let the image run the full article width on desktop instead of the 560px card cap.
   * For a 16:9 hero, which stays short enough not to crowd out the prose. A 4:3 card must not
   * use this: at full width it is ~675px tall and pushes its own explanation off the screen.
   */
  wide?: boolean;
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
export default function Infographic({src, alt, caption, wide}: InfographicProps): React.JSX.Element {
  return (
    <figure className={`${styles.figure}${wide ? ` ${styles.wide}` : ''}`}>
      <img className={styles.image} src={useBaseUrl(src)} alt={alt} loading="lazy" decoding="async" />
      {caption && <figcaption className={styles.caption}>{caption}</figcaption>}
    </figure>
  );
}
