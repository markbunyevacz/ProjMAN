# AI Transformation Playbook (3 az 1-ben)

## 1. PMO-rész átdolgozva, konkrét ROI-számításokkal

### 1.1. PMO szerepe az AI-transzformációban
- A PMO (Project Management Office) kulcsszerepet játszik az AI bevezetésének koordinálásában, a projektek priorizálásában, a változásmenedzsmentben és a sikeres implementációban.
- Feladatai közé tartozik a projektcélok meghatározása, az erőforrások allokálása, a mérföldkövek követése és a megtérülés (ROI) folyamatos monitorozása.

### 1.2. ROI-számítási módszertan
- **ROI képlet:**
  
  ```math
  ROI = \frac{(AI által megtakarított idő \times óradíj \times hónapok száma) - bevezetési költség}{bevezetési költség}
  ```

- **Példa ROI-számítás:**
  - AI agent bevezetése után a meetingek adminisztrációjára fordított idő havi 20 óráról 5 órára csökken.
  - Óradíj: 10 000 Ft
  - Hónapok száma: 12
  - Bevezetési költség: 1 200 000 Ft
  - Megtakarítás: (20-5) × 10 000 × 12 = 1 800 000 Ft
  - ROI = (1 800 000 - 1 200 000) / 1 200 000 = 0,5 (azaz 50% megtérülés 1 év alatt)

- **További ROI-faktorok:**
  - Hibák számának csökkenése
  - Gyorsabb döntéshozatal
  - Elégedettség növekedése

## 2. Agentize technikai támogatás leírása use case-ekkel

### 2.1. Technikai támogatás
- Agentize biztosítja az AI agentek telepítését, integrációját, testreszabását és folyamatos támogatását.
- Felhőalapú vagy on-premise megoldások.
- Biztonság, adatvédelem, auditálhatóság.

### 2.2. Use case-ek
- **Meeting Assistant**
  - Automatikus jegyzőkönyv generálás
  - Action itemek követése
  - E-mail értesítések
- **PMO Report Generator**
  - Excel/Jira adatokból vezetői összefoglaló készítése
  - Grafikonok, statisztikák automatikus generálása

### 2.3. Workflow példa
1. Meeting után a Meeting Assistant automatikusan elkészíti a jegyzőkönyvet és kiküldi az action itemeket.
2. A PMO Report Generator heti rendszerességgel összegzi a projektállapotot a vezetőség számára.

## 3. 90 napos implementációs ütemterv (minta)

| Időszak      | Fő tevékenységek                                      |
|-------------|-------------------------------------------------------|
| 1-30 nap    | Igényfelmérés, pilot agent(ek) kiválasztása, bevezetés|
| 31-60 nap   | Testreszabás, tréning, finomhangolás                  |
| 61-90 nap   | Teljes körű bevezetés, mérés, visszacsatolás          |

---

A következő lépésben elkészítem a Proof of Value kit részletes leírását és sablonjait is.

# 2. Proof of Value kit

## 2.1. AI agentek az első ügyféltalálkozóhoz

### Meeting Assistant
- **Funkciók:**
  - Meeting jegyzőkönyv automatikus generálása (összefoglaló, résztvevők, döntések, action itemek)
  - Action itemek követése, státusz riportálása
  - E-mail értesítések a felelősöknek
- **Demo workflow példa:**
  1. Meeting rögzítése (pl. Teams/Zoom vagy jegyzet feltöltése)
  2. AI automatikusan elkészíti a jegyzőkönyvet, kiemeli a feladatokat
  3. Résztvevők e-mailben megkapják a jegyzőkönyvet és a saját action itemjeiket

#### Jegyzőkönyv sablon (példa)
```markdown
## Meeting Jegyzőkönyv
- **Dátum:** 2025-11-14
- **Résztvevők:** Név1, Név2, Név3

### Főbb döntések
- ...

### Action itemek
| Feladat           | Felelős | Határidő   | Státusz   |
|-------------------|---------|------------|-----------|
| ...               | ...     | ...        | ...       |
```

### PMO Report Generator
- **Funkciók:**
  - Excel vagy Jira adatokból automatikus vezetői összefoglaló generálása
  - Grafikonok, trendek, státuszok
- **Demo workflow példa:**
  1. Projektadatok feltöltése (Excel vagy Jira API)
  2. AI összefoglaló és vizualizáció generálása
  3. PDF/Word riport exportálása

#### Vezetői összefoglaló sablon (példa)
```markdown
## PMO Vezetői Összefoglaló
- **Időszak:** 2025. november
- **Projekt:** Projekt neve

### Főbb mérőszámok
| Mutató           | Érték   |
|------------------|---------|
| Készültség (%)   | 85%     |
| Késés (nap)      | 2       |
| Kockázatok száma | 3       |

### Főbb események
- ...

### Ajánlott akciók
- ...
```

## 2.2. Demo videók és beállítási útmutató vázlat

- **Demo videók:**
  - Rövid, 1-2 perces bemutatók a Meeting Assistant és a PMO Report Generator működéséről
  - Főbb lépések: input feltöltés, AI feldolgozás, output letöltés

- **Beállítási útmutató (példa):**
  1. Agent regisztráció az Agentize platformon
  2. Integráció beállítása (Teams/Zoom/Jira/Excel)
  3. Jogosultságok megadása
  4. Első teszt futtatása
  5. Eredmények ellenőrzése, testreszabás

---

Következő lépés: Success Metrics keretrendszer és ROI-kalkulátor sablon hozzáadása.

# 3. Success Metrics keretrendszer

## 3.1. AI-bevezetés mérési módszertana

- **Főbb mérőszámok (KPI-ok):**
  - Időmegtakarítás (pl. adminisztrációs idő csökkenése)
  - Hibák számának csökkenése
  - Felhasználói elégedettség (survey-k)
  - Automatizált folyamatok aránya
  - Projektkésések csökkenése

- **Mérés gyakorisága:**
  - Havi/Negyedéves riportok
  - Folyamatos monitoring (dashboard)

- **Adatforrások:**
  - Projektmenedzsment rendszerek (Jira, MS Project, Excel)
  - Meeting logok, action tracking
  - Felhasználói visszajelzések

## 3.2. ROI-kalkulátor sablon ügyféltalálkozókhoz

### Excel/Google Sheets sablon leírás

- **Bemeneti adatok:**
  - AI által megtakarított idő (óra/hó)
  - Átlagos óradíj (Ft/óra)
  - Hónapok száma
  - Bevezetési költség (Ft)

- **Kimenet:**
  - Összes megtakarítás
  - ROI (%)

#### ROI-kalkulátor sablon (táblázat)

| Paraméter                | Érték példa   | Ügyfél adata |
|--------------------------|--------------|--------------|
| AI által megtakarított idő (óra/hó) | 15           |              |
| Átlagos óradíj (Ft/óra)            | 10 000       |              |
| Hónapok száma                      | 12           |              |
| Bevezetési költség (Ft)            | 1 200 000    |              |
| **Összes megtakarítás (Ft)**       | 1 800 000    |              |
| **ROI (%)**                        | 50%          |              |

**ROI képlet:**

```
ROI = ((megtakarított idő * óradíj * hónapok száma) - bevezetési költség) / bevezetési költség
```

**Letölthető sablon:**
- [ROI-kalkulátor Excel sablon](link-helye.xlsx)
- [ROI-kalkulátor Google Sheets sablon](link-helye)

---

Ez a Playbook teljes körűen támogatja az AI-transzformációs projektek előkészítését, bemutatását és mérését.