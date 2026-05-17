# 03. Word search II (trie + DFS)  `[hard]`

Given a 2D board of letters and a list of words, return all words from the list that can be formed by 4-directionally adjacent cells (each cell used at most once per word).

## Function signature

```python
def find_words(board: list[list[str]], words: list[str]) -> list[str]: ...
```

## Examples

```
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
words = ["oath","pea","eat","rain"]
result = ["oath","eat"]
```



## Hint

<details>
<summary>Hint</summary>

Build a trie of words. DFS each cell against the trie. Mark cells visited; remove leaf words from the trie as found to prune.
</details>
