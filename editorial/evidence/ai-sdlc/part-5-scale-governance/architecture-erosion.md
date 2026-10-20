# Evidence ledger — Architecture erosion

Page: `docs-ai-sdlc/part-5-scale-governance/architecture-erosion.md`

| # | Claim | Grade | Qualifier | Source |
|---|---|---|---|---|
| 1 | Perry and Wolf named architectural drift and architectural erosion in 1992. | ASSERTED | a definition, ACM SIGSOFT SEN 17(4), October 1992 | https://users.ece.utexas.edu/~perry/work/papers/swa-sen.pdf |
| 2 | Drift makes the architecture less coherent and harder to see, so it is easier to violate. | ASSERTED | Perry and Wolf's argument, not a measurement | https://users.ece.utexas.edu/~perry/work/papers/swa-sen.pdf |
| 3 | Small fixes skip the architecture check; after a few dozen the project lives by different rules. | REPORTED | one practitioner, his own projects, 2026-10-09 | https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/ |
| 4 | One agent changes a contract, another builds a parallel implementation, another documents the workaround. | REPORTED | one practitioner, his own projects | https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/ |
| 5 | 22%–33% of resolved bugs involved more than one fix attempt. | MEASURED | Eclipse JDT core, Eclipse SWT, Mozilla; MSR 2012; human developers | https://web.cs.ucla.edu/~miryung/Publications/msr2012-supplementarypatch.pdf |
| 6 | In the two Eclipse projects, 14%–15% of supplementary-patch files lay outside the initial patch's neighbours. | MEASURED | JDT 15%, SWT 14%; no Mozilla figure | https://web.cs.ucla.edu/~miryung/Publications/msr2012-supplementarypatch.pdf |
| 7 | An ADR log in every agent's settings, consulted by every brief and bug fix, on a 10–20-person-scale project. | REPORTED | one practitioner, his own project, 2026-08-17 | https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/ |
| 8 | Exceptions and wrong programming decisions fell severalfold; he gives no figure. | REPORTED | no number given; not a measurement | https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/ |
| 9 | The extra layer of agent work was smaller than it might sound. | REPORTED | his own assessment | https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/ |
| 10 | Record the decision first, then change the system. | ASSERTED | his rule | https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/ |
| 11 | ADR sections Title, Context, Decision, Status, Consequences; a reversed decision is kept and marked superseded. | ASSERTED | Nygard's 2011 pattern, a convention | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions |
| 12 | A fitness function is an objective assessment of architectural integrity, from tests, metrics and monitors. | ASSERTED | definition attributed to Ford, Parsons and Kua's book | https://www.thoughtworks.com/radar/techniques/architectural-fitness-function |
| 13 | Architecture fitness harness: guides and sensors checking architectural characteristics; ArchUnit hook example. | ASSERTED | practitioner framing, April 2026 | https://martinfowler.com/articles/harness-engineering.html |
| 14 | Semantic judgement by LLM review is expensive and probabilistic. | ASSERTED | her framing | https://martinfowler.com/articles/harness-engineering.html |
| 15 | FreezingArchRule stores existing violations on the first run and reports only new ones. | ASSERTED | tool documentation | https://www.archunit.org/userguide/html/000_Index.html |
| 16 | Import Linter contract types include forbidden, protected, layers and independence; checked by lint-imports. | ASSERTED | tool documentation | https://import-linter.readthedocs.io/en/stable/ |
| 17 | dependency-cruiser validates dependencies against your rules; --init adds circular-dependency rules. | ASSERTED | tool documentation | https://github.com/sverweij/dependency-cruiser |
| 18 | Super-Linter and MegaLinter run jscpd with threshold 0 by default, failing on any duplication. | ASSERTED | per jscpd's documentation; linters' own defaults not checked | https://github.com/kucherenko/jscpd |
| 19 | Duplication change in agent-first repos was not significant; complexity and warnings rose significantly. | MEASURED | matched difference-in-differences, graded in Reading the evidence | https://arxiv.org/abs/2601.13597 |
| 20 | State YAGNI, KISS, SRP and DRY explicitly, because "follow best practices" does not reliably work. | ASSERTED | his recommendation | https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/ |
| 21 | Three consecutive fixes on fixes means it is time to redesign. | ASSERTED | his heuristic; nobody has measured the threshold | https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/ |
| 22 | Asking an agent to rewrite everything properly produces a new project with new problems. | ASSERTED | his warning | https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/ |
