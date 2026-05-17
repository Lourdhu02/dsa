# 18. Palindrome pairs  `[hard]`

Given a list of unique words, return all pairs of distinct indices `(i, j)` such that `words[i] + words[j]` is a palindrome.

## Function signature

```python
def palindrome_pairs(words: list[str]) -> list[list[int]]: ...
```

## Examples

| words | result |
|---|---|
| `["abcd","dcba","lls","s","sssll"]` | `[[0, 1], [1, 0], [3, 2], [2, 4]]` |



## Hint

<details>
<summary>Hint</summary>

For each word w, split into prefix+suffix at every k. If prefix is palindrome and reverse(suffix) is in the dictionary, that pair works. Map of word -> index for Θ(1) lookup.
</details>
