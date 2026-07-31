# Функція може бути передана в іншу функцію як аргумент

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def math_operation(a, b, func):  # func - передаємо якусь ф-цію як параметр
    return func(a, b)


result = math_operation(2, 3, mul)  # передаємо ф-цію  mul як параметр
print(result)

result = math_operation(2, 3, add)  # передаємо ф-цію   add як параметр
print(result)