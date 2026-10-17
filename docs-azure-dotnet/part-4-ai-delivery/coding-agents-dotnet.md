---
title: Coding agents on a .NET codebase
sidebar_position: 2
last_verified: 2026-10-17
---

# A coding agent proposes a change; your checks decide whether it belongs

A generated patch can compile and still return an invented citation. It can also make a failing check
disappear by removing the assertion that exposed the defect. Neither problem is specific to generated
code, but an agent can change the implementation and its tests in the same pass. You need an acceptance
criterion outside that pass.

For P1, the RAG service, give the agent a bounded task, the repository's conventions and a way to run
checks. Then inspect the resulting evidence and diff. Azure is the application's deployment target;
using a coding agent does not require giving it access to the deployed service.
Your Azure subscription does not grant coding-agent access; the client's plan and repository policy
govern that separately.

## How it works on Azure \{#how-it-works-on-azure}

In [Visual Studio agent mode](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=visualstudio),
GitHub Copilot can inspect the codebase, edit files, invoke tools and terminal commands, observe their
results and iterate. You stay in the IDE while it works. A suggested answer becomes a sequence of
actions: read the endpoint, change a test, run it, inspect the failure, patch the endpoint and rerun.

The remote worker is now called
[Copilot cloud agent](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github).
It works in an ephemeral development environment against a GitHub-hosted repository and can prepare
changes on a branch and open a pull request. The backend, then called Copilot coding agent,
[became generally available in September 2025](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/).
This exercise uses IDE agent mode; the separate **Agent (Preview)** option described in the
[Visual Studio release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes)
has its own preview status, independent of the cloud backend's GA announcement.

Repository custom instructions give either workflow project context. Visual Studio supports
[`.github/copilot-instructions.md` and path-specific instruction files](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context?view=visualstudio).
The former covers the repository; `.github/instructions/*.instructions.md` files use `applyTo` globs
to select paths. Put shared validation commands in the repository file; reserve path-specific
instructions for conventions that actually differ. Check the
[client support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support)
before assuming another client reads the same files.

