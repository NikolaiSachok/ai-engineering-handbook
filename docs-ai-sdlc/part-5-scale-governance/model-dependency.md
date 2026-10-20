---
title: "The model is a dependency: pinning, upgrades, exit, and data terms"
sidebar_position: 3.5
---

# The model is a dependency, and someone else holds its release schedule

The [cost lesson](./cost-economics/index.md) priced the model; Parts II–III gated its outputs. With a pinned
library, you choose when to upgrade, so tests can run before the change reaches users. A model's signature
can stay identical while its outputs shift on the supplier's schedule. The interface you depend on is
behaviour, which means the API can keep returning 200 while the workflow built on it has already broken.

Access can disappear too. Andrey Beloborodov, a practitioner who writes publicly about AI-first development,
counts blocked accounts among his reasons to use several assistants. In [his write-up](https://realaillusions.com/ru/materials/threads-sovety-ai-praktika/)
(in Russian), he calls the supplier an “unpredictable partner” (translated from Russian, as are his later
quotes here). His assistants share one repository and knowledge base, so when one model misbehaves he moves
to the next editor pane.

## A pin limits what can move

A model ID can identify a fixed **snapshot** or a **moving alias**, whose target the supplier can replace.
Selecting the snapshot in configuration is **model pinning**, which limits alias-driven changes. Record
its ID on each generated change for [agent/model attribution](./enterprise-tier/index.md).

The tables cite supplier pages read in October 2026: dated examples, not a comparison or recommendation.

| Service | Snapshot | Alias |
|---|---|---|
| OpenAI API | Locks a version; pinning recommended because prompting behaviour can change between snapshots. | Movement not stated on these pages. |
| Anthropic API | Weights/configuration fixed for ID's lifetime; from generation 4.6, dateless IDs are snapshots. | Pre-4.6 aliases resolve to the latest dated snapshot for that minor version. |
| Google Gemini API | Stable models usually do not change. | `latest` hot-swaps across stable/preview/experimental releases; breaking changes get two weeks' email notice. |

Sources (read October 2026): OpenAI [model page](https://developers.openai.com/api/docs/models/gpt-4o) and
[reference](https://developers.openai.com/api/reference/overview), undated; Anthropic
[model IDs](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions), undated;
Gemini [models](https://ai.google.dev/gemini-api/docs/models), updated 2026-10-19.

A pin cannot prevent retirement, a supplier routing a deprecated ID to its replacement, or infrastructure
changes. Anthropic's model-ID page says infrastructure updates occasionally produce minor behavioural
differences under unchanged IDs and weights. Its own [incident report](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues)
(September 17, 2025) says a context-window routing bug affected 16% of Sonnet 4 requests at the worst-impacted
hour on August 31. So [production quality signals](../part-4-platform/observability-rollout.md) must stay on
after pinning, because infrastructure can still change outputs.

## Qualify an upgrade against fixed references

In an arXiv paper, [Chen, Zaharia and Zou](https://arxiv.org/abs/2307.09009v3) report a controlled study that
found GPT-4's prime-versus-composite accuracy fell from 84% in March 2023 to 51% in June. Its third revision (October 2023) concludes that the same service can change substantially within a short time.
[Ma, Yang and Kästner](https://arxiv.org/abs/2311.11123) found 10.9% of individual toxicity-detection
predictions regressed from correct to wrong across API updates in a controlled case study. Updates behind
`gpt-3.5-turbo` were unannounced, so developers using that alias could not test them beforehand.

An August 2026 preprint by [Xu and Wu](https://arxiv.org/abs/2608.17719) measured 900 benchmark items
50 times per model across three upgrade pairs. The GPT-5.4 to GPT-5.5 upgrade raised the overall score on the Omni-MATH hard mathematics benchmark by
7.3 percentage points. The same upgrade improved the IFBench instruction-following score overall, but
8.3% of its items reliably regressed: the newer model answered those items correctly less often across
repeated runs, by more than sampling noise could explain under the study's statistical controls. Aggregate scores hid changes in both directions. A search in October 2026 turned up no published measurement of coding-agent regressions after a model
upgrade; these studies concern classification and benchmark tasks.

Before switching, run the candidate through your own harness: **re-qualification** uses past failures and
[escapes promoted into regression cases](../part-3-verification/escape-ledger.md) to check what an upgrade breaks.

1. Hold the [LLM judge](../part-3-verification/layered-gates/index.md) fixed, because upgrading it with the
   generator obscures whether scores rose through better outputs or more lenient judging. Qualify a new
   judge separately against verdicts a human has confirmed.
2. Repeat cases on both versions to distinguish consistent changes from ordinary answer variation.
3. Compare item by item, because improvements elsewhere can hide an **item-level regression** on a case
   that previously passed.
4. Measure first-try success rate `p` on a representative sample of each task class. Regression cases detect
   breakage; representative work estimates `p` without overweighting past failures.
5. Roll out in stages to limit exposure, and revisit [harness assumptions](../part-1-foundation/preparation-over-model.md),
   because the upgrade may make old workarounds unnecessary.

Beloborodov [swaps which model writes and which reviews](https://realaillusions.com/ru/materials/sovety_ai_praktika_part3/)
to see “who has got dumber”. Repeated cases make that informal check inspectable.

:::tip[▶ Video]

<YouTube id="4gC3oueK9Gc" title="Building Trustworthy AI: Avoid Model Drift & Unsafe Outputs — IBM Technology" />

IBM describes output validation, drift monitoring and filters after deployment; read it as the monitoring
that remains necessary after you pin.

:::

## Exit has a deadline

Once retirement is announced, the **deprecation notice period** is your time to qualify and migrate.
Some platforms also **auto-upgrade**, potentially replacing a version before you have qualified its successor.
Published policies distinguish generally available (GA) models from previews:

| Service | Notice | Retirement / upgrade behaviour |
|---|---|---|
| OpenAI API | GA: at least 6 months; specialized: at least 3 months; previews may get much shorter notice, such as 2 weeks; safety/compliance: as much as reasonably possible. | `o3-2025-04-16`: announced 2026-06-11, shutdown 2026-12-11. Automatic replacement not stated. |
| Anthropic API | Publicly released models: at least 60 days; partner platforms set their schedules. | `claude-opus-4-1-20250805`: notified 2026-06-05, retired 2026-08-05. No automatic replacement; retired-model requests fail. |
| Google Gemini API | Stable: advance notice, no minimum; dates are earliest possible dates. Preview: at least two weeks. | Some deprecated stable endpoints automatically route to replacements; shut-down endpoints become unavailable. |
| Microsoft Foundry | GA: at least 60 days; preview: at least 30 days; emergencies can shorten notice. | Standard-family deployments auto-upgrade at retirement; `NoAutoUpgrade` stops them instead. |

Sources (read October 2026): OpenAI [deprecations](https://developers.openai.com/api/docs/deprecations),
undated; Anthropic [deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations),
undated; Gemini [deprecations](https://ai.google.dev/gemini-api/docs/deprecations), updated 2026-10-20,
and models above; Microsoft [retirements](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements),
dated 2026-07-24.

Foundry's `OnceNewDefaultVersionAvailable` setting upgrades Standard-family deployments when a new default
is set. Provisioned deployments are not auto-upgraded; previews are force-upgraded with at least 30 days' notice.

For GA/stable models, the shortest stated minimum here is 60 days, for Anthropic's publicly released
models and Microsoft's GA models; Google states none for stable models, and preview minimums are shorter. Started at the announcement, a qualification and migration that take longer
than your notice period cannot finish before retirement. The only way to fit inside such a short notice period
is to keep qualifying candidates continuously rather than waiting for the announcement.

Suspension can remove that window altogether. Two published clauses show the grounds and notice conditions:

| Service | Suspension / discontinuation |
|---|---|
| Anthropic API | May suspend when it reasonably believes or determines a listed condition applies, including violations, legal prohibition or materially increased service costs; reasonable efforts at written notice. |
| Google Gemini API | May suspend without notice on reasonable belief of a terms violation; may also discontinue APIs or terminate for any reason at any time (§8(a)). |

Sources (read October 2026): Anthropic [commercial terms](https://www.anthropic.com/legal/commercial-terms),
effective 2025-06-17; Google [APIs terms](https://developers.google.com/terms), modified 2021-11-09.

For a **tested exit**, route calls through one client, keep provider and model in configuration, and run an
alternate provider or self-hosted model against regression cases on a schedule. Measure its first-try success
rate separately, because a different fallback model has its own cost per accepted change. Like a
[backup restore](../part-4-platform/environments-migrations-data.md), switching needs rehearsal to expose failures.

## Memory makes the exit usable

In a [separate post](https://realaillusions.com/ru/materials/vibecoding-ai-first-technical-debt/), Beloborodov
writes that context loss is what people most often bring him. The realisation that project knowledge belongs
outside chats sometimes arrives “sharply and painfully”, for example when an account is blocked.

Knowledge held only in chat depends on account access. Keep rules, decisions, architecture notes and
briefs as [project memory](../part-1-foundation/project-memory-and-tiering.md) in repository files or a knowledge
store: this **vendor-portable memory** lets a replacement assistant read them without the old account.

## The account determines the data terms

Paste the company's code into a personal chat and that subscription's consumer terms govern it.
Once prompts leave your machine, **data terms** determine training use, retention and processing location.
A **data processing addendum (DPA)** defines how the supplier processes personal data on your behalf. Ask what the supplier
trains on, how long it keeps data, where it processes it, and which DPA applies, for each service and tier.

Training and retention are separate questions:

| Service | Training use | Retention |
|---|---|---|
| OpenAI API | Excluded unless you opt in. | Abuse logs: up to 30 days unless law requires longer. Responses state: 30 days by default; some stateful endpoints retain until deleted. |
| Anthropic commercial | Excluded by default; feedback/opt-in may permit training. Commercial terms prohibit training on service customer content. | API inputs/outputs deleted within 30 days, with exceptions including ZDR, Usage Policy enforcement and law. |
| Anthropic consumer | Permission required under the update. | Five years for new/resumed chats and coding sessions if you allow training; otherwise existing 30 days. Update excludes commercial services. |
| Google Gemini API | Unpaid: inputs/outputs used for product development/improvement; human review possible. Paid: excluded from product improvement. | Both tiers: prompts, context and outputs retained 55 days for policy enforcement and legal disclosure duties. |
| Google Vertex AI | Excluded without prior permission or instruction. | Cache deleted within 24 hours; can be disabled. Abuse-detection prompt logging possible; period not stated. |
| Microsoft Foundry | Excluded without permission or instruction. | Stateful-feature and uploaded data kept until the customer deletes it; abuse-monitoring store for human review (period not stated). |

Sources (read October 2026): OpenAI [data controls](https://developers.openai.com/api/docs/guides/your-data),
undated, training policy from 2023-03-01; Anthropic [training](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)
(displays 2026-08-18), [retention](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)
(2026-07-01), commercial terms above, [consumer update](https://www.anthropic.com/news/updates-to-our-consumer-terms)
(2025-08-28); Gemini [terms](https://ai.google.dev/gemini-api/terms) (effective 2026-03-23, updated 2026-04-28),
[usage policies](https://ai.google.dev/gemini-api/docs/usage-policies) (2026-06-09); Vertex
[ZDR](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention) (2026-10-15);
Foundry [data privacy](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy) (2026-05-18).

Zero data retention (ZDR) has eligibility and exceptions; check residency independently:

| Service | Zero data retention | Residency / DPA |
|---|---|---|
| OpenAI API | Requires approval and additional requirements; endpoint eligibility varies. Flagged image/file inputs retained for review even under ZDR; some features retain application state. | Regional processing where supported; storage-only regions allow outside-region processing/temporary storage. Non-US residency requires abuse-monitoring approval and Modified Retention amendment. DPA not stated on cited page. |
| Anthropic commercial | Sales arrangement per organization; flagged content may remain up to two years; some models require 30-day retention unless authorized. Feature eligibility varies; stateful features excluded; legal retention possible. | Inference: US-only/global on 4.6+ models; US-only at 1.1x. Storage: US workspace geo. Commercial terms incorporate a DPA. |
| Anthropic consumer | Not stated. | Residency/DPA not stated. |
| Google Gemini API | Not stated. | Paid-tier logged data may be stored transiently/cached in any country with Google/agent facilities; no residency commitment stated. Paid services use processor terms. |
| Google Vertex AI | Customer configuration plus abuse-logging exception; Grounding with Google Search keeps logs up to three days, with no way to disable storage. | At-rest data stays in selected location; jurisdictional/locational endpoints keep ML processing in that jurisdiction. Global endpoint may process anywhere; no residency guarantee. Google's Cloud Data Processing Addendum (CDPA) referenced by the cited ZDR page. |
| Microsoft Foundry | Abuse-monitoring modification available on application. | Processing in the customer-specified geography, except Global/DataZone deployments (processing only); data at rest stays in the customer geography. DPA linked. |

Sources (read October 2026): OpenAI data controls, Anthropic consumer update, Gemini terms, Vertex ZDR and
Foundry data privacy above; Anthropic [ZDR](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)
and [residency](https://platform.claude.com/docs/en/manage-claude/data-residency), undated; Vertex
[residency](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency), 2026-10-15.
DPAs: [Anthropic](https://www.anthropic.com/legal/data-processing-addendum),
[Google processor terms](https://business.safety.google/processorterms/),
[Google Cloud CDPA](https://cloud.google.com/terms/data-processing-addendum), [Microsoft](https://aka.ms/DPA);
document dates not stated on the cited parent pages.

The [secrets](../part-4-platform/secrets.md) and [environments](../part-4-platform/environments-migrations-data.md)
lessons limited what may enter context. For data that reaches the supplier, record the applicable terms, and re-read them when they change.

## Route by the cost of accepted work

A cheaper model wins only if its first-try success rate falls by less than its price does. Half the price
with less than half the success rate costs more per accepted change. That is **routing by break-even**:
`p_cheap / p_expensive > price_cheap / price_expensive`, from the [cost deep dive](./cost-economics/deep-dive.md).
Measure `p` per task class on representative work, and include human review of failed attempts because it
can dominate the bill. Self-hosting for data requirements is an independent reason to choose a route,
whatever the break-even says. Each additional route also adds a model to pin, a lifecycle to track and terms to read.

:::tip[▶ Video]

<YouTube id="pePAAGfh-IU" title="How to Pick the Right AI Foundation Model — IBM Technology" />

Martin Keen presents six steps for model selection and the costs of a wrong choice; apply that selection
process to each task class you route.

:::

## The three tiers — soloist · small-team · enterprise

The invariant: **pin the version you run, qualify every change to it, and prove you can leave.**

- **Soloist.** Pin the model in configuration, keep project memory in the repository, rerun past failures
  before upgrading, and check notice periods and account terms. *The failure it prevents:* a suspended
  account taking project context with it, or an alias moving to a model you never tested.
- **Small-team.** Route every model call through one client, qualify upgrades with repeated runs, exercise the fallback regularly,
  measure first-try success per task class, and record each service's data commitments. *The failure it prevents:*
  learning about retirement from production errors, or shipping an upgrade whose higher average hid broken cases.
- **Enterprise.** Keep version, provider, region, terms, notice and owner in the model inventory; secure DPA,
  residency and retention commitments; retain qualification and exit evidence. *The failure it prevents:*
  a customer asking where data went and which model produced a change, with nobody able to answer.

## What to take away

- Pinning limits alias-driven changes; retirement, replacement routing and infrastructure remain outside it.
  Keep attribution and quality monitoring in place.
- **Hold the judge fixed** so a more lenient judge cannot masquerade as a better generator.
- Past failures detect regressions, while representative work estimates the `p` routing needs; keep both.
- **Exercise the exit and keep repository memory.** Suspension can strand chat memory; retirement strands
  workflows without a qualified replacement.
- Data commitments depend on the account's service tier, so record its terms and their date.
- Include the human review that failed attempts consume in routing costs, because cheaper tokens can consume more human capacity.

**[New terms](../glossary.md#the-model-is-a-dependency-pinning-upgrades-exit-and-data-terms)**: model snapshot vs moving alias; model pinning; re-qualification (of a model upgrade); item-level regression; deprecation notice period; auto-upgrade; tested exit (fallback provider); vendor-portable memory; data terms (training use, retention, zero data retention, residency, DPA); routing by break-even.
