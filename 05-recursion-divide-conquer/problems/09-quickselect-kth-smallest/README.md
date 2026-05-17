# 09. Kth smallest (quickselect)  `[medium]`

Return the `k`-th smallest element (1-indexed) of an array using quickselect. Expected `Θ(n)`.

## Function signature

```python
def kth_smallest(nums: list[int], k: int) -> int: ...
```

## Examples

| nums | k | result |
|---|---|---|
| `[3, 2, 1, 5, 6, 4]` | 2 | 2 |
| `[3, 2, 3, 1, 2, 4, 5, 5, 6]` | 4 | 3 |

## Constraints

- `1 <= k <= len(nums)`


## Hint

<details>
<summary>Hint</summary>

Same partition as quicksort; recurse only into the side containing position `k - 1` (0-indexed).
</details>
