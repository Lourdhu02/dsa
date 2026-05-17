from solution import MedianFinder


def test_basic_sequence():
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2


def test_single():
    mf = MedianFinder()
    mf.add_num(5)
    assert mf.find_median() == 5
