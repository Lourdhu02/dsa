from solution import TreeNode, lca


def test_basic():
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n6, TreeNode(2, n7, n4))
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)
    assert lca(root, n5, n1) is root
    assert lca(root, n5, n4) is n5
