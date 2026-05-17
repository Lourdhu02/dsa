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
