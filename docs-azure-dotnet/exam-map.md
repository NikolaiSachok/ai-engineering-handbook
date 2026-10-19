---
title: Exam map
sidebar_position: 92
last_verified: 2026-10-19
---

# Map exam objectives to the course work

Use this map beside the current study guide, then use the practice assessment to identify work you
still need: [AI-103 study guide][guide103] and [practice assessment][practice103];
[AI-200 study guide][guide200] and [practice assessment][practice200]. The assessments require sign-in;
the links here are the destinations offered by the official credential pages.

Each row represents one objective bullet in the guides. A bold label starts a skill area; subsequent
rows belong to it until the next label. **Covered** means substantive instruction spans the objective:
explanations for selection/design objectives, configuration recipes or implementation steps for
configure/build objectives. A recipe need not be a complete lab or a live deployment. **Partial** means
some scope is missing, or an implementation objective has conceptual instruction without a recipe;
the note names the remaining work. **Not covered** means there is no instruction for the requested
task beyond mentions or comparisons. Use Microsoft Learn for missing work, and practise implementation
even where a recipe earns Covered.

Project key: **P1** — [RAG service](./part-5-projects/rag-service.md);
**P2** — [Agent behind an AI gateway](./part-5-projects/agent-behind-gateway.md);
**P3** — [Document ingestion pipeline](./part-5-projects/ingestion-pipeline.md).
Project links lead to build milestones; each guide records its execution limits.

The [AI-103 guide][guide103] expects application-development experience in Python; the
[AI-200 guide][guide200] expects proficiency in it. The projects here use C#. Our mapping assumes
that service selection, identity, retrieval and operational concepts carry across the
[Azure SDKs for .NET][dotnetazure]; this is a teaching judgement. Add Python implementation practice
alongside every mapped topic.

## AI-103 — Developing AI Apps and Agents on Azure \{#ai-103}

