# Напишіть функцію create_cache, яка повертає дві функції:
# get_cached для отримання значення з кешу за ключем і set_cached для збереження значення в кеші.
def create_cache():
    """
    Створює простий кеш для зберігання результатів обчислень

    Приклад використання:
    >>> get_cached, set_cached = create_cache()
    >>> set_cached('key1', 'value1')
    >>> get_cached('key1')  # поверне 'value1'
    >>> get_cached('key2')  # поверне None
    """
    cache = {}

    def get_cached(key):
        return cache.get(key)

    def set_cached(key, value):
        cache[key] = value

    return get_cached, set_cached


# Тестування
get_cached, set_cached = create_cache()
set_cached("user_1", {"name": "John", "age": 30})
print(f"Дані з кешу: {get_cached('user_1')}")  # {'name': 'John', 'age': 30}
