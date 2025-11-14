# Screenshot Guide for NotebookLM
## Képernyőképek készítési útmutató

Ez a dokumentum részletes útmutatót ad a képernyőképek készítéséhez, amelyeket NotebookLM segítségével lehet automatizálni.

---

## Meeting Assistant Screenshots

### 01-login.png
**Cél**: Agentize platform bejelentkezési képernyő

**Lépések**:
1. Nyisd meg a böngészőt
2. Navigálj a platform URL-re: `https://platform.agentize.com`
3. Mutasd be a login formot
4. Email és jelszó mezők láthatók
5. "Sign In" gomb

**Komponensek**:
- Agentize logo
- Login form
- "Forgot password?" link
- "Sign up" link (opcionális)

---

### 02-settings.png
**Cél**: Alapvető konfiguráció beállítások

**Lépések**:
1. Bejelentkezés után
2. Kattints a "Settings" gombra
3. Mutasd be a Settings oldalt
4. Alapvető információk form:
   - Szervezet neve mező
   - Időzóna dropdown
   - Alapértelmezett nyelv választó

**Komponensek**:
- Settings menü bal oldalon
- Alapvető információk szekció
- Save gomb

---

### 03-teams-integration.png
**Cél**: Microsoft Teams integráció beállítása

**Lépések**:
1. Settings menüben válaszd az "Integrations" fület
2. Kattints a "Microsoft Teams" opcióra
3. Mutasd be a Teams integráció oldalt
4. "Connect" gomb látható
5. Engedélyezési folyamat (ha lehetséges)

**Komponensek**:
- Integrations lista
- Microsoft Teams kártya
- Connect/Disconnect gomb
- Status indicator (Connected/Not Connected)

---

### 04-jira-integration.png
**Cél**: Jira integráció beállítása

**Lépések**:
1. Integrations menüben válaszd a "Jira" opciót
2. Mutasd be a Jira beállítási formot
3. Jira URL mező
4. API token mező vagy OAuth gomb
5. Projekt választó
6. "Test Connection" gomb

**Komponensek**:
- Jira konfigurációs form
- URL input mező
- Authentication opciók
- Projekt selector
- Test Connection gomb

---

### 05-template-customization.png
**Cél**: Jegyzőkönyv sablon testreszabása

**Lépések**:
1. Settings → Templates menü
2. "Meeting Minutes Template" kiválasztása
3. Mutasd be a sablon szerkesztőt
4. Sablon struktúra látható:
   - Meeting információk szekció
   - Agenda pontok
   - Action item-ek formátuma
5. Preview gomb

**Komponensek**:
- Template editor
- Formátum opciók
- Preview panel
- Save gomb

---

### 06-email-notifications.png
**Cél**: Email értesítések konfigurációja

**Lépések**:
1. Settings → Notifications menü
2. Mutasd be az értesítési beállításokat
3. Címzettek listája
4. Értesítési típusok checkbox-ok:
   - Jegyzőkönyv kész
   - Action item létrehozva
   - Action item státusz változás

**Komponensek**:
- Notification settings form
- Recipient list
- Event checkboxes
- Save gomb

---

### 07-test-results.png
**Cél**: Tesztelés eredményei

**Lépések**:
1. Generált jegyzőkönyv megjelenítése
2. Action item-ek listája
3. Jira ticket-ek (ha integrálva)
4. Success üzenetek

**Komponensek**:
- Generated minutes preview
- Action items list
- Jira tickets list
- Success indicators

---

## PMO Report Generator Screenshots

### 01-login.png
**Ugyanaz mint Meeting Assistant-nál**

---

### 02-jira-integration.png
**Ugyanaz mint Meeting Assistant-nál, de PMO Report Generator kontextusban**

---

### 03-excel-upload.png
**Cél**: Excel fájlok feltöltése

**Lépések**:
1. Integrations → Excel Files
2. "Upload Files" gomb
3. File picker vagy drag-and-drop terület
4. Feltöltött fájlok listája
5. Feldolgozási opciók:
   - Automatikus feldolgozás
   - Manuális mezőleképezés

**Komponensek**:
- Upload terület
- File list
- Processing options
- Save gomb

---

### 04-template-customization.png
**Cél**: Riport sablon testreszabása

**Lépések**:
1. Settings → Report Templates
2. "Executive Summary Template" kiválasztása
3. Sablon szerkesztő:
   - Riport címe
   - KPI-k választó
   - Grafikonok konfigurációja
   - Színséma

**Komponensek**:
- Template editor
- KPI selector
- Chart configuration
- Color scheme picker
- Preview gomb

---

### 05-schedule.png
**Cél**: Ütemezés beállítása

**Lépések**:
1. Settings → Schedule menü
2. Riport generálás gyakorisága:
   - Heti (nap és időpont)
   - Havi
   - Negyedéves
   - Manuális
3. Címzettek listája

**Komponensek**:
- Schedule form
- Frequency selector
- Date/time picker
- Recipient list
- Save gomb

---

### 06-test-results.png
**Cél**: Generált riport eredményei

**Lépések**:
1. Generált riport megjelenítése
2. Executive summary
3. Grafikonok
4. Kockázatok és ajánlások
5. Export opciók (PDF, Excel)

**Komponensek**:
- Report preview
- Executive summary section
- Charts and graphs
- Risks and recommendations
- Export buttons

---

## Általános screenshot készítési útmutató

### Technikai követelmények

- **Felbontás**: Minimum 1920x1080
- **Formátum**: PNG (veszteségmentes)
- **Színmélység**: 24-bit RGB
- **Névkonvenció**: `##-description.png` (pl. `01-login.png`)

### Best practices

1. **Előkészítés**:
   - Demo környezet futtatása
   - Böngésző ablak teljes képernyős módban
   - Tiszta, rendezett desktop

2. **Készítés**:
   - Windows: Win + Shift + S (Snipping Tool)
   - Mac: Cmd + Shift + 4
   - Vagy: OBS Studio screenshot funkció

3. **Utómunka**:
   - Személyes adatok eltávolítása
   - Szövegek olvashatóságának ellenőrzése
   - Fájlok elnevezése a konvenció szerint

### Automatizálás NotebookLM-mel

NotebookLM képes:
- Script alapján screenshot-ok készítésére
- Képernyőfelvétel automatizálására
- Batch feldolgozásra

**Használat**:
1. Töltsd be ezt a dokumentumot NotebookLM-be
2. Add meg a demo környezet URL-jét
3. Futtasd a screenshot scripteket
4. A rendszer automatikusan készíti a képernyőképeket

---

*Ez a dokumentum NotebookLM-hez optimalizálva, könnyen automatizálható formátumban.*