Credential: [Microsoft Certified: Azure AI Apps and Agents Developer Associate][cert103].
The [study guide's outline is effective from 16 April 2026][guide103]: five functional groups,
14 skill areas and 64 objective bullets. The tables keep that order.

### Plan and manage an Azure AI solution (25–30%)

| Skill | Covered by | Note |
|---|---|---|
| **Choose the appropriate Foundry services for generative AI and agents** — select LLMs, small models, multimodal models and Foundry Tools for a task. | [Microsoft Foundry][foundry]; [Model deployments, quotas and cost][deploy] | Partial. The lessons teach catalogue, serving and deployment choices; task-based selection of small and multimodal models and Tools needs additional study. [Microsoft Learn][learn103]. |
| Choose services for generation, grounding, vector search, agent workflows and multimodal processing. | [Microsoft Foundry][foundry]; [RAG on Azure AI Search][search]; [Agents on Azure][agents]; [Getting documents in][ingestion] | Partial. Text generation, retrieval, hosting and document processing are taught; broader multimodal processing is outside the course. [Microsoft Learn][learn103]. |
| Choose retrieval and indexing methods. | [RAG on Azure AI Search][search] | Covered. Compare application push with indexers, skillsets and query vectorisation. |
| Choose memory, tool and knowledge integration services for agents. | [Agents on Azure][agents]; [RAG on Azure AI Search][search]; [Data access][db] | Covered. Separate conversation state, long-term memory, retrieval and authoritative approval records. |
| **Set up AI solutions in Foundry** — design infrastructure for AI apps and agents. | [Infrastructure as code][iac]; [Enterprise-grade AI][enterprise]; [P1 milestone 1][p11]; [P2 milestone 1][p21] | Covered. The guides define resource ownership, identities, hosting and shared dependencies. |
| Choose deployment options. | [Model deployments, quotas and cost][deploy]; [Agents on Azure][agents]; [Choosing compute][compute] | Covered. Compare model deployment types and managed versus self-hosted agents. |
| Configure model and agent deployments. | [Model deployments, quotas and cost][deploy]; [P1 milestone 1][p11]; [P2 milestone 4][p24] | Partial. Model deployment and a self-hosted agent are taught; configuring a Foundry managed agent deployment is missing. [Microsoft Learn][agentlearn]. |
| Integrate Foundry projects with CI/CD. | [Pipelines to Azure][pipelines]; [P1 milestone 7][p17] | Partial. OIDC and application deployment are taught; the pipeline does not deploy Foundry project assets. [Microsoft Learn][learn103]. |
| **Manage, monitor, and secure AI systems** — manage quotas, scaling, rate limits and model/agent costs. | [Model deployments, quotas and cost][deploy]; [The AI gateway][gateway]; [Choosing compute][compute]; [P2 milestone 3][p23] | Covered. Model quotas and throttling, host replicas and persistent project costs have distinct controls. |
| Monitor model performance, drift, safety events and grounding quality. | [Evaluation and tracing][eval]; [P1 milestone 6][p16]; [P2 milestone 6][p26] | Partial. Tracing and groundedness/relevance evaluation are taught; drift monitoring and deployed safety-event monitoring need further work. [Microsoft Learn][learn103]. |
| Monitor ingestion quality, search-index health and retrieval relevance. | [RAG on Azure AI Search][search]; [Evaluation and tracing][eval]; [P3 milestone 6][p36] | Partial. Extraction checks, ingestion progress and relevance diagnosis are taught; a complete search-index health monitoring setup is absent. [Microsoft Learn][learn103]. |
| Configure managed identity, private networking, keyless credentials and role policies. | [RBAC and keyless access][rbac]; [Networking for application engineers][network]; [Enterprise-grade AI][enterprise] | Partial. Identity, roles and keyless configuration are taught; the network lab stops before a complete private-endpoint deployment. [Microsoft Learn][learn103]. |
| **Implement responsible AI across generative AI and agentic systems** — configure safety filters, guardrails, risk detection and moderation. | [Safety on the platform][safety]; [P2 milestone 4][p24] | Partial. Filter inspection and approval controls are taught; creating safety policies and configuring the wider detection/moderation services are missing. [Microsoft Learn][learn103]. |
| Apply evaluators, safety evaluation and explanation tooling. | [Evaluation and tracing][eval]; [P1 milestone 6][p16]; [P2 milestone 6][p26] | Partial. The projects run Groundedness and Relevance evaluators; safety-evaluation runs and explanation tooling are absent. [Microsoft Learn][learn103]. |
| Audit with traces, provenance metadata and approval workflows. | [Evaluation and tracing][eval]; [Getting documents in][ingestion]; [P2 milestone 4][p24]; [P3 milestone 6][p36] | Covered. Trace IDs, source versions and durable decisions connect actions to their evidence. |
| Govern agent behaviour with oversight modes, constraints and tool-access controls. | [Agents on Azure][agents]; [P2 milestone 2][p22]; [P2 milestone 4][p24]; [P2 milestone 5][p25] | Covered. The application validates caller, tool, frozen arguments and approval before execution. |

### Implement generative AI and agentic solutions (30–35%)

| Skill | Covered by | Note |
|---|---|---|
| **Build generative applications by using Foundry** — deploy and consume LLMs, small models, code models and multimodal models. | [Model deployments, quotas and cost][deploy]; [AI in .NET][ai]; [P1 milestone 1][p11]; [P1 milestone 4][p14] | Partial. The implementation uses text-chat and embedding models; small, code and multimodal deployment/consumption are missing. [Microsoft Learn][learn103]. |
| Implement RAG in an application. | [RAG on Azure AI Search][search]; [P1 milestone 3][p13]; [P1 milestone 4][p14] | Covered. Build document embeddings, hybrid retrieval and answers with validated citation identifiers. |
| Design workflows, tool-augmented flows and multistep reasoning pipelines. | [Agents on Azure][agents]; [P2 milestone 4][p24]; [P3 milestone 5][p35] | Partial. A tool-call/approval flow and ingestion stages are taught; a multistep reasoning pipeline is not built. [Microsoft Learn][agentlearn]. |
| Evaluate fabrication, relevance, quality and safety in models and apps. | [Evaluation and tracing][eval]; [P1 milestone 6][p16] | Partial. Groundedness and Relevance are exercised; broader quality and safety evaluators are not run. [Microsoft Learn][learn103]. |
| Integrate generative workflows through Foundry SDKs and connectors. | [AI in .NET][ai]; [P1 milestone 4][p14]; [P2 milestone 4][p24] | Partial. The course integrates resource inference with .NET adapters; project SDK workflow integration and Foundry connectors are not implemented. [Microsoft Learn][sdklearn]. |
| Configure an application to connect to a Foundry project. | — | Not covered. P1 uses the resource inference endpoint; creating a project is not project-client integration. [Microsoft Learn][projectlearn]. |
| **Build agents by using Foundry** — define roles, goals, conversation tracking and tool schemas. | [Agents on Azure][agents]; [P2 milestone 4][p24] | Partial. These are taught for the self-hosted .NET agent; implement the Foundry managed-agent path separately. [Microsoft Learn][agentlearn]. |
| Build agents with retrieval, function calling and conversation memory. | [P2 milestone 2][p22]; [P2 milestone 4][p24] | Partial. P2 combines these in a self-hosted agent; the managed Foundry implementation remains additional work. [Microsoft Learn][agentlearn]. |
| Integrate API, knowledge-store, search, Content Understanding and custom-function tools. | [Agents on Azure][agents]; [P2 milestone 4][p24]; [P3 milestone 3][p33] | Partial. P2 uses retrieval and custom functions; Content Understanding runs in P3, not as an agent tool. Managed tool integrations and that connection are missing. [Microsoft Learn][agentlearn]. |
| Implement orchestrated multi-agent solutions. | — | Not covered. The agent lesson compares orchestration patterns; P2 builds one agent. [Microsoft Learn][agentlearn]. |
| Build autonomous or semiautonomous workflows with safeguards and approvals. | [P2 milestone 2][p22]; [P2 milestone 3][p23]; [P2 milestone 4][p24] | Partial. P2 implements durable approvals and guarded execution in its own host; a Foundry managed workflow is not built. [Microsoft Learn][agentlearn]. |
| Monitor deployed agents, evaluate their behaviour and analyse errors. | [Evaluation and tracing][eval]; [P2 milestone 6][p26] | Partial. P2 specifies application traces, saved-answer evaluation and execution checks; managed-agent monitoring and evaluation are not implemented. [Microsoft Learn][agentlearn]. |
| **Optimize and operationalize generative AI systems** — tune prompts and generation parameters. | — | Not covered. A fixed grounded-answer prompt is used, without a prompt/parameter tuning exercise. [Microsoft Learn][learn103]. |
| Implement reflection, chain-of-thought evaluation and self-critique loops. | — | Not covered. No implementation or evaluation exercise covers these loops. [Microsoft Learn][learn103]. |
| Implement tracing, token analytics, safety signals and latency breakdowns. | [Observability][monitor]; [Evaluation and tracing][eval]; [P1 milestone 5][p15]; [P2 milestone 6][p26] | Partial. Request/model spans and usage are taught; a complete safety-signal and token-analytics setup is not implemented. [Microsoft Learn][learn103]. |
| Orchestrate multiple models, flows or hybrid LLM/rules engines. | — | Not covered. Using chat and embedding clients in RAG does not teach model/flow orchestration. [Microsoft Learn][learn103]. |

### Implement computer vision solutions (10–15%)

| Skill | Covered by | Note |
|---|---|---|
| **Design and implement image- and video-generation solutions** — generate images from prompts and reference media. | — | Not covered. No image-generation application is built. [Microsoft Learn][vision]. |
| Generate video from prompts and reference media. | — | Not covered. No video-generation application is built. [Microsoft Learn][vision]. |
| Configure inpainting, masked edits and prompt-driven image modifications. | — | Not covered. Image-editing workflows are outside the course. [Microsoft Learn][vision]. |
| Implement generated-video editing workflows. | — | Not covered. Video editing is outside the course. [Microsoft Learn][vision]. |
| Select and apply platform generation/editing controls. | — | Not covered. The course does not configure visual generation controls. [Microsoft Learn][vision]. |
| **Design and implement multimodal understanding workflows** — analyse visual context with multimodal models. | — | Not covered. Document OCR/layout work does not implement general visual-context analysis. [Microsoft Learn][vision]. |
| Produce concise or detailed captions for one or more images. | — | Not covered. No image-captioning application is built. [Microsoft Learn][vision]. |
| Implement question answering grounded in visual evidence. | — | Not covered. P1 grounds text answers in retrieved text; it does not pass visual evidence to a multimodal model. [Microsoft Learn][vision]. |
| Generate alt text and extended image descriptions aligned with accessibility guidance. | — | Not covered. No accessibility-description workflow is built. [Microsoft Learn][vision]. |
| Configure Content Understanding to extract visual characteristics. | — | Not covered. P3 uses document layout extraction, not visual-characteristic extraction. [Microsoft Learn][vision]. |
| Process and interpret video segments. | — | Not covered. No video-analysis pipeline is built. [Microsoft Learn][vision]. |
| Configure single-task and pro-mode Content Understanding pipelines. | — | Not covered. The prebuilt document-layout analyzer exercise does not configure both pipeline modes. [Microsoft Learn][vision]. |
| Identify objects, components or regions in images/video. | — | Not covered. No object or region understanding workflow is built. [Microsoft Learn][vision]. |
| **Implement responsible AI for multimodal content** — classify unsafe or disallowed visual content with filters. | — | Not covered. The safety lesson does not implement visual-content filtering. [Microsoft Learn][vision]. |
| Detect and mitigate prompt injection embedded in image text. | — | Not covered. Text Prompt Shields discussion does not implement an image-input defence. [Microsoft Learn][vision]. |
| Enforce watermarks, prohibited-symbol rules, brand requirements and inappropriate-content detection. | — | Not covered. No visual-policy enforcement workflow is built. [Microsoft Learn][vision]. |

### Implement text analysis solutions (10–15%)

| Skill | Covered by | Note |
|---|---|---|
| **Apply language model text analysis** — extract entities, topics, summaries and structured JSON with prompting and Foundry Tools. | — | Not covered. A cited RAG answer and layout JSON are not a text-analysis implementation. [Microsoft Learn][language]. |
| Detect sentiment, tone, safety issues and sensitive content. | [Safety on the platform][safety] | Partial. Text safety mechanisms are explained; sentiment/tone detection and sensitive-content analysis are not implemented. [Microsoft Learn][language]. |
| Translate text with Azure Translator in Foundry Tools or LLM translation flows. | — | Not covered. No translation application is built. [Microsoft Learn][language]. |
| Customise outputs for domain tasks such as compliance summaries and extraction. | — | Not covered. No domain text-analysis or output-customisation exercise is provided. [Microsoft Learn][language]. |
| **Implement speech solutions** — convert speech to text and text to speech for agents. | — | Not covered. No speech-input or speech-output integration is built. [Microsoft Learn][language]. |
| Add speech as an agent modality, including custom speech models. | — | Not covered. No speech agent or custom speech model is configured. [Microsoft Learn][language]. |
| Enable multimodal reasoning from audio. | — | Not covered. The projects accept text or documents, without audio reasoning. [Microsoft Learn][language]. |
| Translate speech with language models and Foundry Tools. | — | Not covered. No speech-translation workflow is built. [Microsoft Learn][language]. |

### Implement information extraction solutions (10–15%)

| Skill | Covered by | Note |
|---|---|---|
| **Build retrieval and grounding pipelines** — ingest and index documents, images, audio and video. | [P1 milestone 3][p13]; [P3 milestone 3][p33]; [P3 milestone 4][p34] | Partial. Text documents and document OCR/layout are taught; image, audio and video retrieval ingestion are missing. [Microsoft Learn][learn103]. |
| Configure semantic, hybrid and vector search for grounding. | [RAG on Azure AI Search][search]; [P1 milestone 3][p13]; [P1 milestone 4][p14] | Covered. The lesson gives semantic field/query settings ([official configuration][semanticconfig], [query options][semanticquery]); P1 implements hybrid text/vector retrieval. Practise semantic ranking separately: P1 omits it. |
| Implement custom or built-in enrichment skills for text, images and layout. | [RAG on Azure AI Search][search]; [Getting documents in][ingestion]; [P3 milestone 3][p33] | Partial. Application-owned document extraction is taught; Search skillset enrichment for text, images and layout is not implemented. [Microsoft Learn][learn103]. |
| Configure RAG ingestion including documents and OCR. | [Getting documents in][ingestion]; [P3 milestone 3][p33]; [P3 milestone 4][p34] | Covered. Extract layout, retain provenance, split, embed and push chunks into P1. |
| Connect retrieval pipelines to workflows and agent tools. | [P2 milestone 4][p24]; [P3 milestone 4][p34]; [P3 milestone 5][p35] | Covered. P2 exposes P1 retrieval as a tool; P3 updates the index the request path reads. |
| **Extract content from documents** — combine OCR, layout and field extraction in multimodal pipelines. | [Getting documents in][ingestion]; [P3 milestone 3][p33] | Partial. OCR and layout are implemented; business-field/schema extraction and a combined semantic pipeline are missing. [Microsoft Learn][learn103]. |
| Produce clean, grounded representations for agents and RAG with Content Understanding. | [P3 milestone 3][p33]; [P3 milestone 4][p34] | Covered. P3 checks layout against the PDF and carries source/page references into chunks. |
| Implement Content Understanding analyzers producing structured or Markdown outputs for downstream reasoning. | [Getting documents in][ingestion]; [P3 milestone 3][p33] | Covered. P3 calls the prebuilt layout analyzer and retains its full structured response and Markdown; it does not build a custom analyzer. |

## AI-200 — Developing AI Cloud Solutions on Azure \{#ai-200}

Credential: [Microsoft Certified: Azure AI Cloud Developer Associate][cert200].
The [study guide's outline is effective from 7 October 2026][guide200]: four functional groups,
nine skill areas and 27 objective bullets.

The guide has an unresolved weighting discrepancy: its summary gives data management **30–35%**, while
the detailed section still says **25–30%**. Its change log says the weight increased. This map uses the
summary's 30–35%; check the [current guide][guide200] before planning revision time.

### Develop containerized solutions on Azure (20–25%)

| Skill | Covered by | Note |
|---|---|---|
| **Implement container application hosting** — build, store, version and manage images with Azure Container Registry. | [Containers and Aspire][containers]; [P1 milestone 5][p15]; [P1 milestone 7][p17]; [Releasing safely][release] | Covered. Build and publish the API image, configure registry identity and retain release tags/digests. |
| Build and run images with Azure Container Registry Tasks. | — | Not covered. Local/CI image publishing does not implement ACR Tasks. [Microsoft Learn][learn200]. |
| Deploy containers to App Service with environment variables and secrets. | — | Not covered. The compute lesson compares App Service, but the project deploys to Container Apps. [Microsoft Learn][learn200]. |
| **Implement container-orchestrated solutions** — deploy to Container Apps with environment configuration and revision management. | [Choosing compute][compute]; [P1 milestone 5][p15]; [P1 milestone 7][p17]; [Releasing safely][release] | Covered. Configure environment, identity, settings, revisions, traffic and rollback. |
| Implement event-driven KEDA scaling in Container Apps. | — | Not covered. The compute lab configures HTTP scaling; P2 uses fixed minimum replicas without a queue-driven KEDA rule. [Microsoft Learn][learn200]. |
| Deploy and manage AKS applications through manifests. | — | Not covered. AKS is compared as a hosting choice; no cluster or workload manifests are built. [Microsoft Learn][learn200]. |
| Monitor/troubleshoot AKS and Container Apps through logs, events and end-to-end connectivity. | [Networking for application engineers][network]; [Observability][monitor]; [P1 milestone 5][p15]; [Releasing safely][release] | Partial. Container Apps requests, logs and dependency paths are taught; AKS diagnostics and event inspection are missing. [Microsoft Learn][learn200]. |

### Develop AI solutions by using Azure data management services (30–35%)

| Skill | Covered by | Note |
|---|---|---|
| **Develop AI solutions by using Azure Cosmos DB for NoSQL** — connect through the SDK and run queries. | — | Not covered. P3 specifies durable job items and conditional writes, without teaching SDK connection and query implementation. [Microsoft Learn][learn200]. |
| Optimise query performance and RU consumption through indexing policies and consistency levels. | — | Not covered. The data lesson explains RUs and consistency tradeoffs; no indexing-policy or query/RU optimisation exercise is provided. [Microsoft Learn][learn200]. |
| Store/retrieve embeddings and run vector similarity search for semantic retrieval. | — | Not covered. Cosmos DB holds P3 job state; the vectors and retrieval queries remain in AI Search. [Microsoft Learn][learn200]. |
| Implement a change feed processor for new/updated items. | — | Not covered. P3 intake uses Event Grid and Service Bus, not the Cosmos DB change feed. [Microsoft Learn][learn200]. |
| **Develop AI solutions by using Azure Database for PostgreSQL** — connect and query through SDKs. | [Data access][db]; [P2 milestone 2][p22] | Covered. Use Npgsql/EF Core with a data source, Entra token refresh and tenant-filtered queries. |
| Model schemas and indexes, choosing tables and data types. | [Data access][db]; [P2 milestone 2][p22] | Covered. Generate and review relational migrations, keys, approval fields and query indexes. |
| Tune indexes to reduce query latency and pgvector compute overhead. | — | Not covered. The course teaches relational query traps; it does not implement or tune pgvector indexes. [Microsoft Learn][learn200]. |
| Configure compute, memory and storage for vector workloads. | — | Not covered. P2 sizes a small transactional store, without measuring or configuring a vector workload. [Microsoft Learn][learn200]. |
| Store embeddings and run vector similarity search, semantic retrieval and metadata-filtered RAG. | — | Not covered. pgvector is compared with AI Search; no PostgreSQL vector retrieval is implemented. [Microsoft Learn][learn200]. |
| Optimise connections for throughput and latency. | — | Not covered. P2 specifies data-source lifetime and credential renewal, without connection/pool performance tuning. [Microsoft Learn][learn200]. |
| **Integrate Azure Managed Redis in AI solutions** — implement caching, expiration and invalidation operations. | — | Not covered. The data lesson explains cache choices; no Redis client operations are implemented. [Microsoft Learn][learn200]. |
| Implement Redis vector indexing for similarity search. | — | Not covered. No Redis vector index or similarity query is built. [Microsoft Learn][learn200]. |

### Connect to and consume Azure services (20–25%)

| Skill | Covered by | Note |
|---|---|---|
| **Develop event- and message-based AI solutions** — process Service Bus queues, dead letters, messages, topics and subscriptions. | [Messaging and events][message]; [P2 milestone 3][p23]; [P3 milestone 2][p32] | Partial. Queue processing has implementation steps; topics/subscriptions have conceptual instruction only. Add topic publishing and subscription receiving with the [official quickstart][topicquick]. |
| Implement Event Grid workflows with filters, custom events and retries. | [Messaging and events][message]; [P3 milestone 5][p35] | Partial. P3 configures filtered BlobCreated subscriptions and delivery recovery; publishing custom events is missing. [Microsoft Learn][learn200]. |
| **Develop and implement Azure Functions** — build serverless APIs with triggers and bindings. | [P3 milestone 1][p31]; [P3 milestone 2][p32]; [P3 milestone 5][p35] | Partial. Event Grid and Service Bus-triggered functions are specified; an HTTP/serverless API and its bindings are not built. [Microsoft Learn][learn200]. |
| Configure and deploy function apps. | [P3 milestone 1][p31]; [P3 milestone 5][p35] | Covered. P3 specifies Flex Consumption, isolated .NET, identities, connection settings and deployment before subscription creation. |

### Secure, monitor, and troubleshoot Azure solutions (20–25%)

| Skill | Covered by | Note |
|---|---|---|
| **Implement secure Azure solutions** — retrieve and rotate secrets with Key Vault. | [Secrets and configuration][secrets]; [P1 milestone 5][p15] | Partial. The lesson teaches vault access and rotation lifecycles; the project does not rehearse an end-to-end secret rotation. [Microsoft Learn][learn200]. |
| Store and retrieve application settings with Azure App Configuration. | [Secrets and configuration][secrets] | Partial. Settings, labels and refresh are explained; store/client integration has no implementation recipe. Add that practice with the [official quickstart][appconfigquick]. |
| **Monitor and troubleshoot Azure solutions** — trace distributed systems with OpenTelemetry SDKs. | [Observability][monitor]; [Evaluation and tracing][eval]; [P1 milestone 5][p15]; [P2 milestone 6][p26] | Covered. Instrument the request/model path and correlate application, dispatch and worker operations. |
| Write KQL queries for logs and metrics. | [Observability][monitor] | Covered. One query over [AppRequests][requesttable] and [AppDependencies][dependencytable] estimates counts, failures and [weighted p95 durations][weightedpercentile]. |

## Gaps \{#gaps}

Plan separate Microsoft Learn work for the objectives marked Not covered and the missing parts of
Partial rows. The course's text RAG service, self-hosted agent and document pipeline leave these gaps:

- **AI-103 vision:** image/video generation and editing, multimodal visual reasoning, captions,
  accessibility descriptions, visual-characteristic extraction, video analysis, Content Understanding
  modes, object/region detection and visual safety. Use the [computer vision training path][vision].
- **AI-103 language and speech:** entity/topic extraction, summaries, structured text-analysis output,
  sentiment/tone and sensitive-content analysis, domain customisation, text translation, speech input,
  speech output, custom speech, audio reasoning and speech translation. Use the
  [language, speech and translation training path][language].
- **AI-103 Foundry application work:** the [Foundry SDK module][sdklearn] and
  [Agent Framework project-connection module][projectlearn] cover project-client integration;
  the [agent training path][agentlearn] supplies the managed-agent and multi-agent implementations.
  Add model-family selection and consumption, reasoning pipelines, prompt/parameter tuning, reflection,
  self-critique and model/flow orchestration from the [AI-103 training][learn103].
- **AI-103 operational and extraction work:** add Foundry project CI/CD, complete private networking,
  drift/index-health monitoring, configured safety policies and signals, safety/explanation evaluation,
  enrichment skillsets, non-document ingestion and semantic field extraction. The [AI-103 training][learn103]
  is the starting point; the table notes identify which part of each objective is missing.
- **AI-200 hosting:** add ACR Tasks, App Service container deployment, queue/event-driven KEDA rules,
  AKS manifests and AKS diagnostics from the [AI-200 training][learn200]. HTTP scaling and Container Apps
  revisions do not cover those tasks.
- **AI-200 data:** add Cosmos DB SDK queries, indexing/RU optimisation, vector retrieval and change feed;
  PostgreSQL vector indexing, vector-resource sizing, filtered RAG and connection tuning; and Redis
  operations and vector indexing. Use the [AI-200 training][learn200]. P2's PostgreSQL approval store
  and P3's Cosmos job records serve different purposes from a vector database exercise.
- **AI-200 integration and security:** add Service Bus topics/subscriptions, custom Event Grid events,
  Functions HTTP APIs, an end-to-end Key Vault rotation and App Configuration client integration from
  the [AI-200 training][learn200].

Python practice remains additional work for both exams, including rows marked Covered.

## Sources \{#sources}

Verified as of 2026-10-19.

- [AI-103 official study guide: skills measured as of 16 April 2026][guide103].
- [AI-200 official study guide: skills measured as of 7 October 2026][guide200], including the conflicting data-management weights.
- [Azure AI Apps and Agents Developer Associate credential][cert103] and its [practice-assessment destination][practice103].
- [Azure AI Cloud Developer Associate credential][cert200] and its [practice-assessment destination][practice200]. Assessment content was not inspected behind sign-in.
- [AI-103 Microsoft Learn course][learn103] and [AI-200 Microsoft Learn course][learn200].
- [Computer vision training][vision] and [language, speech and translation training][language].
- [AI agent training][agentlearn], [Foundry SDK module][sdklearn] and [Agent Framework project-connection module][projectlearn].
- [Azure for .NET developers][dotnetazure].
- [Semantic configuration][semanticconfig] and [semantic query options][semanticquery].
- [Service Bus topics/subscriptions quickstart][topicquick] and [App Configuration quickstart][appconfigquick].
- [AppRequests schema][requesttable], [AppDependencies schema][dependencytable] and [weighted percentiles][weightedpercentile].

[guide103]: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103
[guide200]: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200
[cert103]: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/
[cert200]: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/
[practice103]: https://aiskillsnavigator.microsoft.com/credentials/cert-3fb198f57997226a824aa5f52a1a22af9a4597941b2288ed39371c7a9e6bd7c9
[practice200]: https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b
[learn103]: https://learn.microsoft.com/en-us/training/courses/ai-103t00
[learn200]: https://learn.microsoft.com/en-us/training/courses/ai-200t00
[vision]: https://learn.microsoft.com/en-us/training/paths/develop-computer-vision-with-foundry/
[language]: https://learn.microsoft.com/en-us/training/paths/process-translate-text-azure-cognitive-services/
[agentlearn]: https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/
[sdklearn]: https://learn.microsoft.com/en-us/training/modules/foundry-sdk/
[projectlearn]: https://learn.microsoft.com/en-us/training/modules/develop-ai-agent-with-semantic-kernel/
[dotnetazure]: https://learn.microsoft.com/en-us/dotnet/azure/
[foundry]: ./part-3-llms-on-azure/microsoft-foundry.md
[deploy]: ./part-3-llms-on-azure/deployments-quotas-cost.md
[search]: ./part-3-llms-on-azure/rag-on-ai-search.md
[agents]: ./part-3-llms-on-azure/agents-on-azure.md
[eval]: ./part-3-llms-on-azure/evaluation-and-tracing.md
[safety]: ./part-3-llms-on-azure/platform-safety.md
[enterprise]: ./part-3-llms-on-azure/enterprise-ai.md
[ingestion]: ./part-3-llms-on-azure/document-ingestion.md
[gateway]: ./part-3-llms-on-azure/ai-gateway.md
[compute]: ./part-1-azure-foundations/compute.md
[iac]: ./part-1-azure-foundations/infrastructure-as-code.md
[rbac]: ./part-1-azure-foundations/rbac-and-keyless-access.md
[network]: ./part-1-azure-foundations/networking.md
[monitor]: ./part-1-azure-foundations/observability.md
[message]: ./part-1-azure-foundations/messaging.md
[secrets]: ./part-1-azure-foundations/secrets-and-configuration.md
[db]: ./part-2-modern-dotnet/data-access.md
[ai]: ./part-2-modern-dotnet/ai-in-dotnet.md
[containers]: ./part-2-modern-dotnet/containers-and-aspire.md
[pipelines]: ./part-4-ai-delivery/pipelines-to-azure.md
[release]: ./part-4-ai-delivery/releasing-safely.md
[p11]: ./part-5-projects/rag-service.md#1-establish-one-resource-boundary-and-two-model-deployments
[p13]: ./part-5-projects/rag-service.md#3-turn-public-snapshots-into-searchable-chunks
[p14]: ./part-5-projects/rag-service.md#4-join-retrieval-to-generation-and-validate-citations
[p15]: ./part-5-projects/rag-service.md#5-deploy-the-api-with-identity-settings-and-traces
[p16]: ./part-5-projects/rag-service.md#6-capture-five-answers-and-inspect-their-evaluation
[p17]: ./part-5-projects/rag-service.md#7-deliver-through-oidc-and-rehearse-rollback
[p21]: ./part-5-projects/agent-behind-gateway.md#1-preserve-a-working-p1-baseline
[p22]: ./part-5-projects/agent-behind-gateway.md#2-turn-the-local-store-into-a-durable-approval-boundary
[p23]: ./part-5-projects/agent-behind-gateway.md#3-publish-approved-work-through-a-queue
[p24]: ./part-5-projects/agent-behind-gateway.md#4-let-one-agent-request-approval
[p25]: ./part-5-projects/agent-behind-gateway.md#5-enforce-both-gateway-paths
[p26]: ./part-5-projects/agent-behind-gateway.md#6-capture-evidence-and-evaluate-saved-answers
[p31]: ./part-5-projects/ingestion-pipeline.md#1-bind-p3-to-p1-without-replacing-p1s-resources
[p32]: ./part-5-projects/ingestion-pipeline.md#2-make-one-durable-job-survive-another-delivery
[p33]: ./part-5-projects/ingestion-pipeline.md#3-extract-a-private-source-and-retain-its-structure
[p34]: ./part-5-projects/ingestion-pipeline.md#4-publish-chunks-into-the-existing-retrieval-path
[p35]: ./part-5-projects/ingestion-pipeline.md#5-connect-uploads-then-exercise-replacement-and-recovery
[p36]: ./part-5-projects/ingestion-pipeline.md#6-leave-evidence-that-distinguishes-acceptance-from-completion
[semanticconfig]: https://learn.microsoft.com/en-us/azure/search/semantic-how-to-configure
[semanticquery]: https://learn.microsoft.com/en-us/azure/search/semantic-how-to-query-request
[topicquick]: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-how-to-use-topics-subscriptions
[appconfigquick]: https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-aspnet-core-app
[requesttable]: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/apprequests
[dependencytable]: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/appdependencies
[weightedpercentile]: https://learn.microsoft.com/en-us/kusto/query/percentilesw-aggregation-function?view=microsoft-fabric
