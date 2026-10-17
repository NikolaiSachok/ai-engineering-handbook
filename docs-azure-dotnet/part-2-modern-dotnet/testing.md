---
title: Testing
sidebar_position: 6
last_verified: 2026-10-17
---

# Test the request path without calling the model

A question-answering API can return a plausible sentence while sending the wrong context to the model,
losing its citations or accepting an empty question. Reading a few responses will not reliably expose
those faults. You need repeatable checks that fail when the application's promised behaviour changes.

Calling a live model in every test makes the result harder to interpret. A failure might come from your
request handling, a dependency outage or a different answer. Separate the application behaviour you can
assert exactly from the answer quality you must evaluate. For the RAG service project, P1, that starts
with a request through `/ask` whose model dependency is under the test's control.

## How it works in .NET \{#how-it-works-in-dotnet}

The examples target **.NET 10**, the current LTS release, supported through **14 November 2028** according
to the [live support policy](https://dotnet.microsoft.com/en-us/platform/support/policy).
A test belongs at the smallest boundary that can expose the defect. Checking a function directly is a
unit test; sending a request through the application's HTTP pipeline checks several components working
together. The latter can catch a missing service registration or an incorrectly shaped JSON response
that a direct function call would bypass.

[xUnit](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-csharp-with-xunit) supplies
attributes and assertions for these tests. A `[Fact]` expresses one example; a `[Theory]` with
`[InlineData]` runs a check for several inputs. Arrange the inputs and dependencies, perform the action,
then assert the observable result. Return `Task` from an asynchronous test and await the operation so
the assertion sees its completion or failure.

For ASP.NET Core 10,
[`WebApplicationFactory<Program>`](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0)
starts the application using `TestServer`, an in-process test server. Its client sends requests through
the app's pipeline. You keep routing, parameter binding and response serialization, while changing the
dependencies supplied through dependency injection. This exercises the API without deploying it.

A **test double** stands in for a dependency; a **fake** is a working substitute with deliberately limited
behaviour. Here, the model fake records its input and returns fixed text. The test can distinguish “the
endpoint forwarded the question and context” from “the endpoint returned some text.” An assertion about
the request matters as much as one about the response.

Use the factory's `WithWebHostBuilder`, then `ConfigureTestServices` on its host builder to replace the
model registration, as the integration-testing reference shows. Keep that replacement in the test
project. A production environment switch that silently selects a fake would introduce another
deployment setting to get wrong.

## Choosing the boundary \{#choosing-the-boundary}

| Check | Keep real | Substitute | Do not use it to claim |
|---|---|---|---|
| Unit test | A validation or citation-mapping function | Its external dependencies | The HTTP endpoint is wired correctly. |
| API integration test | Application startup and request pipeline | Model client; retrieval fixture if needed | Azure access or answer quality works. |
| Container integration test | A chosen dependency's engine and client adapter | Disposable data and configuration | A different managed service behaves identically. |
| Deployed smoke test | Deployed app and selected service connections | A small, controlled test input | Broad answer-quality coverage. |
| Answer-quality evaluation | The pipeline being evaluated | A versioned evaluation dataset | Every error path obeys the API contract. |

A unit test is useful for many variations of a small rule: rejecting blank questions, for example.
Repeating every variation through HTTP adds setup without necessarily exposing another defect. Keep a
few HTTP cases that demonstrate binding and the public response, then expand the narrow tests when the
validation rules grow. Conversely, a suite that only calls handlers directly never checks whether the
application can resolve their dependencies.

[Testcontainers for .NET](https://dotnet.testcontainers.org/) manages disposable containers for test
dependencies and requires a Docker-API-compatible runtime. Use it when the bug depends on a real
engine: SQL translation, schema migrations or persistence across operations. For P1, do not add a
relational database just to demonstrate the library. Add container tests when a dependency you actually
use has an appropriate container image or emulator.
Aspire's [AppHost-level test harness](https://aspire.dev/testing/write-your-first-test/) belongs to
II.7, Containers and Aspire.

The lifecycle belongs to the test setup: start the container, wait until its service is usable, supply
its connection details to the app, seed known data, run assertions, then dispose it. The upstream
[best practices](https://dotnet.testcontainers.org/api/best_practices/) recommend pinned image versions
and dynamically assigned host ports. Fixed ports make parallel tests compete for the same address;
shared mutable data makes their results depend on execution order. Give each test isolated data or a
clear reset boundary, even when a container is shared across tests to reduce startup work.

A running container is not necessarily a ready service. Use an appropriate
[wait strategy](https://dotnet.testcontainers.org/api/wait_strategies/) rather than an arbitrary sleep.
A local container also establishes evidence only for the component inside it. Testing another search
engine locally cannot establish Azure AI Search compatibility, and an in-process HTTP test cannot
establish that a managed identity has permission to call a deployed service.

## In an AI workload \{#in-an-ai-workload}

P1 will combine retrieval from public documents with a Foundry model deployment and return citations.
Place the model call behind an application-owned interface so tests can supply fixed completions,
record the context sent to the model and simulate failures. Keep retrieval replaceable separately:
otherwise replacing the model could still leave ordinary API tests dependent on a live search index.
The exercise's `IModelClient` is a deliberately minimal application-owned port; II.8, AI in .NET,
introduces `Microsoft.Extensions.AI`'s
[`IChatClient`](https://learn.microsoft.com/en-us/dotnet/ai/ichatclient), to which the same substitution
technique applies.

Choose assertions about promises the service controls. Given a known document ID, does the response
include that ID? Does a blank question stop before the model call? Does the question reach the model
unchanged? Exact equality is useful for a fake's known output. It does not establish that a real model
will produce the same wording, or that the wording is a correct answer.

Citation wiring has a similar limit. Returning a source ID proves that the API preserved that reference;
it does not prove that the cited passage supports the answer. The
[RAG evaluation lesson](/rag-agents/part-1-rag/cross-cutting/evaluation/) owns the quality checks for
retrieval and generation. Run that evaluation when changing prompts, retrieval settings or model
versions, alongside application tests. The
[AI SDLC lesson on layered gates](/ai-sdlc/part-3-verification/layered-gates/) explains why checks with
different blind spots belong together.

As P1 grows, add controlled model failures and cancellation cases. A fake that throws a timeout lets
you check the API's chosen failure response without waiting for an outage. A cancellation-aware fake
can record whether cancellation reaches the dependency. Specify those behaviours before asserting
them; a test should enforce the service contract rather than preserve an accidental exception message.
Keep live-service checks separately identifiable so a credentials problem does not look like a broken
validation rule.

## Try it \{#try-it}

Build a local slice of P1: `/ask` with a fixed document and an integration test that replaces the model
client. Retrieval is a fixture here; Azure AI Search and the Foundry adapter come later. This slice
establishes the test boundary that the eventual service can retain.

**Verification status:** the commands and code below were run as written on 2026-10-17 with .NET SDK
10.0.402, `Microsoft.AspNetCore.Mvc.Testing` 10.0.13, `Microsoft.NET.Test.Sdk` 18.11.0, `xunit` 2.9.3,
`xunit.runner.visualstudio` 4.0.1 and `coverlet.collector` 10.1.0. The build produced no warnings,
`dotnet test` passed all three cases, and the `doc-2` change described below failed the
successful-request test. The exercise is local only, so no Azure subscription or live service was used.

Install the .NET 10 SDK and start in a new working directory outside an existing solution. These use the
built-in [templates](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new-sdk-templates),
[solution command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln),
[project-reference command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-reference-add)
and [package command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add).
The lab targets the .NET 10 SDK and pins these direct dependencies to the latest stable releases for
their package IDs as of the verification date:
[`Microsoft.AspNetCore.Mvc.Testing` 10.0.13](https://www.nuget.org/packages/Microsoft.AspNetCore.Mvc.Testing),
[`Microsoft.NET.Test.Sdk` 18.11.0](https://www.nuget.org/packages/Microsoft.NET.Test.Sdk/),
[`xunit` 2.9.3](https://www.nuget.org/packages/xunit),
[`xunit.runner.visualstudio` 4.0.1](https://www.nuget.org/packages/xunit.runner.visualstudio) and
[`coverlet.collector` 10.1.0](https://www.nuget.org/packages/coverlet.collector).
It retains the template's `xunit` v2 package, which NuGet now marks as legacy; xUnit v3 uses a separate
package. The package commands update the template's existing references as well as adding the test host.

```bash
mkdir p1-testing
cd p1-testing
dotnet new sln -n P1Testing
dotnet new web -n Rag.Api --framework net10.0
dotnet new xunit -n Rag.Api.Tests --framework net10.0
dotnet sln add Rag.Api/Rag.Api.csproj Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet reference add Rag.Api/Rag.Api.csproj --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add Microsoft.AspNetCore.Mvc.Testing --version 10.0.13 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add Microsoft.NET.Test.Sdk --version 18.11.0 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add xunit --version 2.9.3 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add xunit.runner.visualstudio --version 4.0.1 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add coverlet.collector --version 10.1.0 --project Rag.Api.Tests/Rag.Api.Tests.csproj
```

In `Rag.Api.Tests/Rag.Api.Tests.csproj`, change the opening element's `Sdk` attribute to
`Microsoft.NET.Sdk.Web`, following Learn's
[test-project prerequisites](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0#test-app-prerequisites).

Replace `Rag.Api/Program.cs` with the first snippet. The document is an invented local fixture. The
unconfigured client throws if called: the test must replace it. Later, the real adapter belongs behind
this same interface. The endpoint uses ASP.NET Core's documented
[body, service and cancellation-token binding](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/parameter-binding?view=aspnetcore-10.0).

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<IModelClient, UnconfiguredModelClient>();
var app = builder.Build();

app.MapPost("/ask", async (AskRequest request, IModelClient model,
    CancellationToken cancellationToken) =>
{
    if (string.IsNullOrWhiteSpace(request.Question))
        return Results.BadRequest();

    const string context = "[doc-1] This public sample describes the RAG service.";
    var answer = await model.GenerateAsync(
        request.Question, context, cancellationToken);
    return Results.Ok(new AskResponse(answer, ["doc-1"]));
});
app.Run();

public record AskRequest(string? Question);
public record AskResponse(string Answer, string[] Citations);
public interface IModelClient
{
    Task<string> GenerateAsync(string question, string context,
        CancellationToken cancellationToken);
}
public sealed class UnconfiguredModelClient : IModelClient
{
    public Task<string> GenerateAsync(string question, string context,
        CancellationToken cancellationToken) =>
        throw new InvalidOperationException("Configure a model adapter.");
}
```

.NET 10 [generates the public `Program` declaration](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-10.0?view=aspnetcore-10.0#better-support-for-testing-apps-with-top-level-statements)
itself, so no explicit declaration is needed.
Delete the generated `Rag.Api.Tests/UnitTest1.cs` and create `Rag.Api.Tests/AskTests.cs` with the second
snippet. It removes the original client registration before installing the fake, and keeps both the base
and customised factories in `using` declarations for disposal.

```csharp
using System.Net;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.AspNetCore.TestHost;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;
using Xunit;

namespace Rag.Api.Tests;

public sealed class AskTests
{
    [Fact]
    public async Task Ask_returns_answer_and_citation()
    {
        var fake = new FakeModelClient();
        using var baseFactory = new WebApplicationFactory<Program>();
        using var factory = CreateFactory(baseFactory, fake);
        using var client = factory.CreateClient();
        using var response = await client.PostAsJsonAsync(
            "/ask", new AskRequest("What does the sample describe?"));

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        var body = await response.Content.ReadFromJsonAsync<AskResponse>();
        Assert.NotNull(body);
        Assert.Equal("Fixed test answer.", body.Answer);
        Assert.Equal("doc-1", Assert.Single(body.Citations));
        Assert.Equal("What does the sample describe?", fake.Question);
        Assert.Equal(
            "[doc-1] This public sample describes the RAG service.", fake.Context);
    }

    [Theory]
    [InlineData("")]
    [InlineData("   ")]
    public async Task Ask_rejects_blank_question(string question)
    {
        var fake = new FakeModelClient();
        using var baseFactory = new WebApplicationFactory<Program>();
        using var factory = CreateFactory(baseFactory, fake);
        using var client = factory.CreateClient();
        using var response = await client.PostAsJsonAsync(
            "/ask", new AskRequest(question));

        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
        Assert.Null(fake.Question);
    }

    private static WebApplicationFactory<Program> CreateFactory(
        WebApplicationFactory<Program> baseFactory, FakeModelClient fake) =>
        baseFactory.WithWebHostBuilder(builder =>
            builder.ConfigureTestServices(services =>
            {
                services.RemoveAll<IModelClient>();
                services.AddSingleton<IModelClient>(fake);
            }));

    private sealed class FakeModelClient : IModelClient
    {
        public string? Question { get; private set; }
        public string? Context { get; private set; }

        public Task<string> GenerateAsync(string question, string context,
            CancellationToken cancellationToken)
        {
            cancellationToken.ThrowIfCancellationRequested();
            Question = question;
            Context = context;
            return Task.FromResult("Fixed test answer.");
        }
    }
}
```

From `p1-testing`, run the test project with
[`dotnet test`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test):

```bash
dotnet test Rag.Api.Tests/Rag.Api.Tests.csproj
```

The command should build the projects and run three cases: one successful request and two blank-question
inputs. The success case expects HTTP 200, the fixed answer and `doc-1`; the other cases expect HTTP 400
without a model call. As a check on the assertions, temporarily change the endpoint's citation to
`doc-2`: the successful-request test should fail. Restore it afterwards.

**Cost:** free (local only, no Azure resources). The exercise uses an in-process server and a fake model;
it needs no container runtime, Azure credentials or paid model calls.

**Teardown:** delete the local `p1-testing` folder when finished. There are no Azure resources to remove.

## What to take away \{#what-to-take-away}

- Put repeatable application rules in unit tests; exercise HTTP wiring with a focused integration test.
- Replace model dependencies through the test host and assert what reaches them as well as what comes back.
- Use Testcontainers for relevant real dependencies, with isolated data and an explicit readiness check.
- A fake-model test checks application behaviour. Use evaluation to check real answer quality and citation support.

**[New terms](../glossary.md#testing)**: unit test, integration test, xUnit, test double, fake, WebApplicationFactory, TestServer, Testcontainers, test fixture.

## Sources \{#sources}

Verified as of 2026-10-17.

- [.NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy)
- [Unit testing C# with xUnit](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-csharp-with-xunit)
- [Integration tests in ASP.NET Core 10](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0)
- [ASP.NET Core 10: testing top-level apps](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-10.0?view=aspnetcore-10.0#better-support-for-testing-apps-with-top-level-statements), [ASP0027: unnecessary public Program declaration](https://learn.microsoft.com/en-us/aspnet/core/diagnostics/asp0027?view=aspnetcore-10.0)
- [Minimal API parameter binding](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/parameter-binding?view=aspnetcore-10.0)
- [.NET CLI: new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new), [SDK templates](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new-sdk-templates), [sln](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln), [reference add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-reference-add), [package add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add), [test](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test)
- [Microsoft.AspNetCore.Mvc.Testing package](https://www.nuget.org/packages/Microsoft.AspNetCore.Mvc.Testing)
- Test packages: [Microsoft.NET.Test.Sdk](https://www.nuget.org/packages/Microsoft.NET.Test.Sdk/), [xunit](https://www.nuget.org/packages/xunit), [xunit.runner.visualstudio](https://www.nuget.org/packages/xunit.runner.visualstudio), [coverlet.collector](https://www.nuget.org/packages/coverlet.collector)
- [IChatClient abstraction](https://learn.microsoft.com/en-us/dotnet/ai/ichatclient), [Aspire: write your first test](https://aspire.dev/testing/write-your-first-test/)
- [Testcontainers for .NET](https://dotnet.testcontainers.org/), [best practices](https://dotnet.testcontainers.org/api/best_practices/), [wait strategies](https://dotnet.testcontainers.org/api/wait_strategies/)
