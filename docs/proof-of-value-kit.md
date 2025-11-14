# Proof of Value Kit
## 2 működő AI agent az első ügyféltalálkozóhoz

---

## Áttekintés

Ez a Proof of Value (PoV) kit két működő AI agent bemutatására szolgál, amelyek azonnali értéket nyújtanak a projektmenedzsment és üzleti folyamatokban. A kit tartalmazza a demo anyagokat, beállítási útmutatókat és praktikus példákat.

---

## 1. Meeting Assistant

### 1.1 Funkciók és képességek

A Meeting Assistant egy AI-alapú eszköz, amely automatikusan generál jegyzőkönyveket és követi az action item-eket meetingek után.

**Főbb funkciók:**
- ✅ Automatikus jegyzőkönyv generálás (audio/video feldolgozás)
- ✅ Action item azonosítás és hozzárendelés
- ✅ Kulcsfontosságú pontok kiemelése
- ✅ Következő lépések generálása
- ✅ Integráció Microsoft Teams, Zoom, Google Meet-tel
- ✅ Jira ticket automatikus létrehozás action item-ekből

### 1.2 Demo script

#### Demo bemutatás (10-15 perc)

**1. Bevezetés (2 perc)**
```
"Ma bemutatom a Meeting Assistant-t, amely automatikusan 
generál jegyzőkönyveket és követi az action item-eket. 
Ez körülbelül 2-3 órát takarít meg hetente meeting 
menedzsereknek."
```

**2. Működés bemutatása (5-7 perc)**

**a) Meeting előtti állapot:**
- Mutasd be a meeting beállításokat
- Agenda előkészítés (ha van előző meeting)

**b) Meeting alatt:**
- Valós idejű jegyzetelés (opcionális)
- Kulcsfontosságú pontok azonosítása

**c) Meeting után:**
- Automatikus jegyzőkönyv generálás (5-10 perc)
- Action item-ek kiemelése
- Hozzárendelések automatikus javaslata

**3. Eredmények megmutatása (3-4 perc)**
- Generált jegyzőkönyv áttekintése
- Action item-ek listája
- Jira ticket-ek (ha integrálva van)

**4. ROI bemutatása (2 perc)**
- Időmegtakarítás: 2-3 óra/meeting → 10-15 perc ellenőrzés
- Költségmegtakarítás számítás

### 1.3 Demo videó útmutató

#### Videó 1: Meeting Assistant - Gyors bemutatás (3-5 perc)

**Tartalom:**
1. **Bevezetés** (30 mp)
   - Mi a Meeting Assistant?
   - Milyen problémát old meg?

2. **Működés bemutatása** (2-3 perc)
   - Meeting előtti állapot
   - Meeting alatt (valós idejű jegyzetelés)
   - Meeting után (automatikus generálás)

3. **Eredmények** (1-2 perc)
   - Generált jegyzőkönyv
   - Action item-ek
   - Integrációk

4. **Összefoglalás** (30 mp)
   - Főbb előnyök
   - Időmegtakarítás

**Felvételi útmutató:**
- Használj képernyőfelvételt (Screen recording)
- Mutasd be a valós felhasználói felületet
- Használj valós példa meeting-et (vagy szimulált)
- Legyenek magyarázatok a háttérben

#### Videó 2: Meeting Assistant - Részletes beállítás (10-15 perc)

**Tartalom:**
1. **Beállítások áttekintése** (2-3 perc)
   - Platform bejelentkezés
   - Alapvető konfigurációk

2. **Integrációk beállítása** (5-7 perc)
   - Microsoft Teams integráció
   - Zoom integráció (opcionális)
   - Jira integráció (action item-ekhez)

3. **Testreszabás** (3-5 perc)
   - Jegyzőkönyv sablonok
   - Action item formátumok
   - Email értesítések

**Felvételi útmutató:**
- Lépésről lépésre bemutatás
- Képernyőképek minden lépésnél
- Gyakori hibák és megoldásaik

