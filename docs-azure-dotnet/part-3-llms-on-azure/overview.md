---
id: overview
title: Part III — Running LLMs on Azure
sidebar_label: "Part III — Running LLMs on Azure"
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

- **[Microsoft Foundry](./microsoft-foundry.md)** — resources, projects, the model catalog, Azure OpenAI and models from other providers. The resource and project model organises access to those models.
- **[Model deployments, quotas and cost](./deployments-quotas-cost.md)** — Standard, Global, Data Zone and Provisioned deployments; TPM/RPM quotas and rate limiting. Deployment choices depend on throughput, residency and the cost model.
- **[Safety on the platform](./platform-safety.md)** — content filters, Prompt Shields and groundedness detection. The lesson identifies what platform safety does not cover and links to application guardrails in [RAG & Agents](/rag-agents/).
- **[RAG on Azure AI Search](./rag-on-ai-search.md)** — indexes, hybrid retrieval, semantic ranker, integrated vectorization and agentic retrieval. The comparison is between this AI Search path, pgvector and Cosmos DB vector search.
- **[Getting documents in](./document-ingestion.md)** — Content Understanding and Document Intelligence for OCR, layout, field extraction and Markdown for RAG. These services turn documents into text and structure for retrieval.
- **[Agents on Azure](./agents-on-azure.md)** — Foundry Agent Service versus self-hosted Microsoft Agent Framework; tools, MCP, memory, multi-agent orchestration and approvals. The hosting choice determines where the agent runs.
- **Evaluation and tracing** 🚧 — Foundry evaluations and tracing, mapped to the evaluation lesson in [RAG & Agents](/rag-agents/). Offline and online evaluation check behaviour at different stages.
- **The AI gateway** 🚧 — API Management token limits, load balancing, failover, semantic caching and usage logging. The gateway places these controls in front of model deployments.
- **Enterprise-grade AI** 🚧 — private networking for model endpoints, keyless access, data residency and the AI landing zone. Enterprise requirements constrain model access and data placement.
- **Copilot Studio and the Power Platform** 🚧 — Power Apps, Power Automate, Dataverse and Copilot Studio. The choice between low-code and custom code includes where a workflow should call a custom API.

## Prerequisites \{#prerequisites}

Part I’s identity lessons and deployment foundations: resource organisation, compute and infrastructure
as code. You should be able to explain which identity calls a service and how its resources are created.
Use [RAG & Agents](/rag-agents/) for the retrieval, agent and evaluation ideas applied here; Part II is useful
when you implement the .NET exercises.

## What changes after this part \{#what-changes-after-this-part}

You can compare model deployments, quotas and costs; AI Search, pgvector and Cosmos DB retrieval;
and managed versus self-hosted agents. You can identify the limits of platform safety and choose evaluation,
tracing and gateway controls while accounting for private access and data residency.

:::note[Status]

Published: 6 of 10 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
