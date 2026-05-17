# 04. Level-order traversal  `[medium]`

Return a list of lists: each inner list is one level of the tree, top to bottom.

## Function signature

```python
def level_order(root: TreeNode | None) -> list[list[int]]: ...
```

## Examples

```
    3
   / \
  9   20
     /  \
    15   7
```

Result: `[[3], [9, 20], [15, 7]]`.



## Hint

<details>
<summary>Hint</summary>

BFS layer by layer; collect each layer in a list.
</details>
