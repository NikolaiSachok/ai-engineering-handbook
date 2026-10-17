---
title: Enterprise-grade AI
sidebar_position: 9
last_verified: 2026-10-17
---

# A private model endpoint is only one boundary

A question-answering service can protect its model connection while leaving the documents, search index
or diagnostic logs exposed through a different path. It can also use identity tokens everywhere in its
application code while a forgotten script still authenticates with a shared key. Neither problem appears
in the quality of the answer: the service can return accurate citations while its access controls remain
incomplete.

Review the whole request and document lifecycle. Establish who can reach each dependency, which identity
may use it, where content is processed and what copies persist afterwards. These decisions constrain
ingestion, deployment and support as much as the answering API. A private production design must still
let someone update the corpus, diagnose a failed request and recover the service.

## How it works on Azure \{#how-it-works-on-azure}

Start with the [networking](../part-1-azure-foundations/networking.md) and
[RBAC and keyless access](../part-1-azure-foundations/rbac-and-keyless-access.md) lessons. Here, the task
is to apply those mechanisms to every connection in the RAG service project, P1.

For [Microsoft Foundry inbound isolation](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link),
create and approve a private endpoint for the Foundry resource, make its hostname resolve privately from
the callers' network, and disable public network access. Those are separate settings. Adding a private
endpoint gives callers another route; it does not remove the public one. Apply the same review to
[Azure AI Search](https://learn.microsoft.com/en-us/azure/search/service-create-private-endpoint), then
to Blob Storage and Key Vault.

Keep the service hostname in the client configuration. DNS must resolve that hostname to the private
endpoint address from the environment making the call. Foundry can expose several endpoint suffixes;
configure the [private DNS zones for each one the workload uses](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns),
including `privatelink.openai.azure.com` and `privatelink.services.ai.azure.com` where applicable.
Search uses `privatelink.search.windows.net`. A successful lookup on a developer laptop says little
about resolution inside the running API's network.

Private endpoints control incoming connections to a service. If you later host an agent in Foundry,
its tool and data calls need a separate
[outbound network design](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link).
The model's private endpoint cannot restrict which external destinations an agent calls.

For [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/networking), choose an
environment connected to your own VNet when the app needs private dependencies. The default Azure network
can reach internet-accessible endpoints; its network type cannot be changed after environment creation.
Plan this before treating the prototype environment as production infrastructure. Whether users can
reach the API publicly is a separate ingress decision: private dependencies do not require every product
to have an internal-only user interface.

Authentication is another boundary. [Keyless connections](https://learn.microsoft.com/en-us/azure/developer/ai/keyless-connections)
use Microsoft Entra ID tokens and appropriate data permissions. P1's Container Apps identity should call
Foundry, Search, Blob and Key Vault directly with tokens. Keeping a model key in Key Vault still leaves
the model connection dependent on a key. Key Vault remains useful for secrets that cannot be replaced
with identity-based access.

Enforce the intended authentication method at the receiving service. Foundry's
[`disableLocalAuth` setting](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth)
rejects local key authentication once the change has propagated. Search has its own
[roles-only setting](https://learn.microsoft.com/en-us/azure/search/search-security-enable-roles).
For Blob Storage, review clients and SAS usage before
[disallowing Shared Key](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent).
Changing one resource does not harden the others. Test the runtime and ingestion identities separately;
the answering API should not acquire the ingestion worker's write permissions merely to make a test pass.

## Choosing and tradeoffs \{#choosing-and-tradeoffs}

Choose the network design from the data and exposure requirements. A small public corpus can justify
a simpler learning environment. Sensitive documents may require private dependency access, controlled
outbound traffic and a private route for operators. Write those requirements before selecting a template.

| Choice | When it fits | When to avoid it, or what can fail |
|---|---|---|
| Public service endpoints with Entra authentication | A learning environment or a workload whose requirements permit public network reachability. | It cannot satisfy a requirement to reject public data-plane access, even with correct RBAC. |
| Private endpoints, private DNS and disabled public access | Dependencies must accept traffic only through approved private connectivity. | Without an operator and ingestion route, routine maintenance becomes an outage. |
| Search indexers with shared private links | Search itself must fetch content from a private supported dependency. | The API's inbound Search endpoint does not provide this outbound path; approval and indexer configuration are separate work. |
| A landing-zone reference implementation | Several teams need shared connectivity, governance and operating arrangements. | Deploying an entire reference stack for a small exercise adds resources and responsibilities the exercise does not need. |

The Search distinction is easy to miss. A **shared private link** is an outbound connection managed for
Search, independent of the private endpoint through which your API queries Search. If you use indexers
or integrated vectorisation, check the
[supported targets and workload-specific requirements](https://learn.microsoft.com/en-us/azure/search/search-indexer-howto-access-private).
Set the indexer's [`parameters.configuration.executionEnvironment` to `"private"`](https://learn.microsoft.com/en-us/azure/search/search-indexer-howto-access-private#4---configure-the-indexer-to-run-in-the-private-environment):
the multitenant processing environment cannot use private endpoint connections, so an approved link alone
can still leave ingestion failing. An application that pushes prepared documents into an index has a
different ingestion path. Test the path you actually chose. The current
[Search private-endpoint guide](https://learn.microsoft.com/en-us/azure/search/service-create-private-endpoint)
requires Basic or higher; the Free tier does not support private endpoints. Private Link also has
[endpoint-hour and data-processing charges](https://azure.microsoft.com/en-us/pricing/details/private-link/).
This is a deliberate budget change from a public learning setup.

Network privacy does not establish **data residency**, the location commitments for stored or processed
data. For serverless Foundry model deployments, inspect the
[deployment type](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types):
Global processing can cross geographies; Data Zone processing stays within a Microsoft-defined zone;
Standard and Regional Provisioned processing stays within the specified Azure geography, potentially
across its regions. Availability depends on the model. A resource's region and a private destination IP
therefore do not prove that inference remains in that region. Review the permitted processing boundary
before choosing a deployment or adding a failover target.

For these deployment types, data stored at rest remains in the designated Azure geography. Check the
locations of Search, Blob and telemetry independently; a model deployment does not relocate their data.

Read data handling commitments with their product scope intact. For
[Models sold by Azure, including Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy),
Microsoft states that prompts, completions, embeddings and training data are unavailable to the model
providers, and are not used to train foundation models without your permission or instruction. That
does not mean nothing is retained: stateful features persist content, and abuse monitoring can select
content for human review. Modified abuse monitoring requires approval; preview practices may differ.
[Agent tools can have separate terms](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/agents/data-privacy-security).
Record the selected offer, features and retention behaviour rather than extending one model's
commitments to every tool in the system.

Microsoft's [AI architecture guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/platform/architectures)
links the AI workload landing zone and its reference implementation. Use it to review missing decisions.
The [Foundry chat landing-zone architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-landing-zone)
also makes ownership explicit: the workload team operates its application while the platform team
supplies shared capabilities such as connectivity, DNS and governance. Its application host is App
Service, so it is a reference for P1's responsibilities rather than a Container Apps deployment recipe.
Assign owners for DNS changes, access exceptions and incident support before adopting shared infrastructure.

## In an AI workload \{#in-an-ai-workload}

P1's ASP.NET Core minimal API retrieves passages and sends them with the question to a Foundry model
deployment. A private Search connection protects that transport path; it does not determine which
passages the asking user may see. Keep document authorisation in the
[retrieval design](/rag-agents/part-1-rag/retrieval/). P1's public document set makes the first exercise
simple, but replacing it with internal documents changes the access requirements before it changes the
model client.

Before calling P1 private, review each path and the evidence that would establish it:

| P1 path | Required review and evidence |
|---|---|
| Container Apps → Foundry, Search, Blob, Key Vault | Private DNS and reachable endpoints from the app environment; approved connections; disabled public access; successful token-authenticated operations. |
| Ingestion → Blob, embedding model, Search | A reachable private execution location, its own data grants and a completed ingestion run. If Search performs ingestion, review its outbound links too. |
| GitHub Actions → deployment and data operations | A deployment identity using OIDC; separately, network access from the runner for any private data-plane steps. |
| API → Application Insights | Explicit choice of permitted public egress or private ingestion; a trace received at the approved destination after egress restrictions; access controls and decisions about capturing prompts, passages and responses. |

[GitHub Actions OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect)
removes the stored deployment credential. It does not create a route into the VNet. A deployment can
succeed through the control plane while an index-loading job fails to reach Search. List those jobs
before disabling public access.

For private telemetry ingestion, follow [Azure Monitor Private Link guidance](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/private-link-security)
and its [Private Link Scope design](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/private-link-design).
Azure Monitor uses a separate Azure Monitor Private Link Scope (AMPLS), with its own private endpoint
and DNS configuration. Include that path in the [Part I network review](../part-1-azure-foundations/networking.md);
Foundry and Search endpoints do not carry Application Insights telemetry.

Treat logs and traces as additional copies of workload data. The
[observability lesson](/rag-agents/part-1-rag/cross-cutting/observability/) owns what to measure;
this review asks what content leaves the request path, who can read it and when it is deleted. Apply
[least privilege](/ai-sdlc/part-4-platform/least-privilege-sandboxing/) to these readers too. Keep the
network and authentication settings in P1's Bicep configuration so an `azd` deployment preserves the
reviewed design.

## Try it \{#try-it}

Disable local authentication on P1's Foundry resource. If you completed the earlier teardown, first
recreate a disposable group and account using the [account-creation step](./microsoft-foundry.md#try-it),
which follows Microsoft's [creation guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-projects).
Only the group and Foundry account are needed here; the rest of P1 can stay torn down.

Use local Bash with Azure CLI already signed in, and an account allowed to read and update that resource.
First confirm that every current client supports Entra authentication and has the required permissions. This setting affects other
clients sharing the resource, including ingestion scripts.

**Cost:** free as a configuration-only exercise: the commands read and update an existing resource,
create no infrastructure and send no inference requests. Existing P1 resources retain their normal
charges. Account recreation is separate prerequisite work: an empty account with no model deployment
or consumed features has no expected usage charge, while
[consumed Foundry features are billed separately](https://azure.microsoft.com/en-us/pricing/details/microsoft-foundry/#faq).
No private endpoints or landing-zone stack are deployed here.

These commands were checked against the live
[`az resource show`](https://learn.microsoft.com/en-us/cli/azure/resource?view=azure-cli-latest#az-resource-show)
and [`az resource update`](https://learn.microsoft.com/en-us/cli/azure/resource?view=azure-cli-latest#az-resource-update)
references. They have **not yet been run against a live subscription**; no Azure subscription is
available for this exercise's verification. The property is defined in the stable
[`2025-06-01` account API](https://learn.microsoft.com/en-us/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts).

Replace the resource ID below with P1's Foundry account ID. Read the current state and save the result
in your project notes. Confirm `kind` is `AIServices`, the
[Foundry resource kind](https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture), and the ID
identifies the intended account before running the update.

```bash
P1_FOUNDRY_ID='/subscriptions/REPLACE-SUBSCRIPTION-ID/resourceGroups/REPLACE-RESOURCE-GROUP/providers/Microsoft.CognitiveServices/accounts/REPLACE-FOUNDRY-NAME'

az resource show --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --query '{id:id,kind:kind,disableLocalAuth:properties.disableLocalAuth,publicNetworkAccess:properties.publicNetworkAccess}' \
  --output json
```

Set the Boolean property, then read it back:

```bash
az resource update --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --set properties.disableLocalAuth=true --output none

az resource show --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --query properties.disableLocalAuth --output json
```

**Expected result:** the readback is `true`, meaning the configuration disables local authentication.
It does not prove immediate key rejection. Microsoft documents a
[gateway propagation delay](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth)
that can extend to hours, and requires a data-plane request using a previously valid key to return
HTTP 401 before considering enforcement complete. When P1 is runnable, record that rejection and a
successful Entra-authenticated call using its runtime identity. Keep key values out of notes and logs.

Add `disableLocalAuth: true` inside the owning account's `properties` in P1's Bicep definition before
the next deployment. Record the private-network gaps from the review table as remaining work; this
exercise has changed authentication, not established network isolation.

**Teardown:** the configuration commands created no resources. If you recreated a disposable account
solely for this exercise, follow the [earlier teardown](./microsoft-foundry.md#try-it) to delete its
dedicated group and [purge the account](https://learn.microsoft.com/en-us/azure/ai-services/recover-purge-resources)
after readback. For an existing P1 account, keep local authentication disabled. If you must restore
a previously enabled setting to recover an incompatible client, use the following rollback, then fix
the client and repeat the exercise. Re-enabling keys also has a propagation delay.

```bash
az resource update --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --set properties.disableLocalAuth=false --output none
```

## What to take away \{#what-to-take-away}

- Review the API, ingestion, operators, deployment jobs and telemetry as separate data paths.
- A private dependency needs caller connectivity, working DNS and disabled public access alongside its private endpoint.
- Tokens in application code do not enforce keyless-only access. Disable key authentication at each receiving service and verify rejection.
- Check model processing boundaries and retention commitments separately from network privacy and resource location.
- Use landing-zone references to assign responsibilities and find missing controls before adopting their infrastructure.

**[New terms](../glossary.md#enterprise-ai)**: shared private link, local authentication, data residency, processing boundary, abuse monitoring.

## Sources \{#sources}

Verified as of 2026-10-17.

- **Network paths:** [Foundry network isolation](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link), [private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns), [Search private endpoints](https://learn.microsoft.com/en-us/azure/search/service-create-private-endpoint), [Search shared private links](https://learn.microsoft.com/en-us/azure/search/search-indexer-howto-access-private), [Container Apps networking](https://learn.microsoft.com/en-us/azure/container-apps/networking), [Private Link pricing](https://azure.microsoft.com/en-us/pricing/details/private-link/), [Azure Monitor Private Link](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/private-link-security), [Azure Monitor Private Link Scope design](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/private-link-design).
- **Identity and enforcement:** [Keyless connections](https://learn.microsoft.com/en-us/azure/developer/ai/keyless-connections), [disable Foundry local authentication](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth), [Search RBAC configuration](https://learn.microsoft.com/en-us/azure/search/search-security-enable-roles), [prevent Storage Shared Key authorisation](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent), [GitHub Actions OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect).
- **Data handling:** [Model deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types), [Models sold by Azure privacy statement](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy), [Agent Service privacy statement](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/agents/data-privacy-security).
- **Architecture:** [Foundry resource model](https://learn.microsoft.com/en-us/azure/foundry/concepts/architecture), [AI platform architecture guidance and landing-zone reference](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/platform/architectures), [Foundry chat in an Azure landing zone](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-landing-zone).
- **Exercise reference:** [Account API `2025-06-01`](https://learn.microsoft.com/en-us/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts), [Azure CLI resource commands](https://learn.microsoft.com/en-us/cli/azure/resource?view=azure-cli-latest), [Foundry account creation](https://learn.microsoft.com/en-us/azure/foundry/how-to/create-projects), [Foundry pricing FAQ](https://azure.microsoft.com/en-us/pricing/details/microsoft-foundry/#faq), [Foundry recovery and purge](https://learn.microsoft.com/en-us/azure/ai-services/recover-purge-resources).
