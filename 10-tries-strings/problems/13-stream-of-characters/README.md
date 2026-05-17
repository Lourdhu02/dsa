# 13. Stream of characters  `[hard]`

Implement `StreamChecker(words)` and `query(letter) -> bool`. After each `query`, return True if the suffix of the stream matches any word in `words`.

## Function signature

```python
class StreamChecker:
    def __init__(self, words: list[str]) -> None: ...
    def query(self, letter: str) -> bool: ...
```

## Examples

```
sc = StreamChecker(["cd","f","kl"])
sc.query("a") -> False
sc.query("b") -> False
sc.query("c") -> False
sc.query("d") -> True

```



## Hint

<details>
<summary>Hint</summary>

Build a trie of REVERSED words. Maintain the stream in reverse (or just iterate the suffix backward) walking the trie until a word-end or mismatch.
</details>
