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
