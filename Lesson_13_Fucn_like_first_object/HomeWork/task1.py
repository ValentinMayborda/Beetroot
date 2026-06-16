"""Напишіть програму на Python, яка визначає кількість локальних змінних, оголошених усередині функції."""

def test():
    a = 1
    b = ''
    c = []
    d = {}


print(dir(test))
print(test.__code__)
print(test.__code__.co_nlocals)