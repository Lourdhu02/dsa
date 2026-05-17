import sys
from collections import defaultdict


def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    """Tarjan's bridge algorithm.  Time: Θ(V + E)."""
    sys.setrecursionlimit(10**6)
    adj = defaultdict(list)
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
    disc = [-1] * n
    low = [0] * n
    bridges: list[list[int]] = []
    timer = [0]

    def _dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in adj[u]:
            if disc[v] == -1:
                _dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append([u, v])
            elif v != parent:
                low[u] = min(low[u], disc[v])

    for u in range(n):
        if disc[u] == -1:
            _dfs(u, -1)
    return bridges
