"""Module 12 (DP) manifest."""

PROBLEMS = [
    {
        "slug": "01-fib-dp",
        "title": "Fibonacci (DP)",
        "difficulty": "easy",
        "tags": ["1d-dp"],
        "statement": "Bottom-up Fibonacci.",
        "signature": "def fib(n: int) -> int: ...",
        "examples_md": """## Examples

| n | fib |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 10 | 55 |""",
        "constraints": "",
        "hint": "Iterate from 2 to n.",
        "starter": "def fib(n: int) -> int:\n    raise NotImplementedError\n",
        "reference": """
def fib(n: int) -> int:
    \"\"\"Time: Θ(n).  Space: Θ(1).\"\"\"
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
""",
        "tests": """
import pytest
from solution import fib


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (10, 55), (30, 832040)])
def test_examples(n, expected):
    assert fib(n) == expected
""",
    },
    {
        "slug": "02-climbing-stairs",
        "title": "Climbing stairs",
        "difficulty": "easy",
        "tags": ["1d-dp"],
        "statement": "Each step you can climb 1 or 2 stairs. Return the number of distinct ways to reach the top of `n` stairs.",
        "signature": "def climb_stairs(n: int) -> int: ...",
        "examples_md": """## Examples

| n | ways |
|---|---|
| 2 | 2 |
| 3 | 3 |
| 5 | 8 |""",
        "constraints": "",
        "hint": "Same recurrence as Fibonacci shifted by one.",
        "starter": "def climb_stairs(n: int) -> int:\n    raise NotImplementedError\n",
        "reference": """
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
""",
        "tests": """
import pytest
from solution import climb_stairs


@pytest.mark.parametrize("n, expected", [(1, 1), (2, 2), (3, 3), (5, 8), (10, 89)])
def test_examples(n, expected):
    assert climb_stairs(n) == expected
""",
    },
    {
        "slug": "03-min-cost-climbing-stairs",
        "title": "Min cost climbing stairs",
        "difficulty": "easy",
        "tags": ["1d-dp"],
        "statement": "`cost[i]` is the cost to step on stair i. Once paid, you can step 1 or 2 stairs further. You can start at index 0 or 1. Return the min cost to reach past the last stair.",
        "signature": "def min_cost_climbing_stairs(cost: list[int]) -> int: ...",
        "examples_md": """## Examples

| cost | result |
|---|---|
| `[10, 15, 20]` | 15 |
| `[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]` | 6 |""",
        "constraints": "",
        "hint": "`dp[i] = cost[i] + min(dp[i-1], dp[i-2])`. Final answer is `min(dp[n-1], dp[n-2])`.",
        "starter": "def min_cost_climbing_stairs(cost: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def min_cost_climbing_stairs(cost: list[int]) -> int:
    a = b = 0
    for i in range(2, len(cost) + 1):
        cur = min(b + cost[i - 1], a + cost[i - 2])
        a, b = b, cur
    return b
""",
        "tests": """
import pytest
from solution import min_cost_climbing_stairs


@pytest.mark.parametrize(
    "cost, expected",
    [([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)],
)
def test_examples(cost, expected):
    assert min_cost_climbing_stairs(cost) == expected
""",
    },
    {
        "slug": "04-house-robber",
        "title": "House robber",
        "difficulty": "medium",
        "tags": ["1d-dp"],
        "statement": "You cannot rob two adjacent houses. Return the max amount you can rob from a row of houses.",
        "signature": "def rob(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[1, 2, 3, 1]` | 4 |
| `[2, 7, 9, 3, 1]` | 12 |""",
        "constraints": "",
        "hint": "`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. O(1) space rolling.",
        "starter": "def rob(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def rob(nums: list[int]) -> int:
    prev = curr = 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr
""",
        "tests": """
import pytest
from solution import rob


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12), ([], 0), ([5], 5)],
)
def test_examples(nums, expected):
    assert rob(nums) == expected
