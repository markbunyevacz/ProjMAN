#!/bin/bash

# ProjMAN API Server Startup Script

set -e

echo "🚀 Starting ProjMAN API Server..."
echo ""

# Check for OpenRouter API key
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "⚠️  Warning: OPENROUTER_API_KEY not set"
    echo "   Set it with: export OPENROUTER_API_KEY='your-api-key'"
    echo ""
fi

# Check Python dependencies
echo "📦 Checking dependencies..."
if ! python -c "import fastapi" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo "✅ Dependencies OK"
echo ""

# Initialize database (optional)
if [ "$INIT_DB" = "true" ]; then
    echo "🗄️  Initializing database..."
    python -c "from core.database import init_db; init_db()"
    echo "✅ Database initialized"
    echo ""
fi

# Start API server
echo "🌐 Starting API server on http://localhost:8000"
echo "📚 API docs available at http://localhost:8000/docs"
echo "🏥 Health check at http://localhost:8000/health"
echo ""
echo "Press Ctrl+C to stop"
echo ""

uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

