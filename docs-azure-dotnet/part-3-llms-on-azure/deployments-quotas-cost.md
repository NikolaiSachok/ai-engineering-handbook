---
title: Model deployments, quotas and cost
sidebar_position: 2
last_verified: 2026-10-17
---

# A model deployment sets the boundary for traffic, data and spend

A model call works in a playground, then fails when several people use the application at once. Long
prompts consume the allowance faster than short questions; retries add more traffic just as the service
starts refusing requests. Meanwhile, a working endpoint in a resource created in the right country does not necessarily mean
the model processes its prompts there.

You need to choose where inference may happen, how much traffic the application can send and what you
pay for while it waits. For a small RAG service, these choices should be cheap to change, explicit in
configuration and visible when a request fails. Buying more throughput before measuring the workload
can leave you paying for capacity the service rarely uses.

## How it works on Azure \{#how-it-works-on-azure}

In Microsoft Foundry, a [model deployment](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/create-model-deployments)
binds a model and version to a deployment name, type and capacity setting. Your application calls the
deployment name. For P1, names such as `p1-chat-lab` and `p1-embed-lab` separate application configuration
from the underlying model identifiers. Record the model versions too: a friendly deployment name alone
does not explain what answered a question.

There are three quantities to keep apart. **Quota** is the allowance available to your subscription in
the applicable scope. A deployment's rate limit controls how quickly requests can consume its allocation.
Provisioned throughput reserves processing capacity. A large quota does not mean that you bought that
capacity or that each request will finish within a fixed time.

Azure OpenAI's [quota management](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota)
uses **tokens per minute (TPM)** and **requests per minute (RPM)**. Allocating TPM also sets RPM, with
ratios that vary by model. Token throttling uses an estimate that includes the prompt and requested
maximum output; it is different from the token count billed after processing. An unnecessarily large
output allowance can therefore reduce the traffic you can admit even when actual answers are short.
Request bursts can also hit short evaluation windows before the minute's total looks full.

Check the scope before planning another deployment. Foundry is
[moving models to shared subscription-level quota pools](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/quotas-limits).
The rollout started after 7 May 2026 with Realtime Translate and Realtime Transcribe; the guide says
“and soon all models”, not that migration is complete. Onboarded Global Standard model/version deployments share a pool across regions; Data Zone Standard
shares one within each zone. Other models still use regional pools. The portal's Quota page has a
**Scope** column identifying which system applies. Creating another resource does not automatically
create another allowance. Use the current [model quota tables](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits)
and your subscription's allocation, rather than a default copied from an example.

## Choosing and tradeoffs \{#choosing-and-tradeoffs}

Resolve the processing boundary first, then the traffic and payment model. Standard-family deployments
share serving capacity. Global Standard routes requests across available datacentres; Data Zone Standard
restricts that routing to its zone. The
[deployment-type catalogue](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types)
defines the following choices; availability depends on the model and version.

