# Module 03 — Linked Lists

**By the end you can:**
1. Implement singly-linked and doubly-linked lists with the right pointer hygiene (no dangling next-pointers, no off-by-one tail bugs).
2. Apply the **runner / fast-slow pointer** pattern for cycle detection, midpoint finding, and Nth-from-end.
3. Reverse a linked list in place in `Θ(n)` time and `Θ(1)` extra space, both iteratively and recursively.
4. Build an `LRUCache` from scratch using `dict` + doubly-linked list.

**Time budget:** 30 min reading + 4 h lab.

---

## 1. When is a linked list the right tool?

Almost never in production Python — `list` and `collections.deque` cover 99% of needs and are far better for cache locality. The exception is **anywhere you need `Θ(1)` removal of an arbitrary known node**: hash-map-backed LRU caches, intrusive lists in C systems code, free lists in allocators. The interview-frequent reason is that they're a clean exercise for pointer reasoning.

```mermaid
graph LR
    H[head] --> A[1]
    A --> B[2]
    B --> C[3]
    C --> D[4]
    D --> N[null]
```

## 2. The runner / fast-slow pointer

Two pointers that traverse from the same start but at different speeds.

| Use | Setup |
|---|---|
| Detect a cycle | slow += 1, fast += 2; they meet inside a cycle (Floyd's algorithm) |
| Find the cycle's entrance | After detection, restart one pointer at head; advance both by 1 until they meet |
| Find the midpoint | slow += 1, fast += 2; when fast hits the end, slow is at the middle |
| Find Nth from end | move fast N steps first, then advance both until fast hits the end |

Proof sketch for Floyd's algorithm (CLRS § 22 exercises): if a cycle exists with `λ` nodes and the tail before the cycle has `μ` nodes, after `μ` steps `slow` is at the cycle entry and `fast` is `μ mod λ` steps into the cycle. They will meet after at most `λ` more steps.

## 3. In-place reverse

The canonical three-pointer dance:

```
prev = None, curr = head
while curr:
    nxt  = curr.next      # remember rest
    curr.next = prev      # flip pointer
    prev = curr           # advance prev
    curr = nxt            # advance curr
return prev               # new head
```

Invariant: `prev` points to the head of the reversed prefix; `curr` points to the head of the original suffix yet to be reversed.

## 4. LRU cache

Standard interview "data structure design" problem and a common cache backing in real systems (`functools.lru_cache` is similar). Requirements:

| Op | Cost |
|---|---|
| `get(key)`     | Θ(1) avg |
| `put(key, v)`  | Θ(1) avg |
| evict LRU      | Θ(1) — done as part of `put` when over capacity |

Hash map gives `Θ(1)` lookup; doubly-linked list gives `Θ(1)` move-to-front and remove-from-back. The map's value is a pointer **into** the list, so `get` finds the node and `move_to_front` mutates pointers in place.

## How to use this module

1. Read.
2. Skim `solutions/singly.py`, `solutions/lru.py`.
3. `pytest 03-linked-lists/tests -q` should be green.
4. Work through `problems/`.

## Run

```
pytest 03-linked-lists -q
```

## References

- CLRS 4th ed. § 10.2 (linked lists).
- `functools.lru_cache` source: https://github.com/python/cpython/blob/main/Lib/functools.py
- Floyd, R. W. (1967), *Nondeterministic algorithms*. (Cycle-finding origin.)
