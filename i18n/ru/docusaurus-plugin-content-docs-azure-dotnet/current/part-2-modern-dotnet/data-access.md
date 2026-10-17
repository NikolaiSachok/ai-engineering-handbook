---
title: Доступ к данным
sidebar_position: 5
last_verified: 2026-10-17
---

# Ограничивай время жизни контекста и проверяй изменения схемы

Агент может остановиться в ожидании человека, сервис — перезапуститься, а следующий запрос — попасть на другой экземпляр. Если диалог и предложенное действие хранились только в памяти, продолжить работу будет не с чем. Но сохранить переписку тоже мало: по слову «одобрено» нельзя установить, какое именно действие разрешено, с какими аргументами и от имени какого пользователя.

В слое доступа к данным ты реализуешь эти требования через запросы, обновления и изменения схемы. Ошибки здесь менее заметны, чем неудачный вызов модели: при каждом шаге диалога загружается вся история, устаревшее одобрение затирает более новое решение, в результат попадают строки другого клиента приложения (tenant). Выбор сервиса хранения разобран в [уроке о данных в Azure](../part-1-azure-foundations/data.md). Здесь ты разберёшь, как .NET-приложение работает с базой и как контролировать эту работу.

## Как это устроено в .NET \{#how-it-works-in-dotnet}

