---
id: overview
title: Časť IV — Platforma
sidebar_label: Prehľad časti
---

# Časť IV — Platforma

Časti I až III sa venovali práci v slučke: plánovaniu, dekompozícii, generovaniu a bránam. IV. časť sa
presúva k platforme pod ňou. Tá určuje, aké škody môže spôsobiť chyba. Vetu *pokyn nie je kontrola*
z I. časti tu použijeme štyrikrát: na to, čo agent uchováva, kam dosiahne, s akými dátami pracuje a ako
rýchlo sa dá jeho zmena zastaviť, keď už beží. Pre túto vrstvu znie tá istá zásada takto: **vynucovanie
zabezpečuje platforma, nikdy prompt.**

*Kde to leží na [mape kurzu](../intro.md#course-map): pôda, na ktorej slučka beží — vrstva, ktorá ohraničuje škodu z chyby.*

Postupujeme od najmenšieho zdroja, ktorý môžeš agentovi odoprieť. Najprv ide o prihlasovací údaj, ktorý
agent vôbec nesmie mať. Pri programovacom agentovi môže uniknúť oveľa ľahšie než pri práci vývojára. Agent
číta celý strom súborov, odosiela ho poskytovateľovi modelu a zapisuje svoje uvažovanie do logov. To, čo
prečítal, môže zopakovať aj tam, kam sa nikdy nepozrieš. Ďalšia lekcia rieši prístup, ktorý oprávnene má.
Rozlišuje dve často zamieňané kontroly: rozsah pridelených oprávnení a izolované prostredie, v ktorom agent
beží. Zlyhávajú odlišne, preto sa dopĺňajú. Nasledujú dáta, ktoré sú dosť realistické na užitočnú prácu, no
nie natoľko skutočné, aby boli nebezpečné. Zmeny schémy musia mať cestu späť, ktorú si naozaj vyskúšal.
Napokon príde na rad to, ako sa zmena prejaví po nasadení.

Posledná lekcia uzatvára slučku načrtnutú v úvode. Produkcia neprichádza „po overení“, ale
predstavuje **koncovú bránu reťaze** a telemetria slúži ako jej snímač. Každý defekt, ktorý sa dostane až
sem, je únikom. Patrí do registra z III. časti spolu s názvom brány, ktorá ho nezachytila.

## Čo je vnútri

- **[Secrets](./secrets.md)** — samotná hodnota sa nedostane do repozitára ani do kontextu agenta.
  Uchovávaj iba odkaz, hodnotu vkladaj až počas behu, blokuj ju na strane servera a namiesto vymazania ju
  rotuj.
- **[Najnižšie oprávnenia a sandbox](./least-privilege-sandboxing/index.md)** — nastav rozsah pridelených
  oprávnení štyrmi parametrami. Potom predpokladaj, že prompt injection uspeje, a priprav systém tak, aby to
  prežil. Pokyn neudeľuje oprávnenie.
- **[Prostredia, migrácie a reálne dáta](./environments-migrations-data.md)** — pracuj s realistickými, nie
  skutočnými dátami. Schému meň v poradí expand → migrate → contract. Záloha, ktorej obnovenie si nikdy
  nevyskúšal, nie je záloha.
- **[Pozorovateľnosť, nasadzovanie a núdzový vypínač](./observability-rollout.md)** — niekoľko signálov
  sleduj dôkladne. Postupné nasadenie spoj s automatickým vrátením zmeny. Núdzový vypínač má meniť stav,
  nie spúšťať nový build.

## Predpoklady

Veta z úvodu pochádza z lekcie *Pravidlá, ktoré platia* v I. časti. Všetky štyri lekcie túto zásadu
uplatňujú na úrovni platformy a viaceré odkazujú na tie isté incidenty. Preto ti tu tá jedna lekcia dá viac
než II. a III. časť spolu. Rozmanitosť mechanizmov z III. časti sa tu uplatní dvakrát. Deterministický
skener na secrets dopĺňa kontrolu pri revízii; sandbox sa zas dopĺňa s rozsahom pridelených oprávnení. Z
III. časti preto potrebuješ prvú lekciu aj register únikov. Posledná lekcia tejto časti doň zapisuje vždy,
keď sa chyba dostane do produkcie.

## Čo sa mení po tejto časti

Pri každom agentovi, ktorého spustíš, budeš vedieť štyri odpovede podložiť faktmi o platforme, nie sľubmi:
čo uchováva, kam dosiahne, s akými dátami pracuje a za aký čas ho dokáže jediný človek zastaviť bez toho,
aby musel čokoľvek nanovo zostavovať. Enterprise mechanizmy na správu prihlasovacích údajov už nebudeš
považovať za formalitu. Krátkodobé prihlasovacie údaje viazané na konkrétnu pracovnú záťaž a zoznamy
povolenej odchádzajúcej komunikácie určujú, čo systém smie robiť. Existujú preto, že lacné riešenie
preukázateľne zlyhalo.

:::note[Stav]

IV. časť je hotová — publikované sú všetky štyri lekcie. **Najnižšie oprávnenia a sandbox** obsahuje aj
prehĺbenú druhú časť o vrstvách izolácie, vďaka ktorým systém prežije prompt injection. Dostaneš sa k nej
cez odkaz „Ďalej — druhá časť lekcie“ na konci tejto lekcie. Každá z ostatných troch lekcií má jedinú
stránku.

:::
