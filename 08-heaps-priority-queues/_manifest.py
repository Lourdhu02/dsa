"""Module 08 (heaps & priority queues) manifest."""

PROBLEMS = [
    {
        "slug": "01-heap-sort",
        "title": "Heap sort",
        "difficulty": "easy",
        "tags": ["heap"],
        "statement": "Sort an integer array in place using heap sort. Don't call any library sort.",
        "signature": "def heap_sort(nums: list[int]) -> None: ...",
        "examples_md": """## Examples

| input | sorted |
|---|---|
| `[3, 1, 4, 1, 5, 9, 2, 6]` | `[1, 1, 2, 3, 4, 5, 6, 9]` |""",
        "constraints": "",
        "hint": "Build a max-heap in place (Θ(n)). Then repeatedly swap the root with the last element and sift down on the shrinking prefix.",
        "starter": """
def heap_sort(nums: list[int]) -> None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
def heap_sort(nums: list[int]) -> None:
    \"\"\"Time: Θ(n log n).  Space: Θ(1).\"\"\"
    n = len(nums)

    def _sift_down(start, end):
        i = start
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < end and nums[l] > nums[largest]:
                largest = l
            if r < end and nums[r] > nums[largest]:
                largest = r
            if largest == i:
                return
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest

    for i in range(n // 2 - 1, -1, -1):
        _sift_down(i, n)
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        _sift_down(0, end)
""",
        "tests": """
import pytest
import random
from solution import heap_sort


def test_basic():
    a = [3, 1, 4, 1, 5, 9, 2, 6]
    heap_sort(a)
    assert a == sorted([3, 1, 4, 1, 5, 9, 2, 6])


def test_random():
    rng = random.Random(0)
    for _ in range(10):
        a = [rng.randint(-50, 50) for _ in range(rng.randint(0, 100))]
        expected = sorted(a)
        heap_sort(a)
        assert a == expected
""",
    },
    {
        "slug": "02-kth-largest-element",
        "title": "Kth largest element in array",
        "difficulty": "medium",
        "tags": ["heap", "top-k"],
        "statement": "Return the kth largest element in an unsorted array.",
        "signature": "def find_kth_largest(nums: list[int], k: int) -> int: ...",
        "examples_md": """## Examples

| nums | k | result |
|---|---|---|
| `[3, 2, 1, 5, 6, 4]` | 2 | 5 |
| `[3, 2, 3, 1, 2, 4, 5, 5, 6]` | 4 | 4 |""",
        "constraints": "",
        "hint": "Maintain a min-heap of size k. Push each element; if size > k, pop. Final heap[0] is the answer. Θ(n log k).",
        "starter": """
def find_kth_largest(nums: list[int], k: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    \"\"\"Time: Θ(n log k).  Space: Θ(k).\"\"\"
    h: list[int] = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
""",
        "tests": """
import pytest
from solution import find_kth_largest


@pytest.mark.parametrize(
    "nums, k, expected",
    [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4), ([1], 1, 1)],
)
def test_examples(nums, k, expected):
    assert find_kth_largest(nums, k) == expected
""",
    },
    {
        "slug": "03-top-k-frequent",
        "title": "Top K frequent elements (heap)",
        "difficulty": "medium",
        "tags": ["heap", "counter"],
        "statement": "Return the k most frequent elements of `nums`. (Same problem as module 02 problem 09 but solve with a heap.)",
        "signature": "def top_k_frequent(nums: list[int], k: int) -> list[int]: ...",
        "examples_md": """## Examples

| nums | k | result (any order) |
|---|---|---|
| `[1, 1, 1, 2, 2, 3]` | 2 | `[1, 2]` |""",
        "constraints": "",
        "hint": "Counter, then nlargest by frequency.",
        "starter": """
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return [v for v, _ in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]
""",
        "tests": """
import pytest
from solution import top_k_frequent


@pytest.mark.parametrize(
    "nums, k, expected",
    [([1, 1, 1, 2, 2, 3], 2, {1, 2}), ([1], 1, {1}), ([4, 4, 5, 6, 6], 2, {4, 6})],
)
def test_examples(nums, k, expected):
    assert set(top_k_frequent(nums, k)) == expected
""",
    },
    {
        "slug": "04-kth-largest-stream",
        "title": "Kth largest in stream",
        "difficulty": "easy",
        "tags": ["heap", "design"],
        "statement": "Design `KthLargest(k, nums)` with `add(val) -> int` returning the kth largest element seen so far.",
        "signature": "class KthLargest:\n    def __init__(self, k: int, nums: list[int]) -> None: ...\n    def add(self, val: int) -> int: ...",
        "examples_md": """## Examples

```
k = 3, nums = [4, 5, 8, 2]
add(3) -> 4
add(5) -> 5
add(10) -> 5
add(9) -> 8
add(4) -> 8
```""",
        "constraints": "",
        "hint": "Maintain a min-heap of size k. On add, push and trim. Top is the kth largest.",
        "starter": """
class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        raise NotImplementedError

    def add(self, val: int) -> int:
        raise NotImplementedError
""",
        "reference": """
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.h: list[int] = []
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]
""",
        "tests": """
from solution import KthLargest


def test_classic_sequence():
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4
    assert kl.add(5) == 5
    assert kl.add(10) == 5
    assert kl.add(9) == 8
    assert kl.add(4) == 8
""",
    },
    {
        "slug": "05-last-stone-weight",
        "title": "Last stone weight",
        "difficulty": "easy",
        "tags": ["heap"],
        "statement": "Repeatedly take the two heaviest stones, smash them. If equal, both destroyed. Otherwise the difference replaces them. Return the weight of the last remaining stone, or 0 if none.",
        "signature": "def last_stone_weight(stones: list[int]) -> int: ...",
        "examples_md": """## Examples

| stones | result |
|---|---|
| `[2, 7, 4, 1, 8, 1]` | 1 |
| `[1]` | 1 |
| `[3, 3]` | 0 |""",
        "constraints": "",
        "hint": "Max-heap via negation.",
        "starter": """
def last_stone_weight(stones: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def last_stone_weight(stones: list[int]) -> int:
    h = [-s for s in stones]
    heapq.heapify(h)
    while len(h) > 1:
        a = -heapq.heappop(h)
        b = -heapq.heappop(h)
        if a != b:
            heapq.heappush(h, -(a - b))
    return -h[0] if h else 0
""",
        "tests": """
import pytest
from solution import last_stone_weight


@pytest.mark.parametrize(
    "stones, expected",
    [([2, 7, 4, 1, 8, 1], 1), ([1], 1), ([3, 3], 0), ([2, 2, 1], 1)],
)
def test_examples(stones, expected):
    assert last_stone_weight(stones) == expected
""",
    },
    {
        "slug": "06-k-closest-points-origin",
        "title": "K closest points to origin",
        "difficulty": "medium",
        "tags": ["heap", "top-k"],
        "statement": "Return the k points in `points` closest to the origin by Euclidean distance.",
        "signature": "def k_closest(points: list[list[int]], k: int) -> list[list[int]]: ...",
        "examples_md": """## Examples

| points | k | result |
|---|---|---|
| `[[1, 3], [-2, 2]]` | 1 | `[[-2, 2]]` |
| `[[3, 3], [5, -1], [-2, 4]]` | 2 | `[[3, 3], [-2, 4]]` |""",
        "constraints": "",
        "hint": "Max-heap of size k keyed by squared distance.",
        "starter": """
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    h: list[tuple[int, list[int]]] = []
    for p in points:
        d = p[0] * p[0] + p[1] * p[1]
        if len(h) < k:
            heapq.heappush(h, (-d, p))
        elif -d > h[0][0]:
            heapq.heapreplace(h, (-d, p))
    return [p for _, p in h]
""",
        "tests": """
import pytest
from solution import k_closest


def _sq_dists(points):
    return sorted(p[0] ** 2 + p[1] ** 2 for p in points)


@pytest.mark.parametrize(
    "points, k",
    [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
    ],
)
def test_distance_sets_match(points, k):
    result = k_closest(points, k)
    assert len(result) == k
    # Closest k distances should match
    all_dists = sorted(p[0] ** 2 + p[1] ** 2 for p in points)[:k]
    assert _sq_dists(result) == all_dists
""",
    },
    {
        "slug": "07-merge-k-sorted-lists",
        "title": "Merge k sorted lists",
        "difficulty": "hard",
        "tags": ["heap", "k-way-merge"],
        "statement": "Given `k` sorted linked lists, merge them into one sorted linked list and return its head.",
        "signature": "class ListNode: ...\n\ndef merge_k_lists(lists: list[ListNode | None]) -> ListNode | None: ...",
        "examples_md": """## Examples

```
input: [[1,4,5],[1,3,4],[2,6]]
output: 1->1->2->3->4->4->5->6
```""",
        "constraints": "",
        "hint": "Min-heap of (value, list_idx, node). Pop the smallest, advance that list.",
        "starter": """
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    \"\"\"Time: Θ(N log k).  Space: Θ(k).\"\"\"
    h: list[tuple[int, int, ListNode]] = []
    for i, head in enumerate(lists):
        if head is not None:
            heapq.heappush(h, (head.val, i, head))
    sentinel = ListNode()
    tail = sentinel
    while h:
        val, i, node = heapq.heappop(h)
        tail.next = node
        tail = node
        if node.next is not None:
            heapq.heappush(h, (node.next.val, i, node.next))
    tail.next = None
    return sentinel.next
""",
        "tests": """
from solution import ListNode, merge_k_lists


def _build(xs):
    head = None
    for v in reversed(xs):
        head = ListNode(v, head)
    return head


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_basic():
    lists = [_build([1, 4, 5]), _build([1, 3, 4]), _build([2, 6])]
    assert _to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_empty_lists():
    assert merge_k_lists([]) is None
    assert merge_k_lists([None, None]) is None
""",
    },
    {
        "slug": "08-find-median-stream",
        "title": "Find median from stream",
        "difficulty": "hard",
        "tags": ["heap", "two-heaps", "design"],
        "statement": "Design `MedianFinder.add_num(num)` (Θ(log n)) and `find_median() -> float` (Θ(1)) that maintains the running median of all numbers added so far.",
        "signature": "class MedianFinder:\n    def add_num(self, num: int) -> None: ...\n    def find_median(self) -> float: ...",
        "examples_md": """## Examples

```
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
mf.find_median()   # 1.5
mf.add_num(3)
mf.find_median()   # 2
```""",
        "constraints": "",
        "hint": "Two heaps: max-heap `lo` and min-heap `hi`. Keep sizes balanced within 1.",
        "starter": """
class MedianFinder:
    def __init__(self) -> None:
        raise NotImplementedError

    def add_num(self, num: int) -> None:
        raise NotImplementedError

    def find_median(self) -> float:
        raise NotImplementedError
""",
        "reference": """
import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.lo: list[int] = []  # max-heap (negated)
        self.hi: list[int] = []  # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2
""",
        "tests": """
from solution import MedianFinder


def test_basic_sequence():
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2


def test_single():
    mf = MedianFinder()
    mf.add_num(5)
    assert mf.find_median() == 5
""",
    },
    {
        "slug": "09-ugly-number-ii",
        "title": "Ugly number II",
        "difficulty": "medium",
        "tags": ["heap", "dp-alternative"],
        "statement": "An *ugly number* has only prime factors 2, 3, 5. Return the `n`-th ugly number (1-indexed; 1 is ugly).",
        "signature": "def nth_ugly(n: int) -> int: ...",
        "examples_md": """## Examples

| n | ugly[n] |
|---|---|
| 1 | 1 |
| 10 | 12 |
| 11 | 15 |""",
        "constraints": "",
        "hint": "Min-heap starting with 1. Pop smallest, push that times 2, 3, 5. Dedupe via a set.",
        "starter": """
def nth_ugly(n: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def nth_ugly(n: int) -> int:
    h = [1]
    seen = {1}
    cur = 1
    for _ in range(n):
        cur = heapq.heappop(h)
        for p in (2, 3, 5):
            nxt = cur * p
            if nxt not in seen:
                seen.add(nxt)
                heapq.heappush(h, nxt)
    return cur
""",
        "tests": """
import pytest
from solution import nth_ugly


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (10, 12), (11, 15), (1690, 2123366400)]
)
def test_examples(n, expected):
    assert nth_ugly(n) == expected
""",
    },
    {
        "slug": "10-furthest-building",
        "title": "Furthest building you can reach",
        "difficulty": "medium",
        "tags": ["heap", "greedy"],
        "statement": "Given `heights`, `bricks`, and `ladders`, jump from building 0 forward. Going down is free. Going up by `h` costs either `h` bricks or 1 ladder. Return the furthest building index you can reach.",
        "signature": "def furthest_building(heights: list[int], bricks: int, ladders: int) -> int: ...",
        "examples_md": """## Examples

| heights | bricks | ladders | result |
|---|---|---|---|
| `[4, 2, 7, 6, 9, 14, 12]` | 5 | 1 | 4 |
| `[14, 3, 19, 3]` | 17 | 0 | 3 |""",
        "constraints": "",
        "hint": "Use ladders for the largest jumps; bricks for the rest. Maintain a min-heap of size `ladders` of recent jumps; whenever bigger than top, replace and spend bricks on the popped one.",
        "starter": """
def furthest_building(heights: list[int], bricks: int, ladders: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def furthest_building(heights: list[int], bricks: int, ladders: int) -> int:
    h: list[int] = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        heapq.heappush(h, diff)
        if len(h) > ladders:
            bricks -= heapq.heappop(h)
            if bricks < 0:
                return i
    return len(heights) - 1
""",
        "tests": """
import pytest
from solution import furthest_building


@pytest.mark.parametrize(
    "heights, bricks, ladders, expected",
    [([4, 2, 7, 6, 9, 14, 12], 5, 1, 4), ([14, 3, 19, 3], 17, 0, 3)],
)
def test_examples(heights, bricks, ladders, expected):
    assert furthest_building(heights, bricks, ladders) == expected
""",
    },
    {
        "slug": "11-reorganize-string",
        "title": "Reorganize string",
        "difficulty": "medium",
        "tags": ["heap", "greedy"],
        "statement": "Rearrange the characters of `s` so that no two adjacent characters are equal. Return any valid result, or `\"\"` if impossible.",
        "signature": "def reorganize_string(s: str) -> str: ...",
        "examples_md": """## Examples

| s | possible result |
|---|---|
| `\"aab\"` | `\"aba\"` |
| `\"aaab\"` | `\"\"` |""",
        "constraints": "",
        "hint": "Max-heap by frequency. Always emit the most-frequent letter that is NOT equal to the previous emitted letter.",
        "starter": """
def reorganize_string(s: str) -> str:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq
from collections import Counter


def reorganize_string(s: str) -> str:
    counts = Counter(s)
    if max(counts.values()) > (len(s) + 1) // 2:
        return ""
    h = [(-c, ch) for ch, c in counts.items()]
    heapq.heapify(h)
    out: list[str] = []
    prev_c, prev_ch = 0, ""
    while h:
        c, ch = heapq.heappop(h)
        out.append(ch)
        if prev_c < 0:
            heapq.heappush(h, (prev_c, prev_ch))
        prev_c, prev_ch = c + 1, ch
    return "".join(out)
""",
        "tests": """
from solution import reorganize_string


def _valid(s, t):
    if not t:
        return False
    from collections import Counter
    if Counter(s) != Counter(t):
        return False
    return all(t[i] != t[i + 1] for i in range(len(t) - 1))


def test_possible():
    s = "aab"
    out = reorganize_string(s)
    assert _valid(s, out)


def test_impossible():
    assert reorganize_string("aaab") == ""
""",
    },
    {
        "slug": "12-task-scheduler",
        "title": "Task scheduler",
        "difficulty": "medium",
        "tags": ["heap", "greedy"],
        "statement": "Given a list of CPU tasks and integer `n`, return the minimum number of time units to finish all tasks where the same task must be `n` units apart.",
        "signature": "def least_interval(tasks: list[str], n: int) -> int: ...",
        "examples_md": """## Examples

| tasks | n | result |
|---|---|---|
| `[\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"]` | 2 | 8 |
| `[\"A\",\"C\",\"A\",\"B\",\"D\",\"B\"]` | 1 | 6 |""",
        "constraints": "",
        "hint": "Closed-form: `max(len(tasks), (max_count - 1) * (n + 1) + tied_max)` — derivation in CP-algorithms.",
        "starter": """
def least_interval(tasks: list[str], n: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
from collections import Counter


def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_count = max(counts.values())
    tied = sum(1 for c in counts.values() if c == max_count)
    return max(len(tasks), (max_count - 1) * (n + 1) + tied)
""",
        "tests": """
import pytest
from solution import least_interval


@pytest.mark.parametrize(
    "tasks, n, expected",
    [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "D", "B"], 1, 6),
        (["A"], 0, 1),
    ],
)
def test_examples(tasks, n, expected):
    assert least_interval(tasks, n) == expected
""",
    },
    {
        "slug": "13-ipo",
        "title": "IPO (max capital projects)",
        "difficulty": "hard",
        "tags": ["heap", "greedy"],
        "statement": "Pick at most `k` projects starting with `w` capital. Each project `i` needs `capital[i]` to start and adds `profits[i]` to your capital. Return the maximum capital after at most k projects.",
        "signature": "def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int: ...",
        "examples_md": """## Examples

| k | w | profits | capital | result |
|---|---|---|---|---|
| 2 | 0 | `[1, 2, 3]` | `[0, 1, 1]` | 4 |
| 3 | 0 | `[1, 2, 3]` | `[0, 1, 2]` | 6 |""",
        "constraints": "",
        "hint": "Two heaps: a min-heap of (capital, profit) for not-yet-affordable projects; a max-heap of profits for affordable ones. Each round: move newly affordable to max-heap, take its top.",
        "starter": """
def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    by_cap = sorted(zip(capital, profits))
    affordable: list[int] = []
    i = 0
    for _ in range(k):
        while i < len(by_cap) and by_cap[i][0] <= w:
            heapq.heappush(affordable, -by_cap[i][1])
            i += 1
        if not affordable:
            break
        w += -heapq.heappop(affordable)
    return w
""",
        "tests": """
import pytest
from solution import find_maximized_capital


@pytest.mark.parametrize(
    "k, w, profits, capital, expected",
    [(2, 0, [1, 2, 3], [0, 1, 1], 4), (3, 0, [1, 2, 3], [0, 1, 2], 6)],
)
def test_examples(k, w, profits, capital, expected):
    assert find_maximized_capital(k, w, profits, capital) == expected
""",
    },
    {
        "slug": "14-minimum-cost-connect-ropes",
        "title": "Minimum cost to connect ropes",
        "difficulty": "easy",
        "tags": ["heap", "greedy"],
        "statement": "Connect `n` ropes into one. Connecting two ropes of lengths `a` and `b` costs `a + b`. Return the minimum total cost.",
        "signature": "def connect_ropes(ropes: list[int]) -> int: ...",
        "examples_md": """## Examples

| ropes | cost |
|---|---|
| `[1, 2, 3, 4, 5]` | 33 |
| `[4, 3, 2, 6]` | 29 |""",
        "constraints": "",
        "hint": "Always connect the two shortest. Min-heap.",
        "starter": """
def connect_ropes(ropes: list[int]) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def connect_ropes(ropes: list[int]) -> int:
    h = ropes[:]
    heapq.heapify(h)
    total = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        total += a + b
        heapq.heappush(h, a + b)
    return total
""",
        "tests": """
import pytest
from solution import connect_ropes


@pytest.mark.parametrize(
    "ropes, expected",
    [([1, 2, 3, 4, 5], 33), ([4, 3, 2, 6], 29), ([1], 0), ([], 0)],
)
def test_examples(ropes, expected):
    assert connect_ropes(ropes) == expected
""",
    },
    {
        "slug": "15-find-k-pairs-smallest-sums",
        "title": "Find K pairs with smallest sums",
        "difficulty": "medium",
        "tags": ["heap", "k-way-merge"],
        "statement": "Given two sorted arrays `nums1` and `nums2`, return the `k` pairs `(a, b)` with `a in nums1, b in nums2` having the smallest sums.",
        "signature": "def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]: ...",
        "examples_md": """## Examples

| nums1 | nums2 | k | result |
|---|---|---|---|
| `[1, 7, 11]` | `[2, 4, 6]` | 3 | `[[1, 2], [1, 4], [1, 6]]` |""",
        "constraints": "",
        "hint": "Heap of (sum, i, j) seeded with j=0 for each i. Pop, push (i, j+1). Or seed with one row and expand.",
        "starter": """
def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    if not nums1 or not nums2 or k <= 0:
        return []
    h: list[tuple[int, int, int]] = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(h, (nums1[i] + nums2[0], i, 0))
    out: list[list[int]] = []
    while h and len(out) < k:
        s, i, j = heapq.heappop(h)
        out.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
    return out
""",
        "tests": """
import pytest
from solution import k_smallest_pairs


def test_basic():
    res = k_smallest_pairs([1, 7, 11], [2, 4, 6], 3)
    assert sorted(map(tuple, res)) == sorted([(1, 2), (1, 4), (1, 6)])


def test_k_larger_than_pairs():
    res = k_smallest_pairs([1, 2], [3], 10)
    assert sorted(map(tuple, res)) == sorted([(1, 3), (2, 3)])
""",
    },
    {
        "slug": "16-smallest-range-k-lists",
        "title": "Smallest range covering elements from k lists",
        "difficulty": "hard",
        "tags": ["heap", "k-way-merge"],
        "statement": "Given `k` sorted lists of integers, find the smallest range `[a, b]` that includes at least one number from each list.",
        "signature": "def smallest_range(nums: list[list[int]]) -> list[int]: ...",
        "examples_md": """## Examples

| nums | result |
|---|---|
| `[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]` | `[20, 24]` |""",
        "constraints": "",
        "hint": "Heap of one pointer per list. Track running max. After each pop, update range and advance the popped list's pointer.",
        "starter": """
def smallest_range(nums: list[list[int]]) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq


def smallest_range(nums: list[list[int]]) -> list[int]:
    h: list[tuple[int, int, int]] = []
    cur_max = float("-inf")
    for i, lst in enumerate(nums):
        heapq.heappush(h, (lst[0], i, 0))
        cur_max = max(cur_max, lst[0])
    best: list[int] = [-10**9, 10**9]
    while h:
        v, i, j = heapq.heappop(h)
        if cur_max - v < best[1] - best[0]:
            best = [v, cur_max]
        if j + 1 == len(nums[i]):
            break
        nxt = nums[i][j + 1]
        cur_max = max(cur_max, nxt)
        heapq.heappush(h, (nxt, i, j + 1))
    return best
""",
        "tests": """
import pytest
from solution import smallest_range


def test_basic():
    assert smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]


def test_singletons():
    assert smallest_range([[1], [2], [3]]) == [1, 3]
""",
    },
    {
        "slug": "17-design-twitter",
        "title": "Design Twitter feed",
        "difficulty": "medium",
        "tags": ["heap", "design"],
        "statement": "Implement `Twitter` with `post_tweet(user_id, tweet_id)`, `get_news_feed(user_id) -> list[int]` (10 most recent tweets from the user + followees, newest first), `follow(a, b)`, `unfollow(a, b)`.",
        "signature": "class Twitter:\n    def post_tweet(self, user_id: int, tweet_id: int) -> None: ...\n    def get_news_feed(self, user_id: int) -> list[int]: ...\n    def follow(self, a: int, b: int) -> None: ...\n    def unfollow(self, a: int, b: int) -> None: ...",
        "examples_md": """## Examples

```
t = Twitter()
t.post_tweet(1, 5)
t.get_news_feed(1)   # [5]
t.follow(1, 2)
t.post_tweet(2, 6)
t.get_news_feed(1)   # [6, 5]
t.unfollow(1, 2)
t.get_news_feed(1)   # [5]
```""",
        "constraints": "",
        "hint": "Per-user list of (timestamp, tweet_id). Get_feed: merge user's + followees' streams with a heap, take 10.",
        "starter": """
class Twitter:
    def __init__(self) -> None:
        raise NotImplementedError

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        raise NotImplementedError

    def get_news_feed(self, user_id: int) -> list[int]:
        raise NotImplementedError

    def follow(self, a: int, b: int) -> None:
        raise NotImplementedError

    def unfollow(self, a: int, b: int) -> None:
        raise NotImplementedError
""",
        "reference": """
import heapq
from collections import defaultdict


class Twitter:
    def __init__(self) -> None:
        self._tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self._follow: dict[int, set[int]] = defaultdict(set)
        self._t = 0

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self._t += 1
        self._tweets[user_id].append((self._t, tweet_id))

    def get_news_feed(self, user_id: int) -> list[int]:
        users = self._follow[user_id] | {user_id}
        h: list[tuple[int, int]] = []  # (-timestamp, tweet_id)
        for u in users:
            for t, tid in self._tweets[u][-10:]:
                heapq.heappush(h, (-t, tid))
        out: list[int] = []
        for _ in range(10):
            if not h:
                break
            out.append(heapq.heappop(h)[1])
        return out

    def follow(self, a: int, b: int) -> None:
        if a != b:
            self._follow[a].add(b)

    def unfollow(self, a: int, b: int) -> None:
        self._follow[a].discard(b)
""",
        "tests": """
from solution import Twitter


def test_classic_flow():
    t = Twitter()
    t.post_tweet(1, 5)
    assert t.get_news_feed(1) == [5]
    t.follow(1, 2)
    t.post_tweet(2, 6)
    assert t.get_news_feed(1) == [6, 5]
    t.unfollow(1, 2)
    assert t.get_news_feed(1) == [5]
""",
    },
    {
        "slug": "18-sliding-window-median",
        "title": "Sliding window median",
        "difficulty": "hard",
        "tags": ["heap", "two-heaps", "sliding-window"],
        "statement": "Given an array `nums` and window size `k`, return the median of every length-k contiguous window.",
        "signature": "def median_sliding_window(nums: list[int], k: int) -> list[float]: ...",
        "examples_md": """## Examples

| nums | k | result |
|---|---|---|
| `[1, 3, -1, -3, 5, 3, 6, 7]` | 3 | `[1, -1, -1, 3, 5, 6]` |""",
        "constraints": "",
        "hint": "Two heaps as in median-from-stream, plus a delayed-removal map (since heap removal is Θ(n)). Lazy delete: track removed elements; pop from heap if top is removed.",
        "starter": """
def median_sliding_window(nums: list[int], k: int) -> list[float]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
import heapq
from collections import defaultdict


def median_sliding_window(nums: list[int], k: int) -> list[float]:
    \"\"\"Two heaps with lazy deletion.  Time: Θ(n log k).\"\"\"
    lo: list[int] = []  # max-heap, negated
    hi: list[int] = []  # min-heap
    removed: dict[int, int] = defaultdict(int)
    lo_size = hi_size = 0

    def _balance():
        # Ensure |lo| - |hi| in {0, 1}.
        nonlocal lo_size, hi_size
        while lo_size > hi_size + 1:
            v = -heapq.heappop(lo)
            heapq.heappush(hi, v)
            lo_size -= 1
            hi_size += 1
            while lo and removed[-lo[0]] > 0:
                removed[-lo[0]] -= 1
                heapq.heappop(lo)
        while hi_size > lo_size:
            v = heapq.heappop(hi)
            heapq.heappush(lo, -v)
            hi_size -= 1
            lo_size += 1
            while hi and removed[hi[0]] > 0:
                removed[hi[0]] -= 1
                heapq.heappop(hi)

    def _prune_tops():
        while lo and removed[-lo[0]] > 0:
            removed[-lo[0]] -= 1
            heapq.heappop(lo)
        while hi and removed[hi[0]] > 0:
            removed[hi[0]] -= 1
            heapq.heappop(hi)

    def _median():
        _prune_tops()
        if k % 2 == 1:
            return float(-lo[0])
        return (-lo[0] + hi[0]) / 2.0

    out: list[float] = []
    for i, x in enumerate(nums):
        if not lo or x <= -lo[0]:
            heapq.heappush(lo, -x)
            lo_size += 1
        else:
            heapq.heappush(hi, x)
            hi_size += 1
        _balance()
        if i >= k:
            old = nums[i - k]
            removed[old] += 1
            if old <= -lo[0]:
                lo_size -= 1
            else:
                hi_size -= 1
            _balance()
        if i >= k - 1:
            out.append(_median())
    return out
""",
        "tests": """
import pytest
from solution import median_sliding_window


def test_basic():
    assert median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1, -1, -1, 3, 5, 6]


def test_window_size_1():
    assert median_sliding_window([1, 2, 3, 4], 1) == [1, 2, 3, 4]
""",
    },
]
