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
courses do.

## Terms new to this course — ON PROBATION

Rows start on probation and are settled during native authoring of the page that first uses them.

| EN term | EN gloss | RU decision |
|---|---|---|
| Tenant | the Entra directory an organisation's identities live in | **ON PROBATION** — «тенант» (established in RU Azure practice) |
| Subscription | the unit of billing, quota and administrative boundary | **ON PROBATION** — «подписка» |
| Resource group | resources with a shared lifecycle | **ON PROBATION** — «группа ресурсов» |
| Control plane / data plane | managing a resource vs using what it holds | **ON PROBATION** — «уровень управления / уровень данных» vs kept-EN «control plane / data plane» |
| Managed identity | a workload identity whose credentials the platform manages | **ON PROBATION** — «управляемое удостоверение (managed identity)» (Microsoft's own RU docs) vs kept-EN |
| Service principal | an application's identity inside a tenant | **ON PROBATION** — «субъект-служба» (Microsoft RU docs) vs kept-EN «service principal» |
| Keyless access | authenticating with tokens, no stored keys | **ON PROBATION** — «доступ без ключей» |
| Workload identity federation | trusting an external identity provider's tokens (e.g. CI) instead of a secret | **ON PROBATION** — «федерация удостоверений рабочей нагрузки» vs kept-EN |
| Private endpoint | a private IP for a platform service inside a virtual network | **ON PROBATION** — «частная конечная точка (private endpoint)» |
| Deployment (of a model) | an addressable serving configuration of a model | **ON PROBATION** — «развёртывание модели» |
| Landing zone | a governed foundation workloads deploy into | **ON PROBATION** — «landing zone» kept-EN vs «целевая зона» (Microsoft RU docs) |
| AI gateway | a gateway controlling access to AI services; P2's agent sits behind it | **ON PROBATION** — «AI-шлюз (AI gateway)»; расширяет «LLM-шлюз» из `rag.md` §1.2 на AI-сервисы, без привязки к продукту Microsoft. |
| Ingestion pipeline | P3's processing of incoming documents and updating the retrieval index | **ON PROBATION** — «конвейер загрузки документов (ingestion pipeline)»; конкретизирует нейтральную «загрузку в корпус» из `rag.md` §1.2, не переименовывает стадию Ingestion. |
| Pay-as-you-go | the billing arrangement required to continue after the free-account credit or its 30-day period | **ON PROBATION** — «оплата по мере использования (pay-as-you-go)»; английский мост связывает русский текст с обозначением в Azure. |

## Intro repair — terminology evidence (2026-10-17)

| EN concept / sense | RU decision | Evidence / rejected variant |
|---|---|---|
| Learning path — Microsoft Learn content unit made up of modules | **ON PROBATION** — «схема обучения»; plural «схемы обучения». | Live-checked 2026-10-17: [Microsoft Learn RU FAQ, «Что такое схема обучения?»](https://learn.microsoft.com/ru-ru/training/support/faq) defines the unit as a set of modules; [Python learning path](https://learn.microsoft.com/ru-ru/training/paths/get-started-with-python-fundamentals/) uses «Модули, включенные в эту схему обучения». Reject «учебный маршрут» for this named Learn unit. |
| Governance — platform rules and their enforcement | **ON PROBATION** — in the intro, «правила использования платформы и контроль их соблюдения». | Distinguishes governance from identity; avoid the ambiguous pair «управление удостоверениями / управление платформой» in the course map. |
| Async streaming — processing a stream asynchronously | **ON PROBATION** — «асинхронная работа с потоками данных». | Reject «асинхронная потоковая передача» in the .NET course map: it reads as transport only. |
| AI-assisted delivery — AI assists the software delivery process | **ON PROBATION** — «поставка ПО с помощью AI». | Reject «поставка ПО с AI»: it can mean software containing AI. |
