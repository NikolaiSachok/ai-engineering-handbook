---
id: overview
title: Part IV — AI-assisted delivery on the Microsoft stack
sidebar_label: "Part IV — AI-assisted delivery on the Microsoft stack"
last_verified: 2026-10-17
---

# Part IV — AI-assisted delivery on the Microsoft stack

Parts I–III describe a service and the platform it needs. Part IV works through how a change reaches that
service: first a deployment pipeline with an explicit identity, then coding agents working inside the
repository’s checks, then a release whose effects you can observe and reverse. That order keeps generated
code inside the same delivery process as any other change.

*Where this sits on [the course map](../intro.md#course-map): from a reviewed change to a running service — the delivery path and its checks.*

## What's inside \{#whats-inside}

{/* slugs: pipelines-to-azure, coding-agents-dotnet, releasing-safely */}

- **[Pipelines to Azure](./pipelines-to-azure.md)** — GitHub Actions, Azure DevOps Pipelines, OIDC federation, environments, approvals and `azd` in CI. Federation gives the pipeline access without a stored deployment secret.
- **[Coding agents on a .NET codebase](./coding-agents-dotnet.md)** — GitHub Copilot agent mode, the coding agent, custom instructions and other agents on .NET repositories. The loop and gates from [AI SDLC](/ai-sdlc/) apply to their changes.
- **Releasing safely** 🚧 — deployment slots, Container Apps revisions, traffic splitting, rollback, IaC drift and supply-chain checks. Slots and revisions support controlled releases and rollback.

## Prerequisites \{#prerequisites}

Parts I–III: you need the Azure resource and identity model, a .NET application you can test, and an AI
workload whose behaviour you can evaluate. Return to the relevant lessons at each delivery step.
[AI SDLC](/ai-sdlc/) supplies the agent workflow and verification ideas applied here.

## What changes after this part \{#what-changes-after-this-part}

You can explain how a pipeline authenticates to Azure and where environments, approvals and coding-agent
checks fit. You can compare deployment slots and Container Apps revisions, plan traffic splitting and
rollback, and include infrastructure drift and supply-chain checks in a release.

:::note[Status]

Published: 2 of 3 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Azure Developer CLI overview](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/overview)
