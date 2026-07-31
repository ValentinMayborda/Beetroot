class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"Nickname is {self.nickname} and {self.age} years old."


class Cat(Animal):
    def __init__(self, nickname, age, owner):
        super().__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return f"{self.nickname} says: Meow"

    def get_info(self):
        return 'This is a cat.'




cat = Cat("Barsik", 3, "John")
print(cat.sound())
print(cat.get_info())
print(cat.nickname)
print(cat.age)