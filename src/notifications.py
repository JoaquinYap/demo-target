"""Notification dispatch: build and send notifications."""
from typing import Optional


def add_notification(message: str, recipients: Optional[list] = None) -> list:
    """Add a message to the recipients list and return it.

    Args:
        message: The notification text.
        recipients: List of pending notifications. Defaults to a new list each call.
    """
    # FIX: use None as default and create a new list each call
    if recipients is None:
        recipients = []
    recipients.append(message)
    return recipients


def build_digest(subject: str, items: Optional[list] = None) -> dict:
    """Build a digest dict with subject and accumulated items."""
    # FIX: same pattern — None default, create new list inside
    if items is None:
        items = []
    items.append(subject)
    return {"subject": subject, "items": items}


def collect_errors(error: str, log: Optional[list] = None) -> list:
    """Append an error to the error log."""
    # FIX: each call gets its own fresh list unless one is passed in
    if log is None:
        log = []
    log.append(error)
    return log
