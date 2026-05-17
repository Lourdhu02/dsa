# 16. Spiral matrix  `[medium]`

Given an `m x n` matrix, return all its elements in **spiral order** (right, down, left, up, ... peeling layers).

## Function signature

```python
def spiral_order(matrix: list[list[int]]) -> list[int]: ...
```

## Examples

```
[[1,2,3],
 [4,5,6],
 [7,8,9]]   -> [1,2,3,6,9,8,7,4,5]
```

## Hint

<details>
<summary>Hint</summary>

Track four bounds: `top, bottom, left, right`. In each iteration walk one full layer:
1. Left to right along `top`, then `top += 1`.
2. Top to bottom along `right`, then `right -= 1`.
3. If `top <= bottom`: right to left along `bottom`, then `bottom -= 1`.
4. If `left <= right`: bottom to top along `left`, then `left += 1`.
Repeat while `top <= bottom and left <= right`.
</details>
