# 13. Zigzag level order  `[medium]`

Return level-order traversal alternating direction per level (left→right, right→left, ...).

## Function signature

```python
def zigzag(root: TreeNode | None) -> list[list[int]]: ...
```

## Examples

`[3, 9, 20, None, None, 15, 7]` → `[[3], [20, 9], [15, 7]]`.



## Hint

<details>
<summary>Hint</summary>

BFS but reverse every other layer when appending to the output.
</details>
