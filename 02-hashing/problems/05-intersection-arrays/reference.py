def intersection(a: list[int], b: list[int]) -> list[int]:
    """Time: Θ(n + m).  Space: Θ(min(n, m))."""
    sa = set(a)
    return list({x for x in b if x in sa})
