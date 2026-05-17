def find_max(xs: list[int]) -> int:
    """Max via single pass with explicit invariant.

    Time:  Θ(n)
    Space: Θ(1)
    """
    if not xs:
        raise ValueError("xs must be non-empty")
    best = xs[0]
    # Invariant: best == max(xs[0..i-1]) at the top of iteration i.
    for i in range(1, len(xs)):
        if xs[i] > best:
            best = xs[i]
    return best
