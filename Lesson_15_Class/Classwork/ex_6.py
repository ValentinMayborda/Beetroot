class Employee:
   """Базовий клас для всіх працівників"""
   emp_count = 0

   def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       Employee.emp_count += 1  # показати цей параметр через self. Нам потрібно звертатись через атрибут класу

   def display_count(self):
       print('Усього співробітників: %d' % Employee.emp_count)

   def display_employee(self):
       print('Ім"я: {}. Зарплата: {}'.format(self.name, self.salary))


# Це створить перший об'єкт класу Employee
emp1 = Employee("Андрій", 2000)
# Це створить другий об'єкт класу Employee
emp2 = Employee("Марія", 5000)
emp1.display_employee()
emp2.display_employee()
print("Усього співробітників: %d" % Employee.emp_count)

