"""Module 09 (graphs) manifest."""

PROBLEMS = [
    {
        "slug": "01-number-of-islands",
        "title": "Number of islands",
        "difficulty": "medium",
        "tags": ["dfs", "bfs", "grid"],
        "statement": "Given a 2D grid of `'1'` (land) and `'0'` (water), return the number of islands. An island is a maximal connected component of land cells, connected 4-directionally.",
        "signature": "def num_islands(grid: list[list[str]]) -> int: ...",
        "examples_md": """## Examples

```
[['1','1','1','1','0'],
 ['1','1','0','1','0'],
 ['1','1','0','0','0'],
 ['0','0','0','0','0']]   -> 1

[['1','1','0','0','0'],
 ['1','1','0','0','0'],
 ['0','0','1','0','0'],
 ['0','0','0','1','1']]   -> 3
```""",
        "constraints": "",
        "hint": "Scan each cell; on '1' DFS/BFS to flood-fill, counting +1 per starting cell.",
        "starter": """
def num_islands(grid: list[list[str]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    def _dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        _dfs(i + 1, j)
        _dfs(i - 1, j)
        _dfs(i, j + 1)
        _dfs(i, j - 1)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                _dfs(i, j)
    return count
""",
        "tests": """
import pytest
from solution import num_islands


def test_one():
    g = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert num_islands(g) == 1


def test_three():
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(g) == 3


def test_empty():
    assert num_islands([]) == 0
""",
    },
    {
        "slug": "02-clone-graph",
        "title": "Clone undirected graph",
        "difficulty": "medium",
        "tags": ["dfs", "bfs", "graph"],
        "statement": "Given a reference to a node in a connected undirected graph, return a deep copy.",
        "signature": "class Node:\n    val: int\n    neighbors: list['Node']\n\ndef clone_graph(node: Node | None) -> Node | None: ...",
        "examples_md": """## Examples

Graph `1 - 2, 1 - 4, 2 - 3, 3 - 4` cloned: same structure, all-new Node objects.""",
        "constraints": "",
        "hint": "BFS/DFS. Map original->copy. For each visited node, build its copy's neighbors list via the map.",
        "starter": """
class Node:
    def __init__(self, val: int = 0, neighbors: "list[Node] | None" = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class Node:
    def __init__(self, val: int = 0, neighbors: "list[Node] | None" = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    if node is None:
        return None
    mapping: dict[int, Node] = {}

    def _clone(u: Node) -> Node:
        if id(u) in mapping:
            return mapping[id(u)]
        copy = Node(u.val)
        mapping[id(u)] = copy
        copy.neighbors = [_clone(v) for v in u.neighbors]
        return copy

    return _clone(node)
""",
        "tests": """
from solution import Node, clone_graph


def test_small_graph():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.neighbors = [b, d]
    b.neighbors = [a, c]
    c.neighbors = [b, d]
    d.neighbors = [a, c]
    copy = clone_graph(a)
    assert copy is not a
    assert copy.val == 1
    assert {n.val for n in copy.neighbors} == {2, 4}


def test_none():
    assert clone_graph(None) is None
""",
    },
    {
        "slug": "03-shortest-path-binary-matrix",
        "title": "Shortest path in binary matrix",
        "difficulty": "medium",
        "tags": ["bfs", "grid"],
        "statement": "In an `n x n` binary matrix, return the length of the shortest path from `(0, 0)` to `(n-1, n-1)` walking through 0-cells using 8-directional steps. Return -1 if no such path exists.",
        "signature": "def shortest_path(grid: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| grid | result |
|---|---|
| `[[0, 1], [1, 0]]` | 2 |
| `[[0, 0, 0], [1, 1, 0], [1, 1, 0]]` | 4 |""",
        "constraints": "",
        "hint": "BFS over 8-neighbours. Track distance per cell.",
        "starter": """
def shortest_path(grid: list[list[int]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import deque


def shortest_path(grid: list[list[int]]) -> int:
    n = len(grid)
    if not n or grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1
    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    q = deque([(0, 0, 1)])
    seen = {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if r == n - 1 and c == n - 1:
            return d
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1
""",
        "tests": """
import pytest
from solution import shortest_path


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ],
)
def test_examples(grid, expected):
    assert shortest_path(grid) == expected
""",
    },
    {
        "slug": "04-course-schedule",
        "title": "Course schedule",
        "difficulty": "medium",
        "tags": ["topological-sort", "graph"],
        "statement": "There are `num_courses` courses labeled `0..num_courses-1`. `prereqs[i] = [a, b]` means take `b` before `a`. Return True if you can finish all courses.",
        "signature": "def can_finish(num_courses: int, prereqs: list[list[int]]) -> bool: ...",
        "examples_md": """## Examples

| num_courses | prereqs | result |
|---|---|---|
| 2 | `[[1, 0]]` | True |
| 2 | `[[1, 0], [0, 1]]` | False |""",
        "constraints": "",
        "hint": "Kahn's algorithm. If topological order has length < num_courses, there's a cycle.",
        "starter": """
def can_finish(num_courses: int, prereqs: list[list[int]]) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import deque


def can_finish(num_courses: int, prereqs: list[list[int]]) -> bool:
    indeg = [0] * num_courses
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    for a, b in prereqs:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == num_courses
""",
        "tests": """
import pytest
from solution import can_finish


@pytest.mark.parametrize(
    "n, prereqs, expected",
    [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False), (4, [[1, 0], [2, 1], [3, 2]], True)],
)
def test_examples(n, prereqs, expected):
    assert can_finish(n, prereqs) is expected
""",
    },
    {
        "slug": "05-course-schedule-ii",
        "title": "Course schedule II",
        "difficulty": "medium",
        "tags": ["topological-sort"],
        "statement": "Same as course-schedule but return a valid course order, or `[]` if impossible.",
        "signature": "def find_order(num_courses: int, prereqs: list[list[int]]) -> list[int]: ...",
        "examples_md": """## Examples

| n | prereqs | one valid order |
|---|---|---|
| 4 | `[[1, 0], [2, 0], [3, 1], [3, 2]]` | `[0, 1, 2, 3]` |
| 2 | `[[0, 1], [1, 0]]` | `[]` |""",
        "constraints": "",
        "hint": "Kahn's; return the emitted order.",
        "starter": """
def find_order(num_courses: int, prereqs: list[list[int]]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import deque


def find_order(num_courses: int, prereqs: list[list[int]]) -> list[int]:
    indeg = [0] * num_courses
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    for a, b in prereqs:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    out: list[int] = []
    while q:
        u = q.popleft()
        out.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return out if len(out) == num_courses else []
""",
        "tests": """
import pytest
from solution import find_order


def _validate(n, prereqs, order):
    if not order:
        return False
    pos = {c: i for i, c in enumerate(order)}
    if len(pos) != n:
        return False
    return all(pos[b] < pos[a] for a, b in prereqs)


def test_basic():
    order = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert _validate(4, [[1, 0], [2, 0], [3, 1], [3, 2]], order)


def test_cycle():
    assert find_order(2, [[0, 1], [1, 0]]) == []
""",
    },
    {
        "slug": "06-network-delay-time",
        "title": "Network delay time (Dijkstra)",
        "difficulty": "medium",
        "tags": ["dijkstra", "shortest-path"],
        "statement": "Given `n` nodes labeled `1..n`, `times[i] = [u, v, w]` is a directed edge of weight `w`. Starting at node `k`, return the time it takes for all nodes to receive the signal (max shortest path) or -1 if unreachable.",
        "signature": "def network_delay_time(times: list[list[int]], n: int, k: int) -> int: ...",
        "examples_md": """## Examples

| times | n | k | result |
|---|---|---|---|
| `[[2, 1, 1], [2, 3, 1], [3, 4, 1]]` | 4 | 2 | 2 |
| `[[1, 2, 1]]` | 2 | 1 | 1 |
| `[[1, 2, 1]]` | 2 | 2 | -1 |""",
        "constraints": "",
        "hint": "Standard Dijkstra; answer = max of distances or -1 if any node unreachable.",
        "starter": """
def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq
from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    dist = {k: 0}
    pq = [(0, k)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    if len(dist) < n:
        return -1
    return max(dist.values())
""",
        "tests": """
import pytest
from solution import network_delay_time


@pytest.mark.parametrize(
    "times, n, k, expected",
    [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ],
)
def test_examples(times, n, k, expected):
    assert network_delay_time(times, n, k) == expected
""",
    },
    {
        "slug": "07-cheapest-flights-k-stops",
        "title": "Cheapest flights within K stops",
        "difficulty": "medium",
        "tags": ["bfs", "shortest-path", "bellman-ford"],
        "statement": "Given `n` cities, `flights[i] = [from, to, price]`, find the cheapest price from `src` to `dst` with at most `k` stops, or -1.",
        "signature": "def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int: ...",
        "examples_md": """## Examples

| n | flights | src | dst | k | result |
|---|---|---|---|---|---|
| 3 | `[[0, 1, 100], [1, 2, 100], [0, 2, 500]]` | 0 | 2 | 1 | 200 |
| 3 | same | 0 | 2 | 0 | 500 |""",
        "constraints": "",
        "hint": "Bellman-Ford for `k + 1` iterations; updates only from the previous round's distances.",
        "starter": """
def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(k + 1):
        nxt = dist[:]
        for u, v, w in flights:
            if dist[u] + w < nxt[v]:
                nxt[v] = dist[u] + w
        dist = nxt
    return -1 if dist[dst] == float("inf") else int(dist[dst])
""",
        "tests": """
import pytest
from solution import find_cheapest_price


flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]


@pytest.mark.parametrize(
    "k, expected",
    [(1, 200), (0, 500)],
)
def test_examples(k, expected):
    assert find_cheapest_price(3, flights, 0, 2, k) == expected
""",
    },
    {
        "slug": "08-word-ladder",
        "title": "Word ladder",
        "difficulty": "hard",
        "tags": ["bfs", "graph"],
        "statement": "Given two words `begin_word` and `end_word`, and a word list, return the length of the shortest transformation sequence — each adjacent pair differs by one letter. Return 0 if impossible. Count both `begin_word` and `end_word`.",
        "signature": "def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int: ...",
        "examples_md": """## Examples

| begin | end | wordList | result |
|---|---|---|---|
| `\"hit\"` | `\"cog\"` | `[\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]` | 5 |
| `\"hit\"` | `\"cog\"` | `[\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]` | 0 |""",
        "constraints": "",
        "hint": "Build a wildcard-pattern index: for each word, list `_at`, `c_t`, `ca_` patterns. Two words sharing a pattern are neighbors. BFS.",
        "starter": """
def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import defaultdict, deque


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end_word not in words:
        return 0
    patterns: dict[str, list[str]] = defaultdict(list)
    L = len(begin_word)
    for w in words | {begin_word}:
        for i in range(L):
            patterns[w[:i] + "*" + w[i + 1:]].append(w)
    visited = {begin_word}
    q = deque([(begin_word, 1)])
    while q:
        w, d = q.popleft()
        if w == end_word:
            return d
        for i in range(L):
            key = w[:i] + "*" + w[i + 1:]
            for nb in patterns[key]:
                if nb not in visited:
                    visited.add(nb)
                    q.append((nb, d + 1))
            patterns[key] = []
    return 0
""",
        "tests": """
import pytest
from solution import ladder_length


def test_reachable():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5


def test_unreachable():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
""",
    },
    {
        "slug": "09-surrounded-regions",
        "title": "Surrounded regions",
        "difficulty": "medium",
        "tags": ["dfs", "bfs", "grid"],
        "statement": "Given an `m x n` board of `'X'` and `'O'`, capture all regions of `'O'` that are NOT connected to a border `'O'`. Flip captured `'O'`s to `'X'`.",
        "signature": "def solve(board: list[list[str]]) -> None: ...",
        "examples_md": """## Examples

Border-connected `O`s survive; interior `O`s become `X`.""",
        "constraints": "",
        "hint": "DFS/BFS from each border `O`, marking with a sentinel. Then sweep: sentinel -> O, O -> X.",
        "starter": """
def solve(board: list[list[str]]) -> None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def solve(board: list[list[str]]) -> None:
    if not board:
        return
    m, n = len(board), len(board[0])

    def _dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '#'
        _dfs(i + 1, j); _dfs(i - 1, j); _dfs(i, j + 1); _dfs(i, j - 1)

    for i in range(m):
        _dfs(i, 0); _dfs(i, n - 1)
    for j in range(n):
        _dfs(0, j); _dfs(m - 1, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
""",
        "tests": """
from solution import solve


def test_basic():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solve(board)
    assert board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]


def test_no_change_when_open():
    board = [["O", "O"], ["O", "O"]]
    solve(board)
    assert board == [["O", "O"], ["O", "O"]]
""",
    },
    {
        "slug": "10-pacific-atlantic-water-flow",
        "title": "Pacific Atlantic water flow",
        "difficulty": "medium",
        "tags": ["dfs", "bfs", "grid"],
        "statement": "Given a 2D matrix of heights, return all cells from which water can flow to both the Pacific (top/left edges) and Atlantic (bottom/right edges). Water flows to a neighbor with equal or lower height.",
        "signature": "def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]: ...",
        "examples_md": """## Examples

```
[[1, 2, 2, 3, 5],
 [3, 2, 3, 4, 4],
 [2, 4, 5, 3, 1],
 [6, 7, 1, 4, 5],
 [5, 1, 1, 2, 4]]
result: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```""",
        "constraints": "",
        "hint": "Reverse the flow: BFS/DFS from each ocean (upstream — only step to equal-or-higher cells). Intersection of reachable sets is the answer.",
        "starter": """
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]

    def _dfs(i, j, seen):
        seen[i][j] = True
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj] and heights[ni][nj] >= heights[i][j]:
                _dfs(ni, nj, seen)

    for i in range(m):
        _dfs(i, 0, pacific); _dfs(i, n - 1, atlantic)
    for j in range(n):
        _dfs(0, j, pacific); _dfs(m - 1, j, atlantic)
    out: list[list[int]] = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                out.append([i, j])
    return out
""",
        "tests": """
from solution import pacific_atlantic


def test_basic():
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    expected = {(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)}
    result = pacific_atlantic(heights)
    assert {tuple(c) for c in result} == expected
""",
    },
    {
        "slug": "11-min-cost-connect-points",
        "title": "Min cost to connect all points (Prim MST)",
        "difficulty": "medium",
        "tags": ["mst", "heap"],
        "statement": "Given `points = [[x_i, y_i]]`, return the minimum cost to connect all points using Manhattan distance edges between every pair. (Equivalent to MST of the complete graph.)",
        "signature": "def min_cost_connect(points: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| points | result |
|---|---|
| `[[0,0],[2,2],[3,10],[5,2],[7,0]]` | 20 |
| `[[3,12],[-2,5],[-4,1]]` | 18 |""",
        "constraints": "",
        "hint": "Prim's algorithm starting from any node, using a min-heap keyed on edge weight.",
        "starter": """
def min_cost_connect(points: list[list[int]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def min_cost_connect(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0
    in_tree = [False] * n
    total = 0
    pq: list[tuple[int, int]] = [(0, 0)]
    edges_added = 0
    while pq and edges_added < n:
        w, u = heapq.heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        total += w
        edges_added += 1
        for v in range(n):
            if not in_tree[v]:
                d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(pq, (d, v))
    return total
""",
        "tests": """
import pytest
from solution import min_cost_connect


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
        ([[0, 0]], 0),
    ],
)
def test_examples(points, expected):
    assert min_cost_connect(points) == expected
""",
    },
    {
        "slug": "12-evaluate-division",
        "title": "Evaluate division",
        "difficulty": "medium",
        "tags": ["dfs", "bfs", "graph"],
        "statement": "Given `equations[i] = [A, B]` and `values[i] = A / B`, answer `queries[i] = [C, D]` returning `C / D` or `-1.0` if undetermined.",
        "signature": "def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]: ...",
        "examples_md": """## Examples

```
equations=[["a","b"],["b","c"]], values=[2.0, 3.0]
queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
answer  =[6.0,    0.5,    -1.0,   1.0,    -1.0]
```""",
        "constraints": "",
        "hint": "Treat each variable as a node; an equation `a/b = v` means edge `a -> b` weight `v` and `b -> a` weight `1/v`. For each query DFS from C accumulating the product.",
        "starter": """
def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import defaultdict


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    adj: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for (a, b), v in zip(equations, values):
        adj[a].append((b, v))
        adj[b].append((a, 1.0 / v))

    def _query(src: str, dst: str) -> float:
        if src not in adj or dst not in adj:
            return -1.0
        if src == dst:
            return 1.0
        seen = {src}
        stack = [(src, 1.0)]
        while stack:
            u, prod = stack.pop()
            if u == dst:
                return prod
            for v, w in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append((v, prod * w))
        return -1.0

    return [_query(c, d) for c, d in queries]
""",
        "tests": """
import pytest
from solution import calc_equation


def test_basic():
    out = calc_equation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    assert out == [6.0, 0.5, -1.0, 1.0, -1.0]
""",
    },
    {
        "slug": "13-is-graph-bipartite",
        "title": "Is graph bipartite",
        "difficulty": "medium",
        "tags": ["bfs", "dfs", "coloring"],
        "statement": "Given an undirected adjacency-list graph `graph[i] = neighbors of node i`, return True iff it's bipartite (2-colorable).",
        "signature": "def is_bipartite(graph: list[list[int]]) -> bool: ...",
        "examples_md": """## Examples

| graph | result |
|---|---|
| `[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]` | False |
| `[[1, 3], [0, 2], [1, 3], [0, 2]]` | True |""",
        "constraints": "",
        "hint": "BFS coloring. Color each component with 2 colors; conflict → not bipartite.",
        "starter": """
def is_bipartite(graph: list[list[int]]) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import deque


def is_bipartite(graph: list[list[int]]) -> bool:
    n = len(graph)
    color = [-1] * n
    for s in range(n):
        if color[s] != -1:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
""",
        "tests": """
import pytest
from solution import is_bipartite


@pytest.mark.parametrize(
    "graph, expected",
    [
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
        ([], True),
    ],
)
def test_examples(graph, expected):
    assert is_bipartite(graph) is expected
""",
    },
    {
        "slug": "14-all-paths-source-target",
        "title": "All paths from source to target",
        "difficulty": "medium",
        "tags": ["dfs", "backtracking"],
        "statement": "Given a DAG `graph[i] = list of nodes that i can go to`, return all paths from node 0 to node n-1.",
        "signature": "def all_paths(graph: list[list[int]]) -> list[list[int]]: ...",
        "examples_md": """## Examples

`[[1, 2], [3], [3], []]` → `[[0, 1, 3], [0, 2, 3]]`.""",
        "constraints": "",
        "hint": "DFS with current path; on reaching n-1, record a copy.",
        "starter": """
def all_paths(graph: list[list[int]]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def all_paths(graph: list[list[int]]) -> list[list[int]]:
    out: list[list[int]] = []
    target = len(graph) - 1
    path: list[int] = [0]

    def _dfs(u: int) -> None:
        if u == target:
            out.append(path[:])
            return
        for v in graph[u]:
            path.append(v)
            _dfs(v)
            path.pop()

    _dfs(0)
    return out
""",
        "tests": """
import pytest
from solution import all_paths


def test_basic():
    assert sorted(all_paths([[1, 2], [3], [3], []])) == sorted([[0, 1, 3], [0, 2, 3]])


def test_one_node():
    assert all_paths([[]]) == [[0]]
""",
    },
    {
        "slug": "15-find-eventual-safe-states",
        "title": "Find eventual safe states",
        "difficulty": "medium",
        "tags": ["dfs", "cycle-detection"],
        "statement": "A node is safe if every path starting from it eventually leads to a terminal (no outgoing edges) node. Return all safe nodes sorted.",
        "signature": "def eventual_safe_nodes(graph: list[list[int]]) -> list[int]: ...",
        "examples_md": """## Examples

`[[1, 2], [2, 3], [5], [0], [5], [], []]` → `[2, 4, 5, 6]`.""",
        "constraints": "",
        "hint": "Reverse the graph; nodes reachable in the reverse from terminal-only nodes are safe. Or DFS with three colors (unvisited / on-stack / safe).",
        "starter": """
def eventual_safe_nodes(graph: list[list[int]]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def eventual_safe_nodes(graph: list[list[int]]) -> list[int]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * len(graph)

    def _safe(u: int) -> bool:
        if color[u] == GRAY:
            return False
        if color[u] == BLACK:
            return True
        color[u] = GRAY
        for v in graph[u]:
            if not _safe(v):
                return False
        color[u] = BLACK
        return True

    return [u for u in range(len(graph)) if _safe(u)]
""",
        "tests": """
import pytest
from solution import eventual_safe_nodes


def test_basic():
    assert eventual_safe_nodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]
""",
    },
    {
        "slug": "16-redundant-connection",
        "title": "Redundant connection",
        "difficulty": "medium",
        "tags": ["union-find", "graph"],
        "statement": "An undirected graph started as a tree (n nodes, n-1 edges) then had ONE extra edge added. The edge list is in input order. Return the last redundant edge.",
        "signature": "def find_redundant(edges: list[list[int]]) -> list[int]: ...",
        "examples_md": """## Examples

| edges | result |
|---|---|
| `[[1, 2], [1, 3], [2, 3]]` | `[2, 3]` |
| `[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]` | `[1, 4]` |""",
        "constraints": "",
        "hint": "Union-find. Walk edges; the first that joins two nodes already in the same component is the redundant one.",
        "starter": """
def find_redundant(edges: list[list[int]]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_redundant(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 2))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return [u, v]
        parent[ru] = rv
    return []
""",
        "tests": """
import pytest
from solution import find_redundant


@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ],
)
def test_examples(edges, expected):
    assert find_redundant(edges) == expected
""",
    },
    {
        "slug": "17-keys-and-rooms",
        "title": "Keys and rooms",
        "difficulty": "medium",
        "tags": ["bfs", "dfs"],
        "statement": "Rooms 0..n-1; room i contains keys `rooms[i]`. You start in room 0. Return True if you can visit all rooms.",
        "signature": "def can_visit_all_rooms(rooms: list[list[int]]) -> bool: ...",
        "examples_md": """## Examples

`[[1], [2], [3], []]` → True.
`[[1, 3], [3, 0, 1], [2], [0]]` → False (room 2 has key only for itself).""",
        "constraints": "",
        "hint": "DFS/BFS starting at room 0; check that the visited set equals `range(n)`.",
        "starter": """
def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for k in rooms[u]:
            if k not in seen:
                seen.add(k)
                stack.append(k)
    return len(seen) == len(rooms)
""",
        "tests": """
import pytest
from solution import can_visit_all_rooms


@pytest.mark.parametrize(
    "rooms, expected",
    [
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
        ([[]], True),
    ],
)
def test_examples(rooms, expected):
    assert can_visit_all_rooms(rooms) is expected
""",
    },
    {
        "slug": "18-critical-connections",
        "title": "Critical connections (bridges)",
        "difficulty": "hard",
        "tags": ["tarjan", "bridges", "dfs"],
        "statement": "An undirected graph has `n` nodes and a list of connections. Return all *critical* connections — edges whose removal disconnects the graph.",
        "signature": "def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]: ...",
        "examples_md": """## Examples

`n=4, connections=[[0,1],[1,2],[2,0],[1,3]]` → `[[1, 3]]`.""",
        "constraints": "",
        "hint": "Tarjan's bridge-finding algorithm. DFS with discovery times and `low[u]` = smallest discovery reachable. Edge `(u, v)` is a bridge iff `low[v] > disc[u]`.",
        "starter": """
def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import sys
from collections import defaultdict


def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    \"\"\"Tarjan's bridge algorithm.  Time: Θ(V + E).\"\"\"
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
""",
        "tests": """
import pytest
from solution import critical_connections


def _norm(es):
    return sorted(tuple(sorted(e)) for e in es)


def test_basic():
    assert _norm(critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])) == [(1, 3)]


def test_no_bridges():
    assert critical_connections(3, [[0, 1], [1, 2], [2, 0]]) == []
""",
    },
]
