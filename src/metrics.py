"""Metrics reporting."""


def throughput(items_processed: int, time_seconds: float) -> float:
    """Return items processed per second."""
    if time_seconds == 0:
        return 0.0
    return items_processed / time_seconds


def hit_ratio(hits: int, misses: int) -> float:
    """Return cache hit ratio."""
    if hits + misses == 0:
        return 0.0
    return hits / (hits + misses)


def p99_normalized(p99: float, baseline: float) -> float:
    """Return p99 latency normalized against the baseline."""
    if baseline == 0:
        return 0.0
    return p99 / baseline
