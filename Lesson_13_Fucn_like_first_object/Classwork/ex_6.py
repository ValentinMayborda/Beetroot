# Напишіть функцію create_counter, яка створює лічильник із початковим значенням start.
# Кожен виклик поверненої функції збільшує значення на 1 і повертає його.
# Використовуйте замикання для збереження стану.
def create_counter(start=0):
    """
    Створює лічильник, який зберігає своє значення між викликами

    Приклад використання:
    >>> counter = create_counter(5)
    >>> counter()  # поверне 6
    >>> counter()  # поверне 7
    """
    count = [start]  # Використовуємо список для можливості модифікації значення

    def counter():
        count[0] += 1
        return count[0]

    return counter


# Тестування
counter = create_counter(5)
print(counter())  # 6
print(counter())  # 7
