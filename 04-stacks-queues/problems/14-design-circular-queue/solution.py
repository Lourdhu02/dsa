class MyCircularQueue:
    def __init__(self, k: int) -> None:
        raise NotImplementedError

    def en_queue(self, value: int) -> bool:
        raise NotImplementedError

    def de_queue(self) -> bool:
        raise NotImplementedError

    def front(self) -> int:
        raise NotImplementedError

    def rear(self) -> int:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError
