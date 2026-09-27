"""Twin c02: get_rate_limit returns wrong value when rate_limit is explicitly 0."""
from src.feature_flags import get_rate_limit


def test_zero_rate_limit_not_overridden_by_default():
    """When rate_limit is explicitly 0 (block all), it must NOT be replaced by the default 100."""
    flags = {"rate_limit": 0}
    result = get_rate_limit(flags, default=100)
    assert result == 0, f"Expected 0 but got {result!r}"
