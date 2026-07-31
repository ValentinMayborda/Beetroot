class BadRange:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i
r = BadRange(3)
print(list(r))
print(list(r))

class CountIterator:  # iterator
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i

class Counter:   # iterable
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return CountIterator(self.n)

c = Counter(3)
print(list(c))
print(list(c))
print(list(c))

