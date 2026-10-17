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
