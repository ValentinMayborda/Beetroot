"""Простий калькулятор

Створіть функцію з назвою make_operation, яка приймає:

простий арифметичний оператор як перший параметр
(для простоти нехай це буде тільки '+', '-' або '*')
довільну кількість аргументів (лише числа) як другий параметр

Функція повинна повертати суму, різницю або добуток усіх переданих чисел.

Приклади:

виклик make_operation('+', 7, 7, 2) повинен повернути 16
виклик make_operation('-', 5, 5, -10, -20) повинен повернути 30
виклик make_operation('*', 7, 6) повинен повернути 42"""
from math import prod

def make_operation(operation, *args):

    if operation == '+':
        return sum(args)

    if operation == '-':
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result

    if operation == '*':
        return prod(args)
    return None


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))