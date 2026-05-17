# 12. Reverse pairs (BIT)  `[hard]`

Given an array `nums`, return the number of pairs `(i, j)` with `i < j` and `nums[i] > 2 * nums[j]`.

## Function signature

```python
def reverse_pairs(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[1, 3, 2, 3, 1]` | 2 |
| `[2, 4, 3, 5, 1]` | 3 |



## Hint

<details>
<summary>Hint</summary>

Coordinate-compress (the values + 2*values). For each j scanning right, count nums seen so far that are > 2*nums[j] using a BIT keyed by rank.
</details>
