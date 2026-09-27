import pytest
from src.metrics import throughput


def test_throughput_zero_time():
    """throughput() must not raise ZeroDivisionError when time_seconds=0."""
    result = throughput(100, 0)
    assert result == 0.0
