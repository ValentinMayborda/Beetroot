"""
Створіть власну реалізацію вбудованої функції enumerate, назвавши її with_index.

Функція повинна приймати два параметри:

iterable — будь-який ітерований об'єкт (список, рядок, кортеж тощо);
start — початковий індекс (за замовчуванням 0).

Підказка: перегляньте документацію функції enumerate.
"""

def with_index(iterable, start: int = 0):

    index = start
    for item in iterable:
        yield index, item
        index += 1


#with_index(['a','b', 'c', 'd'],  1)
lst = ['a','b', 'c', 'd']

for i in with_index(lst, 1):
    print(*i)
