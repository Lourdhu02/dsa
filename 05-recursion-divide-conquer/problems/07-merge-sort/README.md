# 07. Merge sort  `[medium]`

Implement merge sort. Return a NEW sorted list; don't mutate the input. Must be stable: equal keys preserve relative order.

## Function signature

```python
def merge_sort(xs: list[int]) -> list[int]: ...
```

## Examples

| xs | sorted |
|---|---|
| `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]` | `[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]` |



## Hint

<details>
<summary>Hint</summary>

Recurse on halves, then linear merge. The merge step's tie-breaker (`<=`, not `<`) is what makes it stable.
</details>
