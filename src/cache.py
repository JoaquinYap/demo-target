"""In-memory cache helpers."""
from typing import Optional


def cache_result(key: str, store: Optional[dict] = None) -> dict:
    """Store a key in the cache dict and return it."""
    if store is None:
        store = {}
    store[key] = True
    return store


def push_to_cache(value: str, cache: Optional[list] = None) -> list:
    """Append a value to the cache list."""
    if cache is None:
        cache = []
    cache.append(value)
    return cache


def register_key(key: str, seen: Optional[list] = None) -> bool:
    """Return True if key was already seen, then register it."""
    if seen is None:
        seen = []
    already = key in seen
    seen.append(key)
    return already
