# 05. House robber II (circular)  `[medium]`

Same as house-robber but houses form a circle (first and last are adjacent).

## Function signature

```python
def rob_circular(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[2, 3, 2]` | 3 |
| `[1, 2, 3, 1]` | 4 |



## Hint

<details>
<summary>Hint</summary>

Two passes: rob houses [0..n-2] and [1..n-1]; max of the two.
</details>
