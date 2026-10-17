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

- **How Azure is organised** 🚧 — tenants, management groups, subscriptions, resource groups and resources; Azure Resource Manager, regions and zones. The hierarchy is the governance and billing model.
- **Identity I — Microsoft Entra ID** 🚧 — users, groups, app registrations, service principals, system-assigned and user-assigned managed identities. Tokens are what an application presents when it asks for access.
- **Identity II — RBAC and keyless access** 🚧 — roles, scopes and inheritance; control-plane versus data-plane roles, `DefaultAzureCredential` and workload identity federation. Keyless access extends to CI without stored secrets.
- **Networking for application engineers** 🚧 — VNets, subnets, NSGs, private versus service endpoints, private DNS, PaaS VNet integration and hub-and-spoke. Ingress choices include Front Door, Application Gateway and Load Balancer.
- **Choosing compute** 🚧 — App Service, Container Apps, Functions (Flex Consumption), AKS and virtual machines. The choice depends on workload shape, scaling model and operational cost.
- **Storing data** 🚧 — Blob Storage, Azure SQL, PostgreSQL flexible server with pgvector, Cosmos DB and Azure Managed Redis. Access patterns guide the choice, including Cosmos DB request units, consistency and vector search.
- **Messaging and events** 🚧 — Service Bus, Event Grid and Event Hubs; dead-lettering, retries and ordering. Commands, events and streams call for different messaging services.
- **Secrets and configuration** 🚧 — Key Vault secrets, keys, certificates, RBAC and rotation; App Configuration. Managed identity provides access to both services.
- **Infrastructure as code** 🚧 — ARM, Bicep, Terraform and Azure Developer CLI (`azd`). Change previews, drift and modules are part of managing infrastructure as code.
- **Observability** 🚧 — Azure Monitor, Log Analytics, Application Insights and the OpenTelemetry distribution. KQL queries turn that telemetry into answers about service behaviour.
- **Governance and architecture frameworks** 🚧 — Azure Policy, Cloud Adoption Framework landing zones, the Well-Architected Framework, tags, cost management, budgets and Defender for Cloud. These cover platform rules, architecture guidance, costs and security posture.

## Prerequisites \{#prerequisites}

None from this course. Production engineering experience is assumed; Azure and other cloud platforms are
not. Start here if subscriptions, managed identities and private endpoints are still disconnected names.

## What changes after this part \{#what-changes-after-this-part}

You can explain the resource hierarchy and access scopes, and compare network, compute, storage and
messaging choices for a workload. You can distinguish the roles of infrastructure as code, telemetry and
platform governance before using them in the later parts.

:::note[Status]

Published: 0 of 11 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Azure application architecture fundamentals](https://learn.microsoft.com/en-us/azure/architecture/guide/)
