# 08. Word ladder  `[hard]`

Given two words `begin_word` and `end_word`, and a word list, return the length of the shortest transformation sequence — each adjacent pair differs by one letter. Return 0 if impossible. Count both `begin_word` and `end_word`.

## Function signature

```python
def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int: ...
```

## Examples

| begin | end | wordList | result |
|---|---|---|---|
| `"hit"` | `"cog"` | `["hot","dot","dog","lot","log","cog"]` | 5 |
| `"hit"` | `"cog"` | `["hot","dot","dog","lot","log"]` | 0 |



## Hint

<details>
<summary>Hint</summary>

Build a wildcard-pattern index: for each word, list `_at`, `c_t`, `ca_` patterns. Two words sharing a pattern are neighbors. BFS.
</details>
