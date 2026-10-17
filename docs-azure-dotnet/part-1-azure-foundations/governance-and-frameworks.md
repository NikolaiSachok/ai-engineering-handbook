---
title: Governance and architecture frameworks
sidebar_position: 11
last_verified: 2026-10-17
---

# A deployment that succeeds can still break the rules

A service answers requests, its deployment is green, and nobody can say who owns its bill. A second
environment puts documents somewhere the organisation has not approved. Both systems work as deployed.
The missing piece is a way to make shared requirements hold across deployments, including changes made
outside the normal pipeline.

Some requirements can be checked mechanically: a resource must carry an owner tag or use an approved
location. Others need an architecture decision: how much downtime is acceptable, which dependencies
must recover together, and what an answer may cost. Governance needs enforceable configuration rules,
design guidance and someone responsible for acting on the findings.

## How it works on Azure \{#how-it-works-on-azure}

[Lesson 1](part-1-azure-foundations/how-azure-is-organised.md#how-it-works-on-azure) introduces the boundary between access
permissions and configuration rules; [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
makes those configuration requirements executable.

A [policy definition](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics)
describes a condition and an effect. Parameters make a definition reusable:
the same rule can require `owner` in one environment and `costCentre` in another. An **assignment**
binds that definition to a scope and supplies parameter values. An
[initiative](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure),
also called a policy set, groups definitions for a shared objective so you can assign them together.

An assignment at a resource group applies to applicable resources within that group; assignments at
subscriptions or management groups reach further down the hierarchy. A compliance result
reports whether an evaluated resource meets an assigned rule.

The [effect determines what happens when the condition
matches](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics).
For resource configuration rules, the available effects include these, among others:

| Effect | Mechanism | Failure to avoid |
|---|---|---|
| [`audit`](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-audit) | Records non-compliance while allowing the request. | Treating a finding as prevention. |
| [`deny`](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny) | Rejects a violating create or update request when enforcement is enabled. | Assuming it deletes or repairs existing resources. |
| [`modify`](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-modify) | Adds, updates or removes supported properties or tags. | Assuming existing resources change merely because a scan found them. |
| [`deployIfNotExists`](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deploy-if-not-exists) | Deploys a related resource when the policy's existence condition is unmet. | Letting automatic deployment create resources nobody operates. |

Existing resources need a remediation task for `modify` or `deployIfNotExists` to repair them. That
work uses the assignment's managed identity and needs the relevant permissions. Review the ownership and
cost of infrastructure changes before enabling them.

The **Cloud Adoption Framework (CAF)** addresses the wider organisational work of adopting Azure,
including preparing and governing the environment. Its
[landing zone guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)
describes the foundation into which workloads deploy. A platform landing zone supplies shared
capabilities and governance structure; application landing zones hold workload environments. Identity,
subscription organisation, networking and security decisions belong in that foundation.

Inside that environment, the
[Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework)
guides workload design through five pillars: Reliability, Security, Cost Optimization, Operational
Excellence and Performance Efficiency. Use them to expose design compromises and turn review findings into
implementation work.

Use the [tag vocabulary and inheritance guidance from lesson 1](part-1-azure-foundations/how-azure-is-organised.md#how-it-works-on-azure)
to choose policy targets, then use `modify` where the required tag value can be derived mechanically.

Use [Cost Management cost
analysis](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)
to investigate spending, and revisit [lesson 1's budget guidance](part-1-azure-foundations/how-azure-is-organised.md#choosing-boundaries)
and [Try it](part-1-azure-foundations/how-azure-is-organised.md#try-it) for alerts and subscription budget setup.

[Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
adds security posture findings and workload threat protection according to the enabled plans.
Its [Foundational CSPM capabilities are free; the Defender CSPM plan adds paid
capabilities](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management).
CSPM means cloud security posture management: assessing resource configurations for security weaknesses.
Check the plans actually enabled before assuming a resource is covered. Assign findings to an owner
and fix the cause in infrastructure code; the [secure
score](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls)
summarises the security findings.

## Choosing rules and accepting tradeoffs \{#choosing-and-tradeoffs}

Start with a requirement you can explain and a scope you can inspect. For P1, a resource group is a
reasonable place to learn one rule. Applying a broad initiative at subscription scope before reading
its definitions can affect unrelated experiments.

| Choice | Use it when | Avoid it when |
|---|---|---|
| Audit or evaluation without enforcement | You need to discover the impact before blocking deployments. | A violation must be prevented immediately. |
| Deny | The constraint is unambiguous and the deployment process can satisfy it. | Exceptions and existing deployment dependencies remain unknown. |
| Modify | There is an agreed, mechanically derivable value, such as a shared project tag. | The platform would have to guess the correct owner. |
| Deploy missing resources | A supporting resource has a standard configuration and an operator. | Its deployment would duplicate application-owned infrastructure. |
| A full landing zone implementation | Several workloads need a shared platform and delegated responsibilities. | You only need a bounded learning exercise in one resource group. |

A useful rollout option is an assignment with
[`enforcementMode:
DoNotEnforce`](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure#enforcement-mode).
It still evaluates compliance while leaving the effect unenforced. This differs from the `disabled`
effect, which skips rule evaluation. Inspect the definition for its supported effects before choosing an assignment strategy.

Inheritance also limits local fixes. A permissive assignment in P1 cannot cancel a deny inherited from
a parent scope. Resolve the requirement with the platform owner and change the applicable assignment
or its approved exceptions.

Architecture tradeoffs remain even with perfect configuration compliance. A recovery copy can improve
reliability while increasing cost and the amount of data to secure. Extra telemetry helps operations
but needs retention and access decisions. Record the requirement that justifies each expense and how
you will check it.

## In an AI workload \{#in-an-ai-workload}

P1 is the planned ASP.NET Core minimal API on Container Apps, answering questions over public documents
with citations. Its dependencies include a
[Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
model deployment, Azure AI Search, Blob Storage, Key Vault through managed identity and Application
Insights. Bicep and `azd` describe provisioning; GitHub Actions uses OIDC for delivery. Treat these as
parts of one workload when reviewing its architecture.

For **Reliability**, ask how to rebuild the search index from the source documents and what the API
returns when generation fails. For **Security**, trace the identities and document access boundaries.
For example, P1 could have an [allowed-locations
assignment](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#resource-manager-modes)
that permits its Foundry resource's region, yet use a **Global Standard** deployment whose prompts and
responses [may be processed across Azure
regions](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types#data-processing-locations).
Record both the allowed resource location and the chosen processing boundary in P1's design.
Part III's *Model deployments, quotas and cost* lesson (planned) covers deployment selection.

For **Cost Optimization**, measure the cost of a useful answer and bound retries and output. **Operational
Excellence** asks whether you can trace a failed answer
through retrieval and generation and repeat a deployment. **Performance Efficiency** asks which stage
causes the delay before increasing capacity.

The distinction between advice and enforcement is developed in
[Rules that hold](/ai-sdlc/part-1-foundation/rules-that-hold).
Keep application checks alongside Policy:
[Evaluation](/rag-agents/part-1-rag/cross-cutting/evaluation/) owns retrieval and answer quality;
[Guardrails](/rag-agents/part-1-rag/cross-cutting/guardrails/) owns the treatment of untrusted inputs
and outputs. A compliant owner tag cannot tell you whether a citation supports an answer.

## Try it \{#try-it}

Assign **Require a tag on resources** in a fresh lab group, then create an untagged resource to inspect
noncompliance before enforcement. This rehearses P1's ownership rule without needing P1 deployed.
You need Azure CLI and subscription permissions to create and delete resource groups and managed
identities, manage policy assignments and read compliance. The
[`Resource Policy Contributor`
role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/management-and-governance#resource-policy-contributor)
covers the policy operations; resource creation needs additional permissions.

No Azure subscription exists for these course examples yet. **These commands were checked against
the current Azure CLI reference and have not yet been run against a live subscription.** Results below
are expected, not observed. Use Bash and keep the variables in the same shell. Choose a new lab group
name and a location permitted by your subscription's policies.

Select the subscription and create the group
([login](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-login),
[account](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az-account-set),
[group](https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-create) references):

```bash
az login
az account set --subscription 'replace-with-subscription-id'
rg='rg-p1-governance-lab'
location='replace-with-approved-location'
assignment='p1-owner-tag-lab'
scope=$(az group create --name "$rg" --location "$location" --query id --output tsv)
```

Stop if any command fails. Inspect the built-in before assigning it
([definition
command](https://learn.microsoft.com/en-us/cli/azure/policy/definition?view=azure-cli-latest#az-policy-definition-show)):

```bash
policy='871b6d14-10aa-478d-b590-94f262ecfa99'
az policy definition show --name "$policy" --output json
```

The [built-in catalogue](https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies#tags)
and its [definition
source](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Tags/RequireTag_Deny.json)
currently list version **1.0.1**, parameter `tagName`, effect `deny` and mode `Indexed`.
It checks tag existence, not whether the value names a real owner. It excludes resource groups;
[`Indexed` targets resource types supporting tags and
location](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#resource-manager-modes).

Create the
[assignment](https://learn.microsoft.com/en-us/cli/azure/policy/assignment?view=azure-cli-latest#az-policy-assignment-create)
with enforcement off:

```bash
az policy assignment create \
  --name "$assignment" \
  --display-name 'P1 owner tag check' \
  --scope "$scope" \
  --policy "$policy" \
  --definition-version '1.*.*' \
  --params '{"tagName":{"value":"owner"}}' \
  --enforcement-mode DoNotEnforce \
  --output json
```

The [version pattern
`1.*.*`](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure#policy-definition-id-and-version)
accepts minor and patch updates within major version 1; patch updates must be accepted.
Check the returned scope, parameter and enforcement mode.

Create a [user-assigned managed
identity](https://learn.microsoft.com/en-us/cli/azure/identity?view=azure-cli-latest#az-identity-create)
without tags. Its resource type [supports tags and
location](https://learn.microsoft.com/en-us/azure/templates/microsoft.managedidentity/2023-01-31/userassignedidentities),
so it qualifies for `Indexed` evaluation:

```bash
az identity create --name 'id-p1-policy-lab' --resource-group "$rg" \
  --location "$location" --output json
```

Allow the assignment to propagate;
[Microsoft documents roughly five minutes before evaluation begins, with no fixed completion
time](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data#evaluation-triggers).
[Request a scan](https://learn.microsoft.com/en-us/cli/azure/policy/state?view=azure-cli-latest#az-policy-state-trigger-scan)
with `--no-wait`, then poll by repeating `state list` below until the identity's result appears:

```bash
az policy state trigger-scan --resource-group "$rg" --no-wait
az policy state list \
  --resource-group "$rg" \
  --policy-assignment "$assignment" \
  --query "[].{Resource:resourceId,State:complianceState}" \
  --output table
```

Expected: `id-p1-policy-lab` reports **NonCompliant** because it lacks `owner`, while `DoNotEnforce`
allows its creation. An empty table means you must wait and query again, then check applicability if
results stay empty. If inherited policies deny creation or add the tag, resolve that with the platform
owner before continuing. Save the identity's result and assignment scope in P1's notes; carry the
required tag into P1's Bicep templates before enforcing the rule there.

**Cost:** [Azure Policy on Azure resources is free](https://azure.microsoft.com/en-us/pricing/details/azure-policy/),
and [managed identities have no extra
cost](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).
The lab provisions no compute, storage or model deployment.

**Teardown:** Delete the
[assignment](https://learn.microsoft.com/en-us/cli/azure/policy/assignment?view=azure-cli-latest#az-policy-assignment-delete)
and the [lab group, including its
identity](https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-delete)
after recording the result:

```bash
az policy assignment delete --name "$assignment" --scope "$scope"
az group delete --name "$rg" --yes
```

## What to take away \{#what-to-take-away}

- Bind a policy definition or initiative to a deliberate scope; the assignment makes the rules apply.
- Choose effects according to the consequence you need. Finding non-compliance, preventing a request
  and repairing resources are different operations.
- Use CAF for the governed foundation and Well-Architected for workload decisions. Keep owners and
  tradeoffs explicit.
- Tags, budgets and security posture findings need follow-through. Budgets do not cap consumption,
  and configuration compliance does not establish answer quality.

**[New terms](../glossary.md#governance-and-frameworks)**: Azure Policy, policy definition, policy effect, policy assignment, policy initiative, compliance state, Cloud Adoption Framework, landing zone, Well-Architected Framework, Cost Management, Microsoft Defender for Cloud, CSPM.

## Sources \{#sources}

Verified as of 2026-10-17.

**Policy and enforcement**

- [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- [Effect basics](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics), [audit](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-audit), [deny](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny), [modify](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-modify), [deployIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deploy-if-not-exists)
- [Assignment structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure) and [definition modes](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics)
- [Initiative structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure)
- [Built-in policy catalogue](https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies#tags) and [require-tag source](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Tags/RequireTag_Deny.json)
- [Compliance evaluation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data)
- [Resource Policy Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/management-and-governance#resource-policy-contributor)

**Architecture, cost and security**

- [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/overview) and [Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)
- [Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework)
- [Cost analysis](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis) and [budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) and [CSPM plan options](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management)
- [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
- [Azure Policy pricing](https://azure.microsoft.com/en-us/pricing/details/azure-policy/) and [managed identities overview and cost](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [Foundry deployment types and processing locations](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types)
- [Secure score](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls)
- [Managed identity resource schema (2023-01-31)](https://learn.microsoft.com/en-us/azure/templates/microsoft.managedidentity/2023-01-31/userassignedidentities)

**CLI reference**

- [Login](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-login), [account](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az-account-set), [resource group](https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest)
- [Policy definitions](https://learn.microsoft.com/en-us/cli/azure/policy/definition?view=azure-cli-latest), [assignments](https://learn.microsoft.com/en-us/cli/azure/policy/assignment?view=azure-cli-latest), [compliance states and scans](https://learn.microsoft.com/en-us/cli/azure/policy/state?view=azure-cli-latest)
- [Managed identities](https://learn.microsoft.com/en-us/cli/azure/identity?view=azure-cli-latest)
