"""Створи базовий клас з назвою Animal, який має метод talk.

Потім створи два підкласи: Dog і Cat, і реалізуй у них власну версію методу talk, яка буде відрізнятися.

Наприклад:
Dog має виводити: "woof woof"
Cat має виводити: "meow"

Також створи просту універсальну функцію, яка приймає об’єкт типу Cat або Dog і викликає в нього метод talk()."""

class Animal:
    def __init__(self, nickname):
        self.nickname = nickname

    def talk(self):
       print('Базовий метод talk')


class Dog(Animal):
    def __init__(self, nickname):
        super().__init__(nickname)

    def talk(self):
        print('woof woof')


class Cat(Animal):
    def __init__(self, nickname):
        super().__init__(nickname)

    def talk(self):
        print('meow')


def universal_talk(animal_obj):
    animal_obj.talk()

cat = Cat('Jhon')
dog = Dog('Rex')
universal_talk(cat)
universal_talk(dog)


animals = [Dog('Рекс'), Dog('Спот'), Cat('Шані'), Cat('Роксі')]
for animal in animals:
    universal_talk(animal)