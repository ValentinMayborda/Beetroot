"""Напишіть декоратор, який виводить назву функції та аргументи, передані їй.

Увага! Потрібно виводити інформацію про виклик функції, а не результат її виконання!

Наприклад:

"add called with 4, 5"
"""
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args):

        print(f'{func.__name__} called with {','.join(map(str, args))}')
        return func(*args)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(4, 4, 5, 10)