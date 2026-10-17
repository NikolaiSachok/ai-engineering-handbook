---
title: Развёртывания моделей, квоты и стоимость
sidebar_position: 2
last_verified: 2026-10-17
---

# Развёртывание модели определяет допустимую нагрузку, место обработки данных и расходы

В песочнице вызов модели может проходить успешно, но при одновременной работе нескольких пользователей приложение получает отказы. Длинные промпты быстрее расходуют доступный лимит, чем короткие вопросы, а повторные попытки увеличивают поток запросов именно тогда, когда сервис уже начинает их отклонять. Даже если конечная точка работает, а ресурс создан в нужной стране, это не означает, что модель обрабатывает промпты в этой стране.

Тебе нужно выбрать, где разрешена обработка запросов, сколько запросов сможет отправлять приложение и придётся ли платить за простой. Для небольшого RAG-сервиса эти решения должны быть явно записаны в конфигурации, а их изменение не должно обходиться дорого. При отказе запроса должно быть видно, какое ограничение сработало. Если купить пропускную способность до замеров рабочей нагрузки, можно платить за мощность, которая почти не используется.

## Как это устроено в Azure \{#how-it-works-on-azure}

В Microsoft Foundry **[развёртывание модели (model deployment)](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/how-to/create-model-deployments)** связывает модель и её версию с именем развёртывания, типом и настройкой мощности. Приложение обращается по имени развёртывания. Для P1 подойдут имена `p1-chat-lab` и `p1-embed-lab`: они отделяют конфигурацию приложения от идентификаторов моделей. Записывай и версии моделей, чтобы по конфигурации можно было установить, какая версия отвечала на вопрос.

Здесь нужно различать три величины:

- **Квота (quota)** — объём, который подписке разрешено распределить в пределах области действия квоты (quota scope).
- **Лимит частоты (rate limit)** развёртывания — ограничение того, как быстро можно использовать выделенный объём.
- **Зарезервированная пропускная способность (provisioned throughput)** — выделенная вычислительная мощность для обработки запросов.

Большая квота сама по себе не означает, что ты покупаешь вычислительную мощность, и не гарантирует фиксированное время выполнения каждого запроса.

В Azure OpenAI [управление квотами](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/quota) опирается на **TPM (tokens per minute, токены в минуту)** и **RPM (requests per minute, запросы в минуту)**. При выделении TPM устанавливается и RPM; соотношение зависит от модели. Для проверки лимита сервис заранее оценивает объём промпта и запрошенный максимум ответа. Этот расчёт отличается от подсчёта токенов после обработки, по которому выставляется счёт. Поэтому завышенный максимум ответа может сократить число допускаемых запросов, даже если фактические ответы короткие. При всплеске запросов сервис может отклонить их по результатам проверки за короткий интервал, хотя лимит за полную минуту ещё не исчерпан.

