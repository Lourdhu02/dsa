class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """O(1) avg per op via dict + doubly-linked list."""

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.map: dict[int, _Node] = {}
        self.head = _Node(0, 0)
        self.tail = _Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        self._move_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node is not None:
            node.value = value
            self._move_front(node)
            return
        if len(self.map) == self.cap:
            self._evict()
        node = _Node(key, value)
        self.map[key] = node
        self._insert_front(node)

    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        nxt = self.head.next
        node.prev = self.head
        node.next = nxt
        self.head.next = node
        nxt.prev = node

    def _move_front(self, node):
        self._unlink(node)
        self._insert_front(node)

    def _evict(self):
        lru = self.tail.prev
        self._unlink(lru)
        del self.map[lru.key]
