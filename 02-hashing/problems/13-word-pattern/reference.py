def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False
    fwd: dict[str, str] = {}
    rev: dict[str, str] = {}
    for c, w in zip(pattern, words):
        if c in fwd:
            if fwd[c] != w:
                return False
        else:
            if w in rev:
                return False
            fwd[c] = w
            rev[w] = c
    return True
