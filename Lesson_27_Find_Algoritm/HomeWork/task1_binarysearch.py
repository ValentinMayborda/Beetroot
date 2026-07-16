"""Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
Визначте складність алгоритму та порівняйте його з бінарним пошуком"""

def binary_search(arr, left, right, target):

    if left > right:
        return f'Елемент {target} не знайдено'

    mid = (right + left) //2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)

    else:
        return binary_search(arr, mid + 1, right, target)


num = [2, 5, 7, 10, 13, 15, 20, 30, 33]
targ = 10

answer = binary_search(num, 0, len(num) - 1, targ)
print(answer)

# O(log n)