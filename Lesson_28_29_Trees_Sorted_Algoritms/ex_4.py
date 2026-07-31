class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.reports_to = None
        self.subordinates = []

    def add_report(self, employee):
        employee.reports_to = self
        self.subordinates.append(employee)

    def total_team_salary(self):
        total = self.salary
        for sub in self.subordinates:
            total += sub.total_team_salary()
        return total

    def team_size(self):
        count = 1
        for sub in self.subordinates:
            count += sub.team_size()
        return count

    def display(self, indent=0):
        print(" " * indent + f"{self.name} ({self.role})")
        for sub in self.subordinates:
            sub.display(indent + 2)


ceo = Employee('Олена', 'CEO', 100000)
cto = Employee('Олександр', 'CTO', 80000)
cfo = Employee('Ольга', 'CFO', 70000)

lead = Employee('Олександр', 'Tech Lead', 60000)
dev1 = Employee('Марія', 'Senior Developer', 50000)
dev2 = Employee('Катерина', 'Junior Developer', 25000)
ceo.add_report(cto)
ceo.add_report(cfo)
cto.add_report(lead)
lead.add_report(dev1)
lead.add_report(dev2)

ceo.display()
print(f"Total company salary: {ceo.total_team_salary()}")
print(f"Company team size: {ceo.team_size()}")
print(f"Devs team size: {cto.team_size()}")
print(f"Total team salary: {cto.total_team_salary()}")