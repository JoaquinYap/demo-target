"""Regression test added in the fix commit for tasks.is_task_expired."""

import sys
sys.path.insert(0, "src")

from datetime import datetime, timezone, timedelta
from tasks import is_task_expired, seconds_until_deadline, is_overdue


def test_expired_task_with_aware_datetime():
    """A past aware deadline must be detected as expired."""
    past = datetime.now(timezone.utc) - timedelta(hours=1)
    assert is_task_expired(past), "Task from 1 hour ago must be expired"


def test_future_task_is_not_expired():
    """A future aware deadline must NOT be detected as expired."""
    future = datetime.now(timezone.utc) + timedelta(hours=1)
    assert not is_task_expired(future), "Task due in 1 hour must not be expired"


def test_seconds_until_deadline_positive_for_future():
    """A future deadline should give positive seconds remaining."""
    future = datetime.now(timezone.utc) + timedelta(seconds=60)
    secs = seconds_until_deadline(future)
    assert secs > 0, f"Expected positive seconds, got {secs}"


def test_overdue_detects_past_deadline():
    """A deadline 10 seconds ago with 0 grace should be overdue."""
    past = datetime.now(timezone.utc) - timedelta(seconds=10)
    assert is_overdue(past, grace_seconds=0)
