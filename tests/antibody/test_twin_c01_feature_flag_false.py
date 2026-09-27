"""Twin c01: is_feature_enabled returns wrong value when flag is explicitly False."""
from src.feature_flags import is_feature_enabled


def test_explicit_false_flag_not_overridden_by_default():
    """When a flag is explicitly set to False, it must NOT be replaced by the default True."""
    flags = {"my_feature": False}
    result = is_feature_enabled(flags, "my_feature", default=True)
    assert result is False, f"Expected False but got {result!r}"
