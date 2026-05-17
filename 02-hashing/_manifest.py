"""Problem manifest for module 02 (hashing).  Consumed by scripts/scaffold.py."""

PROBLEMS = [
    {
        "slug": "01-two-sum",
        "title": "Two sum",
        "difficulty": "easy",
        "tags": ["hash-map"],
        "statement": "Given an integer array `nums` and an integer `target`, return the indices `(i, j)` (with `i < j`) of the two numbers such that `nums[i] + nums[j] == target`. Exactly one solution exists.",
        "signature": "def two_sum(nums: list[int], target: int) -> tuple[int, int]: ...",
        "examples_md": """## Examples

| nums | target | result |
|---|---|---|
| `[2, 7, 11, 15]` | 9 | `(0, 1)` |
| `[3, 2, 4]` | 6 | `(1, 2)` |
| `[3, 3]` | 6 | `(0, 1)` |""",
        "constraints": "- `2 <= len(nums) <= 10^4`",
        "hint": "One pass. For each `x`, check if `target - x` is already in a hash map of `value -> earliest index`. If yes, return the pair. If no, store `x` and continue.",
        "starter": """
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    # TODO: one-pass hash map.
    raise NotImplementedError
""",
        "reference": """
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    \"\"\"One-pass hash map.

    Time:  Θ(n) average (hash lookup), Θ(n²) adversarial worst.
    Space: Θ(n).
    \"\"\"
    seen: dict[int, int] = {}
    for j, x in enumerate(nums):
        if target - x in seen:
            return seen[target - x], j
        seen[x] = j
    raise ValueError("no solution")
""",
        "tests": """
import pytest

from solution import two_sum


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([1, 5, 1, 5], 6, (0, 1)),
    ],
)
def test_examples(nums, target, expected):
    assert two_sum(nums, target) == expected
""",
    },
    {
        "slug": "02-contains-duplicate",
        "title": "Contains duplicate",
        "difficulty": "easy",
        "tags": ["hash-set"],
        "statement": "Return `True` if any value appears at least twice in the array, else `False`.",
        "signature": "def contains_duplicate(nums: list[int]) -> bool: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[1, 2, 3, 1]` | True |
| `[1, 2, 3, 4]` | False |
| `[]` | False |""",
        "constraints": "",
        "hint": "Walk the array, build a set; return True the moment you see a repeat. Alternative: `len(set(nums)) != len(nums)` — slightly slower because it always scans all of nums.",
        "starter": """
def contains_duplicate(nums: list[int]) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def contains_duplicate(nums: list[int]) -> bool:
    \"\"\"Time: Θ(n) avg.  Space: Θ(n).\"\"\"
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
""",
        "tests": """
import pytest

from solution import contains_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 2, 3, 1], True), ([1, 2, 3, 4], False), ([], False), ([1], False), ([1, 1], True)],
)
def test_examples(nums, expected):
    assert contains_duplicate(nums) == expected
""",
    },
    {
        "slug": "03-valid-anagram",
        "title": "Valid anagram",
        "difficulty": "easy",
        "tags": ["hash-map", "counter"],
        "statement": "Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`. Both strings consist of lowercase English letters.",
        "signature": "def is_anagram(s: str, t: str) -> bool: ...",
        "examples_md": """## Examples

| s | t | result |
|---|---|---|
| `"anagram"` | `"nagaram"` | True |
| `"rat"` | `"car"` | False |
| `""` | `""` | True |""",
        "constraints": "",
        "hint": "Compare character counts. Either build two `Counter`s and compare, or sort both strings and compare.",
        "starter": """
def is_anagram(s: str, t: str) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    \"\"\"Time: Θ(n).  Space: Θ(σ) where σ is alphabet size.\"\"\"
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
""",
        "tests": """
import pytest

from solution import is_anagram


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "ab", False),
        ("aabb", "abab", True),
    ],
)
def test_examples(s, t, expected):
    assert is_anagram(s, t) == expected
""",
    },
    {
        "slug": "04-first-unique-char",
        "title": "First unique character",
        "difficulty": "easy",
        "tags": ["hash-map", "counter"],
        "statement": "Return the index of the first character in `s` that appears exactly once, or `-1` if no such character exists.",
        "signature": "def first_uniq_char(s: str) -> int: ...",
        "examples_md": """## Examples

