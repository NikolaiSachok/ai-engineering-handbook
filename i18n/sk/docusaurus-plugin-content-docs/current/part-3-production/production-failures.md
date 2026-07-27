---
id: production-failures
title: Prečo AI-systémy zlyhávajú v produkcii
sidebar_label: Prečo AI zlyháva v produkcii
sidebar_position: 0
---

# Osem spôsobov, ako funkčné demo neprežije produkciu

Demo musí uspieť raz, na ceste, ktorú si niekto vybral. Produkcia musí obstáť aj na cestách, ktoré nikto nenaskriptoval — tisíckrát denne a vtedy, keď ľudia, ktorí ju postavili, spia. Sú to dva rôzne inžinierske problémy a zoznam nižšie je účtom za to, že si vyriešil iba prvý.

Osem kariet čítaj ako mapu, nie ako výstrahu. Každá pomenuje jedno zlyhanie, ukáže produkčné riešenie, ktoré naň odpovedá, a odkáže na lekciu, ktorá ten mechanizmus naozaj vysvetľuje. S niektorými si sa už stretol: kvalita vyhľadávania v Prvej časti príručky, chyby nástrojov v Druhej časti príručky. Ostatné sú presne to, na čo je táto časť. A ak všetky spája jedna niť, tak táto: *takmer nič z toho nie je zlyhanie modelu.* Model je jediný komponent, ktorý si nenapísal. Všetko okolo neho je tvoje.

:::note[Odkiaľ táto mapa pochádza]

Týchto osem spôsobov zlyhania koluje v diskusiách o AI v produkcii; ich usporiadanie podnietila veľmi rozšírená infografika od Alexa Xu (ByteByteGo). Odlišujeme sa od nej zámerne v dvoch veciach. Pôvodná verzia ukazuje iba zlyhania, čo je pri diagnostickom plagáte poctivý rozsah — naše karty pripájajú ku každému zlyhaniu aj **produkčné riešenie**, pretože vedieť, že dáta prichádzajú v zlom stave, ešte nie je to isté ako vedieť, čo postaviť. A na troch miestach nesúhlasíme s rozšíreným odporúčaním: pri drifte, pri evaluačných sadách a pri smerovaní na lacnejší model. Každú nezhodu označíme tam, kde na ňu príde reč.

:::

## 1 · Korpus je produkt

<InfoCard
  title="Korpus je produkt"
  caption="Produkčný ingestion hlási, čo prijal, čo zahodil a čo vôbec nezachytil.">
  <Lane kind="demo" label="DEMO">
    <Node icon="documentStack" label="čisté jednotné dokumenty" />
    <Flow kind="fail" />
    <Branch>
      <Node icon="database" badge="tick" label="index" />
      <Node icon="document" badge="cross" label="potichu zahodené" />
    </Branch>
  </Lane>
  <Lane kind="production" label="PRODUKCIA">
    <Node icon="mixedSources" label="rôzne zdroje" />
    <Flow />
    <Node icon="chunkedPage" label="chunking podľa rozloženia" />
    <Flow />
    <Node icon="clipboard" label="manifest ingestionu" />
  </Lane>
</InfoCard>

Korpus dema je priečinok, ktorý niekto ručne zostavil. V produkcii sú dvojstĺpcové PDF, tabuľky, ktorých význam drží hlavičkový riadok, stránky wiki spolovice prenesené z nástroja, ktorý už neexistuje, a skeny. Bežná rada — validuj schémy pri ingestione (príjme obsahu do indexu) — je správna pri záznamoch, no pri dokumentoch míňa cieľ: chybne sformované pole odpoveď RAG pokazí málokedy. Pokazí ju štruktúra. Tabuľka sploštená na súvislý text, pätička prilepená ku každému chunku (kúsku) a nadovšetko hranica chunku, ktorá oddelí fakt od podmienky, za ktorej platí. „Sadzby vzrástli o 4%“ nie je nesprávne, kým to neodrežeš od „iba v pilotnom projekte z roku 2019“.

Horšie je, že prísny validátor pracuje potichu. Dokumenty, ktoré nezodpovedajú schéme, zahodí bez ohlásenia, index sa postaví a vyzerá zdravo, model odpovedá z neúplného korpusu — sebavedomo, pretože mu nikto nepovedal, že tretina zdrojov nikdy nedorazila. Produkčným riešením preto nie je prísnejšia brána, ale **manifest ingestionu**: ingestion hlási, čo *zahrnul*, čo *vylúčil a prečo* a kde má *slepé miesta*, a hlási to ako artefakt zostavenia, ktorý sa dá prečítať. Vylúčený dokument je rozhodnutie; vylúčený dokument, ktorý nikto nedokáže pomenovať, je chyba. Mechaniku — parsovanie, rozloženie, stratégie chunkingu, metadáta — rozoberá lekcia o [ingestione](../part-1-rag/ingestion/index.md).

