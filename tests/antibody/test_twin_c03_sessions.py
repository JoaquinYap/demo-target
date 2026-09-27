"""Twin c03: naive datetime.now() compared with aware expires_at/created_at in sessions.py.

The correct behavior is that both functions return a value without raising.
Today they raise TypeError because datetime.now() is naive.
"""
from datetime import datetime, timezone, timedelta
from src.sessions import is_session_expired, session_age_seconds


def test_is_session_expired_does_not_raise():
    aware = datetime.now(timezone.utc) + timedelta(minutes=30)
    # Session not yet expired — should return False without raising
    result = is_session_expired(aware)
    assert result is False


def test_session_age_seconds_does_not_raise():
    aware = datetime.now(timezone.utc) - timedelta(minutes=5)
    # Should return a positive age without raising TypeError
    result = session_age_seconds(aware)
    assert result > 0