| s | result |
|---|---|
| `"leetcode"` | 0 |
| `"loveleetcode"` | 2 |
| `"aabb"` | -1 |""",
        "constraints": "",
        "hint": "Two passes: count characters, then scan the string and return the first index whose count is 1.",
        "starter": """
def first_uniq_char(s: str) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def first_uniq_char(s: str) -> int:
    \"\"\"Time: Θ(n).  Space: Θ(σ).\"\"\"
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
""",
        "tests": """
import pytest

from solution import first_uniq_char


@pytest.mark.parametrize(
    "s, expected",
    [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1), ("z", 0), ("", -1)],
)
def test_examples(s, expected):
    assert first_uniq_char(s) == expected
""",
    },
    {
        "slug": "05-intersection-arrays",
        "title": "Intersection of two arrays",
        "difficulty": "easy",
        "tags": ["hash-set"],
        "statement": "Given two integer arrays, return their set-style intersection: each element appears once, order doesn't matter.",
        "signature": "def intersection(a: list[int], b: list[int]) -> list[int]: ...",
        "examples_md": """## Examples

| a | b | result (any order) |
|---|---|---|
| `[1, 2, 2, 1]` | `[2, 2]` | `[2]` |
| `[4, 9, 5]` | `[9, 4, 9, 8, 4]` | `[4, 9]` |""",
        "constraints": "",
        "hint": "Put `a` into a set; iterate `b`; collect items present in the set; deduplicate.",
        "starter": """
def intersection(a: list[int], b: list[int]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def intersection(a: list[int], b: list[int]) -> list[int]:
    \"\"\"Time: Θ(n + m).  Space: Θ(min(n, m)).\"\"\"
    sa = set(a)
    return list({x for x in b if x in sa})
""",
        "tests": """
import pytest

from solution import intersection


def test_examples():
    assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert intersection([], [1, 2]) == []
    assert sorted(intersection([1, 2, 3], [4, 5, 6])) == []
""",
    },
    {
        "slug": "06-happy-number",
        "title": "Happy number",
        "difficulty": "easy",
        "tags": ["hash-set", "cycle-detection"],
        "statement": "A number is *happy* if repeatedly replacing it by the sum of squares of its digits eventually reaches 1. If it loops without reaching 1, it isn't happy. Return whether `n` is happy.",
        "signature": "def is_happy(n: int) -> bool: ...",
        "examples_md": """## Examples

| n | result |
|---|---|
| 19 | True (`19 -> 82 -> 68 -> 100 -> 1`) |
| 2 | False |""",
        "constraints": "",
        "hint": "Keep seen values in a set. If `n` reaches 1, return True; if `n` is already in `seen`, return False (cycle).",
        "starter": """
def is_happy(n: int) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def is_happy(n: int) -> bool:
    \"\"\"Time: Θ(log n) digits per step, bounded number of steps (the squared-digit
    sum has fixed points and short cycles).
    Space: Θ(k) for the seen set, k tiny in practice.
    \"\"\"
    seen: set[int] = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
""",
        "tests": """
import pytest

from solution import is_happy


@pytest.mark.parametrize("n, expected", [(19, True), (2, False), (1, True), (7, True), (4, False)])
def test_examples(n, expected):
    assert is_happy(n) == expected
""",
    },
    {
        "slug": "07-group-anagrams",
        "title": "Group anagrams",
        "difficulty": "medium",
        "tags": ["hash-map", "canonical-form"],
        "statement": "Given an array of strings, group anagrams together. Return the groups in any order; within a group, preserve any order.",
        "signature": "def group_anagrams(strs: list[str]) -> list[list[str]]: ...",
        "examples_md": """## Examples

| strs | groups (any order) |
|---|---|
| `["eat","tea","tan","ate","nat","bat"]` | `[["bat"], ["nat","tan"], ["ate","eat","tea"]]` |
| `[""]` | `[[""]]` |
| `["a"]` | `[["a"]]` |""",
        "constraints": "",
        "hint": "Use sorted-tuple of characters as canonical form. Hash to a `dict[tuple, list[str]]`.",
        "starter": """
