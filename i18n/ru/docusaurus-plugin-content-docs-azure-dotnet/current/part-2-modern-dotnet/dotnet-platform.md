---
title: "Платформа .NET сегодня"
sidebar_position: 1
last_verified: 2026-10-17
---

# SDK, целевую платформу и среду выполнения выбирают отдельно

На ноутбуке приложение собирается, а на другом компьютере не запускается — до обработки первого запроса дело даже не доходит. Причины могут быть разными: сборочная машина выбирает другой компилятор, библиотеке нужны API, на которые проект не рассчитан, или на сервере нет нужной среды выполнения (runtime). Все три случая похожи на «проблему с версией .NET», хотя изменить один номер версии и тем самым устранить все три причины не получится.

Прежде чем добавлять клиент модели, явно задай инструменты сборки, доступный API и среду запуска. В этом уроке ты разберёшь, чем они отличаются, и создашь локальное решение (solution) для RAG-сервиса P1. Начать можно без учётной записи Azure.

## Как это устроено в .NET \{#how-it-works-in-dotnet}

[Платформа .NET](https://learn.microsoft.com/ru-ru/dotnet/core/introduction) предоставляет библиотеки для HTTP и JSON и автоматически управляет памятью с помощью сборщика мусора. Код приложения исполняет среда выполнения, а стек для веб-приложений предоставляет ASP.NET Core. Среда выполнения, библиотеки и ASP.NET Core — отдельные части платформы, хотя часто ты устанавливаешь их вместе.

Для разработки нужен [SDK (software development kit)](https://learn.microsoft.com/ru-ru/dotnet/core/sdk): в него входят `dotnet` CLI, инструменты сборки и среда выполнения для локальной работы. Установи SDK, если собираешься создавать и собирать проекты. Для запуска уже собранного сервиса серверу достаточно среды выполнения; компилятор для этого не требуется.

В упражнении появятся три файла с разными задачами:

- `global.json` выбирает SDK для команд CLI.
- `Rag.Api.csproj` описывает сборку проекта и его целевую платформу.
- `RagService.slnx` — файл решения, который группирует проекты для инструментов разработки и команд CLI. Решение удобно при разработке, но само по себе не является запущенным процессом или ресурсом Azure.

```mermaid
flowchart LR
    G["global.json"] -->|Выбирает| S["SDK"]
    S --> B["Сборка под TFM"]
    B -->|Запуск на| R["Среда выполнения"]
```

Веб-проект в стиле SDK (SDK-style project) на C# может быть совсем небольшим. В этом примере также включено использование файла блокировки:

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <RestorePackagesWithLockFile>true</RestorePackagesWithLockFile>
  </PropertyGroup>
</Project>
```

`Microsoft.NET.Sdk.Web` выбирает правила сборки веб-проекта, а не версию установленного SDK. [SDK проекта](https://learn.microsoft.com/ru-ru/dotnet/core/project-sdk/overview) неявно подключает свойства и цели MSBuild и по соглашению включает обычные исходные файлы: перечислять каждый `.cs` не требуется. `ImplicitUsings` добавляет импорты часто используемых пространств имён, а `Nullable` включает анализ ссылок, которые могут быть `null`, но входящий HTTP-запрос этот анализ не проверяет.

Идентификатор целевой платформы (target framework moniker, TFM) задаёт API, доступный проекту. Значение [`net10.0` означает .NET 10](https://learn.microsoft.com/ru-ru/dotnet/standard/frameworks); это не номер исправления SDK, и его указание не приводит к установке среды выполнения. Изменение `global.json` меняет выбранные инструменты, но не переписывает `TargetFramework`. При разборе ошибки сборки сначала выясни, какой SDK выбран, затем — под какую платформу собирается проект.

Дополнительные библиотеки с собственными версиями поступают через NuGet. Элемент `PackageReference` объявляет прямую зависимость проекта от пакета. Тот, в свою очередь, может потребовать другие пакеты — транзитивные зависимости (transitive dependencies).

[Восстановление зависимостей (restore) разрешает этот граф](https://learn.microsoft.com/ru-ru/nuget/concepts/dependency-resolution) и записывает результат для сборки в `obj/project.assets.json`. Приложение также может хранить [файл блокировки (lock file) `packages.lock.json`](https://learn.microsoft.com/ru-ru/nuget/consume-packages/package-references-in-project-files#locking-dependencies). В нём записан разрешённый граф, и в CI можно требовать, чтобы восстановление ему соответствовало. Сгенерированный `project.assets.json` в репозиторий не добавляют.

Через CLI ты выполняешь весь цикл работы: `dotnet new` создаёт файлы по шаблону, `dotnet restore` разрешает зависимости, `dotnet build` компилирует проект, а `dotnet run` запускает приложение при разработке. [Команды, которым нужно восстановление, обычно выполняют его неявно](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new#implicit-restore). В конвейере полезно разделить восстановление и сборку: тогда ошибки источника пакетов и зависимостей видны ещё до компиляции, а неожиданное изменение графа можно отклонить.

## Как выбрать платформу с действующей поддержкой \{#choosing-a-supported-platform}

Если ты привык к .NET Framework, за сменой названий легко не заметить существенные изменения самой платформы. Разбирая старый репозиторий, сначала определи по таблице, к какой ветви он относится: от этого зависит, что удастся перенести без изменений.

| Платформа | Что обозначает | Решение для сервиса |
|---|---|---|
| .NET Framework 4.x | Платформа Windows для существующих приложений, в том числе ASP.NET Web Forms. Пример TFM — `net481`. | Оставляй существующее приложение на ней, если этого требуют зависимости. Для нового кроссплатформенного API выбирай современный .NET. |
| .NET Core 1–3.1 | Прежнее название кроссплатформенного .NET. `netcoreapp3.1` — TFM тех лет; эти версии [больше не поддерживаются](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core). | Если такой TFM достался вместе с проектом, потребуется обновление. |
| .NET 5 и новее | Продолжение .NET Core под названием .NET. Для современных серверных приложений используется ASP.NET Core. | Выбирай выпуск с действующей поддержкой. Для P1 выбран .NET 10. |

[Рекомендации Microsoft для серверных приложений](https://learn.microsoft.com/ru-ru/dotnet/standard/choosing-core-framework-server) предлагают современный .NET для новых сервисов и перечисляют технологии, из-за которых существующее приложение может потребоваться оставить на .NET Framework. Одной правкой TFM приложение Web Forms не превратить в сервис ASP.NET Core. Сначала составь список зависимостей и выясни, где код предполагает работу в Windows. При миграции можно сохранить взаимодействие через API и разрабатывать новый сервис отдельно.

.NET Standard — ещё одно обозначение, которое можно встретить среди целевых платформ библиотек. Это [спецификация общего набора API](https://learn.microsoft.com/ru-ru/dotnet/standard/net-standard) для разных реализаций .NET, а не отдельная среда выполнения. Она полезна библиотекам, которым нужна такая совместимость. P1 — приложение для .NET 10 с TFM `net10.0`; без конкретного требования совместимости ограничивать его набором API библиотеки .NET Standard незачем.

По [текущей политике Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) основные выпуски выходят каждый ноябрь. Чётные версии получают долгосрочную поддержку (Long Term Support, LTS) на три года. Нечётные — стандартную поддержку (Standard Term Support, STS) на два года. Выпуски этих категорий различаются сроком поддержки, а не качеством.

На 17.10.2026 текущий LTS-выпуск — .NET 10; его поддержка действует до 14 ноября 2028 года. У .NET 8 LTS и .NET 9 STS поддержка заканчивается 10 ноября 2026 года. Если начать новый P1 на любой из этих двух версий, почти сразу придётся его обновлять.

Для учебного сервиса подходит LTS: срок поддержки у него дольше, и приложение будет оставаться на поддерживаемой версии по мере развития проектов курса. Для активно сопровождаемого сервиса можно выбрать STS, если новая версия даёт нужную возможность, а команда успеет обновиться до конца её поддержки. Сравнивай оставшиеся сроки: сама метка LTS не делает более старый выпуск лучшим выбором.

Закрепив версию SDK, ты явно задаёшь, какими инструментами собирать приложение. Если оно использует файлы блокировки пакетов, [задай для `rollForward` значение `disable`](https://learn.microsoft.com/ru-ru/dotnet/core/tools/global-json#rollforward) в `global.json`: тогда разработчики и CI будут использовать одну точную версию SDK. Для некоторых типов проектов SDK добавляет неявные элементы `PackageReference`. При смене SDK версии этих пакетов могут измениться, из-за чего [восстановление в режиме блокировки может завершиться ошибкой](https://learn.microsoft.com/ru-ru/nuget/consume-packages/package-references-in-project-files#locking-dependencies). При обновлении закреплённой версии SDK заново создай затронутые файлы блокировки, затем пересобери и протестируй приложение.

Без файла блокировки можно выбрать `latestPatch`: эта политика допускает более новые установленные исправления в пределах выбранной группы компонентов SDK (SDK feature band). Версии SDK объединяются в группы по разряду сотен в последнем компоненте номера: так обновления возможностей инструментов отделяются от исправлений внутри группы. Исправления среды выполнения выпускаются отдельно от этих групп SDK. Ни `latestPatch`, ни `disable` не устанавливают SDK; при `disable` отсутствие точной версии приведёт к ошибке.

Даже с закреплённой версией нельзя три года обходиться без исправлений: [для сохранения поддержки нужно устанавливать актуальные обновления обслуживания (servicing updates)](https://learn.microsoft.com/ru-ru/dotnet/core/releases-and-support). Отдельно выбирают, как доставлять среду выполнения: [приложение, зависящее от платформы, использует установленную среду, а автономная публикация включает её в поставку](https://learn.microsoft.com/ru-ru/dotnet/core/deploying/). Упаковка и варианты развёртывания разбираются в уроке II.7 [«Контейнеры и Aspire»](./overview.md#whats-inside).

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

[P1 — RAG-сервис курса](../intro.md#how-a-lesson-works): API на .NET отвечает на вопросы по небольшому набору документов из открытых источников и указывает источники в ответе. У клиентских AI-библиотек собственный график выпусков, независимый от .NET LTS: в [истории версий пакетов](https://www.nuget.org/packages/OpenAI/) видны частые обновления и предварительные выпуски. Поддерживаемая среда выполнения сама по себе не говорит, как поведёт себя развёрнутая версия клиентской библиотеки. Выбор библиотек относится к уроку II.8 [«AI в .NET»](./overview.md#whats-inside); здесь ты научишься сохранять сведения о выбранном графе зависимостей для каждого релиза.

Допустим, после обновления ответы перестали содержать ссылки на источники. Сравни `global.json` и `packages.lock.json` у последней исправной сборки и у сборки с ошибкой:

- Если изменилась закреплённая версия SDK, проверь изменения неявных пакетов.
- Если обновился клиент или транзитивный пакет, отдельно проверь это обновление, прежде чем искать причину в модели.
- Если оба файла прежние, переходи к промпту, развёртыванию модели и поисковому индексу: часть переменных сборки уже исключена из поиска причины.

Одинаковые зависимости не гарантируют одинаковые ответы. Сохраняй сведения об изменениях промпта, развёртывания модели и индекса вместе с релизами приложения, чтобы можно было проследить, что изменилось в каждом релизе. Закреплённая версия SDK и файл блокировки описывают инструменты и граф пакетов, но не закрепляют эти внешние данные и настройки. Когда добавишь клиент, запиши точную версию пакета и сохрани полученный файл блокировки, прежде чем сравнивать качество ответов. Если оценка выявит ошибку, у тебя будет конкретное изменение зависимостей, которое можно проверить или исключить.

Успешная сборка ещё не доказывает, что приложение работает правильно. Урок [«Generation — генерация ответа»](/rag-agents/part-1-rag/generation/) разбирает требование отвечать на основе переданного контекста, а [«Многослойные проверки и разнообразие механизмов»](/ai-sdlc/part-3-verification/layered-gates/) объясняет, почему компиляция этого не проверяет. В дальнейших шагах P1 нужно отдельно проверять поиск, работу со ссылками на источники и обычное HTTP-поведение, чтобы успешная компиляция не подменяла результат проверки качества ответов.

## Попробуй \{#try-it}

Создай решение P1 и веб-проект в новой локальной папке. Сначала установи [.NET SDK 10.0.402](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) — стабильный SDK, выбранный для упражнения на 17.10.2026. В него входят среды выполнения .NET и ASP.NET Core 10.0.13. Явные пакеты NuGet на этом шаге не добавляются, поэтому закреплять версии пакетов пока не нужно. Выполняй команды в Bash вне другого репозитория .NET, чтобы чужой `global.json` из родительской папки не повлиял на выбор SDK.

Команды и код этого примера проверены 17.10.2026 на macOS с .NET SDK 10.0.402 и средами выполнения 10.0.13. Проект собран, `dotnet restore --locked-mode` выполнен успешно, локальная конечная точка вернула `Hello World!`. Проверка была только локальной, без обращений к Azure.

```bash
dotnet --list-sdks
mkdir p1-rag-service
cd p1-rag-service

dotnet new globaljson --sdk-version 10.0.402 --roll-forward disable
dotnet --version

dotnet new sln --name RagService
dotnet new web --name Rag.Api --output src/Rag.Api --framework net10.0 --no-restore
dotnet sln RagService.slnx add src/Rag.Api/Rag.Api.csproj
```

Перед восстановлением открой `src/Rag.Api/Rag.Api.csproj` и добавь в `PropertyGroup` строку `<RestorePackagesWithLockFile>true</RestorePackagesWithLockFile>`, как в примере выше. Благодаря этой [настройке в файле проекта](https://learn.microsoft.com/ru-ru/nuget/consume-packages/package-references-in-project-files#enabling-the-lock-file) файл блокировки будет использоваться и при следующих восстановлениях.

```bash
dotnet restore RagService.slnx
dotnet build RagService.slnx --no-restore
dotnet run --project src/Rag.Api/Rag.Api.csproj --no-build --no-launch-profile -- --urls http://127.0.0.1:5080
```

Прежде чем продолжить, убедись, что список установленных SDK содержит `10.0.402`, а `dotnet --version` внутри новой папки выбирает именно эту версию. [Шаблон решения .NET 10 по умолчанию создаёт `.slnx`](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new-sdk-templates#sln), поэтому команды явно указывают `RagService.slnx`. [Шаблон `web`](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new-sdk-templates#web) создаёт проект с основными свойствами из примера выше; настройку файла блокировки ты добавляешь отдельно. Восстановление записывает `src/Rag.Api/packages.lock.json`, а сборка компилирует решение. Пока в файле блокировки будет пустой раздел `net10.0`: явных зависимостей от пакетов на этом шаге нет.

Шаблон `web` создаёт файл `Program.cs`. Как показано в [справочнике по минимальным API](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/minimal-apis?view=aspnetcore-10.0#webapplication), сгенерированный файл содержит следующий код:

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();
```

Не останавливая процесс, открой `http://127.0.0.1:5080/` в браузере. Ожидаемый ответ — `Hello World!`. Параметр [`--no-launch-profile`](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-run) отключает настройки запуска из шаблона. Разделитель `--` передаёт следующие аргументы приложению, а [`--urls` задаёт адрес прослушивания](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-10.0#specify-endpoints-with-urls). По ответу этой конечной точки HTTP на loopback-адресе ты проверяешь только локальный запуск при разработке, без проверки поиска и готовности к Azure.

Храни `global.json`, решение, проект и сгенерированный `packages.lock.json` вместе с исходным кодом. Записи о пакетах появятся в файле блокировки, когда ты начнёшь добавлять пакеты. В будущем конвейер CI сможет запускать [`dotnet restore --locked-mode`](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-restore), чтобы отклонять изменения графа, записанного в файле блокировки; сохраняй вместе с ним и `rollForward: disable`. Сгенерированные каталоги `bin` и `obj` в репозиторий не добавляй.

**Стоимость:** бесплатно. [.NET бесплатен](https://learn.microsoft.com/ru-ru/dotnet/core/introduction); упражнение не создаёт ресурсов Azure и не вызывает модель.

**Удаление ресурсов:** останови процесс сочетанием `Ctrl+C` и удали локальную папку `p1-rag-service`. Если оставляешь её для следующего шага P1, просто останови процесс: останутся только локальные файлы.

## Что перенести в свою практику \{#what-to-take-away}

- Выбирай SDK через `global.json`, а доступный приложению набор API — через `TargetFramework`: эти настройки решают разные задачи.
- Для P1 выбирай `net10.0`, то есть текущий LTS-выпуск .NET 10 с действующей поддержкой, и регулярно устанавливай обновления обслуживания по графику сопровождения.
- Включай использование файла блокировки в проекте и храни сгенерированный файл вместе с закреплённой точной версией SDK. В будущем конвейере CI требуй, чтобы восстановление соответствовало графу из этого файла.
- Закреплённый SDK помогает объяснить результат сборки. После успешной компиляции всё равно отдельно проверяй опору ответов на контекст и ссылки на источники.

**[Новые термины](../glossary.md#dotnet-platform)**: среда выполнения, SDK, проект в стиле SDK, идентификатор целевой платформы (TFM), `global.json`, группа компонентов SDK, LTS, STS, NuGet, `PackageReference`, транзитивная зависимость, восстановление зависимостей, файл блокировки, решение.

## Источники \{#sources}

Проверено на 17.10.2026.

Платформа и поддержка:

- [Общие сведения о .NET](https://learn.microsoft.com/ru-ru/dotnet/core/introduction) · [.NET SDK](https://learn.microsoft.com/ru-ru/dotnet/core/sdk)
- [Обзор SDK проекта](https://learn.microsoft.com/ru-ru/dotnet/core/project-sdk/overview) · [Целевые платформы](https://learn.microsoft.com/ru-ru/dotnet/standard/frameworks) · [global.json](https://learn.microsoft.com/ru-ru/dotnet/core/tools/global-json)
- [Выбор .NET или .NET Framework для серверных приложений](https://learn.microsoft.com/ru-ru/dotnet/standard/choosing-core-framework-server) · [.NET Standard](https://learn.microsoft.com/ru-ru/dotnet/standard/net-standard)
- [Выпуски, исправления и поддержка](https://learn.microsoft.com/ru-ru/dotnet/core/releases-and-support) · [Официальная политика и сроки поддержки](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) · [Загрузка .NET 10 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0)
- [NuGet PackageReference и файлы блокировки](https://learn.microsoft.com/ru-ru/nuget/consume-packages/package-references-in-project-files) · [Разрешение зависимостей](https://learn.microsoft.com/ru-ru/nuget/concepts/dependency-resolution) · [Публикация приложений](https://learn.microsoft.com/ru-ru/dotnet/core/deploying/)

Справочники для упражнения:

- [dotnet](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet) · [dotnet new](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new) · [Шаблоны SDK](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new-sdk-templates) · [dotnet sln](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-sln)
- [dotnet restore](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-restore) · [dotnet build](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-build) · [dotnet run](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-run)
- [Справочник по минимальным API](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/minimal-apis?view=aspnetcore-10.0#webapplication) · [Адреса конечных точек Kestrel](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-10.0#specify-endpoints-with-urls)

История выпусков AI-зависимостей:

- [История версий клиентского AI-пакета](https://www.nuget.org/packages/OpenAI/) — только как пример частоты обновлений и предварительных выпусков; в этом уроке AI-пакеты не устанавливаются.
