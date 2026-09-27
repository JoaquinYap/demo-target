"""User profile data access.

BUG: accessing dict keys directly without .get() -> KeyError at runtime
when the key is missing.
"""


def get_user_email(profile: dict) -> str:
    """Return the user's email address."""
    # BUG: if 'email' key is missing, raises KeyError
    return profile["email"]


def get_user_role(profile: dict) -> str:
    """Return the user's role."""
    # BUG: same — direct key access without safety
    return profile["role"]


def get_display_name(profile: dict) -> str:
    """Return display name, falling back to username."""
    # BUG: crashes if neither 'display_name' nor 'username' key exists
    return profile["display_name"] or profile["username"]
