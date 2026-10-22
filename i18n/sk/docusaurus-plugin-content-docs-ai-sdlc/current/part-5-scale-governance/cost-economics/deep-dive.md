---
title: "Náklady a ekonomika práce agentov — prehĺbenie"
sidebar_label: "Aritmetika: kontext, cachovanie a daň za opakovania"
sidebar_position: 2
---

# Čísla za nákladmi na prijatú zmenu

[Prvá časť](./index.md) stanovila jednotku — náklady na *prijatú* zmenu, nie na token — a pomenovala zvyčajné
prekvapenia: miera opakovaných pokusov preváži nad cenníkovou cenou a na kontext sa často zabúda. Táto stránka
tieto tvrdenia presne vyčísli. Nejde o nič zložité, iba o niekoľko násobení. Keď ich však dotiahneš do konca,
intuícia založená na cenníku sa obráti. Nižšie uvedené sadzby sú len ilustračné (dosaď si údaje svojho
poskytovateľa), no o výške účtu rozhoduje práve *tvar* týchto súčtov.

## Rozklad jedného pokusu \{#one-attempt-decomposed}

Pri jednom pokuse sa účtujú dva prúdy s odlišnými sadzbami, sčítané za všetky jeho kroky: **vstup** (všetko, čo
odosielaš — systémový prompt, pravidlá, zadanie, predchádzajúce kroky, výsledky nástrojov) a **výstup** (to, čo
model vygeneruje). Výstup zvyčajne stojí za token niekoľkonásobne viac než vstup, a preto ľudia sledujú najmä
jeho. Pri práci agentov je však objem vstupu násobne väčší než objem výstupu, takže vyšší účet napokon vytvorí
lacnejší prúd:

```text
attempt_cost = input_tokens × input_rate + output_tokens × output_rate
```

Tu `attempt_cost` znamená iba náklady na tokeny modelu. Do úplných nákladov na prijatú zmenu pripočítaj externé zdroje nástrojov, overovanie a ľudskú revíziu.

Výstupom jedného kroku agenta býva diff, volanie nástroja či odsek — stovky tokenov. Na vstupe je celý pracovný
kontext — tisíce až desiatky tisíc tokenov. Veľký objem preváži nad nízkou sadzbou.

## Prečo rozhoduje kontext: opakované posielanie rastie kvadraticky \{#why-context-dominates-the-re-send-is-quadratic}

Cenník jedného volania túto časť zakrýva. Agent pri každom kroku znova odosiela celú konverzáciu, pretože model
si medzi volaniami stav nepamätá — v 5. kroku teda opäť platíš za načítanie krokov 1 až 4. Ak úloha trvá `N`
krokov a kontext sa v každom zväčší približne o rovnaký objem, celkový účtovaný vstup nie je `N`-násobkom
jedného kroku. Tvorí ho súčet `1 + 2 + … + N`, teda **`O(N²)`**. Dvojnásobný počet krokov znamená približne
*štvornásobné* náklady na vstup.

Tento fakt mení poradie priorít. Vysvetľuje, prečo za úlohu, ktorá si vyžiadala dvojnásobný počet krokov,
zaplatíš približne štvornásobok nákladov na vstup, prečo za nafúknutý kontext platíš pri každom kroku, nielen
raz, aj prečo má [nafúknutý korpus pravidiel](../drift-and-rot.md) z lekcie o drifte okrem následkov na kvalite
aj priamu cenovku. Najväčšiu úsporu pri práci agentov prináša zmenšenie kontextu, no z cenníka jedného volania
to neuvidíš.

## Prompt caching zmierňuje rast nákladov \{#prompt-caching-bends-the-curve-back}

Kvadratické opakované posielanie má priamu protiváhu: poskytovatelia umožňujú cez **prompt caching (cachovanie
promptu) uložiť stabilný prefix**, takže za jeho opätovné odoslanie zaplatíš iba zlomok bežnej vstupnej
sadzby — bežne približne desatinu; presnú zľavu uvádza poskytovateľ, preto ju posudzuj podľa
pravidla kurzu pre údaje od dodávateľov — je to ním nastavená cenová páka, nie nameraná konštanta. Systémový
prompt, korpus pravidiel a uzavreté staršie kroky obsahujú pri každom volaní rovnaké bajty; po uložení do cache
sa už neúčtujú v plnej výške.

Z toho vyplýva konkrétne pravidlo návrhu, ktoré nadväzuje na predchádzajúce lekcie. Cachovanie funguje iba pre
**stabilný prefix**, preto nemenný obsah umiestni na začiatok, premenlivý na koniec — a počas úlohy ho už
*nemeň*. Ak korpus pravidiel upravíš uprostred úlohy alebo sa pre jeho veľkosť pri každom volaní skráti inak,
prefix sa rozpadne a o zľavu prídeš. Hygiena korpusu, ktorú lekcia o drifte zdôvodnila správnosťou, teda
pomáha riadiť aj náklady. Disciplína stabilného prefixu tlmí dôsledky kvadratického rastu.

## Batch vymieňa rýchlosť za zľavu \{#batching-trades-latency-for-a-discount}

