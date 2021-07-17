import pytest
from src.calculator import Calculator
calculator = Calculator()

def test_add():
    calculator.reset()
    assert calculator.add(4) == 4, "Addition method fails"
    calculator.reset()
    assert calculator.add('a') == "Please input a valid number", "Addition method fails"

def test_subtract():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.subtract(2) == 2, "Subtraction method fails"
    calculator.reset()
    assert calculator.subtract('a') == "Please input a valid number", "Subtraction method fails"

def test_multiply():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.multiply(4) == 16, "Multiply method fails"
    calculator.reset()
    assert calculator.multiply('a') == "Please input a valid number", "Multiplication method fails"

def test_division():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.divide(2) == 2, "Division method fails"
    calculator.reset()
    assert calculator.divide(0) == "Please input a valid number! Note that division by zero is invalid", "Division method fails"

def test_root():
    calculator.reset()
    assert calculator.add(8)
    assert calculator.root(3) == 2, "Root method fails"
    calculator.reset()
    assert calculator.add('a') == "Please input a valid number", "Root method fails"

def test_reset():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.reset() == 0, "Reset method fails"

