# 11. Find all concatenated words  `[hard]`

Given a list of distinct words, return all words that are concatenations of at least TWO other words from the list.

## Function signature

```python
def find_all_concatenated_words(words: list[str]) -> list[str]: ...
```

## Examples

```
words=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
result=["catsdogcats","dogcatsdog","ratcatdogcat"]
```



## Hint

<details>
<summary>Hint</summary>

DP per word: `can[i]` = True iff `word[:i]` is a concatenation of at least k words. Use a set of all words.
</details>
