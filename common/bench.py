"""Tiny micro-benchmark harness for the perf modules.

Usage:
    from common.bench import time_it, sweep

    time_it(lambda: sorted(xs))                 # one shot
    sweep(my_sort, sizes=[1_000, 10_000, 100_000])  # growth curve

Notes on measurement quality:

- We use ``time.perf_counter_ns`` (monotonic, highest resolution) rather than
  ``time.time``.  See PEP 564 for the rationale.
- Each measurement runs the target ``repeat`` times and reports the best run,
  not the mean.  Best-of-K is robust to OS jitter; the mean would be dominated
  by the worst noisy sample.  This is the same convention as ``timeit``.
- We freshly construct the input inside the timed block when a builder is
  given so we measure the algorithm, not the JIT-warmth of the input list.

This is *not* a substitute for a real benchmark tool like ``pyperf`` or
``hyperfine``; it is intentionally small so the source is readable inside a
lesson.
"""

from __future__ import annotations

import gc
import statistics
import time
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence


@dataclass(frozen=True)
class BenchResult:
    """One measurement row.  ``ns`` fields are *nanoseconds*."""

    label: str
    n: int
    best_ns: int
    median_ns: int
    repeat: int

    @property
    def best_us(self) -> float:
        return self.best_ns / 1_000.0

    @property
    def best_ms(self) -> float:
        return self.best_ns / 1_000_000.0

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return f"{self.label:24} n={self.n:>8}  best={self.best_ms:>8.3f} ms  median={self.median_ns/1e6:>8.3f} ms"


def time_it(fn: Callable[[], object], *, repeat: int = 5, label: str = "") -> BenchResult:
    """Best-of-``repeat`` wall-clock time of a zero-arg callable.

    Time:  O(repeat * cost(fn))
    Space: O(repeat) for the samples list.
    """
    gc_was_enabled = gc.isenabled()
    gc.disable()
    try:
        samples: list[int] = []
        for _ in range(repeat):
            t0 = time.perf_counter_ns()
            fn()
            samples.append(time.perf_counter_ns() - t0)
    finally:
        if gc_was_enabled:
            gc.enable()
    return BenchResult(
        label=label or getattr(fn, "__name__", "anon"),
        n=0,
        best_ns=min(samples),
        median_ns=int(statistics.median(samples)),
        repeat=repeat,
    )


def sweep(
    fn: Callable[[int], object],
    sizes: Sequence[int],
    *,
    repeat: int = 3,
    label: str = "",
) -> list[BenchResult]:
    """Run ``fn(n)`` for each ``n in sizes`` and return one BenchResult per size.

    The function ``fn`` is expected to take ``n`` and do all of: build the
    input *and* run the algorithm.  Doing both inside the timed block keeps
    cache effects honest at the cost of including allocation in the number.

    Time:  O(sum(cost(fn(n)) for n in sizes) * repeat)
    Space: O(len(sizes))
    """
    out: list[BenchResult] = []
    for n in sizes:
        r = time_it(lambda n=n: fn(n), repeat=repeat, label=label or getattr(fn, "__name__", "anon"))
        out.append(BenchResult(label=r.label, n=n, best_ns=r.best_ns, median_ns=r.median_ns, repeat=repeat))
    return out


def fmt_table(rows: Iterable[BenchResult]) -> str:
    """Pretty-print a list of BenchResult as a markdown table."""
    lines = ["| label | n | best (ms) | median (ms) |", "|---|---:|---:|---:|"]
    for r in rows:
        lines.append(f"| {r.label} | {r.n} | {r.best_ms:.3f} | {r.median_ns/1e6:.3f} |")
    return "\n".join(lines)
