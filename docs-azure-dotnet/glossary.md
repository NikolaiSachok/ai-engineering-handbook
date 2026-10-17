---
id: glossary
title: Glossary
sidebar_position: 95
last_verified: 2026-10-17
---

# Glossary

Every term the lessons introduce, defined once. Each lesson's **New terms** line links to its group
here. The glossary grows with the course.

Verified as of 2026-10-17. Each group's sources are in its lesson's Sources section.

## How Azure is organised \{#how-azure-is-organised}

**Tenant** — an instance of Microsoft Entra ID that holds an organisation's identities and directory objects.

**Management group** — an Azure governance scope that groups subscriptions or other management groups so access and policy assignments can apply down the hierarchy.

**Subscription** — an Azure resource administration scope whose consumed services accrue charges under its billing relationship.

**Resource group** — a container for Azure resources managed through a shared lifecycle, including their eventual deletion.

**Resource** — an item Azure manages, such as an application host, storage account or database.

**Resource provider** — the Azure service that supplies resource types and handles operations on their instances.

**Scope** — the set of Azure resources to which a management assignment, such as a role or policy assignment, applies.

**Resource ID** — the full identifier of an Azure resource, including the scopes and provider path that locate it in the management hierarchy.

**Azure Resource Manager (ARM)** — the shared Azure deployment and management layer, which receives management requests and routes them to resource providers.

**Control plane** — the operations used to create, configure and delete resources.

**Data plane** — the operations used to consume a resource's service, such as reading blobs or querying an index.

**Region** — a geographic area containing Azure datacentres and supporting infrastructure in which regional services can be deployed.

**Availability zone** — a group of datacentres within an Azure region with power, cooling and networking independent of other zones.

**Zonal resource** — a resource deployed into a selected availability zone.

**Zone-redundant resource** — a resource replicated or distributed across zones by its service.

**Tag** — name-value metadata attached to an Azure resource, resource group or subscription for organisation and cost attribution; group tags are not automatically inherited by resources.

**Budget** — a cost or usage target for a defined scope and period, with notifications at configured thresholds; it does not stop consumption.

## Identity I — Microsoft Entra ID \{#entra-id}

**Microsoft Entra ID** — a Microsoft identity and access management service for people and workloads.

**user** — a directory identity representing a person who can sign in and be granted access.

**security group** — a directory group whose membership can be granted access to resources together, reducing individual access assignments.

**app registration** — an application's identity configuration in its home tenant, with a client ID, sign-in settings and exposed API permissions; the application object provides the template for its tenant-local service principals.

**service principal** — a workload's local identity in a Microsoft Entra tenant, to which access can be granted; application registrations and managed identities have different types of service principal.

**managed identity** — a workload identity with credentials managed by Azure, allowing supported workloads to obtain Microsoft Entra access tokens without handling those credentials.

**system-assigned managed identity** — a managed identity tied to one Azure resource's lifecycle and deleted when that resource is deleted.

**user-assigned managed identity** — a managed identity created as a separate Azure resource, with a lifecycle independent of the workloads it is attached to.

**client ID** — an identifier for an application or managed identity, used to select it during authentication; knowing this identifier does not prove identity.

**principal ID** — the object ID of the service principal representing a workload in a tenant, used when granting that principal access.

**Azure resource ID** — the fully qualified Azure Resource Manager path identifying any Azure resource; for example, a user-assigned managed identity's `id` includes its subscription, resource group, provider, type and name.

**access token** — a credential presented to a protected API for access evaluation, issued for a particular audience and with a limited validity period; unrelated to the text tokens counted by a language model.

**audience** — the API a token is intended for, expressed by the `aud` claim in a JWT access token.

**ID token** — an OpenID Connect token that tells a client about a user's authentication; it is not a credential for calling another API.

**authentication** — establishing the identity of a caller.

**authorisation** — deciding whether a caller may perform a particular operation on a resource.

## RBAC and keyless access \{#rbac-and-keyless-access}

**Azure RBAC (role-based access control)** — the Azure authorization system for granting a principal permission to perform operations at a scope. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

**Role definition** — a collection of permitted management or data operations that can be assigned to a principal.

**Role assignment** — the binding of a principal, a role definition and a scope.

**Inheritance** — the application of a role assignment at a parent scope to resources beneath that scope. A narrower assignment does not subtract inherited permissions.

**DefaultAzureCredential** — an Azure Identity credential that tries a preconfigured chain of token sources, including developer and hosted-workload credentials. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/azure/sdk/authentication/credential-chains)

