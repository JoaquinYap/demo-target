"""Config loader."""
from typing import Any


def get_timeout(config: dict, default: int = 30) -> int:
    """Return the timeout from config, falling back to default."""
    # FIX: use explicit None check so that 0 is treated as a valid value
    value = config.get("timeout")
    return value if value is not None else default


def get_max_retries(config: dict, default: int = 3) -> int:
    """Return the max retries setting."""
    # FIX: same — explicit None check
    value = config.get("max_retries")
    return value if value is not None else default


def get_debug_flag(config: dict, default: bool = False) -> bool:
    """Return the debug flag from config."""
    # FIX: explicit None check so False is treated as a valid value
    value = config.get("debug")
    return value if value is not None else default
