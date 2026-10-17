---
id: overview
title: Part III — Running LLMs on Azure
sidebar_label: Part overview
last_verified: 2026-10-17
---

# Part III — Running LLMs on Azure

A model endpoint is only one piece of an AI service. Part III starts with how models are organised and
deployed, then adds safety, retrieval and document processing before agents. Evaluation and the gateway
follow once there is behaviour to measure and traffic to control; enterprise constraints and low-code
choices close the part by placing the service in a wider organisation.

*Where this sits on [the course map](../intro.md#course-map): where platform and application meet — model access, retrieval, agents and their operating controls.*

## What's inside \{#whats-inside}

{/* slugs: microsoft-foundry, deployments-quotas-cost, platform-safety, rag-on-ai-search, document-ingestion, agents-on-azure, evaluation-and-tracing, ai-gateway, enterprise-ai, copilot-studio-power-platform */}

- **Microsoft Foundry** 🚧 — Work through the resource and project model, the model catalog and Azure OpenAI’s place in it. Include models from other providers when deciding what to deploy.
- **Model deployments, quotas and cost** 🚧 — Compare deployment types against throughput, residency and cost requirements. Work through token and request quotas, rate limiting and the capacity a service needs.
- **Safety on the platform** 🚧 — Examine content filters, Prompt Shields and groundedness detection. Identify what platform safety leaves to the application and connect it to the guardrails taught in [RAG & Agents](/rag-agents/).
- **RAG on Azure AI Search** 🚧 — Build the retrieval design around indexes, hybrid retrieval and semantic ranking. Compare integrated vectorization and agentic retrieval with the alternatives in PostgreSQL and Cosmos DB.
- **Getting documents in** 🚧 — Compare Content Understanding and Document Intelligence for OCR, layout and field extraction. Follow the path from an incoming document to text and structure suitable for RAG.
- **Agents on Azure** 🚧 — Compare Foundry Agent Service with a self-hosted Microsoft Agent Framework application. Work through tools, MCP, memory, multi-agent orchestration and approval points.
- **Evaluation and tracing** 🚧 — Map Foundry evaluations and tracing to the evaluation ideas in [RAG & Agents](/rag-agents/). Distinguish offline checks from online evaluation and decide what evidence each supplies.
- **The AI gateway** 🚧 — Place API Management in front of model deployments and work through token limits, load balancing, failover, semantic caching and usage logging. Decide which controls belong at that shared boundary.
- **Enterprise-grade AI** 🚧 — Bring private model access, keyless authentication and data residency together in an AI landing zone. Review the whole access path rather than securing each service in isolation.
- **Copilot Studio and the Power Platform** 🚧 — Orient yourself among Power Apps, Power Automate, Dataverse and Copilot Studio. Decide when a low-code workflow fits and where it should call a custom API.

## Prerequisites \{#prerequisites}

Part I’s identity lessons and deployment foundations: resource organisation, compute and infrastructure
as code. You should be able to explain which identity calls a service and how its resources are created.
Use [RAG & Agents](/rag-agents/) for the retrieval, agent and evaluation ideas applied here; Part II is useful
when you implement the .NET exercises.

## What changes after this part \{#what-changes-after-this-part}

You can trace an AI request from application identity through model access and retrieval to the answer,
and explain how you will evaluate it. You can compare managed and self-hosted agent designs, place gateway
controls deliberately and discuss the networking, residency and cost constraints around the service.

:::note[Status]

Published: 0 of 10 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
