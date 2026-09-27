"""Twin c04: push_to_cache() mutable default list shared across calls."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from cache import push_to_cache


def test_push_to_cache_does_not_share_state_across_calls():
    """Two independent calls without explicit cache must not see each other's values."""
    result1 = push_to_cache("val-1")
    result2 = push_to_cache("val-2")
    assert result2 == ["val-2"], (
        f"Expected ['val-2'] but got {result2!r} — mutable default list is shared"
    )
