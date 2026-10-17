---
title: Агенты для программирования в .NET-проекте
sidebar_position: 2
last_verified: 2026-10-17
---

# Агент предлагает изменения, ты проверяешь и решаешь, принимать ли их

Код после правки может компилироваться и всё равно возвращать выдуманную ссылку на источник. А если агент удалит проверку, которая обнаруживала дефект, тест перестанет сообщать о проблеме. Такое бывает и с кодом, написанным человеком. Но когда агент за один проход меняет реализацию и тесты, критерий приёмки нужно задать независимо от этого прохода.

В этом уроке ты поручишь агенту ограниченную задачу для RAG-сервиса P1: задашь объём изменений, передашь правила репозитория и команды проверок, а затем изучишь результаты запусков и diff. Azure здесь — платформа для развёртывания приложения. Для работы над кодом агенту не нужен доступ к развёрнутому сервису. Подписка Azure также не даёт доступа к агенту: его доступность отдельно определяют тариф клиента и правила репозитория.

## Как это работает в Azure \{#how-it-works-on-azure}

В Visual Studio **режим агента (agent mode)** позволяет GitHub Copilot изучать код, редактировать файлы, вызывать инструменты и команды терминала, читать их результаты и продолжать работу. Ты остаёшься в IDE, пока агент, например, читает обработчик запроса, меняет тест, запускает его, разбирает ошибку, исправляет обработчик и повторяет запуск. Этот цикл действий описан в [документации режима агента Visual Studio](https://learn.microsoft.com/ru-ru/visualstudio/ide/copilot-agent-mode?view=visualstudio).

Для удалённой работы GitHub использует название **Copilot cloud agent**. Он работает с репозиторием на GitHub во временной среде разработки, может подготовить изменения в ветке и открыть pull request. В момент [выхода в общую доступность в сентябре 2025 года](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/) этот агент назывался Copilot coding agent; текущее название приведено в [документации GitHub](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github). В упражнении ниже используется режим агента в IDE. Отдельный вариант Visual Studio **Agent (Preview)** имеет собственный статус предварительной версии — общая доступность облачного агента его не меняет. См. [заметки о выпуске Visual Studio](https://learn.microsoft.com/ru-ru/visualstudio/releases/2026/release-notes).

**Пользовательские инструкции репозитория (repository custom instructions)** передают контекст проекта и агенту в IDE, и удалённому агенту. Visual Studio поддерживает общий файл `.github/copilot-instructions.md` и **инструкции для файлов по шаблону пути (path-specific instructions)** в файлах `.github/instructions/*.instructions.md`. В последних свойство `applyTo` выбирает файлы по glob-шаблонам. Общие команды проверок держи в файле репозитория, а отдельные инструкции заводи там, где правила действительно различаются. Форматы описаны в [документации Visual Studio](https://learn.microsoft.com/ru-ru/visualstudio/ide/copilot-chat-context?view=visualstudio). Прежде чем рассчитывать на те же файлы в другом клиенте, проверь [таблицу поддержки инструкций](https://docs.github.com/en/copilot/reference/custom-instructions-support).

Через **Model Context Protocol (MCP)** AI-клиент получает доступ к инструментам и контексту, которые предоставляет сервер. Режим агента в Visual Studio может использовать выбранные инструменты **MCP-сервера (MCP server)** — локального процесса или удалённого сервиса. См. [поддержку MCP в Visual Studio](https://learn.microsoft.com/ru-ru/visualstudio/ide/mcp-servers?view=visualstudio). Например, [Microsoft Learn MCP server](https://learn.microsoft.com/ru-ru/training/support/mcp) по адресу `https://learn.microsoft.com/api/mcp` позволяет искать документацию, получать страницы целиком и находить примеры кода. Через него агент обращается к документации; корректность внесённых правок этим не проверяется.

## Как выбрать способ работы \{#choosing-and-tradeoffs}

Режим агента в IDE удобен, когда задачу приходится часто уточнять или нужно смотреть промежуточные изменения. Удалённая работа подходит для асинхронной задачи, если её исходные данные и критерии приёмки уже есть в репозитории. Когда локальный запуск зависит от файла на ноутбуке, о котором нигде не сказано, агент не сможет воспроизвести такой запуск. Удалённая среда выявляет такие пробелы в подготовке проекта. Прежде чем поручать удалённому агенту большую задачу, разберись с нерешёнными вопросами архитектуры и настройки окружения.

Если для диагностики нужно оставить файлы без изменений, выбери режим только для чтения и отключи инструменты редактирования. Агент в терминале тоже подходит не для каждой задачи: ему могут быть недоступны нужные средства IDE или платформы. Выбирай среду, в которой можно получить требуемые результаты проверок.

В той же рабочей копии можно использовать агента из терминала. [Руководство по подключению Microsoft Learn MCP](https://learn.microsoft.com/ru-ru/training/support/mcp-get-started) включает GitHub Copilot CLI и Claude Code. При выборе учитывай доступ к репозиторию, разрешения инструментов и возможность запустить проверки. Поддержка одного протокола MCP не означает, что клиенты одинаково находят и загружают инструкции проекта.

Команды терминала в Visual Studio выполняются с правами процесса Visual Studio. Открытое решение само по себе не изолирует агента от остальной файловой системы. Изучай запросы на подтверждение вызовов инструментов, прежде чем разрешать автоматический запуск дополнительных инструментов; поведение описано в [документации режима агента](https://learn.microsoft.com/ru-ru/visualstudio/ide/copilot-agent-mode?view=visualstudio). Предоставь серверу для поиска документации доступ к документации, а учётные данные прода не передавай в задачу разработки.

Инструкции подсказывают агенту нужную команду, но не могут обеспечить успешный результат или запретить разрешённому инструменту переписать тест. Это различие разбирается в уроке [«Правила, которые нельзя обойти»](/ai-sdlc/part-1-foundation/rules-that-hold). Поэтому команды сборки, тестирования и проверки форматирования должны выполняться и в CI, помимо их перечисления в инструкциях.

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

P1 — API на ASP.NET Core, которое отвечает на вопросы и указывает источники. В целевой архитектуре оно обращается к модели в Foundry и к Azure AI Search через управляемое удостоверение (managed identity); для развёртывания используется OIDC. Здесь ты изменишь контракт API для проверки ссылок на источники. Развёрнутый сервис для этого упражнения не нужен.

Разделяй доступ агента к среде разработки, управляемое удостоверение работающего приложения и удостоверение, которое рабочий процесс развёртывания получает через OIDC. Чтобы добавить проверку ссылок на источники, агенту не нужна роль в проде. Применяй рекомендации уроков [«Секреты»](/ai-sdlc/part-4-platform/secrets) и [«Наименьшие привилегии и песочница»](/ai-sdlc/part-4-platform/least-privilege-sandboxing) к инструментам и учётным данным этой задачи.

Метод разработки описан в курсе [AI SDLC](/ai-sdlc/): используй цикл из урока [«План, проверка, реализация, критик»](/ai-sdlc/part-2-loop/plan-review-implement-critic) и подход из урока [«Многослойные проверки и разнообразие механизмов»](/ai-sdlc/part-3-verification/layered-gates). Детерминированный тест может установить, что ID указанного документа входит в набор, полученный при поиске. Но он не определяет, подтверждает ли текст документа ответ модели. Если меняешь поиск, промпт или модель, нужна ещё и [оценка качества ответов](/rag-agents/part-1-rag/cross-cutting/evaluation).

## Попробуй \{#try-it}

Продолжи работу с отдельной тестовой фикстурой (test fixture) `P1Testing.slnx` из упражнения в уроке [«Тестирование»](../part-2-modern-dotnet/testing.md). Сохрани версии пакетов и уже закреплённую версию SDK. Нужен .NET 10 SDK; для работы в Visual Studio — Visual Studio 2026 версии 18.0 или новее и [поддерживаемая версия Windows](https://learn.microsoft.com/ru-ru/visualstudio/releases/2026/vs-system-requirements). Согласно [таблице совместимости SDK и Visual Studio](https://learn.microsoft.com/ru-ru/dotnet/core/porting/versioning-sdk-msbuild-vs#targeting-and-support-rules), поддерживаемая сборка под `net10.0` требует Visual Studio 18.0 или новее. Выбери совместимую пару SDK и IDE. В другой среде используй GitHub Copilot CLI, Claude Code или сопоставимый клиент в терминале с установленным SDK; настрой поддерживаемые им инструкции по руководству выше.

Работай в ветке репозитория на GitHub, поместив фикстуру в его корень. До передачи задачи агенту выполни всю последовательность проверок из блока инструкций ниже. Уже имеющиеся расхождения форматирования устрани отдельно. Если `global.json` нет, добавь его и укажи в `sdk.version` точную установленную версию .NET 10 SDK из вывода [`dotnet --version`](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet#options). Уже закреплённую совместимую версию сохрани; [правила выбора SDK](https://learn.microsoft.com/ru-ru/dotnet/core/tools/global-json) должны действовать локально и в CI. Для форматирования используй `.editorconfig`, если он есть, иначе — настройки форматтера по умолчанию. Если тесты входят в решение P1 с другим именем, замени имя решения одновременно в инструкциях и CI.

**Статус проверки:** команды сверены с актуальными справочниками CLI 18.10.2026. Упражнение целиком и рабочий процесс CI ещё не запускались. Подписки Azure пока нет; команды здесь не выполнялись в действующей подписке. Ожидаемые результаты предполагают, что предыдущие упражнения выполнены, а необходимые средства разработки установлены.

В редакторе создай `.github/copilot-instructions.md` в корне репозитория с фикстурой:

```markdown
# P1 development instructions

Work from the repository root. Keep changes within the requested task.
Preserve package pins and any existing SDK pin in global.json.
Use .editorconfig as the style authority where present; otherwise use formatter defaults.
Do not remove or weaken tests to obtain a passing result.
Do not change dependencies, infrastructure or CI without a separate requirement.

Validation commands, in order:
- Restore: `dotnet restore P1Testing.slnx`
- Build: `dotnet build P1Testing.slnx --configuration Release --no-restore`
- Test (VSTest): `dotnet test P1Testing.slnx --configuration Release --no-build`
- Style: `dotnet format P1Testing.slnx --verify-no-changes --no-restore`

Report command exit statuses, discovered test counts and any checks not run.
Explain the behaviour changed and identify the tests that demonstrate it.
```

Команды соответствуют документированным интерфейсам [restore](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-restore), [build](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-build), [test с VSTest](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-test-vstest) и [format](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-format). В Visual Studio включи загрузку инструкций репозитория. Прежде чем полагаться на них, убедись, что файл появился в списке **References** ответа.

До передачи задачи добавь в этот же репозиторий файл `.github/workflows/p1-checks.yml` по [примеру CI для .NET](https://docs.github.com/en/actions/tutorials/build-and-test-code/net):

```yaml
name: P1 checks
on: [pull_request]
permissions:
  contents: read
jobs:
  p1-checks:
    name: P1 checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - uses: actions/setup-dotnet@2016bd2012dba4e32de620c46fe006a3ac9f0602 # v5.0.1
        with:
          global-json-file: global.json
      - run: dotnet restore P1Testing.slnx
      - run: dotnet build P1Testing.slnx --configuration Release --no-restore
      - run: dotnet test P1Testing.slnx --configuration Release --no-build
      - run: dotnet format P1Testing.slnx --verify-no-changes --no-restore
```

В рабочем процессе [checkout v7.0.1](https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1) и [setup-dotnet v5.0.1](https://github.com/actions/setup-dotnet/releases/tag/v5.0.1) привязаны к конкретным коммитам по SHA. Версию SDK для установки setup-dotnet берёт из `global.json`, указанного в параметре [`global-json-file`](https://github.com/actions/setup-dotnet/blob/v5.0.1/README.md#using-the-global-json-file-input). Событие запуска, исполнитель и разрешения токена заданы по [синтаксису GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax). Рабочий процесс выполняет те же четыре проверки, без развёртывания приложения.

Открой pull request с исходной настройкой и убедись, что `P1 checks` проходит. Проверь изменения и влей pull request, затем создай новую ветку для задачи о ссылках на источники. Файл CI должен остаться за пределами правок агента. Если настройки репозитория позволяют, сделай этот рабочий процесс [обязательной проверкой статуса](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging).

Передай задание через настроенный режим агента в Visual Studio или клиент в терминале. Если хочешь поручить задачу удалённому агенту, создай её на GitHub и назначь через интерфейс Copilot cloud agent, если это разрешают тариф, репозиторий и правила организации:

> Добавь новое правило проверки ссылок на источники в `/ask`. Существующий интерфейс модели возвращает обычный текст. Упрощённая тестовая реализация (fake) для успешного случая должна по-прежнему возвращать `Fixed test answer.`. В ответе API сохрани ссылку на источник `doc-1`.
> В этом упражнении считай встроенные в текст маркеры `[doc-N]`, где N — положительное целое число, идентификаторами документов. Проверяй каждый такой маркер по ID в найденном контексте, переданном модели. Если хотя бы один маркер указывает на отсутствующий ID, возвращай HTTP 502 с пустым телом ответа.
>
> Сначала добавь HTTP-тест, который не проходит: оставь в контексте только `[doc-1]`, а тестовая реализация модели пусть возвращает `Unsupported answer [doc-2].`. Проверь статус и пустое тело ответа. Добавь положительный случай: ответ с `[doc-1]` должен по-прежнему давать HTTP 200. В смешанном случае ответ содержит и `[doc-1]`, и `[doc-2]`; результат должен быть HTTP 502 с пустым телом. Сохрани все существующие тесты.
> Остановись и покажи вывод не прошедшего теста для ревью. Только после ревью внеси минимальное исправление. Не ослабляй условия, которые проверяют тесты, и не меняй пакеты или CI.

Это новый критерий приёмки: в предыдущем упражнении такая проверка ещё не требовалась. Допустимые ID нужно получать из контекста тестовой фикстуры. Запрет конкретной строки `doc-2` или проверка жёстко заданного массива ссылок в ответе не выполняют требование. В будущем структурированный ответ модели может заменить встроенные маркеры, но изменение интерфейса не входит в эту правку.

Прежде чем разрешать реализацию, разбери вывод первого запуска, в котором новый тест завершился ошибкой. После исправления выполни всю последовательность команд и изучи diff. Убедись по выводу, что обнаружены и старые, и новые тесты: одного кода завершения команды недостаточно, чтобы это подтвердить. Открой pull request с задачей и добейся успешного `P1 checks` для текущей версии изменений. После последующих правок повтори запуск.

Сохрани вместе с задачей URL запуска CI, SHA проверенного коммита и вывод об обнаруженных тестах. Приложи также вывод первого запуска, в котором новый тест завершился ошибкой. Для завершения упражнения нужны и локальные результаты, и подтверждение из CI. Разбери журналы запуска и условия, которые проверяют тесты, чтобы оценить результат; краткий отчёт агента не заменяет эти сведения.

Для pull request от удалённого агента проверь правки в рабочем процессе CI, прежде чем одобрять запуск. По умолчанию GitHub [требует такого одобрения](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations), но автоматический запуск можно настроить. Не рассчитывай, что во всех репозиториях выполнение обязательно приостановится.

**Стоимость:** редактирование кода и локальные проверки не создают ресурсов Azure. [Microsoft Learn MCP server](https://learn.microsoft.com/ru-ru/training/support/mcp) не требует аутентификации и предоставляется бесплатно. На использование агента распространяются [AI-кредиты и квоты тарифа](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing). Удалённая работа облачного агента также расходует [минуты GitHub Actions](https://docs.github.com/en/copilot/tutorials/cloud-agent/pilot-cloud-agent). На запуски рабочего процесса для pull request распространяются [правила оплаты Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions).

**Удаление ресурсов:** сохрани проверенные инструкции, тесты, закреплённую версию SDK и рабочий процесс CI, которые планируешь использовать дальше. После завершения можешь закрыть одноразовые pull request и удалить рабочие копии репозитория, созданные для этих задач. Удалять ресурсы Azure в этом упражнении не требуется.

## Что перенести в свою практику \{#what-to-take-away}

- Выбирай локальную или удалённую работу по контексту задачи, необходимым разрешениям и возможности воспроизвести результат.
- Храни полезные инструкции в системе контроля версий. Проверяй соблюдение требований к сборке, тестам и стилю с помощью исполняемых проверок.
- Разделяй доступ агента для программирования, удостоверение приложения и удостоверение развёртывания.
- Детерминированно проверяй, что ID указанных источников есть среди ID найденных документов. Отдельно оценивай, подтверждает ли текст этих источников ответ.

**[Новые термины](../glossary.md#coding-agents-dotnet)**: режим агента, Copilot cloud agent, пользовательские инструкции репозитория, инструкции для файлов по шаблону пути, MCP-сервер.

## Источники \{#sources}

Проверено на 17.10.2026. Уточнённые утверждения и команды повторно проверены 18.10.2026.

- Visual Studio: [agent mode](https://learn.microsoft.com/ru-ru/visualstudio/ide/copilot-agent-mode?view=visualstudio), [release notes](https://learn.microsoft.com/ru-ru/visualstudio/releases/2026/release-notes), [custom instructions](https://learn.microsoft.com/ru-ru/visualstudio/ide/copilot-chat-context?view=visualstudio), [MCP servers](https://learn.microsoft.com/ru-ru/visualstudio/ide/mcp-servers?view=visualstudio).
- GitHub: [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github), [coding agent GA announcement](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/), [custom instruction support](https://docs.github.com/en/copilot/reference/custom-instructions-support).
- Microsoft Learn MCP: [server capabilities, access and cost](https://learn.microsoft.com/ru-ru/training/support/mcp), [client setup](https://learn.microsoft.com/ru-ru/training/support/mcp-get-started).
- GitHub: [agent risks and mitigations](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations), [Copilot billing](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing), [cloud-agent pilot and Actions usage](https://docs.github.com/en/copilot/tutorials/cloud-agent/pilot-cloud-agent).
- .NET CLI: [restore](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-restore), [build](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-build), [test with VSTest](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-test-vstest), [format](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet-format).
- .NET prerequisites: [Visual Studio system requirements](https://learn.microsoft.com/ru-ru/visualstudio/releases/2026/vs-system-requirements), [SDK/Visual Studio support matrix](https://learn.microsoft.com/ru-ru/dotnet/core/porting/versioning-sdk-msbuild-vs), [SDK selection with global.json](https://learn.microsoft.com/ru-ru/dotnet/core/tools/global-json), [dotnet options](https://learn.microsoft.com/ru-ru/dotnet/core/tools/dotnet).
- CI: [.NET build/test pattern](https://docs.github.com/en/actions/tutorials/build-and-test-code/net), [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [required checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [checkout pin](https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1), [setup-dotnet v5.0.1](https://github.com/actions/setup-dotnet/releases/tag/v5.0.1), [SDK setup input](https://github.com/actions/setup-dotnet/blob/v5.0.1/README.md#using-the-global-json-file-input), [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).