def group_anagrams(strs: list[str]) -> list[list[str]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    \"\"\"Bucket by sorted-character key.

    Time:  Θ(N · L log L) where N = number of strings, L = max length.
    Space: Θ(N · L).
    \"\"\"
    buckets: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for s in strs:
        buckets[tuple(sorted(s))].append(s)
    return list(buckets.values())
""",
        "tests": """
import pytest

from solution import group_anagrams


def _norm(groups):
    return sorted(tuple(sorted(g)) for g in groups)


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_examples(strs, expected):
    assert _norm(group_anagrams(strs)) == _norm(expected)
""",
    },
    {
        "slug": "08-longest-consecutive-sequence",
        "title": "Longest consecutive sequence",
        "difficulty": "medium",
        "tags": ["hash-set"],
        "statement": "Given an unsorted integer array, return the length of the longest sequence of consecutive integers. Run in `Θ(n)`.",
        "signature": "def longest_consecutive(nums: list[int]) -> int: ...",
        "examples_md": """## Examples

| nums | answer |
|---|---|
| `[100, 4, 200, 1, 3, 2]` | 4 (`[1, 2, 3, 4]`) |
| `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]` | 9 |
| `[]` | 0 |""",
        "constraints": "",
        "hint": "Put all numbers in a set. For each `x` only start counting when `x - 1` is NOT in the set (so each run is processed once). Walk `x, x+1, x+2, ...` while present. Total work Θ(n) because every element is visited as part of at most one run.",
        "starter": """
def longest_consecutive(nums: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def longest_consecutive(nums: list[int]) -> int:
    \"\"\"Time: Θ(n) avg; each element visited at most twice.  Space: Θ(n).\"\"\"
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 in s:
            continue
        cur = x
        length = 1
        while cur + 1 in s:
            cur += 1
            length += 1
        if length > best:
            best = length
    return best
""",
        "tests": """
import pytest

from solution import longest_consecutive


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1], 1),
        ([1, 2, 0, 1], 3),
    ],
)
def test_examples(nums, expected):
    assert longest_consecutive(nums) == expected
""",
    },
    {
        "slug": "09-top-k-frequent",
        "title": "Top K frequent elements",
        "difficulty": "medium",
        "tags": ["hash-map", "bucket-sort"],
        "statement": "Given an integer array `nums` and integer `k`, return the `k` most frequent elements (any order).",
        "signature": "def top_k_frequent(nums: list[int], k: int) -> list[int]: ...",
        "examples_md": """## Examples

| nums | k | answer (any order) |
|---|---|---|
| `[1,1,1,2,2,3]` | 2 | `[1, 2]` |
| `[1]` | 1 | `[1]` |""",
        "constraints": "",
        "hint": "Count with `Counter`, then either (a) `Counter.most_common(k)` — Θ(n log n) — or (b) bucket sort by frequency in Θ(n).",
        "starter": """
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    \"\"\"Bucket sort by frequency for guaranteed Θ(n).

    Time:  Θ(n).  Space: Θ(n).
    \"\"\"
    counts = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)
    out: list[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for v in buckets[freq]:
            out.append(v)
            if len(out) == k:
                return out
    return out
""",
        "tests": """
import pytest

from solution import top_k_frequent


@pytest.mark.parametrize(
    "nums, k, expected_set",
    [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 5, 5, 6], 2, {4, 5}),
    ],
)
def test_examples(nums, k, expected_set):
    assert set(top_k_frequent(nums, k)) == expected_set
""",
    },
    {
        "slug": "10-design-hashmap",
        "title": "Design HashMap",
        "difficulty": "medium",
        "tags": ["data-structure-design"],
        "statement": "Implement a `MyHashMap` class without using the built-in hash table. Support `put(key, value)`, `get(key) -> int` (return -1 if missing), `remove(key)`. Keys and values are non-negative integers.",
        "signature": "class MyHashMap:\n    def put(self, key: int, value: int) -> None: ...\n    def get(self, key: int) -> int: ...\n    def remove(self, key: int) -> None: ...",
        "examples_md": """## Examples

```
m = MyHashMap()
m.put(1, 1); m.put(2, 2)
m.get(1)            # 1
m.get(3)            # -1
m.put(2, 1)
m.get(2)            # 1
m.remove(2)
m.get(2)            # -1
```""",
        "constraints": "",
        "hint": "Separate chaining with a list of buckets. Bucket index = `hash(key) % m`. Resize when load factor exceeds ~0.75.",
        "starter": """
