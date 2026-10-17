---
title: Защита на уровне платформы
sidebar_position: 3
last_verified: 2026-10-17
---

# Если генерация заблокирована, приложение должно сообщить об этом

При подготовке ответа по документам риск возникает на разных этапах: пользователь может запросить вредоносное содержимое, найденная страница — содержать инструкции для модели, а модель — воспроизвести защищённый материал в ответе. Даже если поиск вернул нужный фрагмент, выдавать ответ пользователю бывает нельзя. Если проверять только вопрос пользователя, найденный контекст и сгенерированный ответ останутся без проверки.

Фильтрация меняет контракт API. Вызов модели может завершиться успешно на уровне HTTP, но без ответа, который можно показать. Если твоё API вернёт пустой ответ со ссылками на источники, клиент не поймёт, заблокировала ли генерацию проверка безопасности или для ответа не хватило подтверждений в источниках. Тебе нужно выяснить, какие проверки применяются, как читать их результаты и что приложение ответит при блокировке генерации.

## Как это устроено в Azure \{#how-it-works-on-azure}

В Microsoft Foundry проверки объединены в именованный ограничитель. Для каждой проверки задаются риск, этап проверки и действие при обнаружении: добавить аннотацию (annotation) или заблокировать содержимое. У развёртывания модели проверяются входные и выходные данные. Проверки вызовов инструментов и их ответов относятся к ограничителям агентов и отдельно помечены как preview. P1 вызывает развёртывание модели из собственного API. Проверки для агентов при таком вызове не применяются. См. [обзор ограничителей](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/guardrails-overview).

