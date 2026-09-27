import pytest
from src.metrics import hit_ratio


def test_hit_ratio_empty_cache():
    """hit_ratio() must not raise ZeroDivisionError when hits+misses=0."""
    result = hit_ratio(0, 0)
    assert result == 0.0
