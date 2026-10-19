---
id: overview
title: Part V — Projects
sidebar_label: "Part V — Projects"
last_verified: 2026-10-17
---

# Part V — Projects

The projects join the lesson exercises into services you can run and explain. Start with the RAG service,
then add the agent and gateway; the document ingestion pipeline is optional. This order establishes a
working request path before adding tool actions and event-driven document processing.

Each project page is intended as a build guide: a goal, architecture diagram, milestones matching the
lessons’ **Try it** steps, a cost table, a teardown script and what you should be able to explain afterwards.

*Where this sits on [the course map](../intro.md#course-map): the build guides — where the lesson exercises become complete services.*

## What's inside \{#whats-inside}

{/* slugs: rag-service, agent-behind-gateway, ingestion-pipeline */}

- **[RAG service](./rag-service.md)** — an ASP.NET Core minimal API over a small public document set, using .NET 10, `Microsoft.Extensions.AI`, a Foundry model deployment, Azure AI Search hybrid retrieval, Blob Storage, Key Vault via managed identity, Container Apps, Application Insights with OpenTelemetry, Bicep, `azd` and GitHub Actions with OIDC. The service answers questions with citations.
- **Agent behind an AI gateway** 🚧 — Microsoft Agent Framework for .NET, API Management AI-gateway policies, Service Bus for long-running work, EF Core with PostgreSQL and Foundry evaluations. The agent calls tools with approvals.
- **Document ingestion pipeline** 🚧 — an optional Event Grid → Functions → Content Understanding → index-update pipeline, with metadata in Cosmos DB or PostgreSQL. Incoming documents trigger processing and retrieval-index updates.

## Prerequisites \{#prerequisites}

Start the RAG service alongside the Part I resource, identity, compute and infrastructure lessons and the
Part III model setup lessons; complete it with Part II, retrieval, evaluation and observability. The agent
project also needs data access, messaging, agent and gateway lessons. For the optional pipeline, add storage,
events, Functions and document processing. Read each guide with its lessons rather than waiting to finish
the whole course.

## What changes after this part \{#what-changes-after-this-part}

You can build the chosen application in milestones and explain its components, checks and costs.
You can demonstrate the result and remove the resources when the exercise is over.

:::note[Status]

Published: 1 of 3 project guides. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Azure for .NET developers](https://learn.microsoft.com/en-us/dotnet/azure/)
