# Реалізуйте клас TransactionalList, який працює як список, але підтримує транзакції.
# ● При вході в контекст створюється копія списку.
# ● Якщо вихід відбувається без помилок, зміни зберігаються.
# ● Якщо виникає виняток, список повертається до попереднього стану.
class TransactionalList:
    def __init__(self, initial_list=None):
        self.data = initial_list or []

    def __enter__(self):
        self._backup = self.data[:]  # Робимо копію списку
        return self

    def append(self, item):
        self.data.append(item)

    def remove(self, item):
        self.data.remove(item)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.data = self._backup  # Відкат до початкового стану
            print("Зміни відхилені через помилку!")
        else:
            print("Зміни підтверджені.")


# Приклад використання:
my_list = TransactionalList([1, 2, 3])
try:
    with my_list as lst:
        lst.append(4)
        lst.append(5)
        print("Усередині контексту:", lst.data)
        raise ValueError("Щось пішло не так!")  # Симулюємо помилку
except ValueError:
    pass
print("Поза контекстом:", my_list.data)  # Має залишитися [1, 2, 3]
