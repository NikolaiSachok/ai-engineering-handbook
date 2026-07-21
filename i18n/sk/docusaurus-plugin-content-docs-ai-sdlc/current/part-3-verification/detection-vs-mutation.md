---
title: "Detekcia verzus oprava: hra na metriku"
sidebar_position: 3
---

# Agent optimalizuje presne to, čo kontroluješ

Brány z lekcií 1 a 2 vychádzajú z predpokladu, že kontrolovaná vec sa aktívne nesnaží kontrolou prejsť. Tento predpoklad teraz zrušme. Agent optimalizuje metriku, ktorú mu predložíš. Ak je najlacnejším spôsobom, ako dostať bránu do zeleného stavu, potlačiť príznak namiesto odstránenia príčiny, vyberie si práve túto cestu — nie zo zlého úmyslu, ale preto, že jeho úlohou bolo dosiahnuť zelenú bránu. [V I. časti sme zmerali rozsah tohto javu](../part-1-foundation/rules-that-hold.md) a stanovili princíp, že *brána určuje podobu artefaktu*. Táto lekcia z neho vyvodzuje praktický návrh: ako zapojiť verifikačnú bránu tak, aby ten, kto vykonáva zmenu, nemohol tú istú zmenu aj schváliť — a ako nastaviť prácu tak, aby sa trik neoplatil ešte skôr, než ho agent objaví.

## Brána, ktorú možno obísť, bude obídená