### 1.4 Beállítási útmutató (lépésről lépésre)

#### 1.4.1 Előfeltételek

**Szükséges:**
- Agentize platform hozzáférés
- Microsoft Teams / Zoom / Google Meet fiók
- Jira hozzáférés (opcionális, action item tracking-hez)

**Rendszerkövetelmények:**
- Internet kapcsolat
- Modern webböngésző (Chrome, Edge, Firefox)
- Mikrofon hozzáférés (ha valós idejű jegyzetelés)

#### 1.4.2 Beállítás lépései

##### Lépés 1: Agentize platform bejelentkezés

1. Nyisd meg a böngészőt és lépj be az Agentize platformra
   ```
   URL: https://platform.agentize.com
   ```

2. Jelentkezz be a megadott hitelesítő adatokkal
   - Email cím: [megadott email]
   - Jelszó: [megadott jelszó]

3. Válaszd ki a "Meeting Assistant" agent-et a dashboard-ról

**Képernyőkép helye:** `screenshots/meeting-assistant/01-login.png`

##### Lépés 2: Alapvető konfiguráció

1. Kattints a "Settings" (Beállítások) gombra

2. Töltsd ki az alapvető információkat:
   - **Szervezet neve**: [szervezet neve]
   - **Időzóna**: [pl. Europe/Budapest]
   - **Alapértelmezett nyelv**: Magyar / Angol

3. Mentsd el a beállításokat

**Képernyőkép helye:** `screenshots/meeting-assistant/02-settings.png`

##### Lépés 3: Microsoft Teams integráció

1. A Settings menüben válaszd ki az "Integrations" (Integrációk) fület

2. Kattints a "Microsoft Teams" opcióra

3. Kattints a "Connect" (Csatlakozás) gombra

4. Jelentkezz be a Microsoft Teams fiókoddal és engedélyezd a hozzáférést

5. Válaszd ki, mely meetingeket szeretnéd követni:
   - Összes meeting
   - Csak kijelölt kalendárok
   - Csak meghívott meetingek

6. Mentsd el a beállításokat

**Képernyőkép helye:** `screenshots/meeting-assistant/03-teams-integration.png`

##### Lépés 4: Jira integráció (opcionális)

1. Az Integrations menüben válaszd ki a "Jira" opciót

2. Add meg a Jira URL-t:
   ```
   Példa: https://yourcompany.atlassian.net
   ```

3. Add meg az API token-t vagy használj OAuth hitelesítést

4. Válaszd ki a projektet, ahová az action item-eket szeretnéd küldeni

5. Teszteld a kapcsolatot a "Test Connection" gombbal

6. Mentsd el a beállításokat

**Képernyőkép helye:** `screenshots/meeting-assistant/04-jira-integration.png`

##### Lépés 5: Jegyzőkönyv sablon testreszabása

1. A Settings menüben válaszd ki a "Templates" (Sablonok) fület

2. Válaszd ki a "Meeting Minutes Template" opciót

3. Testreszabd a sablont:
   - Meeting információk (cím, dátum, résztvevők)
   - Agenda pontok
   - Kulcsfontosságú pontok
   - Action item-ek formátuma
   - Következő lépések

4. Előnézet: Kattints a "Preview" gombra

5. Mentsd el a sablont

**Képernyőkép helye:** `screenshots/meeting-assistant/05-template-customization.png`

##### Lépés 6: Email értesítések beállítása

1. A Settings menüben válaszd ki a "Notifications" (Értesítések) fület

2. Állítsd be, kik kapjanak értesítést:
   - Meeting résztvevők
   - Projektmenedzserek
   - Vezetőség

3. Válaszd ki, mikor küldjön értesítést:
   - Jegyzőkönyv kész
   - Action item létrehozva
   - Action item státusz változás

4. Mentsd el a beállításokat

**Képernyőkép helye:** `screenshots/meeting-assistant/06-email-notifications.png`

##### Lépés 7: Tesztelés

1. Hozz létre egy teszt meeting-et Microsoft Teams-ben

