# 18. Merge two sorted arrays in place  `[easy]`

`nums1` is sorted, has length `m + n`, and ends with `n` placeholder zeros. `nums2` is sorted and has length `n`. Merge `nums2` into `nums1` so that `nums1` becomes a single sorted array. In place, `O(1)` extra space.

The clean approach is to **fill from the back** with two pointers — that way you never overwrite an unread value of `nums1`.

## Function signature

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None: ...
```

## Examples

| nums1 | m | nums2 | n | result |
|---|---|---|---|---|
| `[1,2,3,0,0,0]` | 3 | `[2,5,6]` | 3 | `[1,2,2,3,5,6]` |
| `[1]` | 1 | `[]` | 0 | `[1]` |
| `[0]` | 0 | `[1]` | 1 | `[1]` |

## Hint

<details>
<summary>Hint</summary>

`i = m-1, j = n-1, k = m+n-1`. While `j >= 0`: if `i >= 0 and nums1[i] > nums2[j]`, write `nums1[i]` to `nums1[k]` and `i -= 1`; else write `nums2[j]` and `j -= 1`. Decrement `k`.
</details>
