---
id: overview
title: Časť I — Základ
sidebar_label: Prehľad časti
---

# Časť I — Základ

Hlavnou tézou kurzu je, že softvér vytváraný agentmi neobmedzujú schopnosti modelu, ale **kapacita
overovania**. I. časť túto tézu odvodzuje z dôkazov a ukazuje jej dôsledok. Takmer všetko, čím môžeš toto
obmedzenie zmierniť, musíš urobiť skôr, než agent napíše prvý riadok. V tejto časti nie je žiadny kód a
vychádza z nej celý zvyšok kurzu.

Časť má dve línie. Prvé dve lekcie ti pomôžu určiť, čomu možno veriť. Dostaneš namerané dáta, podľa ktorých
objem výstupu rastie, no kvalita aj porozumenie klesajú a sebahodnotenie zlyháva. Zároveň získaš nástroj,
ktorým každé tvrdenie o tejto téme zaradíš podľa sily dôkazu. Ďalšie tri lekcie tvoria samotný základ:
prípravu, ktorú agentovi poskytneš, pamäť, s ktorou pracuje, a pravidlá, ktoré nedokáže obísť presviedčaním.

Tieto tri súčasti pripravuješ vopred a všetky majú **obmedzenú životnosť**. Harness (lešenie agenta) je
postavený na predpokladoch o modeli, ktoré so zlepšovaním modelov prestávajú platiť. Pamäťový súbor nezostáva
iba uložený: model ho dostáva pri každom kroku znova a podľa meraní to zvyšuje náklady na inferenciu o viac
než 20% na krok. Bez vlastníka pravidlá postupne strácajú konzistentnosť, až napokon dva súbory, ktoré oba
platia ako záväzné, predpisujú protichodné architektúry. Príprava sa musí opakovať. Práve toto ľudia pri
zásade „príprava je dôležitejšia než model“ vynechávajú.

## Čo je vnútri

- **[Úzke miesto overovania](./verification-bottleneck.md)** — téza podložená prvotnými zdrojmi: objem výstupu
  rastie a tento výsledok sa opakuje, kvalita aj porozumenie klesajú a sám na sebe nedokážeš spoľahlivo
  rozpoznať ani jeden z týchto účinkov.
- **[Ako posudzovať dôkazy](./reading-the-evidence.md)** — rebrík `MEASURED` / `REPORTED` / `ASSERTED`, štyri
  kontroly, ktorými musí číslo prejsť, a vysvetlenie, prečo najčastejšie opakovaný údaj v určitej oblasti
  zvyčajne nedokáže nikto overiť.
- **[Príprava je dôležitejšia než model](./preparation-over-model.md)** — dôkazy ukazujú, že príprava
  a vymedzenie rozsahu ovplyvňujú úspech agenta viac ako ktorákoľvek výmena modelu. Naučíš sa tiež čítať údaj
  o úspešnosti od autora nástroja bez toho, aby si ho automaticky vzťahoval na vlastný projekt.
- **[Pamäť projektu a vrstvenie znalostí](./project-memory-and-tiering.md)** — agenti si medzi spusteniami nič
  nepamätajú, no problém spôsobuje aj zapisovanie čoraz väčšieho množstva informácií. Riešením je vrstvenie
  znalostí, nie pridávanie ďalších materiálov.
- **[Pravidlá, ktoré platia](./rules-that-hold.md)** — pokyn nie je kontrola. Agent optimalizuje práve to, čo
  kontroluješ, preto vykonateľné pravidlo nikdy nesmie zostať iba zapísané.

## Predpoklady

Z tohto kurzu nepotrebuješ nič, pretože práve tu sa začína. Predpokladáme však, že si už programovacieho
agenta použil pri skutočnej práci a vytvoril si názor na to, či ťa zrýchlil. Prvá lekcia z veľkej časti
vysvetľuje, prečo tento názor nie je dôkazom. Prines si ho so sebou a počítaj s tým, že ho možno budeš musieť
odložiť.

## Čo sa mení po tejto časti

Každé tvrdenie o produktivite v tejto oblasti dokážeš zaradiť podľa toho, aký malo menovateľ, kto výskum
financoval, či je údaj stále aktuálny a či „17%“ znamenalo percentá alebo percentuálne body. Keď máš konvenciu
zapísanú, vieš rozlíšiť kontrolu od odporúčania. Pred zadaním práce agentovi vieš pripraviť štyri podstatné
veci: ohraničený rozsah, prostredie, v ktorom agent dokáže projekt zostaviť a otestovať, pamäť rozvrstvenú
podľa skutočných potrieb úlohy a vykonateľné pravidlá.

:::note[Stav]

I. časť je hotová — publikovaných je všetkých päť lekcií. Nemá samostatnú prehĺbenú druhú časť. Látku,
ktorá by do nej patrila, preberajú priamo časti II–V a každú z piatich myšlienok uplatňujú v jednej z etáp
slučky.

:::