**Deterministic credential** — an explicit credential choice that makes the intended authentication source predictable, such as `ManagedIdentityCredential` for an Azure-hosted workload.

**Workload identity federation** — a trust arrangement that lets a workload exchange a token from an external identity provider for an Entra access token without a stored client secret.

**Federated identity credential** — the Entra trust configuration specifying an external token's accepted issuer, subject and audience. It does not itself grant Azure resource permissions. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity)

**OIDC (OpenID Connect)** — an identity protocol through which an issuer supplies an identity token. In GitHub-to-Azure federation, that token identifies the job and is exchanged for an Entra access token.

## Networking for application engineers \{#networking}

**Virtual Network (VNet)** — an isolated private address space in one region and subscription, within which resources communicate privately. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/concepts-and-best-practices)

**Subnet** — a portion of a VNet's address space allocated to resources or a service integration, where network controls can be applied.

**Network security group (NSG)** — a collection of stateful inbound and outbound packet rules that allow or deny traffic by addresses, ports and protocol, associated with a subnet or network interface. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

**Private endpoint** — a network interface with a private IP in a VNet that connects to a supported service through Azure Private Link. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

**Service endpoint** — a subnet configuration that supplies VNet identity to a supported Azure service over the Azure backbone while retaining the service's public destination address. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)

**Private DNS zone** — a DNS namespace whose records can be resolved through linked VNets and appropriately configured DNS forwarding. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links)

**VNet integration** — a service-specific mechanism connecting a managed application's networking to a VNet; its inbound and outbound capabilities depend on the hosting service. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration)

**Ingress** — traffic arriving at the application or network boundary being discussed.

**Egress** — traffic leaving the application or network boundary being discussed.

**Hub-and-spoke** — a topology where workload VNets connect to a shared hub VNet for common connectivity services such as DNS, routing and traffic inspection.

**VNet peering** — a connection allowing private network traffic between VNets; peering relationships are nontransitive. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-faq)

**Web application firewall (WAF)** — a control that inspects HTTP(S) requests using web security rules to detect or block attacks.

## Choosing compute \{#compute}

**App Service plan** — the compute capacity and pricing tier on which one or more App Service applications run.

**Container Apps environment** — the managed boundary that groups container apps and jobs with shared networking and logging configuration.

**Workload profile** — a Container Apps configuration that determines the compute and memory resources available to applications assigned to it.

**Replica** — a running instance of a Container Apps revision, added or removed as the application scales.

**Revision** — an immutable snapshot of the app's container image and scale settings.

**Scale to zero** — reducing the running instance count to zero during inactivity, with an external trigger able to start instances when work returns.

**Cold start** — the startup work and delay before a new application instance can handle requests, including resource provisioning and application initialization.

**Scale rule** — a declarative mapping from a demand signal, such as HTTP traffic or queue backlog, to the desired number of running instances.

**Always-ready instance** — capacity deliberately kept running to reduce startup delay, with billing determined by the hosting service and plan.

**Node pool** — a group of Kubernetes worker nodes with common configuration, managed as a unit within a cluster.

## Storing data \{#data}

**Access pattern** — the reads and writes a workload needs, including lookup keys, query shapes, update frequency and freshness requirements.

**Object storage** — storage that addresses named objects containing bytes and metadata; Azure Blob Storage provides this model for documents and other unstructured content.

**Blob container** — a named grouping of blobs within an Azure storage account that can also serve as the scope of a data-access role assignment.

**System of record** — the authoritative store for a piece of data, from which derived copies can be reconstructed or checked.

**pgvector** — a PostgreSQL extension for storing and searching vectors; its extension identifier is `vector`.

**Partition key** — the item property whose value determines an Azure Cosmos DB logical partition, shaping how related data and request load are distributed.

**Request unit (RU)** — Azure Cosmos DB's normalized measure of database-operation work across CPU, I/O and memory; provisioned throughput is expressed in RU/s.

**Consistency level** — the freshness and ordering guarantees a database read must satisfy relative to writes.

**Cache-aside** — an application pattern that reads a cache first, loads from the authoritative store on a miss and places the result in the cache.

**Time to live (TTL)** — the lifetime after which a stored entry expires, limiting how long it remains eligible for reuse.

**Cache invalidation** — removing or replacing cached data when an underlying change makes it unsuitable for reuse.

