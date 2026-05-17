def product_except_self(nums: list[int]) -> list[int]:
    """Prefix-product left pass, then suffix-product right pass into the same array.

    Time:  Θ(n)
    Space: Θ(1) extra (the output array is not counted by the problem).
    """
    n = len(nums)
    answer = [1] * n
    # Left pass: answer[i] = product of nums[0..i-1].
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]
    # Right pass: multiply in product of nums[i+1..n-1] using a running variable.
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer
