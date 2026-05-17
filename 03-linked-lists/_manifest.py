"""Module 03 (linked lists) problem manifest."""

# Small helpers reused inside reference solutions are imported at runtime; the
# generator copies the `reference` string verbatim into each problem's
# reference.py, so any imports it needs must be in that string.

PROBLEMS = [
    {
        "slug": "01-print-linked-list",
        "title": "Build and print a linked list",
        "difficulty": "easy",
        "tags": ["intro", "linked-list"],
        "statement": "Given a Python list `xs`, build a singly-linked list with those values and return the head. Then implement `to_list(head)` that materializes a linked list as a Python list. Both must run in `Θ(n)` time.",
        "signature": "class ListNode:\n    def __init__(self, val=0, next=None): ...\n\ndef build(xs: list[int]) -> ListNode | None: ...\ndef to_list(head: ListNode | None) -> list[int]: ...",
        "examples_md": """## Examples

| xs | to_list(build(xs)) |
|---|---|
| `[]` | `[]` |
| `[1, 2, 3]` | `[1, 2, 3]` |""",
        "constraints": "",
        "hint": "Walk `xs` left to right, maintaining a tail pointer so each append is Θ(1).",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build(xs: list[int]) -> ListNode | None:
    # TODO
    raise NotImplementedError


def to_list(head: ListNode | None) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build(xs: list[int]) -> ListNode | None:
    \"\"\"Time: Θ(n).  Space: Θ(n).\"\"\"
    head: ListNode | None = None
    tail: ListNode | None = None
    for v in xs:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return head


def to_list(head: ListNode | None) -> list[int]:
    \"\"\"Time: Θ(n).  Space: Θ(n) for the output.\"\"\"
    out: list[int] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out
""",
        "tests": """
import pytest

from solution import build, to_list


@pytest.mark.parametrize("xs", [[], [1], [1, 2, 3], list(range(50))])
def test_roundtrip(xs):
    assert to_list(build(xs)) == xs
""",
    },
    {
        "slug": "02-reverse-list",
        "title": "Reverse a linked list",
        "difficulty": "easy",
        "tags": ["pointer-manipulation", "in-place"],
        "statement": "Given the head of a singly-linked list, reverse the list in place and return the new head. `Θ(n)` time, `Θ(1)` extra space.",
        "signature": "def reverse_list(head: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

| input | output |
|---|---|
| `1 -> 2 -> 3 -> 4 -> 5` | `5 -> 4 -> 3 -> 2 -> 1` |
| `1 -> 2` | `2 -> 1` |
| `[]` | `[]` |""",
        "constraints": "",
        "hint": "Three pointers: `prev=None, curr=head`. On each step, save `nxt = curr.next`, set `curr.next = prev`, advance `prev = curr; curr = nxt`.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    \"\"\"Time: Θ(n).  Space: Θ(1).\"\"\"
    prev: ListNode | None = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
""",
        "tests": """
import pytest

from solution import ListNode, reverse_list


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


@pytest.mark.parametrize(
    "xs, expected",
    [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2], [2, 1]), ([], []), ([7], [7])],
)
def test_reverse(xs, expected):
    assert _to_list(reverse_list(_build(xs))) == expected
""",
    },
    {
        "slug": "03-merge-two-sorted-lists",
        "title": "Merge two sorted lists",
        "difficulty": "easy",
        "tags": ["two-pointer", "linked-list"],
        "statement": "Merge two sorted singly-linked lists into one sorted list. Return the new head.",
        "signature": "def merge_two_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

| a | b | merged |
|---|---|---|
| `1->2->4` | `1->3->4` | `1->1->2->3->4->4` |
| `[]` | `[]` | `[]` |
| `[]` | `0` | `0` |""",
        "constraints": "",
        "hint": "Sentinel head + tail pointer; walk both lists picking the smaller; append the remainder.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    \"\"\"Time: Θ(n + m).  Space: Θ(1) auxiliary.\"\"\"
    sentinel = ListNode()
    tail = sentinel
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return sentinel.next
""",
        "tests": """
import pytest