2. Vegyél részt a meeting-en (vagy használj felvételt)

3. Várj 5-10 percet a jegyzőkönyv generálására

4. Ellenőrizd a generált jegyzőkönyvet:
   - Pontosság
   - Action item-ek azonosítása
   - Formátum

5. Ha minden rendben, a Meeting Assistant készen áll a használatra!

**Képernyőkép helye:** `screenshots/meeting-assistant/07-test-results.png`

### 1.5 Gyakori problémák és megoldások

| Probléma | Lehetséges ok | Megoldás |
|----------|---------------|----------|
| Jegyzőkönyv nem generálódik | Integráció nincs beállítva | Ellenőrizd a Teams integrációt |
| Action item-ek nem azonosíthatók | Hang minőség rossz | Használj jobb mikrofont vagy felvételt |
| Jira ticket-ek nem jönnek létre | Jira integráció hibás | Teszteld a Jira kapcsolatot |
| Email értesítések nem érkeznek | Email beállítások hibásak | Ellenőrizd a Notification beállításokat |

---

## 2. PMO Report Generator

### 2.1 Funkciók és képességek

A PMO Report Generator automatikusan összegyűjti az adatokat különböző forrásokból (Jira, Excel) és generál vezetői összefoglaló riportokat.

**Főbb funkciók:**
- ✅ Automatikus adatgyűjtés Jira-ból
- ✅ Excel fájlok feldolgozása
- ✅ AI-alapú trend elemzés
- ✅ Kockázat azonosítás
- ✅ Vezetői összefoglaló generálás
- ✅ Grafikonok és diagramok automatikus létrehozása
- ✅ PDF és Excel formátumú export

### 2.2 Demo script

#### Demo bemutatás (10-15 perc)

**1. Bevezetés (2 perc)**
```
"A PMO Report Generator automatikusan összegyűjti az adatokat 
Jira-ból és Excel-ből, majd generál egy vezetői összefoglaló 
riportot. Ez körülbelül 5-6 órát takarít meg hetente PMO 
szakembereknek."
```

**2. Működés bemutatása (5-7 perc)**

**a) Adatforrások beállítása:**
- Jira projekt(ek) kiválasztása
- Excel fájl(ok) feltöltése

**b) Riport konfiguráció:**
- Riport típusa (heti, havi, negyedéves)
- KPI-k kiválasztása
- Formátum beállítása

**c) Automatikus generálás:**
- Adatgyűjtés folyamata
- AI elemzés
- Riport generálás

**3. Eredmények megmutatása (3-4 perc)**
- Generált riport áttekintése
- Grafikonok és diagramok
- Kockázatok és ajánlások

**4. ROI bemutatása (2 perc)**
- Időmegtakarítás: 5-6 óra/hét → 30-45 perc ellenőrzés
- Költségmegtakarítás számítás

### 2.3 Demo videó útmutató

#### Videó 1: PMO Report Generator - Gyors bemutatás (3-5 perc)

**Tartalom:**
1. **Bevezetés** (30 mp)
   - Mi a PMO Report Generator?
   - Milyen problémát old meg?

2. **Működés bemutatása** (2-3 perc)
   - Adatforrások beállítása
   - Riport konfiguráció
   - Automatikus generálás

3. **Eredmények** (1-2 perc)
   - Generált riport
   - Grafikonok
   - Kockázatok és ajánlások

4. **Összefoglalás** (30 mp)
   - Főbb előnyök
   - Időmegtakarítás

**Felvételi útmutató:**
- Használj képernyőfelvételt
- Mutasd be a valós felhasználói felületet
- Használj valós példa adatokat (anonymizálva)
- Legyenek magyarázatok a háttérben

#### Videó 2: PMO Report Generator - Részletes beállítás (10-15 perc)

**Tartalom:**
1. **Beállítások áttekintése** (2-3 perc)
   - Platform bejelentkezés
   - Alapvető konfigurációk

2. **Integrációk beállítása** (5-7 perc)
   - Jira integráció
   - Excel fájlok feltöltése
   - Adatforrások konfigurálása

