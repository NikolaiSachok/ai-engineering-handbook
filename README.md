# Enterprise RAG & Agents Handbook

A practical, first-principles guide to production RAG (retrieval-augmented generation)
and agentic systems.

🚧 **Work in progress.** The site is a scaffold — lesson content is being written and
added incrementally.

Built with [Docusaurus](https://docusaurus.io/). Bilingual: **Russian (default)** and
**English**, with Mermaid diagrams and offline local search.

## Run locally

```bash
npm install

# Russian (default locale)
npm run start

# English locale
npm run start -- --locale en
```

Docusaurus dev server serves one locale at a time; use the `--locale` flag to preview EN.

## Build

```bash
npm run build   # builds all locales (ru + en)
```

Output is generated into `build/` and can be served with any static host.

## Structure

- `docs/` — the handbook (Russian, the primary locale). Part I — RAG, Part II — Agents, Glossary.
- `i18n/en/` — the English locale tree (translations of the docs, blog, and theme strings).
- `blog/` — article excerpts and notes (placeholder for now).
