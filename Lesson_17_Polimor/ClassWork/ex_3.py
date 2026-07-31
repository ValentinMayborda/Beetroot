class Duck:
    def quack(self) -> str:
        return "Quack!"


class Person:
    def quack(self) -> str:
        return "Я людина але добре імітую крякання"


def make_it_quack(something) -> str:
    return something.quack()

duck = Duck()
person = Person()
print(make_it_quack(duck))
print(make_it_quack(person))