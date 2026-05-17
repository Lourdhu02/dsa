# 06. Search a 2D matrix  `[medium]`

Matrix has rows sorted, and the first element of each row is greater than the last element of the previous row. Return whether target is present. `Θ(log(m*n))`.

## Function signature

```python
def search_matrix(matrix: list[list[int]], target: int) -> bool: ...
```

## Examples

```
[[1, 3, 5, 7],
 [10, 11, 16, 20],
 [23, 30, 34, 60]]
target=3   -> True
target=13  -> False
```



## Hint

<details>
<summary>Hint</summary>

Treat the matrix as a flat sorted array of length m*n; binary-search and decode index to (row, col).
</details>
