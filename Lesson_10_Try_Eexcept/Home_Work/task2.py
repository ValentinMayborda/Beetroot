"""Напишіть функцію, яка отримує від користувача два числа через input(),
 назвіть їх a та b, а потім повертає значення квадрата числа a, поділеного на b.

Створіть блок try-except, який перехоплює виняток, якщо:
значення, введені через input(), не є числами;
значення b дорівнює нулю (ділення на нуль неможливе)."""

def get_numbers():
    while True:
        try:
            #a, b = map(int, input().split())
            a, b = float(input('Введіть число а: ')),float(input('Введіть число b: '))
            return operation(a, b)

        except (ValueError, ZeroDivisionError) as err:
            print('Помилка -', err)

def operation(num1, num2):
    return (num1 * num1) / num2

if __name__ == '__main__':
    while True:
        stop = input('Скрипт повертає значення квадрата числа a, поділеного на b. (Для виходу - q):')
        if stop.lower() == 'q':
            break
        print(get_numbers())
