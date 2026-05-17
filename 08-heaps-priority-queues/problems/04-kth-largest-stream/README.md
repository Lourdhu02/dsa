# 04. Kth largest in stream  `[easy]`

Design `KthLargest(k, nums)` with `add(val) -> int` returning the kth largest element seen so far.

## Function signature

```python
class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None: ...
    def add(self, val: int) -> int: ...
```

## Examples

```
k = 3, nums = [4, 5, 8, 2]
add(3) -> 4
add(5) -> 5
add(10) -> 5
add(9) -> 8
add(4) -> 8
```



## Hint

<details>
<summary>Hint</summary>

Maintain a min-heap of size k. On add, push and trim. Top is the kth largest.
</details>
