# 15. Online stock span  `[medium]`

Design a `StockSpanner.next(price)` that returns the *span* of today's price: the number of consecutive days (including today) for which the price was less than or equal to today's. Amortized `Θ(1)` per call.

## Function signature

```python
class StockSpanner:
    def next(self, price: int) -> int: ...
```

## Examples

```
ss = StockSpanner()
ss.next(100)   # 1
ss.next(80)    # 1
ss.next(60)    # 1
ss.next(70)    # 2
ss.next(60)    # 1
ss.next(75)    # 4
ss.next(85)    # 6
```



## Hint

<details>
<summary>Hint</summary>

Stack of `(price, span)` pairs. On a new price, while the top's price is `<= new_price`, pop and add its span. Push `(price, accumulated_span)`. Each entry is pushed and popped at most once across the whole call sequence — amortized `Θ(1)`.
</details>
