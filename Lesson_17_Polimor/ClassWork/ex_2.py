class Dog:
    def sound(self) -> str:
        return "Woof!"


class Cat:
    def sound(self) -> str:
        return "Meow!"

class Robot:
    def sound(self) -> str:
        return "Beep!"


def make_sound(things) -> str:
    for thing in things:
        print(thing.sound())


make_sound([Dog(), Cat(), Robot()])