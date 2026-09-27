# Antibody 002: A mutable object (list or dict) is used as a function parameter default, causing it to be shared across all calls that omit the argument.

Created 2026-09-27T02:02:39+00:00 from fix_commit `51fac9e`.

## What broke

Python evaluates default argument expressions once when the def statement is executed, not on each call. Any call that relies on the default therefore mutates the same object, making state leak from one call to the next.

**Pattern:** def f(param: list = []) or def f(param: dict = {}) — mutable literal used as a default argument value so a single object is created once at function-definition time and mutated by every call that does not pass an explicit value.

**Triggers when:** The caller omits the argument on at least two successive calls; The function body mutates the default (append, extend, update, etc.)

## How it was fixed

Replace the mutable default with None and, inside the function body, assign a fresh mutable object when the parameter is None.

Original instance: `src/notifications.py:7`

## Twins found and proven

| Twin | Location | Status | Test |
|---|---|---|---|
| c01 | `src/queue_manager.py:7` | fixed | `tests/antibody/test_twin_c01_enqueue_shared_list.py` |
| c02 | `src/queue_manager.py:14` | fixed | `tests/antibody/test_twin_c02_batch_jobs_shared_list.py` |
| c03 | `src/cache.py:7` | fixed | `tests/antibody/test_twin_c03_cache_result_shared_dict.py` |
| c04 | `src/cache.py:14` | fixed | `tests/antibody/test_twin_c04_push_to_cache_shared_list.py` |
| c05 | `src/cache.py:21` | fixed | `tests/antibody/test_twin_c05_register_key_shared_list.py` |

## Immunity

| Round | Detected | Immunity |
|---|---|---|
| 0 (before Antibody) | 3/6 | 50% |
| 1 | 4/6 | 67% |
| 2 | 6/6 | 100% |

## Defenses

- Semgrep rule: `.antibody/antibodies/002-mutable-default-argument/rule.yml`
- Regression tests: listed in the twins table above.
