"""Школа
Створіть у Python структуру класів, яка представляє людей у школі.
Створіть:

базовий клас Person;
клас Student;
клас Teacher.

Спробуйте визначити якомога більше методів і атрибутів, які належать різним класам, враховуючи, які з них є спільними, а які — специфічними.

Наприклад:

ім'я (name) повинно бути атрибутом класу Person;
зарплата (salary) повинна бути доступною лише для класу Teacher."""

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def to_learn(self):
        print(f' I am {self.name}, and I am in {self.group} group.')


class Teacher(Person):
    def __init__(self, name, salary, subject):
        super().__init__(name)
        self.salary = salary
        self.subject = subject

    def to_teach(self):
        print(f' I am {self.name}, and I am  {self.subject} teacher.')

student = Student('Valentyn', 'Python')
teacher = Teacher('Volodymir', 30000, 'Programming')

student.to_learn()
teacher.to_teach()