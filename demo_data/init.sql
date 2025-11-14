-- Demo adatbázis inicializáló script
-- PostgreSQL 14+ kompatibilis

-- Meetings tábla
CREATE TABLE IF NOT EXISTS meetings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id VARCHAR(255) UNIQUE,
    title VARCHAR(500),
    date TIMESTAMP,
    duration_minutes INTEGER,
    participants JSONB,
    audio_url TEXT,
    transcript TEXT,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Meeting minutes tábla
CREATE TABLE IF NOT EXISTS meeting_minutes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    meeting_id UUID REFERENCES meetings(id),
    summary TEXT,
    agenda_items JSONB,
    key_points JSONB,
    action_items JSONB,
    next_steps JSONB,
    minutes_pdf_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Action items tábla
CREATE TABLE IF NOT EXISTS action_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    meeting_id UUID REFERENCES meetings(id),
    description TEXT,
    assignee_email VARCHAR(255),
    due_date DATE,
    priority VARCHAR(20),
    jira_ticket_id VARCHAR(100),
    status VARCHAR(50) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Reports tábla
CREATE TABLE IF NOT EXISTS reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_type VARCHAR(50),
    period_start DATE,
    period_end DATE,
    status VARCHAR(50) DEFAULT 'generating',
    pdf_url TEXT,
    excel_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Report data tábla
CREATE TABLE IF NOT EXISTS report_data (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id UUID REFERENCES reports(id),
    source VARCHAR(50),
    data_type VARCHAR(50),
    raw_data JSONB,
    processed_data JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Report analysis tábla
CREATE TABLE IF NOT EXISTS report_analysis (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id UUID REFERENCES reports(id),
    executive_summary JSONB,
    trends JSONB,
    risks JSONB,
    recommendations JSONB,
    ai_model_version VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexek létrehozása
CREATE INDEX IF NOT EXISTS idx_meetings_external_id ON meetings(external_id);
CREATE INDEX IF NOT EXISTS idx_meetings_status ON meetings(status);
CREATE INDEX IF NOT EXISTS idx_action_items_meeting_id ON action_items(meeting_id);
CREATE INDEX IF NOT EXISTS idx_action_items_status ON action_items(status);
CREATE INDEX IF NOT EXISTS idx_reports_period ON reports(period_start, period_end);
CREATE INDEX IF NOT EXISTS idx_reports_status ON reports(status);

