# 08. Quick sort  `[medium]`

Implement quicksort with a random pivot. Sort in place and return the same list.

## Function signature

```python
def quick_sort(xs: list[int]) -> list[int]: ...
```

## Examples

| xs | sorted |
|---|---|
| `[3, 1, 4, 1, 5]` | `[1, 1, 3, 4, 5]` |



## Hint

<details>
<summary>Hint</summary>

Lomuto partition with a random pivot. After partition, recurse on `[lo, p-1]` and `[p+1, hi]`.
</details>
