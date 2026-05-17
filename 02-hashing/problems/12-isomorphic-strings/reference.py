def is_isomorphic(s: str, t: str) -> bool:
    """Time: Θ(n).  Space: Θ(σ)."""
    if len(s) != len(t):
        return False
    fwd: dict[str, str] = {}
    rev: dict[str, str] = {}
    for a, b in zip(s, t):
        if a in fwd:
            if fwd[a] != b:
                return False
        else:
            if b in rev:
                return False
            fwd[a] = b
            rev[b] = a
    return True