Примеры рассчитаны на [.NET 10 — текущую LTS-версию](https://learn.microsoft.com/ru-ru/dotnet/core/releases-and-support) на дату проверки, с [поддержкой до 14 ноября 2028 года](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core). [EF Core 10 требует SDK и среды выполнения .NET 10](https://learn.microsoft.com/ru-ru/ef/core/what-is-new/ef-core-10.0/whatsnew).

EF Core (Entity Framework Core) — библиотека объектно-реляционного отображения (object-relational mapper, ORM).

Ты описываешь сущности и связи на C#, а [поставщик базы данных (database provider) переводит запросы LINQ](https://learn.microsoft.com/ru-ru/ef/core/querying/) на язык конкретной СУБД. Для PostgreSQL используется [поставщик Npgsql для EF Core](https://www.npgsql.org/efcore/). От поставщика зависят и перевод запросов, и возможности, специфичные для базы данных.

`DbContext` хранит модель, позволяет строить запросы и отслеживает изменения сущностей до сохранения или отказа от изменений. Создавай его на короткую операцию. В веб-API регистрация через `AddDbContext` обычно задаёт время жизни `Scoped`. Контекст [не потокобезопасен](https://learn.microsoft.com/ru-ru/ef/core/dbcontext-configuration/): прежде чем начать следующую операцию на том же экземпляре, дождись завершения предыдущей через `await`. Параллельным ветвям агента нужны отдельные контексты. Для этого [зарегистрируй `AddDbContextFactory<T>` и внедри `IDbContextFactory<T>`](https://learn.microsoft.com/ru-ru/ef/core/dbcontext-configuration/#use-a-dbcontext-factory): создавай контекст для каждой операции и освобождай его после завершения. Если держать один контекст на весь диалог, одно и то же изменяемое состояние будет сохраняться между вызовами модели и во время пауз в ожидании человека.

Запросы, возвращающие сущности, по умолчанию [включают отслеживание изменений (change tracking)](https://learn.microsoft.com/ru-ru/ef/core/querying/tracking). Для записи одобрения это удобно: загрузи ожидающее решение, проверь допустимость перехода, измени состояние и вызови `SaveChangesAsync`. [Механизм отслеживания записывает состояния сущностей](https://learn.microsoft.com/ru-ru/ef/core/change-tracking/), по которым EF Core определяет, какие строки добавить, обновить или удалить.

Для списка диалогов, который нужен только для чтения, используй запрос без отслеживания (no-tracking query) через `AsNoTracking`: контекст не будет удерживать сущности для последующей записи. Независимо от режима отслеживания доступ по-прежнему определяется правами в базе данных и фильтрами по клиенту приложения.

Добавление свойства в класс и сохранение сущности не создают столбец в базе. При создании [миграции (migration) EF Core сравнивает модель с предыдущим снимком модели (model snapshot)](https://learn.microsoft.com/ru-ru/ef/core/managing-schemas/migrations/) и формирует версионируемый набор операций со схемой. База меняется при применении миграции, а история миграций хранит сведения об уже применённых изменениях. Сохраняй миграции и снимок рядом с моделью, чтобы воспроизвести историю схемы в новой базе.

Перед применением проверь сгенерированные операции. Если EF примет переименование за удаление старого столбца и добавление нового, можно потерять данные. Для развёртывания [подготовь SQL-скрипт для проверки или пакет миграций (migration bundle)](https://learn.microsoft.com/ru-ru/ef/core/managing-schemas/migrations/applying). Применяй изменения от имени отдельного удостоверения с правами на изменение схемы, а не от имени удостоверения работающего приложения. Порядок expand–migrate–contract и восстановление разобраны в [уроке AI SDLC о миграциях](/ai-sdlc/part-4-platform/environments-migrations-data). EF генерирует операции, но не определяет, нужен ли старому экземпляру приложения удаляемый столбец.

## Как выбрать способ доступа к данным \{#choosing-and-tradeoffs}

Начни с паттернов доступа: какие запросы и обновления нужны приложению. Транзакционная запись одобрения и отчёт по тем же таблицам могут использовать разные способы доступа.

| Способ | Когда подходит | Когда не подходит / за что ты отвечаешь |
|---|---|---|
| EF Core с LINQ | Обновления сущностей, связи и миграции удобно выражаются через модель. | Если запрос плохо переводится в SQL, изучи результат перевода: удобный C# может скрывать дорогую работу базы. |
| Массовое обновление и удаление в EF Core | `ExecuteUpdateAsync` или `ExecuteDeleteAsync` меняют набор строк без загрузки сущностей. | Эти методы обходят механизм отслеживания. Они не подходят, если нужно синхронизировать уже отслеживаемые экземпляры или рассчитывать на автоматическую проверку конфликтов. |
| SQL через EF Core | Для отдельного запроса нужен явный SQL, а в остальном приложении удобен EF Core. | Сущности из `FromSql` по умолчанию отслеживаются. Значения по-прежнему нужно передавать безопасными параметрами. |
| Dapper | Ты пишешь SQL напрямую и преобразуешь строки результата в небольшие объекты .NET. | Не подходит, если тебе нужны отслеживание изменений и миграции схемы, как в EF Core: в Dapper этих возможностей нет. |
| Npgsql или ADO.NET напрямую | Нужен прямой контроль над командами, соединениями и чтением результатов, без ORM. | Не подходит, если ручное преобразование данных и управление ресурсами добавят работу, а измерения не выявили проблемы, которую такой подход решает. |

В [сравнении EF Core и микро-ORM от Microsoft](https://learn.microsoft.com/ru-ru/dotnet/architecture/modern-web-apps-azure/work-with-data-in-asp-net-core-apps) объясняется различие: в Dapper SQL пишешь ты, а EF Core берёт на себя перевод запросов и отслеживание изменений. Так распределяется ответственность; само по себе это различие не доказывает, что замена EF ускорит HTTP-обработчик. Прежде чем менять библиотеку, проведи измерения на репрезентативных данных и изучи план запроса.

Перед переходом к SQL напрямую посмотри, подходят ли [операции EF для обновления и удаления наборов строк](https://learn.microsoft.com/ru-ru/ef/core/saving/execute-insert-update-delete). `ExecuteUpdateAsync` и `ExecuteDeleteAsync` выполняются сразу: не загружают сущности и не ждут `SaveChanges`.

То, как построен запрос, может влиять на затраты сильнее, чем накладные расходы ORM. При ленивой загрузке связанных данных или запросах внутри цикла может возникнуть [проблема N+1 запросов (N+1 queries)](https://learn.microsoft.com/ru-ru/ef/core/performance/efficient-querying): один запрос за диалогами и ещё по одному за одобрениями каждого диалога. [Ленивую загрузку нужно включать явно](https://learn.microsoft.com/ru-ru/ef/core/querying/related-data/lazy). Заранее выбирай, какие данные нужны: используй проекцию (projection) для нужных столбцов, фильтруй в базе и ограничивай число результатов до их загрузки в память. Если сначала вызвать `ToListAsync`, последующая фильтрация будет происходить уже в памяти приложения. Индекс должен соответствовать фильтру и порядку сортировки запроса; одно его наличие не гарантирует пользы.

Посмотри и на то, как добавление `Include` влияет на запрос. Если один запрос соединяет несколько коллекций одного уровня, число строк может резко вырасти из-за повторяющихся комбинаций — это [декартовый взрыв (cartesian explosion)](https://learn.microsoft.com/ru-ru/ef/core/querying/single-split-queries). Разделённый запрос (split query) позволяет избежать такого перемножения, но добавляет обращения к базе, а между запросами данные могут измениться. Прежде чем выбирать этот вариант, изучи структуру результата и требования к согласованности.

Отслеживание иногда сокращает выделение памяти: если сущность уже отслеживается, EF возвращает тот же экземпляр при её повторном появлении в результате. Если проекция выбирает только скалярные значения, отслеживать нечего. Выбирай режим с учётом [структуры результата и правил отслеживания](https://learn.microsoft.com/ru-ru/ef/core/querying/tracking).

Если запрос неудобно выразить на LINQ, можно использовать [SQL API самого EF](https://learn.microsoft.com/ru-ru/ef/core/querying/sql-queries), не добавляя второй ORM. `FromSql` параметризует интерполированные значения; заранее собранная строка, переданная в `FromSqlRaw`, такой защиты не получает. В параметризованном SQL (parameterized SQL) значения передаются отдельно от текста команды. Произвольные имена таблиц и столбцов через параметры не передать: выбирай их из фиксированного списка разрешённых в приложении идентификаторов. Никогда не выполняй SQL, сгенерированный моделью, лишь на том основании, что его синтаксис успешно разобран.

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

В P2 ты добавляешь хранилище диалогов и одобрений к сервису P1 за AI-шлюзом (AI gateway). Шлюз контролирует доступ к сервису. Каждая операция с хранилищем должна затрагивать только данные аутентифицированного клиента приложения и конкретного ресурса. Идентификатор клиента приложения для фильтра бери из доверенного контекста запроса, а не из аргумента инструмента. В [уроке о вызове инструментов](/rag-agents/part-2-agents/tool-use/) объясняется, почему за выполнение действий и проверку прав отвечает исполняющий код, а не модель.

Настроенное управляемое удостоверение (managed identity) позволяет [подключаться к Azure PostgreSQL с токеном Entra](https://learn.microsoft.com/ru-ru/azure/postgresql/security/security-connect-with-managed-identity). Приложение передаёт токен при подключении вместо хранения пароля базы в строке подключения; настройка разобрана в [уроке о RBAC и доступе без ключей](../part-1-azure-foundations/rbac-and-keyless-access.md).

Сохрани предложение до того, как запрашивать одобрение человека. Решение должно относиться к конкретному диалогу, инструменту и точным аргументам; изменение предложения требует нового решения. Модель данных в упражнении хранит эти поля и статус ожидания. Для полноценного процесса одобрения нужно также хранить, кто и когда принял решение и до какого срока оно действует, а допустимые переходы состояний контролировать в коде. Это позволит исполняющему коду установить, кто одобрил какое действие.

Два запроса могут одновременно прочитать одно ожидающее одобрение. [Оптимистический контроль параллелизма (optimistic concurrency)](https://learn.microsoft.com/ru-ru/ef/core/saving/concurrency) сравнивает исходное значение при обновлении: если другой запрос успел его изменить, EF выбросит `DbUpdateConcurrencyException`. Если токеном параллелизма (concurrency token) служит `Status`, проверка обнаружит конкурирующее изменение статуса, но не любого другого поля. При конфликте заново загрузи данные и оцени, допустим ли переход в текущем состоянии. Повторяй запись только в том случае, если переход по-прежнему допустим. Организуй работу приложения так, чтобы уже одобренное предложение оставалось неизменным.

Для обнаружения изменений во всей строке Npgsql позволяет [сопоставить свойство `uint`, настроенное через `IsRowVersion()`, с системным столбцом PostgreSQL `xmin`](https://www.npgsql.org/efcore/modeling/concurrency.html). Его значение меняется при обновлении строки.

Другой вариант — условный `ExecuteUpdateAsync`, который одной командой переводит конкретное одобрение из `Pending` в следующее состояние. Включи в фильтр доверенное ограничение по клиенту приложения и ресурсу, а также ожидаемое состояние. Продолжай, только убедившись, что изменена ровно одна строка. [При массовых операциях проверка конфликтов остаётся обязанностью вызывающего кода](https://learn.microsoft.com/ru-ru/ef/core/saving/execute-insert-update-delete#concurrency-control-and-rows-affected). Если нужно обнаруживать изменения других полей, добавь в условие и исходный токен.

Сохраняй связанные изменения базы одним вызовом [`SaveChanges`: при поддержке со стороны поставщика этот вызов выполняется транзакционно](https://learn.microsoft.com/ru-ru/ef/core/saving/transactions). Держи транзакцию короткой: ожидание модели или человека удерживает ресурсы базы на непредсказуемое время. Вызов внешнего инструмента в эту транзакцию не входит, и откат строк не отменит уже отправленный запрос. Исполняющий код должен сохранять состояние выполнения и организовывать повторные попытки с ключом идемпотентности (idempotency key). В [уроке об устойчивых запусках](/rag-agents/part-2-agents/durable-runs/) разобрано, кто отвечает за состояние запуска и что нужно проверить перед повторным действием после возобновления.

## Попробуй \{#try-it}

Подготовь локально хранилище PostgreSQL для P2 и первую миграцию: сгенерируй файлы схемы и посмотри SQL запроса без отслеживания. Упражнение не создаёт сервер PostgreSQL и не выполняет чтение или запись в базе.

**Проверка:** код страницы собран 17.10.2026 с .NET SDK 10.0.402, Npgsql.EntityFrameworkCore.PostgreSQL 10.0.3, Microsoft.EntityFrameworkCore.Design 10.0.13 и dotnet-ef 10.0.13. Все показанные команды выполнены как написано; описанные ниже результаты получены в этом прогоне. Сервер PostgreSQL, работающая база данных и подписка Azure не использовались. Ни один шаг к ним не подключается.

С установленным .NET 10 SDK создай временный консольный проект. На 17.10.2026 проверены последние стабильные версии: [поставщик Npgsql 10.0.3](https://www.nuget.org/packages/Npgsql.EntityFrameworkCore.PostgreSQL/10.0.3), [пакет EF для разработки 10.0.13](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Design/10.0.13) и [инструмент EF 10.0.13](https://www.nuget.org/packages/dotnet-ef/10.0.13). Npgsql 10.0.3 совместим с EF Core 10.0.13.

```bash
dotnet new console --framework net10.0 --output P2.Store
cd P2.Store
dotnet new tool-manifest
dotnet tool install --local dotnet-ef --version 10.0.13
dotnet package add Npgsql.EntityFrameworkCore.PostgreSQL --version 10.0.3
dotnet package add Microsoft.EntityFrameworkCore.Design --version 10.0.13
```

Команды используют документированные [шаблоны](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new-sdk-templates), [локальную установку инструмента](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-tool-install) и [добавление пакетов](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-package-add). Создай файл `AgentStore.cs`:

```csharp
using Microsoft.EntityFrameworkCore;

namespace P2.Store;

public sealed class Conversation
{
    public Guid Id { get; set; }
    public required string TenantId { get; set; }
    public required string Title { get; set; }
}

public sealed class Approval
{
    public Guid Id { get; set; }
    public Guid ConversationId { get; set; }
    public required string Tool { get; set; }
    public required string Arguments { get; set; }
    public string Status { get; set; } = "Pending";
}

public sealed class AgentStore : DbContext
{
    public DbSet<Conversation> Conversations => Set<Conversation>();
    public DbSet<Approval> Approvals => Set<Approval>();

    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseNpgsql("Host=localhost;Database=p2;Username=p2");

    protected override void OnModelCreating(ModelBuilder model)
    {
        model.Entity<Conversation>().HasIndex(c => new { c.TenantId, c.Id });
        model.Entity<Approval>().HasOne<Conversation>().WithMany()
            .HasForeignKey(a => a.ConversationId)
            .OnDelete(DeleteBehavior.Restrict);
        model.Entity<Approval>().Property(a => a.Status).IsConcurrencyToken();
    }
}
```

Строка подключения задаёт локальную базу и не содержит пароля; упражнение к ней не подключается. [Контекст с конструктором без параметров](https://learn.microsoft.com/ru-ru/ef/core/cli/dbcontext-creation) позволяет инструментам получить модель. Когда перенесёшь контекст в веб-API, настрой подключение через внедрение зависимостей и конфигурацию работающего приложения.

Внешний ключ связывает одобрения с диалогами, а ограничение удаления не даёт незаметно удалить одобрения вместе с диалогом. Эти настройки не обеспечивают авторизацию по клиенту приложения и не реализуют правила одобрения.

Замени содержимое `Program.cs`:

```csharp
using Microsoft.EntityFrameworkCore;
using P2.Store;

using var db = new AgentStore();
var tenantId = "demo"; // Synthetic trusted tenant for this local exercise.
var conversations = db.Conversations
    .AsNoTracking()
    .Where(c => c.TenantId == tenantId)
    .OrderBy(c => c.Id)
    .Take(20);

Console.WriteLine(conversations.ToQueryString());
```

[`ToQueryString`](https://learn.microsoft.com/ru-ru/dotnet/api/microsoft.entityframeworkcore.entityframeworkqueryableextensions.toquerystring?view=efcore-10.0) выводит SQL для отладки. Чтобы получить данные, позже понадобится асинхронно загрузить результат из настроенной базы. Использование индекса проверяется по плану выполнения.

Сгенерируй первую миграцию и SQL, затем посмотри запрос:

```bash
dotnet ef migrations add InitialAgentStore
dotnet ef migrations script 0 InitialAgentStore --output migration.sql
dotnet run
```

Как описано в [справочнике EF CLI](https://learn.microsoft.com/ru-ru/ef/core/cli/dotnet), появятся каталог `Migrations` с файлами миграции и снимком модели, а также `migration.sql`. Убедись, что в SQL есть две таблицы, внешний ключ одобрения с `ON DELETE RESTRICT` и индекс диалогов. Консоль выведет запрос с фильтром по клиенту приложения, сортировкой и ограничением в 20 строк. Идентификатор клиента приложения и предел числа строк видны как параметры в комментариях над `SELECT`; сами строки из базы не выводятся. Сохрани сгенерированные файлы как начальную схему P2. Применение схемы и проверка сохранения данных в PostgreSQL относятся к следующему шагу интеграции.

**Стоимость:** бесплатно, только локальная работа. Ресурсы Azure, размещённая база данных и вызовы модели не нужны; результат — локальные файлы и SQL.

**Удаление ресурсов:** когда закончишь упражнение, удали локальный каталог `P2.Store`. Удалять базу данных или ресурсы Azure не требуется: они не создавались.

## Что перенести в свою практику \{#what-to-take-away}

- Ограничивай время жизни `DbContext` короткой операцией. Для параллельных ветвей создавай отдельные контексты.
- Для обновлений осознанно выбирай отслеживание изменений. Для чтения без последующей записи выбирай запросы без отслеживания, ограничивай результат и используй подходящую проекцию. Изучи SQL, прежде чем искать причину медленной работы в ORM.
- Проверяй миграции как изменения схемы: сохранение сущностей не развёртывает схему. Сгенерированные операции нужно испытать в PostgreSQL.
- Привязывай одобрение к точному предложению и проверяй конкурирующие переходы состояний. Гарантии при повторном вызове внешнего инструмента нужно продумывать отдельно от транзакций базы данных.

**[Новые термины](../glossary.md#data-access)**: библиотека объектно-реляционного отображения, EF Core, поставщик базы данных, DbContext, отслеживание изменений, запрос без отслеживания, миграция, снимок модели, проекция, проблема N+1 запросов, декартовый взрыв, Dapper, параметризованный SQL, оптимистический контроль параллелизма, токен параллелизма, разделённый запрос, пакет миграций.

## Источники \{#sources}

Проверено на 17.10.2026.

**Платформа и выполнение запросов**

- [Выпуски и поддержка .NET](https://learn.microsoft.com/ru-ru/dotnet/core/releases-and-support) и [Текущие условия поддержки](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core)
- [Новые возможности EF Core 10](https://learn.microsoft.com/ru-ru/ef/core/what-is-new/ef-core-10.0/whatsnew)
- [Запросы к данным](https://learn.microsoft.com/ru-ru/ef/core/querying/) и [Как работают запросы](https://learn.microsoft.com/ru-ru/ef/core/querying/how-query-works)
- [Время жизни и настройка DbContext](https://learn.microsoft.com/ru-ru/ef/core/dbcontext-configuration/)
- [Отслеживание изменений](https://learn.microsoft.com/ru-ru/ef/core/change-tracking/), [Запросы с отслеживанием и без него](https://learn.microsoft.com/ru-ru/ef/core/querying/tracking) и [Обновление и удаление наборов строк](https://learn.microsoft.com/ru-ru/ef/core/saving/execute-insert-update-delete)
- [Эффективное выполнение запросов](https://learn.microsoft.com/ru-ru/ef/core/performance/efficient-querying), [Ленивая загрузка](https://learn.microsoft.com/ru-ru/ef/core/querying/related-data/lazy) и [Один запрос и разделённые запросы](https://learn.microsoft.com/ru-ru/ef/core/querying/single-split-queries)
- [SQL-запросы](https://learn.microsoft.com/ru-ru/ef/core/querying/sql-queries) и [EF Core и микро-ORM](https://learn.microsoft.com/ru-ru/dotnet/architecture/modern-web-apps-azure/work-with-data-in-asp-net-core-apps)
- [Поставщик Npgsql для EF Core](https://www.npgsql.org/efcore/), [Команды и чтение результатов в Npgsql](https://www.npgsql.org/doc/basic-usage.html) и [Документация Dapper](https://github.com/DapperLib/Dapper)

**Схема и согласованность**

- [Обзор миграций](https://learn.microsoft.com/ru-ru/ef/core/managing-schemas/migrations/) и [Применение миграций](https://learn.microsoft.com/ru-ru/ef/core/managing-schemas/migrations/applying)
- [Транзакции](https://learn.microsoft.com/ru-ru/ef/core/saving/transactions), [Конфликты параллельных изменений](https://learn.microsoft.com/ru-ru/ef/core/saving/concurrency) и [Токены параллелизма в Npgsql](https://www.npgsql.org/efcore/modeling/concurrency.html)
- [Подключение к Azure PostgreSQL с управляемым удостоверением](https://learn.microsoft.com/ru-ru/azure/postgresql/security/security-connect-with-managed-identity)
- [Индексы](https://learn.microsoft.com/ru-ru/ef/core/modeling/indexes), [Внешние ключи](https://learn.microsoft.com/ru-ru/ef/core/modeling/relationships/foreign-and-principal-keys) и [Варианты каскадного удаления](https://learn.microsoft.com/ru-ru/ef/core/saving/cascade-delete)

**Документация к упражнению**

- [Шаблоны dotnet new](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new-sdk-templates), [dotnet new](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new), [Добавление пакетов](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-package-add) и [Установка инструментов](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-tool-install) и [dotnet run](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-run)
- [EF CLI](https://learn.microsoft.com/ru-ru/ef/core/cli/dotnet), [Создание контекста для инструментов разработки](https://learn.microsoft.com/ru-ru/ef/core/cli/dbcontext-creation) и [API ToQueryString](https://learn.microsoft.com/ru-ru/dotnet/api/microsoft.entityframeworkcore.entityframeworkqueryableextensions.toquerystring?view=efcore-10.0)
- [Поставщик Npgsql 10.0.3](https://www.nuget.org/packages/Npgsql.EntityFrameworkCore.PostgreSQL/10.0.3), [Пакет EF для разработки 10.0.13](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Design/10.0.13) и [Инструмент EF 10.0.13](https://www.nuget.org/packages/dotnet-ef/10.0.13)