| Choice | Processing boundary | Payment and useful workload | When to avoid it |
|---|---|---|---|
| Standard (`Standard`) | Specified Azure geography. | Per token; interactive work needing that boundary. | Geography-based types arrive last for new models, with no guaranteed date; measured latency may also be unsuitable. |
| Global Standard (`GlobalStandard`) | Azure regions globally where the model is deployed. | Per token; P1's initial, variable traffic. | Your processing requirement excludes global routing. |
| Data Zone Standard (`DataZoneStandard`) | Microsoft-defined data zone. | Per token; interactive work needing that zone. | You require a narrower boundary or the model lacks support there. |
| Provisioned (`GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, `ProvisionedManaged`) | Global, Data Zone or geography, according to the provisioned type. | Allocated PTUs; sustained traffic sized from measurements. | Low or unknown utilisation makes idle capacity expensive. |
| Batch (`GlobalBatch`, `DataZoneBatch`) | Global or the selected data zone, where supported. | Batch token rates; asynchronous jobs. | A person is waiting for an interactive answer. |

The catalogue also lists `DeveloperTier`, omitted here because it is for fine-tuned model evaluation
only, with no SLA or residency guarantee.

Those are inference boundaries. [Data stored at rest stays in the designated Azure geography](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy),
while Global processing can happen elsewhere. The same privacy guidance permits processing between
regions within a geography for non-Global, non-DataZone deployments. Do not treat the word *Standard*
as a single-region guarantee. Data Zone means Microsoft's defined zone, not an availability zone or
a country selected by your application; check the current boundary against your actual requirement.

For P1's public documents, start with Global Standard unless the questions or other submitted content
introduce a residency requirement. Public source documents do not make every user prompt public.
Choose Data Zone Standard for both chat and embeddings when that boundary is required and supported.
Changing only the chat deployment leaves the text sent for embeddings outside the decision.

[Provisioned throughput units (PTUs)](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/provisioned-throughput)
measure reserved model processing capacity. They are not a universal token allowance: throughput depends
on the model and the input/output workload. Measure request rate, prompt length, answer length and
concurrency before sizing. PTU quota is permission to deploy; available capacity is a separate condition.
Having the former does not guarantee the latter.

A throughput deployment and an [Azure Reservation](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/provisioned-throughput-billing)
have separate lifecycles. Provisioned deployments incur a charge per deployed PTU
per hour, including idle time. A reservation discounts matching usage through a financial commitment;
it does not secure deployment capacity. Deleting a provisioned deployment stops its deployment meter
but does not cancel its reservation. That distinction makes provisioned throughput a poor default for
this course's small learning budget.

For token billing, compare the [input, cached-input where applicable, output and embedding rates](https://azure.microsoft.com/en-us/pricing/details/azure-openai/).
A useful estimate multiplies each token category by its own rate and then adds the other service costs.
Count the retrieved passages and conversation history sent on each call, not just the user's new words.
A low TPM setting slows consumption; repeated use can still accumulate a bill throughout the month.

[Batch processing](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/batch)
accepts groups of requests through files, with a separate enqueued-token quota and a 24-hour target
turnaround. Completion within that window is not guaranteed. Consider it for an offline evaluation
run that can wait and whose model/API combination is supported. It does not replace the deployment
serving P1's live questions. The [Batch quota tables](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits#batch-quota)
show N/A for Azure for Students and free trials; do not assume learning credit includes Batch access.

## In an AI workload \{#in-an-ai-workload}

P1's ASP.NET Core API will run on Container Apps. The query path needs an embedding for retrieval and
a chat completion using the selected passages; the [generation lesson](/rag-agents/part-1-rag/generation/)
owns how those passages support an answer with citations. Here the deployment choice determines which
traffic limits each stage must respect. If ingestion and user queries share an embedding deployment,
schedule or limit ingestion so it does not consume the allowance needed to answer questions.

Treat **HTTP 429** as a capacity signal the API must handle. Azure's
[retry guidance](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota#understanding-rate-limits)
says to respect `retry-after-ms` when supplied, otherwise use exponential backoff with random jitter.
Bound the attempts: unsuccessful requests also count towards rate limits. A tight loop can prolong
the condition it is trying to escape.

Read the error and [rate-limit headers](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota#rate-limit-response-headers)
before changing quota. Monitor `x-ratelimit-remaining-requests` and `x-ratelimit-remaining-tokens`.
If `x-ratelimit-limit-tokens` is below configured TPM, Azure has temporarily reduced the effective
limit under shared-pool pressure; that signals a capacity adjustment, not missing quota to allocate.

For P1, give each incoming question a deadline and a bounded wait for an admission slot before calling
the model. A retry may proceed only while that deadline still allows it. When the wait would exceed
the deadline, return a clear temporary failure to the caller. Check the selected SDK's retry policy
before adding another retry layer; nested policies can multiply attempts. Coordinate the allowance
across API replicas, because a per-process semaphore alone cannot control their combined traffic.
[Part III.8, The AI gateway](./ai-gateway.md) covers controls shared across callers.

The [serving lesson](/rag-agents/part-3-production/serving/)
explains the application boundary: retries, concurrency limits, timeouts and partially streamed answers.
In particular, do not silently restart a generation after the caller has already received part of it.
Receiving a 429 before generation and losing a connection halfway through an answer need different
recovery behaviour.

Record chat and embedding attempts separately in Application Insights: deployment name, elapsed time,
status, retry count and reported token usage. Follow the
[observability lesson](/rag-agents/part-1-rag/cross-cutting/observability/)
for tracing the whole request. Compare cost per successful answer and latency including retry waits,
because repeated attempts can make an answer expensive and slow even when each call is cheap.

## Try it \{#try-it}

Create the two model deployments P1 will later consume. You need a subscription and the P1 Foundry
resource from [Part III.1, Microsoft Foundry](./microsoft-foundry.md), plus permission to manage deployments; the
[deployment guide](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/create-model-deployments)
specifies Cognitive Services Contributor or equivalent permissions. Quota viewing needs
[Cognitive Services Usages Reader at subscription scope](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota#prerequisites)
or equivalent access; assignment at resource-group or resource scope does not authorize the Usages API.
This step does not provision Container Apps, Search or the API.

These commands were checked against the live Azure CLI reference on 2026-10-17. They have **not yet
been run against a live subscription**; no Azure subscription is available for this course yet.
The results below are expected from the documentation, not observed execution.

In Bash, replace the first three values. Use the core
[`az login`](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) and
[`az account set`](https://learn.microsoft.com/en-us/cli/azure/account#az-account-set) commands to select
the subscription deliberately.

```bash
P1_SUBSCRIPTION='your-subscription-id'
P1_RESOURCE_GROUP='your-p1-resource-group'
P1_FOUNDRY='your-p1-foundry-resource'
P1_CHAT='p1-chat-lab'
P1_EMBED='p1-embed-lab'
P1_SKU='GlobalStandard'

az login
az account set --subscription "$P1_SUBSCRIPTION"
```

Inspect [models available to the resource](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account#az-cognitiveservices-account-list-models)
and [existing deployments](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-list).
Choose unused deployment names; stop if either lab name already belongs to something else. Read the
[resource location](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account#az-cognitiveservices-account-show),
then [list subscription usages for that location](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/usage#az-cognitiveservices-usage-list).

```bash
P1_LOCATION=$(az cognitiveservices account show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --query location --output tsv)

az cognitiveservices usage list -l "$P1_LOCATION" --output json

az cognitiveservices account list-models \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --query "[?name=='gpt-5-mini' || name=='text-embedding-3-small']" \
  --output json

az cognitiveservices account deployment list \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --output json
```

Use `gpt-5-mini`, version `2025-08-07`, and `text-embedding-3-small`, version `1`.
Both are [GA](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule)
and [listed for Global Standard and Data Zone Standard](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability).
Confirm both versions and the chosen SKU in the returned records, including its capacity minimum and
step. In the portal's Quota page, check the scope and available allowance for each. If residency
requires Data Zone, set `P1_SKU='DataZoneStandard'` before creating either deployment, after confirming
both support it in your resource's zone. The [resource's region determines the Data Zone](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types#by-data-residency-requirement).
Stop if the required combination or quota is unavailable.

Use the core [`deployment create`](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-create)
command. For these TPM-based allocations,
[`--sku-capacity 10` requests 10,000 TPM](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/automate-quota-deployments)
per deployment. This is a deliberately low starting allocation; inspect the resulting limits rather
than inferring an RPM value.

```bash
az cognitiveservices account deployment create \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_CHAT" \
  --model-format OpenAI --model-name gpt-5-mini \
  --model-version 2025-08-07 \
  --sku-name "$P1_SKU" --sku-capacity 10

az cognitiveservices account deployment create \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_EMBED" \
  --model-format OpenAI --model-name text-embedding-3-small \
  --model-version 1 \
  --sku-name "$P1_SKU" --sku-capacity 10
```

Inspect each deployment with [`deployment show`](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-show):

```bash
for P1_DEPLOYMENT in "$P1_CHAT" "$P1_EMBED"; do
  az cognitiveservices account deployment show \
    --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
    --deployment-name "$P1_DEPLOYMENT" --output json
done
```

If creation succeeds, expect two named deployment records with the selected models, versions, SKU and
capacity. Check provisioning state and reported rate limits before recording the names as P1's chat
and embedding configuration. This control-plane check does not establish successful inference.
When the API exists, test that a burst hitting the low limit produces bounded waits and a clear
failure on exhaustion, without duplicate streamed answers. This exercise makes no model calls.

**Cost:** These Standard-family base-model deployments use
[token inference billing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/).
Creating and inspecting them without inference consumes no billable inference tokens. Later playground
or API calls incur token charges; other P1 resources have their own meters. Check current model/type
rates before calling them and keep the course's learning budget in view.

**Teardown:** Delete only the two deployments created here using
[`deployment delete`](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-delete).
Deletion [returns their allocated TPM to quota](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota#resource-deletion).
Keep the P1 resource and any unrelated deployments.

```bash
for P1_DEPLOYMENT in "$P1_CHAT" "$P1_EMBED"; do
  az cognitiveservices account deployment delete \
    --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
    --deployment-name "$P1_DEPLOYMENT"
done
```

## What to take away \{#what-to-take-away}

- Choose the inference boundary explicitly. Stored-at-rest geography and processing location answer
  different questions; apply the decision to embeddings as well as chat.
- Check quota scope and deployed TPM/RPM limits. Another resource or region does not necessarily give
  you an independent allowance.
- Bound admission and retries across the API's replicas. Respect retry delays and stop when the
  caller's deadline expires.
- Start P1 with token billing. Measure workload shape and utilisation before buying PTUs; a throughput
  deployment and a financial reservation have separate lifecycles.

**[New terms](../glossary.md#deployments-quotas-cost)**: deployment type, quota, TPM, RPM, HTTP 429, exponential backoff, PTU, Azure Reservation, batch deployment.

## Sources \{#sources}

Verified as of 2026-10-17.

- **Deployment and residency:** [Deploy models using Azure CLI and Bicep](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/create-model-deployments), [Deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types), [Data, privacy and security](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy), [Model and region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability), [Model retirement schedule](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule).
- **Quota and retries:** [Manage Azure OpenAI quota](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/quota), [Foundry Models quotas and scope](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/quotas-limits), [Azure OpenAI quotas and limits](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits), [Automate quota-based deployments](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/automate-quota-deployments).
- **Throughput and cost:** [Provisioned throughput](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/provisioned-throughput), [Provisioned throughput billing](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/provisioned-throughput-billing), [Batch processing](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/batch), [Azure OpenAI pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/).
- **CLI reference:** [Login](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login), [Select subscription](https://learn.microsoft.com/en-us/cli/azure/account#az-account-set), [Account model inventory and resource details](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account), [Subscription usage list](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/usage#az-cognitiveservices-usage-list), [Deployment create, list, show and delete](https://learn.microsoft.com/en-us/cli/azure/cognitiveservices/account/deployment).
