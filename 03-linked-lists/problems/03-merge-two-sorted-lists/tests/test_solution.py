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
