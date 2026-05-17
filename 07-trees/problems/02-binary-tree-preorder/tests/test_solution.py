from solution import TreeNode, preorder


def test_basic():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert preorder(root) == [1, 2, 3]


def test_empty():
    assert preorder(None) == []
