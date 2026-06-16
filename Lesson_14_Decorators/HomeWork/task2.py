"""Завдання 2
Напишіть декоратор, який приймає список заборонених слів (stop words) і замінює їх на символ * у результаті роботи декорованої функції.
"""
import functools

def stop_words(words: list):
    def stop_words_decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            result = func(*args)

            for word in words:
                result = result.replace(word, '*')

            return result
        return wrapper
    return stop_words_decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"