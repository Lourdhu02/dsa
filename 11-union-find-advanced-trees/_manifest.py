"""Module 11 (DSU & advanced trees) manifest."""

PROBLEMS = [
    {
        "slug": "01-implement-dsu",
        "title": "Implement DSU (Union-Find)",
        "difficulty": "easy",
        "tags": ["union-find"],
        "statement": "Implement DSU on `n` elements with `find(x)`, `union(x, y) -> bool` (returns True if a merge happened), `connected(x, y) -> bool`, and `count` (number of components).",
        "signature": "class DSU:\n    def __init__(self, n: int) -> None: ...\n    def find(self, x: int) -> int: ...\n    def union(self, x: int, y: int) -> bool: ...\n    def connected(self, x: int, y: int) -> bool: ...\n    count: int",
        "examples_md": """## Examples

```
d = DSU(5)
d.union(0, 1)        # True
d.union(0, 1)        # False
d.connected(0, 1)    # True
d.connected(0, 2)    # False
d.count              # 4
```""",
        "constraints": "",
        "hint": "Path compression in find; union by rank in union.",
        "starter": """
class DSU:
    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def find(self, x: int) -> int:
        raise NotImplementedError

    def union(self, x: int, y: int) -> bool:
        raise NotImplementedError

    def connected(self, x: int, y: int) -> bool:
        raise NotImplementedError
""",
        "reference": """
class DSU:
    def __init__(self, n: int) -> None:
        self._p = list(range(n))
        self._r = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        root = x
        while self._p[root] != root:
            root = self._p[root]
        while self._p[x] != root:
            self._p[x], x = root, self._p[x]
        return root

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self._r[rx] < self._r[ry]:
            rx, ry = ry, rx
        self._p[ry] = rx
        if self._r[rx] == self._r[ry]:
            self._r[rx] += 1
        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
""",
        "tests": """
from solution import DSU


def test_basic():
    d = DSU(5)
    assert d.count == 5
    assert d.union(0, 1)
    assert not d.union(0, 1)
    assert d.connected(0, 1)
    assert not d.connected(0, 2)
    assert d.count == 4
""",
    },
    {
        "slug": "02-number-of-provinces",
        "title": "Number of provinces (DSU)",
        "difficulty": "medium",
        "tags": ["union-find", "graph"],
        "statement": "Given an `n x n` matrix `is_connected[i][j] = 1` iff city `i` and `j` are directly connected, return the number of provinces (connected components).",
        "signature": "def find_circle_num(is_connected: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| matrix | provinces |
|---|---|
| `[[1,1,0],[1,1,0],[0,0,1]]` | 2 |
| `[[1,0,0],[0,1,0],[0,0,1]]` | 3 |""",
        "constraints": "",
        "hint": "Walk upper triangle; union i, j on every 1.",
        "starter": """
def find_circle_num(is_connected: list[list[int]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_circle_num(is_connected: list[list[int]]) -> int:
    n = len(is_connected)
    parent = list(range(n))
    rank = [0] * n
    count = n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        nonlocal count
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        count -= 1

    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                union(i, j)
    return count
""",
        "tests": """
import pytest
from solution import find_circle_num


@pytest.mark.parametrize(
    "m, expected",
    [([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2), ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)],
)
def test_examples(m, expected):
    assert find_circle_num(m) == expected
""",
    },
    {
        "slug": "03-accounts-merge",
        "title": "Accounts merge",
        "difficulty": "medium",
        "tags": ["union-find", "hash-map"],
        "statement": "Given accounts `[name, email1, email2, ...]`, merge accounts that share any email. Return merged accounts with `[name, sorted_emails...]` in any order.",
        "signature": "def accounts_merge(accounts: list[list[str]]) -> list[list[str]]: ...",
        "examples_md": """## Examples

```
[
  [\"John\", \"johnsmith@x\", \"john00@y\"],
  [\"John\", \"johnnybravo@z\"],
  [\"John\", \"johnsmith@x\", \"john_newyork@w\"],
  [\"Mary\", \"mary@x\"]
]
->
[
  [\"John\", \"john00@y\", \"john_newyork@w\", \"johnsmith@x\"],
  [\"John\", \"johnnybravo@z\"],
  [\"Mary\", \"mary@x\"]
]
```""",
        "constraints": "",
        "hint": "Union all emails per account. Map email -> account index. Group emails by their root.",
        "starter": """
def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import defaultdict


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    n = len(accounts)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    email_to_idx: dict[str, int] = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_idx:
                union(email_to_idx[email], i)
            email_to_idx[email] = i

    groups: dict[int, list[str]] = defaultdict(list)
    for email, idx in email_to_idx.items():
        groups[find(idx)].append(email)
    return [[accounts[r][0]] + sorted(emails) for r, emails in groups.items()]
""",
        "tests": """
from solution import accounts_merge


def _norm(rs):
    return sorted(tuple([r[0]] + sorted(r[1:])) for r in rs)


def test_basic():
    accs = [
        ["John", "johnsmith@x", "john00@y"],
        ["John", "johnnybravo@z"],
        ["John", "johnsmith@x", "john_newyork@w"],
        ["Mary", "mary@x"],
    ]
    expected = [
        ["John", "john00@y", "john_newyork@w", "johnsmith@x"],
        ["John", "johnnybravo@z"],
        ["Mary", "mary@x"],
    ]
    assert _norm(accounts_merge(accs)) == _norm(expected)
""",
    },
    {
        "slug": "04-graph-valid-tree",
        "title": "Graph valid tree",
        "difficulty": "medium",
        "tags": ["union-find", "graph"],
        "statement": "Given `n` nodes and an `edges` list, return True if the edges form a valid tree (connected, no cycles).",
        "signature": "def valid_tree(n: int, edges: list[list[int]]) -> bool: ...",
        "examples_md": """## Examples

| n | edges | result |
|---|---|---|
| 5 | `[[0, 1], [0, 2], [0, 3], [1, 4]]` | True |
| 5 | `[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]` | False |""",
        "constraints": "",
        "hint": "Tree iff `len(edges) == n - 1` AND no cycle (DSU detects cycles when union returns False).",
        "starter": """
def valid_tree(n: int, edges: list[list[int]]) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True
""",
        "tests": """
import pytest
from solution import valid_tree


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
        (1, [], True),
    ],
)
def test_examples(n, edges, expected):
    assert valid_tree(n, edges) is expected
""",
    },
    {
        "slug": "05-most-stones-removed",
        "title": "Most stones removed with same row or column",
        "difficulty": "medium",
        "tags": ["union-find"],
        "statement": "Given `stones` (list of `[r, c]` coords), you can remove a stone if it shares a row or column with another remaining stone. Return the max number you can remove.",
        "signature": "def remove_stones(stones: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| stones | result |
|---|---|
| `[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]` | 5 |
| `[[0,0],[0,2],[1,1],[2,0],[2,2]]` | 3 |""",
        "constraints": "",
        "hint": "Two stones sharing row OR column are in the same component (union them). Answer = `n - num_components`.",
        "starter": """
def remove_stones(stones: list[list[int]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def remove_stones(stones: list[list[int]]) -> int:
    parent: dict = {}

    def find(x):
        if parent.get(x, x) == x:
            parent[x] = x
            return x
        root = find(parent[x])
        parent[x] = root
        return root

    def union(x, y):
        parent[find(x)] = find(y)

    for r, c in stones:
        union(("r", r), ("c", c))

    roots = {find(("r", r)) for r, _ in stones}
    return len(stones) - len(roots)
""",
        "tests": """
import pytest
from solution import remove_stones


@pytest.mark.parametrize(
    "stones, expected",
    [
        ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
        ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3),
        ([[0, 0]], 0),
    ],
)
def test_examples(stones, expected):
    assert remove_stones(stones) == expected
""",
    },
    {
        "slug": "06-redundant-connection",
        "title": "Redundant connection (DSU)",
        "difficulty": "medium",
        "tags": ["union-find"],
        "statement": "An undirected graph started as a tree (n nodes, n-1 edges) then had ONE extra edge added. Return the last redundant edge in input order.",
        "signature": "def find_redundant_connection(edges: list[list[int]]) -> list[int]: ...",
        "examples_md": """## Examples

| edges | result |
|---|---|
| `[[1, 2], [1, 3], [2, 3]]` | `[2, 3]` |
| `[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]` | `[1, 4]` |""",
        "constraints": "",
        "hint": "DSU. First edge whose endpoints already share a root is redundant.",
        "starter": """
def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_redundant_connection(edges: list[list[int]]) -> list[int]:
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
from solution import find_redundant_connection


@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ],
)
def test_examples(edges, expected):
    assert find_redundant_connection(edges) == expected
""",
    },
    {
        "slug": "07-satisfiability-equality",
        "title": "Satisfiability of equality equations",
        "difficulty": "medium",
        "tags": ["union-find"],
        "statement": "Given equations like `a==b` and `c!=d`, return True iff they're all satisfiable.",
        "signature": "def equations_possible(equations: list[str]) -> bool: ...",
        "examples_md": """## Examples

| equations | result |
|---|---|
| `[\"a==b\",\"b!=a\"]` | False |
| `[\"a==b\",\"b==c\",\"a==c\"]` | True |
| `[\"a!=a\"]` | False |""",
        "constraints": "",
        "hint": "Union all `==` constraints first, then verify each `!=` constraint connects different components.",
        "starter": """
def equations_possible(equations: list[str]) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def equations_possible(equations: list[str]) -> bool:
    parent = list(range(26))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for eq in equations:
        if eq[1] == "=":
            a, b = ord(eq[0]) - 97, ord(eq[3]) - 97
            parent[find(a)] = find(b)
    for eq in equations:
        if eq[1] == "!":
            a, b = ord(eq[0]) - 97, ord(eq[3]) - 97
            if find(a) == find(b):
                return False
    return True
""",
        "tests": """
import pytest
from solution import equations_possible


@pytest.mark.parametrize(
    "eqs, expected",
    [
        (["a==b", "b!=a"], False),
        (["a==b", "b==c", "a==c"], True),
        (["a!=a"], False),
        (["b==a", "a==b"], True),
    ],
)
def test_examples(eqs, expected):
    assert equations_possible(eqs) is expected
""",
    },
    {
        "slug": "08-range-sum-segment-tree",
        "title": "Range sum query (segment tree)",
        "difficulty": "medium",
        "tags": ["segment-tree"],
        "statement": "Implement `NumArray` with `update(i, val)` and `sum_range(l, r)` (inclusive), each `Θ(log n)`.",
        "signature": "class NumArray:\n    def __init__(self, nums: list[int]) -> None: ...\n    def update(self, i: int, val: int) -> None: ...\n    def sum_range(self, l: int, r: int) -> int: ...",
        "examples_md": """## Examples

```
na = NumArray([1, 3, 5])
na.sum_range(0, 2)   # 9
na.update(1, 2)
na.sum_range(0, 2)   # 8
```""",
        "constraints": "",
        "hint": "Segment tree.",
        "starter": """
class NumArray:
    def __init__(self, nums: list[int]) -> None:
        raise NotImplementedError

    def update(self, i: int, val: int) -> None:
        raise NotImplementedError

    def sum_range(self, l: int, r: int) -> int:
        raise NotImplementedError
""",
        "reference": """
class NumArray:
    def __init__(self, nums: list[int]) -> None:
        self._n = len(nums)
        self._t = [0] * (4 * max(1, self._n))
        if self._n:
            self._build(1, 0, self._n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:
            self._t[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def _update(self, node, lo, hi, i, val):
        if lo == hi:
            self._t[node] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node, lo, mid, i, val)
        else:
            self._update(2 * node + 1, mid + 1, hi, i, val)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def sum_range(self, l: int, r: int) -> int:
        return self._q(1, 0, self._n - 1, l, r)

    def _q(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self._t[node]
        mid = (lo + hi) // 2
        return self._q(2 * node, lo, mid, l, r) + self._q(2 * node + 1, mid + 1, hi, l, r)
""",
        "tests": """
from solution import NumArray


def test_basic():
    na = NumArray([1, 3, 5])
    assert na.sum_range(0, 2) == 9
    na.update(1, 2)
    assert na.sum_range(0, 2) == 8
""",
    },
    {
        "slug": "09-range-sum-bit",
        "title": "Range sum query (BIT)",
        "difficulty": "medium",
        "tags": ["fenwick-bit"],
        "statement": "Same problem as #08 but implement with a Binary Indexed Tree.",
        "signature": "class NumArray:\n    def __init__(self, nums: list[int]) -> None: ...\n    def update(self, i: int, val: int) -> None: ...\n    def sum_range(self, l: int, r: int) -> int: ...",
        "examples_md": """## Examples

Same as the segment-tree version.""",
        "constraints": "",
        "hint": "BIT operates on prefix sums; convert update to a delta against the current value.",
        "starter": """
class NumArray:
    def __init__(self, nums: list[int]) -> None:
        raise NotImplementedError

    def update(self, i: int, val: int) -> None:
        raise NotImplementedError

    def sum_range(self, l: int, r: int) -> int:
        raise NotImplementedError
""",
        "reference": """
class NumArray:
    def __init__(self, nums: list[int]) -> None:
        self._n = len(nums)
        self._a = nums[:]
        self._t = [0] * (self._n + 1)
        for i, v in enumerate(nums, start=1):
            self._add(i, v)

    def _add(self, i, delta):
        while i <= self._n:
            self._t[i] += delta
            i += i & -i

    def _prefix(self, i):
        s = 0
        while i > 0:
            s += self._t[i]
            i -= i & -i
        return s

    def update(self, i: int, val: int) -> None:
        delta = val - self._a[i]
        self._a[i] = val
        self._add(i + 1, delta)

    def sum_range(self, l: int, r: int) -> int:
        return self._prefix(r + 1) - self._prefix(l)
""",
        "tests": """
from solution import NumArray


def test_basic():
    na = NumArray([1, 3, 5])
    assert na.sum_range(0, 2) == 9
    na.update(1, 2)
    assert na.sum_range(0, 2) == 8
""",
    },
    {
        "slug": "10-count-of-range-sums",
        "title": "Count of range sums",
        "difficulty": "hard",
        "tags": ["bit", "merge-sort"],
        "statement": "Given an integer array, return the number of pairs `(i, j)` with `i <= j` such that `lower <= sum(nums[i..j]) <= upper`.",
        "signature": "def count_range_sum(nums: list[int], lower: int, upper: int) -> int: ...",
        "examples_md": """## Examples

| nums | lower | upper | result |
|---|---|---|---|
| `[-2, 5, -1]` | -2 | 2 | 3 |
| `[0]` | 0 | 0 | 1 |""",
        "constraints": "",
        "hint": "Modify merge-sort over prefix sums P. For each i, count j > i with `lower <= P[j] - P[i] <= upper`. Use the sortedness of right half to count in Θ(log n) per i.",
        "starter": """
def count_range_sum(nums: list[int], lower: int, upper: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from bisect import bisect_left, bisect_right


def count_range_sum(nums: list[int], lower: int, upper: int) -> int:
    P = [0]
    for x in nums:
        P.append(P[-1] + x)

    def _sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, cl = _sort(arr[:mid])
        right, cr = _sort(arr[mid:])
        cnt = cl + cr
        for x in left:
            lo = bisect_left(right, x + lower)
            hi = bisect_right(right, x + upper)
            cnt += hi - lo
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged, cnt

    _, total = _sort(P)
    return total
""",
        "tests": """
import pytest
from solution import count_range_sum


@pytest.mark.parametrize(
    "nums, lo, up, expected",
    [([-2, 5, -1], -2, 2, 3), ([0], 0, 0, 1), ([1, 2, 3], 3, 5, 4)],
)
def test_examples(nums, lo, up, expected):
    assert count_range_sum(nums, lo, up) == expected
""",
    },
    {
        "slug": "11-range-update-segment-tree",
        "title": "Range update, range sum (lazy propagation)",
        "difficulty": "hard",
        "tags": ["segment-tree", "lazy-propagation"],
        "statement": "Implement `RangeUpdateSum`: build from list, `range_add(l, r, delta)` adds `delta` to every element in [l, r], `range_sum(l, r)` returns the inclusive sum. Both Θ(log n).",
        "signature": "class RangeUpdateSum:\n    def __init__(self, data: list[int]) -> None: ...\n    def range_add(self, l: int, r: int, delta: int) -> None: ...\n    def range_sum(self, l: int, r: int) -> int: ...",
        "examples_md": """## Examples

```
ru = RangeUpdateSum([1, 1, 1, 1])
ru.range_add(0, 2, 5)
ru.range_sum(0, 3)   # (6+6+6+1) = 19
```""",
        "constraints": "",
        "hint": "Standard lazy seg tree. `lazy[node]` accumulates pending +delta to be pushed to children on the next descent.",
        "starter": """
class RangeUpdateSum:
    def __init__(self, data: list[int]) -> None:
        raise NotImplementedError

    def range_add(self, l: int, r: int, delta: int) -> None:
        raise NotImplementedError

    def range_sum(self, l: int, r: int) -> int:
        raise NotImplementedError
""",
        "reference": """
class RangeUpdateSum:
    def __init__(self, data: list[int]) -> None:
        self._n = len(data)
        self._t = [0] * (4 * max(1, self._n))
        self._lz = [0] * (4 * max(1, self._n))
        if self._n:
            self._build(1, 0, self._n - 1, data)

    def _build(self, node, lo, hi, data):
        if lo == hi:
            self._t[node] = data[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, data)
        self._build(2 * node + 1, mid + 1, hi, data)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def _push(self, node, lo, hi):
        if self._lz[node]:
            mid = (lo + hi) // 2
            for child, length in ((2 * node, mid - lo + 1), (2 * node + 1, hi - mid)):
                self._t[child] += self._lz[node] * length
                self._lz[child] += self._lz[node]
            self._lz[node] = 0

    def range_add(self, l, r, delta):
        self._update(1, 0, self._n - 1, l, r, delta)

    def _update(self, node, lo, hi, l, r, delta):
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._t[node] += delta * (hi - lo + 1)
            self._lz[node] += delta
            return
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        self._update(2 * node, lo, mid, l, r, delta)
        self._update(2 * node + 1, mid + 1, hi, l, r, delta)
        self._t[node] = self._t[2 * node] + self._t[2 * node + 1]

    def range_sum(self, l, r):
        return self._q(1, 0, self._n - 1, l, r)

    def _q(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self._t[node]
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        return self._q(2 * node, lo, mid, l, r) + self._q(2 * node + 1, mid + 1, hi, l, r)
""",
        "tests": """
import random
from solution import RangeUpdateSum


def test_basic():
    ru = RangeUpdateSum([1, 1, 1, 1])
    ru.range_add(0, 2, 5)
    assert ru.range_sum(0, 3) == 19
    assert ru.range_sum(0, 0) == 6
    assert ru.range_sum(3, 3) == 1


def test_random_against_brute():
    rng = random.Random(0)
    n = 30
    a = [rng.randint(-5, 5) for _ in range(n)]
    ru = RangeUpdateSum(a)
    for _ in range(50):
        op = rng.choice(["add", "query"])
        l = rng.randrange(n); r = rng.randrange(l, n)
        if op == "add":
            d = rng.randint(-3, 3)
            for i in range(l, r + 1):
                a[i] += d
            ru.range_add(l, r, d)
        else:
            assert ru.range_sum(l, r) == sum(a[l : r + 1])
""",
    },
    {
        "slug": "12-reverse-pairs",
        "title": "Reverse pairs (BIT)",
        "difficulty": "hard",
        "tags": ["bit", "fenwick"],
        "statement": "Given an array `nums`, return the number of pairs `(i, j)` with `i < j` and `nums[i] > 2 * nums[j]`.",
        "signature": "def reverse_pairs(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[1, 3, 2, 3, 1]` | 2 |
| `[2, 4, 3, 5, 1]` | 3 |""",
        "constraints": "",
        "hint": "Coordinate-compress (the values + 2*values). For each j scanning right, count nums seen so far that are > 2*nums[j] using a BIT keyed by rank.",
        "starter": """
def reverse_pairs(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from bisect import bisect_left


def reverse_pairs(nums: list[int]) -> int:
    sorted_unique = sorted(set(nums + [2 * x for x in nums]))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    n = len(sorted_unique)
    bit = [0] * (n + 2)

    def update(i):
        while i <= n:
            bit[i] += 1
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    count = 0
    for x in reversed(nums):
        # count of seen values y where y < x / 2 strictly, i.e., 2y < x.
        idx = bisect_left(sorted_unique, x) + 1  # rank of x in sorted_unique (>=1)
        # We want y such that x > 2*y, i.e., 2*y < x.  rank of largest 2*y < x:
        target_idx = bisect_left(sorted_unique, x) + 1  # placeholder; recompute via 2*y
        # number of seen entries with value strictly less than x/2 (i.e. 2*value < x).
        # We track by value rank in BIT.
        thr_idx = bisect_left(sorted_unique, (x + 1) // 2 if x % 2 else x // 2)
        # We want indices with value < ceil(x/2). For real x, condition is value*2 < x i.e. value < x/2.
        # Equivalently among integers value <= (x-1)//2 if x integer.
        thr = (x - 1) // 2 if x > 0 else (x // 2) - 1
        thr_rank = bisect_left(sorted_unique, thr + 1)  # count of sorted_unique values <= thr
        count += prefix(thr_rank)
        update(rank[x])
    return count
""",
        "tests": """
import pytest
from solution import reverse_pairs


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 3, 2, 3, 1], 2), ([2, 4, 3, 5, 1], 3), ([], 0), ([5], 0)],
)
def test_examples(nums, expected):
    assert reverse_pairs(nums) == expected
