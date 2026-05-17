# 17. Search autocomplete system  `[hard]`

Design `AutocompleteSystem(sentences, times)` and `input(c) -> list[str]`. After each character, return the top 3 matching historical sentences (by frequency desc, then lex asc) for the prefix typed so far. Input `c == '#'` ends a sentence and adds it to history.

## Function signature

```python
class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]) -> None: ...
    def input(self, c: str) -> list[str]: ...
```

## Examples

```
ac = AutocompleteSystem(["i love you","island","ironman","i love leetcode"], [5,3,2,2])
ac.input('i') -> ["i love you","island","i love leetcode"]
ac.input(' ') -> ["i love you","i love leetcode"]
ac.input('a') -> []
ac.input('#') -> []
```



## Hint

<details>
<summary>Hint</summary>

Trie keyed by character; each node holds a Counter of sentences passing through it (or you re-aggregate at query time).
</details>
