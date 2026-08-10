---
id: overview
title: Časť V — Škálovanie a správa
sidebar_label: Prehľad časti
---

# Časť V — Škálovanie a správa

Doteraz sme opisovali jediný pracovný tok: slučku, reťaz brán a podkladovú platformu. V. časť skúma, čo
prestane fungovať, keď takýchto tokov spustíš naraz viac. Narazíš na štyri stropy a ani jeden neurčuje
výpočtová kapacita.

*Kde to leží na [mape kurzu](../intro.md#course-map): tri úrovne zrelosti, čítané naprieč každým prvkom slučky.*

Prvým je **zdieľanie**. Agenti môžu pracovať paralelne iba vtedy, keď nezdieľajú stav. Typický konflikt má
prozaickú príčinu. V jednom pracovnom strome môže byť aktívna vždy iba jedna vetva, preto v ňom práca
dvoch agentov na dvoch vetvách nie je z princípu možná. Riešením je spoločný stav odstrániť, nie riadiť
prístup k nemu. Druhým stropom je **zastarávanie**. Pravidlá a pamäť projektu zachytávajú podobu kódovej
základne, ktorá sa stále mení. Zastarané pravidlo je horšie než nijaké, pretože človek nad neaktuálnou
konvenciou mávne rukou, no agent ju poslušne dodrží. Tretím stropom sú **náklady**. Ešte pred výškou
výdavkov treba vyriešiť menovateľ. Jednotkou sú náklady na *prijatú* zmenu a do čitateľa patria opakované
pokusy, volania overovacích mechanizmov aj čas ľudí venovaný kontrole. Štvrtým stropom je **dôkaz**.
Úroveň enterprise, ktorou sa uzatvárala každá lekcia kurzu, sa konečne stáva hlavnou témou. Jej mechanizmy
spravidla nie sú účinnejšie, no ich uplatnenie sa dá preukázať.

V. časť tak v iných podobách rozvíja hlavnú tézu I. časti. S dvojnásobným počtom agentov dostaneš
dvojnásobný objem výstupu aj dvojnásobne dlhý rad čakajúci na kontrolu. Kapacita na jeho spracovanie sa však
s nimi nezdvojnásobí — tvorí ju reťaz brán a človek, ktorý prácu smeruje. Za každým zo štyroch stropov je
rovnaké obmedzenie, len zakaždým vytvára iný druh nákladov.

## Čo je vnútri

- **[Flotily agentov: izolácia a paralelizmus](./agent-fleets.md)** — zdieľaný stav vynúti sériové
  spracovanie. Oddeľ pracovné priestory, no artefakty, do ktorých postupne pribúdajú zmeny, spracúvaj
  sériovo. Veľkosť flotily prispôsob kapacite overovacej reťaze.
- **[Kontrola driftu a zastarávanie pravidiel](./drift-and-rot.md)** — neaktuálnosť, rozpory a nadbytočný
  obsah. Keď vykonateľné pravidlo zastará, prejaví sa to chybou. Pravidlo zapísané v próze môže zastarať
  bez akéhokoľvek signálu a agent ho bude ďalej dodržiavať.
- **[Náklady a ekonomika práce agentov](./cost-economics/index.md)** — počítaj náklady na prijatú zmenu,
  nie na token. Pri kalkulácii sa často zabúda na náklady na kontext. Vyššie výdavky však samy nezvýšia
  množstvo času, ktoré ľudia dokážu venovať kontrole.
- **[Enterprise úroveň: audit, pôvod a čo je povinné](./enterprise-tier/index.md)** — záverečná lekcia
  sa venuje nepopierateľnosti a pôvodu, v ktorom je zaznamenané, ktorý agent a ktorý model. Venuje sa aj
  oddeleniu právomocí, keď sú agentmi obe strany.

## Predpoklady

Najprv potrebuješ úzke miesto overovania z I. časti, tentoraz ako tvrdenie o *kapacite*, nie o kvalite. Prvá
lekcia podľa neho priamo určuje hornú hranicu veľkosti flotily. Potrebuješ aj pamäť projektu a pravidlá,
ktoré platia, z I. časti. Celá druhá lekcia skúma, čo sa s nimi stane, keď sa kódová základňa ďalej mení.
Lekcia o nákladoch vyčísli, čo stoja sémantické brány z III. časti a prístupové údaje pre jednotlivé úlohy
zo IV. časti. Záverečná lekcia vychádza z argumentácie III. časti o oddelení právomocí.

## Čo sa mení po tejto časti

Veľkosť flotily dokážeš určiť podľa kapacity reťaze brán, nie podľa rozpočtu. Vieš tiež určiť, aký podiel
práce sa nedá paralelizovať. Dokážeš vyčísliť náklady na súbor pravidiel namiesto toho, aby si sa iba
sťažoval na jeho kvalitu. Napokon rozlíšiš kontrolu na úrovni enterprise, ktorá naozaj niečomu **zabráni**, od
kontroly, ktorá to má **dokázať**. Vďaka tomuto rozdielu vieš obhájiť prvý typ a druhý už neodmietať ako
iba formalitu.

:::note[Stav]

V. časť je hotová a publikované sú všetky štyri lekcie. Zároveň uzaviera celý kurz. Lekcie **Náklady a
ekonomika práce agentov** a **Enterprise úroveň** majú aj prehĺbenú druhú časť. Dostaneš sa k nej cez odkaz
„Ďalej — druhá časť lekcie“ na konci ktorejkoľvek z nich. Zvyšné dve lekcie tvorí vždy jediná stránka.

:::