**Data-plane role** — an Azure role granting [data-plane](#how-azure-is-organised) operations, such as Storage Blob Data Reader for reading and listing blobs.

## Messaging and events \{#messaging}

**Command** — a message asking a responsible consumer to carry out an operation.

**Event** — a message reporting a change that has already happened.

**Event stream** — a sequence of observations consumed over time, potentially by several independent applications.

**Namespace (Service Bus)** — a container for messaging entities such as queues and topics, providing an endpoint for access. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview)

**Queue** — a broker entity that holds messages for competing consumers to receive and settle.

**Topic and subscription** — a publish/subscribe arrangement in which a topic routes copies of messages into independently consumed subscriptions.

**Settlement** — the receiver's instruction to the broker about a received message's outcome, such as completing, abandoning or dead-lettering it.

**PeekLock** — a Service Bus receive mode that temporarily locks a message for a receiver until settlement or lock expiry.

**Dead-letter queue (DLQ)** — a subqueue holding messages removed from normal delivery because they were rejected or could not be processed within the delivery policy.

**Message session** — a Service Bus grouping identified by `SessionId` that gives one receiver exclusive access to related messages for ordered handling.

**Idempotency** — the property that repeating an operation has no additional effect beyond its first successful execution.

**Duplicate detection** — a broker feature that discards repeat submissions with the same message identity within a configured interval.

**Partition** — an ordered portion of an event log that can be processed independently of other portions.

**Consumer group** — an independent view of an Event Hubs stream used by an application to consume events separately from other applications.

**Checkpoint** — a saved processing position in a stream partition, used to resume consumption after interruption.

## Secrets and configuration \{#secrets-and-configuration}

**Key Vault secret** — a versioned sensitive value, such as an external service credential, that an authorised application can retrieve from Azure Key Vault.

**Cryptographic key** — key material used for operations such as signing, encryption or wrapping another key; in Key Vault it is a different object type from a stored secret.

**Key Vault certificate** — a versioned certificate object with an associated key and secret, managed through certificate policies and lifecycle operations.

**RBAC permission model** — the Key Vault authorisation model that uses Azure role assignments for data access instead of legacy vault access policies.

**Key Vault Secrets User** — the built-in Azure role that permits reading Key Vault secret contents, including the secret portion of a certificate, without granting secret-writing permissions.

**Azure App Configuration** — an Azure service for centrally managing application settings and feature flags.

**Label (App Configuration)** — an optional App Configuration attribute that distinguishes variants of the same key, such as values for different environments.

**Key Vault reference** — a secret URI stored instead of a credential value; an App Configuration provider or Container Apps resolves it through a separately authenticated call to Key Vault.

**Rotation** — replacing a credential or cryptographic object and coordinating consumer adoption so the previous version can be retired safely.

**Soft delete** — retention of a deleted vault or object in a recoverable state for a configured period.

**Purge protection** — a Key Vault safeguard that prevents permanent deletion of a soft-deleted vault or object before its retention period ends.

## Infrastructure as code \{#infrastructure-as-code}

**Infrastructure as code (IaC)** — defining intended infrastructure configuration in files that can be versioned, reviewed and used by deployment tools.

**ARM template** — a declarative JSON deployment definition submitted to Azure Resource Manager, Azure's deployment and management layer.

**Bicep** — Azure's declarative infrastructure language, compiled into ARM JSON templates.

**Terraform state** — the stored mapping and metadata Terraform uses to connect its configuration to managed infrastructure.

**Module** — in Bicep, a deployment definition called from another file, grouping resources behind parameters and outputs.

**What-if** — ARM's operation for predicting the resource and property changes a proposed deployment would make without applying those changes.

**Configuration drift** — divergence between an environment's actual configuration and its intended configuration in source.

**Incremental deployment** — ARM's default deployment mode, which preserves resources omitted from a template while reapplying declared resources' properties; omitted properties of declared resources reset to defaults. [Deployment modes](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-modes).

**Azure Developer CLI (`azd`)** — a tool that coordinates application packaging, infrastructure provisioning and application deployment using project configuration and infrastructure as code.

## Observability \{#observability}

**Observability** — the ability to investigate a running system's behaviour through the telemetry it emits.

**Azure Monitor** — Azure's platform for collecting, analyzing and acting on telemetry from applications and infrastructure.

**Log Analytics workspace** — the Azure resource that stores log and trace tables and provides a boundary for their configuration and query access.

**Log Analytics** — the Azure portal tool for writing and running queries against log data.

**Application Insights** — the application performance monitoring feature of Azure Monitor; workspace-based resources store their telemetry in a linked Log Analytics workspace.

