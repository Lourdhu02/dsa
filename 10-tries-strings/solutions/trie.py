"""A simple alphabet-agnostic trie."""

from __future__ import annotations


class Trie:
    """Hash-map-backed trie.

    insert / contains / startswith: Θ(L) where L = key length.
    """

    def __init__(self) -> None:
        self._root: dict = {}

    _END = "$"

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self._END] = True

    def contains(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and self._END in node

    def startswith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, s: str) -> dict | None:
        node = self._root
        for ch in s:
            node = node.get(ch)
            if node is None:
                return None
        return node
