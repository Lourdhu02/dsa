# Bibliography

## Primary references

- **CLRS** — Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. Chapter citations throughout the course use this edition.
- **Sedgewick & Wayne** — Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley. Strong on red-black trees, MSTs, and string algorithms.
- **Knuth TAOCP** — Knuth, D. E. *The Art of Computer Programming*. Volumes 1, 3, and 4A in particular.
- **CP-Algorithms** — [https://cp-algorithms.com](https://cp-algorithms.com) — best free reference for competitive-style algorithms with proofs.

## Papers cited in-place

### Hashing and probing
- Knuth, D. E. (1962). *Notes on "open" addressing*.
- Pagh, R., & Rodler, F. F. (2001). *Cuckoo hashing*. ESA 2001.

### Sorting
- Peters, T. (2002). *Timsort description.* `listsort.txt` in the CPython source: https://github.com/python/cpython/blob/main/Objects/listsort.txt
- Musser, D. R. (1997). *Introspective sorting and selection algorithms*. Software: Practice and Experience.

### Trees and balanced trees
- Bayer, R. (1972). *Symmetric binary B-trees: data structure and maintenance algorithms*. The red-black tree origin.
- Adelson-Velsky, G., & Landis, E. (1962). *An algorithm for the organization of information*. The AVL tree.
- Sleator, D. D., & Tarjan, R. E. (1985). *Self-adjusting binary search trees*. Splay trees.
- Morris, J. M. (1979). *Traversing binary trees simply and cheaply*. The O(1)-space Morris traversal.

### Heaps and priority queues
- Williams, J. W. J. (1964). *Heapsort*. CACM 7(6).
- Fredman, M. L., & Tarjan, R. E. (1987). *Fibonacci heaps and their uses in improved network optimization algorithms*. JACM 34(3).

### Graphs
- Dijkstra, E. W. (1959). *A note on two problems in connexion with graphs*. Numerische Mathematik 1.
- Tarjan, R. E. (1972). *Depth-first search and linear graph algorithms*. SIAM J. Computing 1(2). (SCC)
- Kruskal, J. B. (1956). *On the shortest spanning subtree of a graph and the traveling salesman problem*. Proc. AMS 7(1).
- Prim, R. C. (1957). *Shortest connection networks and some generalizations*. Bell System Tech. J. 36(6).
- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). *A formal basis for the heuristic determination of minimum cost paths*. The A* paper.

### Union-Find
- Tarjan, R. E., & van Leeuwen, J. (1984). *Worst-case analysis of set union algorithms*. JACM 31(2). Proves the α(n) amortized bound for path compression + union by rank.

### Strings
- Knuth, D. E., Morris, J. H., & Pratt, V. R. (1977). *Fast pattern matching in strings*. SIAM J. Computing 6(2).
- Karp, R. M., & Rabin, M. O. (1987). *Efficient randomized pattern-matching algorithms*. IBM J. Research and Development 31(2).
- Aho, A. V., & Corasick, M. J. (1975). *Efficient string matching: An aid to bibliographic search*. CACM 18(6).

### Approximate Nearest Neighbour (Capstone)
- Malkov, Y. A., & Yashunin, D. A. (2018). *Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs*. IEEE TPAMI. https://arxiv.org/abs/1603.09320
- Jegou, H., Douze, M., & Schmid, C. (2011). *Product quantization for nearest neighbor search*. IEEE TPAMI 33(1). (IVF + PQ)
- Indyk, P., & Motwani, R. (1998). *Approximate nearest neighbors: towards removing the curse of dimensionality*. STOC.

## Language-stdlib documentation

- Python `dict`/`set` implementation notes: https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
- Python `heapq`: https://docs.python.org/3/library/heapq.html
- Python `bisect`: https://docs.python.org/3/library/bisect.html
- Python `collections.deque`: https://docs.python.org/3/library/collections.html#collections.deque
- Python `sorted` and Timsort: see Peters' `listsort.txt` above.

## Blog posts and lecture notes worth bookmarking

- Erik Demaine's MIT 6.851 *Advanced Data Structures* lecture notes: https://courses.csail.mit.edu/6.851/
- Tim Roughgarden's lecture videos on greedy proofs and randomized algorithms (Stanford CS261).
- Pavel Mavrin's *Competitive Programmer's Handbook*: https://cses.fi/book/book.pdf
