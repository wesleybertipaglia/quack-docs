class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations and stores the last result in memory.
    """
    def __init__(self):
        """
        Initialize a Calculator object with memory set to 0.
        """
        self.memory = 0

    def add(self, a, b):
        """
        Add two numbers together and store the result in memory.

        Args:
            a: First number to add
            b: Second number to add

        Returns:
            The sum of a and b
        """
        result = a + b
        self.memory = result
        return result