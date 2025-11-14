#!/bin/bash

# Agentize Platform Demo Script
# Használat: bash scripts/demo_script.sh

set -e

API_BASE_URL="${API_BASE_URL:-http://localhost:8000}"
DEMO_DATA_DIR="${DEMO_DATA_DIR:-demo_data}"

echo "=== Agentize Platform Demo ==="
echo ""

# Ellenőrzés: API elérhető-e
if ! curl -s "${API_BASE_URL}/health" > /dev/null 2>&1; then
    echo "⚠️  Figyelem: Az API nem elérhető a ${API_BASE_URL} címen"
    echo "   Kérlek, indítsd el a demo környezetet:"
    echo "   docker-compose -f docker-compose.demo.yml up -d"
    echo ""
    read -p "Folytassam a demo scriptet? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "1. Meeting Assistant Demo"
echo "   - Meeting feldolgozás indítása..."

if [ ! -f "${DEMO_DATA_DIR}/meeting_request.json" ]; then
    echo "❌ Hiba: ${DEMO_DATA_DIR}/meeting_request.json nem található"
    exit 1
fi

MEETING_RESPONSE=$(curl -s -X POST "${API_BASE_URL}/api/v1/meetings/process" \
  -H "Content-Type: application/json" \
  -d @"${DEMO_DATA_DIR}/meeting_request.json")

MEETING_ID=$(echo "$MEETING_RESPONSE" | jq -r '.meeting_id // empty')

if [ -z "$MEETING_ID" ] || [ "$MEETING_ID" = "null" ]; then
    echo "⚠️  Figyelem: Meeting ID nem érkezett meg"
    echo "   Válasz: $MEETING_RESPONSE"
    echo ""
    echo "   Ez normális, ha az API még nincs implementálva."
    echo "   A script csak a struktúrát mutatja be."
else
    echo "   - Meeting ID: $MEETING_ID"
    echo "   - Várakozás feldolgozásra..."
    sleep 90
    
    echo "   - Eredmények lekérése..."
    curl -s "${API_BASE_URL}/api/v1/meetings/${MEETING_ID}" | jq '.' || echo "   (API válasz nem érkezett meg)"
fi

echo ""
echo "2. PMO Report Generator Demo"
echo "   - Riport generálás indítása..."

if [ ! -f "${DEMO_DATA_DIR}/report_request.json" ]; then
    echo "❌ Hiba: ${DEMO_DATA_DIR}/report_request.json nem található"
    exit 1
fi

REPORT_RESPONSE=$(curl -s -X POST "${API_BASE_URL}/api/v1/reports/generate" \
  -H "Content-Type: application/json" \
  -d @"${DEMO_DATA_DIR}/report_request.json")

REPORT_ID=$(echo "$REPORT_RESPONSE" | jq -r '.report_id // empty')

if [ -z "$REPORT_ID" ] || [ "$REPORT_ID" = "null" ]; then
    echo "⚠️  Figyelem: Report ID nem érkezett meg"
    echo "   Válasz: $REPORT_RESPONSE"
    echo ""
    echo "   Ez normális, ha az API még nincs implementálva."
    echo "   A script csak a struktúrát mutatja be."
else
    echo "   - Report ID: $REPORT_ID"
    echo "   - Várakozás generálásra..."
    sleep 120
    
    echo "   - Eredmények lekérése..."
    curl -s "${API_BASE_URL}/api/v1/reports/${REPORT_ID}" | jq '.' || echo "   (API válasz nem érkezett meg)"
fi

echo ""
echo "=== Demo befejezve ==="
echo ""
echo "📝 Megjegyzés: Ez a script csak a struktúrát mutatja be."
echo "   A teljes működéshez az API implementálása szükséges."

