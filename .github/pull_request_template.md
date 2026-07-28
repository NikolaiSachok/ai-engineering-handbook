<!--
Conventional-Commit PR title, e.g.:
  docs: add reranking lesson (Part I)
  feat: enable offline search
  ci: add build+lint+leak-scan gates
Squash-merge keeps `main` history clean.
-->

## Summary

<!-- What this PR changes and why. Link issues: Closes #NN -->

## Type

- [ ] `docs` — handbook content (lesson/topic/glossary)
- [ ] `feat` / `fix` — site behavior
- [ ] `ci` / `chore` / `infra` — tooling, workflow, config

## Gates

- [ ] `HANDBOOK_INCLUDE_UNRELEASED=1 npm run build` passes for **every** locale (en + ru + sk, plus
      any gated locale)
- [ ] Markdown lint passes (`npm run lint:md`)
- [ ] Generic leak scan passes (`npm run leak-scan`)
- [ ] Locale structural parity passes (`bash scripts/locale-parity-check.sh`)
- [ ] Icon register drift check passes (`bash scripts/icon-register-check.sh`)
- [ ] Internal links valid (the build's `onBrokenLinks: 'throw'` confirms this)
- [ ] PR title follows **Conventional Commits**

## Content PRs only

- [ ] Literary-edit pass done **for EACH language independently** (every locale the page ships in,
      not just English) — no calques, idiomatic prose, technical meaning preserved exactly
- [ ] New terms added to the Glossary **and** to that language's canon ledger in `editorial/canon/`
- [ ] Any new sidebar category has a translation key in every locale's `current.json`
      (`Locale structural parity` enforces this)
- [ ] General / vendor-neutral only — no confidential, employer-internal, or client-specific material
