"""
In-memory logging handler for recent logs retrieval
"""

import logging
from datetime import datetime
from typing import List, Dict, Optional
from collections import deque

class InMemoryLogHandler(logging.Handler):
    """In-memory log handler that stores recent log entries"""
    
    def __init__(self, max_entries: int = 100):
        super().__init__()
        self.logs: deque = deque(maxlen=max_entries)
        self.max_entries = max_entries
    
    def emit(self, record: logging.LogRecord):
        """Store log record in memory"""
        try:
            log_entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "level": record.levelname,
                "message": record.getMessage(),
                "module": record.module,
                "funcName": record.funcName,
                "lineno": record.lineno
            }
            self.logs.append(log_entry)
        except Exception:
            # Ignore errors in logging handler
            pass
    
    def get_recent_logs(
        self, 
        limit: int = 5, 
        level: Optional[str] = None
    ) -> List[Dict]:
        """Get recent log entries, optionally filtered by level"""
        logs = list(self.logs)
        if level:
            logs = [log for log in logs if log["level"] == level.upper()]
        return logs[-limit:] if limit else logs

# Global instance
_log_handler = InMemoryLogHandler(max_entries=100)

def get_log_handler() -> InMemoryLogHandler:
    """Get the global log handler instance"""
    return _log_handler

