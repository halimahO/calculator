import pytest
from src.calculator import calculator


def test_add():
    calc = calculator.Calculator()
    assert calc.add(4) == 4, "Addition method fails"

def test_subtract():
    calc = calculator.Calculator(4)
    assert calc.subtract(2) == 2, "Subtraction method fails"

def test_multiply():
    calc = calculator.Calculator(4)
    assert calc.multiply(4) == 16, "Multiply method fails"

def test_division():
    calc = calculator.Calculator(4)
    assert calc.divide(2) == 2, "Division method fails"

def test_root():
    calc = calculator.Calculator(8)
    assert calc.root(3) == 2, "Root method fails"

def test_reset():
    calc = calculator.Calculator(5)
    assert calc.reset() == 0, "Reset method fails"

def test_type_error():
    calc = calculator.Calculator(5)
    with pytest.raises(TypeError) as error:
        calc.add("asdf")
    assert str(error.value.args[0]) == "Please input a valid number!"

def test_division_by_zero():
    calc = calculator.Calculator(5)
    with pytest.raises(ZeroDivisionError) as error:
        calc.divide(0)
    assert str(error.value.args[0]) == "Division by zero is invalid!"

def test_validate_init_method():
    with pytest.raises(ValueError) as error:
        calculator.Calculator("asdf")
    assert str(error.value.args[0]) == "Please initialize calculator with a valid number for memory value!"

def test_complex_number():
    calc = calculator.Calculator(-9)
    with pytest.raises(ValueError) as error:
        calc.root(2)
    assert str(error.value.args[0]) == "Root of complex or negative numbers is not allowed"