**OpenTelemetry distribution** — a bundle of the OpenTelemetry SDK, instrumentation libraries and configuration for collecting and exporting telemetry.

**Request telemetry** — records describing incoming application operations, including their duration and success status.

**Dependency telemetry** — records describing outgoing calls from an application to other services or systems.

**KQL (Kusto Query Language)** — the query language used to filter, combine and aggregate tables in Azure Monitor Logs.

**Ingestion** — receiving telemetry into the monitoring data store; collected data volume is a major billing input.

**Retention** — how long a table keeps data available, set per table or inherited from the workspace default. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-configure)

**Sampling** — retaining only a subset of telemetry operations to reduce volume while giving up individual records.

**Daily cap** — a workspace ingestion threshold that stops collection for affected tables until reset; it can leave telemetry gaps and allow billed overage.

## Governance and architecture frameworks \{#governance-and-frameworks}

**Azure Policy** — the Azure service that evaluates resources against configuration rules and applies their configured effects.

**Policy definition** — a reusable rule containing conditions, an effect and any parameters needed to evaluate a resource.

**Policy effect** — the action associated with a matching policy condition, such as auditing, denying a request, modifying supported properties or deploying a related resource.

**Policy assignment** — the binding of a policy definition or initiative to a scope, with parameter values and enforcement settings.

**Policy initiative** — a group of policy definitions managed and assigned together for a shared objective; also called a policy set.

**Compliance state** — the reported result of evaluating a resource against an applicable assigned policy.

**Cloud Adoption Framework (CAF)** — Microsoft's guidance for planning, preparing, adopting and operating cloud environments, including governance and organisational responsibilities.

**Landing zone** — a governed Azure environment with the organisation, access, networking and operational arrangements needed to host workloads.

**Well-Architected Framework** — Azure workload design and review guidance organised around Reliability, Security, Cost Optimization, Operational Excellence and Performance Efficiency.

**Cost Management** — Microsoft's capabilities for analysing, monitoring and optimising cloud costs.

**Microsoft Defender for Cloud** — Microsoft's service for security posture assessment and workload protection, with coverage determined by enabled plans.

**Cloud security posture management (CSPM)** — assessment of cloud resource configurations to identify security weaknesses and guide remediation.

## The .NET platform today \{#dotnet-platform}

**Runtime** — the component that executes application code and provides execution services such as garbage collection.

**SDK (software development kit)** — the tools, runtime and libraries used to create, build and run .NET applications during development.

**SDK-style project** — an MSBuild project file that selects a project SDK and inherits its build rules and default file inclusion conventions.

**Target framework moniker (TFM)** — the identifier in a project file that specifies the framework API surface available to that project, such as `net10.0`.

**global.json** — a configuration file found in the working directory or an ancestor that controls which installed .NET SDK the tools select, independently of the project's target framework.

**SDK feature band** — a group of .NET SDK versions sharing the hundreds portion of the final version component, separating tooling feature updates from patches within that band.

**LTS (Long Term Support)** — the .NET release track with a three-year support window; staying supported also requires current servicing updates.

**STS (Standard Term Support)** — the .NET release track with a two-year support window under the current policy, with the same requirement to apply servicing updates.

**NuGet** — the .NET package system used to distribute, resolve and consume versioned libraries and tools.

**PackageReference** — an MSBuild item declaring a direct NuGet package dependency for a project.

**Transitive dependency** — a package required indirectly through another package in the application's dependency graph.

**Restore** — the operation that resolves a project's package dependency graph and makes the required packages available for building.

**Dependency lock file** — the `packages.lock.json` file recording the resolved NuGet dependency graph so restore can check it in locked mode.

**Solution** — a file grouping projects for development tools and solution-level commands; it does not define a running application instance.

## ASP.NET Core \{#aspnet-core}

**Host** — the object that brings together an application's services, configuration, logging, server and lifetime management.

**Kestrel** — ASP.NET Core's default cross-platform HTTP server. [↗](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0)

**Middleware** — a component in the HTTP request pipeline that can process a request and response, invoke the next component or end processing early.

**Short-circuiting** — producing a response without invoking the remaining downstream request pipeline.

**Endpoint** — an executable request handler with associated metadata, selected by routing to handle an HTTP request.

**Minimal API** — an ASP.NET Core API approach that maps HTTP routes to handler delegates without requiring controller classes.

**Controller** — a class that groups actions using ASP.NET Core MVC's endpoint conventions and features.

**Route group** — a set of endpoints sharing a route prefix and endpoint conventions, such as metadata or authorisation requirements.

