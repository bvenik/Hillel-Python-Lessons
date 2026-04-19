from lesson8_3 import create_calculator
import pytest


def test_operation_add():
    add = create_calculator('+')
    assert add(5, 5) == 10
    assert add(-1, 1) == 0


@pytest.mark.parametrize("x, y, result", [
    (2, 3, -1),
    (-6, -3, -3),
    (10, 0, 10),
])
def test_operation_subtract(x, y, result):
    sub = create_calculator('-')
    assert sub(x, y) == result


def test_operation_multiply():
    mul = create_calculator('*')
    assert mul(3, 3) == 9
    assert mul(10, 0) == 0


def test_operation_divide():
    div = create_calculator('/')
    assert div(10, 2) == 5.0
    assert div(5, 0) == "Error, division by zero"


def test_operation_power():
    pwr = create_calculator('^')
    assert pwr(2, 3) == 8
    assert pwr(16, 0.5) == 4.0


def test_operation_unknown():
    unknown = create_calculator('?')
    assert unknown(1, 1) == "Error, invalid/unknown operator"
