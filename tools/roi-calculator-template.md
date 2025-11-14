# ROI Kalkulátor Sablon
## Ügyféltalálkozókhoz - Excel/Google Sheets sablon útmutató

---

## Áttekintés

Ez a ROI-kalkulátor sablon segít az ügyfeleknek saját adataikkal kiszámolni a várható ROI-t az AI-ügynökök bevezetése esetén. A sablon előre kitöltött példákkal rendelkezik, hogy könnyen érthető legyen.

---

## Használati útmutató

### 1. Excel/Google Sheets sablon struktúra

A sablon a következő munkalapokat tartalmazza:
- **Befektetés (Investment)**: Minden költség kategória
- **Megtakarítás (Savings)**: Időmegtakarítás és költségcsökkentés
- **ROI számítás**: Automatikus számítások
- **Összefoglaló (Summary)**: Főbb eredmények

### 2. Lépésről lépésre kitöltés

#### Lépés 1: Befektetés kategóriák kitöltése

**1.1 Szoftver licenc díjak**

| Kategória | Érték | Megjegyzés |
|-----------|-------|------------|
| Agentize platform előfizetés (havonta) | €500 | Meeting Assistant + PMO Report Generator |
| Éves licenc díj | =B2*12 | Automatikus számítás |

**Kitöltési útmutató:**
- Add meg a havi licenc díjat (ez változhat a csomagtól függően)
- Az éves licenc díj automatikusan számolódik

**Példa értékek:**
- Meeting Assistant csak: €300/hó
- PMO Report Generator csak: €300/hó
- Kombinált: €500/hó

**1.2 Implementációs költségek**

| Kategória | Óra | Óradíj (EUR) | Összesen (EUR) |
|-----------|-----|--------------|----------------|
| Konfiguráció és testreszabás | 60 | €100 | =B5*C5 |
| Tréning és onboarding | 30 | €100 | =B6*C6 |
| Integrációk (Jira, Excel, Teams) | 20 | €100 | =B7*C7 |
| **Összesen** | | | =SUM(D5:D7) |

**Kitöltési útmutató:**
- Becsüld meg az órákat a projekt méretétől függően
- Add meg az óradíjat (ez változhat a szolgáltatótól függően)
- Az összesen automatikusan számolódik

**Példa értékek (kis projekt - 20 fő):**
- Konfiguráció: 40 óra
- Tréning: 20 óra
- Integrációk: 10 óra

**Példa értékek (nagy projekt - 100+ fő):**
- Konfiguráció: 80 óra
- Tréning: 40 óra
- Integrációk: 20 óra

**1.3 Folyamatos karbantartás**

| Kategória | Érték | Megjegyzés |
|-----------|-------|------------|
| Havonta karbantartás (óra) | 8 | |
| Óradíj (EUR) | €100 | |
| Éves karbantartás | =B10*B11*12 | Automatikus számítás |

**Kitöltési útmutató:**
- Becsüld meg a havi karbantartási időt (általában 5-10 óra)
- Add meg az óradíjat
- Az éves karbantartás automatikusan számolódik

**1.4 Összes befektetés (első év)**

| Kategória | Érték (EUR) |
|-----------|-------------|
| Éves licenc díj | =B3 |
| Implementáció | =D8 |
| Éves karbantartás | =B12 |
| **Összesen** | =SUM(B15:B17) |

---

#### Lépés 2: Megtakarítás kategóriák kitöltése

**2.1 Meeting Assistant - Időmegtakarítás**

| Kategória | Előtte (óra/hét) | Utána (óra/hét) | Megtakarítás (óra/hét) | Felhasználók száma | Összes megtakarítás (óra/hét) |
|-----------|------------------|-----------------|------------------------|-------------------|------------------------------|
| Jegyzőkönyv készítés | 2.5 | 0.25 | =B22-C22 | 10 | =D22*E22 |
| Action item tracking | 1.5 | 0.15 | =B23-C23 | 10 | =D23*E23 |
| Meeting előkészítés | 1 | 0.5 | =B24-C24 | 10 | =D24*E24 |
| **Összesen** | | | | | =SUM(F22:F24) |