**Parameter binding** — the process that converts request data or resolves services into arguments for an endpoint handler.

**Route constraint** — a rule that restricts route matching to distinguish endpoints, rather than validate application input.

**ProblemDetails** — a structured HTTP error representation with standard fields for problem type, title, status, detail and instance, plus optional extensions. [↗](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0)

## The Microsoft.Extensions backbone \{#extensions-backbone}

**Dependency injection (DI)** — supplying a component's dependencies from outside it rather than constructing them inside the component.

**Service lifetime** — the rule a dependency injection container uses to decide when to create and reuse a registered service instance.

**Transient** — a service lifetime that creates a new instance each time the container resolves the service.

**Scoped** — a service lifetime that reuses one instance within a DI scope; in an ASP.NET Core HTTP API, a request has its own DI scope.

**Singleton** — a service lifetime that reuses one instance throughout a dependency injection container's lifetime.

**Captive dependency** — a dependency retained by a longer-lived consumer beyond the lifetime it was intended to have.

**Configuration provider** — a component that supplies configuration key-value pairs from a source such as JSON, environment variables or command-line arguments.

**Options pattern** — typed access to a group of related configuration settings through an options class and options services.

**Startup validation** — checking configured rules when the application starts so invalid settings prevent startup.

**Structured logging** — recording a stable message template with separate named values that a logging provider can preserve as queryable fields.

## Async, streaming and cancellation \{#async-streaming-cancellation}

**Task** — a .NET object representing an operation's eventual completion, failure or cancellation; `Task<T>` also provides its result.

**Async stream** — a sequence exposed as `IAsyncEnumerable<T>` whose successive items can be awaited and consumed with `await foreach`. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/generate-consume-asynchronous-stream)

**Server-sent events (SSE)** — an HTTP event-stream format for sending successive messages from a server to a client over one connection.

**Cooperative cancellation** — stopping work through a shared cancellation request that each participating operation must observe and respond to.

**Cancellation token** — a .NET value passed to an operation so it can observe a cancellation request. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads)

**Cancellation token source** — a .NET object that supplies a token and can request cancellation for operations observing it.

**Request cancellation** — the signal exposed by ASP.NET Core's `HttpContext.RequestAborted` when the client or server aborts the HTTP request.

**Linked cancellation** — combining cancellation signals through a token source that is cancelled when any linked input token is cancelled.

**Elapsed-time budget** — a total duration allowed for an operation, after which the application requests cancellation regardless of whether updates are still arriving.

**Idle timeout** — a limit on how long an operation may go without progress, such as receiving the next stream update.

## Data access \{#data-access}

**Object-relational mapper (ORM)** — a library that maps application objects to relational database tables and mediates queries and updates between them.

**EF Core (Entity Framework Core)** — Microsoft's .NET object-relational mapper, with LINQ querying, entity change tracking and schema migrations.

**Database provider** — the database-specific implementation that connects EF Core to an engine and translates queries into that engine's query language.

**DbContext** — EF Core's unit-of-work object, which provides access to the model, queries and tracked entity changes for a bounded operation.

**Change tracking** — recording entity identities, states and property changes so EF Core can determine the writes needed when saving.

**No-tracking query** — an EF Core query whose returned entities are not retained in the context's change tracker for later updates.

**Migration** — a versioned set of schema operations that moves a database from one application model shape to another.

**Model snapshot** — EF Core's saved representation of the model used as the comparison point when generating the next migration.

**Projection** — selecting a specific result shape, such as a few columns, instead of returning a complete entity.

**N+1 queries** — one database query followed by an additional query for each of its N results, caused by patterns such as lazy loading related data or querying inside a per-result loop. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying)

**Cartesian explosion** — multiplication of result rows when a query joins several sibling collections, repeating combinations of their members.

**Dapper** — a .NET micro-ORM that maps explicitly written SQL query results to objects without EF Core's entity change tracker.

**Parameterized SQL** — SQL that sends data values separately from command text, preventing those values from being interpreted as SQL syntax.

**Optimistic concurrency** — detecting conflicting writes by comparing a previously read token with its stored value during an update, then requiring the application to resolve a mismatch.

**Concurrency token** — a property whose originally read value EF Core compares with the stored value when saving an update or delete to detect a conflicting write. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/ef/core/saving/concurrency)

**Split query** — an EF Core query that loads related collections through multiple SQL queries instead of joining them all into one result. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/ef/core/querying/single-split-queries)

