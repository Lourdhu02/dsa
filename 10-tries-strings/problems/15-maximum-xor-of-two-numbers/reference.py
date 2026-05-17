def find_maximum_xor(nums: list[int]) -> int:
    BITS = 31  # safe for non-negative ints up to 2^31 - 1
    root: dict = {}
    for x in nums:
        node = root
        for i in range(BITS, -1, -1):
            b = (x >> i) & 1
            node = node.setdefault(b, {})
    best = 0
    for x in nums:
        node = root
        cur = 0
        for i in range(BITS, -1, -1):
            b = (x >> i) & 1
            target = 1 - b
            if target in node:
                cur |= (1 << i)
                node = node[target]
            else:
                node = node[b]
        best = max(best, cur)
    return best
