"""
Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
Визначте складність алгоритму та порівняйте його з бінарним пошуком"""

def fibonacci_search(arr, target):
    n = len(arr)

    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    # пошук числа в послідовності
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    # визначення індексу
    while fib > 1:

        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib -fib1
            offset = i

        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return f'Елемент {target} не знайдено'

num = [2, 5, 7, 10, 13, 15, 20, 30, 33]
targ = 33

answer = fibonacci_search(num, targ)
print(answer)

# O(log n)