class MyHashMap:
    def __init__(self) -> None:
        # TODO: initialize buckets
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def remove(self, key: int) -> None:
        raise NotImplementedError
""",
        "reference": """
class MyHashMap:
    \"\"\"Separate chaining.  Amortized Θ(1) avg per op.\"\"\"

    INIT_M = 16
    LIMIT = 0.75

    def __init__(self) -> None:
        self._buckets: list[list[tuple[int, int]]] = [[] for _ in range(self.INIT_M)]
        self._n = 0

    def _bucket(self, key: int) -> list[tuple[int, int]]:
        return self._buckets[key % len(self._buckets)]

    def put(self, key: int, value: int) -> None:
        b = self._bucket(key)
        for i, (k, _) in enumerate(b):
            if k == key:
                b[i] = (key, value)
                return
        b.append((key, value))
        self._n += 1
        if self._n / len(self._buckets) > self.LIMIT:
            self._resize(len(self._buckets) * 2)

    def get(self, key: int) -> int:
        for k, v in self._bucket(key):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        b = self._bucket(key)
        for i, (k, _) in enumerate(b):
            if k == key:
                del b[i]
                self._n -= 1
                return

    def _resize(self, new_m: int) -> None:
        old_items = [(k, v) for bucket in self._buckets for (k, v) in bucket]
        self._buckets = [[] for _ in range(new_m)]
        self._n = 0
        for k, v in old_items:
            self.put(k, v)
""",
        "tests": """
from solution import MyHashMap


def test_basic_flow():
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    assert m.get(1) == 1
    assert m.get(3) == -1
    m.put(2, 1)
    assert m.get(2) == 1
    m.remove(2)
    assert m.get(2) == -1


def test_many_inserts_with_resize():
    m = MyHashMap()
    for i in range(200):
        m.put(i, i * 10)
    for i in range(200):
        assert m.get(i) == i * 10


def test_update_does_not_grow():
    m = MyHashMap()
    for _ in range(100):
        m.put(7, 1)
    assert m.get(7) == 1
""",
    },
    {
        "slug": "11-design-hashset",
        "title": "Design HashSet",
        "difficulty": "easy",
        "tags": ["data-structure-design"],
        "statement": "Implement `MyHashSet` with `add`, `remove`, `contains` — without using a built-in hash set.",
        "signature": "class MyHashSet:\n    def add(self, key: int) -> None: ...\n    def remove(self, key: int) -> None: ...\n    def contains(self, key: int) -> bool: ...",
        "examples_md": """## Examples

```
s = MyHashSet()
s.add(1); s.add(2)
s.contains(1)    # True
s.contains(3)    # False
s.remove(2)
s.contains(2)    # False
```""",
        "constraints": "",
        "hint": "Same backbone as MyHashMap but each slot holds a key, no value. Chaining is the simplest path.",
        "starter": """
class MyHashSet:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, key: int) -> None:
        raise NotImplementedError

    def remove(self, key: int) -> None:
        raise NotImplementedError

    def contains(self, key: int) -> bool:
        raise NotImplementedError
""",
        "reference": """
class MyHashSet:
    INIT_M = 16

    def __init__(self) -> None:
        self._buckets: list[list[int]] = [[] for _ in range(self.INIT_M)]
        self._n = 0

    def _bucket(self, key: int) -> list[int]:
        return self._buckets[key % len(self._buckets)]

    def add(self, key: int) -> None:
        b = self._bucket(key)
        if key not in b:
            b.append(key)
            self._n += 1
            if self._n / len(self._buckets) > 0.75:
                self._resize(len(self._buckets) * 2)

    def remove(self, key: int) -> None:
        b = self._bucket(key)
        if key in b:
            b.remove(key)
            self._n -= 1

    def contains(self, key: int) -> bool:
        return key in self._bucket(key)

    def _resize(self, new_m: int) -> None:
        items = [k for bucket in self._buckets for k in bucket]
        self._buckets = [[] for _ in range(new_m)]
        self._n = 0
        for k in items:
            self.add(k)
""",
        "tests": """
from solution import MyHashSet


