# 13. Largest component size by common factor  `[hard]`

Two numbers in `nums` are connected if they share a common factor > 1. Return the size of the largest connected component.

## Function signature

```python
def largest_component_size(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[4, 6, 15, 35]` | 4 |
| `[20, 50, 9, 63]` | 2 |
| `[2, 3, 6, 7, 4, 12, 21, 39]` | 8 |



## Hint

<details>
<summary>Hint</summary>

Union each number with its prime factors. Then count the largest group of original numbers (root by primes).
</details>
