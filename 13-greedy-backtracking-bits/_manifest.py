"""Module 13 manifest."""

PROBLEMS = [
    {
        "slug": "01-assign-cookies",
        "title": "Assign cookies",
        "difficulty": "easy",
        "tags": ["greedy", "sort"],
        "statement": "Children have greed factors `g`. Cookies have sizes `s`. Each child gets at most one cookie that satisfies `s[i] >= g[j]`. Return the max number of satisfied children.",
        "signature": "def find_content_children(g: list[int], s: list[int]) -> int: ...",
        "examples_md": """## Examples

| g | s | result |
|---|---|---|
| `[1, 2, 3]` | `[1, 1]` | 1 |
| `[1, 2]` | `[1, 2, 3]` | 2 |""",
        "constraints": "",
        "hint": "Sort both. Two pointers: assign smallest cookie that fits the smallest unsatisfied child.",
        "starter": "def find_content_children(g: list[int], s: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def find_content_children(g: list[int], s: list[int]) -> int:
    g = sorted(g); s = sorted(s)
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i
""",
        "tests": """
import pytest
from solution import find_content_children


@pytest.mark.parametrize(
    "g, s, expected",
    [([1, 2, 3], [1, 1], 1), ([1, 2], [1, 2, 3], 2), ([10], [1, 1, 1], 0)],
)
def test_examples(g, s, expected):
    assert find_content_children(g, s) == expected
""",
    },
    {
        "slug": "02-meeting-rooms-ii-greedy",
        "title": "Meeting rooms II (greedy + heap)",
        "difficulty": "medium",
        "tags": ["greedy", "heap"],
        "statement": "Same as module 06 #14 — included to drill the greedy/heap perspective.",
        "signature": "def min_meeting_rooms(intervals: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| intervals | rooms |
|---|---|
| `[[0, 30], [5, 10], [15, 20]]` | 2 |""",
        "constraints": "",
        "hint": "Sort by start; min-heap of end times.",
        "starter": "def min_meeting_rooms(intervals: list[list[int]]) -> int:\n    raise NotImplementedError\n",
        "reference": """
import heapq


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals = sorted(intervals)
    h: list[int] = []
    for s, e in intervals:
        if h and h[0] <= s:
            heapq.heappop(h)
        heapq.heappush(h, e)
    return len(h)
""",
        "tests": """
import pytest
from solution import min_meeting_rooms


@pytest.mark.parametrize(
    "intervals, expected",
    [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1), ([], 0)],
)
def test_examples(intervals, expected):
    assert min_meeting_rooms(intervals) == expected
""",
    },
    {
        "slug": "03-jump-game",
        "title": "Jump game",
        "difficulty": "medium",
        "tags": ["greedy"],
        "statement": "`nums[i]` is the max jump length from index i. Return True if you can reach the last index from index 0.",
        "signature": "def can_jump(nums: list[int]) -> bool: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[2, 3, 1, 1, 4]` | True |
| `[3, 2, 1, 0, 4]` | False |""",
        "constraints": "",
        "hint": "Track furthest reachable. If i > furthest, fail. Update furthest = max(furthest, i + nums[i]).",
        "starter": "def can_jump(nums: list[int]) -> bool:\n    raise NotImplementedError\n",
        "reference": """
def can_jump(nums: list[int]) -> bool:
    furthest = 0
    for i, x in enumerate(nums):
        if i > furthest:
            return False
        if i + x > furthest:
            furthest = i + x
    return True
""",
        "tests": """
import pytest
from solution import can_jump


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False), ([0], True), ([1, 0, 1], False)],
)
def test_examples(nums, expected):
    assert can_jump(nums) is expected
""",
    },
    {
        "slug": "04-jump-game-ii",
        "title": "Jump game II (min jumps)",
        "difficulty": "medium",
        "tags": ["greedy", "bfs"],
        "statement": "Same input. Return the min number of jumps to reach the last index. Assume you can always reach it.",
        "signature": "def jump(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[2, 3, 1, 1, 4]` | 2 |
| `[2, 3, 0, 1, 4]` | 2 |""",
        "constraints": "",
        "hint": "BFS-shaped greedy: maintain `current_end` and `farthest`. When `i == current_end`, increment jumps and set `current_end = farthest`.",
        "starter": "def jump(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def jump(nums: list[int]) -> int:
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        if i + nums[i] > farthest:
            farthest = i + nums[i]
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
""",
        "tests": """