## 2 · Vyhľadávanie musí mať možnosť povedať nie

<InfoCard
  title="Vyhľadávanie smie povedať nie"
  caption="Prah relevantnosti uplatnený po rerankingu a generátor, ktorý smie odpovedať, že nemá kontext.">
  <Lane kind="demo" label="DEMO">
    <Node icon="retrieval" label="top-K, vždy" />
    <Flow kind="fail" />
    <Node icon="speechBubble" badge="bang" label="sebavedomo nesprávna odpoveď" />
  </Lane>
  <Lane kind="production" label="PRODUKCIA">
    <Node icon="sortedList" label="reranking" />
    <Flow />
    <Node icon="gauge" label="prah skóre" />
    <Flow />
    <Branch>
      <Node icon="speechBubble" badge="tick" label="odpoveď s oporou" />
      <Node icon="speechBubbleEmpty" badge="tick" label="alebo „bez kontextu“" />
    </Branch>
  </Lane>
</InfoCard>

Toto je zlyhanie, ktoré tímy stojí najviac času, pretože systém vyzerá zdravo od začiatku do konca. Nič neohlási chybu. Služba vráti stav 200. Jednoducho prídu nesprávne chunky a model urobí to, na čo bol postavený — z toho, čo dostal, napíše plynulú odpoveď.

Hodnotiť vyhľadávanie (retrieval) oddelene od generovania (generation) je diagnostická polovica riešenia a Prvá časť príručky ju obhajuje. Bez tohto rozdelenia neodlíšiš zlyhanie vyhľadávania od modelu, ktorý dobrý kontext ignoroval: dva týždne potom ladíš prompt, pričom chyba je v indexácii. Produkčná polovica je však cesta k odmietnutiu a práve tú v deme väčšinou nenájdeš. Demo vráti **top-K** (K najlepších kandidátov), vždy — a top-K je rez zoradeným zoznamom, nie posúdenie: zoradenie podľa podobnosti ti podá svojich päť najlepších kandidátov aj vtedy, keď sa tvojej otázky netýka ani jeden.

Preto vlož **prah skóre** za tú etapu, ktorej skóre má význam. Zlúčené skóre z hybrid search (hybridného vyhľadávania) spája poradia z hustého a z lexikálneho vyhľadávania do jedného čísla, no zdrojové škály nie sú navzájom kalibrované, takže prah nad výsledkom fúzie je v podstate svojvoľný. Naladiť prah sa dá až voči skóre cross-encodera po rerankingu (preusporiadaní). Pod prahom vráti vyhľadávanie zámerne prázdnu množinu a generátor povie, že nemá oporný kontext, namiesto toho, aby zo slabej skupiny chunkov zložil niečo vierohodné.

Ten posledný krok funguje iba vtedy, keď je generátor postavený tak, že smie odmietnuť — a to do detailu rozvádza [generovanie](../part-1-rag/generation/index.md). Hybrid search aj reranking, bez ktorých zmysluplný prah ani nepostavíš, dodáva [vyhľadávanie](../part-1-rag/retrieval/index.md). Demo odpovie na všetko. Produkčný systém smie povedať nie.

## 3 · Jedna evaluačná sada nestačí

<InfoCard
  title="Dve evaluačné sady, nie jedna"
  caption="Každá odpovedá na inú otázku: „pokazil som niečo, čo fungovalo?“ a „zodpovedá moja evaluácia ešte realite?“">
  <Lane kind="demo" label="DEMO">
    <Node icon="clipboard" label="sada prvého týždňa" />
    <Flow kind="fail" />
    <Node icon="dashboard" badge="bang" label="falošná istota" />
  </Lane>
  <Lane kind="production" label="PRODUKCIA">
    <Merge>
      <Node icon="clipboard" badge="padlock" label="zmrazená sada" />
      <Node icon="speechBubbleGroup" label="živá vzorka" />
    </Merge>
    <Flow />
    <Node icon="scales" label="poctivý prehľad skóre" />
  </Lane>
</InfoCard>

