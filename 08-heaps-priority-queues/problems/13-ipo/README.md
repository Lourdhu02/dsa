# 13. IPO (max capital projects)  `[hard]`

Pick at most `k` projects starting with `w` capital. Each project `i` needs `capital[i]` to start and adds `profits[i]` to your capital. Return the maximum capital after at most k projects.

## Function signature

```python
def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int: ...
```

## Examples

| k | w | profits | capital | result |
|---|---|---|---|---|
| 2 | 0 | `[1, 2, 3]` | `[0, 1, 1]` | 4 |
| 3 | 0 | `[1, 2, 3]` | `[0, 1, 2]` | 6 |



## Hint

<details>
<summary>Hint</summary>

Two heaps: a min-heap of (capital, profit) for not-yet-affordable projects; a max-heap of profits for affordable ones. Each round: move newly affordable to max-heap, take its top.
</details>
