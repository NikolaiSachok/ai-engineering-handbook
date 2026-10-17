---
title: Safety on the platform
sidebar_position: 3
last_verified: 2026-10-17
---

# A filtered completion needs an application response

A document Q&A service can retrieve the right passage and still return something it should withhold.
The question may request harmful content; a retrieved page may contain instructions aimed at the model;
the answer may reproduce protected material. These failures happen at different points. Checking only
the user's question leaves the retrieved context and generated answer outside the check.

Filtering also changes the API contract. A model call can end without a usable answer, even when the
HTTP request succeeds. If your API turns that into an empty answer with citations, the caller cannot
distinguish a safety block from missing evidence. You need to know which checks the deployment applies,
what their signals mean, and how to turn a blocked generation into a clear reply.

## How it works on Azure \{#how-it-works-on-azure}

Microsoft Foundry groups safety controls into a named guardrail. Each control identifies a risk,
the point at which to inspect content, and an action such as annotating or blocking. For model
deployments, the relevant points are input and output. The
[guardrails overview](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview)
separately marks agent guardrails, including tool-call and tool-response inspection, as **preview**.
P1 calls a model deployment from its own API; it does not acquire those agent controls by doing so.

The configuration is represented by a responsible AI policy, or **RAI policy**. A deployment's
[`raiPolicyName`](https://learn.microsoft.com/en-us/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts/deployments)
identifies its policy. Creating a custom policy and attaching it to the deployment are separate steps.
Inspect the attachment when diagnosing behaviour; a policy saved elsewhere in the resource does not
establish which settings the chat deployment uses.

The core content classifiers cover hate, sexual content, violence and self-harm. Each category has
safe, low, medium and high severity; safe is annotated but cannot be configured for blocking.
These are [classification levels](https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/concepts/content-filter),
not a confidence score or an application permission. The
[default Medium blocking level](https://learn.microsoft.com/en-us/azure/foundry/guardrails/default-safety-policies)
blocks medium- and high-severity content on input and output. Classifiers can make both kinds of error:
blocking acceptable content and allowing content you wanted withheld.

Other detectors answer different questions. [Prompt Shields](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields)
look for attempts to redirect the model: a direct attack arrives through a user prompt; an indirect
attack is embedded in document content. A retrieved passage that instructs the assistant to abandon
the question belongs to the second case. User-prompt attack detection is enabled by default;
document-attack detection is off by default and must be enabled. The returned `detected` and `filtered`
flags distinguish finding an attack from actually blocking it.

For document checks, the application must also identify its retrieved passages using the
[document delimiters and JSON escaping](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#embedding-documents-in-your-prompt)
specified by the service. Treat that formatting as part of the integration contract. Adding a detector
to the policy does not prove that arbitrarily concatenated Search results are being inspected as documents.

Illustrative message fragment, not a runnable request: escape document quotes, then JSON-serialise the message.

```json
{
  "role": "user",
  "content": "When does it open? \"\"\" <documents>\nHours: \\\"09:00\\\".\n</documents> \"\"\""
}
```

Before implementing P1, check the selected inference **data-plane API version** against the
[annotation compatibility matrix](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#api-version-compatibility)
and verify the supported annotations. Indirect-attack annotations vary by version. The lab's ARM
`2025-06-01` versions management reads, not inference; it establishes no annotation support.

## Choosing controls and thresholds \{#choosing-and-tradeoffs}

Keep the question each control answers visible when choosing it. A harmful-content classifier cannot
tell you whether a cited passage supports an answer, and a supported answer can still contain material
your service should withhold.

| Control | What it examines | When it helps | When it is insufficient |
|---|---|---|---|
| Core content filters | Harm category and severity on input/output. | A shared content policy across model calls. | Document permissions, citation correctness or your application's allowed topics. |
| Prompt Shields | Attempts to override instructions through prompts or documents. | P1 reads text from outside the application. | Authorising access to data or guaranteeing resistance to every attack. |
| Groundedness detection — preview | Whether an answer is supported by supplied sources. | Source-bound Q&A and summaries. | Determining whether the sources themselves are true or current. |
| Protected-material detection | Output matching known protected text or code. | Reducing reproduction of indexed material. | Establishing complete coverage of everything you ingest or generate. |

There is a naming trap in the current configuration surfaces. The
[portal's blocking level](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview#blocking-levels)
describes strictness: Low blocks high severity only; Medium blocks medium and high; High blocks low,
medium and high. In the
[ARM policy schema](https://learn.microsoft.com/en-us/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01),
`severityThreshold` describes the classified severity at which blocking starts. A threshold of Low
therefore means stricter filtering. Record the actual severities blocked, rather than copying “Low”
between interfaces. Turning off core output filtering requires approval for modified guardrails.

Use the default as P1's starting point, then evaluate representative questions and passages before
changing it. An educational document may legitimately discuss a sensitive subject. If that is blocked,
inspect the category, stage and configured threshold before relaxing anything. Changing every category
to solve one false positive makes the effect of the change difficult to assess.

The deployment's [groundedness control is preview](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview#risk-applicability).
The [configuration guide](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#annotations)
currently limits it to streaming scenarios; do not plan to enable it on P1's initial non-streaming path.
Its [source-comparison mechanism](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-groundedness)
also explains its boundary: agreement with an obsolete document can still produce an obsolete answer.
Evaluate retrieval and citations separately.

[Protected-material detection](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-protected-material)
checks known text and code, with English-only support. The documented code index is current only
through **6 April 2023**. For P1, that is a concrete reason to retain source provenance and an ingestion
policy even when detection is enabled. Keep deployment controls distinct from standalone Content Safety
APIs: the [release notes](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/whats-new)
list the Prompt Shields and protected-text APIs as GA, and the protected-code API as **preview**.
One surface's release status does not establish another's.

## In an AI workload \{#in-an-ai-workload}

P1's minimal API will retrieve public passages from Azure AI Search and ask its Foundry chat deployment
for an answer with citations. Publicly readable documents can still contain hostile instructions.
The [application guardrails lesson](/rag-agents/part-1-rag/cross-cutting/guardrails/) owns the broader
defences; here the task is to consume the deployment's safety result correctly. Identity, retrieval
permissions, secret handling and tool authorisation remain application and infrastructure responsibilities.

For this step, choose a buffered, non-streaming **Chat Completions** path. Azure documents
[filtering outcomes](https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/concepts/content-filter#content-filtering-scenarios):
a blocked prompt returns HTTP 400 with a structured `content_filter` error; a filtered completion can
arrive in HTTP 200 with `finish_reason: content_filter`. Partial text can exist. Also check
[`content_filter_results.error`](https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/concepts/content-filter#scenario-6-content-filtering-system-unavailable):
filtering can fail while generation returns HTTP 200, with an error such as `content_filter_error`.
Check both signals before releasing text or citations. These signals belong to this
API surface; do not assume a different model API has the same envelope.

Give P1 an explicit mapping using ASP.NET Core's
[ProblemDetails support](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0).
The following is the proposed application contract, not an automatic Azure translation or an
implemented handler:

| Provider result | P1 reply before response headers are sent |
|---|---|
| HTTP 400 whose structured error code identifies `content_filter` | HTTP 422, `application/problem+json`; withhold the answer. |
| HTTP 200 with the selected completion's `finish_reason` equal to `content_filter` | The same HTTP 422 problem; discard any partial answer and citations. |
| HTTP 200 with `content_filter_results.error`, including `content_filter_error` | HTTP 503, `application/problem+json`, `code: safety_unavailable`; withhold the answer and citations. |
| Another HTTP 400 | Follow the separate provider-error path; do not label every bad request a safety block. |

For either filtered case, set `status` to 422, `title` to “Answer blocked by safety policy” and
`detail` to “The model request or response was blocked by the configured safety policy.” Add the
application extension `code: safety_filtered` and a `traceId` for support. That message avoids blaming
the user when a retrieved passage or generated response caused the block. The client can offer a
revised question without displaying the withheld text.

For failed filter execution, P1 chooses to withhold the answer: set `status` to 503, `title` to
“Safety check unavailable”, `detail` to “The answer was withheld because the safety check could not
complete.”, `code` to `safety_unavailable`, and include `traceId`. This is P1's availability decision;
Azure does not mandate that HTTP status. No policy block was established.

Do not automatically retry the same blocked generation or route it to a less restrictive deployment.
Record the deployment, policy, filtering stage and category when available in Application Insights,
with the request trace. Log failed filter execution as `safety_unavailable`, retaining the provider
error code separately from `safety_filtered`. Keep raw questions, passages and withheld completions
out of routine logs. Distinguish these outcomes from successful answers and empty retrieval.

Streaming changes the response contract again. With
[Asynchronous Filter](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-streaming),
tokens can arrive before their filtering signal. After your API has sent response headers and text,
it cannot replace that response with an HTTP ProblemDetails reply. A streaming version needs an explicit
terminal event and client behaviour for incomplete or withdrawn content. Keep P1 buffered until that
contract is designed; the [serving lesson](/rag-agents/part-3-production/serving/) covers the application mechanics.

## Try it \{#try-it}

Inspect the filter attached to P1's chat deployment from
[the previous lesson](./deployments-quotas-cost.md#try-it). You need Azure CLI, a subscription containing
that deployment, and permission to read the account, deployment and policy. This step changes no settings.

These commands were checked against the live CLI reference on 2026-10-17 and have **not yet been run
against a live subscription**. No subscription is available for this course yet. The expected results
below come from the documented management APIs, not observed execution.

In Bash, replace the first three values, then use
[`az login`](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) and
[`az account set`](https://learn.microsoft.com/en-us/cli/azure/account#az-account-set):

```bash
P1_SUBSCRIPTION='your-subscription-id'
P1_RESOURCE_GROUP='your-p1-resource-group'
P1_FOUNDRY='your-p1-foundry-resource'
P1_CHAT='p1-chat-lab'

az login
az account set --subscription "$P1_SUBSCRIPTION"
```

Read the deployment with the core
[`deployment show`](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-show)
command. Stop on any CLI error rather than treating missing output as a safety setting.

```bash
az cognitiveservices account deployment show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_CHAT" --output json

P1_POLICY=$(az cognitiveservices account deployment show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_CHAT" \
  --query properties.raiPolicyName --output tsv)

P1_ACCOUNT_ID=$(az cognitiveservices account show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --query id --output tsv)
```

The [account command](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account#az-cognitiveservices-account-show)
supplies the resource ID. If the deployment reports a policy name, inspect it using
[`az rest`](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-rest) and the stable
[RAI policy GET API, version 2025-06-01](https://learn.microsoft.com/en-us/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01):

```bash
if [[ -n "$P1_POLICY" && -n "$P1_ACCOUNT_ID" ]]; then
  az rest --method get \
    --url "https://management.azure.com${P1_ACCOUNT_ID}/raiPolicies/${P1_POLICY}?api-version=2025-06-01" \
    --output json
fi
```

Expect a deployment record and, for a retrievable named policy, its configuration. Inspect
`basePolicyName`, `mode` and each `contentFilters` entry's `name`, `source`, `enabled`, `blocking`
and applicable `severityThreshold`.

This subset of the [GET documentation's sample](https://learn.microsoft.com/en-us/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01)
is documentation-derived, not observed P1 output or recommended settings:

```json
[
  {"name": "Hate", "source": "Prompt", "enabled": false,
   "blocking": false, "severityThreshold": "High"},
  {"name": "Hate", "source": "Completion", "enabled": true,
   "blocking": true, "severityThreshold": "Medium"}
]
```

`name` identifies the detector; `Prompt` means input, `Completion` output. Here the input detector is
disabled, so its High threshold does not establish blocking. The output detector runs and blocks
medium/high severity. Read `enabled` and `blocking` before severity: enabled with blocking false
means annotation without blocking.

Confirm inherited/default settings in the [Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#assign-a-guardrail):
open **Build → Models**, select P1's model and inspect its Guardrails panel to confirm assignment.
Under **Build → Guardrails**, inspect the named guardrail's controls; compare `basePolicyName` with
the [documented defaults](https://learn.microsoft.com/en-us/azure/foundry/guardrails/default-safety-policies).
Default guardrails are read-only. If permissions, an incomplete management response or missing portal
detail prevent confirming an effective setting, record **unresolved**. Empty values or failed GETs
do not mean disabled filtering.

Record which severities are blocked on input and output, whether document-attack detection is enabled,
and the protected-material settings. Keep the policy name with P1's deployment configuration so the
later Bicep definition can preserve the choice. This inspection establishes configuration, not detection
accuracy. Retain four API acceptance cases: filtered input, filtered output, HTTP 200 with
`content_filter_results.error` (`content_filter_error`) despite a normal finish reason, and an
unrelated provider 400. Only the two blocks produce `safety_filtered`; failed execution produces
503 `safety_unavailable`. All three withhold answers/citations; the unrelated 400 follows its separate path.

**Cost:** This inspection is free of additional model or safety-analysis usage: it only reads management
configuration and creates no resources or inference requests. Existing P1 resources continue to incur
their own charges.

**Teardown:** None for this step. It creates no Azure resources and changes no policy. Keep the existing
deployment for the next P1 exercise, or use its creating lesson's teardown when ending the lab.

## What to take away \{#what-to-take-away}

- Inspect the policy attached to the chat deployment. A saved policy alone does not establish coverage.
- Record the severities actually blocked; portal blocking level and ARM severity threshold run in opposite directions.
- Enable and integrate document-attack detection deliberately. Retrieved public text is still untrusted input.
- Map input/output blocks and failed filter execution to distinct application outcomes before releasing an answer.
- Keep platform detection alongside application controls, source validation and evaluation; each checks a different failure.

**[New terms](../glossary.md#platform-safety)**: content filter, severity level, severity threshold, blocking level, annotation, Prompt Shields, direct prompt attack, indirect prompt attack, groundedness detection, protected-material detection, RAI policy.

## Sources \{#sources}

Verified as of 2026-10-17.

Response-failure handling, API compatibility and inspection examples rechecked on 2026-10-18.

- **Controls and configuration:** [Guardrails overview](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview), [Default safety policies](https://learn.microsoft.com/en-us/azure/foundry/guardrails/default-safety-policies), [Content filtering and response scenarios](https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/concepts/content-filter), [Configure guardrails and document formatting](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails).
- **Specialised detection:** [Prompt Shields](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields), [Groundedness detection](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-groundedness), [Protected-material detection](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-protected-material), [Content Safety release notes](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/whats-new).
- **Response handling:** [Content streaming](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-streaming), [ASP.NET Core API errors and ProblemDetails](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0).
- **Management schema and CLI:** [Deployment schema, 2025-06-01](https://learn.microsoft.com/en-us/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts/deployments), [RAI policy GET, 2025-06-01](https://learn.microsoft.com/en-us/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01), [Deployment show](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-show), [Account show](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account#az-cognitiveservices-account-show), [Login and REST](https://learn.microsoft.com/en-us/cli/azure/reference-index), [Select subscription](https://learn.microsoft.com/en-us/cli/azure/account#az-account-set).
