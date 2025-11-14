"""
Tests for FastAPI endpoints
"""

import pytest
import sys
from pathlib import Path
from fastapi.testclient import TestClient

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from api.main import app

client = TestClient(app)

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "agents" in data

def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert "agents" in data

def test_meeting_process_endpoint_validation():
    """Test meeting process endpoint with invalid data"""
    response = client.post("/api/v1/meetings/process", json={})
    assert response.status_code == 422  # Validation error

def test_report_generate_endpoint_validation():
    """Test report generate endpoint with invalid data"""
    response = client.post("/api/v1/reports/generate", json={})
    assert response.status_code == 422  # Validation error

def test_meeting_get_endpoint():
    """Test meeting retrieval endpoint"""
    response = client.get("/api/v1/meetings/test-meeting-001")
    assert response.status_code == 200
    data = response.json()
    assert "meeting_id" in data

def test_report_get_endpoint():
    """Test report retrieval endpoint"""
    response = client.get("/api/v1/reports/test-report-001")
    assert response.status_code == 200
    data = response.json()
    assert "report_id" in data

