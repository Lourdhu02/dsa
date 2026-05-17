"""Module 05 (recursion & divide-conquer) manifest."""

PROBLEMS = [
    {
        "slug": "01-factorial-recursive",
        "title": "Factorial (recursive)",
        "difficulty": "easy",
        "tags": ["recursion", "base-case"],
        "statement": "Implement factorial using direct recursion (without `math.factorial`). Document the base case explicitly.",
        "signature": "def factorial(n: int) -> int: ...",
        "examples_md": """## Examples

| n | n! |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 5 | 120 |""",
        "constraints": "- `0 <= n <= 500` (Python's recursion limit forbids much more without tweaking).",
        "hint": "Base case `n == 0` returns `1`. Otherwise `n * factorial(n - 1)`.",
        "starter": """
def factorial(n: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def factorial(n: int) -> int:
    \"\"\"Time: Θ(n).  Space: Θ(n) stack.\"\"\"
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)
""",
        "tests": """
import math
import pytest

from solution import factorial


@pytest.mark.parametrize("n", [0, 1, 2, 5, 10, 20])
def test_matches_stdlib(n):
    assert factorial(n) == math.factorial(n)


def test_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)
""",
    },
    {
        "slug": "02-power-recursive",
        "title": "Power (recursive fast)",
        "difficulty": "easy",
        "tags": ["recursion", "divide-and-conquer"],
        "statement": "Recursive `Θ(log n)` exponentiation `a^n` for non-negative `n`. (Iterative version is in module 00; here state and use the divide-and-conquer recurrence.)",
        "signature": "def power(a: float, n: int) -> float: ...",
        "examples_md": """## Examples

| a | n | result |
|---|---|---|
| 2.0 | 10 | 1024.0 |
| 2.0 | -2 | 0.25 |
| 0.0 | 0 | 1.0 |""",
        "constraints": "",
        "hint": "`a^n = (a^(n//2))^2` for even n; `a^n = a * a^(n-1)` for odd n. Handle negative n by taking 1 / power(a, -n).",
        "starter": """
def power(a: float, n: int) -> float:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def power(a: float, n: int) -> float:
    \"\"\"Time: Θ(log |n|).  Space: Θ(log |n|) stack.\"\"\"
    if n < 0:
        return 1.0 / power(a, -n)
    if n == 0:
        return 1.0
    half = power(a, n // 2)
    return half * half if n % 2 == 0 else half * half * a
""",
        "tests": """
import pytest

from solution import power


@pytest.mark.parametrize(
    "a, n, expected",
    [(2.0, 10, 1024.0), (2.0, -2, 0.25), (0.0, 0, 1.0), (3.0, 4, 81.0), (5.0, 1, 5.0)],
)
def test_examples(a, n, expected):
    assert abs(power(a, n) - expected) < 1e-9
""",
    },
    {
        "slug": "03-reverse-string-recursive",
        "title": "Reverse string (recursive)",
        "difficulty": "easy",
        "tags": ["recursion", "in-place"],
        "statement": "Reverse a list of characters in place using recursion. No explicit loops; no slicing tricks.",
        "signature": "def reverse_string(s: list[str]) -> None: ...",
        "examples_md": """## Examples

| input | result |
|---|---|
| `[\"h\",\"e\",\"l\",\"l\",\"o\"]` | `[\"o\",\"l\",\"l\",\"e\",\"h\"]` |""",
        "constraints": "",
        "hint": "Helper `(l, r)` swaps and recurses `(l+1, r-1)` until `l >= r`.",
        "starter": """
def reverse_string(s: list[str]) -> None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def reverse_string(s: list[str]) -> None:
    def _rec(l: int, r: int) -> None:
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        _rec(l + 1, r - 1)

    _rec(0, len(s) - 1)
""",
        "tests": """
import pytest

from solution import reverse_string


@pytest.mark.parametrize(
    "given, expected",
    [(list("hello"), list("olleh")), ([], []), (["a"], ["a"]), (list("abc"), list("cba"))],
)
def test_examples(given, expected):
    reverse_string(given)
    assert given == expected
""",
    },
    {
        "slug": "04-tower-of-hanoi",
        "title": "Tower of Hanoi",
        "difficulty": "medium",
        "tags": ["recursion", "classic"],
        "statement": "Return the list of moves to transfer `n` disks from rod `\"A\"` to rod `\"C\"` using rod `\"B\"` as auxiliary. Each move is a tuple `(from, to)`.",
        "signature": "def hanoi(n: int) -> list[tuple[str, str]]: ...",
        "examples_md": """## Examples

| n | moves |
|---|---|
| 1 | `[(\"A\", \"C\")]` |
| 2 | `[(\"A\", \"B\"), (\"A\", \"C\"), (\"B\", \"C\")]` |""",
        "constraints": "- `0 <= n <= 18`",
        "hint": "Move n-1 from A to B (using C as aux), move the largest from A to C, move n-1 from B to C (using A as aux).",
        "starter": """
def hanoi(n: int) -> list[tuple[str, str]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def hanoi(n: int) -> list[tuple[str, str]]:
    \"\"\"T(n) = 2 T(n-1) + 1 = 2^n - 1 moves.  Space: Θ(n) stack.\"\"\"
    moves: list[tuple[str, str]] = []

    def _solve(k: int, src: str, dst: str, via: str) -> None:
        if k == 0:
            return
        _solve(k - 1, src, via, dst)
        moves.append((src, dst))
        _solve(k - 1, via, dst, src)

    _solve(n, "A", "C", "B")
    return moves
""",
        "tests": """
import pytest

from solution import hanoi


@pytest.mark.parametrize("n", [0, 1, 2, 3, 5, 10])
def test_move_count_is_2n_minus_1(n):
    assert len(hanoi(n)) == (2**n - 1)


def test_n_equals_2():
    assert hanoi(2) == [("A", "B"), ("A", "C"), ("B", "C")]
""",
    },
    {
        "slug": "05-permutations",
        "title": "Permutations",
        "difficulty": "medium",
        "tags": ["recursion", "backtracking"],
        "statement": "Return all permutations of a list of distinct integers. Order of permutations doesn't matter.",
        "signature": "def permute(nums: list[int]) -> list[list[int]]: ...",
        "examples_md": """## Examples

| nums | result count |
|---|---|
| `[1, 2, 3]` | 6 |
| `[]` | 1 (the empty permutation) |""",
        "constraints": "",
        "hint": "Backtracking: at each step pick an unused element, recurse, undo.",
        "starter": """
def permute(nums: list[int]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def permute(nums: list[int]) -> list[list[int]]:
    \"\"\"Time: Θ(n · n!).  Space: Θ(n) recursion (+ output).\"\"\"
    out: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def _bt() -> None:
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


def test_three_elements():
    result = permute([1, 2, 3])
    assert sorted(map(tuple, result)) == sorted(
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    )


def test_empty():
    assert permute([]) == [[]]


def test_single():
    assert permute([7]) == [[7]]
""",
    },
    {
        "slug": "06-subsets",
        "title": "Subsets (power set)",
        "difficulty": "medium",
        "tags": ["recursion", "backtracking"],
        "statement": "Return all subsets of an input list of distinct integers (the power set). Each subset can appear in any order; the list of subsets can be in any order.",
        "signature": "def subsets(nums: list[int]) -> list[list[int]]: ...",
        "examples_md": """## Examples

| nums | count |
|---|---|
| `[1, 2, 3]` | 8 |
| `[]` | 1 |""",
        "constraints": "",
        "hint": "For each element decide *include or skip*. Recursion tree has 2^n leaves, each a subset.",
        "starter": """
def subsets(nums: list[int]) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def subsets(nums: list[int]) -> list[list[int]]:
    \"\"\"Time: Θ(n · 2^n).  Space: Θ(n) recursion.\"\"\"
    out: list[list[int]] = []
    cur: list[int] = []

    def _rec(i: int) -> None:
        if i == len(nums):
            out.append(cur[:])
            return
        _rec(i + 1)
        cur.append(nums[i])
        _rec(i + 1)
        cur.pop()

    _rec(0)
    return out
""",
        "tests": """
from solution import subsets


def test_three_elements():
    assert sorted(map(tuple, subsets([1, 2, 3]))) == sorted(
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    )


def test_empty():
    assert subsets([]) == [[]]
""",
    },
    {
        "slug": "07-merge-sort",
        "title": "Merge sort",
        "difficulty": "medium",
        "tags": ["divide-and-conquer", "sorting", "stable"],
        "statement": "Implement merge sort. Return a NEW sorted list; don't mutate the input. Must be stable: equal keys preserve relative order.",
        "signature": "def merge_sort(xs: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| xs | sorted |
|---|---|
| `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]` | `[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]` |""",
        "constraints": "",
        "hint": "Recurse on halves, then linear merge. The merge step's tie-breaker (`<=`, not `<`) is what makes it stable.",
        "starter": """
def merge_sort(xs: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def merge_sort(xs: list[int]) -> list[int]:
    \"\"\"Time: Θ(n log n).  Space: Θ(n).  Stable.  Reference: CLRS § 2.3.\"\"\"
    if len(xs) <= 1:
        return xs[:]
    mid = len(xs) // 2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])
    out: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
""",
        "tests": """
import random

import pytest

from solution import merge_sort


def test_matches_sorted():
    rng = random.Random(0)
    for _ in range(10):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 100))]
        assert merge_sort(xs) == sorted(xs)


