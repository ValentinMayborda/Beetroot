"""Створіть декоратор, який дозволяє викликати функцію не більше N разів, після чого повертає
повідомлення про перевищення ліміту."""

import functools


def limit_calls(max_calls):
    def decorator(func):

        func.count = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            if func.count < max_calls:
                func.count += 1
                return func(*args, **kwargs)

            else:
                return f'Error {func.__name__} has called {max_calls} times.'


        return wrapper
    return decorator

@limit_calls(2)
def say_hello(name):
    return f'Hello {name}!'

print(say_hello('Valentyn'))
print(say_hello('Stepan'))
print(say_hello('Petro'))