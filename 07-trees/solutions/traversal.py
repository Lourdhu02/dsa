"""Recursive, iterative, and Morris traversal templates."""

from __future__ import annotations

from typing import Optional

from .tree import TreeNode


def inorder_recursive(root: Optional[TreeNode]) -> list[int]:
    """Standard recursive inorder.  Time: Θ(n).  Space: Θ(h)."""
    out: list[int] = []

    def _rec(node):
        if node is None:
            return
        _rec(node.left)
        out.append(node.val)
        _rec(node.right)

    _rec(root)
    return out


def inorder_iterative(root: Optional[TreeNode]) -> list[int]:
    """Iterative inorder using an explicit stack.  Time: Θ(n).  Space: Θ(h)."""
    out: list[int] = []
    stack: list[TreeNode] = []
    cur = root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def inorder_morris(root: Optional[TreeNode]) -> list[int]:
    """Morris inorder: Θ(1) extra space, Θ(n) time.

    Reference: Morris, J. M. (1979).
    """
    out: list[int] = []
    cur = root
    while cur is not None:
        if cur.left is None:
            out.append(cur.val)
            cur = cur.right
        else:
            pred = cur.left
            while pred.right is not None and pred.right is not cur:
                pred = pred.right
            if pred.right is None:
                pred.right = cur  # plant the thread
                cur = cur.left
            else:
                pred.right = None  # remove the thread
                out.append(cur.val)
                cur = cur.right
    return out


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    """BFS in layers.  Time: Θ(n).  Space: Θ(w) where w = max width."""
    if root is None:
        return []
    out: list[list[int]] = []
    cur_layer = [root]
    while cur_layer:
        out.append([n.val for n in cur_layer])
        nxt = []
        for n in cur_layer:
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        cur_layer = nxt
    return out