Testovacie prípady napísané v prvom týždni opisujú, ako si tím predstavoval, že sa ľudia budú pýtať. Šesť mesiacov reálnej premávky opisuje, ako sa pýtajú naozaj — a v tej medzere začína zelený panel klamať. Bežné odporúčanie žiada vzorkovať živú premávku každý týždeň a používať ju ako benchmark (meradlo, voči ktorému sa porovnávaš). Tu je naša prvá nezhoda: *nahradiť* stálu sadu znamená vymeniť jedno slepé miesto za druhé. Benchmark, ktorý sa mení každý týždeň, ti nepovie, či zmena z tohto týždňa pokazila niečo, čo minulý týždeň fungovalo; presne na to je zmrazená sada.

Ponechaj si obe. **Zmrazená regresná sada** odpovedá na otázku „pokazil som niečo, čo fungovalo?“ — a aby odpovedala, musí zostať nemenná. **Rotujúca sada vzorkovaná z reálnej premávky** odpovedá na otázku „zodpovedá moja evaluácia ešte realite?“ — a aby odpovedala, musí sa hýbať. Na rotáciu je aj druhý dôvod a prichádza z opačnej strany: pevný benchmark, podľa ktorého tím mesiace optimalizuje, prestane merať kvalitu a začne merať, ako dobre ten benchmark pozná. Obe sady potrebujú značky, a práve s tým nikto v rozpočte nepočíta — [evaluácia](../part-1-rag/cross-cutting/evaluation/index.md) to hovorí bez okolkov: bez dátovej sady niet evaluácie.

## 4 · Zelená ešte neznamená správne

<InfoCard
  title="Zelená ešte neznamená správne"
  caption="Dostupnosť je vlastnosť služby. Správnosť je vlastnosť odpovede.">
  <Lane kind="demo" label="DEMO">
    <Node icon="cloud" badge="tick" label="200 OK" />
    <Flow kind="fail" />
    <Node icon="speechBubble" badge="bang" label="nesprávna odpoveď" />
  </Lane>
  <Lane kind="production" label="PRODUKCIA">
    <Node icon="traceSpans" label="trace požiadavky" />
    <Flow />
    <Node icon="scales" label="sudca nad vzorkou" />
    <Flow />
    <Node icon="gauge" badge="tick" label="alert na kvalitu" />
  </Lane>
</InfoCard>

Každý bežný signál môže byť zdravý, kým systém odpovedá nesprávne. Latencia je v poriadku, miera chýb nulová, beží aj samotná nasadzovacia jednotka v Kubernetes (pod) — a odpovede sú sebavedomo nesprávne, pretože obyčajný monitor nemá názor na *obsah* odpovede so stavom 200. Dostupnosť je vlastnosť služby, správnosť je vlastnosť odpovede, a z prvej druhú neodvodíš.

Medzeru zaplnia dve veci. Prvá je **trace** — záznam behu, ktorý zachytí celú cestu jednej požiadavky: dopyt, vrátené chunky aj ich skóre, odoslaný prompt, odpoveď a tokeny. Bez identifikátorov chunkov totiž nezrekonštruuješ ani to, *prečo* bola odpoveď nesprávna. Druhá je **nezávislý sudca nad vzorkou reálnej premávky** (LLM-as-a-judge), aby sa kvalita stala monitorovanou metrikou s prahom a s upozornením, nie niečím, čo sa dozvieš až z hlásenia na podpore. To je [Observability (pozorovateľnosť)](../part-1-rag/cross-cutting/observability/index.md) — aj tá slučka, ktorou sa jej zistenia vracajú do evaluácie.

Jednu vec navrhni vedome a nepreberaj ju z predvolených nastavení: logovanie na ladenie nie je logovanie na dôkaz. Ladenie chce posledných niekoľko dní v takej podrobnosti, akú si vieš dovoliť. Audit — regulované odvetvie, sporná odpoveď, zákazník, ktorý sa pýta, čo mu systém povedal v marci — potrebuje po *mesiacoch* zrekonštruovať, čo sa vyhľadalo a čo sa vrátilo, a to je požiadavka na uchovávanie a integritu, nie nastavenie podrobnosti. Rozhodni sa vopred, ktoré z nich staviaš — logovanie na ladenie alebo **logovanie na úrovni auditu** — skôr než sa za teba rozhodne audítor.

## 5 · Rozhoduje náklad na prijatú odpoveď

