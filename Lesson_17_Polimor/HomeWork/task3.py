"""
Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для
 дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

"""
from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int):

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError('Значення мають бути Int -го типу')

        if denominator == 0:
            raise ZeroDivisionError('Ділення на нуль')

        # Скорочення дробів
        divisor = gcd(numerator, denominator)

        self.numerator = numerator // divisor
        self.denominator = denominator // divisor


    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        return f'Дріб - {self.numerator}/{self.denominator}'

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        # a/b + c/d = (a*d + c*b)/(b*d)
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        # a/b - c/d = (a*d - c*b)/(b*d)
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        # a/b * c/d = (a*c)/(b*d)
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError

        #  a/b ÷ c/d = (a*d)/(b*c)
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator > other.numerator * self.denominator


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
    print(x + y == Fraction(3, 4))
    print(x + y)
    print(y - x)
    print(x * y)
    print(x / y)
    print( x < y)
    print(x == y)
    print(x > y)
