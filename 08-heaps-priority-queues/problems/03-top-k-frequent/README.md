# 03. Top K frequent elements (heap)  `[medium]`

Return the k most frequent elements of `nums`. (Same problem as module 02 problem 09 but solve with a heap.)

## Function signature

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]: ...
```

## Examples

| nums | k | result (any order) |
|---|---|---|
| `[1, 1, 1, 2, 2, 3]` | 2 | `[1, 2]` |



## Hint

<details>
<summary>Hint</summary>

Counter, then nlargest by frequency.
</details>
