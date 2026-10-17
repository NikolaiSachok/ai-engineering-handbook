# Azure & .NET term ledger (RU/EN)

The **living** term ledger for the Azure & .NET course (`docs-azure-dotnet/`, `locales: ['en', 'ru']`). It
records this course's term decisions — kept-EN vs native form, casing, bridge glosses, rejected variants — and
grows with the course: every new lesson seeds its new terms here and settles them during native authoring.

**Load with `_language.md`.** When authoring this course, load `_language.md` (the shared RU/EN language rules)
**plus this ledger** as standing context. For shared AI-engineering vocabulary (agent, retrieval, eval,
guardrail…), **peek, don't load**: a targeted read-only lookup in `rag.md` / `rag-addendum.md` / `ai-sdlc.md`;
reuse a matching decision verbatim and cite it, or FLAG a genuine sense-difference. Never edit `rag.md` (frozen).

## Language policy — product names

This course names a vendor's products on every page, and the vendor renames them often. So:

- **Product and service names stay in English, exactly as the vendor's current docs write them**, with the
  retrieval date recorded in the page's Sources (Microsoft Entra ID, Azure Container Apps, Microsoft Foundry,
  Azure AI Search, Key Vault, Service Bus…). No Russian rendering, no transliteration. Grammatical case is
  carried by a native head noun when the name would otherwise need to decline: «в сервисе Azure Container
  Apps», «через Key Vault», «ресурс Microsoft Foundry».
- **Former names** appear once, in parentheses, where a reader might know only the old one: «Microsoft Entra
  ID (раньше Azure Active Directory)». Never use a former name as the current one.
- **Role names, SKU and tier names, CLI commands and API identifiers** are code-facing and stay as written
  (`Contributor`, `Storage Blob Data Reader`, `Standard`, `Global Standard`, `azd up`, `DefaultAzureCredential`).
- **Concepts behind the products** follow the house term-rendering policy: an established Russian term in the
  body, English in parentheses at first page-mention (see the table below).

## Book units

| EN | RU |
|---|---|
| Part | Часть |
| Lesson | Урок |
| Project | Проект |
| Appendix | Приложение |
| Recap sheet | **SETTLED** — «шпаргалка»; в intro — «Шпаргалка по Azure»: краткий справочник на нескольких страницах для повторения. |

## Recurring block strings (exact strings, every lesson)

| EN | RU |
|---|---|
| `## Try it` | `## Попробуй` |
| `:::note[Coming from AWS or GCP]` | `:::note[Если ты знаком с AWS или GCP]` |
| `## What to take away` | `## Что перенести в свою практику` (REUSE `ai-sdlc.md` lessons) |
| `**[New terms](…)**:` | `**[Новые термины](…)**:` (REUSE) |
| `## Sources` | `## Источники` |
| `Verified as of YYYY-MM-DD.` | **SETTLED** — `Проверено на DD.MM.YYYY.`; intro закрепляет видимую дату `Проверено на 17.10.2026.`, ISO-формат остаётся во frontmatter. |
| Cost note in Try it: `**Cost:**` | `**Стоимость:**` |
| Teardown in Try it: `**Teardown:**` | **SETTLED** — `**Удаление ресурсов:**`; intro прямо требует удалить ресурсы до завершения практической работы, «Уборка» не называет действие. |

## Cross-course reference conventions

Link the RAG & Agents or AI SDLC lesson that owns an underlying idea (hybrid retrieval, evals, guardrails, the
agent loop) instead of re-teaching it; a cross-course link uses the absolute course path, as the other
courses do. When a link names a lesson by title, use that lesson’s exact Russian title as its visible text.

## Terms awaiting settlement — ON PROBATION

Rows start on probation and are settled during native authoring of the page that first uses them.
Settled recap-sheet decisions are recorded once in the dedicated table below.

