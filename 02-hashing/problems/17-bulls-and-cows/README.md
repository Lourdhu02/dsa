# 17. Bulls and cows  `[medium]`

Given a secret number and a guess (both digit strings of the same length), return `"xAyB"` where `x` is the count of digits that are in the right position (bulls) and `y` is the count of digits that are in the secret but in the wrong position (cows).

## Function signature

```python
def get_hint(secret: str, guess: str) -> str: ...
```

## Examples

| secret | guess | result |
|---|---|---|
| `"1807"` | `"7810"` | `"1A3B"` |
| `"1123"` | `"0111"` | `"1A1B"` |



## Hint

<details>
<summary>Hint</summary>

One pass to count bulls. For the rest, count digits in both secret-minus-bulls and guess-minus-bulls and take the per-digit minimum.
</details>
