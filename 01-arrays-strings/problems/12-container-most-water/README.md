# 12. Container with most water  `[medium]`

Given `n` non-negative integers `height[i]` representing vertical lines, find two lines that, together with the x-axis, form a container holding the most water. Return the max area.

Area between lines `i < j` is `(j - i) * min(height[i], height[j])`.

## Function signature

```python
def max_area(height: list[int]) -> int: ...
```

## Examples

| height | answer |
|---|---|
| `[1,8,6,2,5,4,8,3,7]` | 49 |
| `[1,1]` | 1 |
| `[4,3,2,1,4]` | 16 |

## Hint

<details>
<summary>Hint</summary>

Two pointers at the ends. Move the shorter side inward — the longer side is dominating the min already, so shrinking width with the longer side fixed can only equal or worsen the area. Moving the shorter side is the only way to potentially improve.
</details>

## Proof sketch

Suppose at step k we have pointers `l, r` with `height[l] <= height[r]`. The maximum area attainable with `l` fixed (and any `r' < r`) is `(r' - l) * min(height[l], height[r'])`. Since `r' - l < r - l` and `min(height[l], height[r']) <= height[l]`, no `r' < r` can beat the area at `(l, r)` *given that we keep `l`*. So discarding `l` is safe. By symmetry, the same holds when `height[r] < height[l]`. The pointer that's discarded never participates in the optimal pair (CLRS exchange-argument style).
