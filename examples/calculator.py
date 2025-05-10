class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, a, b):
        result = a + b
        self.memory = result
        return result