""",
    },
    {
        "slug": "05-house-robber-ii",
        "title": "House robber II (circular)",
        "difficulty": "medium",
        "tags": ["1d-dp"],
        "statement": "Same as house-robber but houses form a circle (first and last are adjacent).",
        "signature": "def rob_circular(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[2, 3, 2]` | 3 |
| `[1, 2, 3, 1]` | 4 |""",
        "constraints": "",
        "hint": "Two passes: rob houses [0..n-2] and [1..n-1]; max of the two.",
        "starter": "def rob_circular(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def rob_circular(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def _rob(arr):
        prev = curr = 0
        for x in arr:
            prev, curr = curr, max(curr, prev + x)
        return curr

    return max(_rob(nums[:-1]), _rob(nums[1:]))
""",
        "tests": """
import pytest
from solution import rob_circular


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, 2], 3), ([1, 2, 3, 1], 4), ([5], 5), ([1, 2, 3], 3)],
)
def test_examples(nums, expected):
    assert rob_circular(nums) == expected
""",
    },
    {
        "slug": "06-coin-change",
        "title": "Coin change (min coins)",
        "difficulty": "medium",
        "tags": ["1d-dp", "unbounded-knapsack"],
        "statement": "Given coin denominations and an amount, return the fewest coins needed to make the amount, or -1 if impossible.",
        "signature": "def coin_change(coins: list[int], amount: int) -> int: ...",
        "examples_md": """## Examples

| coins | amount | result |
|---|---|---|
| `[1, 2, 5]` | 11 | 3 |
| `[2]` | 3 | -1 |
| `[1]` | 0 | 0 |""",
        "constraints": "",
        "hint": "`dp[a] = min(dp[a - c] + 1)` over coins `c <= a`. Initialize dp[0] = 0, others ∞.",
        "starter": "def coin_change(coins: list[int], amount: int) -> int:\n    raise NotImplementedError\n",
        "reference": """
def coin_change(coins: list[int], amount: int) -> int:
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return -1 if dp[amount] == INF else dp[amount]
""",
        "tests": """
import pytest
from solution import coin_change


@pytest.mark.parametrize(
    "coins, amount, expected",
    [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0), ([1, 4, 5], 7, 2)],
)
def test_examples(coins, amount, expected):
    assert coin_change(coins, amount) == expected
""",
    },
    {
        "slug": "07-coin-change-ii",
        "title": "Coin change II (count combinations)",
        "difficulty": "medium",
        "tags": ["1d-dp", "unbounded-knapsack"],
        "statement": "Return the number of distinct combinations of coins that sum to `amount`.",
        "signature": "def coin_change_count(amount: int, coins: list[int]) -> int: ...",
        "examples_md": """## Examples

