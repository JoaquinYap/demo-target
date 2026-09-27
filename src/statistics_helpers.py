"""Statistics helpers."""


def mean(values: list) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if len(values) == 0:
        return 0.0
    return sum(values) / len(values)


def ratio(numerator: float, denominator: float) -> float:
    """Return numerator divided by denominator."""
    if denominator == 0:
        return 0.0
    return numerator / denominator


def weighted_average(scores: list, weights: list) -> float:
    """Return weighted average given scores and weights."""
    if sum(weights) == 0:
        return 0.0
    return sum(s * w for s, w in zip(scores, weights)) / sum(weights)
