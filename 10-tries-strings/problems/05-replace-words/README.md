# 05. Replace words (with shortest root)  `[medium]`

Given a `dictionary` of word roots and a `sentence`, replace every word in the sentence with its shortest root (if any). Words separated by single spaces.

## Function signature

```python
def replace_words(dictionary: list[str], sentence: str) -> str: ...
```

## Examples

```
dictionary=["cat","bat","rat"]
sentence="the cattle was rattled by the battery"
result="the cat was rat by the bat"
```



## Hint

<details>
<summary>Hint</summary>

Build a trie of roots; for each word, walk through it; emit the first complete-root path encountered.
</details>
