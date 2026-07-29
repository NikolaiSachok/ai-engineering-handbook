import React from 'react';
import styles from './styles.module.css';

/**
 * The commit-first gate on a Design Scenario page: the reader answers the question themselves
 * before the three attempts are shown.
 *
 * Why this exists rather than a plain `<details>`. Docusaurus themes markdown `<details>` as an
 * `alert`-class collapsible — a tinted plate with a coloured border, which is right for the two or
 * three sentences a collapsible usually holds. A scenario's reveal holds the whole body of the
 * page, several thousand words, and at that size the plate stops reading as a callout and starts
 * reading as a different kind of page: the one article in the handbook printed on coloured paper.
 * Reported by the author on the first published scenario.
 *
 * So the affordance is concentrated in the summary — which stays small, and may be coloured — and
 * the revealed body inherits ordinary page styling. A reader who opens it sees handbook prose, not
 * a container.
 *
 * It renders a real `<details>`/`<summary>`: the gate keeps working with JavaScript disabled, the
 * keyboard behaviour is the browser's, and find-in-page can still reach closed content in browsers
 * that support it. Writing `<details>` in MDX would pick the themed component back up, so the
 * element is created here in JSX instead, where the MDX component map does not apply.
 */
export default function Reveal({
  children,
  summary = 'Show the three attempts',
}: {
  children: React.ReactNode;
  /** The affordance's label. Keep it an instruction, not a heading. */
  summary?: string;
}): React.JSX.Element {
  return (
    <details className={styles.reveal}>
      <summary className={styles.summary}>{summary}</summary>
      <div className={styles.body}>{children}</div>
    </details>
  );
}
