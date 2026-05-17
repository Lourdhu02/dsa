# Module 08 — Heaps and Priority Queues

**By the end you can:**
1. Implement a binary heap by hand: `push`, `pop`, `peek`, `heapify` — all with Big-O justifications.
2. Use `heapq` idiomatically (it's a min-heap; for max-heap, negate keys).
3. Apply the **top-K with heap** and **k-way merge** patterns.
4. Maintain a running median in `Θ(log n)` per insert via two heaps.

**Time budget:** 30 min reading + 4–6 h lab.

---

## 1. Binary heap

A complete binary tree stored in an array. For 0-indexed:

| Position | Index |
|---|---|
| parent of `i` | `(i - 1) // 2` |
| left child of `i` | `2*i + 1` |
| right child of `i` | `2*i + 2` |

**Min-heap invariant:** every node's value ≤ its children's. Hence the root is the global min.

| Op | Cost |
|---|---|
| `peek` (min) | Θ(1) |
| `push` | Θ(log n) (sift-up) |
| `pop` | Θ(log n) (sift-down on the moved last element) |
| `heapify` (build from a list) | **Θ(n)** — see CLRS § 6.3 |

Why heapify is Θ(n), not Θ(n log n): nodes deeper in the tree need fewer sift-downs, and there are exponentially more of them. The sum `Σ_{h=0}^{log n} (n / 2^(h+1)) · h = Θ(n)`.

## 2. Python's heapq

`heapq` is a **min-heap** over a regular list:

```python
import heapq

xs = [3, 1, 4, 1, 5]
heapq.heapify(xs)          # in place, Θ(n)
heapq.heappush(xs, 2)      # Θ(log n)
heapq.heappop(xs)          # returns smallest, Θ(log n)
heapq.nsmallest(k, xs)     # Θ(n log k)
heapq.nlargest(k, xs)      # Θ(n log k)
```

For a **max-heap**, store `(-key, value)` tuples and negate on read.

## 3. The top-K with heap pattern

Two valid approaches for "find the k largest of n":

| Approach | Time | Space | When to use |
|---|---|---|---|
| Sort then slice | Θ(n log n) | Θ(n) for sort scratch | k close to n |
| Min-heap of size k | **Θ(n log k)** | Θ(k) | k << n |

The heap variant scans once. For each element: push; if heap exceeds k, pop. At the end the heap has the k largest. **Memorize this.**

## 4. K-way merge

Merging k sorted streams into one sorted output:

- Push one entry from each stream into a min-heap.
- Pop the smallest, append to output, push the next entry from that stream.
- Total: `Θ(N log k)` where `N = total elements`.

## 5. Running median (two heaps)

Maintain a max-heap of the lower half and a min-heap of the upper half. Sizes differ by at most 1. Median = top of the larger heap, or the average of both tops if sizes are equal. Insert is `Θ(log n)`, query is `Θ(1)`.

## How to use this module

1. Read.
2. Skim `solutions/heap.py` for the hand-rolled min-heap.
3. `pytest 08-heaps-priority-queues/tests -q` should be green.
4. Work through `problems/`.

## Run

```
pytest 08-heaps-priority-queues -q
```

## References

- CLRS § 6 (heapsort), § 19 (Fibonacci heaps).
- Williams, J. W. J. (1964), *Algorithm 232: heapsort.*
- `heapq` docs: https://docs.python.org/3/library/heapq.html