from solution import ListNode, merge_two_lists


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


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1, 5, 9], [2, 4, 6, 7], [1, 2, 4, 5, 6, 7, 9]),
    ],
)
def test_examples(a, b, expected):
    assert _to_list(merge_two_lists(_build(a), _build(b))) == expected
""",
    },
    {
        "slug": "04-linked-list-cycle",
        "title": "Linked list cycle detection",
        "difficulty": "easy",
        "tags": ["fast-slow-pointer", "floyd"],
        "statement": "Given the head of a linked list, return `True` if the list contains a cycle, else `False`. Run in `Θ(n)` time, `Θ(1)` extra space.",
        "signature": "def has_cycle(head: ListNode | None) -> bool: ...",
        "examples_md": """## Examples

```
1 -> 2 -> 3 -> 4
          ^---------+
                    |
                  (4.next = 2)
```

Has a cycle starting at 2.""",
        "constraints": "",
        "hint": "Floyd's tortoise and hare. Slow moves 1 step, fast moves 2. If they meet, there's a cycle. If fast hits None, there isn't.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    \"\"\"Floyd's algorithm.  Time: Θ(n).  Space: Θ(1).\"\"\"
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            return True
    return False
""",
        "tests": """
from solution import ListNode, has_cycle


def _build_with_cycle(xs, pos):
    if not xs:
        return None
    nodes = [ListNode(v) for v in xs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def test_no_cycle():
    assert has_cycle(_build_with_cycle([1, 2, 3, 4, 5], -1)) is False


def test_cycle_at_head():
    assert has_cycle(_build_with_cycle([1, 2, 3], 0)) is True


def test_cycle_in_middle():
    assert has_cycle(_build_with_cycle([1, 2, 3, 4, 5], 2)) is True


def test_empty():
    assert has_cycle(None) is False
""",
    },
    {
        "slug": "05-find-cycle-start",
        "title": "Find cycle start",
        "difficulty": "medium",
        "tags": ["fast-slow-pointer", "floyd"],
        "statement": "If the linked list has a cycle, return the node where the cycle begins, else return `None`. Run in `Θ(n)` time, `Θ(1)` extra space.",
        "signature": "def detect_cycle(head: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

Same shape as problem 04 but return the cycle-entry node, not a bool.""",
        "constraints": "",
        "hint": "After Floyd detects a meeting point inside the cycle, restart one pointer at `head` and advance both by 1 step. They meet at the cycle entrance.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def detect_cycle(head: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def detect_cycle(head: ListNode | None) -> ListNode | None:
    \"\"\"Floyd cycle-find with phase-2 entry locator.

    Time:  Θ(n).  Space: Θ(1).
    Proof: see lesson README §2.
    \"\"\"
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p = p.next  # type: ignore[union-attr]
                slow = slow.next  # type: ignore[union-attr]
            return p
    return None
""",
        "tests": """
from solution import ListNode, detect_cycle


def _build(xs, pos):
    if not xs:
        return None, None
    nodes = [ListNode(v) for v in xs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    cycle_node = None
    if pos >= 0:
        nodes[-1].next = nodes[pos]
        cycle_node = nodes[pos]
    return nodes[0], cycle_node


def test_no_cycle():
    head, _ = _build([1, 2, 3], -1)
    assert detect_cycle(head) is None


def test_cycle_in_middle():
    head, cycle_node = _build([3, 2, 0, -4], 1)
    assert detect_cycle(head) is cycle_node


def test_self_loop():
    head, cycle_node = _build([1], 0)
    assert detect_cycle(head) is cycle_node


def test_empty():
    assert detect_cycle(None) is None
""",
    },
    {
        "slug": "06-middle-of-linked-list",
        "title": "Middle of the linked list",
        "difficulty": "easy",
        "tags": ["fast-slow-pointer"],
        "statement": "Return the middle node of a singly-linked list. If there are two middle nodes (even length), return the second.",
        "signature": "def middle_node(head: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

| input | result |
|---|---|
| `1->2->3->4->5` | node with value 3 |
| `1->2->3->4->5->6` | node with value 4 |""",
        "constraints": "",
        "hint": "Fast/slow. Slow moves 1, fast moves 2. When fast reaches end, slow is the middle.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def middle_node(head: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def middle_node(head: ListNode | None) -> ListNode | None:
    \"\"\"Time: Θ(n).  Space: Θ(1).\"\"\"
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
    return slow
""",
        "tests": """
import pytest

from solution import ListNode, middle_node


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


@pytest.mark.parametrize(
    "xs, expected_tail",
    [([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6]), ([1], [1])],
)
def test_examples(xs, expected_tail):
    assert _to_list(middle_node(_build(xs))) == expected_tail
""",
    },
    {
        "slug": "07-remove-nth-from-end",
        "title": "Remove Nth node from end",
        "difficulty": "medium",
        "tags": ["fast-slow-pointer"],
        "statement": "Given the head of a list and integer `n`, remove the `n`-th node from the end (1-indexed) and return the new head.",
        "signature": "def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None: ...",
        "examples_md": """## Examples

| list | n | result |
|---|---|---|
| `1->2->3->4->5` | 2 | `1->2->3->5` |
| `1` | 1 | `[]` |
| `1->2` | 1 | `1` |""",
        "constraints": "",
        "hint": "Use a sentinel node before `head` so removing the actual head is uniform. Move `fast` n+1 steps ahead, then advance both until `fast is None`. `slow.next` is the node to remove.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    \"\"\"One pass with offset fast/slow pointers.

    Time: Θ(L).  Space: Θ(1).
    \"\"\"
    sentinel = ListNode(0, head)
    fast: ListNode | None = sentinel
    slow: ListNode = sentinel
    for _ in range(n + 1):
        if fast is None:
            return head
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next  # type: ignore[assignment]
    if slow.next is not None:
        slow.next = slow.next.next
    return sentinel.next
""",
        "tests": """
import pytest

from solution import ListNode, remove_nth_from_end


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


@pytest.mark.parametrize(
    "xs, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ],
)
def test_examples(xs, n, expected):
    assert _to_list(remove_nth_from_end(_build(xs), n)) == expected
""",
    },
    {
        "slug": "08-palindrome-linked-list",
        "title": "Palindrome linked list",
        "difficulty": "medium",
        "tags": ["two-pointer", "in-place-reverse"],
        "statement": "Return `True` if the singly-linked list reads the same forward and backward. Solve in `Θ(n)` time, `Θ(1)` extra space.",
        "signature": "def is_palindrome(head: ListNode | None) -> bool: ...",
        "examples_md": """## Examples

| list | result |
|---|---|
| `1->2->2->1` | True |
| `1->2` | False |
| `1` | True |""",
        "constraints": "",
        "hint": "Find the midpoint with fast/slow, reverse the second half in place, then walk the two halves in lockstep comparing values. Optionally restore the list afterwards.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def is_palindrome(head: ListNode | None) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def _reverse(head):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def is_palindrome(head: ListNode | None) -> bool:
    \"\"\"Time: Θ(n).  Space: Θ(1).\"\"\"
    if head is None or head.next is None:
        return True
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
    second = _reverse(slow.next)  # type: ignore[union-attr]
    p1, p2 = head, second
    ok = True
    while p2 is not None:
        if p1.val != p2.val:
            ok = False
            break
        p1 = p1.next  # type: ignore[union-attr]
        p2 = p2.next
    return ok
""",
        "tests": """
import pytest

from solution import ListNode, is_palindrome


def _build(xs):
    head = None
    for v in reversed(xs):
        head = ListNode(v, head)
    return head


@pytest.mark.parametrize(
    "xs, expected",
    [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], False),
    ],
)
def test_examples(xs, expected):
    assert is_palindrome(_build(xs)) is expected
""",
    },
    {
        "slug": "09-intersection-two-lists",
        "title": "Intersection of two linked lists",
        "difficulty": "medium",
        "tags": ["two-pointer", "math-trick"],
        "statement": "Given heads of two singly-linked lists, return the node where they first intersect, or `None` if they don't. `Θ(n + m)` time, `Θ(1)` space.",
        "signature": "def get_intersection(a: ListNode | None, b: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

Two lists that share a suffix have an intersection node (the first shared one).""",
        "constraints": "",
        "hint": "Two pointers, each walks list A then list B (and vice versa). After at most `n + m` steps they either both reach `None` (no intersection) or land on the same node (the answer). Proof: both pointers traverse exactly `n + m` nodes total before any miss is recovered.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def get_intersection(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def get_intersection(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    if a is None or b is None:
        return None
    p1, p2 = a, b
    while p1 is not p2:
        p1 = p1.next if p1 is not None else b
        p2 = p2.next if p2 is not None else a
    return p1
""",
        "tests": """
from solution import ListNode, get_intersection


def _link(values_before, shared_values, prefix_to_share=True):
    shared = None
    for v in reversed(shared_values):
        shared = ListNode(v, shared)
    head = shared
    for v in reversed(values_before):
        head = ListNode(v, head)
    return head, shared


def test_intersect_in_middle():
    shared_values = [8, 4, 5]
    a_head, shared = _link([4, 1], shared_values)
    b_head, _ = _link([5, 6, 1], [])
    # rebuild b with the shared tail
    cur = b_head
    while cur.next is not None:
        cur = cur.next
    cur.next = shared
    assert get_intersection(a_head, b_head) is shared


def test_no_intersection():
    a = ListNode(1, ListNode(2))
    b = ListNode(3, ListNode(4))
    assert get_intersection(a, b) is None


def test_both_none():
    assert get_intersection(None, None) is None
""",
    },
    {
        "slug": "10-add-two-numbers",
        "title": "Add two numbers",
        "difficulty": "medium",
        "tags": ["arithmetic", "linked-list"],
        "statement": "Two non-negative integers are represented as linked lists, with each node holding one digit in REVERSE order (so `342` is `2->4->3`). Return the sum as a linked list in the same order.",
        "signature": "def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

| a | b | result |
|---|---|---|
| `2->4->3` (342) | `5->6->4` (465) | `7->0->8` (807) |
| `0` | `0` | `0` |
| `9->9` | `1` | `0->0->1` (100) |""",
        "constraints": "",
        "hint": "Walk both lists together; carry propagates digit by digit.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    \"\"\"Time: Θ(max(n, m)).  Space: Θ(max(n, m)).\"\"\"
    sentinel = ListNode()
    tail = sentinel
    carry = 0
    while a is not None or b is not None or carry:
        x = a.val if a is not None else 0
        y = b.val if b is not None else 0
        s = x + y + carry
        carry, digit = divmod(s, 10)
        tail.next = ListNode(digit)
        tail = tail.next
        a = a.next if a is not None else None
        b = b.next if b is not None else None
    return sentinel.next
""",
        "tests": """
import pytest

from solution import ListNode, add_two_numbers


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


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9], [1], [0, 0, 1]),
        ([1, 9, 9], [9, 9], [0, 9, 9, 1]),
    ],
)
def test_examples(a, b, expected):
    assert _to_list(add_two_numbers(_build(a), _build(b))) == expected
""",
    },
    {
        "slug": "11-remove-duplicates-sorted-list",
        "title": "Remove duplicates from sorted list",
        "difficulty": "easy",
        "tags": ["linked-list"],
        "statement": "Given a sorted singly-linked list, remove duplicates so each element appears only once. Return the modified head.",
        "signature": "def delete_duplicates(head: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

| input | result |
|---|---|
| `1->1->2` | `1->2` |
| `1->1->2->3->3` | `1->2->3` |""",
        "constraints": "",
        "hint": "Walk once. If `cur.next.val == cur.val`, skip: `cur.next = cur.next.next`. Else advance.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode | None) -> ListNode | None:
    cur = head
    while cur is not None and cur.next is not None:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
""",
        "tests": """
import pytest

from solution import ListNode, delete_duplicates


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


@pytest.mark.parametrize(
    "xs, expected",
    [([1, 1, 2], [1, 2]), ([1, 1, 2, 3, 3], [1, 2, 3]), ([], []), ([1], [1])],
)
def test_examples(xs, expected):
    assert _to_list(delete_duplicates(_build(xs))) == expected
""",
    },
    {
        "slug": "12-odd-even-linked-list",
        "title": "Odd-even linked list",
        "difficulty": "medium",
        "tags": ["pointer-manipulation", "in-place"],
        "statement": "Reorder a singly-linked list so that all nodes at odd positions (1-indexed) come before all nodes at even positions, preserving relative order within each group. `Θ(n)` time, `Θ(1)` extra space.",
        "signature": "def odd_even_list(head: ListNode | None) -> ListNode | None: ...",
        "examples_md": """## Examples

| input | result |
|---|---|
| `1->2->3->4->5` | `1->3->5->2->4` |
| `2->1->3->5->6->4->7` | `2->3->6->7->1->5->4` |""",
        "constraints": "",
        "hint": "Maintain two chains: odd-position tail and even-position tail. Walk through the list, pulling alternating nodes into each chain. Finally, set `odd.next = even_head`.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def odd_even_list(head: ListNode | None) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def odd_even_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    odd = head
    even_head = head.next
    even = even_head
    while even is not None and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head
""",
        "tests": """
import pytest

from solution import ListNode, odd_even_list


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


@pytest.mark.parametrize(
    "xs, expected",
    [
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
        ([], []),
        ([1], [1]),
    ],
)
def test_examples(xs, expected):
    assert _to_list(odd_even_list(_build(xs))) == expected
""",
    },
    {
        "slug": "13-reverse-between",
        "title": "Reverse linked list between indices",
        "difficulty": "medium",
        "tags": ["pointer-manipulation", "in-place"],
        "statement": "Reverse the nodes of the list between positions `left` and `right` (1-indexed, inclusive). Single pass, `Θ(1)` extra space.",
        "signature": "def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None: ...",
        "examples_md": """## Examples

| input | left | right | result |
|---|---|---|---|
| `1->2->3->4->5` | 2 | 4 | `1->4->3->2->5` |
| `5` | 1 | 1 | `5` |""",
        "constraints": "",
        "hint": "Use a sentinel. Walk to the node just before `left`. From there, repeatedly take `cur.next` and move it to the front of the sublist (insert after the sentinel of the sublist).",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    if head is None or left == right:
        return head
    sentinel = ListNode(0, head)
    prev = sentinel
    for _ in range(left - 1):
        assert prev.next is not None
        prev = prev.next
    cur = prev.next
    assert cur is not None
    # In-place: move cur.next to position prev.next.
    for _ in range(right - left):
        nxt = cur.next
        assert nxt is not None
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return sentinel.next
""",
        "tests": """
import pytest

from solution import ListNode, reverse_between


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


@pytest.mark.parametrize(
    "xs, left, right, expected",
    [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([1, 2], 1, 2, [2, 1]),
        ([1, 2, 3, 4], 1, 4, [4, 3, 2, 1]),
    ],
)
def test_examples(xs, left, right, expected):
    assert _to_list(reverse_between(_build(xs), left, right)) == expected
""",
    },
    {
        "slug": "14-reorder-list",
        "title": "Reorder list",
        "difficulty": "medium",
        "tags": ["fast-slow-pointer", "in-place-reverse", "merge"],
        "statement": "Given `L0 -> L1 -> ... -> Ln-1`, reorder in place to `L0 -> Ln-1 -> L1 -> Ln-2 -> L2 -> Ln-3 -> ...`. `Θ(n)` time, `Θ(1)` extra space.",
        "signature": "def reorder_list(head: ListNode | None) -> None: ...",
        "examples_md": """## Examples

| input | result |
|---|---|
| `1->2->3->4` | `1->4->2->3` |
| `1->2->3->4->5` | `1->5->2->4->3` |""",
        "constraints": "",
        "hint": "1. Find the midpoint (fast/slow). 2. Reverse the second half. 3. Interleave the two halves.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reorder_list(head: ListNode | None) -> None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reorder_list(head: ListNode | None) -> None:
    if head is None or head.next is None:
        return
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
    second = slow.next  # type: ignore[union-attr]
    slow.next = None  # type: ignore[union-attr]
    prev = None
    curr = second
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev
    p1, p2 = head, second
    while p2 is not None:
        n1, n2 = p1.next, p2.next  # type: ignore[union-attr]
        p1.next = p2  # type: ignore[union-attr]
        p2.next = n1
        p1 = n1
        p2 = n2
""",
        "tests": """
import pytest

from solution import ListNode, reorder_list


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


@pytest.mark.parametrize(
    "xs, expected",
    [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
    ],
)
def test_examples(xs, expected):
    head = _build(xs)
    reorder_list(head)
    assert _to_list(head) == expected
""",
    },
    {
        "slug": "15-rotate-right",
        "title": "Rotate linked list right",
        "difficulty": "medium",
        "tags": ["linked-list"],
        "statement": "Rotate the list to the right by `k` places. `k` may be larger than the list length.",
        "signature": "def rotate_right(head: ListNode | None, k: int) -> ListNode | None: ...",
        "examples_md": """## Examples

| input | k | result |
|---|---|---|
| `1->2->3->4->5` | 2 | `4->5->1->2->3` |
| `0->1->2` | 4 | `2->0->1` |
| `[]` | 1 | `[]` |""",
        "constraints": "",
        "hint": "Close the list into a cycle, walk `n - k % n` steps from head, break the cycle there.",
        "starter": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None or k == 0:
        return head
    n = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        n += 1
    k %= n
    if k == 0:
        return head
    tail.next = head
    steps = n - k
    new_tail = head
    for _ in range(steps - 1):
        assert new_tail.next is not None
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
""",
        "tests": """
import pytest

from solution import ListNode, rotate_right


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


@pytest.mark.parametrize(
    "xs, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([], 1, []),
        ([1], 99, [1]),
    ],
)
def test_examples(xs, k, expected):
    assert _to_list(rotate_right(_build(xs), k)) == expected
""",
    },
    {
        "slug": "16-copy-random-list",
        "title": "Copy list with random pointer",
        "difficulty": "medium",
        "tags": ["hash-map", "linked-list"],
        "statement": "Each node has `next` and `random` pointers (random may point to any node or None). Return a deep copy of the list.",
        "signature": "class Node:\n    val: int\n    next: 'Node | None'\n    random: 'Node | None'\n\ndef copy_random_list(head: Node | None) -> Node | None: ...",
        "examples_md": """## Examples

```
1 -> 2 -> 3
|    |
random=3  random=1
```

Output: an independent copy with the same structure.""",
        "constraints": "",
        "hint": "Two-pass with hash map: pass 1 builds a map `original_node -> cloned_node` for every node. Pass 2 wires `next` and `random` of each clone using the map.",
        "starter": """
class Node:
    def __init__(self, val: int = 0, next: "Node | None" = None, random: "Node | None" = None) -> None:
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node | None) -> Node | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class Node:
    def __init__(self, val: int = 0, next: "Node | None" = None, random: "Node | None" = None) -> None:
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node | None) -> Node | None:
    \"\"\"Time: Θ(n).  Space: Θ(n).\"\"\"
    if head is None:
        return None
    mapping: dict[int, Node] = {}
    cur: Node | None = head
    while cur is not None:
        mapping[id(cur)] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur is not None:
        clone = mapping[id(cur)]
        clone.next = mapping[id(cur.next)] if cur.next is not None else None
        clone.random = mapping[id(cur.random)] if cur.random is not None else None
        cur = cur.next
    return mapping[id(head)]
""",
        "tests": """
from solution import Node, copy_random_list


def _build(values, random_idx):
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, r in enumerate(random_idx):
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None


def _serialize(head):
    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    index = {id(n): i for i, n in enumerate(nodes)}
    return [(n.val, index.get(id(n.random))) for n in nodes]


def test_basic_copy():
    head = _build([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copy = copy_random_list(head)
    assert copy is not head
    assert _serialize(copy) == _serialize(head)


def test_empty():
    assert copy_random_list(None) is None
""",
    },
    {
        "slug": "17-lru-cache",
        "title": "LRU cache",
        "difficulty": "medium",
        "tags": ["doubly-linked-list", "hash-map", "design"],
        "statement": "Implement an `LRUCache` with capacity `cap`. Support `get(key) -> int` (returns -1 if absent), `put(key, value)`. Both must run in average `Θ(1)`. When `put` exceeds capacity, evict the least-recently-used entry.",
        "signature": "class LRUCache:\n    def __init__(self, capacity: int) -> None: ...\n    def get(self, key: int) -> int: ...\n    def put(self, key: int, value: int) -> None: ...",
        "examples_md": """## Examples

```
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)         # 1
cache.put(3, 3)      # evicts 2
cache.get(2)         # -1
cache.put(4, 4)      # evicts 1
cache.get(1)         # -1
cache.get(3)         # 3
cache.get(4)         # 4
```""",
        "constraints": "- `1 <= capacity <= 3000`",
        "hint": "Doubly-linked list + dict. Map key -> node; the list orders nodes by recency, head = most recent, tail = LRU. Sentinel head/tail simplify edge cases.",
        "starter": """
class LRUCache:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError
""",
        "reference": """
class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    \"\"\"O(1) avg per op via dict + doubly-linked list.\"\"\"

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.map: dict[int, _Node] = {}
        self.head = _Node(0, 0)
        self.tail = _Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        self._move_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node is not None:
            node.value = value
            self._move_front(node)
            return
        if len(self.map) == self.cap:
            self._evict()
        node = _Node(key, value)
        self.map[key] = node
        self._insert_front(node)

    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        nxt = self.head.next
        node.prev = self.head
        node.next = nxt
        self.head.next = node
        nxt.prev = node

    def _move_front(self, node):
        self._unlink(node)
        self._insert_front(node)

    def _evict(self):
        lru = self.tail.prev
        self._unlink(lru)
        del self.map[lru.key]
""",
        "tests": """
import pytest

from solution import LRUCache


def test_classic_flow():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4


def test_capacity_one():
    c = LRUCache(1)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == -1
    assert c.get(2) == 2


def test_update_promotes():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)  # promotes 1
    c.put(3, 3)   # should evict 2 since 1 was just used
    assert c.get(2) == -1
    assert c.get(1) == 10
    assert c.get(3) == 3
""",
    },
    {
        "slug": "18-flatten-multilevel-doubly-list",
        "title": "Flatten a multilevel doubly linked list",
        "difficulty": "medium",
        "tags": ["doubly-linked-list", "stack", "dfs"],
        "statement": "Each node in a doubly-linked list has `prev`, `next`, and `child` pointers. `child` may point to a separate doubly-linked list (which may itself have children). Flatten the structure depth-first into a single-level doubly-linked list.",
        "signature": "class Node:\n    val: int\n    prev: 'Node | None'\n    next: 'Node | None'\n    child: 'Node | None'\n\ndef flatten(head: Node | None) -> Node | None: ...",
        "examples_md": """## Examples

```
1 <-> 2 <-> 3
      |
      4 <-> 5
```

becomes

```
1 <-> 2 <-> 4 <-> 5 <-> 3
```""",
        "constraints": "",
        "hint": "Walk left to right. When you see `cur.child`, splice the child sublist between `cur` and `cur.next`. Use a stack to remember the original `cur.next` to attach after the child sublist's tail.",
        "starter": """
class Node:
    def __init__(self, val: int = 0, prev: "Node | None" = None, next: "Node | None" = None, child: "Node | None" = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Node | None) -> Node | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class Node:
    def __init__(self, val: int = 0, prev: "Node | None" = None, next: "Node | None" = None, child: "Node | None" = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Node | None) -> Node | None:
    if head is None:
        return None
    stack: list[Node] = []
    cur = head
    while cur is not None:
        if cur.child is not None:
            if cur.next is not None:
                stack.append(cur.next)
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
        if cur.next is None and stack:
            nxt = stack.pop()
            cur.next = nxt
            nxt.prev = cur
        cur = cur.next
    return head
""",
        "tests": """
from solution import Node, flatten


def _build_simple_flat(values):
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0] if nodes else None


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_no_children():
    head = _build_simple_flat([1, 2, 3])
    assert _to_list(flatten(head)) == [1, 2, 3]


def test_one_level_child():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    d = Node(4)
    e = Node(5)
    d.next = e
    e.prev = d
    b.child = d
    assert _to_list(flatten(a)) == [1, 2, 4, 5, 3]


def test_empty():
    assert flatten(None) is None
""",
    },
]
