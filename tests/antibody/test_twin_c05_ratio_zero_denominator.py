import pytest
from src.statistics_helpers import ratio


def test_ratio_zero_denominator():
    """ratio() must not raise ZeroDivisionError when denominator=0."""
    result = ratio(5.0, 0.0)
    assert result == 0.0
