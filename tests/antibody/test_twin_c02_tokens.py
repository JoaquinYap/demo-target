"""Twin c02: naive datetime.now() compared with aware valid_until in tokens.py.

The correct behavior is that both functions return a value without raising.
Today they raise TypeError because datetime.now() is naive.
"""
from datetime import datetime, timezone, timedelta
from src.tokens import is_token_expired, token_ttl_seconds


def test_is_token_expired_does_not_raise():
    aware = datetime.now(timezone.utc) + timedelta(hours=1)
    # Token not yet expired — should return False without raising
    result = is_token_expired(aware)
    assert result is False


def test_token_ttl_seconds_does_not_raise():
    aware = datetime.now(timezone.utc) + timedelta(hours=1)
    # Should return a positive TTL without raising TypeError
    result = token_ttl_seconds(aware)
    assert result > 0
