def heap_sort(nums: list[int]) -> None:
    """Time: Θ(n log n).  Space: Θ(1)."""
    n = len(nums)

    def _sift_down(start, end):
        i = start
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < end and nums[l] > nums[largest]:
                largest = l
            if r < end and nums[r] > nums[largest]:
                largest = r
            if largest == i:
                return
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest

    for i in range(n // 2 - 1, -1, -1):
        _sift_down(i, n)
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        _sift_down(0, end)
