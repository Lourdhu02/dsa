# 08. Invert binary tree  `[easy]`

Mirror a binary tree (swap left and right at every node).

## Function signature

```python
def invert_tree(root: TreeNode | None) -> TreeNode | None: ...
```

## Examples

`[4, 2, 7, 1, 3, 6, 9]` becomes `[4, 7, 2, 9, 6, 3, 1]`.



## Hint

<details>
<summary>Hint</summary>

Recurse: swap children of the current node, then recurse into both.
</details>