| amount | coins | result |
|---|---|---|
| 5 | `[1, 2, 5]` | 4 |
| 3 | `[2]` | 0 |
| 10 | `[10]` | 1 |""",
        "constraints": "",
        "hint": "`dp[a] += dp[a - c]`. Outer loop over coins (not amounts) to avoid double-counting orderings.",
        "starter": "def coin_change_count(amount: int, coins: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def coin_change_count(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
""",
        "tests": """
import pytest
from solution import coin_change_count


@pytest.mark.parametrize(
    "amount, coins, expected",
    [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1), (0, [], 1)],
)
def test_examples(amount, coins, expected):
    assert coin_change_count(amount, coins) == expected
""",
    },
    {
        "slug": "08-longest-increasing-subsequence",
        "title": "Longest increasing subsequence",
        "difficulty": "medium",
        "tags": ["1d-dp", "binary-search"],
        "statement": "Return the length of the longest strictly increasing subsequence of `nums`. Solve in `Θ(n log n)`.",
        "signature": "def length_of_lis(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[10, 9, 2, 5, 3, 7, 101, 18]` | 4 |
| `[0, 1, 0, 3, 2, 3]` | 4 |
| `[7, 7, 7, 7]` | 1 |""",
        "constraints": "",
        "hint": "Patience sorting: maintain `tails` array; for each x, replace `tails[bisect_left(tails, x)]` (or append).",
        "starter": "def length_of_lis(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
from bisect import bisect_left


def length_of_lis(nums: list[int]) -> int:
    tails: list[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
""",
        "tests": """
import pytest
from solution import length_of_lis


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([], 0),
    ],
)
def test_examples(nums, expected):
    assert length_of_lis(nums) == expected
""",
    },
    {
        "slug": "09-longest-common-subsequence",
        "title": "Longest common subsequence",
        "difficulty": "medium",
        "tags": ["2d-dp"],
        "statement": "Return the length of the longest common subsequence of two strings.",
        "signature": "def lcs(s: str, t: str) -> int: ...",
        "examples_md": """## Examples

| s | t | result |
|---|---|---|
| `\"abcde\"` | `\"ace\"` | 3 |
| `\"abc\"` | `\"abc\"` | 3 |
| `\"abc\"` | `\"def\"` | 0 |""",
        "constraints": "",
        "hint": "`dp[i][j] = dp[i-1][j-1] + 1` if `s[i-1] == t[j-1]` else `max(dp[i-1][j], dp[i][j-1])`.",
        "starter": "def lcs(s: str, t: str) -> int:\n    raise NotImplementedError\n",
        "reference": """
def lcs(s: str, t: str) -> int:
    n, m = len(s), len(t)
    prev = [0] * (m + 1)
    cur = [0] * (m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev, cur = cur, prev
    return prev[m]
""",
        "tests": """
import pytest
from solution import lcs


@pytest.mark.parametrize(
    "s, t, expected",
    [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0), ("", "abc", 0)],
)
def test_examples(s, t, expected):
    assert lcs(s, t) == expected
""",
    },
    {
        "slug": "10-edit-distance",
        "title": "Edit distance (Levenshtein)",
        "difficulty": "hard",
        "tags": ["2d-dp"],
        "statement": "Return the minimum number of single-character insertions, deletions, or substitutions to transform `s` into `t`.",
        "signature": "def min_distance(s: str, t: str) -> int: ...",
        "examples_md": """## Examples

| s | t | result |
|---|---|---|
| `\"horse\"` | `\"ros\"` | 3 |
| `\"intention\"` | `\"execution\"` | 5 |""",
        "constraints": "",
        "hint": "Standard 2D DP. Space-optimize to one row.",
        "starter": "def min_distance(s: str, t: str) -> int:\n    raise NotImplementedError\n",
        "reference": """
def min_distance(s: str, t: str) -> int:
    if len(s) < len(t):
        s, t = t, s
    prev = list(range(len(t) + 1))
    cur = [0] * (len(t) + 1)
    for i, sc in enumerate(s, start=1):
        cur[0] = i
        for j, tc in enumerate(t, start=1):
            if sc == tc:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev, cur = cur, prev
    return prev[len(t)]
""",
        "tests": """
import pytest
from solution import min_distance


@pytest.mark.parametrize(
    "s, t, expected",
    [("horse", "ros", 3), ("intention", "execution", 5), ("", "abc", 3), ("same", "same", 0)],
)
def test_examples(s, t, expected):
    assert min_distance(s, t) == expected
""",
    },
    {
        "slug": "11-word-break-dp",
        "title": "Word break (DP)",
        "difficulty": "medium",
        "tags": ["1d-dp"],
        "statement": "Same as module 10 #12 — included again to drill the DP perspective.",
        "signature": "def word_break(s: str, word_dict: list[str]) -> bool: ...",
        "examples_md": """## Examples

| s | word_dict | result |
|---|---|---|
| `\"leetcode\"` | `[\"leet\",\"code\"]` | True |""",
        "constraints": "",
        "hint": "`dp[i]` True iff `s[:i]` is segmentable.",
        "starter": "def word_break(s: str, word_dict: list[str]) -> bool:\n    raise NotImplementedError\n",
        "reference": """
def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
""",
        "tests": """
import pytest
from solution import word_break


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
def test_examples(s, words, expected):
    assert word_break(s, words) is expected
""",
    },
    {
        "slug": "12-unique-paths",
        "title": "Unique paths in grid",
        "difficulty": "medium",
        "tags": ["2d-dp"],
        "statement": "Robot at top-left of an `m x n` grid moves right or down. Return number of unique paths to bottom-right.",
        "signature": "def unique_paths(m: int, n: int) -> int: ...",
        "examples_md": """## Examples

| m | n | result |
|---|---|---|
| 3 | 7 | 28 |
| 3 | 2 | 3 |
| 1 | 1 | 1 |""",
        "constraints": "",
        "hint": "`dp[i][j] = dp[i-1][j] + dp[i][j-1]`, with first row and column = 1.",
        "starter": "def unique_paths(m: int, n: int) -> int:\n    raise NotImplementedError\n",
        "reference": """
def unique_paths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
""",
        "tests": """
import pytest
from solution import unique_paths


@pytest.mark.parametrize("m, n, expected", [(3, 7, 28), (3, 2, 3), (1, 1, 1)])
def test_examples(m, n, expected):
    assert unique_paths(m, n) == expected
""",
    },
    {
        "slug": "13-unique-paths-ii",
        "title": "Unique paths II (with obstacles)",
        "difficulty": "medium",
        "tags": ["2d-dp"],
        "statement": "Same as #12 but `grid[i][j] == 1` is an obstacle.",
        "signature": "def unique_paths_with_obstacles(grid: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| grid | result |
|---|---|
| `[[0,0,0],[0,1,0],[0,0,0]]` | 2 |
| `[[0,1],[0,0]]` | 1 |""",
        "constraints": "",
        "hint": "If `grid[i][j] == 1`, set `dp[i][j] = 0`.",
        "starter": "def unique_paths_with_obstacles(grid: list[list[int]]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    if not grid or grid[0][0] == 1:
        return 0
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
    return dp[-1]
""",
        "tests": """
import pytest
from solution import unique_paths_with_obstacles


@pytest.mark.parametrize(
    "grid, expected",
    [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2), ([[0, 1], [0, 0]], 1), ([[1]], 0)],
)
def test_examples(grid, expected):
    assert unique_paths_with_obstacles(grid) == expected
""",
    },
    {
        "slug": "14-partition-equal-subset-sum",
        "title": "Partition equal subset sum",
        "difficulty": "medium",
        "tags": ["knapsack"],
        "statement": "Return True if `nums` can be partitioned into two subsets with equal sum.",
        "signature": "def can_partition(nums: list[int]) -> bool: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[1, 5, 11, 5]` | True |
| `[1, 2, 3, 5]` | False |""",
        "constraints": "",
        "hint": "0/1 knapsack: can we hit subset sum = total/2.",
        "starter": "def can_partition(nums: list[int]) -> bool:\n    raise NotImplementedError\n",
        "reference": """
def can_partition(nums: list[int]) -> bool:
    s = sum(nums)
    if s % 2:
        return False
    target = s // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for w in range(target, x - 1, -1):
            dp[w] = dp[w] or dp[w - x]
    return dp[target]
""",
        "tests": """
import pytest
from solution import can_partition


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 5, 11, 5], True), ([1, 2, 3, 5], False), ([2, 2], True), ([1], False)],
)
def test_examples(nums, expected):
    assert can_partition(nums) is expected
