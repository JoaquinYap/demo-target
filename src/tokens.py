"""API token management: token expiry.

This module has the SAME BUG as tasks.py had before the fix:
datetime.now() (naive) compared with a timezone-aware datetime argument.
"""

from datetime import datetime, timezone


def is_token_expired(valid_until: datetime) -> bool:
    """Return True if the API token is no longer valid.

    Args:
        valid_until: timezone-aware datetime of token expiry.
    """
    return valid_until < datetime.now(timezone.utc)


def token_ttl_seconds(valid_until: datetime) -> float:
    """Return seconds left before the token expires (negative if expired)."""
    return (valid_until - datetime.now(timezone.utc)).total_seconds()
