from collections import defaultdict, deque


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end_word not in words:
        return 0
    patterns: dict[str, list[str]] = defaultdict(list)
    L = len(begin_word)
    for w in words | {begin_word}:
        for i in range(L):
            patterns[w[:i] + "*" + w[i + 1:]].append(w)
    visited = {begin_word}
    q = deque([(begin_word, 1)])
    while q:
        w, d = q.popleft()
        if w == end_word:
            return d
        for i in range(L):
            key = w[:i] + "*" + w[i + 1:]
            for nb in patterns[key]:
                if nb not in visited:
                    visited.add(nb)
                    q.append((nb, d + 1))
            patterns[key] = []
    return 0
