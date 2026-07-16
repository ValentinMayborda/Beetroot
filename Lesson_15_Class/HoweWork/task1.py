"""Створіть клас Person.

Метод __init__() повинен приймати параметри:

firstname (ім'я),
lastname (прізвище),
age (вік),

і зберігати їх як атрибути об'єкта.

Також створіть метод talk(), який виводить привітання від особи, наприклад:

"Hello, my name is Carl Johnson and I’m 26 years old"""

class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')

person = Person('Valentyn', 'Maiboroda', 36)

person.talk()