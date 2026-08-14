---
title: "Enterprise úroveň — prehĺbenie"
sidebar_label: "SLSA, SBOM a podpísaný pôvod"
sidebar_position: 2
---

# Ako vzniká dôkaz

[Prvá časť](./index.md) vysvetlila, že na enterprise úrovni sa kontrola počíta iba vtedy, keď niekto iný než
jej vykonávateľ dokáže spätne preukázať, že prebehla — rozhoduje dôkaz, nie samotná existencia mechanizmu.
Pomenovala audit, nepopierateľnosť, pôvod a oddelenie právomocí a technické riešenie nechala na úrovni SBOM na
to, čo dnu vstúpilo, a podpísaných potvrdení na to, čo to vyrobilo. Táto stránka rozoberá konkrétne rámce,
pretože práve detaily sú na tejto úrovni podstatné: rebrík sily pôvodu (SLSA), dva štandardy súpisu (SPDX a
CycloneDX), podpisovú vrstvu, ktorá záznamom dáva nepopierateľnosť (in-toto a Sigstore), a otázku agentov, s
ktorou žiadny z týchto rámcov pôvodne nepočítal. Na konci príde poctivé vymedzenie ich možností, pretože práve
tie sa zvyknú zveličovať.

## SLSA: pôvod ako rebrík, nie políčko na odškrtnutie

