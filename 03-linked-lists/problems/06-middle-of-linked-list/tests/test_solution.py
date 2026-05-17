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
