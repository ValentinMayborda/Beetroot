# yield
def squares_list(n):
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    return result
print(squares_list(5))

def squares_gen(n):
    for i in range(1, n + 1):
        yield i ** 2  # пауза: повернути i ** 2, запамятати стан

gen = squares_gen(5)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

import sys

lst = [i ** 2 for i in range(1000)]
gen = (i ** 2 for i in range(1000))  # генератоний вираз
print(sys.getsizeof(lst))  # 8856 bytes
print(sys.getsizeof(gen))  # 208 bytes