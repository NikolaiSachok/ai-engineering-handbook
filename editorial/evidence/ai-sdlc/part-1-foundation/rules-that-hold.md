# Evidence ledger — Rules that hold

Page: `docs-ai-sdlc/part-1-foundation/rules-that-hold.md`

| # | Claim | Grade | Qualifier | Source |
|---|---|---|---|---|
| 1 | Hooks are deterministic and guarantee the action happens. | ASSERTED | vendor | https://code.claude.com/docs/en/best-practices |
| 2 | Böckeler repeatedly had to ask agents why they had not run sensors checks. | REPORTED | her own practice | https://martinfowler.com/articles/sensors-for-coding-agents.html |
| 3 | A Replit agent deleted a production database during an explicit code freeze in July 2025. | REPORTED | — | https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/ |
| 4 | Meta’s March 2026 incident produced a roughly two-hour data exposure. | REPORTED | Meta internal incident report, as described to The Information | https://techcrunch.com/2026/03/18/meta-is-having-trouble-with-rogue-ai-agents/ |
| 5 | In Meta’s March 2026 incident, the agent acted without asking the engineer for permission. | REPORTED | — | https://techcrunch.com/2026/03/18/meta-is-having-trouble-with-rogue-ai-agents/ |
| 6 | The Nx campaign ran local AI CLIs through their own permission-bypass flags. | REPORTED | Snyk analysis | https://snyk.io/blog/weaponizing-ai-coding-agents-for-malware-in-the-nx-malicious-package/ |
| 7 | GitGuardian counted 2,349 distinct secrets across 1,079 attacker-created exfiltration repositories. | MEASURED | snapshot of 27 August 2025 | https://blog.gitguardian.com/the-nx-s1ngularity-attack-inside-the-credential-leak/ |
| 8 | An agent deleted and rebuilt a production environment; a multi-hour outage followed, with causation disputed. | REPORTED | — | https://www.theregister.com/2026/02/20/amazon_denies_kiro_agentic_ai_behind_outage/ |
| 9 | Independent measured results converge on agents optimizing the thing checked. | MEASURED | — | — |
| 10 | A skill is advice; a hook executes regardless of what the model decides. | ASSERTED | — | — |
| 11 | An audit of 11,000 lines found no staleness mechanism of any kind. | MEASURED | from that audit | — |
