import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check_numbers(lst_numbers):
    start = time.perf_counter()
    for num in lst_numbers:
        print(f'Число -{num} -> {is_prime(num)}')
    print(f'Просту перевірку завершено за {time.perf_counter() - start:0.2f}c')


def check_numbers_thread(lst_numbers):
    start = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, lst_numbers)

        for num, result in zip(lst_numbers, results):
            print(f'Число {num} -> {result}')

    print(f'\nThreadPoolExecutor завершив роботу за {time.perf_counter() - start:.2f} c')


def check_numbers_process(lst_numbers):
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        results = executor.map(is_prime, lst_numbers)

        for num, result in zip(lst_numbers, results):
            print(f'Число -{num} -> {result}')

    print(f'\nProcessPoolExecutor завершив роботу за {time.perf_counter() - start:.2f} c')


if __name__ == '__main__':
    NUMBERS = [
        2,
        1099726899285419,
        1570341764013157,
        1637027521802551,
        1880450821379411,
        1893530391196711,
        2447109360961063,
        3,
        2772290760589219,
        3033700317376073,
        4350190374376723,
        4350190491008389,
        4350190491008390,
        4350222956688319,
        2447120421950803,
        5,
    ]
    print('=======================Проста перевірка=======================')
    check_numbers(NUMBERS)

    print('=========\nПеревірка з викоистанням ThreadPoolExecutor=========')
    check_numbers_thread(NUMBERS)

    print('=========\nПеревірка з використанням ProcessPoolExecutor========')
    check_numbers_process(NUMBERS)
