import json
import os

from solutions.graph import bfs, dfs_iterative, dijkstra, topological_sort

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _load_small():
    with open(os.path.join(REPO_ROOT, "common", "testdata", "graph_small.json")) as f:
        data = json.load(f)
    adj: dict = {n: [] for n in data["nodes"]}
    wadj: dict = {n: [] for n in data["nodes"]}
    for u, v, w in data["edges"]:
        adj[u].append(v)
        wadj[u].append((v, w))
    return data, adj, wadj


def test_bfs_shape():
    _, adj, _ = _load_small()
    d = bfs("A", adj)
    assert d["A"] == 0
    assert d["C"] == 1
    assert d["B"] == 1 or d["B"] == 2  # graph dependent; at least reachable


def test_dfs_visits_reachable():
    _, adj, _ = _load_small()
    visited = dfs_iterative("A", adj)
    assert "A" in visited and "J" in visited  # both reachable


def test_dijkstra_matches_expected():
    data, _, wadj = _load_small()
    dist = dijkstra("A", wadj)
    for k, v in data["shortest_paths_from_A"].items():
        assert dist[k] == v


def test_topo_sort_basic_dag():
    nodes = ["a", "b", "c", "d"]
    adj = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}
    order = topological_sort(nodes, adj)
    assert order is not None
    pos = {n: i for i, n in enumerate(order)}
    for u in nodes:
        for v in adj[u]:
            assert pos[u] < pos[v]


def test_topo_sort_cycle_returns_none():
    nodes = ["a", "b", "c"]
    adj = {"a": ["b"], "b": ["c"], "c": ["a"]}
    assert topological_sort(nodes, adj) is None
