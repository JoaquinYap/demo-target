"""Twin c05: get_prefix returns wrong value when PREFIX is explicitly empty string."""
from src.env_helpers import get_prefix


def test_empty_prefix_not_overridden_by_default():
    """When PREFIX='' (serve at root), it must NOT be replaced by the default '/api'."""
    env = {"PREFIX": ""}
    result = get_prefix(env, default="/api")
    assert result == "", f"Expected '' but got {result!r}"
