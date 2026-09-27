"""Twin c04: get_workers returns wrong value when WORKERS is explicitly 0."""
from src.env_helpers import get_workers


def test_zero_workers_not_overridden_by_default():
    """When WORKERS=0 (disabled), it must NOT be replaced by the default 4."""
    env = {"WORKERS": 0}
    result = get_workers(env, default=4)
    assert result == 0, f"Expected 0 but got {result!r}"
