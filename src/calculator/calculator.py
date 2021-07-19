class Calculator:
    """
    A class to represent a calculator.

    ...

    Attributes
    ----------
    memory_value : float
        value in calculator memory
    """

    def __init__(self, memory_value: float = 0):
        self._memory_value = self._validate_memory_value(memory_value)
        """
        Constructs the necessary attributes for the calculator object.

        Parameters
        ----------
        memory_value : float
            value of the memory
        """

    def add(self, input_value: float) -> float:
        """Takes in a value and add it to the value in memory, returns the addition."""
        self._validate_input(input_value)
        self._memory_value += input_value
        return self._memory_value

    def subtract(self, input_value: float) -> float:
        """Takes in a value and subtract it from the value in memory, returns the subtraction."""
        self._validate_input(input_value)
        self._memory_value -= input_value
        return self._memory_value

    def multiply(self, input_value: float) -> float:
        """Takes in a value and multiply it with the value in memory, returns the multiplication."""
        self._validate_input(input_value)
        self._memory_value *= input_value
        return self._memory_value

    def divide(self, input_value: float) -> float:
        """Takes in a value and divide it by the value in memory, returns the division."""
        self._validate_input(input_value)
        self._division_by_zero(input_value)
        self._memory_value /= input_value
        return self._memory_value

    def root(self, input_value: float) -> float:
        """Takes in a value n, return the nth root of the value in memory."""
        self._validate_input(input_value)
        self._division_by_zero(input_value)
        self._complex_number_for_root(input_value)
        self._memory_value = self._memory_value ** (1.0 / input_value)
        return self._memory_value


    def reset(self) -> float:
        """Resets the value in memory to zero."""
        self._memory_value = 0
        return self._memory_value

    def _validate_memory_value(self, new_value: float) -> float:
        if not isinstance(new_value, (int, float)):
            raise ValueError("Please initialize calculator with a valid number for memory value!")
        self._memory_value = new_value
        return self._memory_value

    def _validate_input(self, input_value: float) -> float:
        if isinstance(input_value, (int, float)):
            return input_value
        raise TypeError("Please input a valid number!")

    def _division_by_zero(self, input_value: float) -> float:
        if input_value == 0:
            raise ZeroDivisionError("Division by zero is invalid!")
        return input_value


    def _complex_number_for_root(self, input_value: float) -> float:
        if self._memory_value < 0:
            raise ValueError("Root of complex or negative numbers is not allowed")
        return input_value
