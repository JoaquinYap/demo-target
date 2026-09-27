import pytest
from src.statistics_helpers import weighted_average


def test_weighted_average_zero_weights():
    """weighted_average() must not raise ZeroDivisionError when all weights=0."""
    result = weighted_average([1.0, 2.0, 3.0], [0.0, 0.0, 0.0])
    assert result == 0.0
