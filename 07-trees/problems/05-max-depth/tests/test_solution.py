from solution import TreeNode, max_depth


def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3


def test_empty():
    assert max_depth(None) == 0


def test_linear():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert max_depth(root) == 4