""",
    },
    {
        "slug": "15-knapsack-01",
        "title": "0/1 knapsack",
        "difficulty": "medium",
        "tags": ["knapsack"],
        "statement": "Given `weights`, `values`, and `capacity`, return the max value subset of items (each item at most once) with total weight ≤ capacity.",
        "signature": "def knapsack(weights: list[int], values: list[int], capacity: int) -> int: ...",
        "examples_md": """## Examples

| weights | values | capacity | result |
|---|---|---|---|
| `[2, 3, 4, 5]` | `[3, 4, 5, 6]` | 5 | 7 |
| `[1, 2, 3]` | `[6, 10, 12]` | 5 | 22 |""",
        "constraints": "",
        "hint": "1D DP: outer loop items, inner loop capacity DESCENDING.",
        "starter": "def knapsack(weights: list[int], values: list[int], capacity: int) -> int:\n    raise NotImplementedError\n",
        "reference": """
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            if dp[c - w] + v > dp[c]:
                dp[c] = dp[c - w] + v
    return dp[capacity]
""",
        "tests": """
import pytest
from solution import knapsack


@pytest.mark.parametrize(
    "weights, values, cap, expected",
    [([2, 3, 4, 5], [3, 4, 5, 6], 5, 7), ([1, 2, 3], [6, 10, 12], 5, 22)],
)
def test_examples(weights, values, cap, expected):
    assert knapsack(weights, values, cap) == expected
