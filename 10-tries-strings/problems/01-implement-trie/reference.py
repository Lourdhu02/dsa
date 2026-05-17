class Trie:
    _END = "$"

    def __init__(self) -> None:
        self._root: dict = {}

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self._END] = True

    def _walk(self, s: str):
        node = self._root
        for ch in s:
            node = node.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and self._END in node

    def startswith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
