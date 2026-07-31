# staticmethod()
# classmethod(cls)
# instance method(self)

class DecoratorTest:
    class_counter = 0

    def doubler(self, x):
        print(f'Instance method. self = {self}')
        return x * 2

    @classmethod
    def triples(cls, x):
        print(f'Class method. cls = {cls}')
        cls.class_counter += 1
        return x * 3

    @staticmethod
    def quad(x):
        print(f'Static method. x = {x}')
        return x * 4

# Виклик через екземпляр класу
decor = DecoratorTest()
print(decor.doubler(4))
print(decor.triples(5))
print(decor.quad(6))

# Виклик через клас
# print(DecoratorTest.doubler(4))
print(DecoratorTest.triples(5))
print(DecoratorTest.quad(6))
print(DecoratorTest.class_counter)