from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
import time
import math
import sys

sys.set_int_max_str_digits(100_000)


def heavy_math(n:int)->dict:
    start = time.perf_counter()
    result =math.factorial(n)
    digits = len(str(result))
    elapsed = time.perf_counter() - start
    return {'n': n, 'digits': digits, 'time': elapsed}


if __name__ == '__main__':
    numbers = [5000, 8000, 10000, 6000, 4000]
    with ProcessPoolExecutor(max_workers=4) as executor:
        t = time.perf_counter()
        results = list(executor.map(heavy_math, numbers))
        print(f'map() завершено за {time.perf_counter() - t:2f}c')
        for r in results:
            print(f'{r['n']}! -> {r["digits"]} цифр за {r['time']}')

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(heavy_math, n):n for n in numbers}
        for future in as_completed(futures):
            n = futures[future]
            try:
                data = future.result(timeout=30)
                print(f'{n}! -> {data}')
            except Exception as e:
                print(f'{n}! -> {e}')

