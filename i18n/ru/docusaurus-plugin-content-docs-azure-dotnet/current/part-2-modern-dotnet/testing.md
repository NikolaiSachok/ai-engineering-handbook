---
title: Тестирование
sidebar_position: 6
last_verified: 2026-10-17
---

# Проверь обработку запроса без вызова модели

API, которое отвечает на вопросы, может выдавать правдоподобный текст и всё же работать неправильно: передавать модели неверный контекст, терять ссылки на источники или принимать пустой вопрос. При обычном чтении ответа такие ошибки легко пропустить. Нужны повторяемые проверки, которые перестанут проходить, если поведение приложения отклонится от заявленного.

Если каждый тест вызывает настоящую модель, при каждом падении приходится разбираться в причине: ошибка в обработке запроса, сбой зависимости или просто другой ответ модели. Отдели поведение приложения, для которого можно задать точные ожидания, от оценки качества ответа. Для RAG-сервиса P1 начни с запроса к `/ask`, подменив зависимость, через которую вызывается модель.

## Как устроены тесты в .NET \{#how-it-works-in-dotnet}

Примеры рассчитаны на .NET 10 — текущую LTS-версию на дату проверки, с поддержкой до 14 ноября 2028 года. Актуальные сроки указаны в [политике поддержки .NET](https://dotnet.microsoft.com/en-us/platform/support/policy).

Выбирая, что включать в тест, ограничься компонентами, которые нужны для обнаружения дефекта. Проверка функции прямым вызовом — модульный тест (unit test). Запрос через HTTP-конвейер проверяет совместную работу нескольких компонентов — это интеграционный тест (integration test). Так можно обнаружить пропущенную регистрацию зависимости или неверную структуру JSON-ответа: при прямом вызове функции эти участки приложения не проверяются.

[xUnit](https://learn.microsoft.com/ru-ru/dotnet/core/testing/unit-testing-csharp-with-xunit) предоставляет атрибуты для объявления тестов и средства проверки результатов. `[Fact]` задаёт один тестовый случай; `[Theory]` вместе с `[InlineData]` запускает одну проверку с разными входными данными. Сначала подготовь данные и зависимости, затем выполни действие и проверь наблюдаемый результат. Асинхронный тест должен возвращать `Task`. Дождись завершения операции через `await`, чтобы проверка учитывала её результат или ошибку.

В ASP.NET Core 10 [`WebApplicationFactory<Program>`](https://learn.microsoft.com/ru-ru/aspnet/core/test/integration-tests?view=aspnetcore-10.0) запускает приложение через `TestServer` — сервер, работающий в том же процессе. Клиент фабрики отправляет запросы через конвейер приложения. Маршрутизация, привязка параметров и сериализация ответа работают как обычно, а механизм внедрения зависимостей позволяет заменить нужные реализации. Так ты проверяешь API без развёртывания приложения.

Тестовый двойник (test double) заменяет зависимость. Упрощённая тестовая реализация (fake) — разновидность двойника: это работающая замена зависимости, которая намеренно воспроизводит лишь часть её поведения. В примере такой клиент модели запоминает входные данные и возвращает фиксированный текст. По записанным данным тест может отличить корректную передачу вопроса и контекста модели от простого возврата какого-то текста. Проверить, что отправлено модели, так же важно, как проверить ответ API.

Для подмены регистрации модели вызови у фабрики `WithWebHostBuilder`, затем у построителя хоста — [`ConfigureTestServices`](https://learn.microsoft.com/ru-ru/aspnet/core/test/integration-tests?view=aspnetcore-10.0). Держи эту подмену в тестовом проекте. Если в конфигурации прода появится переключатель, который незаметно выбирает тестовую реализацию, это будет ещё одна настройка развёртывания, в которой можно ошибиться.

## Что включать в тест \{#choosing-the-boundary}

| Проверка | Что работает по-настоящему | Что подменяется или задаётся тестом | Чего результат не доказывает |
|---|---|---|---|
| Модульный тест | Функция валидации или сопоставления ссылок на источники | Внешние зависимости функции | Что HTTP-обработчик правильно подключён к приложению |
| Интеграционный тест API | Запуск приложения и конвейер запроса | Клиент модели; при необходимости — тестовая фикстура (test fixture) для поиска | Что есть доступ к Azure или что ответ качественный |
| Интеграционный тест с контейнером | Движок выбранной зависимости и клиентский адаптер | Временные данные и конфигурация | Что другой управляемый сервис ведёт себя точно так же |
| Короткая проверка после развёртывания | Развёрнутое приложение и выбранные подключения к сервисам | Небольшой контролируемый набор входных данных | Что качество ответов проверено на широком наборе случаев |
| Оценка качества ответов | Конвейер, качество которого оценивается | Версионируемый набор данных для оценки | Что контракт API соблюдается при каждом варианте ошибки |

Модульные тесты удобны, когда у небольшого правила много вариантов: например, какие пустые вопросы нужно отклонять. Если каждый вариант проводить через HTTP, придётся больше настраивать тесты, хотя новый дефект при этом может и не обнаружиться. Оставь несколько тестов с HTTP-запросами, чтобы проверить привязку параметров и ответ, который получает клиент. По мере усложнения валидации добавляй модульные тесты самих правил. Если же вызывать в тестах только обработчики напрямую, ты никогда не проверишь, может ли приложение предоставить им зависимости.

[Testcontainers for .NET](https://dotnet.testcontainers.org/) управляет контейнерами с зависимостями на время тестов. Для работы нужна среда запуска контейнеров, совместимая с Docker API. Настоящий движок нужен, если ошибка зависит от перевода запросов в SQL, миграций схемы или сохранения данных между операциями. Не добавляй в P1 реляционную базу только ради демонстрации библиотеки. Подключай контейнерные тесты, когда у приложения появится соответствующая зависимость и для неё будет доступен подходящий образ или эмулятор. Тесты на уровне [Aspire AppHost](https://aspire.dev/testing/write-your-first-test/) разбираются в уроке II.7 «Контейнеры и Aspire».

Код подготовки теста должен управлять всем жизненным циклом контейнера: запустить его, дождаться готовности сервиса, передать приложению параметры подключения, загрузить известные данные, выполнить проверки и освободить ресурсы. В [рекомендациях Testcontainers](https://dotnet.testcontainers.org/api/best_practices/) советуют фиксировать версии образов и назначать порты хоста динамически. При фиксированных портах параллельные тесты конкурируют за один адрес. Общие изменяемые данные делают результат зависимым от порядка запуска. Изолируй данные каждого теста или явно определи, когда сбрасывать состояние, даже если ради скорости тесты используют один контейнер.

Даже если контейнер запущен, сервис ещё может быть не готов принимать запросы. Выбирай подходящую [стратегию ожидания](https://dotnet.testcontainers.org/api/wait_strategies/), а не произвольную паузу. Локальный тест проверяет только тот компонент, который находится в контейнере: другой поисковый движок не докажет совместимость с Azure AI Search. Аналогично HTTP-тест внутри процесса не проверит, есть ли у управляемого удостоверения (managed identity) право вызвать развёрнутый сервис.

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

P1 будет искать по документам из открытых источников, обращаться к развёртыванию модели (model deployment) в Foundry и возвращать ссылки на источники. Определи в приложении собственный интерфейс клиента модели: тогда в тестах можно возвращать фиксированные ответы, записывать переданный модели контекст и имитировать сбои. Сделай так, чтобы поиск можно было подменять независимо от клиента модели. Иначе даже после замены клиента модели обычные тесты API могут по-прежнему зависеть от работающего поискового индекса.

В упражнении эту роль выполняет намеренно минимальный интерфейс `IModelClient`. В уроке II.8 «AI в .NET» появится [`IChatClient`](https://learn.microsoft.com/ru-ru/dotnet/ai/ichatclient) из `Microsoft.Extensions.AI`; к нему применим тот же способ подмены зависимости.

Проверяй то, чем приложение управляет. Если известен идентификатор документа, он должен попасть в ответ. Пустой вопрос должен отклоняться до вызова модели, а допустимый — доходить до неё без изменений. Для фиксированного ответа тестовой реализации полезно точное сравнение строк. Оно не доказывает, что настоящая модель ответит теми же словами или даст верный ответ.

Идентификатор источника в ответе подтверждает, что API сохранило ссылку, но не доказывает, что ответ действительно опирается на указанный фрагмент. Проверки качества поиска и генерации разбираются в уроке [Evaluation](/rag-agents/part-1-rag/cross-cutting/evaluation/). После изменения промпта, настроек поиска или версии модели запускай оценку качества наряду с тестами приложения. Урок AI SDLC [«Многослойные проверки и разнообразие механизмов»](/ai-sdlc/part-3-verification/layered-gates/) объясняет, зачем сочетать проверки, которые обнаруживают разные виды ошибок.

По мере развития P1 добавляй случаи с управляемыми сбоями модели и отменой операций. Тестовая реализация, которая выбрасывает исключение по тайм-ауту, позволит проверить, как API отвечает на сбой, не дожидаясь настоящего простоя. Реализация с поддержкой отмены может записать, дошёл ли сигнал отмены до зависимости. Сначала определи нужное поведение сервиса, затем закрепи его тестом. Проверяй соблюдение контракта сервиса, а не случайную формулировку исключения. Тесты, которые обращаются к настоящим сервисам, держи отдельно: тогда ты не примешь проблему с учётными данными (credentials) за ошибку в правилах валидации.

## Попробуй \{#try-it}

Собери локальную часть P1: `/ask`, фиксированный документ и интеграционный тест, который заменяет клиент модели. Здесь поиск представлен тестовыми данными; Azure AI Search и адаптер Foundry появятся позже. В будущем сервисе ты сможешь включать в тест те же компоненты и подменять клиент модели тем же способом.

**Статус проверки:** команды и код в приведённом виде запускались 17.10.2026 с .NET SDK 10.0.402, `Microsoft.AspNetCore.Mvc.Testing` 10.0.13, `Microsoft.NET.Test.Sdk` 18.11.0, `xunit` 2.9.3, `xunit.runner.visualstudio` 4.0.1 и `coverlet.collector` 10.1.0. Сборка прошла без предупреждений, `dotnet test` успешно выполнил все три случая. Когда идентификатор источника в ответе заменили с `doc-1` на `doc-2`, тест успешного запроса перестал проходить; ниже ты повторишь эту проверку. Упражнение выполнялось только локально, без подписки Azure и обращений к работающим облачным сервисам.

Установи .NET 10 SDK и начни в новом рабочем каталоге вне существующего решения. Для упражнения понадобятся встроенные [шаблоны SDK](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new-sdk-templates) и команды для работы с [решением](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-sln), [ссылками на проекты](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-reference-add) и [пакетами](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-package-add).

Упражнение рассчитано на .NET 10 SDK. Прямые зависимости закреплены на последних стабильных версиях соответствующих пакетов на дату проверки: [`Microsoft.AspNetCore.Mvc.Testing` 10.0.13](https://www.nuget.org/packages/Microsoft.AspNetCore.Mvc.Testing), [`Microsoft.NET.Test.Sdk` 18.11.0](https://www.nuget.org/packages/Microsoft.NET.Test.Sdk/), [`xunit` 2.9.3](https://www.nuget.org/packages/xunit), [`xunit.runner.visualstudio` 4.0.1](https://www.nuget.org/packages/xunit.runner.visualstudio) и [`coverlet.collector` 10.1.0](https://www.nuget.org/packages/coverlet.collector). Сохраняется пакет `xunit` v2 из шаблона, хотя NuGet уже помечает его как устаревший; xUnit v3 выпускается отдельным пакетом. Команды ниже обновляют ссылки на пакеты, созданные шаблоном, и добавляют пакет для тестового хоста.

```bash
mkdir p1-testing
cd p1-testing
dotnet new sln -n P1Testing
dotnet new web -n Rag.Api --framework net10.0
dotnet new xunit -n Rag.Api.Tests --framework net10.0
dotnet sln add Rag.Api/Rag.Api.csproj Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet reference add Rag.Api/Rag.Api.csproj --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add Microsoft.AspNetCore.Mvc.Testing --version 10.0.13 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add Microsoft.NET.Test.Sdk --version 18.11.0 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add xunit --version 2.9.3 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add xunit.runner.visualstudio --version 4.0.1 --project Rag.Api.Tests/Rag.Api.Tests.csproj
dotnet package add coverlet.collector --version 10.1.0 --project Rag.Api.Tests/Rag.Api.Tests.csproj
```

В `Rag.Api.Tests/Rag.Api.Tests.csproj` измени атрибут `Sdk` открывающего элемента на `Microsoft.NET.Sdk.Web`, как указано в [требованиях к тестовому проекту](https://learn.microsoft.com/ru-ru/aspnet/core/test/integration-tests?view=aspnetcore-10.0#test-app-prerequisites).

Замени содержимое `Rag.Api/Program.cs` кодом ниже. Документ вымышленный и используется только как локальная тестовая фикстура. Ненастроенный клиент модели выбрасывает исключение при вызове, поэтому тест обязан его заменить. Когда появится настоящий адаптер, подключи его через тот же интерфейс. Обработчик использует документированную [привязку тела запроса, сервиса и токена отмены](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/minimal-apis/parameter-binding?view=aspnetcore-10.0).

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<IModelClient, UnconfiguredModelClient>();
var app = builder.Build();

app.MapPost("/ask", async (AskRequest request, IModelClient model,
    CancellationToken cancellationToken) =>
{
    if (string.IsNullOrWhiteSpace(request.Question))
        return Results.BadRequest();

    const string context = "[doc-1] This public sample describes the RAG service.";
    var answer = await model.GenerateAsync(
        request.Question, context, cancellationToken);
    return Results.Ok(new AskResponse(answer, ["doc-1"]));
});
app.Run();

public record AskRequest(string? Question);
public record AskResponse(string Answer, string[] Citations);
public interface IModelClient
{
    Task<string> GenerateAsync(string question, string context,
        CancellationToken cancellationToken);
}
public sealed class UnconfiguredModelClient : IModelClient
{
    public Task<string> GenerateAsync(string question, string context,
        CancellationToken cancellationToken) =>
        throw new InvalidOperationException("Configure a model adapter.");
}
```

В .NET 10 [публичное объявление `Program` генерируется автоматически](https://learn.microsoft.com/ru-ru/aspnet/core/release-notes/aspnetcore-10.0?view=aspnetcore-10.0#better-support-for-testing-apps-with-top-level-statements); добавлять его вручную не нужно. Удали сгенерированный `Rag.Api.Tests/UnitTest1.cs` и создай `Rag.Api.Tests/AskTests.cs` со следующим содержимым. Настройка тестового хоста сначала удаляет исходную регистрацию клиента модели, затем добавляет тестовую реализацию. Обе фабрики — базовая и настроенная — освобождаются благодаря объявлениям `using`.

```csharp
using System.Net;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.AspNetCore.TestHost;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;
using Xunit;

namespace Rag.Api.Tests;

public sealed class AskTests
{
    [Fact]
    public async Task Ask_returns_answer_and_citation()
    {
        var fake = new FakeModelClient();
        using var baseFactory = new WebApplicationFactory<Program>();
        using var factory = CreateFactory(baseFactory, fake);
        using var client = factory.CreateClient();
        using var response = await client.PostAsJsonAsync(
            "/ask", new AskRequest("What does the sample describe?"));

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        var body = await response.Content.ReadFromJsonAsync<AskResponse>();
        Assert.NotNull(body);
        Assert.Equal("Fixed test answer.", body.Answer);
        Assert.Equal("doc-1", Assert.Single(body.Citations));
        Assert.Equal("What does the sample describe?", fake.Question);
        Assert.Equal(
            "[doc-1] This public sample describes the RAG service.", fake.Context);
    }

    [Theory]
    [InlineData("")]
    [InlineData("   ")]
    public async Task Ask_rejects_blank_question(string question)
    {
        var fake = new FakeModelClient();
        using var baseFactory = new WebApplicationFactory<Program>();
        using var factory = CreateFactory(baseFactory, fake);
        using var client = factory.CreateClient();
        using var response = await client.PostAsJsonAsync(
            "/ask", new AskRequest(question));

        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
        Assert.Null(fake.Question);
    }

    private static WebApplicationFactory<Program> CreateFactory(
        WebApplicationFactory<Program> baseFactory, FakeModelClient fake) =>
        baseFactory.WithWebHostBuilder(builder =>
            builder.ConfigureTestServices(services =>
            {
                services.RemoveAll<IModelClient>();
                services.AddSingleton<IModelClient>(fake);
            }));

    private sealed class FakeModelClient : IModelClient
    {
        public string? Question { get; private set; }
        public string? Context { get; private set; }

        public Task<string> GenerateAsync(string question, string context,
            CancellationToken cancellationToken)
        {
            cancellationToken.ThrowIfCancellationRequested();
            Question = question;
            Context = context;
            return Task.FromResult("Fixed test answer.");
        }
    }
}
```

Из каталога `p1-testing` запусти [`dotnet test`](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-test):

```bash
dotnet test Rag.Api.Tests/Rag.Api.Tests.csproj
```

Команда должна собрать проекты и выполнить три случая: один успешный запрос и два варианта пустого вопроса. В первом случае ожидаются HTTP 200, фиксированный ответ и ссылка `doc-1`; в остальных — HTTP 400 без вызова модели.

Временно замени в обработчике идентификатор источника на `doc-2`. Тест успешного запроса должен перестать проходить: так ты убедишься, что проверки замечают отклонение от заявленного поведения. После этого верни исходный идентификатор.

**Стоимость:** бесплатно, без ресурсов Azure. Сервер внутри процесса и тестовая реализация модели позволяют обойтись без среды запуска контейнеров, учётных данных Azure и платных вызовов модели.

**Удаление ресурсов:** после упражнения удали локальный каталог `p1-testing`. В Azure удалять нечего: упражнение не создаёт облачных ресурсов.

## Что перенести в свою практику \{#what-to-take-away}

- Проверяй повторяемые правила приложения модульными тестами, а взаимодействие компонентов через HTTP — несколькими целевыми интеграционными тестами.
- Подменяй клиент модели через тестовый хост. Проверяй и ответы приложения, и данные, переданные клиенту модели.
- Используй Testcontainers для тех настоящих зависимостей, которые нужны приложению. Изолируй данные и явно проверяй готовность сервиса.
- Тест с подменённой моделью подтверждает поведение приложения. Качество настоящих ответов и их опору на указанные источники проверяй с помощью оценки качества.

**[Новые термины](../glossary.md#testing)**: модульный тест, интеграционный тест, xUnit, тестовый двойник, упрощённая тестовая реализация, WebApplicationFactory, TestServer, Testcontainers, тестовая фикстура.

## Источники \{#sources}

Проверено на 17.10.2026.

- [Политика поддержки .NET](https://dotnet.microsoft.com/en-us/platform/support/policy)
- [Модульное тестирование C# с xUnit](https://learn.microsoft.com/ru-ru/dotnet/core/testing/unit-testing-csharp-with-xunit)
- [Интеграционные тесты в ASP.NET Core 10](https://learn.microsoft.com/ru-ru/aspnet/core/test/integration-tests?view=aspnetcore-10.0)
- [ASP.NET Core 10: тестирование приложений с инструкциями верхнего уровня](https://learn.microsoft.com/ru-ru/aspnet/core/release-notes/aspnetcore-10.0?view=aspnetcore-10.0#better-support-for-testing-apps-with-top-level-statements); [ASP0027: избыточное публичное объявление Program](https://learn.microsoft.com/ru-ru/aspnet/core/diagnostics/asp0027?view=aspnetcore-10.0)
- [Привязка параметров в минимальных API](https://learn.microsoft.com/ru-ru/aspnet/core/fundamentals/minimal-apis/parameter-binding?view=aspnetcore-10.0)
- .NET CLI: [new](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new), [шаблоны SDK](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-new-sdk-templates), [sln](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-sln), [reference add](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-reference-add), [package add](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-package-add), [test](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-test)
- [Пакет Microsoft.AspNetCore.Mvc.Testing](https://www.nuget.org/packages/Microsoft.AspNetCore.Mvc.Testing)
- Пакеты для тестирования: [Microsoft.NET.Test.Sdk](https://www.nuget.org/packages/Microsoft.NET.Test.Sdk/), [xunit](https://www.nuget.org/packages/xunit), [xunit.runner.visualstudio](https://www.nuget.org/packages/xunit.runner.visualstudio), [coverlet.collector](https://www.nuget.org/packages/coverlet.collector)
- [Абстракция IChatClient](https://learn.microsoft.com/ru-ru/dotnet/ai/ichatclient); [Aspire: первый тест](https://aspire.dev/testing/write-your-first-test/)
- [Testcontainers for .NET](https://dotnet.testcontainers.org/), [рекомендации](https://dotnet.testcontainers.org/api/best_practices/), [стратегии ожидания](https://dotnet.testcontainers.org/api/wait_strategies/)
