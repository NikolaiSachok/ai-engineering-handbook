# Evidence ledger — Observability, rollout, and the kill switch

Page: `docs-ai-sdlc/part-4-platform/observability-rollout.md`

| # | Claim | Grade | Qualifier | Source |
|---|---|---|---|---|
| 1 | Beloborodov estimates almost no vibe-coded projects have working observability. | ASSERTED | his estimate | https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/ |
| 2 | None of Beloborodov's clients had observability properly solved. | REPORTED | his own client work | https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/ |
| 3 | The difficult part is deciding what "good" means where engineering meets the business. | ASSERTED | his argument | https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/ |
| 4 | A system that is down emits no data at all. | ASSERTED | his observation; dashboard consequence is the course's inference | https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/ |
| 5 | Black-box monitoring is symptom-oriented; white-box monitoring sees imminent problems. | REPORTED | Google's account of its own practice | https://sre.google/sre-book/monitoring-distributed-systems/ |
| 6 | Page on actionable symptoms; frequent pages train people to ignore real failures. | REPORTED | Google's recommendation from its own practice | https://sre.google/sre-book/monitoring-distributed-systems/ |
| 7 | Set up a tracked way to report a problem on every page before the first release. | ASSERTED | his recommendation | https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/ |
| 8 | Scientist returns the control's result, runs and compares the candidate, records timing and exceptions. | REPORTED | the library's documented behaviour | https://github.com/github/scientist |
| 9 | Beloborodov's deduplication pipeline is in shadow verification, not yet claimed in client reports. | REPORTED | his own project, current state | https://realaillusions.com/ru/projects/cyprus-real-estate-project/ |
| 10 | DORA’s 2025 self-reported survey finds a negative relationship between AI adoption and delivery stability. | MEASURED | self-reported survey; measured only in the weak sense | https://dora.dev/dora-report-2025/ |
| 11 | Keep deploy scripts in version control, re-runnable, with a record of who deployed what. | ASSERTED | his recommendation | https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/ |
| 12 | In his process the AI deploys to test; he deploys production himself, because of secrets. | REPORTED | his own process | https://realaillusions.com/ru/materials/sovety_ai_praktika_part4/ |
