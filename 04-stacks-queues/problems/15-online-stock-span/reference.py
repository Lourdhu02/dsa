class StockSpanner:
    def __init__(self) -> None:
        self._stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self._stack and self._stack[-1][0] <= price:
            span += self._stack.pop()[1]
        self._stack.append((price, span))
        return span
