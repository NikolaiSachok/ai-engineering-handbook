---
title: Data access
sidebar_position: 5
last_verified: 2026-10-17
---

# Keep contexts short and schema changes deliberate

An agent pauses for approval, the process restarts, and the next request arrives at another instance.
If the conversation and pending action existed only in memory, the service has lost the information it
needs to continue. Persisting a chat transcript alone does not fix this: a sentence saying “approved”
must refer to a specific proposed action, with specific arguments, under the right user's authority.

The access layer turns that requirement into queries, updates and schema changes. Its mistakes are
less visible than a failed model call: loading an entire conversation history on every turn, saving an
outdated approval over a newer decision, or fetching another tenant's rows. Choose the database service
in the [Azure data lesson](../part-1-azure-foundations/data.md). Here the question is how your .NET
application uses it without losing control of the work it sends to the database.

## How it works in .NET \{#how-it-works-in-dotnet}

The examples target [.NET 10, the current LTS](https://learn.microsoft.com/en-us/dotnet/core/releases-and-support),
[supported through 14 November 2028](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core).
[EF Core 10 requires the .NET 10 SDK and runtime](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/whatsnew).
EF Core is an object-relational mapper: you describe entities and their relationships in C#, and a
[database provider translates LINQ queries](https://learn.microsoft.com/en-us/ef/core/querying/) into
the database's query language. PostgreSQL uses the [Npgsql EF Core provider](https://www.npgsql.org/efcore/).
The provider matters: SQL translation and database-specific features depend on it.

A `DbContext` represents a short unit of work. It holds the model, builds queries and tracks entity
changes until you save or discard them. In an API, `AddDbContext` normally registers it with a scoped
lifetime. It is [not thread-safe](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/):
await one operation before starting another on the same context. Parallel agent branches need separate
contexts. [Register `AddDbContextFactory<T>` and inject `IDbContextFactory<T>`](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/#use-a-dbcontext-factory)
to create a context for each unit of work, disposing it afterwards. Keeping one context for the life of
a conversation would create shared mutable state spanning model calls and human delays.

Entity queries [track results by default](https://learn.microsoft.com/en-us/ef/core/querying/tracking).
On a write path, that is useful: load a pending approval, validate the transition, change its state,
then call `SaveChangesAsync`. EF's [change tracker records entity states](https://learn.microsoft.com/en-us/ef/core/change-tracking/)
and determines which inserts, updates or deletes to send. On a read-only conversation list,
`AsNoTracking` avoids retaining those entities for later updates. Database permissions and tenant
filters still govern access.

Schema evolution is separate. Adding a property to a class does not add a column when you save an
entity. A [migration compares the model with its previous snapshot](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/)
and records schema operations in versioned files. Applying migrations changes the database; its migration
history records what has been applied. Keep the migration and snapshot alongside the model so a fresh
database can follow the same schema history.

Review the generated operations before applying them. A rename inferred as a drop and add can lose data.
For deployment, [generate a reviewable SQL script or a migration bundle](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying)
and use a schema-changing deployment identity separate from the application's runtime identity.
The [AI SDLC migration lesson](/ai-sdlc/part-4-platform/environments-migrations-data) owns the broader
expand–migrate–contract and restore discipline; EF generates the operations, but cannot decide whether
an old application instance still needs a column.

## Choosing and tradeoffs \{#choosing-and-tradeoffs}

Start with the query and update patterns you need. The choice can differ between a transactional approval
write and a reporting read over the same tables.

| Access path | Use it when | Avoid it when / responsibility you retain |
|---|---|---|
| EF Core with LINQ | Entity updates, relationships and migrations fit the application model. | A particular query translates poorly; inspect the SQL rather than hiding an expensive query behind convenient C#. |
| EF Core bulk update/delete | `ExecuteUpdateAsync` or `ExecuteDeleteAsync` can express a set-based change without loading entities. | You need tracked instances kept in sync or automatic concurrency checks; these APIs bypass the tracker. |
| SQL through EF Core | One query needs explicit SQL while the rest of the store benefits from EF. | `FromSql` entity results are tracked by default; SQL still needs safe parameters. |
| Dapper | You want to write SQL and map result rows to small .NET objects. | You expect it to supply EF's change tracker and schema migration workflow. |
| Raw Npgsql / ADO.NET | You need direct command, connection or reader control without an object mapper. | Manual mapping and resource management would add work without solving a measured problem. |

Microsoft's [EF Core and micro-ORM comparison](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/work-with-data-in-asp-net-core-apps)
explains the difference: Dapper leaves SQL to you, while EF adds query translation and change tracking.
That is a responsibility tradeoff, not proof that replacing EF makes your endpoint faster. Measure the
query under representative data and inspect its plan before changing libraries.

Before writing raw SQL, consider [EF's set-based update and delete APIs](https://learn.microsoft.com/en-us/ef/core/saving/execute-insert-update-delete):
they execute immediately, without loading entities or waiting for `SaveChanges`.

Several traps occur before mapper overhead matters. Lazy loading, or a query per row in a loop, can
produce [N+1 queries](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying): one query
for conversations, followed by a separate query for each conversation's approvals.
[Lazy loading is opt-in](https://learn.microsoft.com/en-us/ef/core/querying/related-data/lazy). Fetch the
needed shape deliberately. Project only the columns the endpoint returns, filter in the database, and
bound the result set before materialising it. Calling `ToListAsync` before filtering moves the remaining
work into application memory. Check that indexes match the filter and ordering; an index does not help
merely because it exists.

Adding more `Include` calls can create a different problem. Loading sibling collections in one query
can multiply rows through a [cartesian explosion](https://learn.microsoft.com/en-us/ef/core/querying/single-split-queries).
Split queries avoid that multiplication but introduce additional database round trips and consistency
considerations between queries. Choose after inspecting the result shape and required consistency.

A tracking query reuses an already tracked entity instance, which can save allocations when the same
entity appears repeatedly. A projection containing only scalar values has no entities to track.
Choose according to [the result shape and tracking rules](https://learn.microsoft.com/en-us/ef/core/querying/tracking).

When LINQ cannot express a query well, [EF's SQL APIs](https://learn.microsoft.com/en-us/ef/core/querying/sql-queries)
may be enough; introducing another mapper is optional. `FromSql` parameterizes interpolated values.
Building a string and handing it to `FromSqlRaw` does not provide that protection. Parameters represent
values, not arbitrary table or column names: choose identifiers from a fixed application allowlist.
A model-generated SQL fragment must never become executable query text merely because it parses.

## In an AI workload \{#in-an-ai-workload}

P2 adds a conversation and approval store to the P1 service behind its AI gateway. The gateway controls
access to the service; the store must still scope each operation to the authenticated tenant and resource.
Use a trusted identity from the request context for that filter, never a tenant supplied in tool arguments.
The [tool-use lesson](/rag-agents/part-2-agents/tool-use/) explains why your runtime, rather than the
model, owns execution and permission checks.

For Azure PostgreSQL, follow [RBAC and keyless access](../part-1-azure-foundations/rbac-and-keyless-access.md):
a configured managed identity can [authenticate with an Entra token](https://learn.microsoft.com/en-us/azure/postgresql/security/security-connect-with-managed-identity),
supplied at connection time instead of storing a database password in the connection string.

Store a proposal before asking a human to approve it. Bind the eventual decision to its conversation,
tool and exact arguments; changing the proposal requires a new decision. The exercise below models those
fields and a pending status. A complete approval workflow also needs the approver, decision time, expiry
and an enforceable transition policy so the runtime can establish who approved which action.

Two requests may load the same pending approval. [Optimistic concurrency](https://learn.microsoft.com/en-us/ef/core/saving/concurrency)
lets EF compare an original token value during an update and throw `DbUpdateConcurrencyException` if
another writer changed it. Marking `Status` as a concurrency token catches competing status changes;
it does not detect every edit to other fields. On a conflict, reload and re-evaluate the transition rather
than blindly replaying the write. Keep an approved proposal immutable in the application workflow.

For row-wide detection, Npgsql can [map a `uint` property configured with `IsRowVersion()` to PostgreSQL's
`xmin` system column](https://www.npgsql.org/efcore/modeling/concurrency.html), which changes whenever the row is updated.

Alternatively, a conditional `ExecuteUpdateAsync` can transition one identified approval from `Pending`
in a single statement. Include the trusted tenant/resource scope and expected state in its filter, then
require exactly one affected row before proceeding. These APIs [leave concurrency checks to the caller](https://learn.microsoft.com/en-us/ef/core/saving/execute-insert-update-delete#concurrency-control-and-rows-affected);
add the original token to the filter when the transition must also detect changes to other fields.

Persist related database changes together: with a supporting provider, one
[`SaveChanges` call is transactional](https://learn.microsoft.com/en-us/ef/core/saving/transactions).
Keep that transaction short. Waiting for a model or a human while holding it open couples database
resources to an unpredictable delay. An external tool action is outside that database transaction;
rolling back rows cannot undo an already sent request. Record execution state and design retries around
an idempotency key. The [durable-runs lesson](/rag-agents/part-2-agents/durable-runs/) covers who owns
that state and what a resumed run must check before acting again.

## Try it \{#try-it}

Prepare P2's PostgreSQL store and its first migration locally. This step generates schema files and
inspects a no-tracking read query; it does not provision PostgreSQL or execute reads or writes.

**Verification:** The code on this page was built with .NET SDK 10.0.402,
Npgsql.EntityFrameworkCore.PostgreSQL 10.0.3, Microsoft.EntityFrameworkCore.Design 10.0.13 and
dotnet-ef 10.0.13 on 2026-10-17. Every command below was run as written, and the results described
are from that run. No PostgreSQL server, live database or Azure subscription was used; none of these
steps connects to one.

With a .NET 10 SDK installed, create a disposable console project. The latest stable pins, verified
on 2026-10-17, are
[Npgsql provider 10.0.3](https://www.nuget.org/packages/Npgsql.EntityFrameworkCore.PostgreSQL/10.0.3),
[EF design package 10.0.13](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Design/10.0.13)
and [EF tool 10.0.13](https://www.nuget.org/packages/dotnet-ef/10.0.13).
Npgsql 10.0.3 accepts EF Core 10.0.13.

```bash
dotnet new console --framework net10.0 --output P2.Store
cd P2.Store
dotnet new tool-manifest
dotnet tool install --local dotnet-ef --version 10.0.13
dotnet package add Npgsql.EntityFrameworkCore.PostgreSQL --version 10.0.3
dotnet package add Microsoft.EntityFrameworkCore.Design --version 10.0.13
```

These use the documented [templates](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new-sdk-templates),
[local tool installation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-tool-install) and
[package command](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add).
Create `AgentStore.cs`:

```csharp
using Microsoft.EntityFrameworkCore;

namespace P2.Store;

public sealed class Conversation
{
    public Guid Id { get; set; }
    public required string TenantId { get; set; }
    public required string Title { get; set; }
}

public sealed class Approval
{
    public Guid Id { get; set; }
    public Guid ConversationId { get; set; }
    public required string Tool { get; set; }
    public required string Arguments { get; set; }
    public string Status { get; set; } = "Pending";
}

public sealed class AgentStore : DbContext
{
    public DbSet<Conversation> Conversations => Set<Conversation>();
    public DbSet<Approval> Approvals => Set<Approval>();

    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseNpgsql("Host=localhost;Database=p2;Username=p2");

    protected override void OnModelCreating(ModelBuilder model)
    {
        model.Entity<Conversation>().HasIndex(c => new { c.TenantId, c.Id });
        model.Entity<Approval>().HasOne<Conversation>().WithMany()
            .HasForeignKey(a => a.ConversationId)
            .OnDelete(DeleteBehavior.Restrict);
        model.Entity<Approval>().Property(a => a.Status).IsConcurrencyToken();
    }
}
```

The connection string names a local target without credentials; this exercise never connects to it.
The [parameterless context pattern](https://learn.microsoft.com/en-us/ef/core/cli/dbcontext-creation)
lets the migration tools obtain the model. When integrating into the API, configure the connection
through dependency injection and runtime configuration. The foreign key ties approvals to conversations;
restricted deletion prevents silently removing approvals with a conversation. It does not enforce tenant
authorisation or approval policy.

Replace `Program.cs` with the read path:

```csharp
using Microsoft.EntityFrameworkCore;
using P2.Store;

using var db = new AgentStore();
var tenantId = "demo"; // Synthetic trusted tenant for this local exercise.
var conversations = db.Conversations
    .AsNoTracking()
    .Where(c => c.TenantId == tenantId)
    .OrderBy(c => c.Id)
    .Take(20);

Console.WriteLine(conversations.ToQueryString());
```

[`ToQueryString`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.entityframeworkqueryableextensions.toquerystring?view=efcore-10.0)
returns a debugging representation of the SQL. To retrieve rows later, the service would materialise
the query asynchronously against the configured database; index use needs an execution plan.

Generate the migration and its SQL, then inspect the query:

```bash
dotnet ef migrations add InitialAgentStore
dotnet ef migrations script 0 InitialAgentStore --output migration.sql
dotnet run
```

As the [EF CLI reference](https://learn.microsoft.com/en-us/ef/core/cli/dotnet) describes, you get a
`Migrations` folder with the migration files and a model snapshot, plus `migration.sql`. Inspect the
script for the two tables, the approval foreign key with `ON DELETE RESTRICT` and the conversation index.
The console prints a tenant-filtered, ordered query with a 20-row cap; the tenant value and the cap
appear as parameters in comments above the `SELECT`. No rows are printed. Keep these files as the starting store schema for P2; applying it and testing
persistence against PostgreSQL remains a later integration step.

**Cost:** Free (local only, no Azure resources). The exercise generates local files and SQL; it uses no
hosted database or model calls.

**Teardown:** Delete the local `P2.Store` folder when finished. There is no database or Azure resource to
remove from this exercise.

## What to take away \{#what-to-take-away}

- Keep a `DbContext` short-lived; use separate contexts for concurrent agent branches.
- Track entities for deliberate updates. Use no-tracking reads, bounded results and appropriate projections
  where updates are unnecessary; inspect SQL before blaming the mapper.
- Treat migrations as reviewed schema changes. Saving an entity does not deploy a schema, and generated
  operations still need testing against PostgreSQL.
- Persist approvals against exact proposals, check concurrent transitions, and keep external tool retries
  separate from database transaction guarantees.

**[New terms](../glossary.md#data-access)**: object-relational mapper, EF Core, database provider, DbContext,
change tracking, no-tracking query, migration, model snapshot, projection, N+1 queries, cartesian explosion,
Dapper, parameterized SQL, optimistic concurrency, concurrency token, split query, migration bundle.

## Sources \{#sources}

Verified as of 2026-10-17.

**Platform and query behaviour**

- [.NET releases and support](https://learn.microsoft.com/en-us/dotnet/core/releases-and-support) and [current support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core)
- [What's new in EF Core 10](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/whatsnew)
- [Querying data](https://learn.microsoft.com/en-us/ef/core/querying/) and [how queries work](https://learn.microsoft.com/en-us/ef/core/querying/how-query-works)
- [DbContext lifetime and configuration](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/)
- [Change tracking](https://learn.microsoft.com/en-us/ef/core/change-tracking/), [tracking versus no-tracking](https://learn.microsoft.com/en-us/ef/core/querying/tracking) and [set-based updates/deletes](https://learn.microsoft.com/en-us/ef/core/saving/execute-insert-update-delete)
- [Efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying), [lazy loading](https://learn.microsoft.com/en-us/ef/core/querying/related-data/lazy) and [single versus split queries](https://learn.microsoft.com/en-us/ef/core/querying/single-split-queries)
- [SQL queries](https://learn.microsoft.com/en-us/ef/core/querying/sql-queries) and [EF Core versus micro-ORMs](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/work-with-data-in-asp-net-core-apps)
- [Npgsql EF Core provider](https://www.npgsql.org/efcore/), [Npgsql command and reader usage](https://www.npgsql.org/doc/basic-usage.html) and [Dapper project documentation](https://github.com/DapperLib/Dapper)

**Schema and consistency**

- [Migrations overview](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/) and [applying migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying)
- [Transactions](https://learn.microsoft.com/en-us/ef/core/saving/transactions), [concurrency conflicts](https://learn.microsoft.com/en-us/ef/core/saving/concurrency) and [Npgsql concurrency tokens](https://www.npgsql.org/efcore/modeling/concurrency.html)
- [Managed identity authentication to Azure PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/security/security-connect-with-managed-identity)
- [Indexes](https://learn.microsoft.com/en-us/ef/core/modeling/indexes), [foreign keys](https://learn.microsoft.com/en-us/ef/core/modeling/relationships/foreign-and-principal-keys) and [cascade delete behaviours](https://learn.microsoft.com/en-us/ef/core/saving/cascade-delete)

**Exercise reference**

- [.NET new templates](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new-sdk-templates), [dotnet new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new), [package add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add) and [tool install](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-tool-install) and [dotnet run](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-run)
- [EF CLI](https://learn.microsoft.com/en-us/ef/core/cli/dotnet), [design-time context creation](https://learn.microsoft.com/en-us/ef/core/cli/dbcontext-creation) and [ToQueryString API](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.entityframeworkqueryableextensions.toquerystring?view=efcore-10.0)
- [Npgsql provider 10.0.3](https://www.nuget.org/packages/Npgsql.EntityFrameworkCore.PostgreSQL/10.0.3), [EF design package 10.0.13](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Design/10.0.13) and [EF tool 10.0.13](https://www.nuget.org/packages/dotnet-ef/10.0.13)
