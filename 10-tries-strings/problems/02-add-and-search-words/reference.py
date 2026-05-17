class WordDictionary:
    _END = "$"

    def __init__(self) -> None:
        self._root: dict = {}

    def add_word(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self._END] = True

    def search(self, word: str) -> bool:
        def _dfs(node, i):
            if i == len(word):
                return self._END in node
            ch = word[i]
            if ch == ".":
                for k, child in node.items():
                    if k == self._END:
                        continue
                    if _dfs(child, i + 1):
                        return True
                return False
            child = node.get(ch)
            return False if child is None else _dfs(child, i + 1)

        return _dfs(self._root, 0)
