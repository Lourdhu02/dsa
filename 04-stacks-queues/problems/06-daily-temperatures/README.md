# 06. Daily temperatures  `[medium]`

Given an array `temps` of daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If no such day exists, `answer[i] = 0`.

## Function signature

```python
def daily_temperatures(temps: list[int]) -> list[int]: ...
```

## Examples

| temps | answer |
|---|---|
| `[73, 74, 75, 71, 69, 72, 76, 73]` | `[1, 1, 4, 2, 1, 1, 0, 0]` |
| `[30, 40, 50, 60]` | `[1, 1, 1, 0]` |
| `[30, 60, 90]` | `[1, 1, 0]` |



## Hint

<details>
<summary>Hint</summary>

Same monotonic stack as next-greater, but record `i - stack.pop()` instead of the value.
</details>
