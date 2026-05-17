# 02. Binary tree preorder traversal  `[easy]`

Return the preorder traversal of a binary tree.

## Function signature

```python
def preorder(root: TreeNode | None) -> list[int]: ...
```

## Examples

| tree | preorder |
|---|---|
| `[1, None, 2, 3]` | `[1, 2, 3]` |



## Hint

<details>
<summary>Hint</summary>

Iterative with a stack: push root, then pop, append val, push right then left.
</details>