<Infographic
  src="/img/infographics/production-failures/05-cost.webp"
  alt="Tri lacné pokusy oproti jednému drahému pokusu s vyznačenou daňou za opakovania"
  caption="Lacnejší model sa oplatí len vtedy, keď na úspešnosti získa aspoň toľko, koľko ušetrí na cene."
/>

Náklady, ktoré v deme vyzerajú ako zaokrúhľovacia chyba, sa v produkcii násobia tromi spôsobmi naraz: agenti opakujú volania, konverzácie pri každom kroku znova odošlú celú svoju históriu a používatelia vložia celé dokumenty do poľa, ktoré si dimenzoval na jednu vetu. Opakované odosielanie sa prehliada najčastejšie — model bez vlastného stavu prečíta prepis znova pri každom kroku, takže dvojnásobne dlhá úloha stojí približne štvornásobok, a skrátiť to, čo sa v kontexte prenáša, je najsilnejšia páka, akú máš. Stabilný prefix promptu, ktorý sa dá cachovať, má väčšiu hodnotu než väčšina prechodov na iný model.

A tu je druhá nezhoda: rada *smeruj rutinnú prácu na lacnejší model* má podmienku a tá sa zvyčajne vynechá. Rozhoduje náklad na prijatú odpoveď, nie náklad na token — lacnejší model, ktorý potrebuje tri pokusy tam, kde drahý potreboval jeden, lacnejší nie je. Ten rozdiel je **daň za opakovania**:

```text
cost_per_accepted ≈ attempt_cost / p          (p = first-try acceptance rate)

the cheaper model wins only when:
    p_cheap / p_expensive  >  price_cheap / price_expensive
```

Čítaj to takto: `p` je podiel odpovedí prijatých na prvý pokus a lacnejší model vyhráva iba vtedy, keď je pomer jeho úspešnosti k úspešnosti drahého väčší než pomer ich cien. Polovičná cena teda nič neprinesie, ak spoľahlivosť nedosahuje ani polovicu. Než uveríš úspore, zmeraj `p` pre každú trasu. [LLMOps](./llmops/index.md) preberá páky — smerovanie, cachovanie, dávkový režim, rozpočty, ktoré sa naozaj vynucujú — a kurz AI-SDLC prepočítava tú istú aritmetiku pre inú jednotku: náklad na prijatú zmenu kódu.

## 6 · Pred pretrénovaním preindexuj

<InfoCard
  title="Pretrénuj až nakoniec"
  caption="Drift zvyčajne sídli v korpuse alebo v dopytoch, nie vo váhach.">
  <Lane kind="demo" label="DEMO">
    <Node icon="driftCurves" label="zistený drift" />
    <Flow kind="fail" />
    <Node icon="chip" badge="refresh" label="pretrénuj model" />
  </Lane>
  <Lane kind="production" label="PRODUKCIA">
    <Node icon="database" badge="refresh" label="preindexuj" rank="1" />
    <Flow />
    <Node icon="sliders" label="zloženie retrievalu" rank="2" />
    <Flow />
    <Node icon="codeFile" label="prompt" rank="3" />
    <Flow />
    <Node icon="chip" label="váhy nakoniec" rank="last" />
  </Lane>
</InfoCard>

Kvalita sa kazí aj bez nasadenia. Používatelia prinesú novú slovnú zásobu, dokumenty pod systémom sa zmenia a hostovaný model, ktorý si nepripol, sa pohne pod tebou. Toto je tretia nezhoda a najostrejšia: bežný reflex — zapojiť prahy driftu (posunu) tak, aby spúšťali **pretrénovanie** — je odpoveď z MLOps prenesená do systému, ktorého váhy takmer nikdy nie sú tým problémom.

Vo vyhľadávacom systéme drift zvyčajne pochádza z korpusu alebo z dopytov, takže **rebrík odpovedí na drift** začína hlboko pod modelom: preindexuj a zmeň chunking, uprav zloženie vyhľadávania, prepracuj prompt — a až potom uvažuj o zásahu do váh, čo pre väčšinu tímov znamená ďalšiu verziu od dodávateľa, nie vlastný tréning. Tri podoby driftu a spôsob, ako každú sledovať, preberá [LLMOps](./llmops/index.md). Užitočný dôsledok znie, že **korpus je vydanie**: patrí mu verzia, diff aj rollback (návrat na predchádzajúcu verziu), presne ako kódu.

## 7 · Prompt a korpus sú vydania

