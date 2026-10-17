---
id: overview
title: Part II — Modern .NET
sidebar_label: "Part II — Modern .NET"
last_verified: 2026-10-17
---

# Part II — Modern .NET

A model call is a small part of an application. The service also needs an HTTP API, configuration, data
access, tests and a way to handle long requests. Part II develops that application foundation in modern .NET:
first the platform and request pipeline, then shared services, async work, persistence and testing, followed
by containers and AI integration.

*Where this sits on [the course map](../intro.md#course-map): inside the application — the .NET service that the Azure platform will host.*

## What's inside \{#whats-inside}

{/* slugs: dotnet-platform, aspnet-core, extensions-backbone, async-streaming-cancellation, data-access, testing, containers-and-aspire, ai-in-dotnet */}

- **[The .NET platform today](./dotnet-platform.md)** — runtime, SDK, LTS cadence, SDK-style project files, `dotnet` CLI and NuGet. The Framework-to-.NET table and support cadence inform the choice of platform and supported version for a project.
- **[ASP.NET Core](./aspnet-core.md)** — hosting, middleware, routing and problem details. Minimal APIs and controllers offer different ways to organise HTTP endpoints.
- **The Microsoft.Extensions backbone** 🚧 — dependency injection lifetimes, configuration providers, the options pattern and logging. These are the shared mechanisms the rest of the service uses.
- **Async, streaming and cancellation** 🚧 — tasks, `IAsyncEnumerable`, server-sent events, timeouts and cancellation. Long LLM calls need both incremental responses and a way to stop work.
- **[Data access](./data-access.md)** — EF Core migrations, change tracking and performance traps. Dapper and raw SQL are alternatives when EF Core is not the right fit.
- **Testing** 🚧 — xUnit, integration tests with `WebApplicationFactory`, Testcontainers and LLM-backed code. A model dependency changes what the tests need to check.
- **Containers and Aspire** 🚧 — container images from `dotnet publish`, the Aspire app host, local orchestration and telemetry. Aspire brings related services and their telemetry into the local development environment.
- **AI in .NET** 🚧 — `Microsoft.Extensions.AI`, Azure OpenAI and OpenAI SDKs, vector data abstractions and Microsoft Agent Framework for .NET. Each integration serves a different role in the application.

## Prerequisites \{#prerequisites}

No lesson from Part I is a strict prerequisite: you can work through the application locally before
learning Azure. Bring experience with C# or another typed language; prior knowledge of modern .NET is not
required.

## What changes after this part \{#what-changes-after-this-part}

You can assemble an ASP.NET Core application with configuration, dependencies, data access and tests,
package it as a container and inspect local telemetry with Aspire. You can organise a long model call,
stream its response and cancel work when the request is no longer needed.

:::note[Status]

Published: 3 of 8 lessons. Pages marked 🚧 are planned.

:::

## Sources \{#sources}

Verified as of 2026-10-17.

- [Introduction to .NET](https://learn.microsoft.com/en-us/dotnet/core/introduction)
