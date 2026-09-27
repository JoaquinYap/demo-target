import pytest
from src.metrics import p99_normalized


def test_p99_normalized_zero_baseline():
    """p99_normalized() must not raise ZeroDivisionError when baseline=0."""
    result = p99_normalized(50.0, 0.0)
    assert result == 0.0
