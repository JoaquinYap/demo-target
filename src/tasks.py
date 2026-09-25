"""Task management: deadlines, expiry checks.

This module handles task expiry logic.
"""

from datetime import datetime, timezone


def is_task_expired(deadline: datetime) -> bool:
    """Return True when the task deadline has passed.

    Args:
        deadline: timezone-aware datetime of the task deadline.
    """
    return deadline < datetime.now(timezone.utc)


def seconds_until_deadline(deadline: datetime) -> float:
    """Return seconds remaining until the deadline (negative if past)."""
    return (deadline - datetime.now(timezone.utc)).total_seconds()


def is_overdue(deadline: datetime, grace_seconds: int = 0) -> bool:
    """Return True if the deadline passed more than grace_seconds ago."""
    elapsed = (datetime.now(timezone.utc) - deadline).total_seconds()
    return elapsed > grace_seconds
