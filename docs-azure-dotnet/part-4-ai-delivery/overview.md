---
id: overview
title: Part IV — AI-assisted delivery on the Microsoft stack
sidebar_label: Part overview
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

- **Pipelines to Azure** 🚧 — Compare GitHub Actions and Azure DevOps Pipelines for deploying the service. Work through OIDC federation, environments, approvals and `azd` in CI without introducing a stored deployment secret.
- **Coding agents on a .NET codebase** 🚧 — Use GitHub Copilot and other coding agents within a .NET repository, including agent workflows and custom instructions. Apply the loop and gates from [AI SDLC](/ai-sdlc/) to changes you can build and review.
- **Releasing safely** 🚧 — Plan deployment slots, Container Apps revisions, traffic splitting and rollback around observable release behaviour. Include infrastructure drift and supply-chain checks in the release decision.

## Prerequisites \{#prerequisites}

Parts I–III: you need the Azure resource and identity model, a .NET application you can test, and an AI
workload whose behaviour you can evaluate. [AI SDLC](/ai-sdlc/) supplies the agent workflow and verification
ideas that this part applies to the Microsoft stack.

## What changes after this part \{#what-changes-after-this-part}

You can describe a change’s path from repository to Azure, including its deployment identity, checks and
approval points. You can give a coding agent bounded work and review the result, then plan a release with
signals that tell you when to continue and a rollback you can carry out.

:::note[Status]

Published: 0 of 3 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Azure Developer CLI overview](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/overview)
