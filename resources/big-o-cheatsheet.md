# Big-O Cheat Sheet

Canonical complexities. **Worst case unless noted.** Source: CLRS 4th ed. unless otherwise cited.

## Data structures — operations

| Structure | Access | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| Array (static) | Θ(1) | Θ(n) | Θ(n) | Θ(n) | Θ(n) |
| Dynamic array (Python `list`, C++ `vector`) | Θ(1) | Θ(n) | amortized Θ(1) append, Θ(n) middle | Θ(n) | Θ(n) |
| Singly linked list | Θ(n) | Θ(n) | Θ(1) at head, Θ(n) middle | Θ(1) given node ref, else Θ(n) | Θ(n) |
| Doubly linked list | Θ(n) | Θ(n) | Θ(1) at either end, Θ(n) middle | Θ(1) given node ref | Θ(n) |
| Hash table (open addressing, load α < 1) | — | Θ(1) avg, Θ(n) worst | Θ(1) amortized | Θ(1) avg | Θ(n) |
| Balanced BST (red-black, AVL) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | Θ(n) |
| Binary heap | Θ(1) min/max | Θ(n) | Θ(log n) | Θ(log n) | Θ(n) |
| Fibonacci heap | Θ(1) min | Θ(n) | Θ(1) amortized | Θ(log n) amortized | Θ(n) |
| Trie (k-ary) | Θ(L) | Θ(L) | Θ(L) | Θ(L) | Θ(N · σ) worst |
| Union-Find (PC + UBR) | — | α(n) amortized | α(n) amortized | n/a | Θ(n) |
| Segment tree | Θ(log n) range query / update | Θ(log n) | Θ(log n) | n/a | Θ(n) |
| Binary indexed tree (BIT) | Θ(log n) prefix / point update | Θ(log n) | Θ(log n) | n/a | Θ(n) |

L = length of key; σ = alphabet size; N = total characters; α = inverse Ackermann (≤ 4 in practice).

> **Hash-table caveat:** Python's `dict` uses open addressing with perturbation (see [PEP 7 + dictobject.c](https://github.com/python/cpython/blob/main/Objects/dictobject.c)). Insertion is amortized Θ(1) but a pathological key sequence can still degrade to Θ(n).

## Sorting

| Algorithm | Best | Average | Worst | Space | Stable? | In-place? |
|---|---|---|---|---|---|---|
| Insertion sort | Θ(n) | Θ(n²) | Θ(n²) | Θ(1) | yes | yes |
| Selection sort | Θ(n²) | Θ(n²) | Θ(n²) | Θ(1) | no | yes |
| Bubble sort | Θ(n) | Θ(n²) | Θ(n²) | Θ(1) | yes | yes |
| Merge sort | Θ(n log n) | Θ(n log n) | Θ(n log n) | Θ(n) | yes | no |
| Quicksort (random pivot) | Θ(n log n) | Θ(n log n) expected | Θ(n²) | Θ(log n) | no | yes |
| Heap sort | Θ(n log n) | Θ(n log n) | Θ(n log n) | Θ(1) | no | yes |
| Tim sort (Python `sorted`, Java) | Θ(n) | Θ(n log n) | Θ(n log n) | Θ(n) | yes | no |
| Counting sort | Θ(n + k) | Θ(n + k) | Θ(n + k) | Θ(n + k) | yes | no |
| Radix sort | Θ(d · (n + b)) | Θ(d · (n + b)) | Θ(d · (n + b)) | Θ(n + b) | yes | no |

CLRS 4th ed. §§ 2, 6, 7, 8.

> **Comparison lower bound:** any comparison-based sort requires Ω(n log n) comparisons in the worst case (decision-tree argument, CLRS § 8.1).

## Searching

| Algorithm | Time | Notes |
|---|---|---|
| Linear search | Θ(n) | Always works. |
| Binary search | Θ(log n) | Requires sorted input. |
| Exponential search | Θ(log i) | i = position of answer; great for unbounded streams. |
| Ternary search | Θ(log n) on unimodal functions | Don't use on sorted arrays — binary is faster (CLRS § 9). |
| Interpolation search | Θ(log log n) average, Θ(n) worst | Only on uniformly distributed keys. |

## Graphs

| Algorithm | Time | Space |
|---|---|---|
| BFS / DFS | Θ(V + E) | Θ(V) |
| Topological sort (Kahn or DFS) | Θ(V + E) | Θ(V) |
| Tarjan SCC | Θ(V + E) | Θ(V) |
| Kosaraju SCC | Θ(V + E) | Θ(V) |
| Dijkstra (binary heap) | Θ((V + E) log V) | Θ(V) |
| Dijkstra (Fibonacci heap) | Θ(V log V + E) | Θ(V) |
| Bellman-Ford | Θ(V · E) | Θ(V) |
| Floyd-Warshall | Θ(V³) | Θ(V²) |
| Prim's MST (binary heap) | Θ((V + E) log V) | Θ(V) |
| Kruskal's MST (with DSU) | Θ(E log V) | Θ(V) |
| A* (with consistent heuristic) | O(b^d) worst, but expands only optimal frontier when heuristic is admissible | Θ(V) |

CLRS § 22–25.

## String algorithms

| Algorithm | Preproc. | Match |
|---|---|---|
| Naive | — | Θ(n · m) |
| KMP | Θ(m) | Θ(n) |
| Z-algorithm | Θ(n + m) | Θ(n + m) |
| Rabin-Karp (rolling hash) | Θ(m) | Θ(n) expected, Θ(n · m) worst |
| Boyer-Moore | Θ(m + σ) | Θ(n / m) best, Θ(n · m) worst |
| Aho-Corasick (k patterns) | Θ(Σ\|pᵢ\|) | Θ(n + k_match) |

## Recurrences (master theorem)

For T(n) = a · T(n/b) + f(n) where a ≥ 1, b > 1:

| Case | Condition | T(n) |
|---|---|---|
| 1 | f(n) = O(n^(log_b a − ε)) | Θ(n^(log_b a)) |
| 2 | f(n) = Θ(n^(log_b a) · log^k n) | Θ(n^(log_b a) · log^(k+1) n) |
| 3 | f(n) = Ω(n^(log_b a + ε)) and a·f(n/b) ≤ c·f(n) for some c < 1 | Θ(f(n)) |

CLRS § 4.5. Common applications:

- Merge sort: T(n) = 2T(n/2) + Θ(n) → case 2 → Θ(n log n).
- Binary search: T(n) = T(n/2) + Θ(1) → case 2 → Θ(log n).
- Strassen: T(n) = 7T(n/2) + Θ(n²) → case 1 → Θ(n^log₂ 7) ≈ Θ(n^2.807).

## What Big-O does *not* measure

- Constants. A Θ(n log n) sort with bad cache behavior can lose to a Θ(n²) sort for n < 32 (this is why Tim Sort and `std::sort` switch to insertion sort below a threshold).
- Memory hierarchy effects. Two algorithms with the same Θ-class can differ 10× in wall time depending on cache locality.
- I/O cost (Aggarwal-Vitter external memory model is a separate analysis).
- Constants hidden in the soft-O notation `Õ(·)` (suppresses polylog factors).
