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
| Governance — platform rules and their enforcement | **ON PROBATION** — in the intro, «правила использования платформы и контроль их соблюдения». | Distinguishes governance from identity; avoid the ambiguous pair «управление удостоверениями / управление платформой» in the course map. |
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
| Service principal — tenant-local application identity | **SETTLED** — «субъект-служба (service principal)», далее «субъект-служба». | Live-checked 2026-10-17: [Microsoft Learn RU, application objects and service principals](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals), the service principal object section. Reject «сервисный принципал» and «учётная запись службы»: the latter loses the global-template versus tenant-local-instance relationship. |
| App registration — global identity blueprint | **SETTLED** — «регистрация приложения (app registration)»; в определении — «глобальное описание (шаблон) приложения». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, application objects](https://learn.microsoft.com/ru-ru/entra/identity-platform/app-objects-and-service-principals), live-checked the same day. Preserve the blueprint versus local service-principal contrast rather than a generic description of an application. |
| Keyless access — token authentication without stored keys | **SETTLED** — «доступ без ключей (keyless access)». | Live-checked 2026-10-17: [Microsoft Learn RU, keyless connections](https://learn.microsoft.com/ru-ru/azure/developer/ai/keyless-connections) uses keyless connection and authentication wording. Reject the erroneous serverless wording in that page’s metadata: keyless does not mean serverless. |
| Workload identity federation — external tokens exchanged for Entra access tokens | **SETTLED** — «федерация удостоверений рабочей нагрузки (workload identity federation)». | Live-checked 2026-10-17: [Microsoft Learn RU, workload identity federation](https://learn.microsoft.com/ru-ru/entra/workload-id/workload-identity-federation), the introduction and external-provider trust description. Reject «федерация идентификации»; use the Entra identity vocabulary consistently. |
| Conditional Access — identity-based access policies | **SETTLED** — kept-EN «Conditional Access (условный доступ)» при первом упоминании, далее «Conditional Access». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, Conditional Access](https://learn.microsoft.com/ru-ru/entra/identity/conditional-access/overview), live-checked the same day, attests the gloss. User, device, location and risk are examples of signals; MFA and blocking access are examples of controls. Do not narrow access to sign-in. |
| Network security group (NSG) — stateful packet rules | **SETTLED** — «группа безопасности сети (NSG)», далее «NSG». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, network security groups](https://learn.microsoft.com/ru-ru/azure/virtual-network/network-security-groups-overview), live-checked the same day, uses this noun phrase. Preserve both allow and deny; a bare acronym at first mention loses the concept. |
| Private endpoint — private-IP network interface exposing a supported service | **SETTLED** — «частная конечная точка (private endpoint)». | Live-checked 2026-10-17: [Microsoft Learn RU, VNet service integration](https://learn.microsoft.com/ru-ru/azure/virtual-network/vnet-integration-for-azure-services). Distinguish a service endpoint, which uses the service’s public address without creating a private IP. Reject «приватный эндпоинт». |
| Private DNS zone — private name resolution for linked VNets | **SETTLED** — «частная зона DNS (private DNS zone)». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, private DNS](https://learn.microsoft.com/ru-ru/azure/dns/private-dns-overview), live-checked the same day, uses «частные зоны DNS» and explains resolution through VNet links. State what the zone supplies, rather than only requiring names to resolve. |
| Deployment of a model — named serving configuration | **SETTLED** — «развёртывание модели (model deployment)». | Live-checked 2026-10-17: [Microsoft Learn RU, model resource and deployment creation](https://learn.microsoft.com/ru-ru/azure/foundry-classic/openai/how-to/create-resource), the deployment section: code uses the deployment name. Distinguish the named object from the application-deployment process; reject «деплоймент». |
| Landing zone — governed foundation for workloads | **SETTLED** — «целевая зона (landing zone)». | Live-checked 2026-10-17: [Microsoft Learn RU, landing zone definition](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ready/landing-zone/) and [design areas](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ready/landing-zone/design-areas). Reject literal aviation metaphors «посадочная зона», «зона высадки», «зона приземления»; Learn itself varies. |
| Governance guardrails — common platform rules and constraints | **SETTLED** — «правила и ограничения»; в Q1 — «для общих правил и ограничений». | Accepted independent-critic sense distinction, 2026-10-17. The intro’s broader governance explanation remains a separate sense under probation. REUSE `rag.md` §1.2: «ограничители» belongs to LLM/agent guardrails and must not be transferred to common Azure governance rules. |
| AI gateway — control access to AI services | **SETTLED** — «AI-шлюз (AI gateway)»; не переименовывает продукт API Management. | REUSE `rag.md` §1.2 «LLM-шлюз», extending the scope to AI services; already introduced in the RU intro. Live-checked 2026-10-17: [Microsoft Learn RU, AI gateway capabilities](https://learn.microsoft.com/ru-ru/azure/api-management/genai-gateway-capabilities) uses gateway terminology. AI spelling follows `_language.md`. |
| Deployment slot — App Service application slot | **SETTLED** — «рабочий слот»; при указании назначения — «рабочий слот прода». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, App Service slots](https://learn.microsoft.com/ru-ru/azure/app-service/deploy-staging-slots), live-checked the same day. Keep Standard, Premium and Isolated as plan names. |
| Rollout — staged release to users | **SETTLED** — «выкатка»; для staged rollout — «поэтапная выкатка». | REUSE the linked AI SDLC page’s title and usage: «Наблюдаемость, выкатка и аварийный стоп» (`part-4-platform/observability-rollout.md`); accepted independent-critic finding, 2026-10-17. Do not substitute deployment for release progression. |
| Production — live operation in prose | **SETTLED** — «прод», «в проде» по контексту. | REUSE `ai-sdlc.md` and the linked RU observability/rollout lesson; accepted independent-critic finding, 2026-10-17. Product names and protected identifiers remain unchanged. |
| Log Analytics workspace — telemetry store and query-access boundary | **SETTLED** — «рабочая область Log Analytics (Log Analytics workspace)», далее «рабочая область Log Analytics». | Accepted independent-critic finding, 2026-10-17; [Microsoft Learn RU, Azure Monitor](https://learn.microsoft.com/ru-ru/azure/azure-monitor/fundamentals/overview), live-checked the same day. Keep the product name and translate the resource concept. |

## Part overview repair — terminology (2026-10-17)

| EN concept / sense | RU decision | Evidence / rejected variant |
|---|---|---|
| Identity — Entra credentials and access, lesson-title sense | **ON PROBATION** — «Удостоверения I — Microsoft Entra ID» / «Удостоверения II — RBAC и доступ без ключей». | Accepted independent-critic finding, 2026-10-17; follows the settled Entra vocabulary above. Reject «Идентификация» for these titles. |
| Service endpoint — VNet access to a service's public endpoint | **ON PROBATION** — «конечная точка службы (service endpoint)». | Accepted independent-critic finding, 2026-10-17; paired with the settled private-endpoint sense above. Do not conflate the two mechanisms. |
| DI lifetime — lifetime of an object managed by the dependency-injection container | **ON PROBATION** — «время жизни»; в обзоре «время жизни объектов». | Accepted independent-critic finding, 2026-10-17. Reject «сроки жизни» in this sense. |
| Options pattern — named .NET configuration pattern | **ON PROBATION** — «паттерн Options (options pattern)». | Accepted independent-critic finding, 2026-10-17. Preserve Options casing; reject «шаблон options». |
| Groundedness detection — platform feature checking responses against supplied source material | **ON PROBATION** — kept-EN «groundedness detection (проверка опоры ответа на источники)», далее «groundedness detection». | [Microsoft Learn, Groundedness detection](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/groundedness), fetched 2026-10-17. Keep the feature name with a short Russian gloss; a gloss alone loses the name readers meet in the product documentation. |
| Request unit (RU) — Cosmos DB throughput accounting unit | **ON PROBATION** — «единица запроса (RU)», во множественном числе «единицы запросов». | The course plan’s Cosmos DB hook names RUs; accepted overview alignment, 2026-10-17. RU here is a service unit, not a locale code. |
