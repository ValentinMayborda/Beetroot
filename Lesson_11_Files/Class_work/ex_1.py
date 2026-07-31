"""
Програма читає та підраховує кількість слів у кожному рядку файлу.
Ім'я файлу та кількість рядків передаються як аргументи командного рядка.
"""
import sys

if len(sys.argv) != 3:
    print('For use: python ex_1.py <file_name> <count_number>')
    sys.exit(1)


try:
    lines_to_read = int(sys.argv[2])
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, 1):
            if i > lines_to_read:
                break
            words = len(line.strip().split())
            print(f"Row {i}: {words} words - {line.strip()}")
except ValueError:
    print('Error: count_number should be int')
except OSError as error:
    print('Error: access to file')
except Exception as err:
    print('Unknown error')
