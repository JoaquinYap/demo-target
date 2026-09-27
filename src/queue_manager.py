"""Job queue management."""
from typing import Optional


def enqueue(job: str, queue: Optional[list] = None) -> list:
    """Add a job to the processing queue."""
    if queue is None:
        queue = []
    queue.append(job)
    return queue


def batch_jobs(job: str, batch: Optional[list] = None) -> list:
    """Accumulate jobs into a batch."""
    if batch is None:
        batch = []
    batch.append(job)
    return batch
