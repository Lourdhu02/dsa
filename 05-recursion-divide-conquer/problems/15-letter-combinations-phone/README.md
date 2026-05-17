# 15. Letter combinations of a phone number  `[medium]`

Given a string of digits 2-9, return all possible letter combinations the number could represent on a standard phone keypad.

## Function signature

```python
def letter_combinations(digits: str) -> list[str]: ...
```

## Examples

| digits | result |
|---|---|
| `"23"` | `["ad","ae","af","bd","be","bf","cd","ce","cf"]` |
| `""` | `[]` |
| `"2"` | `["a","b","c"]` |



## Hint

<details>
<summary>Hint</summary>

Standard backtrack. At each position pick one letter from the digit's mapping.
</details>
