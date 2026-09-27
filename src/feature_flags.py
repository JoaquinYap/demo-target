"""Feature flag management."""
from typing import Any


def is_feature_enabled(flags: dict, name: str, default: bool = True) -> bool:
    """Return whether a feature flag is enabled."""
    value = flags.get(name)
    return value if value is not None else default


def get_rate_limit(flags: dict, default: int = 100) -> int:
    """Return the rate limit from flags."""
    value = flags.get("rate_limit")
    return value if value is not None else default