Ďalšiu možnosť máš pri práci, na ktorej výsledok človek práve nečaká. Poskytovatelia v cenníkoch ponúkajú výrazne lacnejšie rozhrania pre batch — odošleš veľa
požiadaviek a výsledky vyzdvihneš o niekoľko minút až hodín — často približne za polovicu ceny,
pretože túto prácu plánujú mimo špičky. Za nižšiu cenu
dostaneš vyššiu latenciu, čo prirodzene rozdelí workload: **interaktívny** krok agenta, na ktorý niekto čaká,
do batchu nepatrí; **offline** práca — hromadné evaly, transformácia celého korpusu, opätovné generovanie
fixtures — áno. Dodatočné overovacie prechody z III. časti sa často dajú spracovať cez batch, aj keď samotné
generovanie prebiehalo interaktívne.

## Daň za opakovania a hranica, pri ktorej sa cenník obráti \{#the-retry-tax-and-the-break-even-that-inverts-the-price-list}

Teraz presne vyjadrime hlavnú tézu z prvej časti. Ak zmena uspeje na prvý pokus s pravdepodobnosťou `p`,
očakávaný počet pokusov je `1/p`, takže:

```text
cost_per_accepted ≈ attempt_cost / p
```

Porovnaj dva modely. Drahý model s cenou `C` a úspešnosťou prvého pokusu `0.8` stojí na prijatú zmenu `C / 0.8 =
1.25 C`. Lacný model za polovicu, teda `0.5 C`, musí prekonať určitú hranicu úspešnosti:

| Úspešnosť lacnejšieho modelu | Náklady na prijatú zmenu | V porovnaní s 1,25 C |
|---|---|---|
| 0,40 | 0,5 C / 0,40 = 1,25 C | rovnaké náklady |
| 0,50 | 0,5 C / 0,50 = 1,00 C | lacnejší model sa oplatí |
| 0,30 | 0,5 C / 0,30 = 1,67 C | *vyššie* náklady |

Hranica rentability je jednoznačná: lacnejší model sa oplatí iba vtedy, keď `p_cheap / p_expensive > price_cheap / price_expensive`
— pomer jeho úspešnosti k drahšiemu modelu musí byť vyšší než pomer ich cien. Polovičná cena neprinesie nič
pri presne polovičnej spoľahlivosti a pod ňou ťa už bude stáť viac. Celé tvrdenie, že „miera opakovaných
pokusov preváži nad cenníkovou cenou“, sa tak zmestí do jednej nerovnosti, ktorú vieš merať.

## Položka, ktorú zľava na tokenoch nezmení \{#the-line-a-token-discount-cannot-touch}

Zľava na tokenoch zlacní generovanie a overovanie modelom, sama však nezníži cenu ľudskej revízie ani externých zdrojov nástrojov. Úsporu ohraničuje podiel účtu, ktorý sa skutočne platí v tokenoch. Ak revízia tvorí 40% a externé výpočty 30%, aj úplné odstránenie zvyšného účtu za tokeny ušetrí najviac 30%, pokiaľ ostatné náklady zostanú rovnaké. Priepustnosť môžu obmedzovať ľudia aj externé služby. Pred výberom optimalizácie zmeraj ich podiely.

## Čo si odniesť \{#what-to-take-away}

- **Rozlož náklady pokusu:** `input_tokens × input_rate + output_tokens × output_rate`. Výstup stojí za token
  viac, no objem vstupu je oveľa väčší, a preto účet určuje vstup.
- **Opakované posielanie kontextu rastie ako `O(N²)`:** model bez stavu číta pri každom kroku celý prepis,
  takže zdvojnásobenie počtu krokov približne zoštvornásobí náklady na vstup. Najviac ušetríš skrátením
  kontextu.
- **Prompt caching potrebuje stabilný prefix** — nemenný obsah na začiatku, premenlivý na konci a počas úlohy
  ho neupravuj. Neustále meniaci sa alebo nafúknutý korpus pravidiel zruší zľavu, takže hygiena korpusu
  riadi náklady aj kvalitu.
- **Offline prácu spracuj cez batch** (hromadné evaly, transformácie korpusu) a využi výraznú zľavu;
  interaktívne kroky doň nepatria. Rozhoduje, či na výsledok čaká človek.
- **Daň za opakovania:** `cost_per_accepted ≈ attempt_cost / p`. Lacnejší model sa oplatí iba vtedy, keď
  `p_cheap / p_expensive > price_cheap / price_expensive` — spoľahlivosť musí vyvážiť rozdiel v cene.
- **Úsporu na tokenoch obmedzuje ich podiel na účte.** Zľava nemení cenu ľudskej revízie ani externých zdrojov nástrojov.

**[Nové pojmy](../../glossary.md#cost-and-the-economics-of-agent-work)**: rozklad nákladov pokusu, asymetria vstupnej a výstupnej sadzby, kvadratické opakované posielanie kontextu, prompt caching (stabilný prefix), zľava za batch, daň za opakovania, hranica rentability podľa úspešnosti, Amdahlovo obmedzenie úspor na tokenoch.