Прежде чем планировать ещё одно развёртывание, проверь область действия квоты. Foundry [переводит модели на общие пулы квоты на уровне подписки](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/quotas-limits). Переход начался после 7 мая 2026 года с Realtime Translate и Realtime Transcribe; в руководстве сказано, что вскоре к ним присоединятся все модели. Для моделей и версий, которые уже переведены на новую схему, пул квоты у развёртываний Global Standard общий для всех регионов, а у Data Zone Standard — для регионов внутри каждой зоны. У остальных моделей сохраняются региональные пулы. Проверь столбец **Scope** на странице **Quota** портала: он показывает, какая схема действует. Дополнительный ресурс не обязательно добавляет квоту. При планировании используй [актуальные таблицы квот моделей](https://learn.microsoft.com/ru-ru/azure/foundry/openai/quotas-limits) и доступный объём своей подписки, а не скопированные значения по умолчанию.

## Как выбрать тип развёртывания \{#choosing-and-tradeoffs}

Сначала выбери **тип развёртывания (deployment type)** с нужными границами обработки данных, затем определи характер рабочей нагрузки и способ оплаты. Развёртывания семейства Standard используют общую вычислительную мощность: Global Standard направляет запросы в доступные центры обработки данных, а Data Zone Standard ограничивает маршрутизацию своей зоной. В таблице приведены варианты, определённые в [каталоге типов развёртывания](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/deployment-types); их доступность зависит и от модели, и от её версии.

| Вариант | Где обрабатываются запросы | Оплата и подходящая рабочая нагрузка | Когда не подходит |
|---|---|---|---|
| Standard (`Standard`) | В указанной географической области Azure | За токены; интерактивные запросы, которым нужна эта граница | Если задержка не подходит по результатам замеров или нужен новый вариант развёртывания модели с обработкой в географической области: такой вариант появляется последним, без гарантированной даты |
| Global Standard (`GlobalStandard`) | В регионах Azure по всему миру, где развёрнута модель | За токены; начальная переменная рабочая нагрузка P1 | Если требования запрещают глобальную маршрутизацию |
| Data Zone Standard (`DataZoneStandard`) | В зоне данных (data zone), которую определяет Microsoft | За токены; интерактивные запросы с обработкой в пределах зоны | Если нужна более узкая граница или модель не поддерживается в этой зоне |
| Provisioned (`GlobalProvisionedManaged`, `DataZoneProvisionedManaged`, `ProvisionedManaged`) | Глобально, в зоне данных или в географической области — в зависимости от типа | За выделенные PTU; стабильная рабочая нагрузка, которую уже измерили | Если загрузка мала или ещё неизвестна: простаивающая мощность тоже оплачивается |
| Batch (`GlobalBatch`, `DataZoneBatch`) | Глобально или в выбранной зоне, если она поддерживается | По пакетным тарифам на токены; асинхронная работа | Если пользователь ждёт интерактивного ответа |

В каталоге есть и `DeveloperTier`, но в таблицу он не включён: этот тип предназначен только для оценки дообученных моделей, не имеет SLA и не даёт гарантий размещения данных.

В таблице указано, где выполняется инференс (inference). [Хранимые данные остаются в указанной географической области Azure (Azure geography)](https://learn.microsoft.com/ru-ru/azure/foundry/responsible-ai/openai/data-privacy), но у типов Global обработка может происходить за её пределами. Для развёртываний, не относящихся к типам Global и Data Zone, то же руководство по конфиденциальности допускает обработку между регионами одной географической области. Поэтому название Standard не гарантирует обработку в одном регионе. Зону данных определяет Microsoft: это не зона доступности и не страна, которую выбирает приложение. Сопоставляй действующие границы с конкретными требованиями к данным.

В P1 начни с Global Standard для работы с документами из открытых источников, если вопросы пользователей и другое отправляемое содержимое не требуют определённого размещения данных. Открытость исходных документов не делает пользовательские промпты открытыми. Если нужна и поддерживается граница Data Zone, выбери Data Zone Standard и для чата, и для эмбеддингов (embeddings). Если сменишь тип только для чата, текст для эмбеддингов по-прежнему будет обрабатываться в прежних границах.

**PTU (provisioned throughput unit)** — единица зарезервированной вычислительной мощности для модели. [Пропускная способность в PTU](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/provisioned-throughput) не сводится к универсальному количеству токенов: результат зависит от модели и рабочей нагрузки — объёма входных данных и длины ответа. До выбора мощности измерь частоту запросов, длину промптов и ответов, а также число одновременных запросов. Квота PTU разрешает создать развёртывание, но не гарантирует, что для него найдётся свободная мощность.

За каждую развёрнутую PTU начисляется почасовая плата, в том числе во время простоя. **[Azure Reservation](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/provisioned-throughput-billing)** — финансовое обязательство, по которому предоставляется скидка на использование зарезервированной пропускной способности, если оно подпадает под условия обязательства. Покупка Azure Reservation не обеспечивает наличие мощности для развёртывания. Жизненные циклы развёртывания и Azure Reservation независимы: удаление развёртывания прекращает почасовые начисления за него, но не отменяет Azure Reservation. Поэтому для небольшого учебного бюджета курса зарезервированная пропускная способность — неудачный вариант по умолчанию.

При оплате за токены отдельно сравнивай [тарифы на входные токены, кэшированные входные токены (если такой тариф применяется), выходные токены и эмбеддинги](https://azure.microsoft.com/en-us/pricing/details/azure-openai/). Для оценки расходов умножь объём каждой категории на её тариф, сложи результаты и добавь стоимость остальных сервисов. Для каждого вызова учитывай весь отправляемый контекст, включая найденные фрагменты и историю разговора, которые передаёшь модели, а не только новый вопрос пользователя. Малый TPM замедляет расходование лимита, но при многократных вызовах за месяц всё равно может накопиться заметный счёт.

**Пакетное развёртывание (batch deployment)** принимает группы запросов через файлы в режиме [Batch](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/batch). Для токенов в очереди действует отдельная квота (enqueued-token quota). Целевой срок обработки — 24 часа, но завершение за это время не гарантируется. Batch может подойти для оценки качества вне интерактивной работы, если допустима задержка и поддерживается нужное сочетание модели и API. Он не заменяет развёртывание, которое отвечает пользователям P1. В [таблицах квот Batch](https://learn.microsoft.com/ru-ru/azure/foundry/openai/quotas-limits#batch-quota) для Azure for Students и бесплатных пробных подписок стоит N/A, поэтому не рассчитывай, что учебный кредит автоматически даёт доступ к Batch.

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

В P1 API на ASP.NET Core будет работать в Container Apps. При обработке вопроса сначала потребуется эмбеддинг для поиска, затем — вызов чата с найденными фрагментами. Как получать ответы с опорой на фрагменты и ссылками на источники, объясняет урок [«Generation — генерация ответа»](/rag-agents/part-1-rag/generation/). Выбор развёртываний задаёт лимиты каждого из этих этапов. Если загрузка документов и пользовательские вопросы используют одно развёртывание для эмбеддингов, ограничивай загрузку или запускай её по расписанию, чтобы оставлять достаточно квоты для ответов.

В API обрабатывай **HTTP 429 (Too Many Requests)** как сигнал нехватки доступной мощности. По [рекомендациям Azure о повторах](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/quota#understanding-rate-limits), если сервис вернул `retry-after-ms`, нужно выдержать указанную задержку; иначе — применять **экспоненциальную отсрочку (exponential backoff)** со случайным разбросом задержки. Ограничь число попыток: неуспешные запросы тоже учитываются в лимитах частоты, поэтому цикл немедленных повторов может продлить период отказов.

Прежде чем менять квоту, прочитай ошибку и [заголовки ответа с лимитами](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/quota#rate-limit-response-headers). Отслеживай `x-ratelimit-remaining-requests` и `x-ratelimit-remaining-tokens`. Если `x-ratelimit-limit-tokens` ниже настроенного TPM, сервис временно уменьшил фактический лимит из-за конкуренции за общую мощность; это сигнал о корректировке доступной мощности, а не о квоте, которую ты ещё не распределил.

Для каждого вопроса P1 задай предельное время выполнения (deadline). Настрой **допуск запросов (admission control)** перед вызовом модели и ограничь, сколько запрос может ждать своей очереди. Новая попытка допустима, только пока укладывается в общий срок. Если ожидание выйдет за этот срок, верни вызывающей стороне понятную временную ошибку. До добавления собственной логики повторов проверь политику выбранного SDK: вложенные политики могут многократно увеличить число попыток. Согласуй использование квоты между репликами API — семафор внутри одного процесса не ограничивает их суммарный поток запросов. Средства контроля общих лимитов для разных вызывающих сторон появятся в уроке III.8 «AI-шлюз» (запланирован).

Урок [«Serving — сервинг на FastAPI и Docker»](/rag-agents/part-3-production/serving/) объясняет, как на стороне приложения организовать повторы, ограничивать число одновременных запросов и обрабатывать таймауты и обрывы потоковых ответов. Если пользователь получил часть ответа, нельзя незаметно запускать генерацию заново. Для 429 до начала генерации и обрыва соединения посреди ответа нужны разные способы восстановления.

В Application Insights записывай отдельно каждую попытку вызова чата и расчёта эмбеддинга: имя развёртывания, длительность, статус, число повторов и сколько токенов израсходовано по данным сервиса. Урок [«Observability»](/rag-agents/part-1-rag/cross-cutting/observability/) поможет связать их в трассировку всего запроса. Сравнивай стоимость успешного ответа и время до его получения, включая ожидание между попытками. Даже дешёвые по отдельности вызовы при повторах могут сделать итоговый ответ дорогим и медленным.

## Попробуй \{#try-it}

Создай два развёртывания моделей для последующей работы P1. Нужны подписка, ресурс Foundry для P1 из урока III.1 «Microsoft Foundry» (запланирован) и право управлять развёртываниями. [Руководство по развёртыванию](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/how-to/create-model-deployments) указывает роль `Cognitive Services Contributor` или эквивалентные права. Для просмотра квот нужна роль [`Cognitive Services Usages Reader` в области подписки](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/quota#prerequisites) или эквивалентные права. Назначение на уровне группы ресурсов или отдельного ресурса не даёт доступа к Usages API. В этом упражнении не создаются Container Apps, Search и API.

Команды сверены с актуальной справкой Azure CLI на 17.10.2026. На действующей подписке они не запускались: для курса пока нет доступной подписки Azure. Ниже указаны ожидаемые по документации результаты, а не наблюдения после выполнения.

В Bash замени первые три значения своими. Выполни базовую команду [`az login`](https://learn.microsoft.com/ru-ru/cli/azure/reference-index#az-login), затем явно выбери подписку через [`az account set`](https://learn.microsoft.com/ru-ru/cli/azure/account#az-account-set):

```bash
P1_SUBSCRIPTION='your-subscription-id'
P1_RESOURCE_GROUP='your-p1-resource-group'
P1_FOUNDRY='your-p1-foundry-resource'
P1_CHAT='p1-chat-lab'
P1_EMBED='p1-embed-lab'
P1_SKU='GlobalStandard'

az login
az account set --subscription "$P1_SUBSCRIPTION"
```

Сначала узнай [расположение ресурса](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account#az-cognitiveservices-account-show) и [использование квот подписки для этого расположения](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/usage#az-cognitiveservices-usage-list). Затем посмотри [доступные ресурсу модели](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account#az-cognitiveservices-account-list-models) и [существующие развёртывания](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-list). Нужны свободные имена: если `p1-chat-lab` или `p1-embed-lab` уже занято другим развёртыванием, остановись.

```bash
P1_LOCATION=$(az cognitiveservices account show \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --query location --output tsv)

az cognitiveservices usage list -l "$P1_LOCATION" --output json

az cognitiveservices account list-models \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --query "[?name=='gpt-5-mini' || name=='text-embedding-3-small']" \
  --output json

az cognitiveservices account deployment list \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --output json
```

Используй `gpt-5-mini` версии `2025-08-07` и `text-embedding-3-small` версии `1`. Обе версии имеют статус [общей доступности (GA)](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/model-retirement-schedule) и [указаны для Global Standard и Data Zone Standard](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability). В полученных записях проверь обе версии, выбранный SKU, минимальную мощность и шаг её изменения. На странице **Quota** портала уточни область действия и доступную квоту для каждой модели.

Если требования к данным предполагают Data Zone, до создания любого из двух развёртываний задай `P1_SKU='DataZoneStandard'`. Сначала подтверди поддержку обеих моделей в зоне ресурса. [Зона данных определяется регионом ресурса](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/deployment-types#by-data-residency-requirement). Если нужное сочетание или квота недоступны, остановись.

Создай оба развёртывания базовой командой [`deployment create`](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-create). Для этих развёртываний с квотой в TPM параметр [`--sku-capacity 10` запрашивает 10 000 TPM на каждое развёртывание](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/automate-quota-deployments). Начальный объём намеренно мал; фактические лимиты проверь в созданных развёртываниях, включая RPM, вместо того чтобы выводить его из TPM.

```bash
az cognitiveservices account deployment create \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_CHAT" \
  --model-format OpenAI --model-name gpt-5-mini \
  --model-version 2025-08-07 \
  --sku-name "$P1_SKU" --sku-capacity 10

az cognitiveservices account deployment create \
  --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
  --deployment-name "$P1_EMBED" \
  --model-format OpenAI --model-name text-embedding-3-small \
  --model-version 1 \
  --sku-name "$P1_SKU" --sku-capacity 10
```

Проверь обе записи через [`deployment show`](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-show):

```bash
for P1_DEPLOYMENT in "$P1_CHAT" "$P1_EMBED"; do
  az cognitiveservices account deployment show \
    --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
    --deployment-name "$P1_DEPLOYMENT" --output json
done
```

Если создание прошло успешно, ожидаются две именованные записи с выбранными моделями, версиями, SKU и мощностью. Прежде чем записывать имена в конфигурацию чата и эмбеддингов P1, проверь состояние подготовки обоих развёртываний и указанные лимиты частоты. Это проверка плоскости управления (control plane); она не доказывает, что инференс работает. Когда появится API, отправь всплеск запросов при малом лимите и проверь:

- время ожидания ограничено;
- при исчерпании лимита возвращается понятная ошибка;
- части потокового ответа не дублируются.

В текущем упражнении вызовов моделей нет.

**Стоимость:** эти развёртывания базовых моделей семейства Standard используют [оплату инференса за токены](https://azure.microsoft.com/en-us/pricing/details/azure-openai/). Создание и просмотр без вызова модели не расходуют оплачиваемые токены инференса. Последующие вызовы из песочницы или API будут платными; остальные ресурсы P1 тарифицируются отдельно. До вызовов проверь актуальные цены для модели и типа развёртывания и соотнеси их с учебным бюджетом курса.

**Удаление ресурсов:** удали через [`deployment delete`](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-delete) только два развёртывания из этого упражнения. Их [выделенные TPM вернутся в квоту](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/quota#resource-deletion). Сохрани сам ресурс P1 и посторонние развёртывания.

```bash
for P1_DEPLOYMENT in "$P1_CHAT" "$P1_EMBED"; do
  az cognitiveservices account deployment delete \
    --name "$P1_FOUNDRY" --resource-group "$P1_RESOURCE_GROUP" \
    --deployment-name "$P1_DEPLOYMENT"
done
```

## Что перенести в свою практику \{#what-to-take-away}

- Явно выбирай, где разрешён инференс, и применяй это решение и к чату, и к эмбеддингам. Место хранения данных не определяет место их обработки.
- Проверяй область действия квоты и фактические TPM и RPM развёртываний. Ещё один регион или ресурс может использовать тот же доступный объём.
- Настрой допуск запросов с учётом всех реплик API: ограничивай, сколько запрос может ждать своей очереди, и число повторов. Соблюдай задержки перед повтором; когда истечёт срок выполнения, заданный для запроса вызывающей стороны, прекращай и ожидание, и повторные попытки.
- Для P1 начни с оплаты за токены. До перехода на PTU измерь характер рабочей нагрузки и загрузку мощности; учитывай, что у развёртывания с зарезервированной пропускной способностью и у финансового обязательства разные жизненные циклы.

**[Новые термины](../glossary.md#deployments-quotas-cost)**: развёртывание модели, тип развёртывания, квота, TPM, RPM, HTTP 429, экспоненциальная отсрочка, PTU, Azure Reservation, пакетное развёртывание.

## Источники \{#sources}

Проверено на 17.10.2026.

- **Развёртывания и размещение данных:** [Развёртывание моделей через Azure CLI и Bicep](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/how-to/create-model-deployments), [Типы развёртывания](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/deployment-types), [Данные, конфиденциальность и безопасность](https://learn.microsoft.com/ru-ru/azure/foundry/responsible-ai/openai/data-privacy), [Доступность моделей и регионов](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability), [График вывода моделей из эксплуатации](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/model-retirement-schedule).
- **Квоты и повторы:** [Управление квотой Azure OpenAI](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/quota), [Квоты Foundry Models и их область действия](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/quotas-limits), [Квоты и ограничения Azure OpenAI](https://learn.microsoft.com/ru-ru/azure/foundry/openai/quotas-limits), [Автоматизация развёртываний на основе квот](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/automate-quota-deployments).
- **Пропускная способность и стоимость:** [Зарезервированная пропускная способность](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/provisioned-throughput), [Тарификация зарезервированной пропускной способности](https://learn.microsoft.com/ru-ru/azure/foundry/openai/concepts/provisioned-throughput-billing), [Пакетная обработка](https://learn.microsoft.com/ru-ru/azure/foundry/openai/how-to/batch), [Цены Azure OpenAI](https://azure.microsoft.com/en-us/pricing/details/azure-openai/).
- **Справка CLI:** [Вход](https://learn.microsoft.com/ru-ru/cli/azure/reference-index#az-login), [Выбор подписки](https://learn.microsoft.com/ru-ru/cli/azure/account#az-account-set), [Доступные модели и сведения о ресурсе](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account), [Использование квот подписки](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/usage#az-cognitiveservices-usage-list), [Создание, список, просмотр и удаление развёртываний](https://learn.microsoft.com/ru-ru/cli/azure/cognitiveservices/account/deployment).
