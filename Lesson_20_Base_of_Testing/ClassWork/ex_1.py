class Animal:
    def __init__(self, nickname, age, weight):
        self.__nickname = None
        self.__age = None
        self.__weight = None

        self.name = nickname
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Name can't be empty")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Вага не може бути меншою за нуль")


class Turtle(Animal):
    def __init__(self, nickname, age, weight):
        super().__init__(nickname, age, weight)

    @Animal.age.setter
    def age(self, age):
        if age in list(range(0, 150)):
            Animal.age.fset(self, age)
        else:
            raise ValueError("Тварини стільки не живуть")


class Dog(Animal):
    def __init__(self, nickname, age, weight):
        super().__init__(nickname, age, weight)


animal = Animal("Bobik", 5, 10)
print(animal.name, animal.age, animal.weight)
# dog.age = -100
#
turtle = Turtle('Tortilla', 149, 100)
print(turtle.name, turtle.age, turtle.weight)

# dog = Dog('Rex', 199, 100)
# print(dog.name, dog.age, dog.weight)