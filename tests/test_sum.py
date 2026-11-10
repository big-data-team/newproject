from newproject_eadishchev import sum_of_two


def test_one_plus_zero():
    assert sum_of_two(1, 0) == 1


def test_two_plus_two():
    assert sum_of_two(2, 2) == 4
