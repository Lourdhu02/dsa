# 17. Validate BST  `[medium]`

Given the root of a binary tree, determine if it is a valid binary search tree. Every node in the left subtree must be strictly less than the node; every node in the right must be strictly greater. The simplest definition that works is recursive with `(min, max)` bounds.

## Function signature

```python
class TreeNode:
    val: int
    left: 'TreeNode | None'
    right: 'TreeNode | None'

def is_valid_bst(root: TreeNode | None) -> bool: ...
```

## Examples

```
    2
   / \
  1   3       -> True

    5
   / \
  1   4
     / \
    3   6    -> False (3 < 5 but in right subtree)
```



## Hint

<details>
<summary>Hint</summary>

Recurse with `(low, high)` bounds. Node value must satisfy `low < val < high`. Left subtree gets bound `(low, val)`, right gets `(val, high)`.
</details>
