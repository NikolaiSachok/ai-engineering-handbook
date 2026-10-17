---
id: overview
title: Part II — Modern .NET
sidebar_label: Part overview
last_verified: 2026-10-17
---

# Part II — Modern .NET

Part II turns a service design into a .NET application you can build, test and run. It starts with the
platform and request pipeline, then the shared application services that hold configuration and dependencies.
Async work, persistence and testing come before containers and AI integration, so a model call becomes part
of an application whose behaviour you can inspect.

*Where this sits on [the course map](../intro.md#course-map): inside the application — the .NET service that the Azure platform will host.*

## What's inside \{#whats-inside}

{/* slugs: dotnet-platform, aspnet-core, extensions-backbone, async-streaming-cancellation, data-access, testing, containers-and-aspire, ai-in-dotnet */}

- **The .NET platform today** 🚧 — Separate the runtime, SDK and package ecosystem, and learn the `dotnet` CLI and SDK-style project files. Use the Framework-to-.NET comparison and support cadence to orient a new or returning developer.
- **ASP.NET Core** 🚧 — Follow a request through hosting, middleware and routing. Choose between minimal APIs and controllers, and use problem details to make failures understandable to callers.
- **The Microsoft.Extensions backbone** 🚧 — Work through dependency injection lifetimes, configuration providers, the options pattern and logging. These are the shared mechanisms the rest of the service will use.
- **Async, streaming and cancellation** 🚧 — Use tasks, `IAsyncEnumerable` and server-sent events for long model calls. Make timeouts and cancellation part of the request path rather than leaving abandoned work running.
- **Data access** 🚧 — Work through EF Core migrations, change tracking and performance traps. Decide when a query warrants Dapper or raw SQL instead.
- **Testing** 🚧 — Combine xUnit, `WebApplicationFactory` and Testcontainers to test the application at different boundaries. Examine what changes when the code under test depends on an LLM.
- **Containers and Aspire** 🚧 — Package the service with `dotnet publish`, then work through an Aspire app host for local orchestration and telemetry. Connect the local development view to the application you will deploy.
- **AI in .NET** 🚧 — Place `Microsoft.Extensions.AI`, the Azure OpenAI and OpenAI SDKs, vector data abstractions and Microsoft Agent Framework in the application. Learn which layer each integration belongs to before choosing one.

## Prerequisites \{#prerequisites}

No lesson from Part I is a strict prerequisite: you can work through the application locally before
learning Azure. Bring experience with C# or another typed language; prior knowledge of modern .NET is not
required.

## What changes after this part \{#what-changes-after-this-part}

You can read a modern ASP.NET Core service and follow a request through its dependencies, configuration,
data access and model calls. You can add streaming and cancellation, test the important boundaries and
package the application for deployment, with enough understanding to review the code an agent produces.

:::note[Status]

Published: 0 of 8 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Introduction to .NET](https://learn.microsoft.com/en-us/dotnet/core/introduction)
