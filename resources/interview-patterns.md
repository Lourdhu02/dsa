# 25 Interview Patterns mapped to modules

These are the patterns that cover ~95% of coding-interview questions and the majority of production algorithmic code. Each pattern points to the module where it is taught and at least one practice problem.

| # | Pattern | Core idea | Module | Representative problem |
|---|---|---|---|---|
| 1 | Two pointers | Move a left and right cursor through a sorted/array to find pairs | 01 | `01-arrays-strings/02-two-sum-sorted` |
| 2 | Fast / slow pointer (runner) | Two pointers at different speeds; cycle detection, midpoint | 03 | `03-linked-lists/06-linked-list-cycle` |
| 3 | Sliding window (fixed size) | Maintain a window of size k, slide one step at a time | 01 | `01-arrays-strings/05-max-sum-subarray-k` |
| 4 | Sliding window (variable size) | Shrink/grow window to maintain an invariant | 01 | `01-arrays-strings/07-longest-substring-no-repeat` |
| 5 | Prefix sums | Pre-compute cumulative array; answer range queries in O(1) | 01 | `01-arrays-strings/09-subarray-sum-equals-k` |
| 6 | Hash map for counting / lookup | Trade space for O(1) lookup | 02 | `02-hashing/01-two-sum` |
| 7 | Monotonic stack | Stack maintains sorted invariant; next-greater problems | 04 | `04-stacks-queues/05-next-greater-element` |
| 8 | Monotonic deque | Deque with monotonic invariant; sliding-window min/max | 04 | `04-stacks-queues/08-sliding-window-maximum` |
| 9 | Binary search on answer | Search over a value range, not the array | 06 | `06-sorting-searching/09-koko-eating-bananas` |
| 10 | Sort + greedy | Sort then make locally optimal choice | 13 | `13-greedy-backtracking-bits/02-meeting-rooms-ii` |
| 11 | Merge intervals | Sort by start, merge overlapping | 06 | `06-sorting-searching/12-merge-intervals` |
| 12 | Top-K with heap | Min-heap of size k for top-k of stream | 08 | `08-heaps-priority-queues/03-top-k-frequent` |
| 13 | K-way merge | Heap of pointers across k sorted sequences | 08 | `08-heaps-priority-queues/07-merge-k-sorted-lists` |
| 14 | BFS shortest path (unweighted) | Layer-by-layer traversal | 09 | `09-graphs/04-shortest-path-unweighted` |
| 15 | DFS / backtracking | Explore, recurse, undo | 13 | `13-greedy-backtracking-bits/06-permutations` |
| 16 | Topological sort | Kahn's BFS over in-degree | 09 | `09-graphs/08-course-schedule` |
| 17 | Dijkstra / weighted shortest path | Greedy relax via min-heap | 09 | `09-graphs/10-network-delay-time` |
| 18 | Union-Find / DSU | Group connectivity in near-constant amortized | 11 | `11-union-find-advanced-trees/03-number-of-provinces` |
| 19 | Tree DFS (pre/in/post-order) | Recurse children, combine results | 07 | `07-trees/02-binary-tree-inorder` |
| 20 | Tree BFS (level-order) | Queue layer by layer | 07 | `07-trees/05-level-order-traversal` |
| 21 | Trie | Character-by-character prefix index | 10 | `10-tries-strings/01-implement-trie` |
| 22 | DP — 1D | Build answer from earlier indices in O(n) memory | 12 | `12-dynamic-programming/02-climbing-stairs` |
| 23 | DP — 2D | Build a table over two dimensions | 12 | `12-dynamic-programming/10-edit-distance` |
| 24 | DP on subsets (bitmask) | State indexed by bitmask of chosen items | 12 | `12-dynamic-programming/17-tsp-bitmask` |
| 25 | Bit manipulation | XOR tricks, low-bit isolation, popcount | 13 | `13-greedy-backtracking-bits/14-single-number` |

When you face a new problem in the wild, run through this list mentally and ask "could the input shape unlock pattern N?" — that mapping is usually faster than re-deriving from scratch.
