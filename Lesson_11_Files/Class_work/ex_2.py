"""
Читає та аналізує останні N рядків файлу, підраховуючи кількість символів.
Ім'я файлу передається як аргумент командного рядка.
"""
import sys

LAST_LINES = 5

if len(sys.argv) != 2:
    print('For use: python ex_1.py <file_name>')
    sys.exit(1)

try:
    buffer = []
    with open(sys.argv[1], 'r', encoding='utf-8') as file_obj:
        for line in file_obj:
            buffer.append(line.strip())
            if len(buffer) > LAST_LINES:
                buffer.pop(0)
    for i, line in enumerate(buffer, 1):
        char_count = len(line)
        print(f"Row {i} (end): {char_count} symbols - {line}")
except OSError as error:
    print('Error: access to file')
except Exception as err:
    print('Unknown error')
