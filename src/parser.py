"""CSV data parser.

BUG: bare except swallows ALL errors silently — the caller never knows
something went wrong and gets None or garbage data back.
"""


def parse_integer(value: str) -> int:
    """Parse a string into an integer."""
    try:
        return int(value)
    except:  # BUG: catches EVERYTHING including KeyboardInterrupt, SystemExit
        return 0  # BUG: silently returns 0 — caller thinks parsing succeeded


def parse_float(value: str) -> float:
    """Parse a string into a float."""
    try:
        return float(value)
    except:  # BUG: bare except
        return 0.0  # BUG: silent failure


def parse_row(row: str, delimiter: str = ",") -> list:
    """Split a CSV row into fields."""
    try:
        return row.strip().split(delimiter)
    except:  # BUG: bare except — hides real issues like row being None
        return []
