def missing_number(nums: list[int]) -> int:
    out = len(nums)
    for i, x in enumerate(nums):
        out ^= i ^ x
    return out
