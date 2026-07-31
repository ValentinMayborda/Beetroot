from multiprocessing import Pool, cpu_count

import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def count_primes_in_range(rng:tuple)->int:
    start, end = rng
    return sum(1 for n in range(start, end) if is_prime(n))

def multiply(a, b):
    return a * b

if __name__ == '__main__':
    ranges = [
        (0, 250_000),
        (250_000, 500_000),
        (500_000, 750_000),
        (750_000, 1_000_000),
    ]

    print(f'Ядер CPU {cpu_count()}')
    with Pool(processes=4) as pool:
        t = time.perf_counter()
        results = pool.map(count_primes_in_range, ranges)
        print(f'Паралельно: {time.perf_counter() - t:0.2f} c Простих: {sum(results)}')
    with Pool() as pool:
        results = pool.starmap(multiply, [(1,2),(3,4),(5,6),(7,8)])
        print(results)