"""Twin c03: get_port returns wrong value when PORT is explicitly 0."""
from src.env_helpers import get_port


def test_zero_port_not_overridden_by_default():
    """When PORT=0 (random port), it must NOT be replaced by the default 8080."""
    env = {"PORT": 0}
    result = get_port(env, default=8080)
    assert result == 0, f"Expected 0 but got {result!r}"
