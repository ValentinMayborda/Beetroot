"""Напишіть функцію з назвою oops, яка при виклику явно викликає виняток IndexError.
Потім напишіть іншу функцію, яка викликає oops всередині конструкції try/except, щоб перехопити помилку.

Що станеться, якщо змінити oops так, щоб вона викликала KeyError замість IndexError?"""

def oops():
    raise IndexError("oops")

    # raise KeyError("oops")
    # Видає помилку

def call_oops():
    try:
        oops()
    except IndexError:
        print("IndexError inside call_oops")

    # А так не видає помилку - >
    # except KeyError:
    #     print("KeyError inside oops")

call_oops()