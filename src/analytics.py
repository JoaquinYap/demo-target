"""Analytics calculations."""


def conversion_rate(converted: int, total: int) -> float:
    """Return the conversion rate as a ratio between 0 and 1."""
    # FIX: guard against zero denominator
    if total == 0:
        return 0.0
    return converted / total


def average_score(total_score: float, num_users: int) -> float:
    """Return the average score per user."""
    # FIX: guard against zero users
    if num_users == 0:
        return 0.0
    return total_score / num_users


def error_rate(errors: int, requests: int) -> float:
    """Return the fraction of requests that resulted in errors."""
    # FIX: guard against zero requests
    if requests == 0:
        return 0.0
    return errors / requests
