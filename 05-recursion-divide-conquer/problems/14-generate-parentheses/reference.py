def generate_parenthesis(n: int) -> list[str]:
    out: list[str] = []

    def _bt(s: str, opens: int, closes: int) -> None:
        if len(s) == 2 * n:
            out.append(s)
            return
        if opens < n:
            _bt(s + "(", opens + 1, closes)
        if closes < opens:
            _bt(s + ")", opens, closes + 1)

    _bt("", 0, 0)
    return out
