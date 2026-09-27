import subprocess

RUN = r".antibody\runs\20260926-230945-12b21b\variants"


def make_patch(variant_id, file_path, new_content):
    with open(file_path, 'w', newline='\n') as f:
        f.write(new_content)
    result = subprocess.run(['git', 'diff', '--', file_path], capture_output=True, text=True)
    patch = result.stdout
    with open(f"{RUN}\\{variant_id}.patch", 'w', newline='\n') as f:
        f.write(patch)
    subprocess.run(['git', 'checkout', '--', file_path])
    return patch


METRICS_ORIG = open('src/metrics.py').read()
STATS_ORIG = open('src/statistics_helpers.py').read()

# v01: throughput without guard
metrics_v01 = '"""Metrics reporting."""\n\n\ndef throughput(items_processed: int, time_seconds: float) -> float:\n    """Return items processed per second."""\n    return items_processed / time_seconds\n\n\ndef hit_ratio(hits: int, misses: int) -> float:\n    """Return cache hit ratio."""\n    if hits + misses == 0:\n        return 0.0\n    return hits / (hits + misses)\n\n\ndef p99_normalized(p99: float, baseline: float) -> float:\n    """Return p99 latency normalized against the baseline."""\n    if baseline == 0:\n        return 0.0\n    return p99 / baseline\n'
p = make_patch('v01', 'src/metrics.py', metrics_v01)
print("v01:", "ok" if p.strip() else "empty")

# v02: ratio with alias d, no guard
stats_v02 = '"""Statistics helpers."""\n\n\ndef mean(values: list) -> float:\n    """Return the arithmetic mean of a list of numbers."""\n    if len(values) == 0:\n        return 0.0\n    return sum(values) / len(values)\n\n\ndef ratio(numerator: float, denominator: float) -> float:\n    """Return numerator divided by denominator."""\n    d = denominator\n    return numerator / d\n\n\ndef weighted_average(scores: list, weights: list) -> float:\n    """Return weighted average given scores and weights."""\n    if sum(weights) == 0:\n        return 0.0\n    return sum(s * w for s, w in zip(scores, weights)) / sum(weights)\n'
p = make_patch('v02', 'src/statistics_helpers.py', stats_v02)
print("v02:", "ok" if p.strip() else "empty")

# v04: weighted_average with total_weight variable, no guard
stats_v04 = '"""Statistics helpers."""\n\n\ndef mean(values: list) -> float:\n    """Return the arithmetic mean of a list of numbers."""\n    if len(values) == 0:\n        return 0.0\n    return sum(values) / len(values)\n\n\ndef ratio(numerator: float, denominator: float) -> float:\n    """Return numerator divided by denominator."""\n    if denominator == 0:\n        return 0.0\n    return numerator / denominator\n\n\ndef weighted_average(scores: list, weights: list) -> float:\n    """Return weighted average given scores and weights."""\n    total_weight = sum(weights)\n    return sum(s * w for s, w in zip(scores, weights)) / total_weight\n'
p = make_patch('v04', 'src/statistics_helpers.py', stats_v04)
print("v04:", "ok" if p.strip() else "empty")

# v05: mean with // instead of /
stats_v05 = '"""Statistics helpers."""\n\n\ndef mean(values: list) -> float:\n    """Return the arithmetic mean of a list of numbers."""\n    return sum(values) // len(values)\n\n\ndef ratio(numerator: float, denominator: float) -> float:\n    """Return numerator divided by denominator."""\n    if denominator == 0:\n        return 0.0\n    return numerator / denominator\n\n\ndef weighted_average(scores: list, weights: list) -> float:\n    """Return weighted average given scores and weights."""\n    if sum(weights) == 0:\n        return 0.0\n    return sum(s * w for s, w in zip(scores, weights)) / sum(weights)\n'
p = make_patch('v05', 'src/statistics_helpers.py', stats_v05)
print("v05:", "ok" if p.strip() else "empty")

# v06: p99_normalized with is None guard instead of == 0
metrics_v06 = '"""Metrics reporting."""\n\n\ndef throughput(items_processed: int, time_seconds: float) -> float:\n    """Return items processed per second."""\n    if time_seconds == 0:\n        return 0.0\n    return items_processed / time_seconds\n\n\ndef hit_ratio(hits: int, misses: int) -> float:\n    """Return cache hit ratio."""\n    if hits + misses == 0:\n        return 0.0\n    return hits / (hits + misses)\n\n\ndef p99_normalized(p99: float, baseline: float) -> float:\n    """Return p99 latency normalized against the baseline."""\n    if baseline is None:\n        return 0.0\n    return p99 / baseline\n'
p = make_patch('v06', 'src/metrics.py', metrics_v06)
print("v06:", "ok" if p.strip() else "empty")

print("done")