def test_basic_flow():
    s = MyHashSet()
    s.add(1)
    s.add(2)
    assert s.contains(1)
    assert not s.contains(3)
    s.remove(2)
    assert not s.contains(2)


def test_idempotent_add():
    s = MyHashSet()
    for _ in range(10):
        s.add(5)
    assert s.contains(5)
""",
    },
    {
        "slug": "12-isomorphic-strings",
        "title": "Isomorphic strings",
        "difficulty": "easy",
        "tags": ["hash-map", "bijection"],
        "statement": "Two strings `s` and `t` are isomorphic if characters in `s` can be replaced consistently to obtain `t`. Each character must map to exactly one character, and no two characters may map to the same character.",
        "signature": "def is_isomorphic(s: str, t: str) -> bool: ...",
        "examples_md": """## Examples

| s | t | result |
|---|---|---|
| `"egg"` | `"add"` | True |
| `"foo"` | `"bar"` | False |
| `"paper"` | `"title"` | True |""",
        "constraints": "",
        "hint": "Maintain two maps: `s -> t` and `t -> s`. Walk both strings in lockstep, checking that any existing mapping agrees.",
        "starter": """
def is_isomorphic(s: str, t: str) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def is_isomorphic(s: str, t: str) -> bool:
    \"\"\"Time: Θ(n).  Space: Θ(σ).\"\"\"
    if len(s) != len(t):
        return False
    fwd: dict[str, str] = {}
    rev: dict[str, str] = {}
    for a, b in zip(s, t):
        if a in fwd:
            if fwd[a] != b:
                return False
        else:
            if b in rev:
                return False
            fwd[a] = b
            rev[b] = a
    return True
""",
        "tests": """
import pytest

from solution import is_isomorphic


@pytest.mark.parametrize(
    "s, t, expected",
    [("egg", "add", True), ("foo", "bar", False), ("paper", "title", True), ("ab", "aa", False), ("", "", True)],
)
def test_examples(s, t, expected):
    assert is_isomorphic(s, t) == expected
""",
    },
    {
        "slug": "13-word-pattern",
        "title": "Word pattern",
        "difficulty": "easy",
        "tags": ["hash-map", "bijection"],
        "statement": "Given a `pattern` (string of letters) and `s` (string of space-separated words), return True if `s` follows the same pattern: each letter must correspond to exactly one word and vice-versa.",
        "signature": "def word_pattern(pattern: str, s: str) -> bool: ...",
        "examples_md": """## Examples

| pattern | s | result |
|---|---|---|
| `"abba"` | `"dog cat cat dog"` | True |
| `"abba"` | `"dog cat cat fish"` | False |
| `"aaaa"` | `"dog dog dog dog"` | True |""",
        "constraints": "",
        "hint": "Same bijection logic as `isomorphic-strings`, but with words on one side instead of characters.",
        "starter": """
def word_pattern(pattern: str, s: str) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False
    fwd: dict[str, str] = {}
    rev: dict[str, str] = {}
    for c, w in zip(pattern, words):
        if c in fwd:
            if fwd[c] != w:
                return False
        else:
            if w in rev:
                return False
            fwd[c] = w
            rev[w] = c
    return True
""",
        "tests": """
import pytest

from solution import word_pattern


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog dog dog dog", True),
        ("abba", "dog dog dog dog", False),
        ("aaa", "dog cat dog", False),
    ],
)
def test_examples(pattern, s, expected):
    assert word_pattern(pattern, s) == expected
""",
    },
    {
        "slug": "14-fraction-to-decimal",
        "title": "Fraction to recurring decimal",
        "difficulty": "medium",
        "tags": ["hash-map", "long-division"],
        "statement": "Given numerator and denominator, return the decimal expansion as a string. If the fractional part repeats, enclose the repeating part in parentheses.",
        "signature": "def fraction_to_decimal(numerator: int, denominator: int) -> str: ...",
        "examples_md": """## Examples

| n | d | result |
|---|---|---|
| 1 | 2 | `"0.5"` |
| 2 | 1 | `"2"` |
| 4 | 333 | `"0.(012)"` |
| -1 | -2147483648 | `"0.0000000004656612873077392578125"` |""",
        "constraints": "",
        "hint": "Long division.  Track remainders in a `dict[remainder, position_in_output]`. When a remainder repeats you've found the cycle start; insert `(` there and `)` at the end.",
        "starter": """