Pôvod nie je binárna vlastnosť; môže mať rôznu silu a buildová vetva
[SLSA](https://slsa.dev/spec/v1.0/levels) ju vyjadruje číslami. Jednotlivé úrovne čítaj ako odpovede na otázku
„aké ťažké je tento pôvod sfalšovať“ (`ASSERTED` podľa špecifikácie):

- **Build L1** — artefakt obsahuje údaje o pôvode, ktoré opisujú, ako vznikol. Nemusia byť podpísané. Úroveň
  zachytí neúmyselné chyby, no sfalšovať ju je triviálne. Presne na to slúži: je základom, nie ochranou.
- **Build L2** — údaje o pôvode **podpisuje hostovaná buildová platforma**, takže na ich sfalšovanie už nestačí
  chyba v konfigurácii, ale treba platformu skutočne napadnúť. Build beží v prostredí, ktoré ho podpisuje za
  teba.
- **Build L3** — platforma je **odolná proti manipulácii, jednotlivé buildy sú navzájom izolované a kroky
  buildu definované používateľom nemajú prístup k podpisovému kľúču.** Pre flotilu je rozhodujúca posledná
  podmienka: proces, ktorý *vykonáva build*, sa nedostane ku kľúču, ktorý *potvrdzuje jeho dôveryhodnosť*.

Tento rebrík premieňa pravidlo o blast radius (rozsah škôd) na infraštruktúru: každý stupeň poskytuje silnejší
dôkaz za reálnu cenu a vystúpiš iba tak vysoko, ako odôvodňuje vzdialenosť od blast radius. Pri práci agentov má
oddelenie na L3 jednoznačný dôsledok — **agent, ktorý vygeneroval kód, nesmie držať kľúč potvrdzujúci jeho
pôvod**. Je to ten istý argument pre oddelenie právomocí ako v
[prvej časti](./index.md), no namiesto vyhlásenia v politike ho teraz vynucuje platforma.

## SBOM: súpis v jednom z dvoch formátov

**Súpis softvérových súčastí (software bill of materials, SBOM)** uvádza všetko, čo vstúpilo do artefaktu —
každú závislosť, verziu a licenciu. Keď sa zverejní nová zraniteľnosť, namiesto vyšetrovania stačí vyhľadanie
v súpise. Prevládajú dva štandardy, ktoré vznikli v odlišných prostrediach (`ASSERTED`):

- **[SPDX](https://spdx.dev/)** — štandard Linux Foundation (a zároveň ISO/IEC 5962), ktorý modeluje balíky a
  vzťahy medzi nimi; historicky sa sústreďuje na súlad a licencie.
- **[CycloneDX](https://cyclonedx.org/)** — štandard OWASP s kompaktným modelom zameraným na komponenty,
  bezpečnosť a zraniteľnosti; postupne zahrnul aj služby, modely ML a kryptografiu.

Voľba medzi nimi má význam, no nie je prvoradá. Podstatné je, aby SBOM existoval, generoval ho build namiesto
ručného zapisovania a zostával aktuálny. Kód generovaný agentmi túto potrebu ešte zvyšuje: flotila pridáva
závislosti strojovým tempom, takže súpis, ktorý by si človek možno neformálne udržal v hlave, musí vznikať
automaticky. Inak jednoducho nebude správny.

## in-toto a Sigstore: odkiaľ prichádza nepopierateľnosť

SBOM aj záznam o pôvode sú iba dokumenty, kým ich niečo nespojí s buildom a neznemožní ich dodatočnú úpravu.
Tak dostáva konkrétnu podobu požiadavka **nepopierateľnosti (non-repudiation)** z prvej časti. Zabezpečujú ju
dve súčasti:

- **[Potvrdenia in-toto](https://in-toto.io/)** tvoria obálku: podpísané vyhlásenie v tvare *tento predmet
  (artefakt určený hashom) má tento obsah tvrdenia (jeho pôvod alebo SBOM)*. Záznam o pôvode podľa SLSA je sám
  osebe obsahom tvrdenia in-toto a rovnakým spôsobom možno zabaliť SBOM v ktoromkoľvek z oboch formátov —
  obálka od konkrétneho formátu nezávisí.
- **[Sigstore](https://www.sigstore.dev/)** (prostredníctvom `cosign`) tvorí podpisovú vrstvu. Jeho praktickým
  mechanizmom je **podpisovanie bez dlhodobého kľúča (keyless signing)**: namiesto dlhodobého kľúča, ktorý musí
  niekto strážiť, vydá krátkodobý certifikát previazaný cez OIDC s identitou pracovného procesu a podpis
  zaznamená do verejného transparency log. Takéto krátkodobé oprávnenie viazané na identitu uplatňuje
  [princíp najnižších oprávnení](../../part-4-platform/least-privilege-sandboxing/index.md) zo IV. časti priamo
  na podpisovanie.

Spolu odpovedajú na tri otázky, ktoré sa ľahko zamieňajú: SBOM hovorí, *čo je vnútri*, pôvod opisuje, *ako a
čím artefakt vznikol*, a podpis dokazuje, že *záznam nemožno poprieť ani zmeniť*. Záznam, ktorý môže operátor
dodatočne upraviť, je iba rozprávanie; podpis, ktorý nedokázal vytvoriť jeho vlastný buildový krok, je dôkaz.

## Oddelenie právomocí, keď sú obe strany agentmi

Prvá časť zdôvodnila oddelenie právomocí inžiniersky a následne aj požiadavkami na súlad. Konkrétne mechanizmy
obe odôvodnenia spájajú. Podmienka SLSA L3, podľa ktorej kroky buildu definované používateľom nemajú prístup k
podpisovému kľúču, a klasická **revízia dvoma stranami** — jeden aktér vytvára, iný schvaľuje — uplatňujú
rovnaký princíp v rozličných vrstvách. Vo flotile fungujú iba vtedy, keď majú aktéri **skutočne odlišné
identity a prihlasovacie údaje** a záznam jednoznačne ukazuje ich úlohy. Generujúci agent beží pod jednou
identitou, revidujúci pod druhou a schválenie človekom predstavuje skutočný podpis konkrétnej osoby.

Práve posledná podmienka odhaľuje typické zlyhanie tejto úrovne. Treba ho pomenovať priamo, pretože podpis už
má právny význam. Keď človek schvaľuje zmeny rýchlejšie, než ich dokáže reálne prečítať, nejde o dohľad, ale o
zlyhanie [kontroly pri veľkom objeme](../../part-3-verification/review-at-volume.md) doplnené podpisom na účely
súladu. Mechanizmus vie preukázať, že schválenie nastalo; nevie zaručiť, že bolo poctivé. O to sa musia
postarať nižšie vrstvy.

## Poctivé vymedzenie: pôvod nie je správnosť

Tieto mechanizmy dokazujú presne vymedzenú skutočnosť a bežnou chybou je pripisovať im viac. Artefakt s úplnými
potvrdeniami, úrovňou SLSA L3, súpisom SBOM a podpisom Sigstore môže byť stále **chybný** — nezabezpečený,
plný chýb alebo nenápadne nesprávny. Pôvod odpovedá na otázku „vznikol tento nezmenený artefakt z daného zdroja
určeným procesom?“. Nehovorí nič o jeho kvalite. Tú posudzuje celý zvyšok kurzu:
[reťaz brán](../../part-3-verification/layered-gates/index.md), testy a revízia. Integrita dodávateľského
reťazca a správnosť softvéru sú od seba nezávislé; aj program, ktorý dôkladne zabezpečil prvú z nich, môže
vydať chybu s dokonale doloženým pôvodom.

Táto úroveň teda odôvodňuje svoje náklady svojou pozíciou, nie nadradenosťou. Leží najďalej od blast radius,
kde potrebuješ *dôkaz*, a ten si vyžaduje skutočnú infraštruktúru — dôveryhodnú buildovú platformu, podpisovú
službu, transparency log a pipeline na tvorbu súpisu. Po rebríku vystúp iba tak vysoko, ako si vyžadujú
dôsledky prípadného zlyhania. Silu dôkazu o pôvode si nikdy nezamieňaj s kvalitou artefaktu, ktorému tento
pôvod patrí.

## Čo si odniesť

- **SLSA je rebrík, nie políčko na odškrtnutie:** na L1 údaje o pôvode existujú, ale dajú sa sfalšovať; na L2
  ich podpisuje hostovaná platforma, takže sfalšovanie vyžaduje útok; na L3 je podpisový kľúč **neprístupný
  krokom buildu definovaným používateľom** — vo flotile teda agent, ktorý artefakt vytvoril, nemôže potvrdiť
  jeho pôvod.
- **SBOM je súpis** v jednom z dvoch formátov — SPDX (Linux Foundation, súlad a licencie) alebo CycloneDX
  (OWASP, bezpečnosť a zraniteľnosti). Musí ho **generovať build**, pretože flotila pridáva závislosti
  rýchlejšie, než ich ktokoľvek dokáže sledovať ručne.
- **in-toto a Sigstore zabezpečujú nepopierateľnosť:** in-toto je podpísaná obálka, ktorá hashom viaže obsah
  tvrdenia k artefaktu; podpisovanie bez dlhodobého kľúča v Sigstore viaže podpis na krátkodobé poverenie
  vydané pod identitu pracovného procesu — princíp najnižších oprávnení uplatnený na podpisovanie.
- **Tri odpovede nemožno zlúčiť do jednej:** SBOM = *čo je vnútri*, pôvod = *ako artefakt vznikol*, podpis =
  *nemožno ho zmeniť ani poprieť*.
- **Oddelenie právomocí vyžaduje odlišné identity,** ktoré vynucuje platforma, a schválenie, ktoré človek naozaj
  mohol vykonať — inak ide o zlyhanie kontroly pri veľkom objeme doplnené právne významným podpisom.
- **Pôvod nie je správnosť.** Tieto mechanizmy dokazujú pôvod a integritu artefaktu, nikdy nie jeho kvalitu;
  aj artefakt s úplnými potvrdeniami môže byť chybný, preto potrebuješ celý zvyšok kurzu.

**[Nové pojmy](../../glossary.md#the-enterprise-tier-audit-provenance-and-whats-required)**: buildové úrovne SLSA (L1/L2/L3), podpisový kľúč neprístupný krokom buildu definovaným používateľom, formáty SBOM (SPDX / CycloneDX), potvrdenie in-toto, Sigstore / podpisovanie bez dlhodobého kľúča, transparency log, pôvod verzus správnosť, oddelenie právomocí pomocou odlišných identít.
