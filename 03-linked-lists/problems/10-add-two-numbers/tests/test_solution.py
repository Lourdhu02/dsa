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
