"""Core graph algorithms.  Adjacency-list form: dict[node, list[node]]."""

from __future__ import annotations

import heapq
from collections import defaultdict, deque
from typing import Hashable, Iterable

Node = Hashable
Adj = dict[Node, list[Node]]
WAdj = dict[Node, list[tuple[Node, float]]]


def bfs(start: Node, adj: Adj) -> dict[Node, int]:
    """Unweighted shortest path from start to every reachable node.

    Time: Θ(V + E).  Space: Θ(V).
    """
    dist = {start: 0}
    q: deque[Node] = deque([start])
    while q:
        u = q.popleft()
        for v in adj.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def dfs_iterative(start: Node, adj: Adj) -> list[Node]:
    """Iterative DFS preorder.  Time: Θ(V + E)."""
    out: list[Node] = []
    visited: set[Node] = set()
    stack: list[Node] = [start]
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        out.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                stack.append(v)
    return out


def topological_sort(nodes: Iterable[Node], adj: Adj) -> list[Node] | None:
    """Kahn's algorithm.  Returns a topological order or None if a cycle exists.

    Time: Θ(V + E).  Space: Θ(V).
    """
    indeg: dict[Node, int] = {v: 0 for v in nodes}
    for u in indeg:
        for v in adj.get(u, []):
            indeg[v] = indeg.get(v, 0) + 1
    q = deque([v for v, d in indeg.items() if d == 0])
    order: list[Node] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == len(indeg) else None


def dijkstra(start: Node, adj: WAdj) -> dict[Node, float]:
    """Single-source shortest paths with non-negative weights.

    Time: Θ((V + E) log V) with binary heap.  Space: Θ(V).
    Reference: Dijkstra (1959); CLRS § 24.3.
    """
    dist: dict[Node, float] = {start: 0.0}
    pq: list[tuple[float, Node]] = [(0.0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in adj.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