def fraction_to_decimal(numerator: int, denominator: int) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def fraction_to_decimal(numerator: int, denominator: int) -> str:
    \"\"\"Long division with remainder-seen map.

    Time:  Θ(d) where d is the period length (bounded by denominator).
    Space: Θ(d).
    \"\"\"
    if numerator == 0:
        return "0"
    sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
    n, d = abs(numerator), abs(denominator)
    integer, rem = divmod(n, d)
    if rem == 0:
        return sign + str(integer)
    out = [sign, str(integer), "."]
    seen: dict[int, int] = {}
    while rem and rem not in seen:
        seen[rem] = len(out)
        rem *= 10
        digit, rem = divmod(rem, d)
        out.append(str(digit))
    if rem:
        i = seen[rem]
        out.insert(i, "(")
        out.append(")")
    return "".join(out)
""",
        "tests": """
import pytest

from solution import fraction_to_decimal


@pytest.mark.parametrize(
    "n, d, expected",
    [
        (1, 2, "0.5"),
        (2, 1, "2"),
        (4, 333, "0.(012)"),
        (1, 3, "0.(3)"),
        (0, 5, "0"),
        (-1, 2, "-0.5"),
    ],
)
def test_examples(n, d, expected):
    assert fraction_to_decimal(n, d) == expected
""",
    },
    {
        "slug": "15-longest-substring-k-distinct",
        "title": "Longest substring with at most K distinct characters",
        "difficulty": "medium",
        "tags": ["sliding-window", "hash-map"],
        "statement": "Given a string `s` and integer `k`, return the length of the longest substring that contains at most `k` distinct characters.",
        "signature": "def longest_at_most_k(s: str, k: int) -> int: ...",
        "examples_md": """## Examples

| s | k | answer |
|---|---|---|
| `"eceba"` | 2 | 3 (`"ece"`) |
| `"aa"` | 1 | 2 |
| `"abcadcacacaca"` | 3 | 11 |""",
        "constraints": "",
        "hint": "Sliding window. Maintain a count map of characters in the window. While the window has more than k distinct chars, shrink from the left.",
        "starter": """
def longest_at_most_k(s: str, k: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import defaultdict


def longest_at_most_k(s: str, k: int) -> int:
    \"\"\"Variable-size sliding window.  Time: Θ(n).  Space: Θ(σ).\"\"\"
    if k <= 0:
        return 0
    counts: dict[str, int] = defaultdict(int)
    l = 0
    best = 0
    for r, ch in enumerate(s):
        counts[ch] += 1
        while len(counts) > k:
            counts[s[l]] -= 1
            if counts[s[l]] == 0:
                del counts[s[l]]
            l += 1
        if r - l + 1 > best:
            best = r - l + 1
    return best
""",
        "tests": """
import pytest

from solution import longest_at_most_k


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("eceba", 2, 3),
        ("aa", 1, 2),
        ("abcadcacacaca", 3, 11),
        ("", 2, 0),
        ("abc", 0, 0),
    ],
)
def test_examples(s, k, expected):
    assert longest_at_most_k(s, k) == expected
""",
    },
    {
        "slug": "16-substring-concatenation-words",
        "title": "Substring with concatenation of all words",
        "difficulty": "hard",
        "tags": ["sliding-window", "hash-map"],
        "statement": "Given a string `s` and a list of equal-length `words`, return the starting indices of substrings of `s` that are a concatenation of EACH word exactly once (any order, no in-between characters).",
        "signature": "def find_substring(s: str, words: list[str]) -> list[int]: ...",
        "examples_md": """## Examples

| s | words | result |
|---|---|---|
| `"barfoothefoobarman"` | `["foo","bar"]` | `[0, 9]` |
| `"wordgoodgoodgoodbestword"` | `["word","good","best","word"]` | `[]` |
| `"barfoofoobarthefoobarman"` | `["bar","foo","the"]` | `[6, 9, 12]` |""",
        "constraints": "",
        "hint": "Each word has length L. For each starting offset in [0, L), use a sliding window of L words. Maintain a counter; compare to `Counter(words)`.",
        "starter": """
