# HAS-A (Композиція)
class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self) -> str:
        return f"Owner: {self.name}, {self.phone}"

    def update_phone(self, new_phone: str) -> None:
        self.phone = new_phone


class Cat:
    def __init__(self, name: str, age: int, owner_name: str, owner_phone: str):
        self.name = name
        self.age = age
        # Композиція - Owner створюється в середині Cat
        self.owner = Owner(owner_name, owner_phone)
        self.lives = 9

    def get_info(self) -> str:
        return f"Cat: {self.name}, {self.age} years old, lives: {self.lives}"


cat = Cat('Tom', 2, 'Volodymyr', '+3809123456788')
print(cat.get_info())
print(cat.owner.info())
