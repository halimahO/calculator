import pytest
from src.calculator import calculator

calculator = calculator.Calculator()

def test_add():
    calculator.reset()
    assert calculator.add(4) == 4, "Addition method fails"

def test_subtract():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.subtract(2) == 2, "Subtraction method fails"

def test_multiply():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.multiply(4) == 16, "Multiply method fails"

def test_division():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.divide(2) == 2, "Division method fails"

def test_root():
    calculator.reset()
    assert calculator.add(8)
    assert calculator.root(3) == 2, "Root method fails"

def test_reset():
    calculator.reset()
    assert calculator.add(4)
    assert calculator.reset() == 0, "Reset method fails"

def test_type_error():
    with pytest.raises(TypeError) as error:
        calculator.validate_input("a")
    assert str(error.value.args[0]) == "Please input a valid number!"

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as error:
        calculator.division_by_zero(0)
    assert str(error.value.args[0]) == "Division by zero is invalid!"