def find_substring(s: str, words: list[str]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def find_substring(s: str, words: list[str]) -> list[int]:
    \"\"\"Word-level sliding window across L offsets.

    Time:  Θ(n * L) where L = len(words[0]).
    Space: Θ(k) where k = len(words).
    \"\"\"
    if not s or not words or not words[0]:
        return []
    L = len(words[0])
    k = len(words)
    target = Counter(words)
    n = len(s)
    out: list[int] = []
    for offset in range(L):
        l = offset
        count = 0
        window: Counter = Counter()
        for r in range(offset, n - L + 1, L):
            w = s[r : r + L]
            if w not in target:
                window.clear()
                count = 0
                l = r + L
                continue
            window[w] += 1
            count += 1
            while window[w] > target[w]:
                window[s[l : l + L]] -= 1
                l += L
                count -= 1
            if count == k:
                out.append(l)
    return out
""",
        "tests": """
import pytest

from solution import find_substring


def _norm(xs):
    return sorted(xs)


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ],
)
def test_examples(s, words, expected):
    assert _norm(find_substring(s, words)) == _norm(expected)
""",
    },
    {
        "slug": "17-bulls-and-cows",
        "title": "Bulls and cows",
        "difficulty": "medium",
        "tags": ["hash-map", "counter"],
        "statement": "Given a secret number and a guess (both digit strings of the same length), return `\"xAyB\"` where `x` is the count of digits that are in the right position (bulls) and `y` is the count of digits that are in the secret but in the wrong position (cows).",
        "signature": "def get_hint(secret: str, guess: str) -> str: ...",
        "examples_md": """## Examples

| secret | guess | result |
|---|---|---|
| `"1807"` | `"7810"` | `"1A3B"` |
| `"1123"` | `"0111"` | `"1A1B"` |""",
        "constraints": "",
        "hint": "One pass to count bulls. For the rest, count digits in both secret-minus-bulls and guess-minus-bulls and take the per-digit minimum.",
        "starter": """
def get_hint(secret: str, guess: str) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def get_hint(secret: str, guess: str) -> str:
    bulls = sum(s == g for s, g in zip(secret, guess))
    sc: Counter = Counter()
    gc: Counter = Counter()
    for s, g in zip(secret, guess):
        if s != g:
            sc[s] += 1
            gc[g] += 1
    cows = sum((sc & gc).values())
    return f"{bulls}A{cows}B"
""",
        "tests": """
import pytest

from solution import get_hint


@pytest.mark.parametrize(
    "secret, guess, expected",
    [
        ("1807", "7810", "1A3B"),
        ("1123", "0111", "1A1B"),
        ("1", "0", "0A0B"),
        ("1", "1", "1A0B"),
    ],
)
def test_examples(secret, guess, expected):
    assert get_hint(secret, guess) == expected
""",
    },
    {
        "slug": "18-rabbits-in-forest",
        "title": "Rabbits in the forest",
        "difficulty": "medium",
        "tags": ["hash-map", "counting"],
        "statement": "Each rabbit reports `answers[i]` — the number of OTHER rabbits with the same color. Return the minimum total number of rabbits in the forest consistent with the answers.",
        "signature": "def num_rabbits(answers: list[int]) -> int: ...",
        "examples_md": """## Examples

| answers | result |
|---|---|
| `[1, 1, 2]` | 5 |
| `[10, 10, 10]` | 11 |
| `[]` | 0 |""",
        "constraints": "",
        "hint": "Rabbits with answer `a` come in groups of size `a+1`. Count how many rabbits gave each answer `a`; ceil-divide by `a+1` to get the number of groups; multiply each group by `a+1` to get total rabbits.",
        "starter": """
def num_rabbits(answers: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def num_rabbits(answers: list[int]) -> int:
    \"\"\"Time: Θ(n).  Space: Θ(n).\"\"\"
    total = 0
    for a, cnt in Counter(answers).items():
        group_size = a + 1
        groups = -(-cnt // group_size)  # ceil division
        total += groups * group_size
    return total
""",
        "tests": """
import pytest

from solution import num_rabbits


@pytest.mark.parametrize(
    "answers, expected",
    [([1, 1, 2], 5), ([10, 10, 10], 11), ([], 0), ([0, 0, 1, 1, 1], 6)],
)
def test_examples(answers, expected):
    assert num_rabbits(answers) == expected
""",
    },
]
