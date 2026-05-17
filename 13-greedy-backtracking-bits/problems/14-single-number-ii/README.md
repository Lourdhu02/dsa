# 14. Single number II (every element appears 3 times except one)  `[medium]`

Same setup as #13 but every element appears EXACTLY THREE times except for one element that appears once. Return the loner. `Θ(n)` time, `Θ(1)` space.

## Function signature

```python
def single_number_ii(nums: list[int]) -> int: ...
```

## Examples

| nums | result |
|---|---|
| `[2, 2, 3, 2]` | 3 |
| `[0, 1, 0, 1, 0, 1, 99]` | 99 |



## Hint

<details>
<summary>Hint</summary>

For each bit position 0..31, count occurrences mod 3 across all elements. Bits with count mod 3 == 1 belong to the loner.
</details>
