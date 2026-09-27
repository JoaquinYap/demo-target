import subprocess
import pathlib

run = '.antibody/runs/20260926-230641-4fdd23'
variants_dir = pathlib.Path(run) / 'variants'
variants_dir.mkdir(exist_ok=True)


def make_patch(target, mutate_fn, patch_name, new_file=False):
    if new_file:
        pathlib.Path(target).write_text(mutate_fn(), encoding='utf-8')
        subprocess.run(['git', 'add', '-N', target], check=True)
        diff = subprocess.run(['git', 'diff', '--', target], capture_output=True).stdout
        (variants_dir / patch_name).write_bytes(diff)
        pathlib.Path(target).unlink()
        subprocess.run(['git', 'restore', '--staged', target], capture_output=True)
    else:
        orig = pathlib.Path(target).read_text(encoding='utf-8')
        pathlib.Path(target).write_text(mutate_fn(orig), encoding='utf-8')
        diff = subprocess.run(['git', 'diff', '--', target], capture_output=True).stdout
        (variants_dir / patch_name).write_bytes(diff)
        subprocess.run(['git', 'checkout', '--', target], check=True)


# v01: indirection — variable stored first, then `value or default`
def v01(orig):
    old = '    value = env.get("PORT")\n    return value if value is not None else default\n\n\ndef get_workers'
    new = '    value = env.get("PORT")\n    return value or default\n\n\ndef get_workers'
    assert old in orig, f"v01 marker not found in orig:\n{orig!r}"
    return orig.replace(old, new, 1)

make_patch('src/env_helpers.py', v01, 'v01.patch')
print('v01 done')


# v02: relocation — new module with same pattern
def v02_content():
    lines = [
        '"""Application settings loader."""',
        '',
        '',
        'def get_log_level(settings: dict, default: str = "INFO") -> str:',
        '    """Return the log level from settings."""',
        '    return settings.get("log_level") or default',
        '',
    ]
    return '\n'.join(lines)

make_patch('src/settings.py', v02_content, 'v02.patch', new_file=True)
print('v02 done')


# v03: indirection — helper function wraps .get(), then `or default`
def v03(orig):
    old = '    return flags.get("rate_limit") or default\n'
    new = '    return _lookup(flags, "rate_limit") or default\n\n\ndef _lookup(d: dict, key: str):\n    return d.get(key)\n'
    assert old in orig, f"v03 marker not found:\n{orig!r}"
    return orig.replace(old, new, 1)

make_patch('src/feature_flags.py', v03, 'v03.patch')
print('v03 done')


# v04: api_alias — try/except + `or default`
def v04(orig):
    old = '    value = env.get("WORKERS")\n    return value if value is not None else default\n'
    new = '    try:\n        value = env["WORKERS"]\n    except KeyError:\n        value = None\n    return value or default\n'
    assert old in orig, f"v04 marker not found:\n{orig!r}"
    return orig.replace(old, new, 1)

make_patch('src/env_helpers.py', v04, 'v04.patch')
print('v04 done')


# v05: syntax — reversed ternary `default if not value else value`
def v05(orig):
    old = '    value = env.get("PREFIX")\n    return value if value is not None else default\n'
    new = '    value = env.get("PREFIX")\n    return default if not value else value\n'
    assert old in orig, f"v05 marker not found:\n{orig!r}"
    return orig.replace(old, new, 1)

make_patch('src/env_helpers.py', v05, 'v05.patch')
print('v05 done')


# v06: relocation — new app_config module
def v06_content():
    lines = [
        '"""Application-level configuration helpers."""',
        '',
        '',
        'def get_cache_ttl(config: dict, default: int = 300) -> int:',
        '    """Return the cache TTL from config."""',
        '    return config.get("cache_ttl") or default',
        '',
    ]
    return '\n'.join(lines)

make_patch('src/app_config.py', v06_content, 'v06.patch', new_file=True)
print('v06 done')
