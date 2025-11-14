# NotebookLM Quick Start Guide
## Gyors kezdés 5 percben

Ez a rövid útmutató segít gyorsan elkezdeni a NotebookLM használatát a projekt fejlesztéséhez.

---

## 1. Videók készítése (5 perc)

### Lépések:

1. **Nyisd meg NotebookLM-et**
   - Menj a https://notebooklm.google.com oldalra
   - Jelentkezz be Google fiókkal

2. **Hozz létre új notebook-ot**
   - Kattints az "New Notebook" gombra
   - Nevezd el: "Agentize Video Scripts"

3. **Töltsd be a VIDEO_SCRIPTS.md fájlt**
   - Kattints az "Add source" gombra
   - Válaszd a "Upload" opciót
   - Töltsd fel a `notebooklm/VIDEO_SCRIPTS.md` fájlt

4. **Kérj segítséget NotebookLM-től:**
   ```
   "Készítsd el a Meeting Assistant gyors bemutatás videóját 
   a script alapján. Használd a demo környezetet: 
   http://localhost:8000"
   ```

5. **Kövesd a NotebookLM útmutatását**
   - NotebookLM lépésről lépésre vezet
   - Készítsd el a videót a script szerint

---

## 2. Screenshots készítése (3 perc)

### Lépések:

1. **Hozz létre új notebook-ot**
   - Nevezd el: "Agentize Screenshots"

2. **Töltsd be a SCREENSHOT_GUIDE.md fájlt**

3. **Kérj segítséget:**
   ```
   "Készítsd el az összes Meeting Assistant screenshot-ot 
   a guide alapján. Demo környezet: http://localhost:8000"
   ```

4. **NotebookLM automatikusan készíti a screenshot-okat**

---

## 3. Kód generálás (10 perc)

### Lépések:

1. **Hozz létre új notebook-ot**
   - Nevezd el: "Agentize Code Generation"

2. **Töltsd be az INTEGRATION_GUIDE.md fájlt**

3. **Add meg a projekt könyvtárat:**
   ```
   Projekt könyvtár: C:\Users\Admin\.cursor\ProjMAN
   ```

4. **Kérj segítséget:**
   ```
   "Hozd létre a Meeting Assistant agent.py fájlt 
   az INTEGRATION_GUIDE.md specifikáció alapján"
   ```

5. **Ismételd meg az összes fájlhoz:**
   - `core/ai_client.py`
   - `agents/meeting_assistant/prompts.py`
   - `agents/pmo_report_generator/agent.py`
   - `api/routes.py`
   - stb.

---

## 4. Tesztelés (5 perc)

### Lépések:

1. **Futtasd a Docker környezetet:**
   ```bash
   docker-compose -f docker-compose.demo.yml up -d
   ```

2. **Telepítsd a függőségeket:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Futtasd a teszteket:**
   ```bash
   pytest tests/
   ```

---

## Hasznos NotebookLM Prompt-ok

### Videókhoz:
- "Készítsd el a [videó neve] videót a script alapján"
- "Generáld le a videó scriptet [témához]"
- "Készíts storyboard-ot a videóhoz"

### Screenshots-hoz:
- "Készítsd el az összes screenshot-ot [agent neve]-hez"
- "Generáld le a screenshot listát"
- "Ellenőrizd, hogy minden screenshot kész van-e"

### Kód generáláshoz:
- "Hozd létre a [fájl neve] fájlt a specifikáció alapján"
- "Generáld le a [osztály/függvény] kódját"
- "Készíts unit tesztet a [modul]-hoz"

---

## Troubleshooting

### Problem: NotebookLM nem találja a fájlokat
**Megoldás**: Add meg a teljes elérési utat vagy töltsd fel a fájlokat közvetlenül

### Problem: Generált kód nem működik
**Megoldás**: 
1. Ellenőrizd a környezeti változókat (.env fájl)
2. Futtasd a teszteket
3. Kérj segítséget NotebookLM-től a hibák javításához

### Problem: Videó/screenshot minőség rossz
**Megoldás**: 
1. Ellenőrizd a demo környezet beállításait
2. Használj nagyobb felbontást
3. Kérj segítséget NotebookLM-től az optimalizáláshoz

---

## Következő lépések

1. ✅ NotebookLM dokumentumok létrehozva
2. ⏳ Videók készítése
3. ⏳ Screenshots készítése  
4. ⏳ Kód generálás
5. ⏳ Integráció és tesztelés

---

*Utolsó frissítés: 2025-01-15*

