from solution import TreeNode, zigzag


def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert zigzag(root) == [[3], [20, 9], [15, 7]]


def test_empty():
    assert zigzag(None) == []
