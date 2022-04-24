
from src.calc import calc


def test_add():
    result = calc("+", 7, 3)
    assert 10 == result

def test_subtract():
    result = calc("-", 7, 3)
    assert 4 == result

def test_multiply():
    result = calc("*", 2, 3)
    assert 6 == result

def test_divide():
    for x, y, result in [(4, 2, 2), (3, 2, 1.5), (-12, -4, 3)]:
        calc_result = calc("/", x, y)
        assert calc_result == result
