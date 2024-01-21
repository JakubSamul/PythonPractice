import pytest
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

def test_divide_with_y_as_zero():
    with pytest.raises(ZeroDivisionError):
       calc("/", 1, 0)

def test_wih_invalid_operation():
    result = calc("s", 1, 0)
    assert result == None
