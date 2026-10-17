---
id: overview
title: Part I — Azure foundations
sidebar_label: Part overview
last_verified: 2026-10-17
---

# Part I — Azure foundations

An AI service needs somewhere to run, an identity, access to data and a way to explain what went wrong.
Part I builds that platform picture before choosing the AI services. The order matters: establish where
resources belong and who may use them, then choose the network, compute and data services they need.
Infrastructure, telemetry and governance finish the picture by making those choices repeatable and reviewable.

*Where this sits on [the course map](../intro.md#course-map): underneath the application — the Azure resources and boundaries the later parts rely on.*

## What's inside \{#whats-inside}

{/* slugs: how-azure-is-organised, entra-id, rbac-and-keyless-access, networking, compute, data, messaging, secrets-and-configuration, infrastructure-as-code, observability, governance-and-frameworks */}

- **How Azure is organised** 🚧 — Follow tenants, management groups, subscriptions, resource groups and resources through Azure Resource Manager. Connect that hierarchy to regions, zones, governance and billing.
- **Identity I — Microsoft Entra ID** 🚧 — Distinguish users, groups, app registrations, service principals and managed identities. Follow the token an application presents when it asks for access.
- **Identity II — RBAC and keyless access** 🚧 — Work through roles, scopes and inheritance, including the difference between control-plane and data-plane access. Use `DefaultAzureCredential` and workload identity federation to plan access without stored keys.
- **Networking for application engineers** 🚧 — Trace a request through virtual networks, subnets, network security groups and private DNS. Compare private and service endpoints, PaaS network integration, ingress choices and hub-and-spoke layouts.
- **Choosing compute** 🚧 — Compare App Service, Container Apps, Functions, AKS and virtual machines by workload shape. Scaling behaviour and operational work belong in the decision alongside the code you want to run.
- **Storing data** 🚧 — Choose among Blob Storage, Azure SQL, PostgreSQL, Cosmos DB and Azure Managed Redis by access pattern. Include vector search, consistency and capacity in the comparison.
- **Messaging and events** 🚧 — Separate commands, events and streams before choosing Service Bus, Event Grid or Event Hubs. Then account for retries, dead-lettering and ordering.
- **Secrets and configuration** 🚧 — Decide what belongs in Key Vault and what belongs in App Configuration. Work through managed-identity access, permissions and rotation for secrets, keys and certificates.
- **Infrastructure as code** 🚧 — Compare ARM, Bicep and Terraform, then place Azure Developer CLI (`azd`) in the deployment workflow. Modules, change previews and drift make infrastructure changes something you can review.
- **Observability** 🚧 — Connect Azure Monitor, Log Analytics, Application Insights and OpenTelemetry to the questions you need to answer about a service. Practise the KQL needed to investigate its behaviour.
- **Governance and architecture frameworks** 🚧 — Bring Azure Policy, landing zones, the Cloud Adoption Framework and the Well-Architected Framework into an architecture review. Include tags, budgets and Defender for Cloud in the operating plan.

## Prerequisites \{#prerequisites}

None from this course. Production engineering experience is assumed; Azure and other cloud platforms are
not. Start here if subscriptions, managed identities and private endpoints are still disconnected names.

## What changes after this part \{#what-changes-after-this-part}

You can sketch an Azure service and explain where its resources live, who can reach them and how access
is granted. You can choose compute, storage and messaging for a stated workload, then describe how to deploy,
observe and govern it. Those decisions become the foundation for the RAG service project.

:::note[Status]

Published: 0 of 11 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Azure application architecture fundamentals](https://learn.microsoft.com/en-us/azure/architecture/guide/)
