from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        if root is None:
            return ""
        out = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                out.append("null")
            else:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        while out and out[-1] == "null":
            out.pop()
        return ",".join(out)

    def deserialize(self, data):
        if not data:
            return None
        tokens = data.split(",")
        it = iter(tokens)
        root = TreeNode(int(next(it)))
        q = deque([root])
        while q:
            node = q.popleft()
            try:
                left = next(it)
            except StopIteration:
                break
            if left != "null":
                node.left = TreeNode(int(left))
                q.append(node.left)
            try:
                right = next(it)
            except StopIteration:
                break
            if right != "null":
                node.right = TreeNode(int(right))
                q.append(node.right)
        return root
