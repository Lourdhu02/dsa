def single_number_ii(nums: list[int]) -> int:
    out = 0
    for b in range(32):
        cnt = sum((x >> b) & 1 for x in nums)
        if cnt % 3:
            out |= 1 << b
    if out >= 1 << 31:  # interpret as signed 32-bit
        out -= 1 << 32
    return out