3. **Riport testreszabás** (3-5 perc)
   - Riport sablonok
   - KPI-k kiválasztása
   - Formátum beállítások

**Felvételi útmutató:**
- Lépésről lépésre bemutatás
- Képernyőképek minden lépésnél
- Gyakori hibák és megoldásaik

### 2.4 Beállítási útmutató (lépésről lépésre)

#### 2.4.1 Előfeltételek

**Szükséges:**
- Agentize platform hozzáférés
- Jira API hozzáférés
- Excel fájlok (ha vannak)

**Rendszerkövetelmények:**
- Internet kapcsolat
- Modern webböngésző (Chrome, Edge, Firefox)

#### 2.4.2 Beállítás lépései

##### Lépés 1: Agentize platform bejelentkezés

1. Nyisd meg a böngészőt és lépj be az Agentize platformra
   ```
   URL: https://platform.agentize.com
   ```

2. Jelentkezz be a megadott hitelesítő adatokkal

3. Válaszd ki a "PMO Report Generator" agent-et a dashboard-ról

**Képernyőkép helye:** `screenshots/pmo-report-generator/01-login.png`

##### Lépés 2: Jira integráció beállítása

1. Kattints a "Settings" (Beállítások) gombra

2. Válaszd ki az "Integrations" (Integrációk) fület

3. Kattints a "Jira" opcióra

4. Add meg a Jira URL-t:
   ```
   Példa: https://yourcompany.atlassian.net
   ```

5. Add meg az API token-t vagy használj OAuth hitelesítést

6. Válaszd ki a projekt(ek)et, amelyekből adatokat szeretnél gyűjteni:
   - Projekt 1: [projekt neve]
   - Projekt 2: [projekt neve]
   - Stb.

7. Teszteld a kapcsolatot a "Test Connection" gombbal

8. Mentsd el a beállításokat

**Képernyőkép helye:** `screenshots/pmo-report-generator/02-jira-integration.png`

##### Lépés 3: Excel fájlok feltöltése (opcionális)

1. Az Integrations menüben válaszd ki az "Excel Files" opciót

2. Kattints a "Upload Files" (Fájlok feltöltése) gombra

3. Válaszd ki az Excel fájlokat a számítógépedről

4. Állítsd be, hogyan legyenek feldolgozva:
   - Automatikus feldolgozás
   - Manuális mezőleképezés

5. Mentsd el a beállításokat

**Képernyőkép helye:** `screenshots/pmo-report-generator/03-excel-upload.png`

##### Lépés 4: Riport sablon testreszabása

1. A Settings menüben válaszd ki a "Report Templates" (Riport sablonok) fület

2. Válaszd ki a "Executive Summary Template" opciót

3. Testreszabd a sablont:
   - **Riport címe**: [pl. Heti PMO Összefoglaló]
   - **KPI-k**: Válaszd ki a követendő KPI-kat
     - Projekt státuszok
     - Késések száma
     - Költségvetés állapota
     - Kockázatok
   - **Grafikonok**: Válaszd ki a megjelenítendő grafikonokat
   - **Színséma**: Válaszd ki a színsémát

4. Előnézet: Kattints a "Preview" gombra

5. Mentsd el a sablont

**Képernyőkép helye:** `screenshots/pmo-report-generator/04-template-customization.png`

##### Lépés 5: Ütemezés beállítása

1. A Settings menüben válaszd ki a "Schedule" (Ütemezés) fület

2. Állítsd be a riport generálás gyakoriságát:
   - Heti (pl. minden hétfőn 9:00-kor)
   - Havi (pl. minden hónap első napján)
   - Negyedéves (pl. minden negyedév első napján)
   - Manuális (csak kézzel indítható)

3. Add meg a címzetteket:
   - Vezetőség email címei
   - PMO csapat email címei

4. Mentsd el a beállításokat

**Képernyőkép helye:** `screenshots/pmo-report-generator/05-schedule.png`

