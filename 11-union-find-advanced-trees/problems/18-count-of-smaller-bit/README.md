# 18. Count of smaller numbers after self (BIT)  `[hard]`

Same as module 06 #18 but solve with a BIT instead of merge-sort.

## Function signature

```python
def count_smaller(nums: list[int]) -> list[int]: ...
```

## Examples

| nums | counts |
|---|---|
| `[5, 2, 6, 1]` | `[2, 1, 1, 0]` |



## Hint

<details>
<summary>Hint</summary>

Coordinate-compress `nums` to ranks. Iterate right to left; query prefix(rank-1) then add 1 at rank.
</details>
