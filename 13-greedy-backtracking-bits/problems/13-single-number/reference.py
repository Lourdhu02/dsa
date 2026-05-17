def single_number(nums: list[int]) -> int:
    out = 0
    for x in nums:
        out ^= x
    return out