""",
    },
    {
        "slug": "13-largest-component-size-by-common-factor",
        "title": "Largest component size by common factor",
        "difficulty": "hard",
        "tags": ["union-find", "math"],
        "statement": "Two numbers in `nums` are connected if they share a common factor > 1. Return the size of the largest connected component.",
        "signature": "def largest_component_size(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[4, 6, 15, 35]` | 4 |
| `[20, 50, 9, 63]` | 2 |
| `[2, 3, 6, 7, 4, 12, 21, 39]` | 8 |""",
        "constraints": "",
        "hint": "Union each number with its prime factors. Then count the largest group of original numbers (root by primes).",
        "starter": """
def largest_component_size(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def largest_component_size(nums: list[int]) -> int:
    parent: dict = {}
    def find(x):
        if parent.setdefault(x, x) != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        parent[find(x)] = find(y)

    for n in nums:
        x = n
        i = 2
        while i * i <= x:
            if x % i == 0:
                union(n, i)
                while x % i == 0:
                    x //= i
            i += 1
        if x > 1:
            union(n, x)

    groups = Counter(find(n) for n in nums)
    return max(groups.values())
""",
        "tests": """
import pytest
from solution import largest_component_size


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([4, 6, 15, 35], 4),
        ([20, 50, 9, 63], 2),
        ([2, 3, 6, 7, 4, 12, 21, 39], 8),
    ],
)
def test_examples(nums, expected):
    assert largest_component_size(nums) == expected
""",
    },
    {
        "slug": "14-swim-in-rising-water",
        "title": "Swim in rising water",
        "difficulty": "hard",
        "tags": ["union-find", "binary-search-or-dijkstra"],
        "statement": "On `n x n` grid `grid[i][j]` is height. At time `t`, water reaches height `t`. From `(0, 0)` you may move to a neighbour iff both cells have `height <= t`. Return the minimum `t` to reach `(n-1, n-1)`.",
        "signature": "def swim_in_water(grid: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| grid | result |
|---|---|
| `[[0, 2], [1, 3]]` | 3 |
| `[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]` | 16 |""",
        "constraints": "",
        "hint": "Sort cells by height; activate cells in order, union to active neighbours; return current height when (0,0) and (n-1,n-1) connect.",
        "starter": """
def swim_in_water(grid: list[list[int]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def swim_in_water(grid: list[list[int]]) -> int:
    n = len(grid)
    cells = sorted([(grid[i][j], i, j) for i in range(n) for j in range(n)])
    parent = list(range(n * n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    active = [[False] * n for _ in range(n)]
    for h, i, j in cells:
        active[i][j] = True
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and active[ni][nj]:
                parent[find(i * n + j)] = find(ni * n + nj)
        if find(0) == find(n * n - 1):
            return h
    return grid[n - 1][n - 1]
""",
        "tests": """
import pytest
from solution import swim_in_water


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 2], [1, 3]], 3),
        ([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], 16),
    ],
)
def test_examples(grid, expected):
    assert swim_in_water(grid) == expected
