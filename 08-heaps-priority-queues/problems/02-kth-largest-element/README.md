# 02. Kth largest element in array  `[medium]`

Return the kth largest element in an unsorted array.

## Function signature

```python
def find_kth_largest(nums: list[int], k: int) -> int: ...
```

## Examples

| nums | k | result |
|---|---|---|
| `[3, 2, 1, 5, 6, 4]` | 2 | 5 |
| `[3, 2, 3, 1, 2, 4, 5, 5, 6]` | 4 | 4 |



## Hint

<details>
<summary>Hint</summary>

Maintain a min-heap of size k. Push each element; if size > k, pop. Final heap[0] is the answer. Θ(n log k).
</details>
