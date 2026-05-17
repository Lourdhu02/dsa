from collections import Counter


def num_rabbits(answers: list[int]) -> int:
    """Time: Θ(n).  Space: Θ(n)."""
    total = 0
    for a, cnt in Counter(answers).items():
        group_size = a + 1
        groups = -(-cnt // group_size)  # ceil division
        total += groups * group_size
    return total
