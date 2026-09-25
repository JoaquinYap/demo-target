"""Subscription management: plan expiry.

This module has the SAME BUG as tasks.py had before the fix:
datetime.now() (naive) compared with a timezone-aware datetime argument.
"""

from datetime import datetime


def is_subscription_active(renews_at: datetime) -> bool:
    """Return True if the subscription has not yet expired.

    Args:
        renews_at: timezone-aware datetime of the next renewal.
    """
    # BUG: datetime.now() is naive; raises TypeError with aware renews_at
    return datetime.now() < renews_at


def days_until_renewal(renews_at: datetime) -> float:
    """Return days remaining until the next renewal (negative if lapsed)."""
    # BUG: same naive datetime mistake
    return (renews_at - datetime.now()).days
