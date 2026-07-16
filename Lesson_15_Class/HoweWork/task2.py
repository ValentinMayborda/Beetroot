"""Вік собаки в людських роках

Створіть клас Dog з атрибутом класу:

age_factor = 7

Реалізуйте метод __init__(), який приймає вік собаки.

Потім створіть метод human_age(), який повертає еквівалентний вік собаки в людських роках."""

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor

dog = Dog(8)
print(dog.human_age())