Конфигурация хранится в политике RAI (RAI policy, responsible AI policy), а свойство развёртывания [`raiPolicyName`](https://learn.microsoft.com/ru-ru/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts/deployments) указывает, какая политика к нему привязана. После создания своей политики её нужно отдельно привязать к развёртыванию. При диагностике проверяй именно эту привязку: сохранённая в ресурсе политика может не применяться к развёртыванию чата.

Базовые фильтры содержимого (content filters) проверяют четыре категории: ненависть, сексуальный контент, насилие и самоповреждение. Для каждой категории классификатор определяет уровень серьёзности (severity level): `safe`, `low`, `medium` или `high`. Это классификация вредоносности, а не степень уверенности классификатора или разрешение на доступ. Уровень `safe` отражается в аннотациях; настроить его блокировку нельзя. См. [уровни классификации](https://learn.microsoft.com/ru-ru/azure/foundry-classic/foundry-models/concepts/content-filter).

При [уровне блокировки (blocking level) `Medium`, установленном по умолчанию](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/default-safety-policies), фильтры блокируют уровни `medium` и `high` и на входе, и на выходе. Классификаторы могут ошибаться в обе стороны: блокировать допустимое содержимое и пропускать то, которое следовало бы скрыть.

[Prompt Shields](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-filter-prompt-shields) обнаруживает попытки изменить поведение модели. Прямая атака через промпт (direct prompt attack) приходит в пользовательском запросе. Косвенная атака через промпт (indirect prompt attack) находится в содержимом документа: например, в найденном фрагменте ассистенту предлагают игнорировать вопрос пользователя. Обнаружение атак в пользовательских запросах включено по умолчанию; обнаружение атак в документах по умолчанию выключено, его нужно включить отдельно. В результатах различай `detected` и `filtered`: обнаружение атаки и фактическая блокировка — разные события.

Приложение должно обозначить найденные фрагменты с помощью [разделителей и экранирования JSON, предусмотренных сервисом](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/how-to-create-guardrails#embedding-documents-in-your-prompt). Ниже показан фрагмент сообщения для иллюстрации формата; выполнить его как самостоятельный запрос нельзя. Сначала экранируй кавычки внутри документа, затем сериализуй сообщение в JSON:

```json
{
  "role": "user",
  "content": "When does it open? \"\"\" <documents>\nHours: \\\"09:00\\\".\n</documents> \"\"\""
}
```

Форматирование входит в контракт интеграции. Если просто склеить результаты Search и включить детектор в политике, это ещё не доказывает, что сервис проверяет их как документы.

Прежде чем реализовывать P1, выбери версию API для вызовов модели. Этот API относится к плоскости данных (data plane). Сверь выбранную версию с [матрицей совместимости аннотаций](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/how-to-create-guardrails#api-version-compatibility) и проверь, какие аннотации она поддерживает: аннотации косвенных атак зависят от версии. Версия ARM `2025-06-01` в упражнении относится к чтению конфигурации через плоскость управления (control plane); по ней нельзя судить о поддержке аннотаций при генерации.

## Как выбрать проверки и пороги \{#choosing-and-tradeoffs}

У каждой проверки свой вопрос. Классификатор вредоносного содержимого не установит, подтверждает ли цитата ответ. А ответ, подтверждённый источником, всё равно может требовать блокировки.

| Проверка | Что проверяет | Когда полезна | Чего не обеспечивает |
|---|---|---|---|
| Базовые фильтры содержимого | Категорию вредоносного содержимого и уровень серьёзности на входе и выходе | Когда для вызовов нужна общая политика допустимого содержимого | Права на документы, корректность цитат и допустимые для приложения темы |
| Prompt Shields | Попытки подменить инструкции в промптах и документах | Когда P1 читает внешний текст | Авторизацию доступа к данным и защиту от каждой возможной атаки |
| Groundedness detection (проверка того, подтверждают ли источники ответ), preview | Подтверждаются ли утверждения предоставленными источниками | В ответах на вопросы и кратких изложениях, которые должны опираться на источники | Истинность и актуальность самих источников |
| Обнаружение защищённого материала (protected-material detection) | Совпадения выходного текста с известными защищёнными текстами и кодом | Чтобы уменьшить риск воспроизведения материалов, вошедших в индекс детектора | Полную проверку всего загружаемого и выдаваемого содержимого |

Названия уровней в портале и схеме ARM легко перепутать. В [портале уровень блокировки](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/guardrails-overview#blocking-levels) обозначает строгость: `Low` блокирует только `high`, `Medium` — `medium` и `high`, а `High` — `low`, `medium` и `high`. В [схеме политики ARM](https://learn.microsoft.com/ru-ru/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01) параметр `severityThreshold` задаёт порог серьёзности (severity threshold), начиная с которого содержимое блокируется. Порог `Low` делает фильтрацию строже. Записывай конкретные блокируемые уровни: переносить метку `Low` из одного интерфейса в другой без проверки нельзя. Для отключения базовой фильтрации выходных данных требуется разрешение на изменение ограничителей.

Для P1 начни с настроек по умолчанию и проверь их на характерных вопросах и фрагментах документов, прежде чем что-либо менять. Учебный документ может обоснованно затрагивать чувствительную тему. Если он блокируется, сначала выясни категорию, этап проверки и настроенный порог. Если ради одного ложного срабатывания изменить все категории сразу, будет трудно оценить последствия.

Функция groundedness detection для развёртываний [имеет статус preview](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/guardrails-overview#risk-applicability), а текущая [инструкция по настройке](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/how-to-create-guardrails#annotations) ограничивает её потоковыми сценариями. В первой версии P1 ответ не передаётся потоком, поэтому рассчитывать на эту проверку в ней нельзя. Кроме того, [сопоставление ответа с источником](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-filter-groundedness) не устанавливает актуальность: устаревший документ может подтвердить устаревший ответ. Поиск и цитирование оценивай отдельно.

[Обнаружение защищённого материала](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-filter-protected-material) ищет совпадения с известными текстами и кодом и поддерживает только английский язык. Согласно документации, индекс кода отражает состояние на 6 апреля 2023 года. Даже при включённой проверке P1 должен сохранять сведения о происхождении источников и соблюдать правила приёма документов. В [примечаниях к выпускам Content Safety](https://learn.microsoft.com/ru-ru/azure/ai-services/content-safety/whats-new) для отдельных API указаны следующие статусы: Prompt Shields и API обнаружения защищённого текста — GA, а API обнаружения защищённого кода — preview. Проверки в развёртывании и отдельные API различаются; статус одного не определяет статус другого.

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

P1 — минимальное API: оно получает из Azure AI Search фрагменты документов из открытых источников и просит развёртывание чата Foundry составить ответ с цитатами. В таких документах тоже могут быть враждебные инструкции. Общие меры защиты разбирает урок [Guardrails](/rag-agents/part-1-rag/cross-cutting/guardrails/). Здесь задача — правильно обработать результат проверок в развёртывании. За удостоверения, права на поиск, работу с секретами и разрешения на вызов инструментов отвечают приложение и инфраструктура.

Первая реализация использует Chat Completions без потоковой передачи и накапливает ответ до отправки клиенту. При блокировке промпта сервис возвращает HTTP 400 со структурированной ошибкой `content_filter`. При блокировке сгенерированного ответа возможен HTTP 200 с `finish_reason: content_filter`, в том числе с частичным текстом. См. [варианты результатов фильтрации](https://learn.microsoft.com/ru-ru/azure/foundry-classic/foundry-models/concepts/content-filter#content-filtering-scenarios). Если сама проверка не завершилась, сервис может вернуть HTTP 200 с [`content_filter_results.error`](https://learn.microsoft.com/ru-ru/azure/foundry-classic/foundry-models/concepts/content-filter#scenario-6-content-filtering-system-unavailable), например `content_filter_error`. До выдачи текста и цитат проверь и признаки блокировки, и ошибки выполнения фильтра. Этот формат относится к указанному API; для другого API модели его нужно проверять отдельно.

Для P1 предлагается следующий контракт на основе [ASP.NET Core ProblemDetails](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0). Обработчик ещё не реализован; это ответы, которые должно сформировать приложение:

| Результат от поставщика модели | Ответ P1 до отправки HTTP-заголовков |
|---|---|
| HTTP 400 со структурированным кодом `content_filter` | HTTP 422, `application/problem+json`; ответ модели не выдаётся |
| HTTP 200, у выбранного варианта ответа `finish_reason` равен `content_filter` | Тот же HTTP 422; частичный ответ и цитаты отбрасываются |
| HTTP 200 с `content_filter_results.error`, в том числе `content_filter_error` | HTTP 503, `application/problem+json`, `code: safety_unavailable`; ответ и цитаты не выдаются |
| Другой HTTP 400 | Отдельная обработка ошибки поставщика модели; не всякий некорректный запрос означает блокировку |

Для обоих случаев блокировки задай `status = 422`, поле `title` — `Answer blocked by safety policy`, поле `detail` — `The model request or response was blocked by the configured safety policy.`, а расширение `code` — `safety_filtered`. Добавь `traceId`, чтобы можно было найти запрос при обращении в поддержку. Сообщение не обвиняет пользователя: причиной мог стать найденный фрагмент или сгенерированный ответ. Клиент может предложить переформулировать вопрос, но не должен показывать скрытый текст.

Если фильтр не смог выполнить проверку, P1 также не выдаёт ответ. Для этого случая задай `status = 503`, поле `title` — `Safety check unavailable`, поле `detail` — `The answer was withheld because the safety check could not complete.`, расширение `code` — `safety_unavailable` и добавь `traceId`. Это выбор P1 при недоступности проверки; Azure не предписывает приложению этот HTTP-статус. Сбой проверки сам по себе не означает, что политика заблокировала содержимое.

Не повторяй автоматически ту же заблокированную генерацию и не перенаправляй её в развёртывание с менее строгими правилами. В Application Insights записывай имя развёртывания, имя политики, этап проверки и категорию, если эти сведения доступны. Связывай записи с трейсом (trace) запроса. Сбой выполнения фильтра отмечай как `safety_unavailable` и сохраняй код ошибки поставщика; такие записи должны отличаться от блокировок с `safety_filtered`. В обычные журналы не должны попадать исходные вопросы, найденные фрагменты и скрытые ответы. По телеметрии нужно различать эти исходы, успешный ответ и поиск без результатов.

При использовании [Asynchronous Filter](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-streaming) токены могут прийти раньше, чем результат фильтрации. Если API уже отправило заголовки и текст, заменить ответ HTTP-ошибкой в формате ProblemDetails нельзя. Для потоковой версии нужны отдельное завершающее событие и правила клиента для неполного или отозванного текста. Пока этот контракт не спроектирован, оставь в P1 накопление ответа перед отправкой. Механика описана в уроке [Serving](/rag-agents/part-3-production/serving/).

## Попробуй \{#try-it}

Проверь, какой фильтр привязан к развёртыванию чата P1 из [предыдущего урока](./deployments-quotas-cost.md#try-it). Нужны Azure CLI, подписка с этим развёртыванием и права чтения ресурса Foundry, развёртывания и политики. В этом упражнении настройки не меняются.

Команды сверены с актуальной справкой Azure CLI 17.10.2026, но не запускались в реальной подписке: у курса пока нет подписки для такой проверки. Ожидаемые результаты основаны на документации API управления.

В Bash замени первые три значения своими, затем выполни [`az login`](https://learn.microsoft.com/ru-ru/cli/azure/reference-index#az-login) и [`az account set`](https://learn.microsoft.com/ru-ru/cli/azure/account#az-account-set):

```bash
P1_SUBSCRIPTION='your-subscription-id'
P1_RESOURCE_GROUP='your-p1-resource-group'
P1_FOUNDRY='your-p1-foundry-resource'
P1_CHAT='p1-chat-lab'

az login
az account set --subscription "$P1_SUBSCRIPTION"
```

Прочитай развёртывание командой [`deployment show`](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-show). Сохрани `properties.raiPolicyName` в `P1_POLICY`, а `id` ресурса Foundry, полученный через [`az cognitiveservices account show`](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account#az-cognitiveservices-account-show), — в `P1_ACCOUNT_ID`. Если любая команда CLI завершится ошибкой, остановись: отсутствие вывода нельзя трактовать как настройку фильтрации.

```bash
az cognitiveservices account deployment show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_CHAT" --output json

P1_POLICY=$(az cognitiveservices account deployment show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_CHAT" \
  --query properties.raiPolicyName --output tsv)

P1_ACCOUNT_ID=$(az cognitiveservices account show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --query id --output tsv)
```

Команда чтения ресурса возвращает его идентификатор. Если имя политики и идентификатор непустые, выполни GET-запрос к политике RAI через [`az rest`](https://learn.microsoft.com/ru-ru/cli/azure/reference-index#az-rest). Используй стабильную версию `2025-06-01` [API чтения политики RAI](https://learn.microsoft.com/ru-ru/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01):

```bash
if [[ -n "$P1_POLICY" && -n "$P1_ACCOUNT_ID" ]]; then
  az rest --method get \
    --url "https://management.azure.com${P1_ACCOUNT_ID}/raiPolicies/${P1_POLICY}?api-version=2025-06-01" \
    --output json
fi
```

Ожидаемый результат — запись развёртывания и, если именованную политику удалось прочитать, её конфигурация. Проверь `basePolicyName`, `mode` и каждую запись `contentFilters`: `name`, `source`, `enabled`, `blocking` и, где он применим, `severityThreshold`.

Ниже приведена часть [примера из документации GET](https://learn.microsoft.com/ru-ru/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01). Это пример из документации, а не результат проверки P1 или рекомендация по настройке:

```json
[
  {"name": "Hate", "source": "Prompt", "enabled": false,
   "blocking": false, "severityThreshold": "High"},
  {"name": "Hate", "source": "Completion", "enabled": true,
   "blocking": true, "severityThreshold": "Medium"}
]
```

Поле `name` указывает детектор, `Prompt` — входные данные, `Completion` — выходные. В этом примере входной детектор выключен: значение `High` не означает, что он что-либо блокирует. Выходной детектор включён и настроен на блокировку уровней `medium` и `high`. Сначала читай `enabled` и `blocking`, затем порог. При `enabled: true` и `blocking: false` результат аннотируется без блокировки.

В [портале Foundry](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/how-to-create-guardrails#assign-a-guardrail) открой **Build → Models**, выбери модель P1 и проверь назначение в панели **Guardrails**. Затем в **Build → Guardrails** посмотри проверки именованного ограничителя и сопоставь `basePolicyName` с [документированными настройками по умолчанию](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/default-safety-policies). Ограничители по умолчанию доступны только для чтения. Если не хватает прав, ответ API управления неполон или портал не показывает нужные сведения и действующие настройки подтвердить не удаётся, запиши `unresolved`. Пустое поле или неудачный GET не доказывает, что фильтрация выключена.

Запиши, какие уровни действительно блокируются на входе и выходе, включено ли обнаружение атак в документах и как настроено обнаружение защищённого материала. Сохрани имя политики рядом с конфигурацией развёртывания P1, чтобы позже перенести этот выбор в Bicep. Такая проверка устанавливает конфигурацию; точность детекторов она не измеряет.

Зафиксируй четыре сценария для приёмочных проверок API P1: блокировка входных данных; блокировка выходных данных; HTTP 200 с `content_filter_results.error`, например `content_filter_error`, даже при обычном значении причины завершения; и другой HTTP 400 от поставщика модели. Только первые два должны приводить к `safety_filtered`. Третий должен давать HTTP 503 с `safety_unavailable`; во всех первых трёх случаях ответ и цитаты не выдаются. Четвёртый проходит отдельную обработку ошибки поставщика.

**Стоимость:** упражнение сводится к чтению конфигурации через плоскость управления и не создаёт ресурсов. Вызовов модели и анализа безопасности здесь нет, поэтому дополнительная плата за них не возникает. Уже работающие ресурсы P1 продолжают тарифицироваться по своим условиям.

**Удаление ресурсов:** этот шаг не создаёт ресурсы Azure и не меняет политику, поэтому удалять после него нечего. Оставь развёртывание для следующего упражнения P1 либо, если заканчиваешь практическую работу, выполни удаление из урока, в котором оно создавалось.

## Что перенести в свою практику \{#what-to-take-away}

- Проверяй, какая политика привязана к развёртыванию чата: по одной лишь сохранённой политике нельзя определить, какие проверки к нему применяются.
- Записывай конкретные блокируемые уровни серьёзности. Уровень блокировки в портале и порог в ARM меняют строгость в противоположных направлениях.
- Обнаружение атак в документах нужно включить и правильно встроить в приложение. Считай найденный текст из открытых источников недоверенными входными данными.
- До отправки ответа различай блокировку входа, блокировку выхода и сбой выполнения фильтра; каждому исходу нужен определённый ответ приложения.
- Используй проверки платформы наряду с ограничителями приложения, проверкой источников и оценкой качества: они выявляют разные сбои.

**[Новые термины](../glossary.md#platform-safety)**: фильтр содержимого, уровень серьёзности, порог серьёзности, уровень блокировки, аннотация, Prompt Shields, прямая атака через промпт, косвенная атака через промпт, groundedness detection, обнаружение защищённого материала, политика RAI.

## Источники \{#sources}

Проверено на 17.10.2026.

Обработка сбоев проверки, совместимость API и примеры чтения конфигурации повторно проверены 18.10.2026.

- **Проверки и конфигурация:** [Guardrails overview](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/guardrails-overview), [Default safety policies](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/default-safety-policies), [Content filtering and response scenarios](https://learn.microsoft.com/ru-ru/azure/foundry-classic/foundry-models/concepts/content-filter) и [Configure guardrails and document formatting](https://learn.microsoft.com/ru-ru/azure/foundry/guardrails/how-to-create-guardrails).
- **Специализированные детекторы:** [Prompt Shields](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-filter-prompt-shields), [Groundedness detection](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-filter-groundedness), [Protected-material detection](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-filter-protected-material) и [Content Safety release notes](https://learn.microsoft.com/ru-ru/azure/ai-services/content-safety/whats-new).
- **Обработка ответов:** [Content streaming](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/content-streaming) и [ASP.NET Core API errors and ProblemDetails](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0).
- **Схема управления и CLI:** [Deployment schema, 2025-06-01](https://learn.microsoft.com/ru-ru/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts/deployments), [RAI policy GET, 2025-06-01](https://learn.microsoft.com/ru-ru/rest/api/microsoftfoundry/accountmanagement/rai-policies/get?view=rest-microsoftfoundry-accountmanagement-2025-06-01), [Deployment show](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-show), [Account show](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account#az-cognitiveservices-account-show), [Login and REST](https://learn.microsoft.com/ru-ru/cli/azure/reference-index) и [Select subscription](https://learn.microsoft.com/ru-ru/cli/azure/account#az-account-set).
