def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []
    table = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    out: list[str] = []

    def _bt(i: int, cur: str) -> None:
        if i == len(digits):
            out.append(cur)
            return
        for ch in table[digits[i]]:
            _bt(i + 1, cur + ch)

    _bt(0, "")
    return out
