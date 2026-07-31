class Employee:
    emp_count = 0  # АТРИБУТ КЛАСУ - спільний для всіх екземплярів класу

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1  # звертаємось через імя класу


    def display(self):
        print(f"Імя: {self.name}. Зарплата: {self.salary}")


emp1 = Employee('Іван', 60000)
emp2 = Employee('Марія', 75000)

emp1.display()
emp2.display()

print(f"Всього співробітників: {Employee.emp_count}")
emp3 = Employee('Петро', 70000)
print(f"Всього співробітників: {Employee.emp_count}")
print(emp1.emp_count)
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)
# print(emp2.emp_count)
# print(emp3.emp_count)


