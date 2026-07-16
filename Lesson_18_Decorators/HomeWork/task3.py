"""
Напишіть клас TypeDecorators, який містить кілька декораторів для перетворення результату функції на певний тип (якщо це можливо).

Необхідно реалізувати такі декоратори:

to_int — перетворює результат функції в int;
to_str — перетворює результат функції в str;
to_bool — перетворює результат функції в bool;
to_float — перетворює результат функції в float.

Не забудьте використовувати декоратор @wraps із модуля functools.
"""

import functools


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)

        return wrapper

    @staticmethod
    def to_str(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_float(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if str(result).lower() in ["true", "1"]:
                return True
            else:
                return False

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
