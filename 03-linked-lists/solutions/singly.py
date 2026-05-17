"""Singly-linked list with the operations the practice problems lean on.

We use the ``ListNode`` class throughout the module; importing it from here keeps
test fixtures consistent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Iterator, Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = field(default=None, repr=False)


def from_iterable(xs: Iterable[int]) -> Optional[ListNode]:
    """Build a list from any iterable.  Time/Space: Θ(n)."""
    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None
    for v in xs:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return head


def to_list(head: Optional[ListNode]) -> list[int]:
    """Materialize a linked list as a Python list.  Time: Θ(n)."""
    out: list[int] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out


def iter_nodes(head: Optional[ListNode]) -> Iterator[ListNode]:
    cur = head
    while cur is not None:
        yield cur
        cur = cur.next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    """In-place reverse.  Time: Θ(n).  Space: Θ(1).

    Invariant: at the top of each iteration, ``prev`` is the head of the
    already-reversed prefix and ``curr`` is the head of the unprocessed
    suffix.
    """
    prev: Optional[ListNode] = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
