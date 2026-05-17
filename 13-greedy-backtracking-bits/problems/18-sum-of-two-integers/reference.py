def get_sum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a < 0x80000000 else a - 0x100000000
