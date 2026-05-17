"""TreeNode and a handful of constructors used across the practice problems."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = field(default=None, repr=False)
    right: Optional["TreeNode"] = field(default=None, repr=False)


def from_level_order(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a level-order list with ``None`` for missing children.

    Time/Space: Θ(n).
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])  # type: ignore[arg-type]
    q: list[TreeNode] = [root]
    i = 1
    while q and i < len(values):
        node = q.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])  # type: ignore[arg-type]
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])  # type: ignore[arg-type]
            q.append(node.right)
        i += 1
    return root


def to_level_order(root: Optional[TreeNode]) -> list[Optional[int]]:
    """Serialize a tree in level-order with trailing Nones trimmed."""
    if root is None:
        return []
    out: list[Optional[int]] = []
    q: list[Optional[TreeNode]] = [root]
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
