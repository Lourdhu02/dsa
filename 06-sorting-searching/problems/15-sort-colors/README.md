# 15. Sort colors (Dutch national flag)  `[medium]`

Given an array with values in {0, 1, 2}, sort it in place in `Θ(n)` time, `Θ(1)` space — without using a library sort.

## Function signature

```python
def sort_colors(nums: list[int]) -> None: ...
```

## Examples

| input | result |
|---|---|
| `[2, 0, 2, 1, 1, 0]` | `[0, 0, 1, 1, 2, 2]` |
| `[2, 0, 1]` | `[0, 1, 2]` |



## Hint

<details>
<summary>Hint</summary>

Dutch national flag: three pointers `lo, i, hi`. Walk `i` from 0 to hi. If `nums[i] == 0`, swap with `nums[lo]`, advance both; if 2, swap with `nums[hi]`, decrement hi; if 1, advance i.
</details>
