"""Data loader from external sources.

BUG: bare except silently swallows errors — same mistake as parser.py.
"""
import json


def load_json(text: str) -> dict:
    """Parse a JSON string into a dict."""
    try:
        return json.loads(text)
    except:  # BUG: bare except — hides malformed JSON silently
        return {}  # BUG: caller gets empty dict, thinks load succeeded


def load_number(value: str) -> float:
    """Convert a string value to a number."""
    try:
        return float(value)
    except:  # BUG: bare except
        return -1.0  # BUG: -1.0 looks like valid data to the caller


def safe_split(text: str, sep: str) -> list:
    """Split text by separator."""
    try:
        return text.split(sep)
    except:  # BUG: hides NoneType errors when text is None
        return []
