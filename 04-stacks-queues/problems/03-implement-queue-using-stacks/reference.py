class MyQueue:
    """Amortized O(1) per op: each element is pushed and popped on each stack at most once."""

    def __init__(self) -> None:
        self._in: list[int] = []
        self._out: list[int] = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self._shift()
        return self._out.pop()

    def peek(self) -> int:
        self._shift()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out

    def _shift(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
