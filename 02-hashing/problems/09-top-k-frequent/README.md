# 09. Top K frequent elements  `[medium]`

Given an integer array `nums` and integer `k`, return the `k` most frequent elements (any order).

## Function signature

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]: ...
```

## Examples

| nums | k | answer (any order) |
|---|---|---|
| `[1,1,1,2,2,3]` | 2 | `[1, 2]` |
| `[1]` | 1 | `[1]` |



## Hint

<details>
<summary>Hint</summary>

Count with `Counter`, then either (a) `Counter.most_common(k)` — Θ(n log n) — or (b) bucket sort by frequency in Θ(n).
</details>
