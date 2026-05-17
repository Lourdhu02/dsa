# 11. Sudoku solver  `[hard]`

Solve a 9x9 Sudoku in place. Empty cells are `'.'`.

## Function signature

```python
def solve_sudoku(board: list[list[str]]) -> None: ...
```

## Examples

Standard 9x9 sudoku grid; modify in place to a valid solution.



## Hint

<details>
<summary>Hint</summary>

Backtrack cell by cell. Maintain row/col/box sets of used digits for O(1) check.
</details>
