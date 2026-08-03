---
title: "Prierezové aspekty"
slug: /part-1-rag/cross-cutting/
---

# To, čo nepatrí žiadnej jednej fáze

Ingestion, retrieval aj generation majú v pipeline svoje miesto — okamih, kedy sa dejú. Tri veci ho
nemajú. Nedá sa ukázať na krok, v ktorom sa systém stane dôveryhodným, bezpečným alebo priehľadným:
tieto vlastnosti sú buď zabudované v každej fáze, alebo nie sú nikde. Práve preto sú prierezové, a
nie štvrtá, piata a šiesta fáza.

Sú to zároveň tie tri, ktoré odlišujú demo od produkcie. Preto stoja na konci prvej časti a preto sa
na ne na pohovoroch pýtajú najviac.

## Čo je vnútri

- **[Evaluácia](./evaluation/index.md)** — ako zistíš, že systém funguje, namiesto toho, aby si tomu
  veril. Vyhľadávanie a generovanie sa kazia inak a opravujú sa inými pákami, takže sa aj merajú
  zvlášť. Týmto je dobré začať: bez čísla je každá ďalšia zmena v pipeline odhad, ktorý „pôsobí
  lepšie“.
- **[Guardrails](./guardrails/index.md)** — ako ho udržíš bezpečný. Model nevie spoľahlivo odlíšiť
  inštrukciu od dát, takže všetko, čo sa dostane do kontextu, je niečo, čo môže poslúchnuť.
  Guardrails sú presne tá vrstva na vstupe a na výstupe, ktorá s tým počíta.
- **[Observabilita](./observability/index.md)** — ako uvidíš, čo systém robí, keď ho už majú skutoční
  používatelia. Tracy, spany a vzorkovanie premenia „kvalita klesla“ na „klesla *tu*, začalo sa to
  *vtedy*, kvôli *tejto* zmene“ — a zlyhávajúce tracy, ktoré sa tým nájdu, sa stanú novými prípadmi
  pre evaluáciu.

Každá z tých troch je lekcia plus **hĺbkový rozbor**: lekcia dá pracovný model, rozbor ide o vrstvu
nižšie, k mechanizmom a k tomu, ako sa to láme. Odkaz „Ďalej — 2. časť lekcie“ nájdeš na konci každej
lekcie.

Poradie nie je náhodné. Evaluácia prvá, lebo guardrails aj observabilita produkujú signály, ktoré sú
bez niečoho na porovnanie bezcenné. Observabilita posledná, lebo uzatvára kruh: to, na čom systém
padne v produkcii, sa stane tým, čo evaluácia testuje nabudúce.