##### Lépés 6: Tesztelés

1. Kattints a "Generate Report" (Riport generálása) gombra

2. Válaszd ki a riport típusát:
   - Heti összefoglaló
   - Havi összefoglaló
   - Egyedi időszak

3. Várj 2-5 percet a riport generálására

4. Ellenőrizd a generált riportot:
   - Adatok pontossága
   - Grafikonok helyessége
   - Kockázatok azonosítása
   - Formátum

5. Ha minden rendben, a PMO Report Generator készen áll a használatra!

**Képernyőkép helye:** `screenshots/pmo-report-generator/06-test-results.png`

### 2.5 Gyakori problémák és megoldások

| Probléma | Lehetséges ok | Megoldás |
|----------|---------------|----------|
| Jira adatok nem töltődnek be | API token hibás | Ellenőrizd a Jira API token-t |
| Excel fájlok nem dolgozódnak fel | Formátum nem támogatott | Konvertáld XLSX formátumra |
| Grafikonok nem jelennek meg | Adatok hiányoznak | Ellenőrizd az adatforrásokat |
| Email nem érkezik | Email beállítások hibásak | Ellenőrizd a Schedule beállításokat |

---

## 3. Kombinált használat

### 3.1 Integrált workflow

A Meeting Assistant és PMO Report Generator együtt használva még hatékonyabb:

1. **Meeting Assistant** generál jegyzőkönyveket és action item-eket
2. **Action item-ek** automatikusan Jira ticket-ekké alakulnak
3. **PMO Report Generator** követi a ticket-ek státuszát
4. **Heti riport** tartalmazza a meeting eredményeket és action item státuszokat

### 3.2 Színergia hatások

- **Jobban koordinált projektek**: Meeting eredmények automatikusan bekerülnek a riportokba
- **Gyorsabb döntéshozatal**: Teljesebb áttekintés a vezetőség számára
- **Nagyobb időmegtakarítás**: Kombinált használat esetén 7-9 óra/hét

---

## 4. Demo anyagok checklist

### Meeting Assistant
- [ ] Demo videó (3-5 perc) - Gyors bemutatás
- [ ] Demo videó (10-15 perc) - Részletes beállítás
- [ ] Beállítási útmutató (lépésről lépésre)
- [ ] Képernyőképek (minden lépéshez)
- [ ] Gyakori problémák és megoldások dokumentáció

### PMO Report Generator
- [ ] Demo videó (3-5 perc) - Gyors bemutatás
- [ ] Demo videó (10-15 perc) - Részletes beállítás
- [ ] Beállítási útmutató (lépésről lépésre)
- [ ] Képernyőképek (minden lépéshez)
- [ ] Gyakori problémák és megoldások dokumentáció

### Kombinált használat
- [ ] Integrált workflow dokumentáció
- [ ] Színergia hatások leírása

---

## 5. Ügyféltalálkozó előkészítés

### 5.1 Előzetes felkészülés

**1 hét előtte:**
- [ ] Demo környezet előkészítése
- [ ] Teszt adatok betöltése
- [ ] Demo script átnézése
- [ ] Videók ellenőrzése

**1 nap előtte:**
- [ ] Demo környezet tesztelése
- [ ] Internet kapcsolat ellenőrzése
- [ ] Backup terv előkészítése

**Találkozó napján:**
- [ ] Korai érkezés (15-30 perc)
- [ ] Demo környezet végső ellenőrzése
- [ ] Anyagok előkészítése

### 5.2 Demo prezentáció struktúra

**1. Bevezetés (5 perc)**
- Üdvözlés
- Napirend áttekintése
- Agentize platform bemutatása

**2. Meeting Assistant demo (15 perc)**
- Funkciók bemutatása
- Működés bemutatása
- Eredmények megmutatása
- ROI számítás

**3. PMO Report Generator demo (15 perc)**
- Funkciók bemutatása
- Működés bemutatása
- Eredmények megmutatása
- ROI számítás

