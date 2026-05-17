def subsets(nums: list[int]) -> list[list[int]]:
    """Time: Θ(n · 2^n).  Space: Θ(n) recursion."""
    out: list[list[int]] = []
    cur: list[int] = []

    def _rec(i: int) -> None:
        if i == len(nums):
            out.append(cur[:])
            return
        _rec(i + 1)
        cur.append(nums[i])
        _rec(i + 1)
        cur.pop()

    _rec(0)
    return out
