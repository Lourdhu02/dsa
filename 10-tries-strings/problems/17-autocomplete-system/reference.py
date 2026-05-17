import heapq
from collections import Counter, defaultdict


class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]) -> None:
        self._counts: Counter = Counter()
        for s, t in zip(sentences, times):
            self._counts[s] += t
        self._buf: list[str] = []

    def input(self, c: str) -> list[str]:
        if c == "#":
            sentence = "".join(self._buf)
            self._counts[sentence] += 1
            self._buf.clear()
            return []
        self._buf.append(c)
        prefix = "".join(self._buf)
        candidates = [(-cnt, s) for s, cnt in self._counts.items() if s.startswith(prefix)]
        heapq.heapify(candidates)
        out: list[str] = []
        for _ in range(3):
            if not candidates:
                break
            _, s = heapq.heappop(candidates)
            out.append(s)
        return out
