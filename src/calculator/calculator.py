class Calculator:
    """
    A class to represent a calculator.

    ...

    Attributes
    ----------
    memory_value : float
        value in calculator memory

    Methods
    -------
    add(self, input_value):
        Adds input value to memory value.

    subtract(self, input_value):
        Subtracts input value from memory value.

    divide(self, input_value):
        Divides input value by memory value.

    multiply(self, input_value):
        Multiplies input value by memory value.

    root(self, input_value):
        Returns the input value root of the memory value.

    reset(self):
        Resets memory value to zero.
        """

    def __init__(self, memory_value: float = 0) -> float:
        self._memory_value = memory_value
        """
        Constructs the necessary attributes for the calculator object.

        Parameters
        ----------
        memory_value : float
            value of the memory
        """

    def add(self, input_value: float) -> float:
        """Takes in a value and add it to the value in memory, returns the addition."""
        self.validate_input(input_value)
        self._memory_value += input_value
        return self._memory_value

    def subtract(self, input_value: float) -> float:
        """Takes in a value and subtract it from the value in memory, returns the subtraction."""
        self.validate_input(input_value)
        self._memory_value -= input_value
        return self._memory_value

    def multiply(self, input_value: float) -> float:
        """Takes in a value and multiply it with the value in memory, returns the multiplication."""
        self.validate_input(input_value)
        self._memory_value *= input_value
        return self._memory_value

    def divide(self, input_value: float) -> float:
        """Takes in a value and divide it by the value in memory, returns the division."""
        self.validate_input(input_value)
        self.division_by_zero(input_value)
        self._memory_value /= input_value
        return self._memory_value

    def root(self, input_value: float) -> float:
        """Takes in a value n, return the nth root of the value in memory."""
        self.validate_input(input_value)
        self.division_by_zero(input_value)
        self._memory_value = self._memory_value ** (1.0 / input_value)
        return self._memory_value


    def reset(self):
        """Resets the value in memory to zero."""
        self._memory_value = 0
        return self._memory_value

    def validate_input(self, input_value):
        if isinstance(input_value, (int, float)):
            return input_value
        raise TypeError("Please input a valid number!")

    def division_by_zero(self, input_value):
        if input_value == 0:
            raise ZeroDivisionError("Division by zero is invalid!")
        return input_value
