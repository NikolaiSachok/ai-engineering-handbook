---
id: intro
title: Introduction
sidebar_position: 1
slug: /
last_verified: 2026-10-17
---

# How to read this course

This course teaches you to design, build, secure and run a production-shaped LLM service on Azure in
.NET, and to defend each choice in an architecture review.

It is written for a senior engineer with little cloud experience, or only a loose knowledge of a cloud
other than Azure. You may last have written .NET in the .NET Framework era, or never. Production
engineering experience is assumed; Azure and modern .NET knowledge are not.

Each Azure concept starts with the problem it solves, then explains how Azure's mechanism works. No
explanation assumes you already know AWS or Google Cloud. Microsoft Learn is linked for the fine detail,
while the lessons concentrate on choices, tradeoffs and failure modes.

AI workloads run through every part: identity matters
because a service needs access to a model and its data; deployment matters because a change must be
tested, observed and reversible.

For the AI ideas the course assumes, use [RAG & Agents](/rag-agents/) and [AI SDLC](/ai-sdlc/).
Their lessons explain retrieval, agents, evaluation and the development workflow; this course links
back to them rather than teaching those ideas again.

## The course map \{#course-map}

| Part | What you will work through |
|---|---|
| [I — Azure foundations](./part-1-azure-foundations/overview.md) | Identity, networking, compute, data, messaging, infrastructure, observability and governance for an AI service. |
| [II — Modern .NET](./part-2-modern-dotnet/overview.md) | The platform, web services, configuration, async streaming, data access, testing and AI integration. |
| [III — Running LLMs on Azure](./part-3-llms-on-azure/overview.md) | Models, retrieval, agents, safety, evaluation and the gateway around them. |
| [IV — AI-assisted delivery on the Microsoft stack](./part-4-ai-delivery/overview.md) | Pipelines, coding agents and releases you can check and roll back. |
| [V — Projects](./part-5-projects/overview.md) | Build guides that join the lesson exercises into services you can run and explain. |

The appendices are references to return to:

- [Azure recap sheet](./recap-sheet.md) — the whole platform on a few pages, for revision.
- [Exam map](./exam-map.md) — AI-103 and AI-200 skill areas matched to lessons and project steps.
- [Glossary](./glossary.md) — one definition for each course term.

## How a lesson works \{#how-a-lesson-works}

A lesson opens with the problem, explains the Azure or .NET mechanism, then compares choices and
their failure modes. It then shows what each choice changes for an AI workload, before you try it yourself.
The closing sections collect what to take away, new terms and sources.

Every **Try it** step advances a project. It gives commands and an expected result, carries a cost
note, and ends with teardown. Read the cost note before creating resources; complete the teardown
before leaving the lab.

The projects give those steps a destination:

- **[P1 — RAG service](./part-5-projects/rag-service.md):** a .NET API answering questions over a small public document set, with citations.
- **[P2 — Agent behind an AI gateway](./part-5-projects/agent-behind-gateway.md):** a tool-calling agent with approvals and a gateway controlling access.
- **[P3 — Optional ingestion pipeline](./part-5-projects/ingestion-pipeline.md):** process incoming documents and update the retrieval index.

## Budget for the exercises \{#budget}

Use the free account's credit first. **As of 2026-10-17**, the
[Azure account offer](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)
gives eligible new customers **USD 200 to use within 30 days**. Continuing after 30 days or once the
credit is used up, whichever comes first, requires moving to pay-as-you-go.

After the credit, the course's learning budget is **USD 10 per month**, with alerts at 50%, 80% and
100%. This is a target to plan the exercises around, not a guaranteed bill. An
[Azure budget sends alerts; it does not stop consumption or affect running resources](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).
That is why every lab ends with teardown.

## Using the course for certification \{#certification}

The exam map connects the course to **AI-103 — Developing AI Apps and Agents on Azure** and
**AI-200 — Developing AI Cloud Solutions on Azure**. Both current study guides expect Python:
[AI-103](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)
expects experience developing applications in it;
[AI-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)
expects proficiency in Python programming.

The projects here use .NET. If you are preparing for either exam, add the Python learning paths linked
from each study guide's *Get trained* row: the .NET projects alone do not build the Python experience
both guides expect.

## Reading a page later \{#freshness}

Azure renames products and retires model versions. Azure AI Foundry is now Microsoft Foundry, and its
classic portal has a [migration guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic);
model versions follow a published
[lifecycle and retirement policy](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements).
Every page carries a visible "Verified as of" date and a Sources list. Code examples name the runtime and package versions they
were compiled against and state whether they were also run against live Azure. Check those details
when an example behaves differently from the current platform.

## Where to start \{#where-to-start}

Start with [How Azure is organised](./part-1-azure-foundations/how-azure-is-organised.md), the first lesson of
Part I. The [RAG & Agents](/rag-agents/) course covers the retrieval ideas the first project builds on.

## Sources \{#sources}

Verified as of 2026-10-17.

- [Azure account offer](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)
- [Create and manage Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [Study guide for Exam AI-103](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)
- [Study guide for Exam AI-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)
- [Migrate from the Foundry (classic) portal](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic)
- [Foundry Models lifecycle and support policy](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements)
