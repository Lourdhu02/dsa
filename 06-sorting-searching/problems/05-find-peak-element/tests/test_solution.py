from solution import find_peak


def _is_peak(nums, i):
    n = len(nums)
    left = nums[i - 1] if i - 1 >= 0 else float("-inf")
    right = nums[i + 1] if i + 1 < n else float("-inf")
    return nums[i] > left and nums[i] > right


def test_simple():
    assert _is_peak([1, 2, 3, 1], find_peak([1, 2, 3, 1]))


def test_multi_peak():
    nums = [1, 2, 1, 3, 5, 6, 4]
    assert _is_peak(nums, find_peak(nums))


def test_singleton():
    assert find_peak([7]) == 0
