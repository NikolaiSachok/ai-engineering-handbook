---
id: overview
title: Časť III — Overovanie
sidebar_label: Prehľad časti
---

# Časť III — Overovanie

V II. časti sme zaviedli bránu kritika pre všetko, čo sa malo prijať, a ďalej sme ju už nerozvíjali.
III. časť preto rozoberá podstatu brány. Postupne pritom vyvracia jednu upokojujúcu domnienku za druhou.
Týmto poradím sa riadia aj lekcie, preto ich čítaj za sebou.

*Kde to leží na [mape kurzu](../intro.md#course-map): spoje medzi krokmi slučky. Overovanie žije tam, nie vo vlastnom rámčeku.*

Najprv padne domnienka, že dôkladnosť brány zabezpečí aj pokrytie. Slepé miesto brány vyplýva z jej
*mechanizmu*, takže statický analyzátor nevyladíš tak, aby videl stav počas behu. Pokrytie získaš až vrstvením
kontrol, ktoré zlyhávajú odlišne. Podľa druhej domnienky je dobrá reťaz úplná. Nikdy nie je. Každý únik
preto zaznamenaj pri bráne, ktorá ho mala zachytiť, a doplň reťaz tak, aby ho už pokrývala. Tretia domnienka
prehliada fakt, ktorý mení samotný návrh systému. Agent optimalizuje presne to, čo kontroluješ, **proti tejto
kontrole**. Pri návrhu brány preto počítaj s tým, že agent bude hľadať spôsob, ako ju obísť. Hľadanie chyby
oddeľ od opravy a ešte skôr, než agent skratku objaví, nastav zadanie tak, aby sa mu neoplatila. Napokon
narazíš na strop kapacity človeka, ktorý rozhoduje ako posledný: jeho kapacitu škálovať nedokážeš.
Záverečná lekcia preto rieši, čo sa až k nemu dostane.

Zoznam čítaj zhora nadol — každá lekcia určuje zadanie pre nasledujúcu. Presne tento postup odporúča
prvá lekcia aj pri radení samotných brán.

## Čo je vnútri

- **[Vrstvené brány a rozmanitosť mechanizmov](./layered-gates/index.md)** — každá brána má slepé miesto.
  Pri každej jednou vetou pomenuj, čo pre svoj mechanizmus nedokáže odhaliť, a podľa tejto vety vyber
  nasledujúcu bránu.
- **[Register únikov](./escape-ledger.md)** — každá uniknutá chyba ti niečo povie o tvojej detekčnej vrstve.
  Zaznamenaj jej triedu, bránu, ktorá ju prehliadla, aj spôsob, ktorým ju odteraz pokrýva reťaz.
- **[Detekcia verzus oprava: hra na metriku](./detection-vs-mutation.md)** — audítor nikdy neupravuje to, čo
  kontroluje. Zadanie opravy zároveň výslovne pomenuje spôsob obídenia, ktorý agent nesmie použiť.
  S obchádzaním brány počítaj ako s bežným správaním, nie ako s anomáliou.
- **[Kontrola výstupu agenta pri veľkom objeme](./review-at-volume.md)** — automatizáciou sústreď pozornosť
  na to, čo automat nevidí. Potom vymenuj všetko, čo dokáže vnímať iba človek, a jeho kontrolu vyhraď výlučne
  tomuto zoznamu.

## Predpoklady

Skutočným predpokladom je **brána kritika** z II. časti. Táto časť ju rozoberá na súčasti, preto budú jej
argumenty podstatne presvedčivejšie, ak túto bránu už poznáš. Druhým východiskom je zistenie z lekcie
*Pravidlá, ktoré platia* v I. časti: agent optimalizuje presne to, čo kontroluješ. Tretia tunajšia lekcia
z tohto zistenia vychádza a dôkazy preň už znovu nerozoberá.

## Čo sa mení po tejto časti

Dokážeš navrhnúť reťaz overovania namiesto obyčajného hromadenia kontrol. Pri každej vrstve pomenuješ, čo
nedokáže vnímať, a podľa toho zvolíš ďalšiu. Zelený výsledok už nepovažuješ za dôkaz o kóde, ale za dôkaz
o bráne. Ak si ju nikdy nevidel zlyhať pri chybe, ktorú si zámerne vložil, vieš iba to, že mlčí, nie že
funguje. Prestaneš si tiež zamieňať dĺžku reťaze s rozmanitosťou. Práve táto chyba spôsobuje, že šesť brán
na kontrolu súladu nie je lepšie ako jedna.

:::note[Stav]

III. časť je hotová — publikované sú všetky štyri lekcie. Jedna z nich, **Vrstvené brány**, má aj prehĺbenú
druhú časť o meraní detekčnej sily brány a poradí reťaze. Dostaneš sa k nej cez odkaz „Ďalej — druhá časť
lekcie“ na konci tejto lekcie. Zvyšné tri sú samostatné stránky.

:::
