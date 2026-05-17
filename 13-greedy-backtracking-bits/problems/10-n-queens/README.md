# 10. N-queens  `[hard]`

Return all valid N-queens board configurations as a list of lists of strings (rows).

## Function signature

```python
def solve_n_queens(n: int) -> list[list[str]]: ...
```

## Examples

| n | result count |
|---|---|
| 4 | 2 |
| 1 | 1 |



## Hint

<details>
<summary>Hint</summary>

Place row by row. Track 3 sets: occupied columns, occupied diagonals (`r - c`), occupied anti-diagonals (`r + c`).
</details>
