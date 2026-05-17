from solution import DynamicArray


def test_basic_push():
    da = DynamicArray()
    for i in range(5):
        da.push(i)
    assert len(da) == 5
    assert [da[i] for i in range(5)] == [0, 1, 2, 3, 4]


def test_amortized_bound():
    # After n pushes total copies must be <= 2n - 1 (geometric series).
    for n in (1, 2, 5, 16, 17, 100, 1024, 1025, 10_000):
        da = DynamicArray()
        for i in range(n):
            da.push(i)
        assert da.copies <= 2 * n - 1, f"violated amortized bound at n={n}: copies={da.copies}"


def test_capacity_at_most_doubled():
    da = DynamicArray()
    for i in range(1000):
        da.push(i)
        assert da.capacity <= 2 * max(len(da), 1)


def test_get_out_of_range():
    import pytest

    da = DynamicArray()
    da.push(1)
    with pytest.raises(IndexError):
        _ = da[5]
