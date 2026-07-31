# public        -> self.name
# protected     -> self._name
# private       -> self.__name

class Person:
    def __init__(self, name, age, ssn):
        self.name = name  # public - можна читати або писати звідусіль
        self._age = age   # protected - тільки для класу і нащадків
        self.__ssn = ssn  # private - тільки всередині цього класу

    def get_ssn_last_4(self):
        return f"*******{self.__ssn[-4:]}"

    def _validate_age(self):
        return 0 <= self._age <= 120


p = Person("John", 30, '123456789')
print(p.name)
print(p._age)
# print(p.__ssn)
# print(p._Person__ssn)
print(p.get_ssn_last_4())
print(p._validate_age())