""",
    },
    {
        "slug": "15-longest-consecutive-dsu",
        "title": "Longest consecutive sequence (DSU)",
        "difficulty": "medium",
        "tags": ["union-find"],
        "statement": "Given an unsorted integer array, return the length of the longest run of consecutive integers. Solve with DSU. (Module 02 covered the hash-set version.)",
        "signature": "def longest_consecutive(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[100, 4, 200, 1, 3, 2]` | 4 |
| `[]` | 0 |""",
        "constraints": "",
        "hint": "Index-based DSU. For each value `v`, union with `v+1` if seen. Track component sizes.",
        "starter": """
def longest_consecutive(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    parent: dict = {v: v for v in s}
    size: dict = {v: 1 for v in s}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        parent[ry] = rx
        size[rx] += size[ry]
    for v in s:
        if v + 1 in parent:
            union(v, v + 1)
    return max(size[find(v)] for v in s) if s else 0
""",
        "tests": """
import pytest
from solution import longest_consecutive


@pytest.mark.parametrize(
    "nums, expected",
    [([100, 4, 200, 1, 3, 2], 4), ([], 0), ([1, 2, 0, 1], 3)],
)
def test_examples(nums, expected):
    assert longest_consecutive(nums) == expected
""",
    },
    {
        "slug": "16-evaluate-mst-kruskal",
        "title": "MST cost (Kruskal + DSU)",
        "difficulty": "medium",
        "tags": ["union-find", "mst", "kruskal"],
        "statement": "Given `n` nodes 0..n-1 and a list of weighted edges `[u, v, w]`, return the cost of the minimum spanning tree, or -1 if the graph is disconnected.",
        "signature": "def mst_cost(n: int, edges: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| n | edges | result |
|---|---|---|
| 4 | `[[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 10]]` | 6 |""",
        "constraints": "",
        "hint": "Sort edges by weight; union; sum weights of accepted edges.",
        "starter": """
def mst_cost(n: int, edges: list[list[int]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def mst_cost(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    cost = 0
    used = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        parent[ru] = rv
        cost += w
        used += 1
        if used == n - 1:
            return cost
    return -1
""",
        "tests": """
import pytest
from solution import mst_cost


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (4, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 10]], 6),
        (3, [[0, 1, 5]], -1),
    ],
)
def test_examples(n, edges, expected):
    assert mst_cost(n, edges) == expected
