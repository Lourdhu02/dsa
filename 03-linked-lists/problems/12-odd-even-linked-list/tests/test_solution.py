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
