# AI-SDLC evidence ledgers

These ledgers are the audit layer for the course’s evidence grades.
The reader layer carries each grade in the wording, as Lesson 2 prescribes.
Each ledger mirrors its page’s relative path beneath `docs-ai-sdlc/`.
Its title is `# Evidence ledger — <page title>`, followed by `Page: ` and the page path in backticks.
The table columns are `#`, `Claim`, `Grade`, `Qualifier`, and `Source`.
Rows follow page order; each claim summary is at most 20 words and preserves any quoted numbers exactly.
Grades are MEASURED, REPORTED, ASSERTED, or UNKNOWN; an absent qualifier or source is `—`.
Source URLs are copied verbatim from the page and separated by `<br>` when there are several.
Add a row in the same PR as any new graded claim; keep existing rows aligned with their claims.
`scripts/evidence-ledger-check.py` enforces the format and guards against grade tokens in the reader layer.
