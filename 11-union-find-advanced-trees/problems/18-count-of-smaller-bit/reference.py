def count_smaller(nums: list[int]) -> list[int]:
    sorted_unique = sorted(set(nums))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    n = len(sorted_unique)
    bit = [0] * (n + 2)

    def update(i):
        while i <= n:
            bit[i] += 1
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    out = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        r = rank[nums[i]]
        out[i] = prefix(r - 1)
        update(r)
    return out
