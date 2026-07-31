class Student:
    # grades = []

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    
a = Student('Vadym')
b = Student('Ivan')
a.add_grade(10)
print(b.grades)
