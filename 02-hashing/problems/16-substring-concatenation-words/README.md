# 16. Substring with concatenation of all words  `[hard]`

Given a string `s` and a list of equal-length `words`, return the starting indices of substrings of `s` that are a concatenation of EACH word exactly once (any order, no in-between characters).

## Function signature

```python
def find_substring(s: str, words: list[str]) -> list[int]: ...
```

## Examples

| s | words | result |
|---|---|---|
| `"barfoothefoobarman"` | `["foo","bar"]` | `[0, 9]` |
| `"wordgoodgoodgoodbestword"` | `["word","good","best","word"]` | `[]` |
| `"barfoofoobarthefoobarman"` | `["bar","foo","the"]` | `[6, 9, 12]` |



## Hint

<details>
<summary>Hint</summary>

Each word has length L. For each starting offset in [0, L), use a sliding window of L words. Maintain a counter; compare to `Counter(words)`.
</details>
