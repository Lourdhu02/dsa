from solution import TreeNode, postorder


def test_basic():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert postorder(root) == [3, 2, 1]


def test_empty():
    assert postorder(None) == []