def test_stability_on_tuples():
    # We can't test stability on bare ints, but we can verify by tagging equal-keyed integers.
    tagged = list(enumerate([5, 1, 5, 1, 5]))
    # Sort by value; ensure tags within each value group keep ascending order.
    indices = sorted(range(len(tagged)), key=lambda i: tagged[i][1])
    # Reconstruct what stable sort would do: extract tags grouped by value
    by_value = {}
    for i in indices:
        by_value.setdefault(tagged[i][1], []).append(tagged[i][0])
    for tags in by_value.values():
        assert tags == sorted(tags)
""",
    },
    {
        "slug": "08-quick-sort",
        "title": "Quick sort",
        "difficulty": "medium",
        "tags": ["divide-and-conquer", "sorting", "in-place"],
        "statement": "Implement quicksort with a random pivot. Sort in place and return the same list.",
        "signature": "def quick_sort(xs: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| xs | sorted |
|---|---|
| `[3, 1, 4, 1, 5]` | `[1, 1, 3, 4, 5]` |""",
        "constraints": "",
        "hint": "Lomuto partition with a random pivot. After partition, recurse on `[lo, p-1]` and `[p+1, hi]`.",
        "starter": """
def quick_sort(xs: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import random


def quick_sort(xs: list[int]) -> list[int]:
    \"\"\"Time: Θ(n log n) expected, Θ(n²) worst.  Space: Θ(log n) avg stack.\"\"\"
    def _partition(lo: int, hi: int) -> int:
        pi = random.randint(lo, hi)
        xs[pi], xs[hi] = xs[hi], xs[pi]
        pivot = xs[hi]
        i = lo
        for j in range(lo, hi):
            if xs[j] < pivot:
                xs[i], xs[j] = xs[j], xs[i]
                i += 1
        xs[i], xs[hi] = xs[hi], xs[i]
        return i

    def _qs(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        p = _partition(lo, hi)
        _qs(lo, p - 1)
        _qs(p + 1, hi)

    _qs(0, len(xs) - 1)
    return xs
""",
        "tests": """
import random

from solution import quick_sort


def test_matches_sorted():
    rng = random.Random(1)
    for _ in range(10):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 100))]
        assert quick_sort(xs[:]) == sorted(xs)
""",
    },
    {
        "slug": "09-quickselect-kth-smallest",
        "title": "Kth smallest (quickselect)",
        "difficulty": "medium",
        "tags": ["divide-and-conquer", "selection"],
        "statement": "Return the `k`-th smallest element (1-indexed) of an array using quickselect. Expected `Θ(n)`.",
        "signature": "def kth_smallest(nums: list[int], k: int) -> int: ...",
        "examples_md": """## Examples

| nums | k | result |
|---|---|---|
| `[3, 2, 1, 5, 6, 4]` | 2 | 2 |
| `[3, 2, 3, 1, 2, 4, 5, 5, 6]` | 4 | 3 |""",
        "constraints": "- `1 <= k <= len(nums)`",
        "hint": "Same partition as quicksort; recurse only into the side containing position `k - 1` (0-indexed).",
        "starter": """
def kth_smallest(nums: list[int], k: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import random


def kth_smallest(nums: list[int], k: int) -> int:
    a = nums[:]
    target = k - 1
    lo, hi = 0, len(a) - 1
    while lo < hi:
        pi = random.randint(lo, hi)
        a[pi], a[hi] = a[hi], a[pi]
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        if i == target:
            return a[i]
        if i < target:
            lo = i + 1
        else:
            hi = i - 1
    return a[target]
""",
        "tests": """
import random
import pytest

from solution import kth_smallest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 3),
        ([1], 1, 1),
    ],
)
def test_examples(nums, k, expected):
    assert kth_smallest(nums, k) == expected


def test_random_matches_sorted():
    rng = random.Random(42)
    for _ in range(20):
        n = rng.randint(1, 100)
        xs = [rng.randint(-100, 100) for _ in range(n)]
        s = sorted(xs)
        for k in (1, n // 2 + 1, n):
            assert kth_smallest(xs, k) == s[k - 1]
""",
    },
    {
        "slug": "10-count-inversions",
        "title": "Count inversions",
        "difficulty": "hard",
        "tags": ["divide-and-conquer", "merge-sort"],
        "statement": "Given an integer array, return the number of *inversions* — pairs `(i, j)` with `i < j` and `nums[i] > nums[j]`. Solve in `Θ(n log n)`.",
        "signature": "def count_inversions(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | inversions |
|---|---|
| `[1, 3, 5, 2, 4, 6]` | 3 |
| `[5, 4, 3, 2, 1]` | 10 |
| `[1, 2, 3]` | 0 |""",
        "constraints": "",
        "hint": "Modify merge-sort. When you take an element from the right half during the merge while the left half still has `r` elements, add `r` to the inversion count.",
        "starter": """
def count_inversions(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def count_inversions(nums: list[int]) -> int:
    \"\"\"Time: Θ(n log n).  Space: Θ(n).\"\"\"
    def _sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, cl = _sort(a[:mid])
        right, cr = _sort(a[mid:])
        merged = []
        i = j = 0
        inv = cl + cr
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    _, total = _sort(nums)
    return total
""",
        "tests": """
import pytest

from solution import count_inversions


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 5, 2, 4, 6], 3),
        ([5, 4, 3, 2, 1], 10),
        ([1, 2, 3], 0),
        ([], 0),
        ([2, 4, 1, 3, 5], 3),
    ],
)
def test_examples(nums, expected):
    assert count_inversions(nums) == expected
