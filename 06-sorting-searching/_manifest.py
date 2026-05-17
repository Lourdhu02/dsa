"""Module 06 (sorting & searching) manifest."""

PROBLEMS = [
    {
        "slug": "01-binary-search",
        "title": "Binary search",
        "difficulty": "easy",
        "tags": ["binary-search"],
        "statement": "Given a sorted array of distinct integers and a target, return the index of target or -1.",
        "signature": "def search(nums: list[int], target: int) -> int: ...",
        "examples_md": """## Examples

| nums | target | result |
|---|---|---|
| `[-1, 0, 3, 5, 9, 12]` | 9 | 4 |
| `[-1, 0, 3, 5, 9, 12]` | 2 | -1 |""",
        "constraints": "- `0 <= len(nums) <= 10^4`",
        "hint": "Standard closed-interval binary search. Pick one variant and stick to it.",
        "starter": """
def search(nums: list[int], target: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""",
        "tests": """
import pytest
from solution import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [([-1, 0, 3, 5, 9, 12], 9, 4), ([-1, 0, 3, 5, 9, 12], 2, -1), ([], 1, -1), ([1], 1, 0)],
)
def test_examples(nums, target, expected):
    assert search(nums, target) == expected
""",
    },
    {
        "slug": "02-first-bad-version",
        "title": "First bad version",
        "difficulty": "easy",
        "tags": ["binary-search"],
        "statement": "You have `n` versions [1, n]. There exists a smallest version `k` such that all versions `>= k` are bad. Find `k` using as few `is_bad(v)` calls as possible. `is_bad` is supplied as an argument here (it is supplied by an API in the real LeetCode problem).",
        "signature": "def first_bad_version(n: int, is_bad: Callable[[int], bool]) -> int: ...",
        "examples_md": """## Examples

```
n=5, is_bad: 4 and 5 are bad, others are good
result: 4
```""",
        "constraints": "",
        "hint": "Binary search for the smallest k with is_bad(k) True. Use the half-open invariant `[lo, hi)`.",
        "starter": """
from typing import Callable


def first_bad_version(n: int, is_bad: Callable[[int], bool]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from typing import Callable


def first_bad_version(n: int, is_bad: Callable[[int], bool]) -> int:
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
""",
        "tests": """
import pytest

from solution import first_bad_version


@pytest.mark.parametrize(
    "n, first_bad",
    [(5, 4), (1, 1), (10, 7), (100, 50)],
)
def test_finds_first_bad(n, first_bad):
    assert first_bad_version(n, lambda v: v >= first_bad) == first_bad
""",
    },
    {
        "slug": "03-search-insert-position",
        "title": "Search insert position",
        "difficulty": "easy",
        "tags": ["binary-search"],
        "statement": "Given a sorted array of distinct integers and a target, return the index where the target would be inserted to keep the array sorted.",
        "signature": "def search_insert(nums: list[int], target: int) -> int: ...",
        "examples_md": """## Examples

| nums | target | result |
|---|---|---|
| `[1, 3, 5, 6]` | 5 | 2 |
| `[1, 3, 5, 6]` | 2 | 1 |
| `[1, 3, 5, 6]` | 7 | 4 |""",
        "constraints": "",
        "hint": "Lower bound: smallest index with `nums[i] >= target`.",
        "starter": """
def search_insert(nums: list[int], target: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
""",
        "tests": """
import pytest
from solution import search_insert


@pytest.mark.parametrize(
    "nums, target, expected",
    [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4), ([], 5, 0)],
)
def test_examples(nums, target, expected):
    assert search_insert(nums, target) == expected
""",
    },
    {
        "slug": "04-find-first-last-position",
        "title": "Find first and last position",
        "difficulty": "medium",
        "tags": ["binary-search"],
        "statement": "Given a sorted array (with duplicates) and target, return `[first, last]` of target. `[-1, -1]` if absent.",
        "signature": "def search_range(nums: list[int], target: int) -> list[int]: ...",
        "examples_md": """## Examples

| nums | target | result |
|---|---|---|
| `[5, 7, 7, 8, 8, 10]` | 8 | `[3, 4]` |
| `[5, 7, 7, 8, 8, 10]` | 6 | `[-1, -1]` |
| `[]` | 0 | `[-1, -1]` |""",
        "constraints": "",
        "hint": "Two binary searches: lower_bound(target) and upper_bound(target) - 1.",
        "starter": """
def search_range(nums: list[int], target: int) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def search_range(nums: list[int], target: int) -> list[int]:
    def lb(t):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    left = lb(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = lb(target + 1) - 1
    return [left, right]
""",
        "tests": """
import pytest
from solution import search_range


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2], 2, [0, 1]),
    ],
)
def test_examples(nums, target, expected):
    assert search_range(nums, target) == expected
""",
    },
    {
        "slug": "05-find-peak-element",
        "title": "Find peak element",
        "difficulty": "medium",
        "tags": ["binary-search"],
        "statement": "A peak is strictly greater than its neighbors. Find any peak index in `Θ(log n)`. Assume `nums[-1] = nums[n] = -inf`.",
        "signature": "def find_peak(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | possible result |
|---|---|
| `[1, 2, 3, 1]` | 2 |
| `[1, 2, 1, 3, 5, 6, 4]` | 1 or 5 |""",
        "constraints": "",
        "hint": "Compare `nums[mid]` to `nums[mid+1]`. If smaller, peak is in `[mid+1, hi]`; else in `[lo, mid]`. The slope must change since the boundaries are -inf.",
        "starter": """
def find_peak(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_peak(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
""",
        "tests": """
from solution import find_peak


def _is_peak(nums, i):
    n = len(nums)
    left = nums[i - 1] if i - 1 >= 0 else float("-inf")
    right = nums[i + 1] if i + 1 < n else float("-inf")
    return nums[i] > left and nums[i] > right


def test_simple():
    assert _is_peak([1, 2, 3, 1], find_peak([1, 2, 3, 1]))


def test_multi_peak():
    nums = [1, 2, 1, 3, 5, 6, 4]
    assert _is_peak(nums, find_peak(nums))


def test_singleton():
    assert find_peak([7]) == 0
""",
    },
    {
        "slug": "06-search-2d-matrix",
        "title": "Search a 2D matrix",
        "difficulty": "medium",
        "tags": ["binary-search", "matrix"],
        "statement": "Matrix has rows sorted, and the first element of each row is greater than the last element of the previous row. Return whether target is present. `Θ(log(m*n))`.",
        "signature": "def search_matrix(matrix: list[list[int]], target: int) -> bool: ...",
        "examples_md": """## Examples

```
[[1, 3, 5, 7],
 [10, 11, 16, 20],
 [23, 30, 34, 60]]
target=3   -> True
target=13  -> False
```""",
        "constraints": "",
        "hint": "Treat the matrix as a flat sorted array of length m*n; binary-search and decode index to (row, col).",
        "starter": """
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = matrix[mid // n][mid % n]
        if v == target:
            return True
        if v < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
""",
        "tests": """
import pytest
from solution import search_matrix


M = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        (M, 3, True),
        (M, 13, False),
        ([], 1, False),
        ([[1]], 1, True),
    ],
)
def test_examples(matrix, target, expected):
    assert search_matrix(matrix, target) is expected
""",
    },
    {
        "slug": "07-find-min-rotated",
        "title": "Find min in rotated sorted array",
        "difficulty": "medium",
        "tags": ["binary-search"],
        "statement": "Sorted array of distinct ints was rotated at an unknown pivot. Return the minimum element. `Θ(log n)`.",
        "signature": "def find_min(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[3, 4, 5, 1, 2]` | 1 |
| `[4, 5, 6, 7, 0, 1, 2]` | 0 |
| `[11, 13, 15, 17]` | 11 |""",
        "constraints": "",
        "hint": "Compare `nums[mid]` to `nums[hi]`. If greater, min is in `[mid+1, hi]`; else in `[lo, mid]`.",
        "starter": """
def find_min(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def find_min(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]
""",
        "tests": """
import pytest
from solution import find_min


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
    ],
)
def test_examples(nums, expected):
    assert find_min(nums) == expected
""",
    },
    {
        "slug": "08-valid-perfect-square",
        "title": "Valid perfect square",
        "difficulty": "easy",
        "tags": ["binary-search"],
        "statement": "Given a non-negative integer `num`, return True if it is a perfect square.",
        "signature": "def is_perfect_square(num: int) -> bool: ...",
        "examples_md": """## Examples

| num | result |
|---|---|
| 16 | True |
| 14 | False |
| 1 | True |""",
        "constraints": "",
        "hint": "Binary-search `r` in `[1, num]`; check `r*r`.",
        "starter": """
def is_perfect_square(num: int) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def is_perfect_square(num: int) -> bool:
    if num < 2:
        return num >= 0
    lo, hi = 1, num
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == num:
            return True
        if sq < num:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
""",
        "tests": """
import pytest
from solution import is_perfect_square


@pytest.mark.parametrize(
    "n, expected", [(16, True), (14, False), (1, True), (0, True), (2147395600, True)]
)
def test_examples(n, expected):
    assert is_perfect_square(n) is expected
""",
    },
    {
        "slug": "09-koko-eating-bananas",
        "title": "Koko eating bananas",
        "difficulty": "medium",
        "tags": ["binary-search-on-answer"],
        "statement": "Koko eats `k` bananas per hour from one pile. If a pile has fewer than `k`, she still spends a full hour. Given `piles` and `h` hours, return the minimum `k` such that she finishes within `h` hours.",
        "signature": "def min_eating_speed(piles: list[int], h: int) -> int: ...",
        "examples_md": """## Examples

| piles | h | result |
|---|---|---|
| `[3, 6, 7, 11]` | 8 | 4 |
| `[30, 11, 23, 4, 20]` | 5 | 30 |""",
        "constraints": "",
        "hint": "Binary-search the smallest k in `[1, max(piles)]` with `sum(ceil(p/k) for p in piles) <= h`.",
        "starter": """
def min_eating_speed(piles: list[int], h: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def min_eating_speed(piles: list[int], h: int) -> int:
    def hours(k: int) -> int:
        return sum(-(-p // k) for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
""",
        "tests": """
import pytest
from solution import min_eating_speed


@pytest.mark.parametrize(
    "piles, h, expected",
    [([3, 6, 7, 11], 8, 4), ([30, 11, 23, 4, 20], 5, 30), ([1], 1, 1)],
)
def test_examples(piles, h, expected):
    assert min_eating_speed(piles, h) == expected
""",
    },
    {
        "slug": "10-ship-within-days",
        "title": "Capacity to ship packages within D days",
        "difficulty": "medium",
        "tags": ["binary-search-on-answer"],
        "statement": "Given weights of packages (must ship in given order) and `days`, return the minimum ship capacity that allows shipping in `days`.",
        "signature": "def ship_within_days(weights: list[int], days: int) -> int: ...",
        "examples_md": """## Examples

| weights | days | result |
|---|---|---|
| `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` | 5 | 15 |
| `[3, 2, 2, 4, 1, 4]` | 3 | 6 |
| `[1, 2, 3, 1, 1]` | 4 | 3 |""",
        "constraints": "",
        "hint": "Binary-search the smallest capacity in `[max(weights), sum(weights)]` such that greedy day-count is `<= days`.",
        "starter": """
def ship_within_days(weights: list[int], days: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def ship_within_days(weights: list[int], days: int) -> int:
    def needed(cap: int) -> int:
        d = 1
        load = 0
        for w in weights:
            if load + w > cap:
                d += 1
                load = 0
            load += w
        return d

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if needed(mid) <= days:
            hi = mid
        else:
            lo = mid + 1
    return lo
""",
        "tests": """
import pytest
from solution import ship_within_days


@pytest.mark.parametrize(
    "weights, days, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
    ],
)
def test_examples(weights, days, expected):
    assert ship_within_days(weights, days) == expected
""",
    },
    {
        "slug": "11-split-array-largest-sum",
        "title": "Split array largest sum",
        "difficulty": "hard",
        "tags": ["binary-search-on-answer"],
        "statement": "Split `nums` into exactly `k` non-empty contiguous parts so as to minimize the largest part-sum. Return that minimized largest sum.",
        "signature": "def split_array(nums: list[int], k: int) -> int: ...",
        "examples_md": """## Examples

| nums | k | result |
|---|---|---|
| `[7, 2, 5, 10, 8]` | 2 | 18 |
| `[1, 2, 3, 4, 5]` | 2 | 9 |
| `[1, 4, 4]` | 3 | 4 |""",
        "constraints": "",
        "hint": "Binary-search the answer in `[max(nums), sum(nums)]`. The predicate is: can we split into <= k parts each with sum <= x.",
        "starter": """
def split_array(nums: list[int], k: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def split_array(nums: list[int], k: int) -> int:
    def feasible(x: int) -> bool:
        parts = 1
        cur = 0
        for v in nums:
            if cur + v > x:
                parts += 1
                cur = v
            else:
                cur += v
        return parts <= k

    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
""",
        "tests": """
import pytest
from solution import split_array


@pytest.mark.parametrize(
    "nums, k, expected",
    [([7, 2, 5, 10, 8], 2, 18), ([1, 2, 3, 4, 5], 2, 9), ([1, 4, 4], 3, 4)],
)
def test_examples(nums, k, expected):
    assert split_array(nums, k) == expected
""",
    },
    {
        "slug": "12-merge-intervals",
        "title": "Merge intervals",
        "difficulty": "medium",
        "tags": ["sort", "intervals"],
        "statement": "Given an array of `intervals` where `intervals[i] = [start, end]`, merge overlapping intervals.",
        "signature": "def merge(intervals: list[list[int]]) -> list[list[int]]: ...",
        "examples_md": """## Examples

| intervals | result |
|---|---|
| `[[1,3],[2,6],[8,10],[15,18]]` | `[[1,6],[8,10],[15,18]]` |
| `[[1,4],[4,5]]` | `[[1,5]]` |""",
        "constraints": "",
        "hint": "Sort by start. Walk; if current.start <= last.end, extend last; else append.",
        "starter": """
def merge(intervals: list[list[int]]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    out: list[list[int]] = [intervals[0][:]]
    for s, e in intervals[1:]:
        if s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
""",
        "tests": """
import pytest
from solution import merge


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([], []),
        ([[1, 4], [0, 4]], [[0, 4]]),
    ],
)
def test_examples(intervals, expected):
    assert merge(intervals) == expected
""",
    },
    {
        "slug": "13-insert-interval",
        "title": "Insert interval",
        "difficulty": "medium",
        "tags": ["intervals"],
        "statement": "You have a set of non-overlapping intervals sorted by start. Insert a new interval, merging overlaps. `Θ(n)`.",
        "signature": "def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]: ...",
        "examples_md": """## Examples

| intervals | new | result |
|---|---|---|
| `[[1,3],[6,9]]` | `[2,5]` | `[[1,5],[6,9]]` |
| `[[1,2],[3,5],[6,7],[8,10],[12,16]]` | `[4,8]` | `[[1,2],[3,10],[12,16]]` |""",
        "constraints": "",
        "hint": "Single pass: pass through intervals that end before new starts; merge those that overlap; append the rest.",
        "starter": """
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    i, n = 0, len(intervals)
    s, e = new_interval
    while i < n and intervals[i][1] < s:
        out.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= e:
        s = min(s, intervals[i][0])
        e = max(e, intervals[i][1])
        i += 1
    out.append([s, e])
    out.extend(intervals[i:])
    return out
""",
        "tests": """
import pytest
from solution import insert


@pytest.mark.parametrize(
    "intervals, new, expected",
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([], [5, 7], [[5, 7]]),
    ],
)
def test_examples(intervals, new, expected):
    assert insert(intervals, new) == expected
""",
    },
    {
        "slug": "14-meeting-rooms-ii",
        "title": "Meeting rooms II",
        "difficulty": "medium",
        "tags": ["sort", "heap", "intervals"],
        "statement": "Given an array of meeting time intervals, return the minimum number of conference rooms required.",
        "signature": "def min_meeting_rooms(intervals: list[list[int]]) -> int: ...",
        "examples_md": """## Examples

| intervals | result |
|---|---|
| `[[0, 30], [5, 10], [15, 20]]` | 2 |
| `[[7, 10], [2, 4]]` | 1 |""",
        "constraints": "",
        "hint": "Sort starts and ends separately. Sweep: each start increments room count; each end decrements. Track max.",
        "starter": """
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = best = 0
    j = 0
    for s in starts:
        while j < len(ends) and ends[j] <= s:
            rooms -= 1
            j += 1
        rooms += 1
        if rooms > best:
            best = rooms
    return best
""",
        "tests": """
import pytest
from solution import min_meeting_rooms


@pytest.mark.parametrize(
    "intervals, expected",
    [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1), ([], 0), ([[1, 5]], 1)],
)
def test_examples(intervals, expected):
    assert min_meeting_rooms(intervals) == expected
""",
    },
    {
        "slug": "15-sort-colors",
        "title": "Sort colors (Dutch national flag)",
        "difficulty": "medium",
        "tags": ["three-way-partition", "in-place"],
        "statement": "Given an array with values in {0, 1, 2}, sort it in place in `Θ(n)` time, `Θ(1)` space — without using a library sort.",
        "signature": "def sort_colors(nums: list[int]) -> None: ...",
        "examples_md": """## Examples

| input | result |
|---|---|
| `[2, 0, 2, 1, 1, 0]` | `[0, 0, 1, 1, 2, 2]` |
| `[2, 0, 1]` | `[0, 1, 2]` |""",
        "constraints": "",
        "hint": "Dutch national flag: three pointers `lo, i, hi`. Walk `i` from 0 to hi. If `nums[i] == 0`, swap with `nums[lo]`, advance both; if 2, swap with `nums[hi]`, decrement hi; if 1, advance i.",
        "starter": """
def sort_colors(nums: list[int]) -> None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def sort_colors(nums: list[int]) -> None:
    \"\"\"Dijkstra's Dutch national flag.  Time: Θ(n).  Space: Θ(1).\"\"\"
    lo, i, hi = 0, 0, len(nums) - 1
    while i <= hi:
        if nums[i] == 0:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[hi] = nums[hi], nums[i]
            hi -= 1
        else:
            i += 1
""",
        "tests": """
import pytest
from solution import sort_colors


@pytest.mark.parametrize(
    "given, expected",
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([], []),
    ],
)
def test_examples(given, expected):
    sort_colors(given)
    assert given == expected
""",
    },
    {
        "slug": "16-wiggle-sort",
        "title": "Wiggle sort",
        "difficulty": "medium",
        "tags": ["sort", "in-place"],
        "statement": "Reorder `nums` such that `nums[0] <= nums[1] >= nums[2] <= nums[3] ...`. In place; `Θ(n)`.",
        "signature": "def wiggle_sort(nums: list[int]) -> None: ...",
        "examples_md": """## Examples

| input | a valid output |
|---|---|
| `[3, 5, 2, 1, 6, 4]` | `[3, 5, 1, 6, 2, 4]` |
| `[1, 2, 3, 4]` | `[1, 3, 2, 4]` |""",
        "constraints": "",
        "hint": "Walk left to right. At each index, if the local order is wrong (e.g. at even index `nums[i] > nums[i+1]`), swap. Local swap preserves the prefix invariant.",
        "starter": """
def wiggle_sort(nums: list[int]) -> None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def wiggle_sort(nums: list[int]) -> None:
    for i in range(len(nums) - 1):
        if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
""",
        "tests": """
import pytest
from solution import wiggle_sort


def _is_wiggle(a):
    for i in range(len(a) - 1):
        if i % 2 == 0:
            if not a[i] <= a[i + 1]:
                return False
        else:
            if not a[i] >= a[i + 1]:
                return False
    return True


@pytest.mark.parametrize(
    "given",
    [[3, 5, 2, 1, 6, 4], [1, 2, 3, 4], [4, 1, 3, 2], [1], []],
)
def test_examples(given):
    a = given[:]
    wiggle_sort(a)
    assert _is_wiggle(a)
""",
    },
    {
        "slug": "17-h-index",
        "title": "H-index",
        "difficulty": "medium",
        "tags": ["sort", "counting-sort"],
        "statement": "Given citations of a researcher's papers, return the h-index: the largest `h` such that the researcher has `h` papers each cited at least `h` times.",
        "signature": "def h_index(citations: list[int]) -> int: ...",
        "examples_md": """## Examples

| citations | h-index |
|---|---|
| `[3, 0, 6, 1, 5]` | 3 |
| `[1, 3, 1]` | 1 |
| `[]` | 0 |""",
        "constraints": "",
        "hint": "Counting-sort by citation count (cap at n). Then walk from highest count downward accumulating papers; first `count >= h` is the answer.",
        "starter": """
def h_index(citations: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def h_index(citations: list[int]) -> int:
    \"\"\"Time: Θ(n).  Space: Θ(n).\"\"\"
    n = len(citations)
    buckets = [0] * (n + 1)
    for c in citations:
        buckets[min(c, n)] += 1
    total = 0
    for h in range(n, -1, -1):
        total += buckets[h]
        if total >= h:
            return h
    return 0
""",
        "tests": """
import pytest
from solution import h_index


@pytest.mark.parametrize(
    "citations, expected",
    [([3, 0, 6, 1, 5], 3), ([1, 3, 1], 1), ([], 0), ([100], 1), ([0, 0, 0], 0)],
)
def test_examples(citations, expected):
    assert h_index(citations) == expected
""",
    },
    {
        "slug": "18-count-smaller-after-self",
        "title": "Count of smaller numbers after self",
        "difficulty": "hard",
        "tags": ["divide-and-conquer", "merge-sort"],
        "statement": "Given an integer array `nums`, return an array `counts` where `counts[i]` is the number of elements to the right of `nums[i]` that are smaller. `Θ(n log n)`.",
        "signature": "def count_smaller(nums: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| nums | counts |
|---|---|
| `[5, 2, 6, 1]` | `[2, 1, 1, 0]` |
| `[-1]` | `[0]` |
| `[-1, -1]` | `[0, 0]` |""",
        "constraints": "",
        "hint": "Modify merge sort: track original indices. During merge, when an element from the right half is placed before some elements still pending in the left half, increment the count for those left elements... actually simpler: count for left element when it is placed (i.e., right elements already taken == count to add).",
        "starter": """
def count_smaller(nums: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def count_smaller(nums: list[int]) -> list[int]:
    \"\"\"Time: Θ(n log n).  Space: Θ(n).\"\"\"
    n = len(nums)
    counts = [0] * n
    idxs = list(range(n))

    def _sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = _sort(arr[:mid])
        right = _sort(arr[mid:])
        merged = []
        i = j = 0
        right_used = 0
        while i < len(left) and j < len(right):
            if nums[left[i]] <= nums[right[j]]:
                counts[left[i]] += right_used
                merged.append(left[i])
                i += 1
            else:
                right_used += 1
                merged.append(right[j])
                j += 1
        while i < len(left):
            counts[left[i]] += right_used
            merged.append(left[i])
            i += 1
        merged.extend(right[j:])
        return merged

    _sort(idxs)
    return counts
""",
        "tests": """
import pytest
from solution import count_smaller


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([-1], [0]),
        ([-1, -1], [0, 0]),
        ([2, 0, 1], [2, 0, 0]),
    ],
)
def test_examples(nums, expected):
    assert count_smaller(nums) == expected
""",
    },
]
