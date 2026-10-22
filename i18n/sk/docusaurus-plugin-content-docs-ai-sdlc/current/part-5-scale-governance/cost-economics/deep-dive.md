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

Pri generovaní v jednom pokuse sa tokeny účtujú ako dva prúdy s odlišnými sadzbami, sčítané za všetky jeho kroky: **vstup** (všetko, čo
odosielaš — systémový prompt, pravidlá, zadanie, predchádzajúce kroky, výsledky nástrojov) a **výstup** (to, čo
model vygeneruje). Výstup zvyčajne stojí za token niekoľkonásobne viac než vstup, a preto ľudia sledujú najmä
jeho. Pri práci agentov je však objem vstupu násobne väčší než objem výstupu, takže vyšší účet napokon vytvorí
lacnejší prúd tokenov:

```text
attempt_cost = input_tokens × input_rate + output_tokens × output_rate
```

Tu `attempt_cost` znamená iba náklady na tokeny generovania. Do úplných nákladov na prijatú zmenu pripočítaj externé zdroje nástrojov, overovanie a ľudskú revíziu.

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

Na ilustráciu nákladov na tokeny predpokladaj, že každý pokus stojí rovnakú sumu, výsledky pokusov sú nezávislé a pravdepodobnosť úspechu `p` je stále rovnaká, pričom `0 < p ≤ 1`. Ak opakuješ až do úspechu bez obmedzenia počtu pokusov, očakávaný počet pokusov je `1/p`. Samotná úspešnosť prvého pokusu tieto predpoklady nepotvrdzuje. V tomto zjednodušenom modeli platí:

```text
token_cost_per_accepted = attempt_cost / p
```

Tu `attempt_cost` stále zahŕňa iba tokeny pri generovaní. Porovnaj dva modely podľa tejto položky. Prvý stojí `C` za pokus a uspeje s pravdepodobnosťou `0.8`, takže očakávané náklady na tokeny generovania na prijatú zmenu sú `C / 0.8 = 1.25 C`. Druhý stojí `0.5 C` za pokus:

| Pravdepodobnosť úspechu lacnejšieho modelu za pokus | Očakávané náklady na tokeny generovania na prijatú zmenu | Oproti 1,25 C za tokeny |
|---|---|---|
| 0,40 | 0,5 C / 0,40 = 1,25 C | rovnaké náklady |
| 0,50 | 0,5 C / 0,50 = 1,00 C | nižšie náklady na tokeny |
| 0,30 | 0,5 C / 0,30 = 1,67 C | vyššie náklady na tokeny |

V tomto modeli sú náklady na tokeny na prijatú zmenu nižšie, keď `p_cheap / p_expensive > price_cheap / price_expensive`. Každá cena tu znamená náklady na tokeny generovania za pokus. Pri polovičnej cene musí pravdepodobnosť úspechu presiahnuť polovicu pravdepodobnosti druhého modelu, teda `0.40`. Táto hranica porovnáva náklady na tokeny, nie celkové náklady.

Pri úplnom porovnaní zahrň všetkých päť položiek z prvej časti: kontext, opakované pokusy a prerábanie, overovanie, ľudskú revíziu a externé zdroje nástrojov. Zohľadni, kedy každý výdavok vzniká, a ten istý výdavok nezapočítaj dvakrát. Opakovaný pokus môže použiť kontext z cache, znova spustiť platené výpočty, vyžiadať ďalšie overenie alebo pomoc človeka. Tieto rozdiely môžu obrátiť poradie modelov podľa celkovej ceny. Ak je počet opakovaní obmedzený, náklady pokusov sa menia alebo sú ich výsledky závislé, meraj všetky výdavky za prijaté aj opustené behy na prijatú zmenu. Geometrický odhad vtedy nemôžeš použiť bez úpravy.

## Položka, ktorú zľava na tokenoch nezmení \{#the-line-a-token-discount-cannot-touch}

Zľava na tokenoch zlacní generovanie a overovanie modelom, sama však nezníži cenu ľudskej revízie ani externých zdrojov nástrojov. Úsporu ohraničuje podiel účtu, ktorý sa skutočne platí v tokenoch. Ak revízia tvorí 40% a externé výpočty 30%, aj úplné odstránenie zvyšného účtu za tokeny ušetrí najviac 30%, pokiaľ ostatné náklady zostanú rovnaké. Priepustnosť môžu obmedzovať ľudia aj externé služby. Pred výberom optimalizácie zmeraj ich podiely.

## Čo si odniesť \{#what-to-take-away}

- **Rozlož náklady na tokeny generovania:** `input_tokens × input_rate + output_tokens × output_rate` je iba časť nákladov. Väčší objem vstupu môže v účte za tokeny prevážiť nad nižšou sadzbou.
- **Opakované posielanie kontextu rastie ako `O(N²)`:** model bez stavu číta pri každom kroku celý prepis,
  takže zdvojnásobenie počtu krokov približne zoštvornásobí náklady na vstup. Najviac ušetríš skrátením
  kontextu.
- **Prompt caching potrebuje stabilný prefix** — nemenný obsah na začiatku, premenlivý na konci a počas úlohy
  ho neupravuj. Neustále meniaci sa alebo nafúknutý korpus pravidiel zruší zľavu, takže hygiena korpusu
  riadi náklady aj kvalitu.
- **Offline prácu spracuj cez batch** (hromadné evaly, transformácie korpusu) a využi výraznú zľavu;
  interaktívne kroky doň nepatria. Rozhoduje, či na výsledok čaká človek.
- **Odhad nákladov na tokeny pri opakovaní:** `token_cost_per_accepted = attempt_cost / p` predpokladá nezávislé pokusy s rovnakou cenou, nemennou pravdepodobnosťou úspechu a bez limitu opakovaní. Nerovnosť cien a úspešnosti porovnáva iba tokeny; pre celkovú cenu porovnaj všetkých päť položiek aj ich náklady pri opakovaní.
- **Úsporu na tokenoch obmedzuje ich podiel na účte.** Zľava nemení cenu ľudskej revízie ani externých zdrojov nástrojov.

**[Nové pojmy](../../glossary.md#cost-and-the-economics-of-agent-work)**: rozklad nákladov pokusu, asymetria vstupnej a výstupnej sadzby, kvadratické opakované posielanie kontextu, prompt caching (stabilný prefix), zľava za batch, daň za opakovania, hranica rentability podľa úspešnosti, Amdahlovo obmedzenie úspor na tokenoch.
