from newproject_eadishchev import subtract_of_two


def two():
    return 2


def test_one_minus_zero():
    assert subtract_of_two(1, 0) == 1


def test_four_minus_two():
    assert subtract_of_two(4, 2) == two()
