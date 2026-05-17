def reverse_string(s: list[str]) -> None:
    def _rec(l: int, r: int) -> None:
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        _rec(l + 1, r - 1)

    _rec(0, len(s) - 1)
