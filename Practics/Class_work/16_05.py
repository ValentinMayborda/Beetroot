"""Перевірити, чи впорядкований список за зростанням.
numbers = [1, 2, 3, 5, 4]
"""
numbers = [1, 2, 3, 5, 6]

i = 0
is_sorted = True
while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
    i += 1

print(is_sorted)




