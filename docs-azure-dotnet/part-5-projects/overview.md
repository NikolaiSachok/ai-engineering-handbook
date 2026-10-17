---
id: overview
title: Part V — Projects
sidebar_label: Part overview
last_verified: 2026-10-17
---

# Part V — Projects

The projects join the lesson exercises into services you can run and explain. Start with the RAG service,
then add the agent and gateway; the document ingestion pipeline is optional. This order establishes a
working request path before adding tool actions and event-driven document processing.

*Where this sits on [the course map](../intro.md#course-map): the build guides — where the lesson exercises become complete services.*

## What's inside \{#whats-inside}

{/* slugs: rag-service, agent-behind-gateway, ingestion-pipeline */}

- **RAG service** 🚧 — Build an ASP.NET Core API that answers questions over a small public document set with citations. Join model access, hybrid retrieval, keyless access, telemetry and repeatable deployment in one service.
- **Agent behind an AI gateway** 🚧 — Build a tool-calling agent with approvals and gateway controls. Add long-running work, persistent state and evaluation so you can explain what an action may do and how it is checked.
- **Document ingestion pipeline** 🚧 — Optional: process incoming documents and update the retrieval index. Connect events, document processing and metadata storage, and account for retries along the path.

## Prerequisites \{#prerequisites}

Start the RAG service alongside the Part I resource, identity, compute and infrastructure lessons and the
Part III model setup lessons; complete it with Part II, retrieval, evaluation and observability. The agent
project also needs data access, messaging, agent and gateway lessons. For the optional pipeline, add storage,
events, Functions and document processing. Read each guide with its lessons rather than waiting to finish
the whole course.

## What changes after this part \{#what-changes-after-this-part}

Each project page is a build guide with a goal, architecture diagram and milestones matching the lessons’
**Try it** steps. It includes a cost table, teardown script and questions you should be able to answer about
the result. You can use the finished service to explain the choices between its components, demonstrate
its checks and remove the resources when the exercise is over.

:::note[Status]

Published: 0 of 3 project guides. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Azure for .NET developers](https://learn.microsoft.com/en-us/dotnet/azure/)
