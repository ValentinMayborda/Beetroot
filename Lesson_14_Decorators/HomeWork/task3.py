"""Напишіть декоратор arg_rules, який перевіряє аргументи, передані функції.

Декоратор повинен приймати 3 параметри:

max_length: 15 — максимальна довжина аргументу;
type_: str — очікуваний тип аргументу;
contains: [] — список символів або підрядків, які обов'язково повинні бути присутні в аргументі.

Якщо будь-яка з перевірок повертає False, функція повинна:

Вивести причину помилки;
Повернути False.

Якщо всі перевірки пройдені успішно, потрібно повернути результат виконання функції.
"""
import functools

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            value = args[0]

            if not isinstance(value, type_):
                print("Не той тип аргументу")
                return False

            if len(value) > max_length:
                print("Перевищено максимальну довжину аргумента")
                return False

            for elem in contains:
                if elem not in value:
                    print(f"Відсутня обов'зкова частина: {elem}")
                    return False

            return func(*args)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('joh.com'))
print(create_slogan('S@SH05'))

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'