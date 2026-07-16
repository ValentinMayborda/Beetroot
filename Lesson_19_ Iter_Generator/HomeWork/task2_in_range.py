"""
Створіть власну реалізацію функції range, назвавши її in_range().

Функція приймає:

start
end
необов'язковий step

Підказка: перегляньте документацію функції range.
"""


def in_range(start: int, end: int, step: int = 1):
    current = start

    if step == 0:
        raise ValueError('Крок не може бути 0!')

    if step > 0:
        while current < end:
            yield current
            current += step

    # step < 0
    else:
        while current > end:
            yield current
            current += step


# for i in in_range(1, 10, 2):
#     print(i)

# for i in in_range(10, 1, -2):
#     print(i)

# for i in in_range(-10, 1, 2):
#     print(i)

# for i in in_range(10, 1, 0):
#     print(i)

# for i in in_range(1, 10):
#      print(i)