**Migration bundle** — an executable artifact containing EF Core migrations that can apply schema changes without the application's source code, .NET SDK or EF tools on the target machine. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying#bundles)

## Testing \{#testing}

**Unit test** — an executable check of an isolated piece of application behaviour.

**Integration test** — an executable check that multiple application components work together across a chosen boundary.

**xUnit** — a .NET testing framework that defines tests with attributes such as `Fact` and `Theory` and checks their results with assertions. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-csharp-with-xunit)

**Test double** — a substitute for a dependency used to control or observe its behaviour during a test.

**Fake** — a test double with a working, deliberately limited implementation.

**WebApplicationFactory** — the ASP.NET Core test helper that starts an application for integration tests and allows its test-host configuration to be customised. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0)

**TestServer** — ASP.NET Core's in-process server for exercising an application's HTTP pipeline in tests.

**Testcontainers** — a library that manages disposable containers used as test dependencies.

**Test fixture** — known setup or data supplied to tests, with a defined lifetime and cleanup responsibility.

## Containers and Aspire \{#containers-and-aspire}

**Container image** — a packaged filesystem and runtime configuration used to create container instances of an application.

**Image digest** — the content-derived SHA-256 identifier of an image manifest, used to identify a specific image independently of a mutable tag. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts#manifest-digest)

**PublishContainer** — the .NET SDK target that creates a container image from a published application and a base image without requiring a Dockerfile. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/containers/sdk-publish)

**AppHost** — an Aspire project or file that declares application resources and their relationships for orchestration. ↗ [Aspire](https://aspire.dev/get-started/app-host/)

**Aspire resource** — an application component or dependency represented in the AppHost model, such as an API project or a container.

**Service Defaults** — a shared C# project containing configurable setup for telemetry, health checks, service discovery and HTTP client resilience. ↗ [Aspire](https://aspire.dev/get-started/csharp-service-defaults/)

**OpenTelemetry** — a vendor-neutral framework for instrumenting applications and collecting and exporting telemetry signals, including traces, metrics and logs. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel)

**OTLP (OpenTelemetry Protocol)** — the protocol used to transmit OpenTelemetry signals between applications, collectors and telemetry backends. ↗ [Aspire](https://aspire.dev/fundamentals/telemetry/)

**Span** — a record of one operation within a distributed trace, carrying timing, context and associated attributes.

**Service discovery** — resolving a logical service name to the endpoints a client can call.

## AI in .NET \{#ai-in-dotnet}

**Microsoft.Extensions.AI** — .NET libraries that supply shared AI client contracts and composable behaviours such as telemetry, caching and function invocation. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai)

**IChatClient** — the Microsoft.Extensions.AI interface for exchanging chat messages with a model service, returning a complete response or a stream of updates. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/ai/ichatclient)

**IEmbeddingGenerator** — the Microsoft.Extensions.AI contract for converting typed inputs into typed embeddings; the text-to-vector form used here is `IEmbeddingGenerator<string, Embedding<float>>`. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/ai/iembeddinggenerator)

**Provider adapter** — a component that exposes a provider's SDK client through a shared application interface, translating between their types and operations.

**Delegating client pipeline** — a sequence of wrappers around an AI client, each adding behaviour before or after forwarding an operation; `DelegatingChatClient` is the base class for chat wrappers that pass calls to an inner `IChatClient`. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.ai.delegatingchatclient?view=net-10.0-pp)

**Microsoft.Extensions.VectorData** — .NET abstractions for accessing vector stores and typed record collections through provider implementations. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/ai/vector-stores/overview)

**Microsoft Agent Framework** — Microsoft's SDK for building agents and workflows, with support for tools, session state and orchestration. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/overview/)

## Microsoft Foundry \{#microsoft-foundry}

**Foundry resource** — an Azure resource that holds shared serverless model deployments, networking and security settings; its type is `Microsoft.CognitiveServices/accounts` with kind `AIServices`.

**Foundry project** — a child resource within a Foundry resource that organises assets such as agents, evaluations, files and managed-compute deployments, with project access controls alongside the parent's shared settings.

**Model catalog** — the discovery surface for model offerings, capabilities and deployment options; finding a model there does not create a deployment or establish subscription eligibility.

**Model deployment** — a named serving configuration for a selected model and version, addressed by deployment name in deployment-based inference requests.

**Inference endpoint** — the API address through which a client sends model inputs and receives outputs.

**Keyless access** — authentication with Microsoft Entra ID tokens instead of a stored service API key; the caller still needs permission, and enforcing keyless-only use requires disabling local authentication.

