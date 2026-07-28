# AI Engineering Handbook

A hub of first-principles courses on production AI engineering. Two courses ship today,
each complete and each available in every language the site ships in:

- **RAG & Agents** (`/rag-agents`) — production RAG (retrieval-augmented generation) and
  agentic systems: ingestion, retrieval, generation, agents, plus the eval, guardrails and
  LLMOps that keep them honest. Part I — RAG, Part II — Agents, Part III — Production & LLMOps.
- **AI SDLC** (`/ai-sdlc`) — the AI-assisted software development lifecycle: planning,
  building, reviewing and shipping when AI agents are part of the team. Parts I–V, plus
  optional deep-dives.

Alongside them, **Field notes** (`/blog`) is the making-of: dated, first-person notes on
building this handbook *using* the SDLC it teaches. Deliberately English-only — see the
standing note on the blog index for why.

Built with [Docusaurus](https://docusaurus.io/). It ships in **English** (default, served
at the site root), **Russian** (`/ru/`) and **Slovak** (`/sk/`) — with Mermaid diagrams and
offline local search in every locale.

## Run locally

```bash
npm install

# English (default locale)
npm run start

# Another locale
npm run start -- --locale ru
```

Docusaurus dev server serves one locale at a time; use the `--locale` flag to preview the others.

## Build

```bash
npm run build                                  # every released locale
HANDBOOK_INCLUDE_UNRELEASED=1 npm run build    # …plus the gated ones CI validates
```

Output is generated into `build/` and can be served with any static host.

## Structure

- `docs/` — the **RAG & Agents** course in English, the canonical locale. It is the default
  docs instance, served at `/rag-agents`.
- `docs-ai-sdlc/` — the **AI SDLC** course in English, its own docs instance, served at `/ai-sdlc`.
- `blog/` — the English-only **Field notes** blog, served at `/blog`.
- `src/pages/index.tsx` — the landing hub. Its course cards derive from the `COURSES` array in
  `docusaurus.config.ts`, the single source of truth the navbar, footer and search index also read.
- `i18n/<locale>/` — one tree per non-default locale (docs + theme strings), served at `/<locale>/`:
  Russian at `/ru/` and Slovak at `/sk/` today. Every one of them is audience-primary: written natively,
  never machine-translated.
- `editorial/` — the style canon: a thin cross-language router (`style-canon.md`) plus a per-language folder
  `canon/<lang>/`, each holding the shared course-independent language rules (`_language.md`) and one
  per-course term ledger (`rag.md`, `ai-sdlc.md`, …).

## Contributing / workflow

The handbook follows a small, real SDLC (kept proportionate to a docs site):

- **Trunk-based, PR-only.** `main` is always deployable and auto-deploys to GitHub Pages.
  All changes land via a short-lived branch + Pull Request — no direct pushes to `main`.
- **Conventional Commits** for messages (`docs:`, `feat:`, `fix:`, `chore:`, `ci:`) and PR
  titles. PRs are **squash-merged**.
- **CI gates every PR.** The jobs are listed here under the exact names GitHub reports them by —
  those strings are what branch protection matches on, so this table is the one to copy into
  *Settings → Branches → main → Require status checks*, and the one place the gate list is kept
  (`CLAUDE.md` points here rather than holding a second copy):

  | job name in CI | what it runs | what it catches |
  |---|---|---|
  | `Build (both locales)` | `npm run build` for **every** locale | dead internal links (`onBrokenLinks: 'throw'`), a broken i18n tree |
  | `Markdown lint` | `npm run lint:md` | structure/format hygiene |
  | `Generic leak scan` | `npm run leak-scan` | secrets, credentials, local paths, emails |
  | `Icon register drift check` | `scripts/icon-register-check.sh` | infographic icons drifting from the register |
  | `Locale structural parity` | `scripts/locale-parity-check.sh` | a translated page losing sections, figures or card nodes; a sidebar category with no translation key; a released locale missing a whole course |

  The `Build (both locales)` job name is **stale** — it builds every released locale plus the gated
  ones, which is four today, not two. It is left as-is deliberately: if branch protection requires
  checks by name, renaming the job silently stops satisfying the requirement, so the rename and the
  branch-protection update have to land together.

  **Are these actually *required*, or only *reported*? Unverified — treat it as an open
  question.** Reading `repos/…/branches/main/protection` needs repo-admin scope that the tokens in
  use here don't have (it `403`s), so nobody has checked the setting. Every phrasing anyone has
  written for it — "requires", "should require" — is `ASSERTED` in the handbook's own grading
  vocabulary, not `MEASURED`: an instruction file records intent, and intent is not evidence.
  `CLAUDE.md` records the same open question, worded to agree with this one. Anyone with settings
  access can settle it in a minute by comparing the job names above against *Settings → Branches →
  main → Require status checks*, and both documents should then be reconciled to whatever turns out
  to be true. It matters because advisory and required look identical on a green PR and differ
  entirely on a red one.
- **Content PRs** additionally require a **literary-edit pass per language, independently**
  (see the editorial standard in `CLAUDE.md`) — enforced via the PR-template checklist.
- **Issues & milestones** are the planning surface: issues track lessons/topics; a milestone
  is a Part of a course; labels `lesson` / `editorial` / `infra` / `chore`.

### Enable the pre-commit hook (once per clone)

A local pre-commit hook mirrors the generic leak scan so leaks are caught before they're
committed. No extra toolchain — enable it with:

```bash
git config core.hooksPath .githooks
```
