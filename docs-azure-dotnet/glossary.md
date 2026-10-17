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