## Model deployments, quotas and cost \{#deployments-quotas-cost}

**Deployment type** — the model-serving option that determines the inference-processing boundary, capacity model and billing mechanism.

**Quota** — the allowance available to a subscription for a model or deployment category in the applicable scope; it permits allocation without purchasing processing capacity.

**TPM (tokens per minute)** — a token-throughput rate limit; Azure OpenAI's throttling estimate differs from the token count used for billing.

**RPM (requests per minute)** — a request-rate limit whose enforcement can reject bursts within shorter evaluation windows.

**HTTP 429** — the “Too Many Requests” response used when the model service throttles a request.

**Exponential backoff** — a retry policy that increases the delay after repeated failures; random jitter spreads retries across clients.

**PTU (provisioned throughput unit)** — a unit of reserved model processing capacity; the throughput it supplies depends on the model and workload.

**Azure Reservation** — a financial commitment that discounts matching provisioned-throughput usage, managed separately from the deployment that consumes capacity.

**Batch deployment** — a model deployment for asynchronous groups of requests, using batch token pricing and enqueued-token quota rather than an interactive request path.

## Safety on the platform \{#platform-safety}

**Content filter** — a platform check that classifies content and applies configured actions, such as annotating or blocking input or output.

**Severity level** — a category-specific classification of how harmful content is, rather than a measure of classifier confidence or access permission.

**Severity threshold** — the classified severity at which a content filter starts blocking, including higher severities.

**Blocking level** — the Foundry portal's setting for filtering strictness; a higher blocking level blocks a broader range of classified severities.

**Annotation** — structured metadata reporting a detector's result and, where supported, whether the content was filtered.

**Prompt Shields** — Microsoft's detectors for attempts to redirect model behaviour through user prompts or document content. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields)

**Direct prompt attack** — an attempt to override the model's instructions through the user-prompt channel.

**Indirect prompt attack** — an attempt to override the model's instructions through content supplied as data, such as a retrieved document.

**Groundedness detection** — checking whether generated statements are supported by the source material supplied for the task. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-groundedness)

**Protected-material detection** — checking generated output for matches to known protected text or code. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-protected-material)

**RAI policy (responsible AI policy)** — a named Azure configuration of safety controls that a model deployment can reference.

## RAG on Azure AI Search \{#rag-on-ai-search}

**Search index** — a collection of keyed search documents whose schema defines their fields and the operations available on those fields.

**Field attributes** — schema settings that determine whether a field can participate in search, be returned in results, support filters, supply sort values or produce facet counts.

**Vector search profile** — a named index configuration that connects a vector field to a search algorithm and optional compression and vectorizer settings.

**Hybrid query** — a search request that runs keyword and vector retrieval and combines their ranked results.

**Reciprocal rank fusion (RRF)** — an algorithm that combines ranked lists using each document's position in those lists. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking)

**Semantic ranker** — Azure AI Search's query-side capability for reranking retrieved candidates using their text and optionally extracting captions and answers.

**Indexer** — an Azure AI Search component that reads a supported data source and drives the pipeline that populates an index.

**Skillset** — a configuration of enrichment operations that an Azure AI Search indexer can apply to source content, such as splitting text and generating embeddings.

**Integrated vectorization** — Azure AI Search's built-in indexing and query pipeline support for generating vectors through embedding skills and vectorizers.

**Query vectorizer** — a configured connection through which Azure AI Search converts query input into an embedding at query time.

**Knowledge base** — an Azure AI Search object that coordinates agentic retrieval across configured knowledge sources and holds retrieval settings.

**Knowledge source** — an Azure AI Search definition of content available to a knowledge base, backed by an index or retrieved from a remote platform.

## Getting documents in \{#document-ingestion}

**OCR (optical character recognition)** — recognition of text characters in page images so they can be processed as machine-readable text.

**Layout analysis** — extraction of a document's structural elements and their relationships, such as headings, paragraphs, tables and selection marks.

**Field extraction** — mapping document content to named values in a schema, such as an invoice date or total.

**Analyzer** — a Content Understanding configuration that selects content extraction behaviour and can define a field schema and generative processing.

**Bounding region** — a page reference and polygon locating an extracted document element in the source page's coordinate system.

**Provenance** — the record connecting derived content to its original source and the processing that produced it.

## Agents on Azure \{#agents-on-azure}

**Prompt agent** — a managed agent defined through configuration of instructions, model and tools rather than custom runtime code.

**Hosted agent** — an agent whose custom code runs in a container on Foundry-managed infrastructure.

