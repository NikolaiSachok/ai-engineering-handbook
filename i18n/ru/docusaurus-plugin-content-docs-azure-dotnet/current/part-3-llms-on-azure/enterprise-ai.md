---
title: AI для корпоративной среды
sidebar_position: 9
last_verified: 2026-10-17
---

# Частное подключение к модели — лишь часть защиты

Сервис ответов на вопросы может обращаться к модели по защищённому соединению, пока документы, индекс или журналы доступны по другому пути. Код приложения использует токены, а забытый скрипт по-прежнему работает с общим ключом. Даже точные ссылки в ответах ничего не говорят о том, все ли пути доступа проверены.

Проследи весь жизненный цикл запроса и документа: откуда можно подключиться, каким удостоверениям разрешён доступ, где обрабатываются данные и какие копии остаются после обработки. Эти решения затрагивают и API, которое отвечает на вопросы, и приём документов, и развёртывание, и сопровождение. В проде нужно обновлять корпус, разбирать неудачные запросы и восстанавливать работу сервиса.

## Как это устроено в Azure \{#how-it-works-on-azure}

Механизмы из уроков о [сетях](../part-1-azure-foundations/networking.md) и [RBAC и доступе без ключей](../part-1-azure-foundations/rbac-and-keyless-access.md) нужно применить к каждому соединению RAG-сервиса P1. Для [изоляции входящих подключений к Microsoft Foundry](https://learn.microsoft.com/ru-ru/azure/foundry/how-to/configure-private-link) создай частную конечную точку (private endpoint), одобри подключение, настрой разрешение имени в частный адрес из сети вызывающей стороны и отключи публичный сетевой доступ. Создание конечной точки добавляет частный маршрут, но публичный маршрут остаётся, пока ты не отключишь его отдельно. Так же проверь [Azure AI Search](https://learn.microsoft.com/ru-ru/azure/search/service-create-private-endpoint), Blob Storage и Key Vault.

Оставь в конфигурации клиента имя сервиса. В среде, откуда приложение обращается к сервису, это имя должно разрешаться через DNS в адрес частной конечной точки. Для Foundry могут понадобиться `privatelink.openai.azure.com` и `privatelink.services.ai.azure.com`, для Search — `privatelink.search.windows.net`. Настрой [частные зоны DNS (private DNS zones) для всех используемых суффиксов](https://learn.microsoft.com/ru-ru/azure/private-link/private-endpoint-dns). Проверка DNS на ноутбуке разработчика мало говорит о том, как разрешается имя в сети API.

Частная конечная точка обслуживает входящие подключения к сервису. Если позднее агент будет работать в Foundry, для его обращений к инструментам и данным понадобится [отдельно спроектировать исходящие подключения](https://learn.microsoft.com/ru-ru/azure/foundry/how-to/configure-private-link). Частная конечная точка модели не ограничивает внешние адреса, к которым обращается агент.

Для приложения с частными зависимостями выбирай [среду Azure Container Apps, подключённую к собственной VNet](https://learn.microsoft.com/ru-ru/azure/container-apps/networking). Сеть Azure, используемая по умолчанию, позволяет обращаться к конечным точкам, доступным из интернета. Тип сети среды нельзя изменить после её создания, поэтому этот выбор нужно сделать до переноса прототипа в прод. Доступ пользователей к API настраивается отдельно: частные подключения к зависимостям не требуют, чтобы само API было доступно только из внутренней сети.

[Доступ без ключей (keyless access)](https://learn.microsoft.com/ru-ru/azure/developer/ai/keyless-connections) означает токены Microsoft Entra ID и подходящие разрешения на операции с данными. В P1 приложение в Container Apps должно напрямую обращаться к Foundry, Search, Blob и Key Vault с токенами, полученными для его удостоверения. Если ключ модели хранится в Key Vault, соединение с моделью всё равно зависит от ключа. Key Vault полезен и для секретов, которые пока нельзя заменить доступом через удостоверение.

Ограничения аутентификации должен применять принимающий сервис. У Foundry для отключения локальной аутентификации (local authentication) есть [настройка `disableLocalAuth`](https://learn.microsoft.com/ru-ru/azure/ai-services/disable-local-auth): после распространения изменения сервис отклоняет аутентификацию по локальным ключам. У Search — [собственная настройка доступа только через роли](https://learn.microsoft.com/ru-ru/azure/search/search-security-enable-roles). Перед [запретом Shared Key в Storage](https://learn.microsoft.com/ru-ru/azure/storage/common/shared-key-authorization-prevent) проверь существующих клиентов и SAS. Изменение одного ресурса не меняет защиту остальных. Отдельно проверь удостоверения приложения и обработчика документов; не выдавай API права на запись, нужные обработчику, лишь ради успешной проверки.

## Как выбрать подход и учесть компромиссы \{#choosing-and-tradeoffs}

Начни с требований к данным и доступности сервиса извне. Для небольшого корпуса из открытых источников может подойти простая учебная среда. Для конфиденциальных документов могут потребоваться частные подключения к зависимостям, контроль исходящего трафика (egress) и частный сетевой доступ для специалистов сопровождения. Запиши требования до выбора инфраструктурного шаблона.

| Подход | Когда подходит | Где возникает проблема |
|---|---|---|
| Публичные конечные точки сервисов и аутентификация через Entra | Для обучения или когда требования допускают доступ через публичную сеть | Даже корректный RBAC не выполняет требование запретить публичный доступ к операциям с данными |
| Частные конечные точки, частные зоны DNS и отключённый публичный доступ | Когда к зависимостям можно обращаться только по одобренным частным соединениям | Если не предусмотрен сетевой доступ для сопровождения и приёма документов, обычное обслуживание приводит к недоступности сервиса |
| Индексаторы Search и общие частные каналы (shared private links) | Когда Search сам получает данные из поддерживаемой частной зависимости | Частная конечная точка для запросов к Search не даёт ему исходящего подключения; одобрение канала и настройка индексатора выполняются отдельно |
| Эталонная реализация целевой зоны (landing zone) | Когда несколько команд используют общие средства подключения, правила управления платформой и эксплуатационные процессы | Полный набор инфраструктуры для небольшого упражнения добавляет лишние ресурсы и обязанности |

Общий частный канал — исходящее соединение, которым управляет Search. Он настраивается независимо от конечной точки, через которую клиенты отправляют поисковые запросы. Если используешь индексатор или встроенную векторизацию, проверь [поддерживаемые зависимости и требования к выбранной рабочей нагрузке](https://learn.microsoft.com/ru-ru/azure/search/search-indexer-howto-access-private). Для индексатора нужно [задать `parameters.configuration.executionEnvironment` значение `"private"`](https://learn.microsoft.com/ru-ru/azure/search/search-indexer-howto-access-private#4---configure-the-indexer-to-run-in-the-private-environment): среда обработки, общая для нескольких клиентов, не может использовать подключения к частным конечным точкам. Поэтому загрузка документов может не работать даже после одобрения канала.

Если приложение само отправляет подготовленные документы в Search, путь приёма данных будет другим — проверь именно тот путь, который используешь. Согласно [руководству по частным конечным точкам Search](https://learn.microsoft.com/ru-ru/azure/search/service-create-private-endpoint), нужен уровень Basic или выше; Free не подходит. У Private Link отдельно оплачиваются [часы работы конечной точки и обработка данных](https://azure.microsoft.com/en-us/pricing/details/private-link/). Переход от публичной учебной среды к частным подключениям нужно заранее учесть в учебном бюджете.

Частная сеть не определяет обязательства по размещению данных (data residency). При выборе бессерверного развёртывания (serverless deployment) Foundry проверь [допустимые места обработки](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/deployment-types).

Географические границы обработки (processing boundary) задаются типом развёртывания. Global допускает обработку в разных географических областях. Data Zone ограничивает её зоной, определённой Microsoft. Standard и Regional Provisioned — указанной географической областью Azure (Azure geography), в которой обработка может идти в разных регионах. Доступные варианты зависят от модели. Ни регион ресурса, ни частный IP назначения не доказывают, что инференс выполняется в том же регионе. Проверь разрешённую географию обработки до выбора развёртывания и резервной площадки на случай сбоя.

Для перечисленных типов развёртывания хранимые данные остаются в назначенной географической области Azure. Расположение данных Search, Blob и телеметрии нужно проверить отдельно: развёртывание модели их никуда не переносит.

Для моделей категории [Models sold by Azure, включая Azure OpenAI](https://learn.microsoft.com/ru-ru/azure/foundry/responsible-ai/openai/data-privacy) Microsoft заявляет, что промпты, ответы, эмбеддинги (embeddings) и обучающие данные недоступны поставщикам моделей и без разрешения или указания клиента не используются для обучения базовых моделей. Это не обещание ничего не сохранять: функции с сохранением состояния хранят содержимое, а мониторинг злоупотреблений (abuse monitoring) может отбирать его для проверки человеком. Для изменённого режима мониторинга требуется одобрение; для функций на стадии предварительного тестирования порядок работы с данными может отличаться. [Для инструментов агентов могут действовать отдельные условия](https://learn.microsoft.com/ru-ru/azure/foundry/responsible-ai/agents/data-privacy-security). Зафиксируй, на каких условиях предоставляется выбранная модель, какие функции используются и как хранятся данные, чтобы не переносить обязательства по одной модели на все подключённые инструменты.

В [рекомендациях Microsoft по AI-архитектуре](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ai/platform/architectures) есть целевая зона для AI-рабочих нагрузок и эталонная реализация. Используй их, чтобы определить, по каким вопросам решения ещё не приняты. В [архитектуре чата Foundry в целевой зоне](https://learn.microsoft.com/ru-ru/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-landing-zone) за эксплуатацию приложения отвечает его команда, а платформенная команда — за общие подключения, DNS и правила управления платформой. Приложение в этом примере размещено в App Service. Для P1 полезно такое распределение обязанностей, но пример не служит инструкцией по развёртыванию в Container Apps. Прежде чем подключать общую инфраструктуру, определи, кто меняет DNS, согласует исключения для доступа и помогает при инцидентах.

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

В P1 минимальное API ASP.NET Core находит фрагменты (chunks) и отправляет их вместе с вопросом в развёртывание модели (model deployment) Foundry. Частное соединение с Search защищает путь передачи данных. Какие фрагменты разрешено видеть пользователю, нужно определять при [проектировании поиска](/rag-agents/part-1-rag/retrieval/). Документы из открытых источников упрощают первое упражнение. Если заменишь их внутренними документами, в первую очередь изменятся требования к доступу, а уже затем — клиент модели.

Прежде чем считать P1 изолированным в частной сети, собери подтверждения для каждого пути:

| Путь | Что нужно подтвердить |
|---|---|
| Container Apps → Foundry, Search, Blob, Key Vault | DNS в среде самого приложения разрешает имена в частные адреса; конечные точки достижимы; подключения одобрены; публичный доступ отключён; нужные операции по токенам выполняются успешно |
| Приём документов → Blob, модель эмбеддингов, Search | Обработчик работает там, откуда доступны частные зависимости, имеет собственные разрешения на данные и завершает приём документов. Если данные получает Search, проверь также его исходящие каналы |
| GitHub Actions → развёртывание и операции с данными | Для развёртывания используется удостоверение через OIDC. Для операций с данными в частной сети отдельно подтверждён сетевой доступ из среды, где выполняется задание GitHub Actions |
| API → Application Insights | Явно выбран разрешённый публичный исходящий маршрут либо частный приём телеметрии; после ограничения исходящего трафика трейс (trace) получен в разрешённой системе сбора телеметрии. Настроены права на чтение и определено, попадают ли в телеметрию промпты, фрагменты и ответы |

[GitHub Actions OIDC](https://learn.microsoft.com/ru-ru/azure/developer/github/connect-from-azure-openid-connect) избавляет от хранимых учётных данных (credentials) для развёртывания, но не создаёт маршрут в VNet. Развёртывание через плоскость управления может пройти успешно, даже если задание, наполняющее индекс, не может подключиться к Search. До отключения публичного доступа составь список заданий, которые работают с данными.

Если телеметрия должна поступать по частному соединению, используй [руководство по Azure Monitor Private Link](https://learn.microsoft.com/ru-ru/azure/azure-monitor/fundamentals/private-link-security) и [проектированию Private Link Scope](https://learn.microsoft.com/ru-ru/azure/azure-monitor/fundamentals/private-link-design). У Azure Monitor для этого есть отдельный Azure Monitor Private Link Scope (AMPLS) со своей частной конечной точкой и настройками DNS. Включи этот путь в [проверку сети из части I](../part-1-azure-foundations/networking.md): конечные точки Foundry и Search не передают телеметрию Application Insights.

Журналы и трейсы создают дополнительные копии данных рабочей нагрузки. Что измерять, разбирается в уроке о [наблюдаемости](/rag-agents/part-1-rag/cross-cutting/observability/). Здесь проверь, какие данные при обработке запроса попадают в журналы и трейсы, кто может их прочитать и когда они удаляются. [Принцип наименьших привилегий](/ai-sdlc/part-4-platform/least-privilege-sandboxing/) относится и к тем, кто читает диагностические данные.

Запиши сетевые настройки и настройки аутентификации в Bicep проекта P1, чтобы проверенная конфигурация применялась при следующем развёртывании через `azd`.

## Попробуй \{#try-it}

Отключи локальную аутентификацию на ресурсе Foundry (Foundry resource) проекта P1. Если ресурсы после предыдущего упражнения уже удалены, сначала заново создай временную группу ресурсов и ресурс Foundry по [шагу создания](./microsoft-foundry.md#try-it) и [руководству Microsoft](https://learn.microsoft.com/ru-ru/azure/foundry/how-to/create-projects). Для этого упражнения нужны только они; остальные ресурсы P1 можно не восстанавливать.

Выполняй команды локально в Bash. Перед началом войди в Azure CLI под учётной записью с правами на чтение и изменение ресурса. До изменения убедись, что все существующие клиенты поддерживают Entra и имеют нужные разрешения: настройка затрагивает всех клиентов общего ресурса, включая скрипты приёма документов.

**Стоимость:** команды только читают и меняют настройки существующего ресурса. Они не создают инфраструктуру и не отправляют запросы на инференс, поэтому само упражнение бесплатно. Существующие ресурсы P1 продолжают оплачиваться по обычным правилам. Повторное создание ресурса Foundry — отдельный подготовительный шаг. Если ресурс пуст, модели не развёрнуты и функции не используются, плата за потребление не ожидается. При использовании [функции Foundry оплачиваются отдельно](https://azure.microsoft.com/en-us/pricing/details/microsoft-foundry/#faq). Частные конечные точки и инфраструктура целевой зоны в упражнении не развёртываются.

Команды [`az resource show`](https://learn.microsoft.com/ru-ru/cli/azure/resource?view=azure-cli-latest#az-resource-show) и [`az resource update`](https://learn.microsoft.com/ru-ru/cli/azure/resource?view=azure-cli-latest#az-resource-update) проверены по актуальному справочнику CLI. В реальной подписке они не запускались: подписки для такой проверки не было. Свойство определено в стабильном [API `2025-06-01`](https://learn.microsoft.com/ru-ru/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts).

Подставь идентификатор ресурса Foundry из P1 вместо значений-заглушек. Прочитай текущее состояние и сохрани его в заметках проекта. До изменения проверь, что идентификатор указывает на нужный ресурс, а `kind` равен `AIServices` — это [тип ресурса Foundry](https://learn.microsoft.com/ru-ru/azure/foundry/concepts/architecture).

```bash
P1_FOUNDRY_ID='/subscriptions/REPLACE-SUBSCRIPTION-ID/resourceGroups/REPLACE-RESOURCE-GROUP/providers/Microsoft.CognitiveServices/accounts/REPLACE-FOUNDRY-NAME'

az resource show --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --query '{id:id,kind:kind,disableLocalAuth:properties.disableLocalAuth,publicNetworkAccess:properties.publicNetworkAccess}' \
  --output json
```

Отключи локальную аутентификацию, затем прочитай значение свойства:

```bash
az resource update --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --set properties.disableLocalAuth=true --output none

az resource show --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --query properties.disableLocalAuth --output json
```

**Ожидаемый результат:** `true` — в конфигурации задано отключение локальной аутентификации. Это ещё не доказывает, что ключи уже отклоняются: Microsoft предупреждает, что [распространение настройки по шлюзам может занимать часы](https://learn.microsoft.com/ru-ru/azure/ai-services/disable-local-auth). Отключение подтверждено на практике, когда запрос к сервису с ранее действовавшим ключом возвращает HTTP 401. Когда P1 можно будет запустить, зафиксируй и этот отказ, и успешный вызов с токеном Entra, полученным для удостоверения работающего приложения. Не сохраняй значения ключей в заметках и журналах.

До следующего развёртывания добавь `disableLocalAuth: true` в `properties` соответствующего ресурса в Bicep проекта P1. По таблице выше запиши, что ещё нужно сделать для частных сетевых соединений: упражнение меняет аутентификацию, но не создаёт сетевую изоляцию.

**Удаление ресурсов:** эти команды не создают ресурсов. Если ресурс Foundry был повторно создан только для упражнения, после чтения результата удали выделенную группу по [инструкции из предыдущего упражнения](./microsoft-foundry.md#try-it) и выполни [окончательное удаление ресурса (purge)](https://learn.microsoft.com/ru-ru/azure/ai-services/recover-purge-resources). На существующем ресурсе P1 оставь локальную аутентификацию отключённой.

Если несовместимому клиенту нужно восстановить доступ и до упражнения локальная аутентификация была включена, можно временно вернуть прежнюю настройку. Затем исправь клиент и повтори упражнение:

```bash
az resource update --ids "$P1_FOUNDRY_ID" --api-version 2025-06-01 \
  --set properties.disableLocalAuth=false --output none
```

Повторное включение ключей тоже требует времени на распространение настройки.

## Что перенести в свою практику \{#what-to-take-away}

- Проверяй отдельно пути API, приёма документов, сопровождения, заданий развёртывания и телеметрии.
- Для частного доступа к зависимости нужны вместе частная конечная точка, сетевой маршрут от вызывающей стороны, работающий DNS и отключённый публичный доступ.
- Использование токенов в приложении не запрещает ключи на стороне сервиса. Отключай аутентификацию по ключам на каждом принимающем сервисе и проверяй, что он их отклоняет.
- Проверяй географические границы обработки моделью и обязательства по хранению данных отдельно от сетевой изоляции и расположения ресурса.
- Используй эталонные архитектуры целевых зон, чтобы распределить обязанности и найти недостающие меры защиты до подключения инфраструктуры.

**[Новые термины](../glossary.md#enterprise-ai)**: общий частный канал, локальная аутентификация, размещение данных, географические границы обработки, мониторинг злоупотреблений.

## Источники \{#sources}

Проверено на 17.10.2026.

- **Сетевые пути:** [Foundry network isolation](https://learn.microsoft.com/ru-ru/azure/foundry/how-to/configure-private-link), [private endpoint DNS](https://learn.microsoft.com/ru-ru/azure/private-link/private-endpoint-dns), [Search private endpoints](https://learn.microsoft.com/ru-ru/azure/search/service-create-private-endpoint), [Search shared private links](https://learn.microsoft.com/ru-ru/azure/search/search-indexer-howto-access-private), [Container Apps networking](https://learn.microsoft.com/ru-ru/azure/container-apps/networking), [Private Link pricing](https://azure.microsoft.com/en-us/pricing/details/private-link/), [Azure Monitor Private Link](https://learn.microsoft.com/ru-ru/azure/azure-monitor/fundamentals/private-link-security) и [Azure Monitor Private Link Scope design](https://learn.microsoft.com/ru-ru/azure/azure-monitor/fundamentals/private-link-design).
- **Удостоверения и применение ограничений:** [Keyless connections](https://learn.microsoft.com/ru-ru/azure/developer/ai/keyless-connections), [disable Foundry local authentication](https://learn.microsoft.com/ru-ru/azure/ai-services/disable-local-auth), [Search RBAC configuration](https://learn.microsoft.com/ru-ru/azure/search/search-security-enable-roles), [prevent Storage Shared Key authorisation](https://learn.microsoft.com/ru-ru/azure/storage/common/shared-key-authorization-prevent) и [GitHub Actions OIDC](https://learn.microsoft.com/ru-ru/azure/developer/github/connect-from-azure-openid-connect).
- **Работа с данными:** [Model deployment types](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/deployment-types), [Models sold by Azure privacy statement](https://learn.microsoft.com/ru-ru/azure/foundry/responsible-ai/openai/data-privacy) и [Agent Service privacy statement](https://learn.microsoft.com/ru-ru/azure/foundry/responsible-ai/agents/data-privacy-security).
- **Архитектура:** [Foundry resource model](https://learn.microsoft.com/ru-ru/azure/foundry/concepts/architecture), [AI platform architecture guidance and landing-zone reference](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ai/platform/architectures) и [Foundry chat in an Azure landing zone](https://learn.microsoft.com/ru-ru/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-landing-zone).
- **Справка к упражнению:** [Account API `2025-06-01`](https://learn.microsoft.com/ru-ru/azure/templates/microsoft.cognitiveservices/2025-06-01/accounts), [Azure CLI resource commands](https://learn.microsoft.com/ru-ru/cli/azure/resource?view=azure-cli-latest), [Foundry account creation](https://learn.microsoft.com/ru-ru/azure/foundry/how-to/create-projects), [Foundry pricing FAQ](https://azure.microsoft.com/en-us/pricing/details/microsoft-foundry/#faq) и [Foundry recovery and purge](https://learn.microsoft.com/ru-ru/azure/ai-services/recover-purge-resources).
