# 09. Surrounded regions  `[medium]`

Given an `m x n` board of `'X'` and `'O'`, capture all regions of `'O'` that are NOT connected to a border `'O'`. Flip captured `'O'`s to `'X'`.

## Function signature

```python
def solve(board: list[list[str]]) -> None: ...
```

## Examples

Border-connected `O`s survive; interior `O`s become `X`.



## Hint

<details>
<summary>Hint</summary>

DFS/BFS from each border `O`, marking with a sentinel. Then sweep: sentinel -> O, O -> X.
</details>
