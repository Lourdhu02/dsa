"""Module 07 (trees) manifest."""

# Common helpers replicated per problem (the scaffold copies each reference
# string verbatim; problems can't share helpers across files).

PROBLEMS = [
    {
        "slug": "01-binary-tree-inorder",
        "title": "Binary tree inorder traversal",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Given the root of a binary tree, return the inorder traversal as a list. Implement both recursive and iterative; submit either.",
        "signature": "class TreeNode: ...\n\ndef inorder_traversal(root: TreeNode | None) -> list[int]: ...",
        "examples_md": """## Examples

```
    1
     \\
      2
     /
    3
```

Result: `[1, 3, 2]`.""",
        "constraints": "",
        "hint": "Recursive: visit left, append node, visit right. Iterative: stack; walk left, pop, append, go right.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode | None) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode | None) -> list[int]:
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
""",
        "tests": """
from solution import TreeNode, inorder_traversal


def test_basic():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorder_traversal(root) == [1, 3, 2]


def test_empty():
    assert inorder_traversal(None) == []


def test_single():
    assert inorder_traversal(TreeNode(7)) == [7]
""",
    },
    {
        "slug": "02-binary-tree-preorder",
        "title": "Binary tree preorder traversal",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return the preorder traversal of a binary tree.",
        "signature": "def preorder(root: TreeNode | None) -> list[int]: ...",
        "examples_md": """## Examples

| tree | preorder |
|---|---|
| `[1, None, 2, 3]` | `[1, 2, 3]` |""",
        "constraints": "",
        "hint": "Iterative with a stack: push root, then pop, append val, push right then left.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode | None) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    out: list[int] = []
    stack: list[TreeNode] = [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return out
""",
        "tests": """
from solution import TreeNode, preorder


def test_basic():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert preorder(root) == [1, 2, 3]


def test_empty():
    assert preorder(None) == []
""",
    },
    {
        "slug": "03-binary-tree-postorder",
        "title": "Binary tree postorder traversal",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return the postorder traversal of a binary tree.",
        "signature": "def postorder(root: TreeNode | None) -> list[int]: ...",
        "examples_md": """## Examples

| tree | postorder |
|---|---|
| `[1, None, 2, 3]` | `[3, 2, 1]` |""",
        "constraints": "",
        "hint": "Reverse preorder with swapped child push order works: collect `root,right,left` then reverse.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def postorder(root: TreeNode | None) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def postorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    out: list[int] = []
    stack: list[TreeNode] = [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    out.reverse()
    return out
""",
        "tests": """
from solution import TreeNode, postorder


def test_basic():
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert postorder(root) == [3, 2, 1]


def test_empty():
    assert postorder(None) == []
""",
    },
    {
        "slug": "04-level-order-traversal",
        "title": "Level-order traversal",
        "difficulty": "medium",
        "tags": ["tree", "bfs"],
        "statement": "Return a list of lists: each inner list is one level of the tree, top to bottom.",
        "signature": "def level_order(root: TreeNode | None) -> list[list[int]]: ...",
        "examples_md": """## Examples

```
    3
   / \\
  9   20
     /  \\
    15   7
```

Result: `[[3], [9, 20], [15, 7]]`.""",
        "constraints": "",
        "hint": "BFS layer by layer; collect each layer in a list.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    out: list[list[int]] = []
    layer = [root]
    while layer:
        out.append([n.val for n in layer])
        nxt = []
        for n in layer:
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        layer = nxt
    return out
""",
        "tests": """
from solution import TreeNode, level_order


def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_empty():
    assert level_order(None) == []
""",
    },
    {
        "slug": "05-max-depth",
        "title": "Maximum depth of binary tree",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return the maximum depth of a binary tree (number of nodes on longest root-to-leaf path).",
        "signature": "def max_depth(root: TreeNode | None) -> int: ...",
        "examples_md": """## Examples

| tree | depth |
|---|---|
| `[3, 9, 20, None, None, 15, 7]` | 3 |
| `[]` | 0 |""",
        "constraints": "",
        "hint": "`max_depth(None) == 0; else 1 + max(left, right)`.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
""",
        "tests": """
from solution import TreeNode, max_depth


def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3


def test_empty():
    assert max_depth(None) == 0


def test_linear():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert max_depth(root) == 4
""",
    },
    {
        "slug": "06-same-tree",
        "title": "Same tree",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return True if two binary trees are structurally identical and have equal values.",
        "signature": "def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool: ...",
        "examples_md": """## Examples

| p | q | same |
|---|---|---|
| `[1, 2, 3]` | `[1, 2, 3]` | True |
| `[1, 2]` | `[1, None, 2]` | False |""",
        "constraints": "",
        "hint": "Recurse: both null → True; one null → False; values differ → False; else recurse on children.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None or q is None:
        return p is q
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
""",
        "tests": """
from solution import TreeNode, is_same_tree


def test_same():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) is True


def test_different():
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p, q) is False


def test_both_empty():
    assert is_same_tree(None, None) is True
""",
    },
    {
        "slug": "07-symmetric-tree",
        "title": "Symmetric tree",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return True if the binary tree is mirror-symmetric about its center.",
        "signature": "def is_symmetric(root: TreeNode | None) -> bool: ...",
        "examples_md": """## Examples

```
    1
   / \\
  2   2
 / \\ / \\
3  4 4  3        symmetric
```""",
        "constraints": "",
        "hint": "Helper compares `(left, right)`: same val AND mirror children.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode | None) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode | None) -> bool:
    def _mirror(a, b):
        if a is None or b is None:
            return a is b
        return a.val == b.val and _mirror(a.left, b.right) and _mirror(a.right, b.left)

    return root is None or _mirror(root.left, root.right)
""",
        "tests": """
from solution import TreeNode, is_symmetric


def test_symmetric():
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert is_symmetric(root) is True


def test_asymmetric():
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert is_symmetric(root) is False


def test_empty():
    assert is_symmetric(None) is True
""",
    },
    {
        "slug": "08-invert-binary-tree",
        "title": "Invert binary tree",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Mirror a binary tree (swap left and right at every node).",
        "signature": "def invert_tree(root: TreeNode | None) -> TreeNode | None: ...",
        "examples_md": """## Examples

`[4, 2, 7, 1, 3, 6, 9]` becomes `[4, 7, 2, 9, 6, 3, 1]`.""",
        "constraints": "",
        "hint": "Recurse: swap children of the current node, then recurse into both.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
""",
        "tests": """
from solution import TreeNode, invert_tree


def _level_order(root):
    if root is None:
        return []
    out, q = [], [root]
    while q:
        nxt = []
        for n in q:
            out.append(n.val)
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        q = nxt
    return out


def test_basic():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(root)
    assert _level_order(inverted) == [4, 7, 2, 9, 6, 3, 1]


def test_empty():
    assert invert_tree(None) is None
""",
    },
    {
        "slug": "09-balanced-binary-tree",
        "title": "Balanced binary tree",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return True if for every node, the heights of its two subtrees differ by at most 1.",
        "signature": "def is_balanced(root: TreeNode | None) -> bool: ...",
        "examples_md": """## Examples

`[3, 9, 20, None, None, 15, 7]` is balanced.
`[1, 2, 2, 3, 3, None, None, 4, 4]` is not.""",
        "constraints": "",
        "hint": "Bottom-up: each call returns the height OR -1 if unbalanced. Propagate -1 up.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    def _height(node):
        if node is None:
            return 0
        lh = _height(node.left)
        if lh == -1:
            return -1
        rh = _height(node.right)
        if rh == -1 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return _height(root) != -1
""",
        "tests": """
from solution import TreeNode, is_balanced


def test_balanced():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(root) is True


def test_unbalanced():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert is_balanced(root) is False


def test_empty():
    assert is_balanced(None) is True
""",
    },
    {
        "slug": "10-diameter-binary-tree",
        "title": "Diameter of binary tree",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return the length (number of edges) of the longest path between any two nodes. The path may or may not pass through the root.",
        "signature": "def diameter(root: TreeNode | None) -> int: ...",
        "examples_md": """## Examples

| tree | diameter |
|---|---|
| `[1, 2, 3, 4, 5]` | 3 (path 4-2-1-3 or 5-2-1-3) |
| `[1, 2]` | 1 |""",
        "constraints": "",
        "hint": "Bottom-up. Each node returns its height; the diameter through that node is `left_height + right_height`. Track max.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def diameter(root: TreeNode | None) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def diameter(root: TreeNode | None) -> int:
    best = 0

    def _h(node):
        nonlocal best
        if node is None:
            return 0
        lh = _h(node.left)
        rh = _h(node.right)
        best = max(best, lh + rh)
        return 1 + max(lh, rh)

    _h(root)
    return best
""",
        "tests": """
from solution import TreeNode, diameter


def test_basic():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter(root) == 3


def test_linear():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert diameter(root) == 2


def test_empty():
    assert diameter(None) == 0
""",
    },
    {
        "slug": "11-path-sum",
        "title": "Path sum (root to leaf)",
        "difficulty": "easy",
        "tags": ["tree", "dfs"],
        "statement": "Return True if there is a root-to-leaf path with values summing to `target`.",
        "signature": "def has_path_sum(root: TreeNode | None, target: int) -> bool: ...",
        "examples_md": """## Examples

```
target=22
tree=[5,4,8,11,null,13,4,7,2,null,null,null,1]   -> True (5+4+11+2)
```""",
        "constraints": "",
        "hint": "Recurse subtracting. At a leaf check if remaining == 0.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode | None, target: int) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode | None, target: int) -> bool:
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == target
    rem = target - root.val
    return has_path_sum(root.left, rem) or has_path_sum(root.right, rem)
""",
        "tests": """
from solution import TreeNode, has_path_sum


def test_present():
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    assert has_path_sum(root, 22) is True


def test_absent():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert has_path_sum(root, 5) is False


def test_empty():
    assert has_path_sum(None, 0) is False
""",
    },
    {
        "slug": "12-right-side-view",
        "title": "Binary tree right-side view",
        "difficulty": "medium",
        "tags": ["tree", "bfs"],
        "statement": "Return the values visible when looking at the tree from the right side, top to bottom.",
        "signature": "def right_side_view(root: TreeNode | None) -> list[int]: ...",
        "examples_md": """## Examples

```
   1
  / \\
 2   3
  \\   \\
   5   4
```

Result: `[1, 3, 4]`.""",
        "constraints": "",
        "hint": "Level-order BFS; take the last node of each level.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode | None) -> list[int]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    out: list[int] = []
    layer = [root]
    while layer:
        out.append(layer[-1].val)
        nxt = []
        for n in layer:
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        layer = nxt
    return out
""",
        "tests": """
from solution import TreeNode, right_side_view


def test_basic():
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]


def test_empty():
    assert right_side_view(None) == []
""",
    },
    {
        "slug": "13-zigzag-level-order",
        "title": "Zigzag level order",
        "difficulty": "medium",
        "tags": ["tree", "bfs"],
        "statement": "Return level-order traversal alternating direction per level (left→right, right→left, ...).",
        "signature": "def zigzag(root: TreeNode | None) -> list[list[int]]: ...",
        "examples_md": """## Examples

`[3, 9, 20, None, None, 15, 7]` → `[[3], [20, 9], [15, 7]]`.""",
        "constraints": "",
        "hint": "BFS but reverse every other layer when appending to the output.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def zigzag(root: TreeNode | None) -> list[list[int]]:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def zigzag(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    out: list[list[int]] = []
    layer = [root]
    rev = False
    while layer:
        vals = [n.val for n in layer]
        out.append(list(reversed(vals)) if rev else vals)
        rev = not rev
        nxt = []
        for n in layer:
            if n.left is not None:
                nxt.append(n.left)
            if n.right is not None:
                nxt.append(n.right)
        layer = nxt
    return out
""",
        "tests": """
from solution import TreeNode, zigzag


def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert zigzag(root) == [[3], [20, 9], [15, 7]]


def test_empty():
    assert zigzag(None) == []
""",
    },
    {
        "slug": "14-validate-bst",
        "title": "Validate BST",
        "difficulty": "medium",
        "tags": ["tree", "bst"],
        "statement": "Return True if a binary tree is a valid BST (strict: left < node < right for every node).",
        "signature": "def is_valid_bst(root: TreeNode | None) -> bool: ...",
        "examples_md": """## Examples

`[2, 1, 3]` → True.
`[5, 1, 4, None, None, 3, 6]` → False (3 sits in 5's right subtree).""",
        "constraints": "",
        "hint": "Recurse with `(low, high)` bounds.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    def _rec(node, lo, hi):
        if node is None:
            return True
        if node.val <= lo or node.val >= hi:
            return False
        return _rec(node.left, lo, node.val) and _rec(node.right, node.val, hi)

    return _rec(root, float("-inf"), float("inf"))
""",
        "tests": """
from solution import TreeNode, is_valid_bst


def test_valid():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root) is True


def test_invalid():
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(root) is False


def test_empty():
    assert is_valid_bst(None) is True
""",
    },
    {
        "slug": "15-kth-smallest-bst",
        "title": "Kth smallest in BST",
        "difficulty": "medium",
        "tags": ["tree", "bst", "inorder"],
        "statement": "Return the kth smallest value (1-indexed) in a BST.",
        "signature": "def kth_smallest(root: TreeNode | None, k: int) -> int: ...",
        "examples_md": """## Examples

`[3, 1, 4, None, 2]`, k=1 → 1. k=3 → 3.""",
        "constraints": "",
        "hint": "Inorder traversal yields sorted order; stop at the kth element.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode | None, k: int) -> int:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode | None, k: int) -> int:
    stack: list[TreeNode] = []
    cur = root
    count = 0
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        count += 1
        if count == k:
            return cur.val
        cur = cur.right
    raise IndexError(k)
""",
        "tests": """
from solution import TreeNode, kth_smallest


def test_basic():
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4
""",
    },
    {
        "slug": "16-lowest-common-ancestor-bst",
        "title": "LCA in BST",
        "difficulty": "medium",
        "tags": ["tree", "bst"],
        "statement": "Find the lowest common ancestor of nodes with values `p` and `q` in a BST. Both values exist in the tree.",
        "signature": "def lca_bst(root: TreeNode | None, p: int, q: int) -> TreeNode | None: ...",
        "examples_md": """## Examples

In `[6,2,8,0,4,7,9,None,None,3,5]`, LCA(2, 8) = 6. LCA(2, 4) = 2.""",
        "constraints": "",
        "hint": "Walk from the root. If both `p, q` are less than `root.val`, go left. If both greater, go right. Else split point — return root.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lca_bst(root: TreeNode | None, p: int, q: int) -> TreeNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lca_bst(root: TreeNode | None, p: int, q: int) -> TreeNode | None:
    lo, hi = min(p, q), max(p, q)
    cur = root
    while cur is not None:
        if cur.val < lo:
            cur = cur.right
        elif cur.val > hi:
            cur = cur.left
        else:
            return cur
    return None
""",
        "tests": """
from solution import TreeNode, lca_bst


def test_basic():
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    assert lca_bst(root, 2, 8).val == 6
    assert lca_bst(root, 2, 4).val == 2
    assert lca_bst(root, 3, 5).val == 4
""",
    },
    {
        "slug": "17-lowest-common-ancestor",
        "title": "LCA in binary tree",
        "difficulty": "medium",
        "tags": ["tree", "dfs"],
        "statement": "Find the lowest common ancestor of nodes `p` and `q` in a binary tree (NOT a BST). Both nodes exist.",
        "signature": "def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None: ...",
        "examples_md": """## Examples

In `[3,5,1,6,2,0,8,None,None,7,4]`, LCA(5, 1) = 3.""",
        "constraints": "",
        "hint": "Recurse. Return p/q on match; null on miss. If both subtrees return non-null, this node is the LCA. Otherwise propagate whichever child returned non-null.",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    # TODO
    raise NotImplementedError
""",
        "reference": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if root is None or root is p or root is q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left is not None and right is not None:
        return root
    return left if left is not None else right
""",
        "tests": """
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
""",
    },
    {
        "slug": "18-serialize-deserialize-binary-tree",
        "title": "Serialize and deserialize binary tree",
        "difficulty": "hard",
        "tags": ["tree", "design", "bfs"],
        "statement": "Design `serialize(root) -> str` and `deserialize(s) -> root` such that `deserialize(serialize(t))` reproduces the original tree.",
        "signature": "class Codec:\n    def serialize(self, root: TreeNode | None) -> str: ...\n    def deserialize(self, data: str) -> TreeNode | None: ...",
        "examples_md": """## Examples

Any reversible encoding works. Suggested: level-order with `\"null\"` for missing children, comma-separated.""",
        "constraints": "",
        "hint": "BFS for serialize. For deserialize, parse tokens, build the root, then a queue of parents — for each parent, consume 2 tokens (left, right).",
        "starter": """
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        raise NotImplementedError

    def deserialize(self, data: str) -> TreeNode | None:
        raise NotImplementedError
""",
        "reference": """
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
""",
        "tests": """
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
""",
    },
]