<InfoCard
  title="Prompt a korpus sú vydania"
  caption="Všetko, čo mení správanie, potrebuje verziu a cestu späť.">
  <Lane kind="demo" label="DEMO">
    <Node icon="codeFile" label="prompt v kóde" />
    <Flow kind="fail" />
    <Node icon="cloud" badge="bang" label="každá úprava je nasadenie" />
  </Lane>
  <Lane kind="production" label="PRODUKCIA">
    <Merge>
      <Node icon="document" badge="tag" label="verziovaný prompt" />
      <Node icon="chip" badge="tag" label="pripnutý model" />
      <Node icon="database" badge="tag" label="snímka korpusu" />
    </Merge>
    <Flow />
    <Node icon="branchSplit" label="canary, rollback" />
  </Lane>
</InfoCard>

Kým prompt sedí priamo v aplikačnom kóde, úprava jednej vety je nasadenie — a tak aj oprava formulácie nesie riziko nasadenia a nikto si ju netrúfne považovať za malú zmenu, ktorou v skutočnosti je. Presuň prompty do **konfigurácie vo verziovacom systéme** a daj im vlastné brány kvality. Prompty sa tým začnú dať porovnávať diffom a vracať späť, namiesto toho, aby si pri každej zmene len dúfal.

Potom uplatni ten istý štandard na všetko ostatné, čo mení správanie bez zmeny kódu: pripni verziu modelu, urob snímku korpusu, vydávaj cez canary release (kanárikové nasadenie) a pre každú z tých troch vecí drž samostatnú cestu rollbacku. Systém, pod ktorým sa môže nezávisle pohnúť prompt, model aj index, nemá reprodukovateľný stav vôbec, a nijaké testovanie to nenapraví. Mechanika vydávania je téma [LLMOps](./llmops/index.md).

## 8 · Pipeline potrebuje brány medzi krokmi

<InfoCard
  title="Najlacnejšia kontrola prvá"
  caption="Každá etapa odmietne chybný vstup a najlacnejšia kontrola beží prvá.">
  <Lane kind="demo" label="DEMO">
    <Node icon="chainSteps" label="bez kontrol" />
    <Flow kind="fail" />
    <Node icon="document" badge="crack" label="prvá chyba sa šíri" />
  </Lane>
  <Lane kind="production" label="PRODUKCIA">
    <Node icon="gate" label="schéma" rank="1" />
    <Flow />
    <Node icon="gate" label="citácie" rank="2" />
    <Flow />
    <Node icon="gate" label="sudca" rank="last" />
  </Lane>
</InfoCard>

Vo viackrokovej pipeline sa prvý chybný výstup stane dôveryhodným vstupom ďalšieho kroku. Zlyhanie vyhľadávania sa zmení na sebavedomý súhrn, súhrn na rozhodnutie — a kým si niekto všimne, že je niečo v neporiadku, pôvodná chyba leží o niekoľko transformácií dozadu. Odpoveďou je validácia medzi krokmi a každá etapa má byť postavená tak, aby chybný vstup odmietla, nie aby s ním urobila, čo sa dá: etapa, ktorá nikdy neodmietne, robí z chyby dôveryhodný výsledok.

Doplniť sa oplatí ešte jedno: poradie. Brány nie sú rovnako drahé. Kontrola schémy stojí mikrosekundy, kontrola citácií a ich groundingu (opretia odpovede o kontext) stojí jedno vyhľadávanie a posúdenie modelom stojí volanie modelu. Púšťaj ich tak, že najlacnejšia kontrola ide prvá — za chyby, ktoré by zachytil regulárny výraz, tak nikdy nezaplatíš cenu sudcu. Toto poradie rozvádza kurz AI-SDLC v lekcii o vrstvených bránach; mechaniku na strane RAG — čo strážiť na vstupe, na výstupe a pri ingestione — vysvetľujú [guardrails](../part-1-rag/cross-cutting/guardrails/index.md).

## 9 · Štyri zlyhania, ktoré v zoznamoch zvyčajne chýbajú

<InfoCard
  title="Štyri prehliadané zlyhania"
  caption="Štyri zlyhania, ktoré bežné zoznamy vynechávajú — a pri poslednom zlyhá nástroj skôr než model.">
  <Grid tone="fail">
    <Node icon="lockOpen" label="neobmedzený prístup" />
    <Node icon="document" label="otrávené dokumenty" />
    <Node icon="globe" label="jediný jazyk" />
    <Node icon="plug" label="nespoľahlivé nástroje" />
  </Grid>
</InfoCard>

Ešte štyri, a každé z nich už raz vyradilo produkčný systém, kým sa všetci pozerali na predchádzajúcich osem.

