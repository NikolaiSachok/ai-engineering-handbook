---
title: Storing data
sidebar_position: 6
last_verified: 2026-10-17
---

# Choose storage from the reads and writes it must serve

A service can keep its source files, application records, search index and cached answers in one place.
The trouble starts when those uses pull in different directions. Updating a document should preserve enough
history to explain a citation. Updating a business record may require a transaction. Losing a cached answer
should cause another lookup, with no loss of authoritative data. “We need a database” leaves those decisions open.

Start with the operations: what identifies a record, which queries must be fast, which changes must happen
together, and how old a read may be. Then decide which data is authoritative and which you can rebuild.
For an AI service, this prevents a costly mistake: selecting every store because it supports
vectors, while leaving ownership, authorization and recovery undefined.

## How Azure stores different kinds of data \{#how-azure-stores-data}

[Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
holds objects such as PDFs, text files and images. A storage account provides their namespace; a container
groups blobs within that account; each blob has a name used to address it. Block blobs suit the source
documents in this course. Fetching an original by its name is a different operation from asking which
paragraphs best answer a question. Blob Storage owns the first job; P1 gives the second to Azure AI Search.

Relational state belongs behind a schema and transactions when relationships and coordinated updates matter.
[Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql)
is a managed relational service based on SQL Server. Azure handles platform work such as patching and
backups; you still design the schema, queries and application transactions. It also supports a native
[`vector` type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type) and
[`VECTOR_DISTANCE`](https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-distance-transact-sql). An ingestion-job table with
status, source version and completion time is a plausible use. Keeping that table does not require storing
the original document bytes in it.

[Azure Database for PostgreSQL flexible server supports pgvector](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-use-pgvector),
so relational records and vector retrieval can share a database. The extension's actual name is `vector`:
you allowlist it on the server and enable it in each database that needs it. This can remove a separate
retrieval store when PostgreSQL already owns the relevant records. It also makes retrieval queries compete
with the rest of the database workload. Measure that combined workload before deciding consolidation is simpler.

Azure Cosmos DB takes another approach. In its NoSQL model, a
[partition key](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning) groups related items into
logical partitions. Your key and queries determine how work spreads. A tenant identifier may be convenient
for tenant-local reads, but one exceptionally busy tenant can concentrate traffic. A query that cannot
restrict its partition scope may have to search across partitions.

Cosmos DB accounts for database work using
[request units](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units), or RUs: a normalized measure
of CPU, I/O and memory used by operations. Provisioned throughput expresses capacity in RU/s; serverless
billing accounts for consumed RUs. An RU is neither a row nor an HTTP request. Reading an item and running
a broad query can consume very different amounts. Inspect request charges with representative data and
filters before sizing capacity.

[Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview) keeps data in memory and supports
patterns such as cache-aside: look in the cache, fetch from the authoritative store on a miss, then cache the
result. Expiration and eviction make room or retire entries. That means the application needs a working miss
path. Microsoft's [security guidance](https://learn.microsoft.com/en-us/azure/redis/secure-azure-managed-redis)
positions it as a cache and temporary store rather than a primary persistent database.

## Choose by access pattern, then test the awkward case \{#choosing-and-tradeoffs}

Write down the most important read and update before comparing services. Include the operation that is
awkward for your preferred choice: a join, a large download, a cross-tenant query or a burst of cache misses.
That operation often reveals the boundary earlier than a happy-path benchmark.

| Service | A fitting access pattern | When to choose something else |
|---|---|---|
| Blob Storage | Store and fetch original files by name; retain inputs for reprocessing. | Queries require joins or transactional updates across application records. |
| Azure SQL Database | Relational state, constraints, transactions and SQL Server tooling, with native [`vector` and `VECTOR_DISTANCE`](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type) support. | The only need is named-file storage, or PostgreSQL compatibility is a requirement. |
| PostgreSQL flexible server + pgvector | Relational application data with vector retrieval close to those records. | Retrieval needs independent scaling or search features that your database design does not provide. |
| Cosmos DB for NoSQL | Document access organised around a deliberate partition key. | Frequent cross-partition queries or relational joins dominate the workload. |
| Azure Managed Redis | Repeated reads whose results can expire, be evicted or be reconstructed. | Losing an entry would lose the only authoritative copy. |

Blob's capacity price is only part of its cost. Its
[access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview/) trade storage
charges against access costs and retention assumptions. Hot is a reasonable starting point for documents
you repeatedly ingest during development. Cooler storage can cost more when documents are read or replaced
often; Archive requires rehydration before their contents can be read. An ingestion pipeline waiting for an
archived source is an access-pattern mismatch, even if its storage bill looks small.

For Cosmos DB, also choose what a successful read promises. Its
[five consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) give different
freshness and ordering guarantees:

| Level | Read guarantee to reason about |
|---|---|
| Strong | The latest committed item version. |
| Bounded staleness | Lag stays within a configured version or time bound. |
| Session | Guarantees such as reading your own writes within the session, using session tokens. |
| Consistent prefix | Writes appear in order, without gaps. |
| Eventual | Replicas converge when writes stop; freshness and ordering are not guaranteed. |

Session consistency does not mean that every independent API replica automatically shares a user's read
history. Design how session tokens travel when a request moves between clients. Strong and bounded-staleness
reads consume more RUs than weaker consistency choices. Choose the guarantee from the user-visible action:
a user confirming a just-saved record has different needs from a background report that tolerates lag.

Cosmos DB for NoSQL also offers
[integrated vector search](https://learn.microsoft.com/en-us/azure/cosmos-db/vector-search), with vectors
alongside operational items, embedding and index policies, filters and the `VectorDistance` query function.
Enable the account feature before configuring it.
[Vector search is unsupported on shared-throughput accounts and cannot be disabled once enabled on a container](https://learn.microsoft.com/en-us/azure/cosmos-db/vector-search#current-limitations).
This makes Cosmos a candidate when those documents already
live there; it does not settle partition design, request cost or retrieval quality. For the underlying
retrieval choices, use [Retrieval](/rag-agents/part-1-rag/retrieval/).

A Redis cache introduces a different failure mode: a fast answer that is no longer valid. Set an explicit
time to live, and decide which writes invalidate cached values. For example, a document update may need to
invalidate answers derived from the previous version.
[Expiration bounds reuse time; it cannot guarantee that a cached answer is still valid](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside#problems-and-considerations).

## In an AI workload, keep originals and derived data traceable \{#in-an-ai-workload}

[P1](../part-5-projects/rag-service.md) is an ASP.NET Core minimal API on Azure Container Apps. Its retrieval path uses Azure AI Search,
a Foundry model deployment and citations over a small public document set. Blob Storage holds the originals.
That division lets you rebuild the search index when parsing, chunking or embedding choices change. The
[Ingestion lesson](/rag-agents/part-1-rag/ingestion/) owns those transformations; this storage decision keeps
their input available.

Give each processed source a stable identifier and record the version that produced its indexed chunks.
Otherwise replacing a file can leave a citation pointing at text different from the text used to answer.
Treat the original, derived index and any answer cache as separate update targets, with an explicit rule
for when a new source version becomes searchable. A database transaction in one store cannot, by itself,
coordinate that whole sequence.

Access follows the component doing the work. The API gets
[Storage Blob Data Reader](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access)
for the source container, allowing reads and listing. A separate ingestion writer needs its own grant.
The API identity's access also does not decide which documents an end user may see; that belongs in the
retrieval authorization design. Keeping credentials out of application configuration follows the
[Secrets lesson](/ai-sdlc/part-4-platform/secrets). Here, Entra tokens and a data role replace an account-key
connection string.

## Try it \{#try-it}

Create P1's document container and a user-assigned identity for the future API. A
[user-assigned identity can be attached to a Container App](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity)
later, so this step does not require deploying the API. Use a local Bash shell with Azure CLI installed.
You need permission to create resources and assign roles, including
[`Microsoft.Authorization/roleAssignments/write`](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access).

The CLI references were checked; the commands have not been run against a live subscription for this
lesson. The results below are expected from the documented operations, not observed output. Follow
[lesson 1’s Try it](/azure-dotnet/part-1-azure-foundations/how-azure-is-organised#try-it) to select a learning subscription and set its budget;
this exercise recreates P1’s tagged resource group.

[Sign in](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest), replace the
subscription placeholder and [select it](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az-account-set).
Keep the same shell for the exercise:

```bash
az login
AZURE_SUBSCRIPTION_ID="<id>"
az account set --subscription "$AZURE_SUBSCRIPTION_ID"

AZURE_RESOURCE_GROUP="rg-p1-rag-dev-$RANDOM"
location='westeurope'
storage="p1docs${RANDOM}${RANDOM}"
container='sources'
az group create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$AZURE_RESOURCE_GROUP" --location "$location" \
  --tags project=p1-rag environment=dev owner=learner --output none
```

Create a standard general-purpose v2 account, then its container using the control plane. The
[account flags](https://learn.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az-storage-account-create)
explicitly disable Shared Key authorization and anonymous blob access. The
[`container-rm` command](https://learn.microsoft.com/en-us/cli/azure/storage/container-rm?view=azure-cli-latest#az-storage-container-rm-create)
uses the resource provider, so container creation needs no account key. If the generated account name is
already taken, choose another lowercase alphanumeric `storage` value and retry the account command.

```bash
az storage account create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$storage" --resource-group "$AZURE_RESOURCE_GROUP" --location "$location" \
  --kind StorageV2 --sku Standard_LRS --access-tier Hot \
  --allow-blob-public-access false --allow-shared-key-access false \
  --https-only true --min-tls-version TLS1_2 --output none

az storage container-rm create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --resource-group "$AZURE_RESOURCE_GROUP" --storage-account "$storage" \
  --name "$container" --public-access off --output none
```

[Create the identity](https://learn.microsoft.com/en-us/cli/azure/identity?view=azure-cli-latest#az-identity-create)
and [assign its role](https://learn.microsoft.com/en-us/cli/azure/role/assignment?view=azure-cli-latest#az-role-assignment-create)
at container scope. The principal object ID identifies who receives the grant.
Lessons 2–3, [Identity I — Microsoft Entra ID](./entra-id.md) and [Identity II — RBAC and keyless access](./rbac-and-keyless-access.md), explain managed identities, roles and scopes.

```bash
api_principal=$(az identity create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name p1-api --resource-group "$AZURE_RESOURCE_GROUP" --location "$location" \
  --query principalId --output tsv)
printf 'API principal ID: %s\n' "$api_principal"
storage_id=$(az storage account show \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$storage" --resource-group "$AZURE_RESOURCE_GROUP" --query id --output tsv)
container_scope="$storage_id/blobServices/default/containers/$container"

az role assignment create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --assignee-object-id "$api_principal" \
  --assignee-principal-type ServicePrincipal \
  --role 'Storage Blob Data Reader' --scope "$container_scope"

az storage account show --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$storage" --resource-group "$AZURE_RESOURCE_GROUP" \
  --query '{sharedKey:allowSharedKeyAccess,anonymousBlobs:allowBlobPublicAccess}'
az storage container-rm show \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --resource-group "$AZURE_RESOURCE_GROUP" --storage-account "$storage" --name "$container"
az role assignment list \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --assignee-object-id "$api_principal" --scope "$container_scope" \
  --query '[].{role:roleDefinitionName, principal:principalId}' --output table
```

Expect the account inspection to show `false` for both displayed settings, a container named `sources`,
and `Storage Blob Data Reader` for the principal ID printed earlier. This inspects configuration; it does
not test an API blob read. The container is empty. Uploading the public source set later requires a separately authorized
writer using Entra authentication. Attach `p1-api` to the API and configure its credential selection before
testing reads; role changes can take time to propagate. Disabling anonymous access also leaves the network
endpoint public; network isolation is a separate choice.

**Cost:** The empty container’s capacity charge is effectively nil because it holds no document bytes;
[Blob Storage meters stored capacity separately from operations](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/).
For scale, the
[Microsoft retail API](https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20%27Storage%27%20and%20armRegionName%20eq%20%27westeurope%27%20and%20skuName%20eq%20%27Hot%20LRS%27%20and%20priceType%20eq%20%27Consumption%27)
lists West Europe general-purpose v2 Hot LRS storage at USD 0.0196 per GB-month in the first capacity tier.
One GB retained for a month therefore costs about USD 0.02 for capacity alone. Operations and applicable
transfer charges are additional; check the [pricing page](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/)
for your region and agreement.
[Managed identities have no extra cost](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview),
and [Azure RBAC is free](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview#license-requirements).
The exercise creates no database, search service or model deployment.

**Teardown:** Delete this exercise's resource group, including its storage and identity, before leaving the
lab. Later project steps can recreate them. Keep the `AZURE_RESOURCE_GROUP` value until this
[deletion](https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-delete) completes:

```bash
az group delete \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$AZURE_RESOURCE_GROUP" --yes
az group exists \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$AZURE_RESOURCE_GROUP"
```

The final command should return `false`; check that deletion has completed.

## What to take away \{#what-to-take-away}

- Choose storage from required reads, writes and consistency guarantees; vector support alone does not establish those guarantees.
- Keep source documents authoritative and derived retrieval data rebuildable, with version links that make citations traceable.
- Measure Cosmos DB request charges with real query shapes and partition choices; choose consistency from the user-visible action.
- Give the API a container-scoped data role and token-based access. Keep ingestion writes under a separately authorized identity.

**[New terms](../glossary.md#data)**: access pattern, object storage, blob container, system of record, pgvector, partition key, request unit, consistency level, cache-aside, time to live, cache invalidation, data-plane role.

## Sources \{#sources}

Verified as of 2026-10-17.

- **Storage and relational services:** [Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction), [access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview/), [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql), [SQL vector type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type), [VECTOR_DISTANCE](https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-distance-transact-sql), [PostgreSQL pgvector](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-use-pgvector).
- **Cosmos DB:** [Partitioning](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning), [request units](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units), [consistency](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels), [vector search for NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/vector-search).
- **Redis:** [Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview), [security guidance](https://learn.microsoft.com/en-us/azure/redis/secure-azure-managed-redis), [cache-aside](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside).
- **Access:** [Blob data roles and scopes](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access), [prevent Shared Key authorization](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent), [Container Apps managed identities](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity), [role assignment procedure](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli), [managed identity overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview), [Azure RBAC licensing](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview#license-requirements).
- **CLI:** [Sign-in](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest), [account](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest), [group](https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest), [storage account](https://learn.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest), [container management](https://learn.microsoft.com/en-us/cli/azure/storage/container-rm?view=azure-cli-latest), [identity](https://learn.microsoft.com/en-us/cli/azure/identity?view=azure-cli-latest), [role assignment](https://learn.microsoft.com/en-us/cli/azure/role/assignment?view=azure-cli-latest).
- **Pricing:** [Blob pricing](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/), [retail API: West Europe Hot LRS consumption meters](https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20%27Storage%27%20and%20armRegionName%20eq%20%27westeurope%27%20and%20skuName%20eq%20%27Hot%20LRS%27%20and%20priceType%20eq%20%27Consumption%27).
