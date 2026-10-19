---
title: Хранение данных
sidebar_position: 6
last_verified: 2026-10-17
---

# Выбирай хранилище под операции чтения и записи

Исходные файлы, записи приложения, поисковый индекс и кэш ответов можно разместить в одном сервисе, хотя требования к ним могут противоречить друг другу. При обновлении документа нужно сохранять историю изменений, по которой можно объяснить происхождение цитаты в ответе. Для изменения бизнес-записей может понадобиться транзакция. Если ответ исчез из кэша, приложение должно получить данные заново из основного хранилища, где они сохраняются.

Прежде чем выбирать сервис, опиши **паттерн доступа (access pattern)**: чем идентифицируется запись, какие запросы должны выполняться быстро, какие изменения нужно вносить совместно и насколько свежими должны быть результаты чтения. Затем определи **основное хранилище (system of record)** для каждого вида данных и реши, какие копии можно построить заново.

Такой порядок помогает избежать дорогостоящей ошибки: выбрать все хранилища для AI-сервиса лишь по поддержке векторов, не решив, где хранить основные данные, кому и к каким данным разрешить доступ и как восстановиться после сбоя.

## Как Azure хранит разные виды данных \{#how-azure-stores-data}

[Azure Blob Storage](https://learn.microsoft.com/ru-ru/azure/storage/blobs/storage-blobs-introduction) — **объектное хранилище (object storage)** для PDF, текстовых файлов, изображений и других объектов. Учётная запись хранения (storage account) задаёт пространство имён.

Внутри учётной записи хранения **контейнер блобов (blob container)** объединяет объекты, а имя блоба позволяет обратиться к конкретному объекту. Для исходных документов курса подходят блочные блобы (block blobs).

Когда нужно получить исходный файл по имени, ты обращаешься к Blob Storage. Если же нужно найти во всём наборе документов абзацы, которые лучше всего отвечают на вопрос, в проекте P1 за это отвечает Azure AI Search.

Когда важны связи между записями и согласованное внесение изменений, нужны реляционная схема и транзакции. [Azure SQL Database](https://learn.microsoft.com/ru-ru/azure/azure-sql/database/sql-database-paas-overview?view=azuresql) — управляемый реляционный сервис на основе SQL Server. Azure устанавливает обновления платформы и делает резервные копии; ты проектируешь схему, запросы и транзакции приложения. Сервис также поддерживает встроенный тип [`vector`](https://learn.microsoft.com/ru-ru/sql/t-sql/data-types/vector-data-type) и функцию [`VECTOR_DISTANCE`](https://learn.microsoft.com/ru-ru/sql/t-sql/functions/vector-distance-transact-sql). Например, в таблице заданий на загрузку документов можно хранить статус, версию источника и время завершения. Наличие такой таблицы не обязывает хранить в ней и байты исходных документов.

[Azure Database for PostgreSQL flexible server поддерживает pgvector](https://learn.microsoft.com/ru-ru/azure/postgresql/extensions/how-to-use-pgvector) — расширение PostgreSQL для хранения векторов и поиска по ним рядом с реляционными данными. Сначала добавь расширение в список разрешённых на сервере, затем включи его в каждой базе, где оно нужно. Имя расширения — `vector`. Если нужные записи уже находятся в PostgreSQL, такой вариант может избавить от отдельного хранилища для поиска. Но поисковые запросы будут конкурировать с остальной рабочей нагрузкой базы. Прежде чем считать объединение упрощением, измерь, как база работает при совместной рабочей нагрузке.

В модели NoSQL сервиса Azure Cosmos DB **[ключ раздела (partition key)](https://learn.microsoft.com/ru-ru/azure/cosmos-db/partitioning)** определяет, какие элементы попадут в один логический раздел (logical partition). От выбора ключа и запросов зависит, как нагрузка распределяется между разделами. Например, идентификатор клиента приложения может упростить чтение данных этого клиента, но запросы особенно активного клиента приложения могут сосредоточить нагрузку на одном разделе. Если запрос нельзя ограничить нужными разделами, он может затронуть несколько разделов.

Расход ресурсов на операции Cosmos DB измеряется в **[единицах запросов (request units, RU)](https://learn.microsoft.com/ru-ru/azure/cosmos-db/request-units)**: они выражают затраты CPU, ввода-вывода и памяти в единой нормализованной величине. При выделенной пропускной способности (provisioned throughput) ты задаёшь её в `RU/s`, а в бессерверном режиме (serverless) платишь за потреблённые RU. Единица запроса не равна строке базы или HTTP-запросу: чтение одного элемента и широкий запрос могут стоить очень по-разному. Прежде чем задавать пропускную способность, посмотри расход RU на характерных данных и с теми фильтрами, которые будет использовать приложение.

[Azure Managed Redis](https://learn.microsoft.com/ru-ru/azure/redis/overview) хранит данные в памяти и подходит для **cache-aside (кэширования по запросу)**. Приложение сначала читает кэш; если записи нет, обращается к основному хранилищу и помещает результат в кэш. Кэш освобождает место, удаляя записи по истечении срока или вытесняя их, поэтому приложение должно уметь получить данные и при промахе кэша. В [рекомендациях Microsoft по безопасности](https://learn.microsoft.com/ru-ru/azure/redis/secure-azure-managed-redis) Redis рассматривается как кэш и временное хранилище, а не как основная база для постоянного хранения данных.

## Сопоставь сервис с запросами и проверь неудобный случай \{#choosing-and-tradeoffs}

Перед сравнением сервисов запиши основные операции чтения и обновления. Добавь случай, который неудобен для предпочитаемого сервиса: соединение таблиц, скачивание большого файла, запрос по нескольким клиентам приложения или всплеск промахов кэша. Такая проверка часто обнаруживает ограничения раньше, чем замер на удобном запросе.

| Сервис | Для каких операций подходит | Когда стоит выбрать другой вариант |
|---|---|---|
| Blob Storage | Хранение и получение исходных файлов по имени; сохранение входных данных для повторной обработки. | Записи приложения требуют соединений или транзакционных изменений нескольких записей. |
| Azure SQL Database | Реляционные данные, ограничения, транзакции, инструменты SQL Server, встроенные [`vector` и `VECTOR_DISTANCE`](https://learn.microsoft.com/ru-ru/sql/t-sql/data-types/vector-data-type). | Нужно только хранить файлы по имени либо требуется совместимость с PostgreSQL. |
| PostgreSQL flexible server + pgvector | Реляционные данные приложения и векторный поиск рядом с ними. | Поиск нужно масштабировать отдельно или ему нужны возможности, которых нет в выбранной конфигурации базы. |
| Cosmos DB for NoSQL | Доступ к документам с продуманным ключом раздела. | Преобладают запросы по нескольким разделам или реляционные соединения. |
| Azure Managed Redis | Повторное чтение результатов, которые можно удалить по истечении срока, вытеснить или получить заново. | При потере записи исчезнет единственная основная копия данных. |

В Blob Storage плата за объём — лишь часть расходов. [Уровни доступа (access tiers)](https://learn.microsoft.com/ru-ru/azure/storage/blobs/access-tiers-overview/) различаются стоимостью хранения и обращений к данным, а также условиями, связанными со сроком хранения. Для многократной загрузки документов в индекс во время разработки разумно начать с Hot. Более холодный уровень может оказаться дороже, если документы часто читаются или заменяются. Для чтения содержимого из Archive сначала нужно восстановить блоб из архива (rehydration). Если конвейер загрузки документов вынужден ждать восстановления исходного файла из архива, этот уровень доступа не соответствует паттерну доступа, даже при низкой стоимости хранения.

В Cosmos DB отдельно выбери **уровень согласованности (consistency level)** — какие гарантии даёт успешное чтение. [Уровней пять](https://learn.microsoft.com/ru-ru/azure/cosmos-db/consistency-levels); они различаются свежестью данных и порядком, в котором чтение видит записи.

| Уровень | Гарантия при чтении |
|---|---|
| Строгая согласованность (Strong) | Последняя зафиксированная версия элемента. |
| Ограниченное устаревание (Bounded staleness) | Отставание ограничено настроенным числом версий или временем. |
| Согласованность сеанса (Session) | В пределах сеанса гарантируется, в частности, чтение собственных записей; используются токены сеанса. |
| Согласованный префикс (Consistent prefix) | Записи видны по порядку, без пропусков. |
| Согласованность в конечном счёте (Eventual) | Если запись прекращается, реплики сходятся; гарантий свежести и порядка нет. |

На уровне согласованности сеанса контекст сеанса пользователя не передаётся автоматически между независимыми экземплярами API. Продумай, как передавать токен сеанса (session token), если запросы переходят между клиентами. Чтение со строгой согласованностью или ограниченным устареванием расходует больше RU, чем при более слабых уровнях согласованности. Выбирай гарантию под действие пользователя: подтверждение только что сохранённых данных и фоновый отчёт, который допускает отставание, предъявляют разные требования.

В Cosmos DB for NoSQL есть **[встроенный векторный поиск](https://learn.microsoft.com/ru-ru/azure/cosmos-db/vector-search)**: векторы хранятся рядом с рабочими элементами, а поиск использует политики эмбеддингов и индексации, фильтры и `VectorDistance`. Перед настройкой включи эту возможность в учётной записи Cosmos DB. [Она не поддерживается в учётных записях Cosmos DB с общей пропускной способностью; после включения в контейнере отключить её нельзя](https://learn.microsoft.com/ru-ru/azure/cosmos-db/vector-search#current-limitations). Если документы уже находятся в Cosmos, сервис стоит рассмотреть. Но поддержка векторов не определяет за тебя ключ раздела, стоимость запросов или качество поиска. Сам выбор поисковых методов разбирается в уроке [«Как найти нужный контекст под запрос»](/rag-agents/part-1-rag/retrieval/).

Даже если Redis отвечает быстро, сохранённый в кэше ответ уже может быть неверным. Явно задай **срок жизни (TTL)** и определи, какие изменения требуют **инвалидации кэша (cache invalidation)**. Например, обновление документа может потребовать удалить ответы, основанные на прежней версии. [TTL ограничивает, как долго можно повторно использовать ответ, но не гарантирует, что он всё ещё верен](https://learn.microsoft.com/ru-ru/azure/architecture/patterns/cache-aside#problems-and-considerations).

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

[P1](../part-5-projects/rag-service.md) использует минимальные API ASP.NET Core в Azure Container Apps. Azure AI Search и развёртывание модели (model deployment) в Foundry обеспечивают поиск и ответы с цитатами по небольшому набору документов из открытых источников. Исходные файлы хранятся в Blob Storage. Благодаря этому поисковый индекс можно перестроить, когда изменятся парсинг, чанкинг или эмбеддинги. Сами преобразования разбираются в уроке [«Из документов — в поисковый индекс»](/rag-agents/part-1-rag/ingestion/); сейчас задача — сохранить доступными данные, из которых строится индекс.

Назначь каждому обрабатываемому источнику стабильный идентификатор и фиксируй, из какой версии получены чанки индекса. Если просто заменить файл и не сохранить эту связь, цитата может вести к тексту, отличному от того, на котором основан ответ. Оригинал, производный индекс и кэш ответов обновляются отдельно. Явно задай правило, по которому новая версия источника становится доступной для поиска. Транзакция в одном хранилище сама по себе не может скоординировать всю последовательность обновлений.

Права выдавай тому компоненту, который выполняет соответствующую работу. Для API назначь **роль плоскости данных (data-plane role)** [`Storage Blob Data Reader`](https://learn.microsoft.com/ru-ru/azure/storage/blobs/assign-azure-role-data-access) с областью действия (scope), ограниченной контейнером исходных документов. Она разрешает читать блобы и получать их список. Компоненту загрузки, который записывает документы, нужны отдельные права. Доступ удостоверения API к блобам ещё не определяет, какие документы вправе видеть конечный пользователь: это нужно решить при проектировании авторизации поиска.

В уроке [«Секрет, которого агент никогда не держал, не может утечь»](/ai-sdlc/part-4-platform/secrets) разобрана конфигурация приложения без хранения учётных данных. Здесь токены Entra и роль доступа к данным заменяют строку подключения с ключом учётной записи хранения.

## Попробуй \{#try-it}

Создай контейнер документов P1 и управляемое удостоверение (managed identity), назначаемое пользователем (user-assigned), для будущего API. [Позже его можно подключить к Container App](https://learn.microsoft.com/ru-ru/azure/container-apps/managed-identity); развёртывать API сейчас не требуется. Выполняй команды локально в Bash с установленным Azure CLI. Нужны права на создание ресурсов и назначение ролей, включая [`Microsoft.Authorization/roleAssignments/write`](https://learn.microsoft.com/ru-ru/azure/storage/blobs/assign-azure-role-data-access).

Справочные страницы CLI для этих команд проверены. Сами команды при подготовке урока не запускались в действующей подписке Azure. Ниже описаны ожидаемые по документации результаты, а не наблюдения после запуска.

Сначала выполни блок [«Попробуй» из урока 1](/azure-dotnet/part-1-azure-foundations/how-azure-is-organised#try-it): выбери учебную подписку и настрой учебный бюджет. Здесь ты заново создашь группу ресурсов P1 с тегами.

[Войди в Azure](https://learn.microsoft.com/ru-ru/cli/azure/authenticate-azure-cli?view=azure-cli-latest), подставь идентификатор своей подписки вместо `<id>` и [выбери её](https://learn.microsoft.com/ru-ru/cli/azure/account?view=azure-cli-latest#az-account-set). Оставайся в одной оболочке до конца упражнения: следующим командам нужны переменные из предыдущих шагов.

```bash
az login
AZURE_SUBSCRIPTION_ID="<id>"
az account set --subscription "$AZURE_SUBSCRIPTION_ID"

AZURE_RESOURCE_GROUP="rg-p1-rag-dev-$RANDOM"
location='westeurope'
storage="p1docs${RANDOM}${RANDOM}"
container='sources'
az group create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$AZURE_RESOURCE_GROUP" --location "$location" \
  --tags project=p1-rag environment=dev owner=learner --output none
```

Создай стандартную учётную запись хранения общего назначения v2, затем контейнер через плоскость управления (control plane). [Флаги учётной записи хранения](https://learn.microsoft.com/ru-ru/cli/azure/storage/account?view=azure-cli-latest#az-storage-account-create) отключают авторизацию Shared Key и анонимный доступ к блобам. Команда [`container-rm`](https://learn.microsoft.com/ru-ru/cli/azure/storage/container-rm?view=azure-cli-latest#az-storage-container-rm-create) создаёт контейнер через поставщика ресурсов (resource provider), поэтому ключ учётной записи хранения ей не нужен. Если сгенерированное имя учётной записи хранения уже занято, запиши в `storage` другое имя из строчных латинских букв и цифр и повтори команду создания учётной записи хранения.

```bash
az storage account create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$storage" --resource-group "$AZURE_RESOURCE_GROUP" --location "$location" \
  --kind StorageV2 --sku Standard_LRS --access-tier Hot \
  --allow-blob-public-access false --allow-shared-key-access false \
  --https-only true --min-tls-version TLS1_2 --output none

az storage container-rm create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --resource-group "$AZURE_RESOURCE_GROUP" --storage-account "$storage" \
  --name "$container" --public-access off --output none
```

[Создай удостоверение](https://learn.microsoft.com/ru-ru/cli/azure/identity?view=azure-cli-latest#az-identity-create) и получи идентификатор его объекта — `principalId`. Он определяет, кому будут выданы права. Затем получи идентификатор ресурса (resource ID) учётной записи хранения, составь область действия контейнера и [назначь роль](https://learn.microsoft.com/ru-ru/cli/azure/role/assignment?view=azure-cli-latest#az-role-assignment-create). Удостоверения, роли и области действия подробнее разобраны в уроках 2 и 3 — [«Удостоверения I — Microsoft Entra ID»](./entra-id.md) и [«Удостоверения II — RBAC и доступ без ключей»](./rbac-and-keyless-access.md).

```bash
api_principal=$(az identity create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name p1-api --resource-group "$AZURE_RESOURCE_GROUP" --location "$location" \
  --query principalId --output tsv)
printf 'API principal ID: %s\n' "$api_principal"
storage_id=$(az storage account show \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$storage" --resource-group "$AZURE_RESOURCE_GROUP" --query id --output tsv)
container_scope="$storage_id/blobServices/default/containers/$container"

az role assignment create \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --assignee-object-id "$api_principal" \
  --assignee-principal-type ServicePrincipal \
  --role 'Storage Blob Data Reader' --scope "$container_scope"

az storage account show --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$storage" --resource-group "$AZURE_RESOURCE_GROUP" \
  --query '{sharedKey:allowSharedKeyAccess,anonymousBlobs:allowBlobPublicAccess}'
az storage container-rm show \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --resource-group "$AZURE_RESOURCE_GROUP" --storage-account "$storage" --name "$container"
az role assignment list \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --assignee-object-id "$api_principal" --scope "$container_scope" \
  --query '[].{role:roleDefinitionName, principal:principalId}' --output table
```

Ожидаемый результат проверки учётной записи хранения — `false` для обеих настроек. Проверка контейнера должна показать `sources`, а список назначений — `Storage Blob Data Reader` для ранее выведенного идентификатора объекта удостоверения API.

Эти команды проверяют конфигурацию. Они не проверяют чтение блобов через API; контейнер пока пуст. Чтобы позже загрузить документы из открытых источников, понадобится отдельный компонент с правами на запись и аутентификацией через Entra. Перед проверкой чтения привяжи удостоверение `p1-api` к приложению API и настрой приложение так, чтобы оно получало токен с использованием нужного удостоверения. Изменения ролей могут применяться с задержкой.

После отключения анонимного доступа сетевая конечная точка остаётся публичной. Применять ли сетевую изоляцию — отдельное решение.

**Стоимость:** в пустом контейнере нет байтов документов, поэтому плата за занимаемый ими объём практически нулевая. [Blob Storage тарифицирует объём отдельно от операций](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/). На дату проверки урока [Microsoft retail API](https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20%27Storage%27%20and%20armRegionName%20eq%20%27westeurope%27%20and%20skuName%20eq%20%27Hot%20LRS%27%20and%20priceType%20eq%20%27Consumption%27) указывает для стандартной учётной записи хранения общего назначения v2 в West Europe тариф Hot LRS: 0,0196 USD за GB в месяц в первой ценовой ступени. Хранение 1 GB в течение месяца обойдётся примерно в 0,02 USD только за объём. Дополнительно оплачиваются операции и передача данных, если она тарифицируется. Проверь цену для своего региона и договора на [странице цен](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/). [Управляемые удостоверения не требуют доплаты](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview), [Azure RBAC бесплатен](https://learn.microsoft.com/ru-ru/azure/role-based-access-control/overview#license-requirements). Упражнение не создаёт базу данных, поисковый сервис или развёртывание модели.

**Удаление ресурсов:** до завершения практической работы [удали группу ресурсов](https://learn.microsoft.com/ru-ru/cli/azure/group?view=azure-cli-latest#az-group-delete) вместе с хранилищем и удостоверением. Для следующих шагов проекта их можно создать заново. Сохраняй значение `AZURE_RESOURCE_GROUP` до завершения удаления.

```bash
az group delete \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$AZURE_RESOURCE_GROUP" --yes
az group exists \
  --subscription "$AZURE_SUBSCRIPTION_ID" \
  --name "$AZURE_RESOURCE_GROUP"
```

Проверь, что удаление завершилось: последняя команда должна вернуть `false`.

## Что перенести в свою практику \{#what-to-take-away}

- Выбирай хранилище под нужные операции чтения, записи и гарантии согласованности: сама по себе поддержка векторов этих гарантий не даёт.
- Сохраняй исходные документы как основные данные, а производные данные для поиска делай восстанавливаемыми. Связь с версией источника позволяет проследить происхождение цитаты.
- Измеряй расход RU в Cosmos DB на характерных запросах с выбранным ключом раздела. Уровень согласованности выбирай под действие пользователя.
- Выдавай API роль доступа к данным в пределах контейнера и используй токены. Компоненту загрузки документов выдавай права на запись через отдельное удостоверение.

**[Новые термины](../glossary.md#data)**: паттерн доступа, объектное хранилище, контейнер блобов, основное хранилище, pgvector, ключ раздела, единица запроса, уровень согласованности, cache-aside, срок жизни, инвалидация кэша, роль плоскости данных.

## Источники \{#sources}

Проверено на 17.10.2026.

- **Хранение и реляционные сервисы:** [Blob Storage](https://learn.microsoft.com/ru-ru/azure/storage/blobs/storage-blobs-introduction), [уровни доступа](https://learn.microsoft.com/ru-ru/azure/storage/blobs/access-tiers-overview/), [Azure SQL Database](https://learn.microsoft.com/ru-ru/azure/azure-sql/database/sql-database-paas-overview?view=azuresql), [тип SQL `vector`](https://learn.microsoft.com/ru-ru/sql/t-sql/data-types/vector-data-type), [`VECTOR_DISTANCE`](https://learn.microsoft.com/ru-ru/sql/t-sql/functions/vector-distance-transact-sql), [PostgreSQL pgvector](https://learn.microsoft.com/ru-ru/azure/postgresql/extensions/how-to-use-pgvector).
- **Cosmos DB:** [разделы](https://learn.microsoft.com/ru-ru/azure/cosmos-db/partitioning), [единицы запросов](https://learn.microsoft.com/ru-ru/azure/cosmos-db/request-units), [согласованность](https://learn.microsoft.com/ru-ru/azure/cosmos-db/consistency-levels), [векторный поиск для NoSQL](https://learn.microsoft.com/ru-ru/azure/cosmos-db/vector-search).
- **Redis:** [обзор](https://learn.microsoft.com/ru-ru/azure/redis/overview), [безопасность](https://learn.microsoft.com/ru-ru/azure/redis/secure-azure-managed-redis), [cache-aside](https://learn.microsoft.com/ru-ru/azure/architecture/patterns/cache-aside).
- **Доступ:** [роли и области действия для данных блобов](https://learn.microsoft.com/ru-ru/azure/storage/blobs/assign-azure-role-data-access), [запрет авторизации Shared Key](https://learn.microsoft.com/ru-ru/azure/storage/common/shared-key-authorization-prevent), [управляемые удостоверения Container Apps](https://learn.microsoft.com/ru-ru/azure/container-apps/managed-identity), [назначение ролей](https://learn.microsoft.com/ru-ru/azure/role-based-access-control/role-assignments-cli), [обзор управляемых удостоверений](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview), [лицензирование Azure RBAC](https://learn.microsoft.com/ru-ru/azure/role-based-access-control/overview#license-requirements).
- **CLI:** [вход](https://learn.microsoft.com/ru-ru/cli/azure/authenticate-azure-cli?view=azure-cli-latest), [подписка](https://learn.microsoft.com/ru-ru/cli/azure/account?view=azure-cli-latest), [группа ресурсов](https://learn.microsoft.com/ru-ru/cli/azure/group?view=azure-cli-latest), [учётная запись хранения](https://learn.microsoft.com/ru-ru/cli/azure/storage/account?view=azure-cli-latest), [управление контейнером](https://learn.microsoft.com/ru-ru/cli/azure/storage/container-rm?view=azure-cli-latest), [удостоверение](https://learn.microsoft.com/ru-ru/cli/azure/identity?view=azure-cli-latest), [назначение роли](https://learn.microsoft.com/ru-ru/cli/azure/role/assignment?view=azure-cli-latest).
- **Цены:** [Blob Storage](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/), [retail API: тарифы потребления West Europe Hot LRS](https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20%27Storage%27%20and%20armRegionName%20eq%20%27westeurope%27%20and%20skuName%20eq%20%27Hot%20LRS%27%20and%20priceType%20eq%20%27Consumption%27).