**4. Kombinált használat (5 perc)**
- Integrált workflow
- Színergia hatások

**5. Kérdések és válaszok (10-15 perc)**
- Q&A session
- Következő lépések megbeszélése

**Összesen: 50-60 perc**

---

## 6. Következő lépések

### Rövid távú (0-7 nap)
1. Demo anyagok végső ellenőrzése
2. Ügyféltalálkozó előkészítése
3. Demo prezentáció gyakorlása

### Közép távú (8-30 nap)
1. Ügyféltalálkozó lebonyolítása
2. Visszajelzések gyűjtése
3. Finomhangolások (ha szükséges)

### Hosszú távú (31-90 nap)
1. Pilot bevezetés
2. Teljes körű implementáció
3. ROI mérés

---

## 7. Demo adatok és folyamatok

### 7.1 Demo adatbázis előkészítése

#### 7.1.1 Meeting Assistant demo adatok

**Demo meeting átirat (meeting_demo_transcript.txt):**

```
Meeting: Heti projekt státusz - 2025-01-15 10:00-11:00
Résztvevők: Kovács Péter (PM), Nagy Anna (Dev Lead), Szabó István (QA Lead), Tóth Mária (Product Owner)

Kovács Péter: Üdvözlöm mindenkit! Kezdjük a heti státusz meetinggel.
Nagy Anna: A fejlesztési csapat jól halad. A user authentication modul 80%-ban kész.
Szabó István: A QA tesztelés elkezdődött, de még vannak kritikus bugok a login flow-ban.
Tóth Mária: Fontos, hogy a következő sprintben befejezzük, mert a következő hónapban kell a demo.
Kovács Péter: Rendben. Anna, kérlek, foglalkozz a kritikus bugokkal prioritásként.
Nagy Anna: Értem, ma elkezdem.
Szabó István: Én segítek a tesztelésben, ha kész lesz.
Tóth Mária: Köszönöm! Következő meeting: jövő hétfőn, ugyanekkor.
```

**Várható AI output (meeting_minutes_demo.json):**

```json
{
  "summary": "Heti projekt státusz meeting a user authentication modul fejlesztéséről. A fejlesztés 80%-ban kész, de kritikus bugok vannak a login flow-ban, amelyeket prioritásként kell kezelni.",
  "agenda_items": [
    {
      "topic": "Fejlesztési státusz",
      "discussion": "A user authentication modul 80%-ban kész",
      "decisions": "Kritikus bugok prioritásként kezelendők"
    },
    {
      "topic": "QA tesztelés",
      "discussion": "Tesztelés elkezdődött, kritikus bugok azonosítva",
      "decisions": "Szabó István segít a tesztelésben"
    }
  ],
  "key_points": [
    "User authentication modul 80% kész",
    "Kritikus bugok a login flow-ban",
    "Demo következő hónapban",
    "Következő meeting: jövő hétfőn"
  ],
  "action_items": [
    {
      "id": "AI-001",
      "description": "Kritikus bugok javítása a login flow-ban",
      "assignee": "Nagy Anna",
      "due_date": "2025-01-17",
      "priority": "high"
    },
    {
      "id": "AI-002",
      "description": "QA tesztelés támogatása",
      "assignee": "Szabó István",
      "due_date": "2025-01-18",
      "priority": "medium"
    }
  ],
  "next_steps": [
    "Kritikus bugok javítása (Nagy Anna)",
    "QA tesztelés folytatása (Szabó István)",
    "Következő meeting: 2025-01-22 10:00"
  ]
}
```

**Demo Jira ticket-ek (várt output):**

```
JIRA-123: [HIGH] Kritikus bugok javítása a login flow-ban
- Assignee: Nagy Anna
- Due: 2025-01-17
- Description: A login flow-ban azonosított kritikus bugok javítása prioritásként.

JIRA-124: [MEDIUM] QA tesztelés támogatása
- Assignee: Szabó István
- Due: 2025-01-18
- Description: QA tesztelés támogatása a user authentication modulhoz.
```