**Function tool** — a callable operation described to a model through a name, parameters and description, with execution handled by the application.

**Model Context Protocol (MCP)** — a protocol through which an AI application connects to servers exposing tools and context. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol)

**Conversation** — the stored history of messages, tool calls and outputs used to continue an interaction.

**Hosted-agent session** — a Foundry sandbox's compute and filesystem working state; reusing its ID does not itself restore conversation history. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-sessions)

**Agent Framework session** — the conversation-associated state held by `AgentSession`, including history or references to externally stored history and other state needed between runs. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/microsoft.agents.ai.agentsession?view=agent-framework-dotnet-latest)

**Long-term memory** — selected information retained for use across separate conversations or sessions.

**Approval request** — a pending proposal for a specific action that requires a decision from an authorized person before execution.

**Idempotency key** — an identifier used to recognize retries of the same logical operation and prevent duplicate effects.

**Workflow checkpoint** — a saved record of execution state from which a workflow can resume.

## Evaluation and tracing \{#evaluation-and-tracing}

**Evaluator** — a scoring method that measures a specified quality, safety or reliability property of model or application outputs.

**Groundedness evaluator** — a scoring method that assesses whether a generated response is supported by its grounding context. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators)

**Relevance evaluator** — a scoring method that assesses how well a generated response addresses the user's query. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators)

**Offline evaluation** — assessment of a fixed set of test cases outside the live request path, used to inspect behaviour and compare application versions.

**Continuous evaluation** — recurring assessment of sampled live interactions as traffic arrives, rather than a check that blocks each response before delivery.

**Scheduled evaluation** — an evaluation run triggered at a configured time or recurrence, using its configured data source and scoring criteria.

**Custom evaluator** — an application-defined scoring method implemented through code, a judge prompt or an external endpoint.

**Trace identifier** — the identifier shared by operations belonging to one distributed trace, used to correlate their execution records. ↗ [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/distributed-tracing-concepts)

## The AI gateway \{#ai-gateway}

**AI gateway** — a proxy in the model request path that applies shared access, consumption, routing and telemetry controls.

**Token-limit policy** — a gateway rule that restricts model token consumption by a rate, a quota over a period, or both.

**Counter key** — the value identifying which shared consumption counter a gateway policy updates for a request.

**Backend pool** — a group of backend endpoints treated as one routing target, with rules for distributing requests among them.

**Circuit breaker** — a control that temporarily stops sending requests to a backend after configured failure conditions are met, allowing it time to recover.

**Semantic cache** — a cache that reuses a stored model response when an incoming prompt meets a semantic-similarity threshold and the configured reuse conditions.

**Token metric** — a measurement of model token consumption, reported or estimated for monitoring and aggregation.

## Enterprise-grade AI \{#enterprise-ai}

**Shared private link** — an outbound private connection managed for Azure AI Search to reach a supported dependency, configured independently of the private endpoint that accepts client requests into Search.

**Local authentication** — service authentication using a resource's own credentials, such as API keys, rather than Microsoft Entra ID tokens.

**Data residency** — the location commitments that govern where a workload's data is stored or processed.

**Processing boundary** — the permitted geographic scope within which a service may process a workload's inputs and outputs.

**Abuse monitoring** — service-side detection and review of usage that may violate applicable terms, which can include reviewing selected prompts and completions.

## Copilot Studio and the Power Platform \{#copilot-studio-power-platform}

**Power Apps** — Microsoft's low-code application builder for canvas interfaces and model-driven applications built on Dataverse.

**Power Automate** — Microsoft's workflow service for automating sequences of actions, including cloud flows triggered manually, by events or on a schedule.

**Dataverse** — Microsoft's managed business-data platform with tables, relationships and role-based access for applications.

**Copilot Studio** — Microsoft's low-code builder for agents and agent flows that can connect to services through tools.

**Power Platform environment** — a container for managing platform assets such as apps, flows, connections and business data within a Microsoft Entra tenant.

**Custom connector** — a definition that exposes an API's operations, data shapes and authentication to Power Platform callers.

**Connection** — a configured instance of access to a service through a connector, using the credentials associated with that instance.

**Connection reference** — a solution component that points to a connection for a specific connector, allowing operations in a solution-aware flow to bind to that connection.

**Data policy** — a Power Platform governance rule controlling connector use and permitted combinations of connectors to constrain data movement.

**Power Platform solution** — a package of platform components used to manage customisations and move them between environments; distinct from a .NET solution file.
