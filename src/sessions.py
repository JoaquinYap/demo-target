"""Session management: login expiry.

This module has the SAME BUG as tasks.py had before the fix:
datetime.now() (naive) compared with a timezone-aware datetime argument.
"""

from datetime import datetime, timezone


def is_session_expired(expires_at: datetime) -> bool:
    """Return True when the user session has expired.

    Args:
        expires_at: timezone-aware datetime when the session expires.
    """
    return expires_at < datetime.now(timezone.utc)


def session_age_seconds(created_at: datetime) -> float:
    """Return how many seconds ago this session was created."""
    return (datetime.now(timezone.utc) - created_at).total_seconds()
