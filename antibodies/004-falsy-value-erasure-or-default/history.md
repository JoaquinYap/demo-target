# Antibody 004: Falsy-value erasure: `value or default` silently replaces any valid falsy config value (0, False, empty string) with the default.

Created 2026-09-27T02:43:56+00:00 from fix_commit `03e0464`.

## What broke

In Python, `0 or 30` evaluates to `30`, `False or False` evaluates to `False` (the default, not the set value), and `'' or 'x'` evaluates to `'x'`. Any caller that explicitly sets a falsy value in the config silently receives the default instead.

**Pattern:** A config/settings lookup uses `value or default` (boolean short-circuit) instead of an explicit `None`-check, so legitimate falsy values such as 0, False, or '' are treated as absent and overwritten by the default.

**Triggers when:** A config key is present in the mapping with a falsy but meaningful value (e.g. timeout=0, max_retries=0, debug=False, feature_flag=False, prefix=''); The reader uses `config.get(key) or default` or `settings.get(key) or default` or the equivalent `x = d.get(k); return x or default`

## How it was fixed

Replace `value or default` with an explicit None-guard: `value if value is not None else default`, or use `dict.get(key, default)` when the key is always expected to be absent rather than falsy.

Original instance: `src/config_loader.py:8`

## Twins found and proven

| Twin | Location | Status | Test |
|---|---|---|---|
| c01 | `src/feature_flags.py:10` | fixed | `tests/antibody/test_twin_c01_feature_flag_false.py` |
| c02 | `src/feature_flags.py:16` | fixed | `tests/antibody/test_twin_c02_rate_limit_zero.py` |
| c03 | `src/env_helpers.py:10` | fixed | `tests/antibody/test_twin_c03_port_zero.py` |
| c04 | `src/env_helpers.py:16` | fixed | `tests/antibody/test_twin_c04_workers_zero.py` |
| c05 | `src/env_helpers.py:22` | fixed | `tests/antibody/test_twin_c05_prefix_empty_string.py` |

## Immunity

| Round | Detected | Immunity |
|---|---|---|
| 0 (before Antibody) | 6/6 | 100% |
| 1 | 6/6 | 100% |
| 2 | 6/6 | 100% |

## Defenses

- Semgrep rule: `.antibody/antibodies/004-falsy-value-erasure-or-default/rule.yml`
- Regression tests: listed in the twins table above.
