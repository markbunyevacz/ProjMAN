#!/bin/bash

# Complete Demo Script - Meeting Assistant & PMO Report Generator

set -e

API_BASE_URL="${API_BASE_URL:-http://localhost:8000}"

echo "========================================="
echo "   ProjMAN AI Agents - Complete Demo"
echo "========================================="
echo ""

# Check API is running
echo "🔍 Checking API status..."
if ! curl -s "${API_BASE_URL}/health" > /dev/null 2>&1; then
    echo "❌ API is not running at ${API_BASE_URL}"
    echo ""
    echo "Start the API with:"
    echo "  bash scripts/run_api.sh"
    echo "  OR"
    echo "  docker-compose -f docker-compose.demo.yml up"
    exit 1
fi

HEALTH=$(curl -s "${API_BASE_URL}/health")
echo "✅ API is healthy"
echo "$HEALTH" | python -m json.tool
echo ""

# Demo 1: Meeting Assistant
echo "========================================="
echo "   Demo 1: Meeting Assistant"
echo "========================================="
echo ""

echo "📝 Processing demo meeting..."
if [ ! -f "demo_data/meeting_request.json" ]; then
    echo "❌ demo_data/meeting_request.json not found"
    exit 1
fi

MEETING_RESPONSE=$(curl -s -X POST "${API_BASE_URL}/api/v1/meetings/process" \
  -H "Content-Type: application/json" \
  -d @demo_data/meeting_request.json)

echo "✅ Meeting processed!"
echo ""
echo "📊 Results:"
echo "$MEETING_RESPONSE" | python -m json.tool | head -50
echo ""

# Demo 2: PMO Report Generator
echo "========================================="
echo "   Demo 2: PMO Report Generator"
echo "========================================="
echo ""

echo "📈 Generating PMO report..."
if [ ! -f "demo_data/report_request.json" ]; then
    echo "❌ demo_data/report_request.json not found"
    exit 1
fi

REPORT_RESPONSE=$(curl -s -X POST "${API_BASE_URL}/api/v1/reports/generate" \
  -H "Content-Type: application/json" \
  -d @demo_data/report_request.json)

echo "✅ Report generated!"
echo ""
echo "📊 Results:"
echo "$REPORT_RESPONSE" | python -m json.tool | head -50
echo ""

echo "========================================="
echo "   Demo Complete! ✅"
echo "========================================="
echo ""
echo "Next steps:"
echo "  - Open http://localhost:8000/docs for API documentation"
echo "  - Open frontend/index.html in browser for Web UI"
echo "  - Check demo_data/ for more examples"

