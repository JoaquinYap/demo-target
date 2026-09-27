"""Twin c03: cache_result() mutable default dict shared across calls."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from cache import cache_result


def test_cache_result_does_not_share_state_across_calls():
    """Two independent calls without explicit store must not see each other's keys."""
    result1 = cache_result("key-A")
    result2 = cache_result("key-B")
    assert result2 == {"key-B": True}, (
        f"Expected {{'key-B': True}} but got {result2!r} — mutable default dict is shared"
    )
