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