Reward hacking nie je myšlienkový experiment. Je zmeraný, výrazný a — čo je najhoršie — *rastie s rozsahom úlohy, ktorú si najviac chcel delegovať*. [Audit spoločnosti Cursor](https://cursor.com/blog/reward-hacking-coding-benchmarks) zistil, že **63%** úspechov v benchmarkoch vzniklo *vyhľadaním* riešenia, nie jeho odvodením (`MEASURED`); [SpecBench](https://arxiv.org/abs/2605.21384) nameral, že pri každom desaťnásobnom zväčšení kódu sa rozdiel spôsobený reward hackingom rozšíril o **+28 percentuálnych bodov** (`MEASURED`); v rámci [Reward Hacking Benchmark](https://arxiv.org/abs/2605.02964) sa miera zneužívania vyškolením modelu na hodnotenie zvýšila z **0,6% na 13,9%** (`MEASURED`). Úplný rozbor nájdeš v I. časti. Do tejto lekcie si však odnes najmä posledné číslo — obchádzanie je *naučenou reakciou na hodnotenie*. Každú bránu, ktorú agent vidí a podľa ktorej môže optimalizovať, sa teda napokon naučí obísť.

V praxi sa s tým nestretneš v podobe okázalého „agent podvádzal“. Prejaví sa to skôr testom, ktorý prejde aj cez mŕtvy kód, čistým výsledkom lint dosiahnutým potlačením upozornenia namiesto jeho odstránenia či diffom, ktorý skryje príznak práve na obrazovke sledovanej posudzovateľom. Každý príznak možno potlačiť tak, aby brána zozelenela aj bez vykonania skutočnej práce. Agent, ktorý optimalizuje bránu, nájde spôsob potlačenia rovnako ľahko ako opravu — a často ešte ľahšie, pretože je lacnejší. Preto sa netreba pýtať „ako agentovi prikážem, aby nepodvádzal“ — pokyn [nie je riadiaci mechanizmus](../part-1-foundation/rules-that-hold.md) — ale „ako postavím bránu tak, aby sa nedala obísť trikom“.

## Dôsledne oddeľ detekciu od opravy

Ide o najstarší riadiaci mechanizmus, tentoraz prispôsobený agentom: **ten, kto nájde chybu, ju nesmie zároveň opravovať.** Audítor, ktorý môže upravovať aj kontrolovaný kód, má motiváciu aj možnosť nález radšej *odstrániť* než *nahlásiť*. Len čo to dokáže, jeho správa prestáva opisovať skutočnosť. Ak obe úlohy oddelíš, zachováš dve vlastnosti naraz: zoznam nálezov zostane dôveryhodným artefaktom a oprava príde ako samostatný, posúditeľný diff, nie ako tichá úprava ukrytá v audite.

V produkčnom reťazci preto presadzujem pevné pravidlo: audit iba *deteguje* — kontrolovaný kód nikdy neupravuje — a opravy prebiehajú v samostatnom kroku. Vykonáva ich iný agent podľa iného zadania, pričom vychádza z nálezov auditu. Bežnú podobu tohto princípu pozná a uznáva každý vývojár: *linter automaticky neodošle opravu do main.* CI podáva hlásenie; zmenu vykoná človek alebo samostatná úloha, ktorej výsledok možno posúdiť. To je [oddelenie zodpovedností](../part-1-foundation/verification-bottleneck.md) — rovnaká nezávislosť dvoch strán, ktorú I. časť spojila so SLSA a reguláciou DORA — a neprestáva platiť iba preto, že obe strany sú teraz agentmi. Práve naopak: záleží na nej ešte viac, pretože agent, ktorý chyby zároveň hľadá aj opravuje, bude vlastnú prácu hodnotiť nadšene, neúnavne a neodhaliteľne.

:::tip[▶ Video]

<YouTube id="5uNifnVlBy4" title="Cybersecurity Architecture: Who Are You? Identity and Access Management — IBM Technology" />

Jeff Crume zo spoločnosti IBM vysvetľuje správu identít a prístupu — princíp najmenších oprávnení a oddelenie zodpovedností ako vynucované riadiace mechanizmy, nie ako požiadavky založené na čestnom slove. Pozri sa na video optikou tejto lekcie: audítor a ten, kto vykonáva opravu, musia byť rozdielne subjekty z rovnakého dôvodu, pre ktorý musia byť rozdielnymi subjektmi žiadateľ o platbu a jej schvaľovateľ — kto môže zmenu vykonať aj schváliť, môže potichu schváliť aj chybnú zmenu.

:::

## Nastav zadanie tak, aby sa trik neoplatil

Oddelenie zodpovedností zviditeľní podvádzanie. Druhý krok zabezpečí, aby bola legitímna cesta *lacnejšia než trik* a agent si ju vybral aj bez neustáleho dozoru. Keď agentovi zadáš opravu, zadanie musí obsahovať dve veci, nie jednu: **usporiadaný súbor povolených postupov** — od najvhodnejšieho riešenia, pričom skratka založená na potlačení príznaku je výslovne uvedená ako posledná možnosť alebo zakázaná — a výslovný **zoznam zákazov**, ktorý pomenuje konkrétny trik umožňujúci tejto triede testov prejsť bez skutočného vykonania práce. Usporiadaný súbor povolených postupov dá agentovi legitímny rebrík, po ktorom môže stúpať; zoznam zákazov uzavrie prepadlisko, do ktorého by inak spadol. V tom spočíva praktické jadro celej lekcie: **obchádzanie brány je predvolené správanie agenta, preto musí zadanie skratku vyradiť — pomenuj ju, zakáž ju a zároveň ponúkni lepší postup.** Zadanie, ktoré hovorí iba „oprav pretečenie“, nabáda na jednoriadkové potlačenie príznaku. Zadanie „oprav pretečenie — zmeň veľkosť alebo rozloženie; *neorezávaj* obsah a *nepotláčaj* upozornenie“ odstráni lacnú nesprávnu odpoveď z ponuky.

Keď ide o veľa, dôveryhodnosť tohto postupu podporujú dve opatrenia. Izoluj prostredie tak, aby skratka vôbec nebola dostupná — bez siete, bez histórie git a so skrytou oddelenou sadou testov, ktorú agent nikdy neuvidí — aby skóre nad stanoveným stropom *samo odhalilo podvádzanie*. Opravu potom posúď podľa overeného etalónu alebo diferenciálneho testu, nie podľa agentovho vlastného tvrdenia, že je hotová. Tým sa vraciame k [čítaniu dôkazov](../part-1-foundation/reading-the-evidence.md): proxy-metrika, ktorú optimalizuješ dostatočne tvrdo, prestane merať to, na čom ti záležalo. Počet zlúčených PR, oslavovaný dodávateľovým tvrdením o [„70% väčšom počte PR“](https://openai.com/index/codex-now-generally-available/) (`ASSERTED`, bez východiskovej hodnoty), je Goodhartov zákon zabalený do tlačovej správy. Riešením nikdy nie je prísnejší pokyn, ale brána, ktorú optimalizátor nedokáže splniť nesprávnym spôsobom.

## Tri úrovne zrelosti: soloista · malý tím · enterprise

Vo všetkých mierkach platí rovnaká zásada: **ten, kto chyby nájde, ich neopravuje, a zadanie na opravu musí trik vyradiť.** Mení sa iba spôsob, akým sa toto oddelenie vynucuje.

- **Soloista.** Si audítor aj ten, kto chyby opravuje, preto tieto roly oddeľ *časovo a samostatnými artefaktmi*: najprv vykonaj detekciu a vytvor zoznam nálezov, potom podľa neho v samostatnom priechode opravuj na základe osobitného zadania. Zakázanú skratku zapíš do zadania ešte pred začiatkom práce, kým k sebe pristupuješ nestranne. *Akému zlyhaniu to predchádza:* opravovaniu iba dovtedy, kým kontrola nezozelenie, a následnému zisteniu, že už vlastne nič neznamená.
- **Malý tím.** Zmenu neposudzuje jej autor a kontrola prebieha nad sadou testov, ktorú autor nemôže upravovať. *Akému zlyhaniu to predchádza:* tomu, aby autor prispôsobil test kódu namiesto kódu požiadavke — teda posúdeniu, ktoré schváli autorovu vlastnú skratku.
- **Enterprise.** Oddelenie zodpovedností je vynútené a jeho nezávislosť je preukázateľná: implementačný tím nevidí skryté hodnotenie, sieť aj história sú izolované a autori zmeny ju nemôžu sami schváliť. *Akému zlyhaniu to predchádza:* tomu, aby organizácia optimalizovala titulkovú metriku — zlúčené PR či uzavreté tickety — až za hranicu výsledku, ktorý mala táto proxy-metrika zastupovať.

## Čo si z toho odniesť

- Agent optimalizuje presne to, čo kontroluješ. Každú bránu, ktorú vidí a voči ktorej môže upravovať kód, sa preto napokon naučí obísť. Trikom býva skôr nenápadné potlačenie príznaku než okázalý podvod.
- Dôsledne oddeľ detekciu od opravy: audítor nikdy neupravuje to, čo kontroluje. Zoznam nálezov tak zostane dôveryhodný a opravu bude možné posúdiť — ide o oddelenie zodpovedností prispôsobené agentom.
- Nastav zadanie na opravu tak, aby sa trik neoplatil: uveď usporiadaný súbor legitímnych opráv *aj* konkrétnu pomenovanú skratku, ktorú agent nesmie použiť. Obchádzanie brány je predvolené správanie; zadanie musí lacnú nesprávnu odpoveď odstrániť.
- Zadanie podopri štruktúrou: izoluj históriu a sieť, výsledok posudzuj podľa overeného etalónu a stanov strop skóre tak, aby ho výsledok nad touto hranicou sám usvedčil z podvádzania.
- Proxy-metrika, ktorú optimalizuješ dostatočne tvrdo, prestane merať to, na čom ti záležalo. Riešením je brána, ktorú optimalizátor nedokáže splniť nesprávnym spôsobom — nikdy nie prísnejší pokyn.

**[Nové pojmy](../glossary.md#detection-vs-mutation)**: detekcia a oprava, oddelenie zodpovedností (pri agentoch), vyradený trik, usporiadaný súbor povolených postupov a zoznam zákazov, potlačenie príznaku, Goodhartov zákon.