""",
    },
    {
        "slug": "16-maximum-product-subarray",
        "title": "Maximum product subarray",
        "difficulty": "medium",
        "tags": ["1d-dp"],
        "statement": "Return the largest product of any contiguous subarray.",
        "signature": "def max_product(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[2, 3, -2, 4]` | 6 |
| `[-2, 0, -1]` | 0 |
| `[-2, 3, -4]` | 24 |""",
        "constraints": "",
        "hint": "Track both running max AND running min ending at i (a negative * negative_min becomes large positive).",
        "starter": "def max_product(nums: list[int]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def max_product(nums: list[int]) -> int:
    best = lo = hi = nums[0]
    for x in nums[1:]:
        candidates = (x, hi * x, lo * x)
        hi = max(candidates)
        lo = min(candidates)
        if hi > best:
            best = hi
    return best
""",
        "tests": """
import pytest
from solution import max_product


@pytest.mark.parametrize(
    "nums, expected",
    [([2, 3, -2, 4], 6), ([-2, 0, -1], 0), ([-2, 3, -4], 24), ([0, 2], 2)],
)
def test_examples(nums, expected):
    assert max_product(nums) == expected
""",
    },
    {
        "slug": "17-tsp-bitmask",
        "title": "Travelling salesman (bitmask DP)",
        "difficulty": "hard",
        "tags": ["bitmask-dp"],
        "statement": "Given an `n x n` distance matrix (n ≤ 15), return the cost of the shortest tour visiting each city exactly once starting and ending at city 0.",
        "signature": "def tsp(dist: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

```
dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
result = 80
```""",
        "constraints": "- `1 <= n <= 15`",
        "hint": "`dp[mask][i]` = min cost ending at city i having visited exactly the cities in mask. Transition: `dp[mask | 1<<j][j] = dp[mask][i] + dist[i][j]`.",
        "starter": "def tsp(dist: list[list[int]]) -> int:\n    raise NotImplementedError\n",
        "reference": """
def tsp(dist: list[list[int]]) -> int:
    n = len(dist)
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1, 1 << n):
        if not (mask & 1):
            continue
        for i in range(n):
            if not (mask >> i) & 1:
                continue
            cur = dp[mask][i]
            if cur == INF:
                continue
            for j in range(n):
                if (mask >> j) & 1 or i == j:
                    continue
                new_mask = mask | (1 << j)
                if cur + dist[i][j] < dp[new_mask][j]:
                    dp[new_mask][j] = cur + dist[i][j]
    full = (1 << n) - 1
    return int(min(dp[full][i] + dist[i][0] for i in range(1, n)))
""",
        "tests": """
import pytest
from solution import tsp


def test_basic():
    dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    assert tsp(dist) == 80


def test_two_cities():
    assert tsp([[0, 5], [5, 0]]) == 10
""",
    },
    {
        "slug": "18-distinct-subsequences",
        "title": "Distinct subsequences",
        "difficulty": "hard",
        "tags": ["2d-dp"],
        "statement": "Given strings `s` and `t`, return the number of distinct subsequences of `s` that equal `t`.",
        "signature": "def num_distinct(s: str, t: str) -> int: ...",
        "examples_md": """## Examples

| s | t | result |
|---|---|---|
| `\"rabbbit\"` | `\"rabbit\"` | 3 |
| `\"babgbag\"` | `\"bag\"` | 5 |""",
        "constraints": "",
        "hint": "`dp[i][j]` = number of subsequences of `s[:i]` equal to `t[:j]`. If `s[i-1] == t[j-1]`: `dp[i-1][j-1] + dp[i-1][j]`; else `dp[i-1][j]`.",
        "starter": "def num_distinct(s: str, t: str) -> int:\n    raise NotImplementedError\n",
        "reference": """
def num_distinct(s: str, t: str) -> int:
    n, m = len(s), len(t)
    if m > n:
        return 0
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, m), 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[m]
""",
        "tests": """
import pytest
from solution import num_distinct


@pytest.mark.parametrize(
    "s, t, expected",
    [("rabbbit", "rabbit", 3), ("babgbag", "bag", 5), ("a", "", 1), ("", "a", 0)],
)
def test_examples(s, t, expected):
    assert num_distinct(s, t) == expected
""",
    },
]
