class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"Animal: {self.nickname}, {self.age} years old"


class Cat(Animal):
    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def get_info(self) -> str:
        return f"Cat: {self.nickname}, {self.age} years old"

    def sound(self) -> str:
        return "Meow!"


class Dog(Animal):
    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def get_info(self) -> str:
        return f"Dog: {self.nickname}, {self.age} years old"

    def sound(self) -> str:
        return "Woof!"

cat = Cat("Tom", 3, "John")
dog = Dog("Max", 5, "Alice")


print(isinstance(dog, Animal))  # True <- IS-A Animal
print(isinstance(dog, Cat))     # False
print(isinstance(dog, Dog))     # True

print(type(dog) is Dog)
print(type(dog) is Animal)

for animal in [cat, dog]:
    print(animal.get_info())

for animal in [cat, dog]:
    print(animal.sound())