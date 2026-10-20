---
id: overview
title: Časť V — Škálovanie a správa
sidebar_label: Prehľad časti
---

# Časť V — Škálovanie a správa

Doteraz sme opisovali jediný pracovný tok: slučku, reťaz brán a podkladovú platformu. V. časť skúma, čo
prestane fungovať, keď takýchto tokov spustíš naraz viac. Narazíš na štyri stropy a ani jeden neurčuje
výpočtová kapacita. Pridáva sa k nim jedno riziko na strane poskytovateľa, ktoré existuje aj pri jedinom pracovnom toku: model je závislosť, ktorú ovláda niekto iný.

*Kde to leží na [mape kurzu](../intro.md#course-map): tri úrovne zrelosti, čítané naprieč každým prvkom slučky.*

Prvým je **zdieľanie**. Agenti môžu pracovať paralelne iba vtedy, keď nezdieľajú stav. Typický konflikt má
prozaickú príčinu. V jednom pracovnom strome môže byť aktívna vždy iba jedna vetva, preto v ňom práca
dvoch agentov na dvoch vetvách nie je z princípu možná. Riešením je spoločný stav odstrániť, nie riadiť
prístup k nemu. Druhým stropom je **zastarávanie**. Pravidlá a pamäť projektu zachytávajú podobu kódovej
základne, ktorá sa stále mení. Zastarané pravidlo je horšie než nijaké, pretože človek nad neaktuálnou
konvenciou mávne rukou, no agent ju poslušne dodrží. Rovnako sa, jedna rozumná oprava za druhou, rozpadá aj
samotná štruktúra kódu. Zabrániš tomu iba vtedy, ak každá oprava vychádza z rozhodnutí, ktoré túto štruktúru
určujú, a zároveň automatické kontroly overujú nosné hranice. Tretím stropom sú **náklady**. Ešte pred výškou
výdavkov treba vyriešiť menovateľ. Jednotkou sú náklady na *prijatú* zmenu a do čitateľa patria opakované
pokusy, volania overovacích mechanizmov aj čas ľudí venovaný kontrole. Štvrtým stropom je **dôkaz**.
Úroveň enterprise, ktorou sa uzatvárala každá lekcia kurzu, sa konečne stáva hlavnou témou. Jej mechanizmy
spravidla nie sú účinnejšie, no ich uplatnenie sa dá preukázať.

V. časť tak v iných podobách rozvíja hlavnú tézu I. časti. S dvojnásobným počtom agentov dostaneš
dvojnásobný objem výstupu aj dvojnásobne dlhý rad čakajúci na kontrolu. Kapacita na jeho spracovanie sa však
s nimi nezdvojnásobí — tvorí ju reťaz brán a človek, ktorý prácu smeruje. Za každým zo štyroch stropov je
rovnaké obmedzenie, len zakaždým vytvára iný druh nákladov. Výnimkou je závislosť od modelu: toto riziko leží u poskytovateľa, na druhej strane volania API. Služba sa môže zmeniť alebo zmiznúť, aj keď tvoja kapacita zostane rovnaká.

## Čo je vnútri

- **[Flotily agentov: izolácia a paralelizmus](./agent-fleets.md)** — zdieľaný stav vynúti sériové
  spracovanie. Oddeľ pracovné priestory, no artefakty, do ktorých postupne pribúdajú zmeny, spracúvaj
  sériovo. Veľkosť flotily prispôsob kapacite overovacej reťaze.
- **[Kontrola driftu a zastarávanie pravidiel](./drift-and-rot.md)** — neaktuálnosť, rozpory a nadbytočný
  obsah. Keď vykonateľné pravidlo zastará, prejaví sa to chybou. Pravidlo zapísané v próze môže zastarať
  bez akéhokoľvek signálu a agent ho bude ďalej dodržiavať.
- **[Erózia architektúry](./architecture-erosion.md)** — štruktúru kódu narúša jedna rozumná oprava za druhou.
  Zaznamenaj rozhodnutie pred zmenou, nosné hranice overuj fitness funkciami a sériu opráv, z ktorých každá
  opravuje predchádzajúcu, ber ako spúšťač prepracovania návrhu, nie celkového prepisu.
- **[Náklady a ekonomika práce agentov](./cost-economics/index.md)** — počítaj náklady na prijatú zmenu,
  nie na token. Pri kalkulácii sa často zabúda na náklady na kontext. Vyššie výdavky však samy nezvýšia
  množstvo času, ktoré ľudia dokážu venovať kontrole.
- **[Model ako závislosť: pripnutie, upgrady, odchod a podmienky pre dáta](./model-dependency.md)** — pripni verziu, preveruj upgrady a udržiavaj vyskúšanú možnosť odchodu. Volanie API môže byť úspešné aj vtedy, keď pracovný tok, ktorému slúži, už nefunguje.
- **[Enterprise úroveň: audit, pôvod a čo je povinné](./enterprise-tier/index.md)** — záverečná lekcia
  sa venuje nepopierateľnosti a pôvodu, v ktorom je zaznamenané, ktorý agent a ktorý model. Venuje sa aj
  oddeleniu právomocí, keď sú agentmi obe strany.

## Predpoklady

Najprv potrebuješ úzke miesto overovania z I. časti, tentoraz ako tvrdenie o *kapacite*, nie o kvalite. Prvá
lekcia podľa neho priamo určuje hornú hranicu veľkosti flotily. Potrebuješ aj pamäť projektu a pravidlá, ktoré
platia, z I. časti. Celá druhá lekcia skúma, čo sa s nimi stane, keď sa kódová základňa ďalej mení. Tretia
lekcia nadväzuje na cyklus s kritikom z II. časti, pretože kritikovi dáva okrem diffu aj denník rozhodnutí.
Lekcia o nákladoch vyčísli, čo stoja sémantické brány z III. časti, a zo IV. časti si preberá prihlasovacie údaje
vydávané na úlohu, aby sa výdavky dali priradiť. Lekcia o modeli ako závislosti využíva pri smerovaní [hranicu rentability z prehĺbenia o nákladoch](./cost-economics/deep-dive.md). [Pamäť projektu](../part-1-foundation/project-memory-and-tiering.md) z I. časti v nej vystupuje ako predpoklad toho, aby si mohol od poskytovateľa odísť. Na lekcie o [secrets](../part-4-platform/secrets.md) a [prostrediach](../part-4-platform/environments-migrations-data.md) zo IV. časti lekcia nadväzuje otázkou, čo sa deje s dátami, ktoré sa dostanú k poskytovateľovi. Záverečná lekcia vychádza z argumentácie III. časti o
oddelení právomocí.

## Čo sa mení po tejto časti

Veľkosť flotily dokážeš určiť podľa kapacity reťaze brán, nie podľa rozpočtu. Vieš tiež určiť, aký podiel
práce sa nedá paralelizovať. Dokážeš vyčísliť náklady na súbor pravidiel namiesto toho, aby si sa iba
sťažoval na jeho kvalitu. Dokážeš zariadiť, aby porušenie nosnej hranice zastavilo zostavenie, a nemusíš
sa spoliehať, že ju dodrží každá oprava. Upgrade modelu dokážeš preveriť ako upgrade ktorejkoľvek inej závislosti a od poskytovateľa odísť vtedy, keď sa rozhodneš ty, nie keď ti to určí on. Napokon rozlíšiš kontrolu na úrovni enterprise, ktorá naozaj
niečomu **zabráni**, od kontroly, ktorá to má **dokázať**. Vďaka tomuto rozdielu vieš obhájiť prvý typ
a druhý už neodmietať ako iba formalitu.

:::note[Stav]

V. časť je hotová a publikovaných je všetkých šesť lekcií. Zároveň uzaviera celý kurz. Lekcie **Náklady a
ekonomika práce agentov** a **Enterprise úroveň** majú aj prehĺbenú druhú časť. Dostaneš sa k nej cez odkaz
„Ďalej — druhá časť lekcie“ na konci ktorejkoľvek z nich. Zvyšné štyri lekcie tvorí vždy jediná stránka.

:::
