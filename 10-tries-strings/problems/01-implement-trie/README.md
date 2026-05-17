# 01. Implement Trie (prefix tree)  `[medium]`

Implement `Trie` with `insert(word)`, `search(word) -> bool`, `startswith(prefix) -> bool`.

## Function signature

```python
class Trie:
    def insert(self, word: str) -> None: ...
    def search(self, word: str) -> bool: ...
    def startswith(self, prefix: str) -> bool: ...
```

## Examples

```
t = Trie()
t.insert("apple")
t.search("apple")    # True
t.search("app")      # False
t.startswith("app")  # True
t.insert("app")
t.search("app")      # True
```



## Hint

<details>
<summary>Hint</summary>

Dict-of-dicts; an `END` sentinel marks a complete word.
</details>
