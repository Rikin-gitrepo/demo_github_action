# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(20, 4) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_modulo():
    assert modulo(10, 3) == 1

def modulo(arg1, arg2):
    raise NotImplementedError

def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(10, 0)