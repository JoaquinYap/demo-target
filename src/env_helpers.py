"""Environment variable helpers."""
from typing import Any


def get_port(env: dict, default: int = 8080) -> int:
    """Return the PORT from env, falling back to default."""
    value = env.get("PORT")
    return value if value is not None else default


def get_workers(env: dict, default: int = 4) -> int:
    """Return the number of workers from env."""
    value = env.get("WORKERS")
    return value if value is not None else default


def get_prefix(env: dict, default: str = "/api") -> str:
    """Return the URL prefix from env."""
    value = env.get("PREFIX")
    return value if value is not None else default
