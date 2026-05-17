# Module 06 — Sorting and Searching

**By the end you can:**
1. Pick the right sort for a problem (stable vs unstable, in-place vs auxiliary, comparison vs radix) and defend the choice.
2. Write the four binary-search variants (exact match, first-`>=`, last-`<=`, "binary search on answer") without off-by-one bugs.
3. State the comparison lower bound and explain when radix/counting sort beats `n log n`.

**Time budget:** 30 min reading + 5–6 h lab.

---

## 1. Sort taxonomy

| Sort | Best | Avg | Worst | Space | Stable | In place | Use when... |
|---|---|---|---|---|---|---|---|
| Insertion | n | n² | n² | 1 | yes | yes | n ≤ ~32 or nearly sorted |
| Bubble | n | n² | n² | 1 | yes | yes | never in production |
| Selection | n² | n² | n² | 1 | no | yes | minimize writes |
| Merge | n log n | n log n | n log n | n | yes | no | stability required, external sort, linked lists |
| Quicksort (random pivot) | n log n | n log n | n² | log n | no | yes | in-place, hot path |
| Heapsort | n log n | n log n | n log n | 1 | no | yes | guaranteed bound, no extra space |
| Timsort (Python `sorted`, Java) | n | n log n | n log n | n | yes | no | the default in Python |
| Counting sort | n + k | n + k | n + k | n + k | yes | no | small integer range k |
| Radix sort | d(n + b) | d(n + b) | d(n + b) | n + b | yes | no | fixed-width keys |

`Python's sorted` uses **Timsort** (Peters 2002). It is `Θ(n log n)` worst case, `Θ(n)` best case on already-sorted runs, and **stable**. Source: `Objects/listsort.txt` in CPython.

## 2. Comparison lower bound

Any comparison-based sort requires `Ω(n log n)` comparisons in the worst case. Proof via decision-tree argument (CLRS § 8.1): there are `n!` possible orderings; a decision tree distinguishing them must have at least `n!` leaves, depth `log₂(n!) = Ω(n log n)`.

This is why counting/radix sort can be faster: they don't compare keys, they bucket them.

## 3. The four binary-search invariants

Bug-free binary search lives or dies on the invariant. Pick one and never deviate.

| Variant | Initial range | Invariant | What you return |
|---|---|---|---|
| Exact match (return index or -1) | `[lo=0, hi=n-1]` (closed) | answer ∈ `[lo, hi]` | mid on match; -1 if `lo > hi` |
| First index with `a[i] >= target` | `[lo=0, hi=n]` (half-open right) | answer ∈ `[lo, hi]` | `lo` after loop |
| Last index with `a[i] <= target` | symmetric to above | symmetric | `hi - 1` |
| Binary search on **answer** | `[lo=feasible-low, hi=feasible-high]` | answer ∈ `[lo, hi]` | `lo` if monotone-feasible predicate |

For the "first-with-property" variant the loop is:

```python
def first_with(p, lo, hi):
    # invariant: every answer is in [lo, hi]; lo may equal hi at exit.
    while lo < hi:
        mid = (lo + hi) // 2
        if p(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo  # smallest index where p is True, or hi if no such index
```

## 4. Binary search on the answer

Many "find min X such that ..." problems are NOT searches in an array — they are searches over a value range with a monotone predicate. Examples in this module:

| Problem | Search space | Predicate (monotone in capacity) |
|---|---|---|
| Koko eating bananas (`09`) | min eat rate | `total hours <= H` |
| Capacity to ship packages (`10`) | min ship capacity | `days needed <= D` |
| Split array largest sum (`11`) | min largest part | `parts needed <= K` |

Pattern: define `feasible(x)`. Binary-search the smallest `x` for which `feasible(x)` is True. Time = `log(value range) * cost(feasible)`.

## How to use this module

1. Read.
2. Skim `solutions/binary_search.py` and `solutions/sorts.py`.
3. Open `notebook.ipynb` for the sort race.
4. `pytest 06-sorting-searching/tests -q` should be green.
5. Work through `problems/`.

## Run

```
pytest 06-sorting-searching -q
```

## References

- CLRS § 2, § 6, § 7, § 8 (sorting).
- Tim Peters, *listsort.txt*: https://github.com/python/cpython/blob/main/Objects/listsort.txt
- Bentley & McIlroy (1993), *Engineering a sort function*. (Hoare partition refinements.)
