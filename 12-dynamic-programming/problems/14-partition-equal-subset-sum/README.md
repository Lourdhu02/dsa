# 14. Partition equal subset sum  `[medium]`

Return True if `nums` can be partitioned into two subsets with equal sum.

## Function signature

```python
def can_partition(nums: list[int]) -> bool: ...
```

## Examples

| nums | result |
|---|---|
| `[1, 5, 11, 5]` | True |
| `[1, 2, 3, 5]` | False |



## Hint

<details>
<summary>Hint</summary>

0/1 knapsack: can we hit subset sum = total/2.
</details>
