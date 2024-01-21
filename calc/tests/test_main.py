
from src.main import suma, minus, advance_minus


def test_suma():
    result = suma(3, 4)
    assert result == 7


def test_minus():
    result = minus(3, 4)
    assert result == -1


def test_advance_minus_shoul_return_0():
    result = advance_minus(2, 3)
    assert result == 0


def test_advance_minus_should_return_number_gte_0():
    result = advance_minus(4, 1)
    assert result == 3
