
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