# namespace
# bult-in - print(), len(), int()
# global - на рівні модуля
# local - на рівні функції
class Dog:
    special = 'German'
    def __init__(self, name):  # конструктор
        self.name = name

d = Dog('Rex')
print(d.__dict__)  # простір імен екземпляра класу
print(Dog.__dict__.keys())   # простір імен класу