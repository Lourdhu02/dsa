# 12. Word search  `[medium]`

Given a 2D board of letters and a word, return True if the word can be formed by 4-directionally adjacent cells (each cell used at most once).

## Function signature

```python
def exist(board: list[list[str]], word: str) -> bool: ...
```

## Examples

```
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCCED"   -> True
word = "SEE"     -> True
word = "ABCB"    -> False
```



## Hint

<details>
<summary>Hint</summary>

DFS with visited mark; restore on backtrack.
</details>
