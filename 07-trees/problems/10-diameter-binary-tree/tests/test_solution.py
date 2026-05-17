from solution import TreeNode, diameter


def test_basic():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter(root) == 3


def test_linear():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert diameter(root) == 2


def test_empty():
    assert diameter(None) == 0
