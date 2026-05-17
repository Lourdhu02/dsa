# 02. Design add and search words  `[medium]`

Implement `WordDictionary` with `add_word(word)` and `search(word) -> bool` where `word` may contain `'.'` matching any single letter.

## Function signature

```python
class WordDictionary:
    def add_word(self, word: str) -> None: ...
    def search(self, word: str) -> bool: ...
```

## Examples

```
wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")
wd.search("pad")   # False
wd.search("bad")   # True
wd.search(".ad")   # True
wd.search("b..")   # True
```



## Hint

<details>
<summary>Hint</summary>

Trie. On `'.'`, recurse into all children of the current node.
</details>
