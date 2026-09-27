"""Twin c05: register_key() mutable default list shared across calls."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from cache import register_key


def test_register_key_does_not_share_state_across_calls():
    """A key registered in one logical context must not appear seen in a fresh context."""
    # First call: registers "token-A", returns False (not seen before)
    register_key("token-A")
    # Second independent call with a different key should return False (never seen)
    # If the default list is shared, "token-A" persists and a fresh call would
    # see the previous registration. We verify the list is fresh by checking that
    # re-registering in what should be an isolated call does not carry prior state.
    result = register_key("token-A")  # should be False in a fresh list
    assert result is False, (
        f"Expected False (fresh list) but got {result!r} — mutable default list is shared"
    )
