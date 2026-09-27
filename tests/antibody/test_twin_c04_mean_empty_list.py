import pytest
from src.statistics_helpers import mean


def test_mean_empty_list():
    """mean() must not raise ZeroDivisionError on an empty list."""
    result = mean([])
    assert result == 0.0
