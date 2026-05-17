from solutions.traversal import inorder_iterative, inorder_morris, inorder_recursive, level_order
from solutions.tree import from_level_order, to_level_order


def _sample():
    # Tree:        1
    #            /   \
    #           2     3
    #          / \
    #         4   5
    return from_level_order([1, 2, 3, 4, 5])


def test_serialize_roundtrip():
    values = [1, 2, 3, None, 4, None, 5]
    t = from_level_order(values)
    assert to_level_order(t) == [1, 2, 3, None, 4, None, 5]


def test_three_inorders_agree():
    root = _sample()
    rec = inorder_recursive(root)
    itr = inorder_iterative(root)
    mor = inorder_morris(root)
    assert rec == itr == mor == [4, 2, 5, 1, 3]


def test_level_order():
    assert level_order(_sample()) == [[1], [2, 3], [4, 5]]
    assert level_order(None) == []
