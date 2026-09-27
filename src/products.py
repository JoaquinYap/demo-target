"""Product catalog access.

BUG: direct dict key access — same KeyError mistake as user_profile.py.
"""


def get_product_price(product: dict) -> float:
    """Return the product price."""
    # BUG: crashes if 'price' key is missing
    return product["price"]


def get_product_category(product: dict) -> str:
    """Return the product category."""
    # BUG: same — category might not always be present
    return product["category"]


def get_stock_count(product: dict) -> int:
    """Return the available stock count."""
    # BUG: stock might be absent for pre-order items
    return product["stock"]
