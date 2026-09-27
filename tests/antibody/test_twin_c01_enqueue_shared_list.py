"""Twin c01: enqueue() mutable default list shared across calls."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from queue_manager import enqueue


def test_enqueue_does_not_share_state_across_calls():
    """Two independent calls without explicit queue must not see each other's jobs."""
    result1 = enqueue("job-A")
    result2 = enqueue("job-B")
    # If the default is shared, result2 will contain both "job-A" and "job-B"
    assert result2 == ["job-B"], (
        f"Expected ['job-B'] but got {result2!r} — mutable default list is shared"
    )
