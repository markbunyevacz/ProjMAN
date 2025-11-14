# Scripts

Ez a mappa tartalmazza a demo környezet működtetéséhez szükséges scripteket.

## Fájlok

- `load_demo_data.py` - Demo adatok betöltése
- `demo_script.sh` - Teljes demo folyamat automatizálása

## Használat

### Demo adatok betöltése

```bash
# Összes demo adat
python scripts/load_demo_data.py --all

# Csak meeting transcript
python scripts/load_demo_data.py --meeting-transcript demo_data/meeting_demo_transcript.txt

# Csak Jira adatok
python scripts/load_demo_data.py --jira-data demo_data/jira_demo_data.json
```

### Demo script futtatása

```bash
# Futtathatóvá tétel
chmod +x scripts/demo_script.sh

# Futtatás
bash scripts/demo_script.sh

# Vagy közvetlenül
./scripts/demo_script.sh
```

## Előfeltételek

- Python 3.8+
- curl
- jq (JSON parser)
- Docker és Docker Compose (demo környezethez)