**Kitöltési útmutató:**
- Add meg az előtte értékeket (mennyi időt töltesz most ezekkel a feladatokkal)
- Add meg az utána értékeket (mennyi időt fogsz tölteni az AI-val)
- Add meg a felhasználók számát
- A megtakarítás automatikusan számolódik

**Példa értékek:**
- Jegyzőkönyv: 2-3 óra → 10-15 perc (0.25 óra)
- Action tracking: 1-2 óra → 5-10 perc (0.15 óra)
- Előkészítés: 1 óra → 30 perc (0.5 óra)

**2.2 PMO Report Generator - Időmegtakarítás**

| Kategória | Előtte (óra/hét) | Utána (óra/hét) | Megtakarítás (óra/hét) | Felhasználók száma | Összes megtakarítás (óra/hét) |
|-----------|------------------|-----------------|------------------------|-------------------|------------------------------|
| Riport készítés | 5 | 0.75 | =B28-C28 | 2 | =D28*E28 |
| Adatgyűjtés | 2 | 0 | =B29-C29 | 2 | =D29*E29 |
| Adatelemzés | 1 | 0.25 | =B30-C30 | 2 | =D30*E30 |
| **Összesen** | | | | | =SUM(F28:F30) |

**Kitöltési útmutató:**
- Ugyanaz, mint a Meeting Assistant-nál
- PMO Report Generator esetén általában kevesebb felhasználó van (2-5 fő)

**2.3 Költség megtakarítás számítása**

| Kategória | Megtakarítás (óra/hét) | Hetek száma/év | Összes megtakarítás (óra/év) | Átlagos óradíj (EUR) | Költség megtakarítás (EUR/év) |
|-----------|------------------------|----------------|------------------------------|---------------------|-------------------------------|
| Meeting Assistant | =F25 | 50 | =B34*C34 | 80 | =D34*E34 |
| PMO Report Generator | =F31 | 50 | =B35*C35 | 100 | =D35*E35 |
| **Összesen** | | | | | =SUM(F34:F35) |

**Kitöltési útmutató:**
- A megtakarítás automatikusan jön a fenti táblázatokból
- Add meg a hetek számát évente (általában 50)
- Add meg az átlagos óradíjat (ez változhat a pozíciótól függően)
- A költség megtakarítás automatikusan számolódik

**Példa óradíjak:**
- Meeting menedzser: €70-€90/óra
- PMO szakember: €90-€120/óra
- Projektmenedzser: €80-€100/óra

**2.4 További megtakarítások**

| Kategória | Érték (EUR/év) | Megjegyzés |
|-----------|----------------|------------|
| Hibák csökkentése | 3000 | Manuális adatbevitel hibák csökkentése |
| Gyorsabb döntéshozatal | 5000 | Információ gyorsabb elérhetősége |
| Szinergia hatások | 2000 | Jobban koordinált projektek |
| **Összesen** | =SUM(B39:B41) | |

**Kitöltési útmutató:**
- Ezek nehezebben mérhető megtakarítások
- Becsüld meg konzervatívan
- Opcionális, de ajánlott figyelembe venni

---

#### Lépés 3: ROI számítás

**3.1 Alapadatok**

| Kategória | Érték (EUR) |
|-----------|-------------|
| Összes befektetés (első év) | =B18 |
| Időmegtakarítás alapú megtakarítás | =F36 |
| További megtakarítások | =B42 |
| **Összes megtakarítás** | =SUM(C46:C47) |

**3.2 ROI számítás**

| Metrika | Képlet | Érték |
|---------|--------|-------|
| Nettó megtakarítás (EUR) | =C48-C45 | Automatikus |
| ROI (%) | =((C48-C45)/C45)*100 | Automatikus |
| Payback period (hónap) | =(C45/C48)*12 | Automatikus |

**3.3 Értelmezés**

**ROI értelmezés:**
- **> 200%**: Kiváló ROI, erősen ajánlott
- **100-200%**: Jó ROI, ajánlott
- **50-100%**: Elfogadható ROI, érdemes megfontolni
- **< 50%**: Alacsony ROI, részletesebb elemzés szükséges

**Payback period értelmezés:**
- **< 3 hónap**: Nagyon gyors megtérülés
- **3-6 hónap**: Gyors megtérülés
- **6-12 hónap**: Elfogadható megtérülés
- **> 12 hónap**: Lassú megtérülés

---

## Példa számítások

