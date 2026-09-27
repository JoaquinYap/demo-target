"""Twin c01: naive datetime.now() compared with aware renews_at in subscriptions.py.

The correct behavior is that both functions return a value without raising.
Today they raise TypeError because datetime.now() is naive.
"""
from datetime import datetime, timezone, timedelta
from src.subscriptions import is_subscription_active, days_until_renewal


def test_is_subscription_active_does_not_raise():
    aware = datetime.now(timezone.utc) + timedelta(days=30)
    # Should return True without raising TypeError
    result = is_subscription_active(aware)
    assert result is True


def test_days_until_renewal_does_not_raise():
    aware = datetime.now(timezone.utc) + timedelta(days=30)
    # Should return a positive number without raising TypeError
    result = days_until_renewal(aware)
    assert result > 0