""",
    },
    {
        "slug": "17-range-min-segment-tree",
        "title": "Range min query (segment tree)",
        "difficulty": "medium",
        "tags": ["segment-tree"],
        "statement": "Implement `NumArrayMin` with `update(i, val)` and `range_min(l, r)` (inclusive) in `Θ(log n)`.",
        "signature": "class NumArrayMin:\n    def __init__(self, nums: list[int]) -> None: ...\n    def update(self, i: int, val: int) -> None: ...\n    def range_min(self, l: int, r: int) -> int: ...",
        "examples_md": """## Examples

```
nm = NumArrayMin([5, 2, 6, 1, 4])
nm.range_min(0, 4)   # 1
nm.update(3, 100)
nm.range_min(0, 4)   # 2
```""",
        "constraints": "",
        "hint": "Same skeleton as range-sum but combine with `min` and use a sentinel ∞ for empty queries.",
        "starter": """
class NumArrayMin:
    def __init__(self, nums: list[int]) -> None:
        raise NotImplementedError

    def update(self, i: int, val: int) -> None:
        raise NotImplementedError

    def range_min(self, l: int, r: int) -> int:
        raise NotImplementedError
""",
        "reference": """
class NumArrayMin:
    INF = float("inf")

    def __init__(self, nums: list[int]) -> None:
        self._n = len(nums)
        self._t = [self.INF] * (4 * max(1, self._n))
        if self._n:
            self._build(1, 0, self._n - 1, nums)

    def _build(self, node, lo, hi, nums):
        if lo == hi:
            self._t[node] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, nums)
        self._build(2 * node + 1, mid + 1, hi, nums)
        self._t[node] = min(self._t[2 * node], self._t[2 * node + 1])

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def _update(self, node, lo, hi, i, val):
        if lo == hi:
            self._t[node] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node, lo, mid, i, val)
        else:
            self._update(2 * node + 1, mid + 1, hi, i, val)
        self._t[node] = min(self._t[2 * node], self._t[2 * node + 1])

    def range_min(self, l: int, r: int) -> int:
        return self._q(1, 0, self._n - 1, l, r)

    def _q(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return self.INF
        if l <= lo and hi <= r:
            return self._t[node]
        mid = (lo + hi) // 2
        return min(self._q(2 * node, lo, mid, l, r), self._q(2 * node + 1, mid + 1, hi, l, r))
""",
        "tests": """
from solution import NumArrayMin


def test_basic():
    nm = NumArrayMin([5, 2, 6, 1, 4])
    assert nm.range_min(0, 4) == 1
    nm.update(3, 100)
    assert nm.range_min(0, 4) == 2
    assert nm.range_min(0, 0) == 5
""",
    },
    {
        "slug": "18-count-of-smaller-bit",
        "title": "Count of smaller numbers after self (BIT)",
        "difficulty": "hard",
        "tags": ["fenwick-bit"],
        "statement": "Same as module 06 #18 but solve with a BIT instead of merge-sort.",
        "signature": "def count_smaller(nums: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| nums | counts |
|---|---|
| `[5, 2, 6, 1]` | `[2, 1, 1, 0]` |""",
        "constraints": "",
        "hint": "Coordinate-compress `nums` to ranks. Iterate right to left; query prefix(rank-1) then add 1 at rank.",
        "starter": """
def count_smaller(nums: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def count_smaller(nums: list[int]) -> list[int]:
    sorted_unique = sorted(set(nums))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    n = len(sorted_unique)
    bit = [0] * (n + 2)

    def update(i):
        while i <= n:
            bit[i] += 1
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    out = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        r = rank[nums[i]]
        out[i] = prefix(r - 1)
        update(r)
    return out
""",
        "tests": """
import pytest
from solution import count_smaller


@pytest.mark.parametrize(
    "nums, expected",
    [([5, 2, 6, 1], [2, 1, 1, 0]), ([-1], [0]), ([2, 0, 1], [2, 0, 0])],
)
def test_examples(nums, expected):
    assert count_smaller(nums) == expected
""",
    },
]
