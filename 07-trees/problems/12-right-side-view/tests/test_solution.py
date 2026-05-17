from solution import TreeNode, right_side_view


def test_basic():
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]


def test_empty():
    assert right_side_view(None) == []
