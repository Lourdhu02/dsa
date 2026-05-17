def diff_ways_to_compute(expression: str) -> list[int]:
    memo: dict[str, list[int]] = {}

    def _rec(s: str) -> list[int]:
        if s in memo:
            return memo[s]
        out: list[int] = []
        for i, ch in enumerate(s):
            if ch in "+-*":
                left = _rec(s[:i])
                right = _rec(s[i + 1 :])
                for a in left:
                    for b in right:
                        if ch == "+":
                            out.append(a + b)
                        elif ch == "-":
                            out.append(a - b)
                        else:
                            out.append(a * b)
        if not out:
            out = [int(s)]
        memo[s] = out
        return out

    return _rec(expression)
