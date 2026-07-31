import time

def o_1_example(n):
    return 0  # O(1)

def o_n_example(n):
    total = 0
    for i in range(n):  # O(n)
        total += i
    return total

def o_n2_example(n):
    total = 0
    for i in range(n):
        for j in range(n):  # O(n^2)
            total += i + j
    return total


sizes = [1000, 10_000]

for n in sizes:
    for name, func in (('O(1)', o_1_example),
                       ('O(n)', o_n_example),
                       ('O(n^2)', o_n2_example)):
        start = time.time()
        func(n)
        print(f'{name} для n={n}: time: {time.time() - start:.6f} seconds')