#### 7.1.2 PMO Report Generator demo adatok

**Demo Jira adatok (jira_demo_data.json):**

```json
{
  "projects": [
    {
      "key": "PROJ-1",
      "name": "User Authentication Module",
      "status": "In Progress",
      "progress": 80,
      "issues": {
        "total": 25,
        "open": 5,
        "in_progress": 8,
        "done": 12
      },
      "sprint": {
        "name": "Sprint 15",
        "start_date": "2025-01-08",
        "end_date": "2025-01-22"
      }
    },
    {
      "key": "PROJ-2",
      "name": "Payment Integration",
      "status": "At Risk",
      "progress": 45,
      "issues": {
        "total": 30,
        "open": 12,
        "in_progress": 10,
        "done": 8
      },
      "sprint": {
        "name": "Sprint 15",
        "start_date": "2025-01-08",
        "end_date": "2025-01-22"
      }
    }
  ],
  "period": {
    "start": "2025-01-08",
    "end": "2025-01-14"
  }
}
```

**Demo Excel adatok (budget_demo.xlsx struktúra):**

| Projekt | Tervezett költség | Tényleges költség | Különbség | Státusz |
|---------|-------------------|-------------------|-----------|---------|
| PROJ-1  | €50,000          | €48,000          | -€2,000   | Under   |
| PROJ-2  | €75,000          | €82,000          | +€7,000   | Over    |

**Várható AI output (pmo_report_demo.json):**

```json
{
  "executive_summary": {
    "overview": "A heti PMO riport szerint 2 projekt aktív. A User Authentication Module jól halad (80%), míg a Payment Integration késésben van és kockázat alatt áll.",
    "key_metrics": {
      "total_projects": 2,
      "on_track": 1,
      "at_risk": 1,
      "delayed": 0,
      "budget_variance": "+3.2%"
    },
    "critical_risks": [
      {
        "project": "Payment Integration",
        "risk": "45% progress, de 12 nyitott ticket. Lehetőség van késésre.",
        "impact": "high",
        "mitigation": "Erőforrás újraallokáció vagy sprint hosszabbítás megfontolása"
      }
    ],
    "recommendations": [
      "Payment Integration projekt erőforrás növelése",
      "Heti follow-up meeting a kockázatos projekttel",
      "Budget review a túlköltés miatt"
    ]
  }
}
```

### 7.2 Demo folyamatok

#### 7.2.1 Meeting Assistant demo folyamat

**Előfeltételek:**
- [ ] Demo meeting átirat betöltve
- [ ] OpenRouter API kulcs beállítva
- [ ] Jira integráció konfigurálva (opcionális)
- [ ] Email SMTP beállítva

**Folyamat lépései:**

1. **Meeting trigger szimulálása:**
   ```bash
   curl -X POST http://localhost:8000/api/v1/meetings/process \
     -H "Content-Type: application/json" \
     -d '{
       "meeting_id": "demo-meeting-001",
       "transcript": "[demo transcript content]",
       "participants": ["kovacs.peter@demo.com", "nagy.anna@demo.com"],
       "meeting_title": "Heti projekt státusz",
       "meeting_date": "2025-01-15T10:00:00Z"
     }'
   ```

2. **Feldolgozás követése:**
   ```bash
   curl http://localhost:8000/api/v1/meetings/demo-meeting-001/status
   ```

3. **Eredmények ellenőrzése:**
   - Jegyzőkönyv PDF letöltése
   - Action item-ek listája
   - Jira ticket-ek (ha integrálva)

**Várható időzítés:**
- Transcript feldolgozás: 30-60 másodperc
- AI generálás: 10-20 másodperc
- PDF generálás: 5-10 másodperc
- Jira ticket létrehozás: 5-10 másodperc
- **Összesen: ~1-2 perc**

#### 7.2.2 PMO Report Generator demo folyamat

**Előfeltételek:**
- [ ] Demo Jira adatok importálva
- [ ] Demo Excel fájl feltöltve
- [ ] OpenRouter API kulcs beállítva
- [ ] Email címzettek konfigurálva

