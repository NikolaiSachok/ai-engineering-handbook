# Canon

Per-language canons for the handbook's prose — terms, register, kept-English tokens — one directory
per target language:

- [`ru/`](ru/) — Russian
- [`sk/`](sk/) — Slovak
- [`de/`](de/) — German (**bootstrap**). The locale is wired as an *unreleased* locale (built and
  link-gated in CI, absent from the deployed dropdown). The canon mirrors the Slovak canon's *shape*
  but inverts its central decision: German practitioner prose keeps most terms **English with a German
  article**, so the kept-EN register is several times larger and the "an anglicism is a defect" gate is
  deliberately **not** ported. Adds two sections the Slavic canons have no need for:
  gender/plural/genitive for every kept-EN noun, and Denglisch verb morphology. Rows carry honesty
  tokens — a term marked OPEN is **not** settled; do not translate against it.

**The infographic canon is cross-language and lives outside this directory:**
[`editorial/infographics/STYLE.md`](../infographics/STYLE.md) — palette, dimensions, naming and
embedding for both card substrates, plus the badge lexicon, the `rank` ordering ramp, the connector
vocabulary, the icon register with its blind-naming verdicts, and the sizing grid. Icon provenance
and licensing sit with the assets, in `src/components/InfoCard/icons/NOTICE.md`.
