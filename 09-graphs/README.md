# Module 09 — Graphs

**By the end you can:**
1. Pick the right graph representation: adjacency list vs adjacency matrix vs edge list.
2. Run BFS and DFS as templates without reinventing them per problem.
3. Topologically sort a DAG with both Kahn's algorithm and DFS post-order.
4. Apply Dijkstra and A* over weighted graphs, and explain when each is admissible.
5. Find MSTs with Prim and Kruskal.

**Time budget:** 40 min reading + 6 h lab.

---

## 1. Representations

| Representation | Space | Iterate neighbors | Edge query (u,v) | Use when |
|---|---|---|---|---|
| Adjacency list | Θ(V + E) | Θ(deg(u)) | Θ(deg(u)) | sparse graphs (E ≪ V²) |
| Adjacency matrix | Θ(V²) | Θ(V) | Θ(1) | dense graphs, frequent edge queries |
| Edge list | Θ(E) | n/a (must scan) | Θ(E) | Kruskal, sorted edge algorithms |

In Python the canonical choice is a `dict[node, list[node]]` adjacency list. For weighted graphs: `dict[node, list[tuple[node, weight]]]`.

## 2. BFS and DFS templates

**BFS** discovers nodes in order of *number of edges from the source*. It computes unweighted shortest paths. Time `Θ(V + E)`, space `Θ(V)`.

```python
from collections import deque

def bfs(start, adj):
    visited = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return visited
```

**DFS** discovers nodes by recursion (or explicit stack). It's the right traversal for tree-like decomposition, cycle detection, topological sort, SCC. Time `Θ(V + E)`, space `Θ(V)`.

## 3. Topological sort

A DAG only — a graph with a cycle has no topo order.

| Algorithm | Idea |
|---|---|
| **Kahn's** (BFS) | Repeatedly emit nodes with in-degree 0; decrement neighbors. |
| **DFS post-order** | Reverse post-order of DFS gives a topo order. |

Both run in `Θ(V + E)`. Kahn detects cycles naturally (some nodes never reach in-degree 0).

## 4. Dijkstra's shortest path

For non-negative edge weights only. With a binary heap (`heapq`), `Θ((V + E) log V)`.

```python
import heapq

def dijkstra(src, adj):
    dist = {src: 0}
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue              # stale entry, skip
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

The "lazy" decrease-key — pushing duplicates and skipping stale entries — is the idiomatic Python pattern. With a Fibonacci heap you'd get the textbook `Θ(V log V + E)` but the constants in Python make it usually slower than the binary-heap version.

**Negative edges?** Use Bellman-Ford (`Θ(V·E)`). Dijkstra silently gives wrong answers; never call it on a graph that might have negative weights.

## 5. A* search

A* is Dijkstra with a **heuristic** `h(v)` added to the priority: `f(v) = g(v) + h(v)`, where `g` is the actual cost so far. If `h` is **admissible** (never overestimates) AND **consistent** (monotone), A* finds the optimal path and expands fewer nodes than Dijkstra. Reference: Hart, Nilsson, Raphael (1968).

## 6. MST: Prim vs Kruskal

| Algorithm | Approach | Time |
|---|---|---|
| Prim | Grow a tree by always picking the cheapest crossing edge | Θ((V + E) log V) with binary heap |
| Kruskal | Sort edges; add if it doesn't form a cycle (Union-Find checks) | Θ(E log V) |

Both produce the same total weight; structure may differ if multiple edges have equal weight.

## How to use this module

1. Read.
2. Skim `solutions/graph.py` (BFS, DFS, Dijkstra, topo).
3. `pytest 09-graphs/tests -q` should be green.
4. Open `notebook.ipynb` to see the canonical small graph drawn.
5. Work through `problems/`.

## Run

```
pytest 09-graphs -q
```

## References

- CLRS § 22 (graph algorithms), § 23 (MST), § 24 (shortest paths), § 25 (all-pairs).
- Hart, Nilsson, Raphael (1968), *A formal basis for the heuristic determination of minimum cost paths.*
- `heapq` docs and lazy decrease-key idiom.
