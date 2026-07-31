class Dog:
    def __init__(self, name, age):  # конструктор
        # ініціалізація атрибувтів name, age
        self.name = name   # атрибут екземпляра
        self.age = age

    def sit(self):
        print(f"{self.name.title()} сідає")

    def roll_over(self):
        print(f"{self.name.title()} перекочується")


my_dog = Dog('Rex', 3)  # Dog.__init__ з аргументами 'Rex' і 3
your_dog = Dog('jessie', 5)
print(f'My dog name is: {my_dog.name.title()}')
print(f'My dog age is: {my_dog.age}')
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
print(f'My dog name is: {your_dog.name}')
your_dog.roll_over()
