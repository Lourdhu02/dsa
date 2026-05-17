# 03. Binary tree postorder traversal  `[easy]`

Return the postorder traversal of a binary tree.

## Function signature

```python
def postorder(root: TreeNode | None) -> list[int]: ...
```

## Examples

| tree | postorder |
|---|---|
| `[1, None, 2, 3]` | `[3, 2, 1]` |



## Hint

<details>
<summary>Hint</summary>

Reverse preorder with swapped child push order works: collect `root,right,left` then reverse.
</details>
