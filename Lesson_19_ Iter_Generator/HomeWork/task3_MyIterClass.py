"""
Створіть власний ітерований клас, який можна використовувати у циклі

Також потрібно реалізувати можливість отримувати елементи через квадратні дужки

"""

class MyIterClass:

    def __init__(self, iterable):
        self.data = iterable
        self.index = 0

    def __iter__(self):
        self.index = 0 # рестарт ітератора
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        return_value = self.data[self.index]
        self.index += 1
        return return_value

    def __getitem__(self, item):
        return self.data[item]


my = MyIterClass([10, 20, 30])

for i in my:
    print(i)

for i in my:
    print(i)

print(my[0], my[1], my[2])
