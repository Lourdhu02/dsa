def hanoi(n: int) -> list[tuple[str, str]]:
    """T(n) = 2 T(n-1) + 1 = 2^n - 1 moves.  Space: Θ(n) stack."""
    moves: list[tuple[str, str]] = []

    def _solve(k: int, src: str, dst: str, via: str) -> None:
        if k == 0:
            return
        _solve(k - 1, src, via, dst)
        moves.append((src, dst))
        _solve(k - 1, via, dst, src)

    _solve(n, "A", "C", "B")
    return moves
