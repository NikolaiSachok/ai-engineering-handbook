# Evidence ledger — Bringing the loop to an existing codebase

Page: `docs-ai-sdlc/part-1-foundation/existing-codebase.md`

| # | Claim | Grade | Qualifier | Source |
|---|---|---|---|---|
| 1 | Toub calls `dotnet/runtime` "the ultimate brownfield project", with decades of history and millions of lines. | REPORTED | his description of the repository | https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/ |
| 2 | Tracked agent PR success went from 38.1% before the first setup changes to 69% after. | MEASURED | single repository, first-party, March 2026 | https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/ |
| 3 | A 100,000+ line TypeScript platform built with two AI assistants had stopped developing stably. | REPORTED | his own account of a stabilisation he ran, 2026-09-16 | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 4 | Start with an audit if at least three of nine warning signs apply. | ASSERTED | his rule of thumb, not a validated diagnostic | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 5 | The new-chat test: an agent that cannot recall last week's decisions works from its own version. | ASSERTED | his diagnosis | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 6 | Asking AI to rewrite everything properly creates a new project with new problems. | ASSERTED | his argument, 2026-10-09 | https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/ |
| 7 | The audit covered 13 fixed dimensions and ran on several independent models. | REPORTED | his account | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 8 | One model gave the project 4 out of 5; another said operating it was impossible. | REPORTED | his account; his interpretation that each judged something different | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 9 | Start an important check with at least two different models. | ASSERTED | his rule | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 10 | Some payment checks were out of date and some critical checks were greps for a string such as `PAID`. | REPORTED | his account | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 11 | Characterization testing documents a system's actual behaviour, not the behaviour you wish it had. | ASSERTED | Feathers' definition of his own technique (blog, 2016) | https://michaelfeathers.silvrback.com/characterization-testing |
| 12 | The recovery ran in two phases, then a repeat audit found the identified problems fixed. | REPORTED | his account; no duration carried | https://realaillusions.com/ru/materials/ai-project-stabilization-case/ |
| 13 | Context files raised inference cost by over 20% on average. | MEASURED | ETH Zurich; verified against v3 (29 Sep 2026) on 2026-10-21; abstract, §4.2 | https://arxiv.org/abs/2602.11988 |
| 14 | Task-success effects of context files were marginal and not statistically significant either way. | MEASURED | verified against v3 (29 Sep 2026) on 2026-10-21; §4.2, Table 3, §6; v1 reported different numbers | https://arxiv.org/abs/2602.11988 |
| 15 | Omit LLM-generated context files; keep human-written ones to what the README does not already say. | ASSERTED | the authors' recommendation from their results; verified against v3 (29 Sep 2026) on 2026-10-21; §1 | https://arxiv.org/abs/2602.11988 |
| 16 | Chat summaries turned into rules files are generated context files by another route. | ASSERTED | this course's extension of the ETH finding | — |
| 17 | Sixteen experienced developers on mature repositories took 19% longer with AI. | MEASURED | randomised trial, early 2025; METR now marks it out of date | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| 18 | Participants expected a 24% speed-up and afterwards believed AI had sped them up by 20%. | MEASURED | same trial; perception vs measurement | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| 19 | The repositories averaged about 10 years old with over 1,100,000 lines of code. | MEASURED | from the paper | https://arxiv.org/abs/2507.09089 |
| 20 | Developers are likely more sped up now; the data is only very weak evidence for the size. | REPORTED | METR's February 2026 update; selection effects | https://metr.org/blog/2026-02-24-uplift-update/ |
| 21 | In one migration, 80% of code modifications in landed changes were fully AI-authored. | MEASURED | tracked; Google experience report, Google authors | https://arxiv.org/abs/2501.06972 |
| 22 | That migration's engineers estimated total time fell by about 50% versus a similar migration without LLMs. | REPORTED | engineers' self-estimate; experience report, not a study | https://arxiv.org/abs/2501.06972 |
| 23 | Audit ownership sits outside the delivery team, and auditors do not edit what they audit. | ASSERTED | this course's enterprise design | — |
