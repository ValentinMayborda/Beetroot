from random import randint

class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        return randint(self.start, self.end)

    def __repr__(self):
        return f'RandIterator({self.start}, {self.end}, {self.quantity})'

rand_it = RandIterator(1, 20, 5)
for num in rand_it:
    print(num, end=' ')

print()
rand_it2 = RandIterator(1, 100, 3)
print(next(rand_it2))
print(next(rand_it2))
print(next(rand_it2))
# print(next(rand_it2))

numbers = list(RandIterator(1, 100, 10))
print(numbers)
temp = RandIterator(1, 10, 3)
print(list(temp))
temp = RandIterator(1, 10, 3)
print(list(temp))  # [next(temp) + next(temp) + next(temp)]
# print(next(temp))
print(temp.count)