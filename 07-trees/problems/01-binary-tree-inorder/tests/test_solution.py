from solution import TreeNode, inorder_traversal


def test_basic():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorder_traversal(root) == [1, 3, 2]


def test_empty():
    assert inorder_traversal(None) == []


def test_single():
    assert inorder_traversal(TreeNode(7)) == [7]
