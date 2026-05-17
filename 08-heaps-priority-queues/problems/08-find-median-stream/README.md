# 08. Find median from stream  `[hard]`

Design `MedianFinder.add_num(num)` (Θ(log n)) and `find_median() -> float` (Θ(1)) that maintains the running median of all numbers added so far.

## Function signature

```python
class MedianFinder:
    def add_num(self, num: int) -> None: ...
    def find_median(self) -> float: ...
```

## Examples

```
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
mf.find_median()   # 1.5
mf.add_num(3)
mf.find_median()   # 2
```



## Hint

<details>
<summary>Hint</summary>

Two heaps: max-heap `lo` and min-heap `hi`. Keep sizes balanced within 1.
</details>
