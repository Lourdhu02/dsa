# 01. Heap sort  `[easy]`

Sort an integer array in place using heap sort. Don't call any library sort.

## Function signature

```python
def heap_sort(nums: list[int]) -> None: ...
```

## Examples

| input | sorted |
|---|---|
| `[3, 1, 4, 1, 5, 9, 2, 6]` | `[1, 1, 2, 3, 4, 5, 6, 9]` |



## Hint

<details>
<summary>Hint</summary>

Build a max-heap in place (Θ(n)). Then repeatedly swap the root with the last element and sift down on the shrinking prefix.
</details>
