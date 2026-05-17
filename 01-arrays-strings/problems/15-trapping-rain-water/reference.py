def trap(height: list[int]) -> int:
    """Two-pointer trap-water.

    Invariant: ``left_max`` is the max in ``height[0..l-1]`` and
    ``right_max`` is the max in ``height[r+1..n-1]``.  Whichever bar is
    shorter at the current pointer is the limiting wall; advance from there.

    Time:  Θ(n)
    Space: Θ(1)
    """
    n = len(height)
    if n < 3:
        return 0
    l, r = 0, n - 1
    left_max = right_max = 0
    total = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                total += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                total += right_max - height[r]
            r -= 1
    return total
