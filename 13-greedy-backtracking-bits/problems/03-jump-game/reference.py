def can_jump(nums: list[int]) -> bool:
    furthest = 0
    for i, x in enumerate(nums):
        if i > furthest:
            return False
        if i + x > furthest:
            furthest = i + x
    return True