**Neobmedzený prístup.** V deme beží agent s oprávneniami, pri ktorých všetko funguje, a index drží každý dokument, ku ktorému sa crawler dostal. V produkcii je to isté usporiadanie kanálom na vynesenie dát (data exfiltration): vyhľadávanie, ktoré nefiltruje podľa oprávnení volajúceho, bez problémov odpovie citáciou z dokumentu, ktorý volajúci nikdy nesmel otvoriť. **Vyhľadávanie s ohľadom na oprávnenia** nie je funkcia, ktorú doplníš neskôr — mení podobu samotného indexu.

**Otrávené dokumenty.** Vyhľadaný text je nedôveryhodný vstup. Dokument s ukrytými inštrukciami dokáže prevziať kontrolu nad modelom, ktorý ho prečítal — a najlacnejšie sa to zachytáva pri indexácii, nie až pri dopyte.

**Jediný jazyk.** Embeddingový model a reranker natrénované na angličtine prehliadnu relevantné anglické dokumenty, keď otázka príde v inom jazyku, a to zlyhanie je tiché: menej výsledkov a všetky vierohodné. Ak sú tvoji používatelia viacjazyční a tvoja evaluácia nie, nezmeral si systém, ktorý tí používatelia majú.

**Nespoľahlivé nástroje.** Nástroje zlyhajú skôr než model. Volaniu API vyprší časový limit, MCP server sa reštartuje, vektorové úložisko odmietne spojenie — a agent bez časového limitu, bez opakovania a bez fallbacku (záložnej cesty) jednoducho zostane visieť, a používatelia to vnímajú ako pokazený systém, nie ako pomalý. Radšej zámerne vráť horšiu odpoveď než nechať používateľa čakať v tichu — to je **riadené zhoršenie**. Celý cyklus volania aj spracovanie jeho chýb rozvádza lekcia o [používaní nástrojov](../part-2-agents/tool-use/index.md).

## Čo si odniesť z lekcie

- Takmer nič z toho nie je zlyhanie modelu. Model je komponent, ktorý si nenapísal; zlyhania sídlia v systéme okolo neho.
- Ingestion nemá iba validovať, má hlásiť — čo zahrnul, čo vylúčil a prečo, a kde má slepé miesta. Zahodenie bez ohlásenia dá sebavedomú odpoveď z neúplného korpusu.
- Vyhľadávanie potrebuje cestu k odmietnutiu: prah skóre po rerankingu, zámerne prázdnu množinu a generátor, ktorý povie, že nemá kontext.
- Dve evaluačné sady — jedna zmrazená na regresie, jedna rotujúca z reálnej premávky na realitu. Ani jedna nenahrádza druhú.
- Dostupnosť nie je správnosť. Pridaj trace s identifikátormi chunkov a sudcu nad vzorkou premávky; a samostatne rozhodni, či máš voči niekomu povinnosť viesť audítorskú stopu.
- Jednotkou je náklad na prijatú odpoveď: `cost ≈ attempt_cost / p`, a lacnejší model musí cenový pomer prekonať spoľahlivosťou.
- Na drift odpovedaj preindexovaním dávno pred pretrénovaním; korpus je vydanie, s verziou aj rollbackom.
- Prompt, verzia modelu a korpus potrebujú každý svoju verziu a cestu späť, inak systém nemá reprodukovateľný stav.
- Brány medzi krokmi, najlacnejšia kontrola prvá — každá etapa chybný vstup odmietne, namiesto toho, aby z neho robila dôveryhodný výsledok.
- A tie štyri, ktoré nikto nevypisuje: neobmedzený prístup, otrávené dokumenty, testovanie v jedinom jazyku a nespoľahlivé nástroje.

Časť III teraz skladá odpovede: [serving](./serving/index.md) samotného systému (prevádzka ako sieťovej služby), [cloudové platformy](./cloud-platforms/index.md), na ktorých beží, [ekosystém nástrojov](./tooling-ecosystem/index.md), ktorý ho meria a chráni, a [LLMOps](./llmops/index.md) pre jeho život po vydaní.

**[Nové pojmy](../glossary.md#production-failures)**: score floor / relevance floor, ingestion manifest, blind spot (ingestion), frozen regression set, rotating live-sampled set, benchmark familiarity, audit-grade logging, cost per accepted answer, retry tax, drift response ladder, corpus as a release, permission-aware retrieval, cross-lingual retrieval gap, graceful degradation (tools).
