"""Order data access.

BUG: direct dict key access — same KeyError mistake as user_profile.py.
"""


def get_order_status(order: dict) -> str:
    """Return the order status."""
    # BUG: crashes with KeyError if 'status' is missing
    return order["status"]


def get_shipping_address(order: dict) -> str:
    """Return the shipping address."""
    # BUG: same
    return order["shipping_address"]


def get_discount_code(order: dict) -> str:
    """Return the discount code applied to the order."""
    # BUG: discount_code is optional in most orders — will almost always crash
    return order["discount_code"]
