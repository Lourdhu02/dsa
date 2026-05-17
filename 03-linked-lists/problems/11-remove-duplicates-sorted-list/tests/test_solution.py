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
