from solution import Codec, TreeNode


def _flatten(root):
    if root is None:
        return []
    out, q = [], [root]
    while q:
        node = q.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def test_roundtrip_basic():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    assert _flatten(codec.deserialize(codec.serialize(root))) == _flatten(root)


def test_empty():
    codec = Codec()
    assert codec.deserialize(codec.serialize(None)) is None
