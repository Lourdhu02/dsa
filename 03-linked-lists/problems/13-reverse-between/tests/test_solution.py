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
