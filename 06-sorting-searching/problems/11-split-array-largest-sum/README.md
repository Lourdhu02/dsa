# 11. Split array largest sum  `[hard]`

Split `nums` into exactly `k` non-empty contiguous parts so as to minimize the largest part-sum. Return that minimized largest sum.

## Function signature

```python
def split_array(nums: list[int], k: int) -> int: ...
```

## Examples

| nums | k | result |
|---|---|---|
| `[7, 2, 5, 10, 8]` | 2 | 18 |
| `[1, 2, 3, 4, 5]` | 2 | 9 |
| `[1, 4, 4]` | 3 | 4 |



## Hint

<details>
<summary>Hint</summary>

Binary-search the answer in `[max(nums), sum(nums)]`. The predicate is: can we split into <= k parts each with sum <= x.
</details>
