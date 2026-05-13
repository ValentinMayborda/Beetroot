"""Найбільше число

Напиши програму на Python, яка знаходить найбільше число у списку випадкових чисел довжиною 10 елементів.

Обмеження: використовуй лише цикл while та модуль random для генерації чисел."""
import random

list_numbers = []

i = 0
while i < 10:
    list_numbers.append(random.randint(1, 100))
    i += 1

print(f'Наш список: {list_numbers}')
print(f'Найбільше число у списку: {max(list_numbers)}')
