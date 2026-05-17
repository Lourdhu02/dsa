class StreamChecker:
    _END = "$"

    def __init__(self, words: list[str]) -> None:
        self._root: dict = {}
        for w in words:
            node = self._root
            for ch in reversed(w):
                node = node.setdefault(ch, {})
            node[self._END] = True
        self._stream: list[str] = []

    def query(self, letter: str) -> bool:
        self._stream.append(letter)
        node = self._root
        for ch in reversed(self._stream):
            child = node.get(ch)
            if child is None:
                return False
            if self._END in child:
                return True
            node = child
        return False