| EN term | EN gloss | RU decision |
|---|---|---|
| Ingestion pipeline | P3's processing of incoming documents and updating the retrieval index | **ON PROBATION** — «конвейер загрузки документов (ingestion pipeline)»; конкретизирует нейтральную «загрузку в корпус» из `rag.md` §1.2, не переименовывает стадию Ingestion. |
| Pay-as-you-go | the billing arrangement required to continue after the free-account credit or its 30-day period | **ON PROBATION** — «оплата по мере использования (pay-as-you-go)»; английский мост связывает русский текст с обозначением в Azure. |

## Intro repair — terminology evidence (2026-10-17)

| EN concept / sense | RU decision | Evidence / rejected variant |
|---|---|---|
| Learning path — Microsoft Learn content unit made up of modules | **ON PROBATION** — «схема обучения»; plural «схемы обучения». | Live-checked 2026-10-17: [Microsoft Learn RU FAQ, «Что такое схема обучения?»](https://learn.microsoft.com/ru-ru/training/support/faq) defines the unit as a set of modules; [Python learning path](https://learn.microsoft.com/ru-ru/training/paths/get-started-with-python-fundamentals/) uses «Модули, включенные в эту схему обучения». Reject «учебный маршрут» for this named Learn unit. |
| Governance — platform rules and their enforcement | **SETTLED** — «правила использования платформы и контроль их соблюдения»; in running prose, «общие правила» when the scope is explicit. | Reused in the first lesson, 2026-10-17. Live-checked: [Microsoft Learn RU, Azure Policy overview](https://learn.microsoft.com/ru-ru/azure/governance/policy/overview) describes organizational standards, compliance and allowed-region constraints; [management groups](https://learn.microsoft.com/ru-ru/azure/governance/management-groups/overview) applies common rules across subscriptions. This is a descriptive rendering, not a renamed product. Distinguish it from identity management and the separate billing-contract hierarchy. |
| Async streaming — processing a stream asynchronously | **ON PROBATION** — «асинхронная работа с потоками данных». | Reject «асинхронная потоковая передача» in the .NET course map: it reads as transport only. |
| AI-assisted delivery — AI assists the software delivery process | **ON PROBATION** — «поставка ПО с помощью AI». | Reject «поставка ПО с AI»: it can mean software containing AI. |

## Microsoft Learn link policy

For Russian pages, prefer the `ru-ru` Microsoft Learn URL with the **same path, query and fragment** as the
English source when a live request confirms HTTP 200 at that Russian URL. Otherwise retain `en-us`; never
infer availability from a translated title or a different path. Apply the rule to inline citations and Sources
alike. On 2026-10-17 all 93 distinct Learn URLs used by `recap-sheet.md` returned HTTP 200 at their `ru-ru`
counterparts, without a locale fallback; the additional Learn evidence URLs in the table below were also
live-checked. Other vendors’ URLs and internal course paths are unchanged.

## Recap sheet — settled terms (2026-10-17)

| EN concept / sense | RU decision | Evidence / rejected variant |
|---|---|---|
| Tenant — Entra identity directory | **SETTLED** — «тенант (tenant)», далее «тенант». | Live-checked 2026-10-17: [Microsoft Learn RU, Azure Arc resource organization](https://learn.microsoft.com/ru-ru/azure/azure-arc/servers/cloud-native/inventory-resource), the Azure tenants section, defines the tenant through Microsoft Entra ID. The [application objects page](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals) alternates between «клиент» and «арендатор»; reject both here to avoid confusion with OAuth/SDK clients or resource-renting organizations. |
| Subscription — administration, quota and accumulated-charge boundary | **SETTLED** — «подписка (subscription)», далее «подписка». | Live-checked 2026-10-17: [Microsoft Learn RU, ARM terminology and management scopes](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/overview) uses «подписка» in the resource hierarchy. Distinguish it from a billing account. |
| Resource group — common resource lifecycle | **SETTLED** — «группа ресурсов (resource group)», далее «группа ресурсов». | Live-checked 2026-10-17: [Microsoft Learn RU, ARM resource groups](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/overview) connects the group to a shared lifecycle. Reject «ресурсная группа» in favor of the established documentation term. |
| Management group — subscription hierarchy scope | **SETTLED** — «группа управления (management group)», далее «группа управления». | Live-checked 2026-10-17: [Microsoft Learn RU, ARM management scopes](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/overview) places subscriptions under management groups. This is a concept, not a product name. |
| Billing account — commercial invoicing hierarchy | **SETTLED** — «учётная запись для выставления счетов (billing account)». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, billing and tenant relationships](https://learn.microsoft.com/ru-ru/azure/cost-management-billing/understand/understand-billing-tenant-relationship), live-checked the same day, uses the billing-account wording and distinguishes billing roles and contracts from subscription administration. Reject «платёжная учётная запись» for this sense. |
| Control plane; data plane — resource management versus resource use | **SETTLED** — «плоскость управления (control plane)» и «плоскость данных (data plane)». | Live-checked 2026-10-17: [Microsoft Learn RU, control plane and data plane](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/control-plane-and-data-plane). The body varies between «уровень» and «плоскость»; adopt the symmetrical title pair. Reject bare English and mixed pairs. |
| Managed identity — platform-managed workload credentials | **SETTLED** — «управляемое удостоверение (managed identity)», далее «управляемое удостоверение»; подвиды — «назначаемое системой (system-assigned)» и «назначаемое пользователем (user-assigned)». | Live-checked 2026-10-17: [Microsoft Learn RU, managed identities](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview). Reject «управляемая идентичность» to keep Entra identity terminology consistent. |
| Service principal — tenant-local workload identity | **SETTLED** — «субъект-служба (service principal)», далее «субъект-служба». | Live-checked 2026-10-17: [Microsoft Learn RU, application objects and service principals](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals), the service principal object section. Reject «сервисный принципал» and «учётная запись службы»: the latter loses the global-template versus tenant-local-instance relationship. |
| App registration — global identity blueprint | **SETTLED** — «регистрация приложения (app registration)»; в определении — «глобальное описание (шаблон) приложения». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, application objects](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals), live-checked the same day. Preserve the blueprint versus local service-principal contrast rather than a generic description of an application. |
| Keyless access — token authentication without stored keys | **SETTLED** — «доступ без ключей (keyless access)». | Live-checked 2026-10-17: [Microsoft Learn RU, keyless connections](https://learn.microsoft.com/ru-ru/azure/developer/ai/keyless-connections) uses keyless connection and authentication wording. Reject the erroneous serverless wording in that page’s metadata: keyless does not mean serverless. |
| Workload identity federation — external tokens exchanged for Entra access tokens | **SETTLED** — «федерация удостоверений рабочей нагрузки (workload identity federation)». | Live-checked 2026-10-17: [Microsoft Learn RU, workload identity federation](https://learn.microsoft.com/ru-ru/entra/workload-id/workload-identity-federation), the introduction and external-provider trust description. Reject «федерация идентификации»; use the Entra identity vocabulary consistently. |
| Conditional Access — identity-based access policies | **SETTLED** — kept-EN «Conditional Access (условный доступ)» при первом упоминании, далее «Conditional Access». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, Conditional Access](https://learn.microsoft.com/ru-ru/entra/identity/conditional-access/overview), live-checked the same day, attests the gloss. User, device, location and risk are examples of signals; MFA and blocking access are examples of controls. Do not narrow access to sign-in. |
| Network security group (NSG) — stateful packet rules | **SETTLED** — «группа безопасности сети (NSG)», далее «NSG». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, network security groups](https://learn.microsoft.com/ru-ru/azure/virtual-network/network-security-groups-overview), live-checked the same day, uses this noun phrase. Preserve both allow and deny; a bare acronym at first mention loses the concept. |
| Private endpoint — private-IP network interface exposing a supported service | **SETTLED** — «частная конечная точка (private endpoint)». | Live-checked 2026-10-17: [Microsoft Learn RU, VNet service integration](https://learn.microsoft.com/ru-ru/azure/virtual-network/vnet-integration-for-azure-services). Distinguish a service endpoint, which uses the service’s public address without creating a private IP. Reject «приватный эндпоинт». |
| Private DNS zone — private name resolution for linked VNets | **SETTLED** — «частная зона DNS (private DNS zone)». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, private DNS](https://learn.microsoft.com/ru-ru/azure/dns/private-dns-overview), live-checked the same day, uses «частные зоны DNS» and explains resolution through VNet links. State what the zone supplies, rather than only requiring names to resolve. |
| Deployment of a model — named serving configuration | **SETTLED** — «развёртывание модели (model deployment)». | Live-checked 2026-10-17: [Microsoft Learn RU, model resource and deployment creation](https://learn.microsoft.com/ru-ru/azure/foundry-classic/openai/how-to/create-resource), the deployment section: code uses the deployment name. Distinguish the named object from the application-deployment process; reject «деплоймент». |
| Landing zone — governed foundation for workloads | **SETTLED** — «целевая зона (landing zone)». | Live-checked 2026-10-17: [Microsoft Learn RU, landing zone definition](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ready/landing-zone/) and [design areas](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ready/landing-zone/design-areas). Reject literal aviation metaphors «посадочная зона», «зона высадки», «зона приземления»; Learn itself varies. |
| Governance guardrails — common platform rules and constraints | **SETTLED** — «правила и ограничения»; в Q1 — «для общих правил и ограничений». | Accepted independent-critic sense distinction, 2026-10-17. The intro’s broader governance explanation is settled separately in the intro terminology table. REUSE `rag.md` §1.2: «ограничители» belongs to LLM/agent guardrails and must not be transferred to common Azure governance rules. |
| AI gateway — control access to AI services | **SETTLED** — «AI-шлюз (AI gateway)»; не переименовывает продукт API Management. | REUSE `rag.md` §1.2 «LLM-шлюз», extending the scope to AI services; already introduced in the RU intro. Live-checked 2026-10-17: [Microsoft Learn RU, AI gateway capabilities](https://learn.microsoft.com/ru-ru/azure/api-management/genai-gateway-capabilities) uses gateway terminology. AI spelling follows `_language.md`. |
| Deployment slot — App Service application slot | **SETTLED** — «рабочий слот»; при указании назначения — «рабочий слот прода». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, App Service slots](https://learn.microsoft.com/ru-ru/azure/app-service/deploy-staging-slots), live-checked the same day. Keep Standard, Premium and Isolated as plan names. |
| Rollout — staged release to users | **SETTLED** — «выкатка»; для staged rollout — «поэтапная выкатка». | REUSE the linked AI SDLC page’s title and usage: «Наблюдаемость, выкатка и аварийный стоп» (`part-4-platform/observability-rollout.md`); accepted independent-critic finding, 2026-10-17. Do not substitute deployment for release progression. |
| Production — live operation in prose | **SETTLED** — «прод», «в проде» по контексту. | REUSE `ai-sdlc.md` and the linked RU observability/rollout lesson; accepted independent-critic finding, 2026-10-17. Product names and protected identifiers remain unchanged. |
| Log Analytics workspace — telemetry store and query-access boundary | **SETTLED** — «рабочая область Log Analytics (Log Analytics workspace)», далее «рабочая область Log Analytics». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, Azure Monitor](https://learn.microsoft.com/ru-ru/azure/azure-monitor/fundamentals/overview), live-checked the same day. Keep the product name and translate the resource concept. |

## Part overview repair — terminology (2026-10-17)

| EN concept / sense | RU decision | Evidence / rejected variant |
|---|---|---|
| Identity — Entra credentials and access, lesson-title sense | **SETTLED** — «Удостоверения I — Microsoft Entra ID» / «Удостоверения II — RBAC и доступ без ключей». | Accepted independent-critic finding, 2026-10-17; settlement confirmed by independent RU critics (fidelity + naturalness), 2026-10-17. Live-checked: [Microsoft Learn RU, managed identities](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview) uses «удостоверение» for the represented actor and its managed credentials. Reject «Идентификация» for these titles: it names a process rather than an identity. |
| Service endpoint — VNet access to a service's public endpoint | **ON PROBATION** — «конечная точка службы (service endpoint)». | Accepted independent-critic finding, 2026-10-17; paired with the settled private-endpoint sense above. Do not conflate the two mechanisms. |
| DI lifetime — lifetime of an object managed by the dependency-injection container | **ON PROBATION** — «время жизни»; в обзоре «время жизни объектов». | Accepted independent-critic finding, 2026-10-17. Reject «сроки жизни» in this sense. |
| Options pattern — named .NET configuration pattern | **ON PROBATION** — «паттерн Options (options pattern)». | Accepted independent-critic finding, 2026-10-17. Preserve Options casing; reject «шаблон options». |
| Groundedness detection — platform feature checking responses against supplied source material | **ON PROBATION** — kept-EN «groundedness detection (проверка опоры ответа на источники)», далее «groundedness detection». | [Microsoft Learn, Groundedness detection](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/groundedness), fetched 2026-10-17. Keep the feature name with a short Russian gloss; a gloss alone loses the name readers meet in the product documentation. |
| Request unit (RU) — Cosmos DB throughput accounting unit | **ON PROBATION** — «единица запроса (RU)», во множественном числе «единицы запросов». | The course plan’s Cosmos DB hook names RUs; accepted overview alignment, 2026-10-17. RU here is a service unit, not a locale code. |

## How Azure is organised — terminology evidence (2026-10-17)

The lesson reuses the settled tenant, subscription, management-group, resource-group, billing-account,
control/data-plane, app-registration, managed-identity and model-deployment senses above. Rows still marked **ON PROBATION** await an independent language pass; live Microsoft evidence
establishes the technical sense and attested wording, without claiming that such a pass ran. Later
settlements are recorded in the relevant rows.

| EN concept / sense | RU decision | Evidence / rejected variant |
|---|---|---|
| Resource — Azure-managed item | **SETTLED** — «ресурс (resource)», then «ресурс». | Live-checked 2026-10-17: [Microsoft Learn RU, ARM terminology](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/overview) defines an Azure-managed item. Some resource types exist above resource-group scope; do not narrow the definition to items inside a group. Settlement confirmed by independent RU critics (fidelity + naturalness), 2026-10-17; the same RU page was live-checked again on that date. |
| Resource provider — service supplying resource types and operations | **ON PROBATION** — «поставщик ресурсов (resource provider)». | Live-checked 2026-10-17: [Microsoft Learn RU, ARM terminology](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/overview) attests «поставщик ресурсов». It is an Azure service, not the organisation selling cloud services. |
| Scope — extent of a management assignment | **ON PROBATION** — «область действия (scope)». | Live-checked 2026-10-17: [Microsoft Learn RU, RBAC scope levels](https://learn.microsoft.com/ru-ru/azure/role-based-access-control/scope-overview) uses «область действия» for the resource set and inherited assignments. Reject «масштаб» for this technical sense. |
| Resource ID — full management-hierarchy identifier | **SETTLED** — «идентификатор ресурса (resource ID)». | Live-checked 2026-10-17: [Microsoft Learn RU, scope format](https://learn.microsoft.com/ru-ru/azure/role-based-access-control/scope-overview#scope-format) attests «идентификатор ресурса» and the subscription, group and provider path. A group's own ID ends before a child-resource provider path. Settlement confirmed by independent RU critics (fidelity + naturalness), 2026-10-17; the same-path [RU managed-identity REST reference](https://learn.microsoft.com/ru-ru/rest/api/managedidentity/user-assigned-identities/get?view=rest-managedidentity-2024-11-30), also live-checked, distinguishes `id` from `clientId` and `principalId`. In the Entra lesson use «идентификатор ресурса Azure (Azure resource ID)» to make the distinction explicit. |
| Azure Resource Manager (ARM) — common deployment and management service | **ON PROBATION** — kept-EN «Azure Resource Manager (ARM)», then «ARM» or «Resource Manager». | Live-checked 2026-10-17: [Microsoft Learn RU, ARM overview](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/overview) retains the English product name and describes management-request routing. Reject «диспетчер ресурсов» as a product-name substitution under this course's policy. |
| Region — geographical placement of Azure regional services | **ON PROBATION** — «регион (region)». | Live-checked 2026-10-17: [Microsoft Learn RU, regions overview](https://learn.microsoft.com/ru-ru/azure/reliability/regions-overview) uses «регион». Keep it distinct from a broader Azure geography, a data zone and the metadata location of a resource group. |
| Availability zone — independent infrastructure within a region | **ON PROBATION** — «зона доступности (availability zone)». | Live-checked 2026-10-17: [Microsoft Learn RU, availability zones](https://learn.microsoft.com/ru-ru/azure/reliability/availability-zones-overview) attests the term and separate datacentres. Do not imply recovery from a whole-region outage. |
| Zonal resource — resource in a selected zone | **ON PROBATION** — «зональный ресурс (zonal resource)». | Live-checked 2026-10-17: [Microsoft Learn RU, zone-support types](https://learn.microsoft.com/ru-ru/azure/reliability/availability-zones-overview) uses «зональные ресурсы» for selected-zone deployment. The term does not itself promise zone-failure tolerance. |
| Zone-redundant resource — service distributes or replicates across zones | **ON PROBATION** — «ресурс с избыточностью между зонами (zone-redundant resource)». | Live-checked 2026-10-17: [Microsoft Learn RU, zone-support types](https://learn.microsoft.com/ru-ru/azure/reliability/availability-zones-overview) uses «ресурсы с избыточностью между зонами». Prefer this explicit phrase to the page's competing compressed adjective «зонально-избыточный». |
| Tag — name-value metadata for organisation and cost attribution | **ON PROBATION** — «тег (tag)», plural bridge «теги (tags)». | Live-checked 2026-10-17: [Microsoft Learn RU, tags](https://learn.microsoft.com/ru-ru/azure/azure-resource-manager/management/tag-resources) attests «теги» for resource, group and subscription metadata. Use «тег» consistently in prose and tables. A tag grants no access; group tags do not automatically propagate to resources. |
| Cost Management tag inheritance — tags on child usage records | **ON PROBATION** — «наследование тегов в Cost Management (tag inheritance)». | Live-checked 2026-10-17: [Microsoft Learn RU, tag inheritance](https://learn.microsoft.com/ru-ru/azure/cost-management-billing/costs/enable-tag-inheritance) attests «наследование тегов» and distinguishes usage records from resource tags. Preserve opt-in behaviour and support **only** for EA/MCA/MPA billing accounts, with the additional Azure plan requirement for MPA. |
| Budget — cost or usage target with notifications | **ON PROBATION** — «бюджет (budget)». | Live-checked 2026-10-17: [Microsoft Learn RU, budgets](https://learn.microsoft.com/ru-ru/azure/cost-management-billing/costs/tutorial-acm-create-budgets) attests «бюджет» and actual-cost notifications. Reject «лимит расходов»: a budget does not stop consumption. |
| Soft delete — recoverable retained state after deletion | **ON PROBATION** — «обратимое удаление (soft delete)»; purge — «окончательное удаление». | Live-checked 2026-10-17: [Microsoft Learn RU, Key Vault soft delete](https://learn.microsoft.com/ru-ru/azure/key-vault/general/soft-delete-overview) uses «обратимое удаление» alongside «мягкое удаление». Prefer the recoverability-based term; retain the distinction from final deletion and immediate name reuse. |

All 34 distinct Microsoft Learn destinations in the lesson packet returned HTTP 200 at their same-path
`ru-ru` counterparts on 2026-10-17, without an English-locale fallback. Published URLs retain the source
path, query and fragment. Azure pricing links and internal course paths remain as supplied in the packet.

## Entra ID — terminology evidence (2026-10-17)

The lesson reuses the settled tenant, subscription, resource-group, app-registration, service-principal
and managed-identity decisions, including the system-assigned and user-assigned subtype wording. The
lesson-title identity sense, resource and resource-ID rows above are confirmed by independent RU critics
(fidelity + naturalness), 2026-10-17. New rows below remain **ON PROBATION** after the accepted
claim-level and naturalness findings from those critics were applied. The live Microsoft ru-ru evidence
establishes the sense and attested vocabulary; review does not automatically settle new rows.

| EN concept / sense | RU decision | Evidence / rejected variant |
|---|---|---|
| Workload — running software represented by an identity, broader than an app-registration application | **ON PROBATION** — «рабочая нагрузка»; keep distinct from «приложение» in the application-object sense. | Accepted independent RU fidelity finding 3, 2026-10-17; reuses the wording in the settled workload-identity-federation row. Managed identities have service principals without application objects. Use the workload sense in sharing, permission boundaries and the corresponding glossary definitions. |
| Microsoft Entra ID — identity and access management service | **ON PROBATION** — kept-EN «Microsoft Entra ID»; shorter «Entra ID» only where the source uses it. | Live-checked 2026-10-17: [Microsoft Learn RU, application objects](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals) preserves this product spelling. Follow the course product-name rule; reject translated or transliterated product names. |
| User — person represented in the directory | **ON PROBATION** — «пользователь (user)», then «пользователь». | Live-checked 2026-10-17: [Microsoft Learn RU, groups and access](https://learn.microsoft.com/ru-ru/entra/fundamentals/concept-learn-about-groups) distinguishes individual users from groups. Do not use this word for the API's own downstream identity. |
| Security group — membership-based access administration | **ON PROBATION** — «группа безопасности (security group)». | Live-checked 2026-10-17: [Microsoft Learn RU, group types](https://learn.microsoft.com/ru-ru/entra/fundamentals/concept-learn-about-groups) uses «группы безопасности» and permits service-principal membership. Distinguish from the already settled network security group. |
| Application object — home-tenant identity configuration and template | **ON PROBATION** — «объект приложения (application object)». | Live-checked 2026-10-17: [Microsoft Learn RU, application object](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals) attests the term and the template-to-local-principal relationship. Registration configures identity; it does not deploy executable code. A managed identity has no associated application object. |
| Credentials — authentication material, not identifiers | **ON PROBATION** — «учётные данные (credentials)», then «учётные данные». | Live-checked 2026-10-17: [Microsoft Learn RU, managed identities](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview) uses «учетные данные» for material managed by Azure. Do not equate the material with a client ID, principal ID or resource ID. |
| Client ID — selector for application or managed identity | **ON PROBATION** — «идентификатор клиента (client ID)»; retain `clientId` in code, «client ID» when referring back to the selector. | Live-checked 2026-10-17: [Microsoft Learn RU, app registration](https://learn.microsoft.com/ru-ru/entra/identity-platform/quickstart-register-app) uses «идентификатор приложения (клиента)»; the [RU managed-identity REST reference](https://learn.microsoft.com/ru-ru/rest/api/managedidentity/user-assigned-identities/get?view=rest-managedidentity-2024-11-30) exposes `clientId`. The shorter native form covers both application and managed-identity selection. It is an identifier, not authentication proof. |
| Principal ID — service principal object ID used for access grants | **ON PROBATION** — «идентификатор субъекта (principal ID)»; explain as «идентификатор объекта субъекта-службы»; retain `principalId` in code. | Live-checked 2026-10-17: [Microsoft Learn RU, developer overview](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview-for-developers) associates principal ID with the identity's service principal; the [RU REST reference](https://learn.microsoft.com/ru-ru/rest/api/managedidentity/user-assigned-identities/get?view=rest-managedidentity-2024-11-30) distinguishes `principalId`, `clientId` and `id`. Reject «главный идентификатор»: principal names the represented actor, not priority. |
| Access token — credential presented to a protected API | **ON PROBATION** — «токен доступа (access token)». | Live-checked 2026-10-17: [Microsoft Learn RU, access tokens](https://learn.microsoft.com/ru-ru/entra/identity-platform/access-tokens) varies between «токен» and «маркер доступа». Adopt «токен» consistently with the ID-token heading below; distinguish this security credential from model text-token counts. |
| Audience — intended API recipient of a token | **ON PROBATION** — «аудитория (audience)»; explain as «API, которому предназначен токен»; retain `aud`. | Live-checked 2026-10-17: [Microsoft Learn RU, access-token claims](https://learn.microsoft.com/ru-ru/entra/identity-platform/access-token-claims-reference) calls `aud` the token's «целевая аудитория». It identifies the receiving API, not a group of human users. |
| ID token — OpenID Connect evidence of user authentication for a client | **ON PROBATION** — «токен идентификации (ID token)». | Live-checked 2026-10-17: [Microsoft Learn RU, ID tokens](https://learn.microsoft.com/ru-ru/entra/identity-platform/id-tokens) uses «Токены идентификации» in its title and excludes API calls as their purpose. Reject «токен доступа» for this sense. |
| Authentication — establishing the caller's identity | **ON PROBATION** — «аутентификация (authentication)». | Live-checked 2026-10-17: [Microsoft Learn RU, service-principal objects](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals) uses «аутентификация» for sign-in and distinguishes it from resource-access authorisation. «Проверка подлинности» occurs in Learn too; keep one term in this lesson. |
| Authorisation — deciding whether an operation is permitted | **ON PROBATION** — «авторизация (authorisation)». | Live-checked 2026-10-17: [Microsoft Learn RU, service-principal objects](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals) uses «авторизация» for resource access. Reject use of this word for sign-in or token validation alone. |
| Claim — named statement carried in a JWT | **ON PROBATION** — «утверждение (claim)» when defining the term; `iss`, `aud`, `nbf`, `exp` remain literal. | Live-checked 2026-10-17: [Microsoft Learn RU, claims validation](https://learn.microsoft.com/ru-ru/entra/identity-platform/claims-validation) and [claims reference](https://learn.microsoft.com/ru-ru/entra/identity-platform/access-token-claims-reference) use «утверждение». Do not substitute «заявка» or an unbridged «клейм». |
| Issuer — token-issuing authority identified by `iss` | **ON PROBATION** — «издатель»; retain `iss` as the bridge in the validation checklist. | Live-checked 2026-10-17: [Microsoft Learn RU, access-token claims](https://learn.microsoft.com/ru-ru/entra/identity-platform/access-token-claims-reference) uses «издатель» in the issuer discussion. Distinguish the issuer from the API named by `aud`. |
| Identity endpoint — host-provided managed-identity token acquisition endpoint | **ON PROBATION** — «конечная точка удостоверения»; in prose explain that the hosting platform provides it. | Live-checked 2026-10-17: [Microsoft Learn RU, managed identities in Container Apps](https://learn.microsoft.com/ru-ru/azure/container-apps/managed-identity) describes the platform endpoint. This is a token-acquisition endpoint, not the protected downstream service or a private network endpoint. |

All 33 distinct Microsoft Learn URLs in the Entra semantic packet returned HTTP 200 at their same-path
`ru-ru` counterparts on 2026-10-17, without an English-locale fallback. Path, query and fragment are
preserved in inline links and Sources. Internal course links are unchanged. Shared retrieval vocabulary
reuses `rag.md` §1.2 («поиск» for retrieval as an action); no sibling ledger was changed.