### Példa 1: Kis projekt (20 fős csapat)

**Befektetés:**
- Licenc: €500/hó × 12 = €6,000/év
- Implementáció: 60 óra × €100 = €6,000
- Karbantartás: 8 óra/hó × €100 × 12 = €9,600/év
- **Összesen**: €21,600

**Megtakarítás:**
- Meeting Assistant: 5 óra/hét × 50 hét × €80 = €20,000/év
- PMO Report Generator: 8 óra/hét × 50 hét × €100 = €40,000/év
- További megtakarítások: €5,000/év
- **Összesen**: €65,000/év

**ROI:**
- Nettó megtakarítás: €65,000 - €21,600 = €43,400
- ROI: (€43,400 / €21,600) × 100 = **201%**
- Payback period: (€21,600 / €65,000) × 12 = **4 hónap**

### Példa 2: Nagy projekt (100+ fős csapat)

**Befektetés:**
- Licenc: €800/hó × 12 = €9,600/év
- Implementáció: 100 óra × €100 = €10,000
- Karbantartás: 10 óra/hó × €100 × 12 = €12,000/év
- **Összesen**: €31,600

**Megtakarítás:**
- Meeting Assistant: 25 óra/hét × 50 hét × €80 = €100,000/év
- PMO Report Generator: 10 óra/hét × 50 hét × €100 = €50,000/év
- További megtakarítások: €20,000/év
- **Összesen**: €170,000/év

**ROI:**
- Nettó megtakarítás: €170,000 - €31,600 = €138,400
- ROI: (€138,400 / €31,600) × 100 = **438%**
- Payback period: (€31,600 / €170,000) × 12 = **2.2 hónap**

---

## Excel/Google Sheets sablon létrehozása

### Excel sablon létrehozása

1. **Új munkafüzet létrehozása**
   - Nyisd meg az Excel-t
   - Hozz létre egy új munkafüzetet

2. **Munkalapok létrehozása**
   - "Befektetés" munkalap
   - "Megtakarítás" munkalap
   - "ROI számítás" munkalap
   - "Összefoglaló" munkalap

3. **Formázás**
   - Használj fejléceket és színezést
   - Formázd a számokat (pénznem, tizedesjegyek)
   - Használj feltételes formázást (pl. zöld ha ROI > 200%)

4. **Képletek beillesztése**
   - Másold be a fenti képleteket
   - Teszteld a számításokat példa adatokkal

### Google Sheets sablon létrehozása

1. **Új táblázat létrehozása**
   - Nyisd meg a Google Sheets-t
   - Hozz létre egy új táblázatot

2. **Ugyanaz, mint az Excel-nél**
   - Munkalapok, formázás, képletek

3. **Megosztás**
   - Állítsd be a megosztást (csak megtekintés vagy szerkesztés)
   - Küldd el az ügyfélnek

---

## Használati tippek

### Ügyféltalálkozókon

1. **Előre készülj fel**: Töltsd ki a sablont példa adatokkal
2. **Interaktív használat**: Mutasd be a sablont, majd kérdezd meg az ügyfelet, hogy töltse ki saját adataival
3. **Valós példák**: Használj valós példákat az ügyfél szervezetéből
4. **Konzervatív becslések**: Jobb konzervatív becsléseket használni, mint túl optimistákat

### Sablon testreszabása

1. **Szervezeti igények**: Testreszabd a sablont a szervezeti igényekhez
2. **További metrikák**: Adj hozzá további metrikákat, ha szükséges
3. **Vizualizációk**: Adj hozzá grafikonokat és diagramokat
4. **Nyelvek**: Fordítsd le a sablont a helyi nyelvre

---

## Következő lépések

### Rövid távú (0-7 nap)
1. Excel/Google Sheets sablon létrehozása
2. Példa adatokkal való tesztelés
3. Formázás és vizualizációk hozzáadása

### Közép távú (8-30 nap)
1. Ügyféltalálkozókon való használat
2. Visszajelzések gyűjtése
3. Sablon finomhangolása

### Hosszú távú (31+ nap)
1. Sablon folyamatos fejlesztése
2. További metrikák hozzáadása
3. Best practices dokumentálása

---

*Dokumentum verzió: 1.0*  
*Utolsó frissítés: 2025-01-XX*

