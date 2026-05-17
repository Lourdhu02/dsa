class MyCircularQueue:
    def __init__(self, k: int) -> None:
        self._cap = k
        self._buf: list[int] = [0] * k
        self._head = 0
        self._size = 0

    def en_queue(self, value: int) -> bool:
        if self._size == self._cap:
            return False
        self._buf[(self._head + self._size) % self._cap] = value
        self._size += 1
        return True

    def de_queue(self) -> bool:
        if self._size == 0:
            return False
        self._head = (self._head + 1) % self._cap
        self._size -= 1
        return True

    def front(self) -> int:
        if self._size == 0:
            return -1
        return self._buf[self._head]

    def rear(self) -> int:
        if self._size == 0:
            return -1
        return self._buf[(self._head + self._size - 1) % self._cap]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._cap
