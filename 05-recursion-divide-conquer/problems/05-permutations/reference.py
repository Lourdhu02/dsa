def permute(nums: list[int]) -> list[list[int]]:
    """Time: Θ(n · n!).  Space: Θ(n) recursion (+ output)."""
    out: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def _bt() -> None:
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            _bt()
            path.pop()
            used[i] = False

    _bt()
    return out
