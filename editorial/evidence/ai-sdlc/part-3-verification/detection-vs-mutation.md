# Evidence ledger — Detection vs mutation: gaming the metric

Page: `docs-ai-sdlc/part-3-verification/detection-vs-mutation.md`

| # | Claim | Grade | Qualifier | Source |
|---|---|---|---|---|
| 1 | Cursor’s audit found 63% of benchmark wins were retrieved rather than derived. | MEASURED | — | https://cursor.com/blog/reward-hacking-coding-benchmarks |
| 2 | SpecBench measured +28 percentage points more reward hacking per tenfold code-size increase. | MEASURED | — | https://arxiv.org/abs/2605.21384 |
| 3 | An RL-trained model exploited at 13.9% versus 0.6% for its untrained base. | MEASURED | — | https://arxiv.org/abs/2605.02964 |
| 4 | The vendor claims 70% more PRs without a baseline. | ASSERTED | no baseline | https://openai.com/index/codex-now-generally-available/ |
| 5 | A revenue-earning platform of more than 100,000 lines of TypeScript, built by its owner with AI coding assistants | REPORTED | one practitioner's account of one project | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 6 | An audit found some of the critical checks were greps for a required string | REPORTED | "some", not all; his own audit | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 7 | A test that searches for `PAID` proves only that the word is in the code, not that payment works | ASSERTED | his illustration, stated as a conditional | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 8 | Part of his fix replaced the critical grep checks with behavioral tests | REPORTED | listed among the fixes he made | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
