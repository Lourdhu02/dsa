# 01. Binary tree inorder traversal  `[easy]`

Given the root of a binary tree, return the inorder traversal as a list. Implement both recursive and iterative; submit either.

## Function signature

```python
class TreeNode: ...

def inorder_traversal(root: TreeNode | None) -> list[int]: ...
```

## Examples

```
    1
     \
      2
     /
    3
```

Result: `[1, 3, 2]`.



## Hint

<details>
<summary>Hint</summary>

Recursive: visit left, append node, visit right. Iterative: stack; walk left, pop, append, go right.
</details>
