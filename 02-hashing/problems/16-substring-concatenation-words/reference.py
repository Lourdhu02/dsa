from collections import Counter


def find_substring(s: str, words: list[str]) -> list[int]:
    """Word-level sliding window across L offsets.

    Time:  Θ(n * L) where L = len(words[0]).
    Space: Θ(k) where k = len(words).
    """
    if not s or not words or not words[0]:
        return []
    L = len(words[0])
    k = len(words)
    target = Counter(words)
    n = len(s)
    out: list[int] = []
    for offset in range(L):
        l = offset
        count = 0
        window: Counter = Counter()
        for r in range(offset, n - L + 1, L):
            w = s[r : r + L]
            if w not in target:
                window.clear()
                count = 0
                l = r + L
                continue
            window[w] += 1
            count += 1
            while window[w] > target[w]:
                window[s[l : l + L]] -= 1
                l += L
                count -= 1
            if count == k:
                out.append(l)
    return out
