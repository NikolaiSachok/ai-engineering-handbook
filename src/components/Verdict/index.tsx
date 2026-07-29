import React from 'react';
import styles from './styles.module.css';

/**
 * The assessment of one Design Scenario attempt, set apart from the attempt itself.
 *
 * Why this is a component rather than a bolded lead-in. A scenario page runs three long answers in
 * the candidates' own voices, and those answers are full of bolded section labels — `**Rollout.**`,
 * `**Classification.**` — because that is how engineers write at a whiteboard. A verdict introduced
 * the same way reads as one more of the candidate's own headings, so the reader cannot tell whether
 * they are being told what the design achieves (the interviewee's claim) or what it would actually
 * cost them (the assessment). Reported on the first published scenario; the fix is a different
 * typographic device, not different wording.
 *
 * It is a component and not an admonition for a hard reason: the three attempts live inside a
 * `<details>` reveal, and Docusaurus does not process `:::` directives inside JSX. A component
 * renders there.
 *
 * The label names the speaker. The page establishes an interviewer who holds a rubric written
 * before any answer existed; the verdict is that interviewer's, and saying so is what stops the
 * assessment from being read as the candidate's own summary.
 */
export default function Verdict({
  children,
  /** Overrides the label. Use only where the assessing voice genuinely differs. */
  label = "The interviewer's verdict",
}: {
  children: React.ReactNode;
  label?: string;
}): React.JSX.Element {
  return (
    <aside className={styles.verdict} aria-label={label}>
      <p className={styles.label}>{label}</p>
      <div className={styles.body}>{children}</div>
    </aside>
  );
}
