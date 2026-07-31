class Calculator:

    def __init__(self):
        ...

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 ==0:
            raise ZeroDivisionError('Ділення на нуль неможливе')
        return x1 / x2