**Folyamat lépései:**

1. **Riport generálás indítása:**
   ```bash
   curl -X POST http://localhost:8000/api/v1/reports/generate \
     -H "Content-Type: application/json" \
     -d '{
       "report_type": "weekly",
       "period_start": "2025-01-08",
       "period_end": "2025-01-14",
       "jira_projects": ["PROJ-1", "PROJ-2"],
       "excel_files": ["budget_demo.xlsx"],
       "recipients": ["executive@demo.com"]
     }'
   ```

2. **Feldolgozás követése:**
   ```bash
   curl http://localhost:8000/api/v1/reports/{report_id}/status
   ```

3. **Eredmények ellenőrzése:**
   - PDF riport letöltése
   - Excel export letöltése
   - Email kézbesítés ellenőrzése

**Várható időzítés:**
- Adatgyűjtés (Jira + Excel): 10-20 másodperc
- AI elemzés: 15-30 másodperc
- Grafikonok generálása: 5-10 másodperc
- PDF/Excel export: 5-10 másodperc
- **Összesen: ~1-2 perc**

### 7.3 Demo környezet setup

**Docker Compose konfiguráció (docker-compose.demo.yml):**

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:14
    environment:
      POSTGRES_DB: agentize_demo
      POSTGRES_USER: demo
      POSTGRES_PASSWORD: demo123
    ports:
      - "5432:5432"
    volumes:
      - ./demo_data/init.sql:/docker-entrypoint-initdb.d/init.sql

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  minio:
    image: minio/minio
    command: server /data --console-address ":9001"
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    volumes:
      - ./demo_data/storage:/data

  agentize-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://demo:demo123@postgres:5432/agentize_demo
      REDIS_URL: redis://redis:6379/0
      OPENROUTER_API_KEY: ${OPENROUTER_API_KEY}
    depends_on:
      - postgres
      - redis
      - minio
```

**Demo adatok betöltése:**

```bash
# 1. Adatbázis inicializálás
psql -h localhost -U demo -d agentize_demo -f demo_data/init.sql

# 2. Demo meeting átirat feltöltése
python scripts/load_demo_data.py --meeting-transcript demo_data/meeting_demo_transcript.txt

# 3. Demo Jira adatok importálása
python scripts/load_demo_data.py --jira-data demo_data/jira_demo_data.json

# 4. Demo Excel fájl feltöltése
python scripts/load_demo_data.py --excel-file demo_data/budget_demo.xlsx
```

### 7.4 Demo script végrehajtása

**Teljes demo folyamat (demo_script.sh):**

```bash
#!/bin/bash

echo "=== Agentize Platform Demo ==="
echo ""

echo "1. Meeting Assistant Demo"
echo "   - Meeting feldolgozás indítása..."
MEETING_ID=$(curl -s -X POST http://localhost:8000/api/v1/meetings/process \
  -H "Content-Type: application/json" \
  -d @demo_data/meeting_request.json | jq -r '.meeting_id')

echo "   - Meeting ID: $MEETING_ID"
echo "   - Várakozás feldolgozásra..."
sleep 90

echo "   - Eredmények lekérése..."
curl -s http://localhost:8000/api/v1/meetings/$MEETING_ID | jq '.'

echo ""
echo "2. PMO Report Generator Demo"
echo "   - Riport generálás indítása..."
REPORT_ID=$(curl -s -X POST http://localhost:8000/api/v1/reports/generate \
  -H "Content-Type: application/json" \
  -d @demo_data/report_request.json | jq -r '.report_id')

echo "   - Report ID: $REPORT_ID"
echo "   - Várakozás generálásra..."
sleep 120

echo "   - Eredmények lekérése..."
curl -s http://localhost:8000/api/v1/reports/$REPORT_ID | jq '.'

echo ""
echo "=== Demo befejezve ==="
```

---

*Dokumentum verzió: 1.0*  
*Utolsó frissítés: 2025-01-XX*

