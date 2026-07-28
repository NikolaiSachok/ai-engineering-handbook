---
id: overview
title: Časť II — Slučka
sidebar_label: Prehľad časti
---

# Časť II — Slučka

I. časť priniesla jedno obmedzenie: softvér vytváraný agentmi obmedzuje overovanie, nie generovanie. II. časť
naň odpovedá slučkou, ktorá voľne využíva lacné generovanie a vzácnu kapacitu overovania sústreďuje iba tam,
kde môže zmeniť výsledok.

Päť lekcií postupne odpovedá na jednu otázku: kde sa v skutočnosti využíva **kapacita overovania**? Najprv
rozhoduje podoba plánu, pretože etapa musí určovať kontrolovateľnú podmienku dokončenia, nie iba opisovať
krok. Potom veľkosť jednotky, pretože prácu dokážeš kontrolovať iba po jednotkách, na ktoré si ju rozdelil.
Ďalej záleží na tom, čo prechádza každou hranicou. Rozhodnutie zachytené iba v rozhovore nemožno skontrolovať
ani zobraziť ako zmenu v kóde (diff). Nasledujú dve brány: plán skontroluješ pred začatím práce a hotovú prácu
posúdi kritik skôr, než sa začlení do výsledku. Napokon stojíš nad slučkou a smeruješ prácu, nie v nej ako
ďalšia etapa.

Celou časťou prechádza jeden rozpor. Zámerne zostáva bez riešenia, pretože definitívne riešenie nemá. Písomné
artefakty umožňujú slučku kontrolovať, no ak ich neriadiš, ju zahltia. Zahltenie artefaktmi niekto naozaj
zmeral. Čím jemnejšie rozkladáš prácu, tým viac narastá. Prvý, koho z procesu vytlačí, je človek, ktorému mali
artefakty slúžiť. Preto túto časť čítaj ako úvahu o tom, koľko informácií zaznamenať, nielen ktoré.

## Čo je vnútri

- **[Od vízie k overiteľným etapám](./vision-to-stages.md)** — každej etape priraď podmienku dokončenia,
  ktorú vieš potvrdiť bez toho, aby si musel veriť agentovi. Uprednostni kontrolu, ktorej výsledok nemožno
  spochybniť, a podľa nej urči rozsah etapy.
- **[Atomárne úlohy: dekompozícia ako nástroj kontroly](./atomic-tasks.md)** — atomárna úloha je najväčšia
  jednotka, ktorú ešte dokážeš overiť pri jednom čítaní. Pri väčšej už stav „hotovo“ posudzuješ iba na základe
  úsudku. Pri menšej si réžia koordinácie vyžiada viac úsilia než samotná práca.
- **[Artefakty ako jediné rozhranie](./artifacts-interface.md)** — medzi etapami odovzdávaj iba artefakty
  uložené na disku, nie obsah rozhovoru. Pri ďalšej etape obnov kontext z trvalého artefaktu namiesto
  prenášania zhrnutia.
- **[Plán, kontrola, implementácia, kritik](./plan-review-implement-critic.md)** — nosná lekcia tejto časti.
  Predstaví dve rozhodujúce brány, generovanie medzi nimi a kritika, ktorý nikdy nesmie byť tým istým agentom,
  ktorého prácu kontroluje.
- **[Roly a miesto človeka](./roles-and-the-human.md)** — tvojím miestom nie je ďalšia etapa slučky: stojíš
  nad ňou a smeruješ prácu. Spoznáš tri nevyhnutné kontrolné body aj dôvod, prečo kontrola všetkého vedie
  k mechanickému schvaľovaniu namiesto skutočného dohľadu.

## Predpoklady

Z I. časti nepotrebuješ všetko. Rozhodujú dve myšlienky: samotné **úzke miesto overovania** a rozlíšenie
**výpočtová kontrola verzus kontrola založená na úsudku** z lekcie *Pravidlá, ktoré platia*. Prvá lekcia
tejto časti sa na toto rozlíšenie priamo odvoláva a znova ho neodvodzuje. Vrstvenie znalostí z lekcie *Pamäť
projektu a vrstvenie znalostí* poskytuje užitočné pozadie k zahlteniu artefaktmi, no nie je nevyhnutným
predpokladom.

## Čo sa mení po tejto časti

Dokážeš z plánu vyčítať, či podľa neho môžeš spustiť agentov. Vieš posúdiť, či každá etapa pomenúva to, čo po
nej bude platiť, či veľkosť jednotiek zodpovedá kontrole, ktorú naozaj dokážeš vykonať, a či cez niektorú
hranicu neprechádza niečo, čo nikto nedokáže skontrolovať. Zároveň si vieš určiť vlastné miesto v práci.
Rozpoznáš kontrolné body, ktoré musíš prevziať ty, pretože ich nemôže prevziať nikto ani nič iné, aj tie,
ktoré môžeš odovzdať bez narušenia dôveryhodnosti slučky.

:::note[Stav]

II. časť je hotová — publikovaných je všetkých päť lekcií. Táto časť nemá prehĺbený druhý prechod. Bránu
slučky podrobne rozoberá III. časť. Platformu, na ktorej slučka beží, rozoberá IV. časť.

:::
