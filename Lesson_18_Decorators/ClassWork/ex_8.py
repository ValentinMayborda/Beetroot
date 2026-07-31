class BoundedAttribute:
    def __init__(self, min_val=0, max_value=100):
        self.min_val = min_val
        self.max_value = max_value
        self.storage_name = f"_{id(self)}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, self.min_val)

    def __set__(self, instance, value):
        if value < self.min_val:
            value = self.min_val
        elif value > self.max_value:
            value = self.max_value
        setattr(instance, self.storage_name, value)


class Character:
    health = BoundedAttribute(min_val=0, max_value=100)
    mana = BoundedAttribute(min_val=0, max_value=50)


hero = Character()
hero.health = 150
hero.mana = -30

print(hero.health)
print(hero.mana)