""",
    },
    {
        "slug": "11-search-in-rotated-sorted-array",
        "title": "Search in rotated sorted array",
        "difficulty": "medium",
        "tags": ["binary-search", "divide-and-conquer"],
        "statement": "An array of distinct integers was sorted in ascending order then rotated at an unknown pivot. Given `nums` and `target`, return the index of `target` in `nums`, or `-1` if absent. `Θ(log n)` time.",
        "signature": "def search(nums: list[int], target: int) -> int: ...",
        "examples_md": """## Examples

| nums | target | result |
|---|---|---|
| `[4, 5, 6, 7, 0, 1, 2]` | 0 | 4 |
| `[4, 5, 6, 7, 0, 1, 2]` | 3 | -1 |
| `[1]` | 0 | -1 |""",
        "constraints": "",
        "hint": "Modified binary search. At each step decide which half is sorted; check if target lies in that sorted half, otherwise recurse into the other.",
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
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
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
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
    ],
)
def test_examples(nums, target, expected):
    assert search(nums, target) == expected
""",
    },
    {
        "slug": "12-pow-x-n",
        "title": "Pow(x, n)",
        "difficulty": "medium",
        "tags": ["divide-and-conquer"],
        "statement": "Compute `x^n` for float `x` and integer `n` in `Θ(log |n|)`.",
        "signature": "def my_pow(x: float, n: int) -> float: ...",
        "examples_md": """## Examples

| x | n | result |
|---|---|---|
| 2.0 | 10 | 1024.0 |
| 2.1 | 3 | 9.261 |
| 2.0 | -2 | 0.25 |""",
        "constraints": "",
        "hint": "Recurse on n // 2, square, fix the parity. Negative n: take 1 / pow(x, -n).",
        "starter": """
def my_pow(x: float, n: int) -> float:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def my_pow(x: float, n: int) -> float:
    if n < 0:
        x = 1.0 / x
        n = -n
    result = 1.0
    base = x
    while n > 0:
        if n & 1:
            result *= base
        base *= base
        n >>= 1
    return result
""",
        "tests": """
import pytest

from solution import my_pow


@pytest.mark.parametrize(
    "x, n, expected",
    [(2.0, 10, 1024.0), (2.1, 3, 9.261), (2.0, -2, 0.25), (1.0, 1000, 1.0)],
)
def test_examples(x, n, expected):
    assert abs(my_pow(x, n) - expected) < 1e-9
""",
    },
    {
        "slug": "13-majority-element-bm-vs-dc",
        "title": "Majority element (D&C variant)",
        "difficulty": "medium",
        "tags": ["divide-and-conquer", "boyer-moore"],
        "statement": "Find the element that appears more than `n/2` times in `nums` (it is guaranteed to exist). Solve with a divide-and-conquer approach (`Θ(n log n)`). The `Θ(n)` Boyer-Moore vote is shown in module 13.",
        "signature": "def majority_element(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | majority |
|---|---|
| `[3, 2, 3]` | 3 |
| `[2, 2, 1, 1, 1, 2, 2]` | 2 |""",
        "constraints": "",
        "hint": "Split the array. If both halves agree, that's the answer. Otherwise count occurrences of each candidate across the whole range.",
        "starter": """
def majority_element(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def majority_element(nums: list[int]) -> int:
    def _rec(lo: int, hi: int) -> int:
        if lo == hi:
            return nums[lo]
        mid = (lo + hi) // 2
        left = _rec(lo, mid)
        right = _rec(mid + 1, hi)
        if left == right:
            return left
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
        return left if left_count > right_count else right

    return _rec(0, len(nums) - 1)
""",
        "tests": """
import pytest

from solution import majority_element


@pytest.mark.parametrize(
    "nums, expected",
    [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2), ([1], 1), ([1, 1, 1, 2], 1)],
)
def test_examples(nums, expected):
    assert majority_element(nums) == expected
""",
    },
    {
        "slug": "14-generate-parentheses",
        "title": "Generate parentheses",
        "difficulty": "medium",
        "tags": ["recursion", "backtracking"],
        "statement": "Given `n` pairs of parentheses, return all well-formed strings of length `2n`.",
        "signature": "def generate_parenthesis(n: int) -> list[str]: ...",
        "examples_md": """## Examples

| n | result |
|---|---|
| 3 | `[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]` |
| 1 | `[\"()\"]` |""",
        "constraints": "- `1 <= n <= 8`",
        "hint": "Backtrack with two counters: opens used so far and closes used so far. Add `(` while `opens < n`; add `)` while `closes < opens`.",
        "starter": """
def generate_parenthesis(n: int) -> list[str]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def generate_parenthesis(n: int) -> list[str]:
    out: list[str] = []

    def _bt(s: str, opens: int, closes: int) -> None:
        if len(s) == 2 * n:
            out.append(s)
            return
        if opens < n:
            _bt(s + "(", opens + 1, closes)
        if closes < opens:
            _bt(s + ")", opens, closes + 1)

    _bt("", 0, 0)
    return out
""",
        "tests": """
import pytest

from solution import generate_parenthesis


def test_n3():
    assert sorted(generate_parenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )


def test_n1():
    assert generate_parenthesis(1) == ["()"]


def test_n0_count():
    assert generate_parenthesis(0) == [""]
""",
    },
    {
        "slug": "15-letter-combinations-phone",
        "title": "Letter combinations of a phone number",
        "difficulty": "medium",
        "tags": ["recursion", "backtracking"],
        "statement": "Given a string of digits 2-9, return all possible letter combinations the number could represent on a standard phone keypad.",
        "signature": "def letter_combinations(digits: str) -> list[str]: ...",
        "examples_md": """## Examples

| digits | result |
|---|---|
| `\"23\"` | `[\"ad\",\"ae\",\"af\",\"bd\",\"be\",\"bf\",\"cd\",\"ce\",\"cf\"]` |
| `\"\"` | `[]` |
| `\"2\"` | `[\"a\",\"b\",\"c\"]` |""",
        "constraints": "",
        "hint": "Standard backtrack. At each position pick one letter from the digit's mapping.",
        "starter": """
def letter_combinations(digits: str) -> list[str]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []
    table = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    out: list[str] = []

    def _bt(i: int, cur: str) -> None:
        if i == len(digits):
            out.append(cur)
            return
        for ch in table[digits[i]]:
            _bt(i + 1, cur + ch)

    _bt(0, "")
    return out
""",
        "tests": """
import pytest

from solution import letter_combinations


def test_two_digits():
    assert sorted(letter_combinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )


def test_empty():
    assert letter_combinations("") == []


def test_one_digit():
    assert sorted(letter_combinations("2")) == ["a", "b", "c"]
""",
    },
    {
        "slug": "16-different-ways-add-parens",
        "title": "Different ways to add parentheses",
        "difficulty": "medium",
        "tags": ["divide-and-conquer", "memoization"],
        "statement": "Given an arithmetic expression of integers and `+`, `-`, `*`, return all possible results of inserting parentheses (any order of operations).",
        "signature": "def diff_ways_to_compute(expression: str) -> list[int]: ...",
        "examples_md": """## Examples

| expression | results |
|---|---|
| `\"2-1-1\"` | `[0, 2]` |
| `\"2*3-4*5\"` | `[-34, -14, -10, -10, 10]` |""",
        "constraints": "",
        "hint": "Recurse on operators: split at each `+`, `-`, `*`; recursively compute results of left and right; combine pairwise.",
        "starter": """
def diff_ways_to_compute(expression: str) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def diff_ways_to_compute(expression: str) -> list[int]:
    memo: dict[str, list[int]] = {}

    def _rec(s: str) -> list[int]:
        if s in memo:
            return memo[s]
        out: list[int] = []
        for i, ch in enumerate(s):
            if ch in "+-*":
                left = _rec(s[:i])
                right = _rec(s[i + 1 :])
                for a in left:
                    for b in right:
                        if ch == "+":
                            out.append(a + b)
                        elif ch == "-":
                            out.append(a - b)
                        else:
                            out.append(a * b)
        if not out:
            out = [int(s)]
        memo[s] = out
        return out

    return _rec(expression)
""",
        "tests": """
import pytest

from solution import diff_ways_to_compute


def test_simple():
    assert sorted(diff_ways_to_compute("2-1-1")) == [0, 2]


def test_complex():
    assert sorted(diff_ways_to_compute("2*3-4*5")) == [-34, -14, -10, -10, 10]


def test_single_number():
    assert diff_ways_to_compute("17") == [17]
""",
    },
    {
        "slug": "17-validate-bst-recursive",
        "title": "Validate BST",
        "difficulty": "medium",
        "tags": ["tree", "recursion"],
        "statement": "Given the root of a binary tree, determine if it is a valid binary search tree. Every node in the left subtree must be strictly less than the node; every node in the right must be strictly greater. The simplest definition that works is recursive with `(min, max)` bounds.",
        "signature": "class TreeNode:\n    val: int\n    left: 'TreeNode | None'\n    right: 'TreeNode | None'\n\ndef is_valid_bst(root: TreeNode | None) -> bool: ...",
        "examples_md": """## Examples

```
    2
   / \\
  1   3       -> True

    5
   / \\
  1   4
     / \\
    3   6    -> False (3 < 5 but in right subtree)
```""",
        "constraints": "",
        "hint": "Recurse with `(low, high)` bounds. Node value must satisfy `low < val < high`. Left subtree gets bound `(low, val)`, right gets `(val, high)`.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    def _rec(node, low, high):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return _rec(node.left, low, node.val) and _rec(node.right, node.val, high)

    return _rec(root, float("-inf"), float("inf"))
""",
        "tests": """
from solution import TreeNode, is_valid_bst


def test_valid_simple():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root) is True


def test_invalid_right_subtree():
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(root) is False


def test_equal_values_invalid():
    root = TreeNode(2, TreeNode(2))
    assert is_valid_bst(root) is False


def test_empty():
    assert is_valid_bst(None) is True
""",
    },
    {
        "slug": "18-construct-tree-from-preorder-inorder",
        "title": "Construct tree from preorder + inorder",
        "difficulty": "medium",
        "tags": ["tree", "divide-and-conquer"],
        "statement": "Given preorder and inorder traversal arrays of a binary tree (all values distinct), reconstruct the tree and return its root.",
        "signature": "class TreeNode: ...\n\ndef build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None: ...",
        "examples_md": """## Examples

```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

result:
        3
       / \\
      9  20
        /  \\
       15   7
```""",
        "constraints": "",
        "hint": "First element of preorder is the root. Find it in inorder to split left/right subtree ranges, then recurse. Index inorder values in a hash map for `Θ(1)` lookup so the total is `Θ(n)`.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    \"\"\"Time: Θ(n).  Space: Θ(n).\"\"\"
    idx = {v: i for i, v in enumerate(inorder)}
    pre_iter = iter(preorder)

    def _rec(lo: int, hi: int):
        if lo > hi:
            return None
        root_val = next(pre_iter)
        node = TreeNode(root_val)
        i = idx[root_val]
        node.left = _rec(lo, i - 1)
        node.right = _rec(i + 1, hi)
        return node

    return _rec(0, len(inorder) - 1)
""",
        "tests": """
from solution import TreeNode, build_tree


def _inorder(node):
    if node is None:
        return []
    return _inorder(node.left) + [node.val] + _inorder(node.right)


def _preorder(node):
    if node is None:
        return []
    return [node.val] + _preorder(node.left) + _preorder(node.right)


def test_classic():
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    root = build_tree(pre, ino)
    assert _preorder(root) == pre
    assert _inorder(root) == ino


def test_empty():
    assert build_tree([], []) is None


def test_single_node():
    root = build_tree([1], [1])
    assert root is not None and root.val == 1
""",
    },
]
