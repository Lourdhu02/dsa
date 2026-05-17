# 18. Sliding window median  `[hard]`

Given an array `nums` and window size `k`, return the median of every length-k contiguous window.

## Function signature

```python
def median_sliding_window(nums: list[int], k: int) -> list[float]: ...
```

## Examples

| nums | k | result |
|---|---|---|
| `[1, 3, -1, -3, 5, 3, 6, 7]` | 3 | `[1, -1, -1, 3, 5, 6]` |



## Hint

<details>
<summary>Hint</summary>

Two heaps as in median-from-stream, plus a delayed-removal map (since heap removal is Θ(n)). Lazy delete: track removed elements; pop from heap if top is removed.
</details>