import pytest
from solution import jump


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, 1, 1, 4], 2), ([2, 3, 0, 1, 4], 2), ([0], 0), ([1, 2], 1)],
)
def test_examples(nums, expected):
    assert jump(nums) == expected
""",
    },
    {
        "slug": "05-gas-station",
        "title": "Gas station",
        "difficulty": "medium",
        "tags": ["greedy"],
        "statement": "Given `gas[i]` and `cost[i]` arrays around a circle of gas stations, return the starting index that lets you complete the loop, or -1.",
        "signature": "def can_complete_circuit(gas: list[int], cost: list[int]) -> int: ...",
        "examples_md": """## Examples

| gas | cost | result |
|---|---|---|
| `[1,2,3,4,5]` | `[3,4,5,1,2]` | 3 |
| `[2,3,4]` | `[3,4,3]` | -1 |""",
        "constraints": "",
        "hint": "If total gas < total cost: -1. Otherwise the answer is the position right after the running tank dipped to its minimum.",
        "starter": "def can_complete_circuit(gas: list[int], cost: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
""",
        "tests": """
import pytest
from solution import can_complete_circuit


@pytest.mark.parametrize(
    "gas, cost, expected",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5], [4], 0),
    ],
)
def test_examples(gas, cost, expected):
    assert can_complete_circuit(gas, cost) == expected
""",
    },
    {
        "slug": "06-partition-labels",
        "title": "Partition labels",
        "difficulty": "medium",
        "tags": ["greedy", "hash-map"],
        "statement": "Given a string `s`, partition it so each letter appears in at most one part. Return the lengths of these parts.",
        "signature": "def partition_labels(s: str) -> list[int]: ...",
        "examples_md": """## Examples

| s | result |
|---|---|
| `\"ababcbacadefegdehijhklij\"` | `[9, 7, 8]` |
| `\"eccbbbbdec\"` | `[10]` |""",
        "constraints": "",
        "hint": "Map char -> last index. Walk while tracking `end = max(end, last[s[i]])`. When i == end, record length and reset start.",
        "starter": "def partition_labels(s: str) -> list[int]:\n    raise NotImplementedError\n",
        "reference": """
def partition_labels(s: str) -> list[int]:
    last = {ch: i for i, ch in enumerate(s)}
    out: list[int] = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            out.append(end - start + 1)
            start = i + 1
    return out
""",
        "tests": """
import pytest
from solution import partition_labels


@pytest.mark.parametrize(
    "s, expected",
    [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10]), ("a", [1])],
)
def test_examples(s, expected):
    assert partition_labels(s) == expected
""",
    },
    {
        "slug": "07-permutations",
        "title": "Permutations (backtracking)",
        "difficulty": "medium",
        "tags": ["backtracking"],
        "statement": "Return all permutations of an array of distinct integers.",
        "signature": "def permute(nums: list[int]) -> list[list[int]]: ...",
        "examples_md": """## Examples

| nums | count |
|---|---|
| `[1, 2, 3]` | 6 |""",
        "constraints": "",
        "hint": "Standard backtracking with `used` array.",
        "starter": "def permute(nums: list[int]) -> list[list[int]]:\n    raise NotImplementedError\n",
        "reference": """
def permute(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    used = [False] * len(nums)
    path: list[int] = []

    def _bt():
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            _bt()
            path.pop()
            used[i] = False

    _bt()
    return out
""",
        "tests": """
from solution import permute


def test_three():
    res = permute([1, 2, 3])
    assert sorted(map(tuple, res)) == sorted([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])


def test_empty():
    assert permute([]) == [[]]
""",
    },
    {
        "slug": "08-combinations",
        "title": "Combinations (backtracking)",
        "difficulty": "medium",
        "tags": ["backtracking"],
        "statement": "Return all `k`-element subsets of `{1, 2, ..., n}`.",
        "signature": "def combine(n: int, k: int) -> list[list[int]]: ...",
        "examples_md": """## Examples

| n | k | count |
|---|---|---|
| 4 | 2 | 6 |""",
        "constraints": "",
        "hint": "Backtrack with start index. Prune via `for i in range(start, n - (k - len(path)) + 2)`.",
        "starter": "def combine(n: int, k: int) -> list[list[int]]:\n    raise NotImplementedError\n",
        "reference": """
def combine(n: int, k: int) -> list[list[int]]:
    out: list[list[int]] = []
    path: list[int] = []

    def _bt(start):
        if len(path) == k:
            out.append(path[:])
            return
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            _bt(i + 1)
            path.pop()

    _bt(1)
    return out
""",
        "tests": """
from solution import combine


def test_basic():
    assert sorted(map(tuple, combine(4, 2))) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


def test_n_eq_k():
    assert combine(3, 3) == [[1, 2, 3]]
""",
    },
    {
        "slug": "09-combination-sum",
        "title": "Combination sum (unbounded reuse)",
        "difficulty": "medium",
        "tags": ["backtracking"],
        "statement": "Given distinct positive `candidates` and a `target`, return all unique combinations (each candidate may be used unlimited times) that sum to target.",
        "signature": "def combination_sum(candidates: list[int], target: int) -> list[list[int]]: ...",
        "examples_md": """## Examples

| candidates | target | result |
|---|---|---|
| `[2, 3, 6, 7]` | 7 | `[[2, 2, 3], [7]]` |""",
        "constraints": "",
        "hint": "Backtrack with start index (don't go back). Avoid duplicates by always advancing or staying at start.",
        "starter": "def combination_sum(candidates: list[int], target: int) -> list[list[int]]:\n    raise NotImplementedError\n",
        "reference": """
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    candidates = sorted(candidates)
    out: list[list[int]] = []
    path: list[int] = []

    def _bt(start, remaining):
        if remaining == 0:
            out.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break
            path.append(c)
            _bt(i, remaining - c)
            path.pop()

    _bt(0, target)
    return out
""",
        "tests": """
from solution import combination_sum


def test_basic():
    res = combination_sum([2, 3, 6, 7], 7)
    assert sorted(map(tuple, res)) == sorted([(2, 2, 3), (7,)])


def test_no_solution():
    assert combination_sum([2, 4], 7) == []
""",
    },
    {
        "slug": "10-n-queens",
        "title": "N-queens",
        "difficulty": "hard",
        "tags": ["backtracking", "constraint-satisfaction"],
        "statement": "Return all valid N-queens board configurations as a list of lists of strings (rows).",
        "signature": "def solve_n_queens(n: int) -> list[list[str]]: ...",
        "examples_md": """## Examples

| n | result count |
|---|---|
| 4 | 2 |
| 1 | 1 |""",
        "constraints": "",
        "hint": "Place row by row. Track 3 sets: occupied columns, occupied diagonals (`r - c`), occupied anti-diagonals (`r + c`).",
        "starter": "def solve_n_queens(n: int) -> list[list[str]]:\n    raise NotImplementedError\n",
        "reference": """
def solve_n_queens(n: int) -> list[list[str]]:
    out: list[list[str]] = []
    cols: set[int] = set()
    diag1: set[int] = set()
    diag2: set[int] = set()
    placement: list[int] = []

    def _bt(r):
        if r == n:
            board = []
            for col in placement:
                row = ["."] * n
                row[col] = "Q"
                board.append("".join(row))
            out.append(board)
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            cols.add(c); diag1.add(r - c); diag2.add(r + c); placement.append(c)
            _bt(r + 1)
            cols.remove(c); diag1.remove(r - c); diag2.remove(r + c); placement.pop()

    _bt(0)
    return out
""",
        "tests": """
import pytest
from solution import solve_n_queens


def test_n4():
    res = solve_n_queens(4)
    assert len(res) == 2
    assert all(len(b) == 4 and all(len(r) == 4 for r in b) for b in res)


def test_n1():
    assert solve_n_queens(1) == [["Q"]]
""",
    },
    {
        "slug": "11-sudoku-solver",
        "title": "Sudoku solver",
        "difficulty": "hard",
        "tags": ["backtracking", "constraint-satisfaction"],
        "statement": "Solve a 9x9 Sudoku in place. Empty cells are `'.'`.",
        "signature": "def solve_sudoku(board: list[list[str]]) -> None: ...",
        "examples_md": """## Examples

Standard 9x9 sudoku grid; modify in place to a valid solution.""",
        "constraints": "",
        "hint": "Backtrack cell by cell. Maintain row/col/box sets of used digits for O(1) check.",
        "starter": "def solve_sudoku(board: list[list[str]]) -> None:\n    raise NotImplementedError\n",
        "reference": """
def solve_sudoku(board: list[list[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties: list[tuple[int, int]] = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.':
                empties.append((r, c))
            else:
                rows[r].add(v); cols[c].add(v); boxes[(r // 3) * 3 + c // 3].add(v)

    def _bt(idx):
        if idx == len(empties):
            return True
        r, c = empties[idx]
        b = (r // 3) * 3 + c // 3
        for d in '123456789':
            if d in rows[r] or d in cols[c] or d in boxes[b]:
                continue
            board[r][c] = d
            rows[r].add(d); cols[c].add(d); boxes[b].add(d)
            if _bt(idx + 1):
                return True
            rows[r].remove(d); cols[c].remove(d); boxes[b].remove(d)
        board[r][c] = '.'
        return False

    _bt(0)
""",
        "tests": """
from solution import solve_sudoku


def test_simple():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solve_sudoku(board)
    for row in board:
        assert sorted(row) == list("123456789")
    for c in range(9):
        col = [board[r][c] for r in range(9)]
        assert sorted(col) == list("123456789")
""",
    },
    {
        "slug": "12-word-search",
        "title": "Word search",
        "difficulty": "medium",
        "tags": ["backtracking", "grid"],
        "statement": "Given a 2D board of letters and a word, return True if the word can be formed by 4-directionally adjacent cells (each cell used at most once).",
        "signature": "def exist(board: list[list[str]], word: str) -> bool: ...",
        "examples_md": """## Examples

```
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = \"ABCCED\"   -> True
word = \"SEE\"     -> True
word = \"ABCB\"    -> False
```""",
        "constraints": "",
        "hint": "DFS with visited mark; restore on backtrack.",
        "starter": "def exist(board: list[list[str]], word: str) -> bool:\n    raise NotImplementedError\n",
        "reference": """
def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def _dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False
        ch = board[i][j]
        board[i][j] = '#'
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if _dfs(i + di, j + dj, k + 1):
                board[i][j] = ch
                return True
        board[i][j] = ch
        return False

    for i in range(m):
        for j in range(n):
            if _dfs(i, j, 0):
                return True
    return False
""",
        "tests": """
import pytest
from solution import exist


board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]


@pytest.mark.parametrize(
    "word, expected",
    [("ABCCED", True), ("SEE", True), ("ABCB", False)],
)
def test_examples(word, expected):
    assert exist([row[:] for row in board], word) is expected
""",
    },
    {
        "slug": "13-single-number",
        "title": "Single number (XOR)",
        "difficulty": "easy",
        "tags": ["bit-manipulation"],
        "statement": "Every element appears twice except one. Return that one. `Θ(n)` time, `Θ(1)` space.",
        "signature": "def single_number(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[2, 2, 1]` | 1 |
| `[4, 1, 2, 1, 2]` | 4 |""",
        "constraints": "",
        "hint": "XOR all elements. Pairs cancel.",
        "starter": "def single_number(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def single_number(nums: list[int]) -> int:
    out = 0
    for x in nums:
        out ^= x
    return out
""",
        "tests": """
import pytest
from solution import single_number


@pytest.mark.parametrize("nums, expected", [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([7], 7)])
def test_examples(nums, expected):
    assert single_number(nums) == expected
""",
    },
    {
        "slug": "14-single-number-ii",
        "title": "Single number II (every element appears 3 times except one)",
        "difficulty": "medium",
        "tags": ["bit-manipulation"],
        "statement": "Same setup as #13 but every element appears EXACTLY THREE times except for one element that appears once. Return the loner. `Θ(n)` time, `Θ(1)` space.",
        "signature": "def single_number_ii(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[2, 2, 3, 2]` | 3 |
| `[0, 1, 0, 1, 0, 1, 99]` | 99 |""",
        "constraints": "",
        "hint": "For each bit position 0..31, count occurrences mod 3 across all elements. Bits with count mod 3 == 1 belong to the loner.",
        "starter": "def single_number_ii(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def single_number_ii(nums: list[int]) -> int:
    out = 0
    for b in range(32):
        cnt = sum((x >> b) & 1 for x in nums)
        if cnt % 3:
            out |= 1 << b
    if out >= 1 << 31:  # interpret as signed 32-bit
        out -= 1 << 32
    return out
""",
        "tests": """
import pytest
from solution import single_number_ii


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 2, 3, 2], 3), ([0, 1, 0, 1, 0, 1, 99], 99), ([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2], -4)],
)
def test_examples(nums, expected):
    assert single_number_ii(nums) == expected
""",
    },
    {
        "slug": "15-counting-bits",
        "title": "Counting bits",
        "difficulty": "easy",
        "tags": ["bit-manipulation", "dp"],
        "statement": "For `n >= 0`, return an array `out[i]` for `i in [0, n]` where `out[i]` is the number of set bits in `i`. Solve in `Θ(n)`.",
        "signature": "def count_bits(n: int) -> list[int]: ...",
        "examples_md": """## Examples

| n | result |
|---|---|
| 5 | `[0, 1, 1, 2, 1, 2]` |
| 2 | `[0, 1, 1]` |""",
        "constraints": "",
        "hint": "`dp[i] = dp[i >> 1] + (i & 1)`.",
        "starter": "def count_bits(n: int) -> list[int]:\n    raise NotImplementedError\n",
        "reference": """
def count_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
""",
        "tests": """
import pytest
from solution import count_bits


@pytest.mark.parametrize("n, expected", [(5, [0, 1, 1, 2, 1, 2]), (2, [0, 1, 1]), (0, [0])])
def test_examples(n, expected):
    assert count_bits(n) == expected
""",
    },
    {
        "slug": "16-missing-number-xor",
        "title": "Missing number (XOR)",
        "difficulty": "easy",
        "tags": ["bit-manipulation"],
        "statement": "Given `nums` containing `n` distinct numbers from `[0, n]`, return the one missing.",
        "signature": "def missing_number(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[3, 0, 1]` | 2 |
| `[0, 1]` | 2 |
| `[9, 6, 4, 2, 3, 5, 7, 0, 1]` | 8 |""",
        "constraints": "",
        "hint": "XOR all values in `nums` and all integers in `[0, n]`. Pairs cancel; the missing one survives.",
        "starter": "def missing_number(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def missing_number(nums: list[int]) -> int:
    out = len(nums)
    for i, x in enumerate(nums):
        out ^= i ^ x
    return out
""",
        "tests": """
import pytest
from solution import missing_number


@pytest.mark.parametrize(
    "nums, expected",
    [([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8), ([0], 1)],
)
def test_examples(nums, expected):
    assert missing_number(nums) == expected
""",
    },
    {
        "slug": "17-find-duplicate-number",
        "title": "Find the duplicate number (Floyd cycle)",
        "difficulty": "medium",
        "tags": ["fast-slow-pointer", "graph"],
        "statement": "Given an array of `n + 1` integers each in `[1, n]` with exactly one repeated value, find the duplicate. `Θ(n)` time, `Θ(1)` extra space (don't modify input).",
        "signature": "def find_duplicate(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[1, 3, 4, 2, 2]` | 2 |
| `[3, 1, 3, 4, 2]` | 3 |""",
        "constraints": "",
        "hint": "Treat `nums[i]` as a pointer. There's a cycle. Floyd's tortoise/hare; the cycle entrance is the duplicate.",
        "starter": "def find_duplicate(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def find_duplicate(nums: list[int]) -> int:
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    p = nums[0]
    while p != slow:
        p = nums[p]
        slow = nums[slow]
    return p
""",
        "tests": """
import pytest
from solution import find_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3), ([1, 1], 1), ([1, 1, 2], 1)],
)
def test_examples(nums, expected):
    assert find_duplicate(nums) == expected
""",
    },
    {
        "slug": "18-sum-of-two-integers",
        "title": "Sum of two integers without + or -",
        "difficulty": "medium",
        "tags": ["bit-manipulation"],
        "statement": "Compute the sum of two integers `a + b` without using `+` or `-`.",
        "signature": "def get_sum(a: int, b: int) -> int: ...",
        "examples_md": """## Examples

| a | b | result |
|---|---|---|
| 1 | 2 | 3 |
| -1 | 1 | 0 |
| -2 | 3 | 1 |""",
        "constraints": "",
        "hint": "Carry-add via bitwise: `sum_no_carry = a ^ b`, `carry = (a & b) << 1`. Loop until carry == 0. Mask to 32 bits and reinterpret negatives because Python ints are unbounded.",
        "starter": "def get_sum(a: int, b: int) -> int:\n    raise NotImplementedError\n",
        "reference": """
def get_sum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a < 0x80000000 else a - 0x100000000
""",
        "tests": """
import pytest
from solution import get_sum


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (-1, 1, 0), (-2, 3, 1), (0, 0, 0), (5, 5, 10)])
def test_examples(a, b, expected):
    assert get_sum(a, b) == expected
""",
    },
]
