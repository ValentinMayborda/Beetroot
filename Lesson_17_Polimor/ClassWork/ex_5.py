# HAS-A (Агрегація)
class Owner:
    def __init__(self, name: str, phone: str, pets_count: int = 0) -> None:
        self.name = name
        self.phone = phone
        self.pets_count = pets_count

    def info(self) -> str:
        return f"Owner: {self.name}, {self.phone}. Pets: {self.pets_count}"

    def update_phone(self, new_phone: str) -> None:
        self.phone = new_phone

    def add_pet(self) -> None:
        self.pets_count += 1

    def remove_pet(self) -> None:
        if self.pets_count > 0:
            self.pets_count -= 1


class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner) -> None:
        self.nickname = nickname
        self.age = age
        # Агрегація Owner - передається ззовні
        self.owner = owner
        self.owner.add_pet()
        self.lives = 9

    def get_info(self) -> str:
        return f"Cat: {self.nickname}, {self.age} years old, lives: {self.lives}"


owner = Owner('Volodymyr', '+3809123456788')
cat1 = Cat('Tom', 2, owner)
cat2 = Cat('Jerry', 3, owner)

print(cat1.get_info())
print(owner.info())