Model Context Protocol (MCP) connects an AI client to tools and context exposed by an MCP server.
In [Visual Studio's MCP support](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=visualstudio),
agent mode can use selected server tools; servers can run as local processes or be reached remotely.
For example, the [Microsoft Learn MCP server](https://learn.microsoft.com/en-us/training/support/mcp)
exposes documentation search, page fetching and code-sample search at `https://learn.microsoft.com/api/mcp`.
It gives the agent a documentation lookup mechanism. It does not verify that an edit is correct.

## Choosing and tradeoffs \{#choosing-and-tradeoffs}

Use IDE agent mode when the task needs frequent clarification or you want to inspect intermediate
changes. Remote work suits an asynchronous task whose inputs and acceptance criteria are already in
the repository. It also exposes missing setup: an agent cannot reproduce a local success that depends
on an undocumented file on your laptop.

Do not send a broad remote implementation task while architecture decisions or setup steps remain
unresolved. Settle those first. For diagnosis that must leave files untouched, use a read-only workflow
with editing tools disabled. A terminal agent is a poor fit when the required checks depend on IDE or
platform tools unavailable in its environment; choose an environment that can produce the evidence.

A terminal agent is another option for the same checkout. Microsoft's
[Learn MCP getting-started guide](https://learn.microsoft.com/en-us/training/support/mcp-get-started)
includes GitHub Copilot CLI and Claude Code. Choose by repository access, tool permissions and whether
the client can run your checks. A shared protocol does not guarantee shared instruction discovery.

Tool access matters more than the chat surface. Visual Studio's
[agent-mode documentation](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=visualstudio)
warns that terminal commands run with the Visual Studio process's permissions; solution visibility is
not a filesystem sandbox. Review tool confirmations before broadening approval. Give a documentation
lookup server documentation access, and keep production credentials out of the development task.

Instructions help the agent choose the right command. They cannot enforce a passing result or prevent
an authorised tool from editing a test. The AI SDLC lesson
[An instruction is not a control](/ai-sdlc/part-1-foundation/rules-that-hold) explains that distinction.
Keep build, test and formatting checks in CI as well as in the instructions.

## In an AI workload \{#in-an-ai-workload}

P1 is an ASP.NET Core API answering questions with citations. Its target design uses a Foundry model
and Azure AI Search, with managed identity for application access and OIDC for deployment. The task
here changes the API's citation contract; it does not need a deployed service.

Keep three identities separate: the coding agent's development access, the running application's
managed identity and the deployment workflow's OIDC identity. A citation-validation patch needs no
production role. Apply the recommendations in
[Secrets](/ai-sdlc/part-4-platform/secrets) and
[Least privilege and sandboxing](/ai-sdlc/part-4-platform/least-privilege-sandboxing)
when deciding which tools and credentials the task receives.

The [AI SDLC course](/ai-sdlc/) owns the development method. Use its
[loop](/ai-sdlc/part-2-loop/plan-review-implement-critic)
and [layered gates](/ai-sdlc/part-3-verification/layered-gates) for this change.
A deterministic test can establish that a cited document ID belongs to the retrieved set. It cannot
establish that the document supports the answer. Retrieval, prompt or model changes also need
[answer-quality evaluation](/rag-agents/part-1-rag/cross-cutting/evaluation).

## Try it \{#try-it}

Extend the standalone `P1Testing.slnx` fixture from
[Testing](../part-2-modern-dotnet/testing.md). Preserve its package versions and any existing SDK pin.
Use the .NET 10 SDK. For Visual Studio agent mode, use **Visual Studio 2026 18.0 or later** on a
[supported Windows version](https://learn.microsoft.com/en-us/visualstudio/releases/2026/vs-system-requirements):
Microsoft's [SDK/Visual Studio support matrix](https://learn.microsoft.com/en-us/dotnet/core/porting/versioning-sdk-msbuild-vs#targeting-and-support-rules)
requires 18.0+ for supported `net10.0` targeting; choose a compatible SDK/IDE pairing from that matrix.
On other environments, use a terminal client such as GitHub Copilot CLI or Claude Code with the SDK
and the client's supported instructions setup, as linked above.

Work on a branch in a GitHub repository containing the fixture at its root. Run the validation sequence
below before assigning the task, and settle pre-existing formatting differences separately. If the fixture
has no `global.json`, add one whose `sdk.version` is the exact installed .NET 10 SDK
version reported by [`dotnet --version`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet#options).
Keep an existing compatible pin. The [SDK selection rules](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json)
apply locally and in CI. Use `.editorconfig` where present; otherwise the formatter uses its defaults.
Once these tests join a differently named P1 solution,
adapt the solution filename in the instructions and CI together.

**Verification status:** the commands were checked against live CLI references on 2026-10-18. This
combined exercise and CI workflow have not been executed. No Azure subscription is available yet,
and no commands here
have been run against a live subscription. The expected results below are conditional on completing
the preceding labs and installing their toolchains.

In your editor, create `.github/copilot-instructions.md` at the fixture's root with this full content.
The .NET commands belong inside the instructions because an agent working on this codebase needs its
actual build, test and style checks.

```markdown
# P1 development instructions

Work from the repository root. Keep changes within the requested task.
Preserve package pins and any existing SDK pin in global.json.
Use .editorconfig as the style authority where present; otherwise use formatter defaults.
Do not remove or weaken tests to obtain a passing result.
Do not change dependencies, infrastructure or CI without a separate requirement.

Validation commands, in order:
- Restore: `dotnet restore P1Testing.slnx`
- Build: `dotnet build P1Testing.slnx --configuration Release --no-restore`
- Test (VSTest): `dotnet test P1Testing.slnx --configuration Release --no-build`
- Style: `dotnet format P1Testing.slnx --verify-no-changes --no-restore`

Report command exit statuses, discovered test counts and any checks not run.
Explain the behaviour changed and identify the tests that demonstrate it.
```

These commands use the documented
[restore](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-restore),
[build](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build),
[VSTest test](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test-vstest) and
[format](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format) interfaces.
In Visual Studio, enable repository instructions and confirm the file appears in the response's
References before relying on it.

Before the agent task, add `.github/workflows/p1-checks.yml` in that fixture repository, using
GitHub's [.NET CI pattern](https://docs.github.com/en/actions/tutorials/build-and-test-code/net).
This small workflow runs the same four checks on pull requests; it has no deployment step.
The pinned [checkout release](https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1)
and [setup-dotnet release](https://github.com/actions/setup-dotnet/releases/tag/v5.0.1) identify the action code;
[`global-json-file`](https://github.com/actions/setup-dotnet/blob/v5.0.1/README.md#using-the-global-json-file-input)
installs the SDK selected above. The [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
defines the trigger, runner and token permissions.

```yaml
name: P1 checks
on: [pull_request]
permissions:
  contents: read
jobs:
  p1-checks:
    name: P1 checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - uses: actions/setup-dotnet@2016bd2012dba4e32de620c46fe006a3ac9f0602 # v5.0.1
        with:
          global-json-file: global.json
      - run: dotnet restore P1Testing.slnx
      - run: dotnet build P1Testing.slnx --configuration Release --no-restore
      - run: dotnet test P1Testing.slnx --configuration Release --no-build
      - run: dotnet format P1Testing.slnx --verify-no-changes --no-restore
```

Open a baseline PR, confirm `P1 checks` succeeds and merge the reviewed setup before assigning the
citation task on a new branch. Keep this workflow outside the agent's patch. Where repository settings permit, make it a
[required status check](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging).

Give the agent this task in Visual Studio agent mode with the setup above, or through your terminal
client. A GitHub issue assigned through the cloud-agent UI is an
optional remote route if your plan, repository and organisation policy allow it.

> Add a new citation-validation rule to `/ask`. The existing model interface returns plain text;
> preserve the successful fake's `Fixed test answer.` and the response citation `doc-1`.
> For this exercise, treat inline `[doc-N]` markers, where N is a positive integer, as document IDs.
> Validate every such marker against the IDs in the retrieved context supplied to the model.
> If any marker names an absent ID, return HTTP 502 with an empty response body.
>
> Add a failing HTTP test first: retain context containing only `[doc-1]`, and use a negative model
> fake returning `Unsupported answer [doc-2].`. Assert the status and empty body. Add a positive case
> returning an answer with `[doc-1]`, which must remain HTTP 200, and a mixed case containing
> `[doc-1]` and `[doc-2]`, which must return the empty HTTP 502. Preserve every existing test.
> Stop with the failing output for review, then implement the smallest patch after that review;
> do not weaken assertions or change packages or CI.

This is a **new acceptance criterion**, not behaviour promised by the previous lab. Derive the allowed
IDs from the context fixture; banning the literal `doc-2` or checking the response's hardcoded citation
array would miss the requirement. A later structured model response can replace inline markers;
changing that interface is outside this patch.

Inspect the first failing test's output before allowing implementation. Afterwards, run the full
validation sequence and inspect the diff. Require discovered tests, including the old cases and the
new ones; an exit status without discovery evidence is insufficient. Open the task PR and require a
successful `P1 checks` run for its current revision, rerunning after edits. Save the run URL, tested
commit SHA and test-discovery output with the task, alongside the initial failing output. Completion
requires both local results and that CI evidence; local success alone leaves the exercise incomplete.
Read logs and assertions rather than accepting the agent's summary as proof.

For a remote PR, review any workflow edits before approving workflow execution. GitHub
[requires approval by default for cloud-agent PR workflows](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations),
but automatic execution can be configured. Do not assume that pause will protect every repository.

**Cost:** editing and local checks create no Azure resources. The
[Learn MCP server](https://learn.microsoft.com/en-us/training/support/mcp) requires no authentication
and has no charge. Agent use remains subject to your plan's
[AI credits and allowances](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing);
remote cloud-agent work also consumes
[GitHub Actions minutes](https://docs.github.com/en/copilot/tutorials/cloud-agent/pilot-cloud-agent).
The PR workflow is also subject to [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).

**Teardown:** keep reviewed instructions, tests, SDK pin and CI workflow you intend to reuse; close
disposable PRs and remove their workspaces when finished if desired. This exercise requires no Azure
resource deletion.

## What to take away \{#what-to-take-away}

- Choose local or remote execution by the task's context, permissions and reproducibility needs.
- Version useful instructions, then enforce build, test and style requirements through checks.
- Keep coding-agent access separate from application and deployment identities.
- Verify citation-ID membership deterministically; evaluate whether the cited text supports the answer separately.

**[New terms](../glossary.md#coding-agents-dotnet)**: agent mode, Copilot cloud agent, repository custom instructions, path-specific instructions, MCP server.

## Sources \{#sources}

Verified as of 2026-10-17. Revised claims and commands rechecked on 2026-10-18.

- Visual Studio: [agent mode](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=visualstudio), [release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes), [custom instructions](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context?view=visualstudio), [MCP servers](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=visualstudio).
- GitHub: [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github), [coding agent GA announcement](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/), [custom instruction support](https://docs.github.com/en/copilot/reference/custom-instructions-support).
- Microsoft Learn MCP: [server capabilities, access and cost](https://learn.microsoft.com/en-us/training/support/mcp), [client setup](https://learn.microsoft.com/en-us/training/support/mcp-get-started).
- GitHub: [agent risks and mitigations](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations), [Copilot billing](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing), [cloud-agent pilot and Actions usage](https://docs.github.com/en/copilot/tutorials/cloud-agent/pilot-cloud-agent).
- .NET CLI: [restore](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-restore), [build](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build), [test with VSTest](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test-vstest), [format](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format).
- .NET prerequisites: [Visual Studio system requirements](https://learn.microsoft.com/en-us/visualstudio/releases/2026/vs-system-requirements), [SDK/Visual Studio support matrix](https://learn.microsoft.com/en-us/dotnet/core/porting/versioning-sdk-msbuild-vs), [SDK selection with global.json](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json), [dotnet options](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet).
- CI: [.NET build/test pattern](https://docs.github.com/en/actions/tutorials/build-and-test-code/net), [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [required checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [checkout pin](https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1), [setup-dotnet v5.0.1](https://github.com/actions/setup-dotnet/releases/tag/v5.0.1), [SDK setup input](https://github.com/actions/setup-dotnet/blob/v5.0.1/README.md#using-the-global-json-file-input), [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).
