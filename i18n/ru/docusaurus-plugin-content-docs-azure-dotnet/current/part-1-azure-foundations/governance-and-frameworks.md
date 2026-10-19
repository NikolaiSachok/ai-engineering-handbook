---
title: Правила использования платформы и архитектурные рекомендации
sidebar_position: 11
last_verified: 2026-10-17
---

# Сервис работает. Соблюдены ли требования организации?

Сервис отвечает на запросы, развёртывание прошло успешно, но неизвестно, кто несёт ответственность за расходы. В другом окружении документы хранятся там, где организация не разрешала их размещать. Обе системы работают в том виде, в котором их развернули. Не хватает механизма, который обеспечивал бы соблюдение общих требований при каждом развёртывании, в том числе при изменениях в обход обычного конвейера.

Некоторые требования можно проверить автоматически: есть ли тег (tag) `owner`, используется ли разрешённое расположение. Другие требуют архитектурного решения: какой простой допустим, какие зависимости должны восстанавливаться вместе, сколько можно платить за ответ. Поэтому нужны и исполняемые правила конфигурации, и рекомендации по проектированию, и ответственный, который примет меры по результатам проверок правил и архитектурного ревью.

## Как это работает в Azure \{#how-it-works-on-azure}

В [уроке 1](./how-azure-is-organised.md#how-it-works-on-azure) разобрана разница между правом выполнить операцию и требованиями к конфигурации ресурса. [Azure Policy](https://learn.microsoft.com/ru-ru/azure/governance/policy/overview) превращает такие требования в исполняемые правила.

**Определение политики (policy definition)** содержит условие и действие при его выполнении — эффект политики (policy effect). С параметрами одно правило можно использовать в разных окружениях: например, в одном требовать тег `owner`, в другом — `costCentre`. Структура описана в [документации определений](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/definition-structure-basics).

**Назначение политики (policy assignment)** связывает определение с областью действия (scope) и задаёт значения параметров. Чтобы назначать вместе несколько определений с общей целью, объедини их в **инициативу политик (policy initiative)**. Её также называют набором политик (policy set). См. [структуру инициативы](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/initiative-definition-structure).

Назначение на группу ресурсов (resource group) распространяется на ресурсы внутри неё, к которым применимо правило. Назначение на подписку (subscription) или группу управления (management group) распространяется на нижележащие уровни иерархии. После проверки Azure сообщает **состояние соответствия (compliance state)**: удовлетворяет ли проверенный ресурс назначенному правилу.

Когда условие выполнено, дальнейшее действие зависит от [эффекта политики](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-basics). Для правил конфигурации доступны, например, следующие эффекты:

| Эффект | Что происходит | О чём легко забыть |
|---|---|---|
| [`audit`](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-audit) | Фиксирует несоответствие, но разрешает запрос. | Обнаружить нарушение ещё не значит предотвратить его. |
| [`deny`](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-deny) | Отклоняет нарушающий правило запрос на создание или обновление, если применение эффекта включено. | Существующие ресурсы не удаляются и не исправляются. |
| [`modify`](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-modify) | Добавляет, обновляет или удаляет поддерживаемые свойства либо теги. | Одна лишь проверка соответствия не меняет существующие ресурсы. |
| [`deployIfNotExists`](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-deploy-if-not-exists) | Развёртывает связанный ресурс, если он отсутствует или не соответствует условию политики. | При автоматическом развёртывании политика может создать ресурсы, за эксплуатацию которых никто не отвечает. |

Чтобы исправить существующие ресурсы с помощью `modify` или `deployIfNotExists`, нужна отдельная задача исправления (remediation task). Для этой работы используется управляемое удостоверение (managed identity), привязанное к назначению политики; ему нужны соответствующие разрешения. До включения таких изменений разберись, кто будет отвечать за инфраструктуру и её стоимость.

**Cloud Adoption Framework (CAF)** помогает организации осваивать Azure: подготовить среду, установить правила её использования и контролировать их соблюдение. [Рекомендации по целевым зонам (landing zones)](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ready/landing-zone/) описывают основу для размещения рабочих нагрузок. В платформенной целевой зоне (platform landing zone) сосредоточены общие сервисы и средства управления, а в целевых зонах приложений (application landing zones) — окружения рабочих нагрузок. При подготовке этой основы определяют, как будут устроены удостоверения, подписки, сети и безопасность.

Внутри такого окружения проектировать и разбирать конкретную рабочую нагрузку помогает [Well-Architected Framework](https://learn.microsoft.com/ru-ru/azure/well-architected/what-is-well-architected-framework). В нём пять направлений: надёжность (Reliability), безопасность (Security), оптимизация затрат (Cost Optimization), операционная эффективность (Operational Excellence) и эффективность производительности (Performance Efficiency). На ревью нужно выявить архитектурные компромиссы и превратить выводы в задачи по реализации.

Выбирая, какие ресурсы проверять на наличие тегов, опирайся на [набор тегов и правила наследования из урока 1](./how-azure-is-organised.md#how-it-works-on-azure). Если нужное значение можно однозначно получить по заданному правилу, для его установки подходит `modify`.

Разобраться в расходах поможет [анализ затрат в Cost Management](https://learn.microsoft.com/ru-ru/azure/cost-management-billing/costs/quick-acm-cost-analysis). Как настроить бюджет (budget) подписки и оповещения, описано в [объяснении бюджетов](./how-azure-is-organised.md#choosing-boundaries) и блоке [«Попробуй»](./how-azure-is-organised.md#try-it) первого урока.

[Microsoft Defender for Cloud](https://learn.microsoft.com/ru-ru/azure/defender-for-cloud/defender-for-cloud-introduction) формирует рекомендации по устранению недостатков конфигурации безопасности и защищает рабочие нагрузки от угроз в зависимости от включённых планов. **Управление состоянием безопасности облака (cloud security posture management, CSPM)** — это проверка конфигурации ресурсов на уязвимые места. [Foundational CSPM предоставляет бесплатные возможности, а план Defender CSPM добавляет платные](https://learn.microsoft.com/ru-ru/azure/defender-for-cloud/concept-cloud-security-posture-management). Прежде чем рассчитывать на защиту, проверь, какие планы включены. Назначь ответственного за выполнение каждой рекомендации и устраняй причину проблемы в коде инфраструктуры. [Secure score](https://learn.microsoft.com/ru-ru/azure/defender-for-cloud/secure-score-security-controls) обобщает рекомендации по безопасности в одном показателе.

## Как выбирать правила и учитывать компромиссы \{#choosing-and-tradeoffs}

Начни с требования, которое можешь объяснить, и области действия, которую можешь проверить. Для знакомства с одним правилом в P1 достаточно группы ресурсов. Если сразу назначить большую инициативу на подписку, не прочитав определения, можно задеть чужие эксперименты.

| Вариант | Когда подходит | Когда не стоит применять |
|---|---|---|
| Аудит или проверка без применения эффекта | Нужно понять последствия до блокировки запросов. | Нарушение требуется предотвращать сразу. |
| `deny` | Ограничение однозначно, а процесс развёртывания уже умеет его соблюдать. | Ещё неизвестны исключения и зависимости существующих развёртываний. |
| `modify` | Значение согласовано и выводится по правилу — например, общий тег проекта. | Платформе пришлось бы угадывать, кто настоящий владелец ресурса. |
| Развёртывание недостающих ресурсов | Есть стандартная конфигурация вспомогательного ресурса и ответственный за его эксплуатацию. | Ресурс продублирует инфраструктуру, которой уже управляет приложение. |
| Полная реализация целевой зоны | Нескольким рабочим нагрузкам нужна общая платформа с распределением ответственности. | Учебная задача ограничена одной группой ресурсов. |

Назначение с [`enforcementMode: DoNotEnforce`](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/assignment-structure#enforcement-mode) продолжает проверять соответствие, но не применяет эффект. Так ты сначала оценишь последствия правила. Эффект `disabled` вообще отключает проверку. Прежде чем выбирать способ введения правила, посмотри, какие эффекты поддерживает определение.

Наследование ограничивает и то, что можно исправить на уровне P1. Назначение политики, допускающее операцию в P1, не отменит `deny`, унаследованный от родительской области. Согласуй требование с владельцем платформы: потребуется изменить действующее назначение либо оформить допустимые исключения.

Даже полное соответствие конфигурации правилам не избавляет от архитектурных компромиссов. Копия данных для восстановления может повысить надёжность, но увеличит расходы и объём данных, которые нужно защищать. Дополнительная телеметрия помогает эксплуатации, однако для неё надо определить сроки хранения и права доступа. Записывай, какое требование оправдывает расходы и как ты проверишь его выполнение.

## Что это меняет для AI-сервиса \{#in-an-ai-workload}

В [P1](../part-5-projects/rag-service.md) используется минимальный API на ASP.NET Core в Container Apps: он отвечает на вопросы по общедоступным документам и указывает источники. В состав проекта входят развёртывание модели (model deployment) в [Microsoft Foundry](https://learn.microsoft.com/ru-ru/azure/foundry/what-is-foundry), Azure AI Search, Blob Storage, доступ к Key Vault через управляемое удостоверение и Application Insights. Создание ресурсов описывают Bicep и `azd`, а поставку — GitHub Actions с OIDC. На архитектурном ревью рассматривай все эти компоненты как одну рабочую нагрузку.

При проверке надёжности выясни, как восстановить поисковый индекс из исходных документов и что API возвращает при сбое генерации. Для проверки безопасности проследи, какие удостоверения используются и где проходят границы доступа к документам.

Разрешённый регион (region) ресурса ещё не определяет, где обрабатываются данные. Например, в P1 [назначение политики разрешённых расположений](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/definition-structure-basics#resource-manager-modes) может допускать регион ресурса Foundry, а при развёртывании Global Standard промпты и ответы [могут обрабатываться в разных регионах Azure](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/deployment-types#data-processing-locations). Зафиксируй в проекте P1 и допустимое расположение ресурса, и выбранные географические границы обработки. Выбору развёртывания посвящён урок [«Развёртывания моделей, квоты и стоимость»](../part-3-llms-on-azure/deployments-quotas-cost.md) Части III.

Оптимизация затрат начинается с измерения стоимости полезного ответа и ограничения повторных попыток и объёма вывода. Для проверки операционной эффективности выясни, сможешь ли ты по телеметрии разобраться, что произошло при поиске и генерации неудачного ответа. Проверь также, сможешь ли повторить развёртывание. Эффективность производительности требует сначала найти этап, на котором возникает задержка, и лишь затем наращивать мощности.

Разницу между рекомендацией и исполняемым правилом подробнее разбирает урок [«Правила, которые нельзя обойти»](/ai-sdlc/part-1-foundation/rules-that-hold). Вместе с Azure Policy сохраняй проверки самого приложения: [Evaluation](/rag-agents/part-1-rag/cross-cutting/evaluation/) — для качества поиска и ответов, [Guardrails](/rag-agents/part-1-rag/cross-cutting/guardrails/) — для работы с недоверенными входными и выходными данными. Соответствие конфигурации правилам не доказывает качество ответа: наличие тега `owner` ничего не говорит о том, подтверждает ли цитата ответ.

## Попробуй \{#try-it}

Назначь встроенную политику `Require a tag on resources` на новую учебную группу ресурсов, создай ресурс без тега и посмотри на результат проверки до включения эффекта. Так ты отработаешь правило P1 об обязательном теге владельца, не развёртывая сам P1.

Понадобятся Azure CLI и разрешения в подписке: создавать и удалять группы ресурсов и управляемые удостоверения, управлять назначениями политик и читать результаты проверки соответствия. Роль [`Resource Policy Contributor`](https://learn.microsoft.com/ru-ru/azure/role-based-access-control/built-in-roles/management-and-governance#resource-policy-contributor) даёт права для операций с политиками; для создания ресурсов нужны дополнительные разрешения.

**Для примеров курса пока нет подписки Azure. Команды сверены с актуальным справочником Azure CLI, но не выполнялись в действующей подписке. Ниже описаны ожидаемые результаты.**

Используй Bash и выполняй команды в одной оболочке, чтобы сохранить переменные. Выбери новое имя учебной группы и расположение, разрешённое политиками подписки. Войди, выбери подписку и создай группу. Описание команд — в справочниках [входа](https://learn.microsoft.com/ru-ru/cli/azure/reference-index?view=azure-cli-latest#az-login), [учётной записи](https://learn.microsoft.com/ru-ru/cli/azure/account?view=azure-cli-latest#az-account-set) и [группы ресурсов](https://learn.microsoft.com/ru-ru/cli/azure/group?view=azure-cli-latest#az-group-create).

```bash
az login
az account set --subscription 'replace-with-subscription-id'
rg='rg-p1-governance-lab'
location='replace-with-approved-location'
assignment='p1-owner-tag-lab'
scope=$(az group create --name "$rg" --location "$location" --query id --output tsv)
```

Если какая-то команда завершилась с ошибкой, остановись. Перед назначением получи определение встроенной политики в JSON и изучи его. Описание команды — в [справочнике](https://learn.microsoft.com/ru-ru/cli/azure/policy/definition?view=azure-cli-latest#az-policy-definition-show).

```bash
policy='871b6d14-10aa-478d-b590-94f262ecfa99'
az policy definition show --name "$policy" --output json
```

В [каталоге встроенных политик](https://learn.microsoft.com/ru-ru/azure/governance/policy/samples/built-in-policies#tags) и [исходном определении](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Tags/RequireTag_Deny.json) сейчас указаны версия `1.0.1`, параметр `tagName`, эффект `deny` и режим `Indexed`. Правило проверяет только наличие тега. Указан ли в нём настоящий владелец, оно не проверяет. На группы ресурсов эта политика не распространяется. [Режим `Indexed` проверяет типы ресурсов, поддерживающие теги и расположение](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/definition-structure-basics#resource-manager-modes).

Создай [назначение](https://learn.microsoft.com/ru-ru/cli/azure/policy/assignment?view=azure-cli-latest#az-policy-assignment-create) на область действия группы: требуемый тег — `owner`, шаблон версии определения — `1.*.*`, режим применения — `DoNotEnforce`. Проверка будет работать, а эффект `deny` применяться не будет.

```bash
az policy assignment create \
  --name "$assignment" \
  --display-name 'P1 owner tag check' \
  --scope "$scope" \
  --policy "$policy" \
  --definition-version '1.*.*' \
  --params '{"tagName":{"value":"owner"}}' \
  --enforcement-mode DoNotEnforce \
  --output json
```

[Шаблон версии `1.*.*`](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/assignment-structure#policy-definition-id-and-version) допускает обновления минорной версии и исправления в пределах основной версии `1`; исправления (patch) применяются всегда. Проверь область действия, значение параметра и режим применения в возвращённом назначении.

Теперь создай [управляемое удостоверение, назначаемое пользователем (user-assigned)](https://learn.microsoft.com/ru-ru/cli/azure/identity?view=azure-cli-latest#az-identity-create), без тегов. Этот тип ресурса [поддерживает теги и расположение](https://learn.microsoft.com/ru-ru/azure/templates/microsoft.managedidentity/2023-01-31/userassignedidentities), поэтому подходит для проверки в режиме `Indexed`.

```bash
az identity create --name 'id-p1-policy-lab' --resource-group "$rg" \
  --location "$location" --output json
```

Подожди, пока назначение вступит в силу. [Microsoft указывает примерно пять минут до начала проверки, но не задаёт фиксированного времени её завершения](https://learn.microsoft.com/ru-ru/azure/governance/policy/how-to/get-compliance-data#evaluation-triggers). После этого [запроси проверку](https://learn.microsoft.com/ru-ru/cli/azure/policy/state?view=azure-cli-latest#az-policy-state-trigger-scan) с `--no-wait` и повторяй `state list`, пока не появится результат для удостоверения.

```bash
az policy state trigger-scan --resource-group "$rg" --no-wait
az policy state list \
  --resource-group "$rg" \
  --policy-assignment "$assignment" \
  --query "[].{Resource:resourceId,State:complianceState}" \
  --output table
```

Ожидаемый результат для `id-p1-policy-lab` — `NonCompliant`: тег `owner` отсутствует. Режим `DoNotEnforce` позволяет создать ресурс с нарушением правила. Если таблица пуста, подожди и запроси её снова; если результат так и не появляется, проверь применимость политики. Если унаследованная политика запрещает создание ресурса или добавляет тег, сначала разберись с ней вместе с владельцем платформы.

Сохрани результат для удостоверения и область действия назначения в заметках P1. Прежде чем включать применение правила в P1, добавь обязательный тег в шаблоны Bicep.

**Стоимость:** [Сервис Azure Policy для ресурсов Azure бесплатен](https://azure.microsoft.com/en-us/pricing/details/azure-policy/), а [управляемые удостоверения не требуют дополнительной платы](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview). Упражнение не создаёт вычислительных ресурсов, хранилищ или развёртываний моделей.

**Удаление ресурсов:** после сохранения результата удали [назначение](https://learn.microsoft.com/ru-ru/cli/azure/policy/assignment?view=azure-cli-latest#az-policy-assignment-delete), затем [учебную группу вместе с удостоверением](https://learn.microsoft.com/ru-ru/cli/azure/group?view=azure-cli-latest#az-group-delete).

```bash
az policy assignment delete --name "$assignment" --scope "$scope"
az group delete --name "$rg" --yes
```

## Что перенести в свою практику \{#what-to-take-away}

- Выбирай область действия осознанно. Определение или инициативу нужно назначить на эту область, чтобы правила начали действовать.
- Выбирай эффект по нужному результату. Обнаружить несоответствие, предотвратить запрос и исправить ресурс — разные действия.
- Используй CAF для подготовки среды с общими правилами, а Well-Architected — для проектирования конкретной рабочей нагрузки. Явно записывай компромиссы и ответственных.
- Доводи до результата работу с тегами, бюджетами и рекомендациями по безопасности. Бюджет не ограничивает потребление, а соответствие конфигурации правилам не доказывает качество ответов.

**[Новые термины](../glossary.md#governance-and-frameworks)**: Azure Policy, определение политики, эффект политики, назначение политики, инициатива политик, состояние соответствия, Cloud Adoption Framework, целевая зона, Well-Architected Framework, Cost Management, Microsoft Defender for Cloud, CSPM.

## Источники \{#sources}

Проверено на 17.10.2026.

**Политики и применение правил**

- [Обзор Azure Policy](https://learn.microsoft.com/ru-ru/azure/governance/policy/overview)
- [Основы эффектов](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-basics), [audit](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-audit), [deny](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-deny), [modify](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-modify), [deployIfNotExists](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/effect-deploy-if-not-exists)
- [Структура назначения](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/assignment-structure) и [режимы определения](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/definition-structure-basics)
- [Структура инициативы](https://learn.microsoft.com/ru-ru/azure/governance/policy/concepts/initiative-definition-structure)
- [Каталог встроенных политик](https://learn.microsoft.com/ru-ru/azure/governance/policy/samples/built-in-policies#tags) и [исходное определение обязательного тега](https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Tags/RequireTag_Deny.json)
- [Проверка соответствия](https://learn.microsoft.com/ru-ru/azure/governance/policy/how-to/get-compliance-data)
- [Resource Policy Contributor](https://learn.microsoft.com/ru-ru/azure/role-based-access-control/built-in-roles/management-and-governance#resource-policy-contributor)

**Архитектура, расходы и безопасность**

- [Cloud Adoption Framework](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/overview) и [целевые зоны Azure](https://learn.microsoft.com/ru-ru/azure/cloud-adoption-framework/ready/landing-zone/)
- [Well-Architected Framework](https://learn.microsoft.com/ru-ru/azure/well-architected/what-is-well-architected-framework)
- [Анализ затрат](https://learn.microsoft.com/ru-ru/azure/cost-management-billing/costs/quick-acm-cost-analysis) и [бюджеты](https://learn.microsoft.com/ru-ru/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [Defender for Cloud](https://learn.microsoft.com/ru-ru/azure/defender-for-cloud/defender-for-cloud-introduction) и [варианты планов CSPM](https://learn.microsoft.com/ru-ru/azure/defender-for-cloud/concept-cloud-security-posture-management)
- [Что такое Microsoft Foundry?](https://learn.microsoft.com/ru-ru/azure/foundry/what-is-foundry)
- [Стоимость Azure Policy](https://azure.microsoft.com/en-us/pricing/details/azure-policy/) и [обзор управляемых удостоверений и их стоимости](https://learn.microsoft.com/ru-ru/entra/identity/managed-identities-azure-resources/overview)
- [Типы развёртываний Foundry и расположения обработки](https://learn.microsoft.com/ru-ru/azure/foundry/foundry-models/concepts/deployment-types)
- [Secure score](https://learn.microsoft.com/ru-ru/azure/defender-for-cloud/secure-score-security-controls)
- [Схема ресурса управляемого удостоверения (2023-01-31)](https://learn.microsoft.com/ru-ru/azure/templates/microsoft.managedidentity/2023-01-31/userassignedidentities)

**Справочник CLI**

- [Вход](https://learn.microsoft.com/ru-ru/cli/azure/reference-index?view=azure-cli-latest#az-login), [учётная запись](https://learn.microsoft.com/ru-ru/cli/azure/account?view=azure-cli-latest#az-account-set), [группа ресурсов](https://learn.microsoft.com/ru-ru/cli/azure/group?view=azure-cli-latest)
- [Определения политик](https://learn.microsoft.com/ru-ru/cli/azure/policy/definition?view=azure-cli-latest), [назначения](https://learn.microsoft.com/ru-ru/cli/azure/policy/assignment?view=azure-cli-latest), [состояния соответствия и проверки](https://learn.microsoft.com/ru-ru/cli/azure/policy/state?view=azure-cli-latest)
- [Управляемые удостоверения](https://learn.microsoft.com/ru-ru/cli/azure/identity?view=azure-cli-latest)
