"""Twin c02: batch_jobs() mutable default list shared across calls."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from queue_manager import batch_jobs


def test_batch_jobs_does_not_share_state_across_calls():
    """Two independent calls without explicit batch must not see each other's jobs."""
    result1 = batch_jobs("job-X")
    result2 = batch_jobs("job-Y")
    assert result2 == ["job-Y"], (
        f"Expected ['job-Y'] but got {result2!r} — mutable default list is shared"
    )
